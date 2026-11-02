#!/usr/bin/env python3
"""Independent direct triple-loop check of orthogonal-array fault spectra."""
from itertools import product

def counts(q,t):
    pts=list(product(range(q),repeat=2))
    def ar(p):
        x,y=p
        return tuple([x,y]+[(x+s*y)%q for s in range(1,t-1)])
    data=[ar(z) for z in pts]
    assert all(len({(v[i],v[j]) for v in data})==q*q
               for i in range(t) for j in range(i))
    N=len(pts)
    vals={}
    for a in range(N):
        for b in range(a+1,N):
            an=sum(data[a][i]==data[b][i] for i in range(t))==1
            table={(x,y):0 for x,y in product((0,1), repeat=2)}
            for z in range(N):
                if z==a or z==b:continue
                za=int(any(data[a][i]==data[z][i] for i in range(t)))
                zb=int(any(data[b][i]==data[z][i] for i in range(t)))
                table[za,zb]+=1
            key=int(an)
            for pat,num in table.items():
                if (key,pat) in vals:assert vals[key,pat]==num,(q,t,key,pat)
                vals[key,pat]=num
    return vals

def expected(q,t):
    k=t*(q-1); la=q-2+(t-1)*(t-2); mu=t*(t-1)
    return {
      (1,(1,1)):la,(1,(1,0)):k-la-1,(1,(0,1)):k-la-1,(1,(0,0)):q*q-2*k+la,
      (0,(1,1)):mu,(0,(1,0)):k-mu,(0,(0,1)):k-mu,(0,(0,0)):q*q-2-2*k+mu
    }

if __name__=='__main__':
    # Independent modular prime-field implementation; does not import other checker.
    for q in (3,5,7,11):
        for t in range(2,q):
            a=counts(q,t); b=expected(q,t)
            assert a==b,(q,t,a,b)
        print('prime order',q,'all t and ordered-pair patterns PASS')
    # At optimal t, verify the first deletion can destroy the extension property.
    for q in (5,7,11):
        t=(q+1)//2; pts=list(product(range(q),repeat=2))
        co=lambda z:tuple([z[0],z[1]]+[(z[0]+s*z[1])%q for s in range(1,t-1)])
        data=[co(z) for z in pts]
        N=len(data)
        def adj(a,b):return a!=b and bool(set(enumerate(data[a]))&set(enumerate(data[b])))
        best=10**9; choice=None
        for a in range(N):
            for b in range(a+1,N):
                for p in product((0,1),repeat=2):
                    w=tuple(z for z in range(N) if z not in (a,b) and (int(adj(a,z)),int(adj(b,z)))==p)
                    if len(w)<best:best=len(w);choice=(a,b,p,w)
        a,b,p,w=choice
        assert not any((int(adj(a,z)),int(adj(b,z)))==p for z in range(N) if z not in (a,b) and z not in w)
        print('prime order',q,'optimal t',t,'sharp failure deletion count',best,'PASS')
    print('INDEPENDENT RESULT PASS')
