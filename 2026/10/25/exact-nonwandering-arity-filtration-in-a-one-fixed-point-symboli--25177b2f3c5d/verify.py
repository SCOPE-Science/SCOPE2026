"""Exact combinatorial and finite-window checks for symmetric-product arity thresholds."""
from itertools import product

def pred(a,b,c,p):
    if not p:
        return None if c or not a or not b else 2*max(a,b)
    return 2*c+2*max(a,b)+(1 if c==0 and a==b else 0)

def vertices(a,b,c,p):
    return (['p'] if p else [])+[f'x{i}' for i in range(a)]+[f'y{i}' for i in range(b)]+[f'z{i}' for i in range(c)]

def arcs(v):
    e=[]
    for u in v:
      for w in v:
        allowed=(u=='p' or (u.startswith('x') and (w=='p' or w.startswith('y'))) or (u.startswith('y') and (w=='p' or w.startswith('x'))) or (u.startswith('z') and w=='p'))
        if allowed:
            e.append((u,w))
    return e

def dp_min_arrows(a,b,c,p):
    v=vertices(a,b,c,p); m=len(v); ix={u:i for i,u in enumerate(v)}
    dp={0:0}
    for u,w in arcs(v):
        mask=(1<<ix[u]) | (1<<(m+ix[w]))
        prev=list(dp.items())
        for state,cost in prev:
            new=state|mask
            if dp.get(new,10**9)>cost+1: dp[new]=cost+1
    return dp.get((1<<(2*m))-1)

def witness_edges(a,b,c,p):
    xs=[f'x{i}' for i in range(a)]
    ys=[f'y{i}' for i in range(b)]
    zs=[f'z{i}' for i in range(c)]
    E=[]
    if not p:
        assert not c and a and b
        for i in range(max(a,b)):
            E.append((xs[i%a],ys[i%b]))
            E.append((ys[i%b],xs[i%a]))
        return E
    for z in zs:E.extend([('p',z),(z,'p')])
    for i in range(min(a,b)):
        E.extend([(xs[i],ys[i]),(ys[i],xs[i])])
    for i in range(min(a,b),a):E.extend([(xs[i],'p'),('p',xs[i])])
    for i in range(min(a,b),b):E.extend([(ys[i],'p'),('p',ys[i])])
    if c==0 and a==b: E.append(('p','p'))
    return E

def transition_label(u):
    if u=='p':return 'p'
    return u[0]

def rep_edge(u,v,N):
    """A shift-compatible model: X[r],Y[r],Z[start,end],W[start,end],P.
    x_i step 0->1 at 5i, y_j step 1->0 at 5j,
    finite z_i is 1 on [5i,5i+2), separated from other types by type.
    """
    def pos(s):return 5*int(s[1:])
    if u=='p' and v=='p':return ('P',)
    if u=='p':
        if v[0]=='x':return ('X',N+pos(v))
        if v[0]=='y':return ('Y',N+pos(v))
        if v[0]=='z':return ('Z',N+pos(v),N+pos(v)+2)
    if v=='p':
        if u[0]=='x':return ('X',pos(u))
        if u[0]=='y':return ('Y',pos(u))
        if u[0]=='z':return ('Z',pos(u),pos(u)+2)
    if u[0]=='x' and v[0]=='y': return ('Z',pos(u),N+pos(v))
    if u[0]=='y' and v[0]=='x': return ('W',pos(u),N+pos(v))
    raise ValueError((u,v))

def shifted(rep,N):
    return (rep[0],)+tuple(x-N for x in rep[1:])

def word(rep,R):
    typ=rep[0]
    if typ=='P':return 'p'
    seq=[]
    for k in range(-R,R+1):
        if typ=='X':z=int(k>=rep[1])
        elif typ=='Y':z=int(k<rep[1])
        elif typ=='Z':z=int(rep[1]<=k<rep[2])
        elif typ=='W':z=int(not(rep[1]<=k<rep[2]))
        seq.append(str(z))
    return ''.join(seq)

def matches(rep,u,R):
    w=word(rep,R)
    if u=='p':return w=='p' or len(set(w))==1
    if u[0]=='x':return w==word(('X',5*int(u[1:])),R)
    if u[0]=='y':return w==word(('Y',5*int(u[1:])),R)
    if u[0]=='z':return w==word(('Z',5*int(u[1:]),5*int(u[1:])+2),R)
    return False

def main():
    count=0
    for p,a,b,c in product((False,True),range(3),range(3),range(3)):
        if not p and not (a+b+c):continue
        m=pred(a,b,c,p); got=dp_min_arrows(a,b,c,p)
        assert got==m,(a,b,c,p,m,got)
        if m is not None:
            E=witness_edges(a,b,c,p)
            assert len(E)==m
            v=set(vertices(a,b,c,p))
            assert set(u for u,w in E)==v
            assert set(w for u,w in E)==v
            R=12; N=200
            reps=[rep_edge(u,w,N) for u,w in E]
            assert len(reps)==len(set(reps)), (a,b,c,p,E,reps)
            ends=[shifted(r,N) for r in reps]
            assert len(ends)==len(set(ends)),(a,b,c,p,E,ends)
            for (u,w),rep,end in zip(E,reps,ends):
                assert matches(rep,u,R),('source',u,w,rep,word(rep,R))
                assert matches(end,w,R),('target',u,w,end,word(end,R))
        count+=1
    print(f'VERIFY_OK: {count} exact minimal edge-cover tests and finite-window orbit witnesses')

if __name__=='__main__':main()
