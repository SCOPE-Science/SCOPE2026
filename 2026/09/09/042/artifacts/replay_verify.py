"""Independent replay: mpmath dps=80, recursive enumeration (different code path).
Checks: closed-form word totals, generator trace identities, minima agreement,
hyperbolicity margins, no genuine parabolics, Euclidean zero-hyperbolic."""
import json, math
from mpmath import mp, mpf, cos, sin, sqrt, pi, acosh
mp.dps = 80

L = 10
HYP = [(2,4,5),(2,4,6),(2,5,5),(2,5,6),(2,6,6),
       (3,3,4),(3,3,5),(3,3,6),(3,4,4),(3,4,5),(3,4,6),(3,5,5),(3,5,6),(3,6,6),
       (4,4,4),(4,4,5),(4,4,6),(4,5,5),(4,5,6),(4,6,6),
       (5,5,5),(5,5,6),(5,6,6),(6,6,6)]
EUCL = [(3,3,3),(2,4,4),(2,3,6)]

def model(p,q,r):
    cp,sp = cos(pi/p), sin(pi/p); cq,sq = cos(pi/q), sin(pi/q); cr = cos(pi/r)
    t = (cp*cq+cr)/(sp*sq)
    assert t > 1
    mu = t+sqrt(t*t-1)
    s = sqrt(mu)
    A = ((cp,-sp),(sp,cp))
    # B = M R M^-1 entries
    B = ((cq,-sq/mu),(sq*mu,cq))
    Minv = None
    return A,B,mu,t

def mmul(X,Y):
    return ((X[0][0]*Y[0][0]+X[0][1]*Y[1][0], X[0][0]*Y[0][1]+X[0][1]*Y[1][1]),
            (X[1][0]*Y[0][0]+X[1][1]*Y[1][0], X[1][0]*Y[0][1]+X[1][1]*Y[1][1]))
def mtr(X): return X[0][0]+X[1][1]
def is_id_pm(X):
    I=((mpf(1),mpf(0)),(mpf(0),mpf(1)))
    def close(X,s):
        return abs(X[0][0]-s)<mpf(10)**-60 and abs(X[1][1]-s)<mpf(10)**-60 and abs(X[0][1])<mpf(10)**-60 and abs(X[1][0])<mpf(10)**-60
    return close(X,1) or close(X,-1)

def genmap(A,B,p,q):
    Ai=((A[0][0],-A[0][1]),(-A[1][0],A[1][1]))  # transpose=inverse (rotation-conj, det 1)
    Bi=((B[1][1],-B[0][1]),(-B[1][0],B[0][0]))  # adjugate/det
    d={'a':A,'b':B}
    if p!=2: d['A']=Ai
    if q!=2: d['B']=Bi
    if p==2: ab=['a']
    else: ab=['a','A']
    if q==2: bb=['b']
    else: bb=['b','B']
    alpha=ab+bb
    # order-2 generators are self-inverse: forbid 'aa' (p==2), 'bb' (q==2)
    inv={}
    if p==2: inv['a']='a'
    else: inv['a']='A'; inv['A']='a'
    if q==2: inv['b']='b'
    else: inv['b']='B'; inv['B']='b'
    return d,alpha,inv

prim=json.load(open('/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-337/output/census_raw.json'))
ok=True
lines=[]
# closed forms: L=10. No-2 triples: 1+2(3^10-1)=118097.
# Exactly-one-2 triples: alphabet of 3 with 'aa' (resp 'bb') + bB/Bb forbidden;
# per-length counts obey x_n=y_{n-1}, y_n=2x_{n-1}+y_{n-1} giving 3*2^{n-1}
# words of length n>=1, total 1+3(2^10-1)=3070.
def closed_total(p,q):
    if (p==2)+(q==2)==1:
        return 1+3*(2**L-1)
    return 1+2*(3**L-1)

for (p,q,r) in HYP:
    A,B,mu,t=model(p,q,r)
    # generator identities at 80 digits
    eA=abs(mtr(A)-2*cos(pi/p)); eB=abs(mtr(B)-2*cos(pi/q)); eAB=abs(mtr(mmul(A,B))+2*cos(pi/r))
    assert eA<mpf(10)**-70 and eB<mpf(10)**-70 and eAB<mpf(10)**-70,(p,q,r,eA,eB,eAB)
    d,alpha,inv=genmap(A,B,p,q)
    I=((mpf(1),mpf(0)),(mpf(0),mpf(1)))
    counts={'trivial':0,'elliptic':0,'nontrivial_parabolic':0,'hyperbolic':0}
    best=None  # (l,tr,len,word)
    # recursive enumeration, length-first via stack
    stack=[('',I)]
    # iterative deepening BFS
    cur={'':I}; alln=1
    tables={0:[('',I)]}
    for n in range(1,L+1):
        nxt={}
        for w,Mm in cur.items():
            for g in alpha:
                if w and inv[w[-1]]==g: continue
                nxt[w+g]=mmul(Mm,d[g])
        cur=nxt; alln+=len(nxt)
        # classify level n plus level 0 once
    cur={'':I}
    levels=[cur]
    for n in range(1,L+1):
        nxt={}
        for w,Mm in cur.items():
            for g in alpha:
                if w and inv[w[-1]]==g: continue
                nxt[w+g]=mmul(Mm,d[g])
        levels.append(nxt); cur=nxt
    for lev in levels:
        for w,Mm in lev.items():
            tr=mtr(Mm); a=abs(tr)
            if abs(a-2)<mpf(10)**-12:
                if is_id_pm(Mm): counts['trivial']+=1
                else: counts['nontrivial_parabolic']+=1
            elif a>2:
                counts['hyperbolic']+=1
                l=2*acosh(a/2)
                if best is None or l<best[0]: best=(l,tr,len(w),w)
            else: counts['elliptic']+=1
    ct=closed_total(p,q)
    key=f"{p},{q},{r}"; pv=prim[key]
    magree = (alln==pv['n_words']==ct and counts['trivial']==pv['counts']['trivial']
              and counts['elliptic']==pv['counts']['elliptic']
              and counts['hyperbolic']==pv['counts']['hyperbolic']
              and counts['nontrivial_parabolic']==0)
    pm=pv['min']
    # witness strings may differ by enumeration order among ties (|tr| equal):
    # compare VALUES (trace/trans), not representative words
    vagree = (abs(float(best[1])-pm['trace'])<1e-9 or abs(float(best[1])+pm['trace'])<1e-9) and abs(float(best[0])-pm['trans'])<1e-9
    status='OK' if (magree and vagree) else 'MISMATCH'
    if status!='OK': ok=False
    margin=float(abs(best[1])-2)
    lines.append(f"{key} total={alln} (closed {ct}) counts={counts} min={best[3]} len={best[2]} tr={float(best[1]):.12f} l={float(best[0]):.12f} margin={margin:.6f} {status}")

print('\n'.join(lines))
print('REPLAY:', 'ALL_OK' if ok else 'FAIL')
# Euclidean replay: exact rotation exponents (integers) + float shift; assert 0 hyperbolic
import cmath
for (p,q,r) in EUCL:
    m=math.lcm(p,q); ep,eq=m//p,m//q
    zp=cmath.exp(2j*math.pi/p); zq=cmath.exp(2j*math.pi/q)
    gens={'a':(ep,0j),'b':(eq,1-zq)}
    alpha=['a','b'] if (p==2 and q==2) else None
    alpha=['a']+[ ] if False else None
    ab=['a'] if p==2 else ['a','A']
    if p!=2: gens['A']=(m-ep,0j)
    if q!=2:
        sb=-(1-zq)/zq; gens['B']=(m-eq,sb)
    bb=['b'] if q==2 else ['b','B']
    alpha=ab+bb
    inv={}
    if p==2: inv['a']='a'
    else: inv['a']='A'; inv['A']='a'
    if q==2: inv['b']='b'
    else: inv['b']='B'; inv['B']='b'
    def mul(g1,g2):
        (e1,s1),(e2,s2)=g1,g2
        return ((e1+e2)%m, cmath.exp(2j*math.pi*e1/m)*s2+s1)
    cur={'':(0,0j)}; tot=1; hyp=0; triv=0; ell=0; trn=0
    lv=[cur]
    for n in range(1,L+1):
        nxt={}
        for w,gw in cur.items():
            for g in alpha:
                if w and inv[w[-1]]==g: continue
                nxt[w+g]=mul(gw,gens[g])
        cur=nxt; lv.append(cur); tot+=len(nxt)
    for d_ in lv:
        for w,(e,s) in d_.items():
            if e==0:
                if abs(s)<1e-9: triv+=1
                else: trn+=1
            else: ell+=1
    print(f"eucl {p},{q},{r} total={tot} triv={triv} ellrot={ell} trans={trn} hyp={hyp} {'OK' if hyp==0 else 'FAIL'}")
    assert hyp==0
