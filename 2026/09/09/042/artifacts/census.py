"""Primary census: Fuchsian models of D(p,q,r), reduced words to L=10.
Deterministic enumeration order; float64 traces; JSON summary out."""
import numpy as np, json, math, hashlib

L = 10
HYP = [(2,4,5),(2,4,6),(2,5,5),(2,5,6),(2,6,6),
       (3,3,4),(3,3,5),(3,3,6),(3,4,4),(3,4,5),(3,4,6),(3,5,5),(3,5,6),(3,6,6),
       (4,4,4),(4,4,5),(4,4,6),(4,5,5),(4,5,6),(4,6,6),
       (5,5,5),(5,5,6),(5,6,6),(6,6,6)]
EUCL = [(3,3,3),(2,4,4),(2,3,6)]
TOL = 1e-9

def mats(p,q,r):
    cp,sp = math.cos(math.pi/p), math.sin(math.pi/p)
    cq,sq = math.cos(math.pi/q), math.sin(math.pi/q)
    cr = math.cos(math.pi/r)
    t = (cp*cq+cr)/(sp*sq)
    assert t > 1.0, (p,q,r,t)
    mu = t+math.sqrt(t*t-1)
    A = np.array([[cp,-sp],[sp,cp]])
    R = np.array([[cq,-sq],[sq,cq]])
    M = np.diag([math.sqrt(mu),1.0/math.sqrt(mu)])
    B = M@R@np.linalg.inv(M)
    return A,B,mu,t

def gens(A,B,p,q):
    d = {'a':A}
    if p==2: al=['a']
    else: d['A']=np.linalg.inv(A); al=['a','A']
    d['b']=B
    if q==2: bl=['b']
    else: d['B']=np.linalg.inv(B); bl=['b','B']
    # order-2 generators are self-inverse: forbid 'aa' (p==2), 'bb' (q==2)
    inv={}
    if p==2: inv['a']='a'
    else: inv['a']='A'; inv['A']='a'
    if q==2: inv['b']='b'
    else: inv['b']='B'; inv['B']='b'
    return d,al+bl,inv

def enumerate_words(p,q,r,L):
    A,B,mu,t = mats(p,q,r)
    d,alpha,inv = gens(A,B,p,q)
    I=np.eye(2)
    cur={ '' : I }; allw={ '' : I }
    for n in range(1,L+1):
        nxt={}
        for w,Mm in cur.items():
            last=w[-1] if w else None
            for g in alpha:
                if last is not None and inv[last]==g: continue
                nxt[w+g]=Mm@d[g]
        cur=nxt; allw.update(cur)
    return allw,A,B,mu,t

def classify(tr):
    a=abs(tr)
    if abs(a-2.0)<=TOL: return 'parabolic_or_trivial'
    return 'hyperbolic' if a>2.0 else 'elliptic'

def is_trivial(Mm):
    I=np.eye(2)
    return np.allclose(Mm,I,atol=1e-8) or np.allclose(Mm,-I,atol=1e-8)

def tl(tr):
    return 2.0*math.acosh(abs(tr)/2.0)

out={}
for (p,q,r) in HYP:
    allw,A,B,mu,t = enumerate_words(p,q,r,L)
    n=len(allw)
    counts={'trivial':0,'elliptic':0,'parabolic_or_trivial':0,'hyperbolic':0}
    # generator sanity
    trA=np.trace(np.linalg.matrix_power(A,p if p<=6 else 1))
    hyp_list=[]
    for w,Mm in allw.items():
        tr=float(np.trace(Mm))
        c=classify(tr)
        if c=='parabolic_or_trivial':
            if is_trivial(Mm): counts['trivial']+=1
            else: counts['parabolic_or_trivial']+=1
        elif c=='hyperbolic':
            counts['hyperbolic']+=1
            hyp_list.append((tl(tr),tr,len(w),w))
        else: counts['elliptic']+=1
    hyp_list.sort()
    top=hyp_list[:10]
    # checks
    assert counts['parabolic_or_trivial']==0,(p,q,r,'unexpected parabolic')
    out[f"{p},{q},{r}"]={'n_words':n,'mu':mu,'t':t,
        'trA':float(np.trace(A)),'trB':float(np.trace(B)),'trAB':float(np.trace(A@B)),
        'trA_exact':2*math.cos(math.pi/p),'trB_exact':2*math.cos(math.pi/q),
        'trAB_exact':-2*math.cos(math.pi/r),
        'counts':counts,
        'min':{'word':top[0][3],'len':top[0][2],'trace':top[0][1],'trans':top[0][0]} if top else None,
        'top10':[{'word':w,'len':k,'trace':tr,'trans':l} for (l,tr,k,w) in top]}

json.dump(out,open('/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-337/output/census_raw.json','w'),indent=1)
for k,v in out.items():
    m=v['min']
    print(k,'n=',v['n_words'],v['counts'],'MIN',m['word'],'len',m['len'],'tr=%.9f'%m['trace'],'l=%.9f'%m['trans'])
print('margin above 2 of minima:', min(v['min']['trace'] for v in out.values() if v['min']['trace']>0),
      min(abs(v['min']['trace'])-2 for v in out.values()))
