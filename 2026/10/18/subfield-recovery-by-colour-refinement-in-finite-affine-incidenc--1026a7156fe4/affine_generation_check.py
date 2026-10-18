"""Separate geometry-closure verification (joins, meets and parallels).
Imports only finite-field arithmetic from affine_refinement_check; no colour refinement calls.
"""
from affine_refinement_check import Field

def close(F, seeds):
    p,q=F.p,F.q
    mul,sub,add=F.multiply,F.sub,F.add
    inv={x:next(y for y in range(1,q) if mul(x,y)==1) for x in range(1,q)}
    def div(a,b):return mul(a,inv[b])
    def join(a,b):
        (x,y),(u,v)=a,b
        if x==u:return ('v',x)
        slope=div(sub(v,y),sub(u,x))
        return ('n',slope,sub(y,mul(slope,x)))
    def meet(a,b):
        if a==b:return None
        if a[0]=='v' and b[0]=='v':return None
        if a[0]=='v':
            x=a[1];return (x,add(mul(b[1],x),b[2]))
        if b[0]=='v':
            x=b[1];return (x,add(mul(a[1],x),a[2]))
        if a[1]==b[1]:return None
        x=div(sub(b[2],a[2]),sub(a[1],b[1]))
        return (x,add(mul(a[1],x),a[2]))
    def parallel(point,line):
        x,y=point
        if line[0]=='v':return ('v',x)
        return ('n',line[1],sub(y,mul(line[1],x)))
    pts=set(seeds);lines=set()
    for iteration in range(100):
        old=(len(pts),len(lines));P=list(pts); L=list(lines)
        for i,a in enumerate(P):
            for b in P[i+1:]:lines.add(join(a,b))
        L=list(lines)
        for i,a in enumerate(L):
            for b in L[i+1:]:
                x=meet(a,b)
                if x is not None:pts.add(x)
        for a in P:
            for b in L:lines.add(parallel(a,b))
        if (len(pts),len(lines))==old:return pts,lines,iteration+1
    raise AssertionError('closure did not stabilize')

if __name__=='__main__':
    for p,mod in [(2,(0,1)),(3,(0,1)),(5,(0,1)),(7,(0,1)),
                  (2,(1,1,1)),(2,(1,1,0,1)),(3,(1,0,1)),(2,(1,1,0,0,1)),(5,(2,0,1))]:
        F=Field(p,mod)
        start=[(0,0),(1,0),(0,1)]
        P,L,r=close(F,start)
        assert len(P)==p*p and len(L)==p*(p+1),(F.q,len(P),len(L))
        print('q',F.q,'three_seed_geometry',len(P),len(L),'iterations',r)
        if F.n>1:
            P,L,r=close(F,start+[(p,0)])
            assert len(P)==F.q**2 and len(L)==F.q*(F.q+1),(F.q,len(P),len(L))
            print('q',F.q,'four_seed_geometry',len(P),len(L),'iterations',r)
    print('GEOMETRY_CLOSURE_PASS')
