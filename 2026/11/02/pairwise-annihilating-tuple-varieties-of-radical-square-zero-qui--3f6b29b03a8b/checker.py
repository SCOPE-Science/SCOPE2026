"""Verify pairwise annihilating tuples in radical-square-zero path algebras."""
import itertools

class F:
    def __init__(self, q):
        self.q=q
        self.add=lambda a,b:(a+b)%q
        self.mul=lambda a,b:(a*b)%q
        if q==4:
            self.add=lambda a,b:a^b
            def mul(a,b):
                acc=0
                for i in range(2):
                    if (b>>i)&1: acc^=a<<i
                if (acc>>3)&1: acc^=0b1100 # x^3 = x^2+x
                if (acc>>2)&1: acc^=0b111  # x^2 = x+1
                return acc
            self.mul=mul

def pairzero(t, n, edges, f):
    for i in range(len(t)):
        for j in range(len(t)):
            if i==j:continue
            a,b=t[i],t[j]
            for v in range(n):
                if f.mul(a[v],b[v]):return False
            for h,(s,d) in enumerate(edges):
                if f.add(f.mul(a[s], b[n+h]), f.mul(a[n+h], b[d])):return False
    return True

def formula(q,n,edges,m):
    E=len(edges)
    result=0
    for mask in range(1<<n):
        S={v for v in range(n) if mask>>v&1}
        result+=(m*(q-1))**(n-len(S))*q**(E+(m-1)*sum(int(s in S and t in S) for s,t in edges))
    return result

def exhaustive(q,n,edges,m):
    f=F(q)
    els=list(itertools.product(range(q), repeat=n+len(edges)))
    if len(els)**m>400000:raise ValueError('too many tuples')
    actual=sum(pairzero(t,n,edges,f) for t in itertools.product(els,repeat=m))
    expected=formula(q,n,edges,m)
    assert actual==expected,(q,n,edges,m,actual,expected)
    return actual

cases=[
(2,1,[],1),(2,1,[],3),(2,1,[(0,0)],2),(2,1,[(0,0)],3),
(2,2,[(0,1)],2),(2,2,[(0,1)],3),(2,2,[(0,1)],4),
(2,2,[(0,1),(0,1)],2),(2,2,[(0,1),(1,0)],2),
(2,3,[(0,1),(1,2)],2),(2,3,[(0,1),(1,2)],3),
(2,3,[(0,1),(1,2),(2,0)],2),
(3,2,[(0,1)],2),(3,2,[(0,1)],3),(3,1,[(0,0)],3),
(4,2,[(0,1)],2),(4,1,[(0,0)],2)
]
if __name__=='__main__':
    for case in cases:
        print('PASS',case,exhaustive(*case))
    print('ANNIHILATING_QUIVER_TUPLES_OK',len(cases))
