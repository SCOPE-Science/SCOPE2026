#!/usr/bin/env python3
"""Exact integer checks for an h-ary three-generator numerical-semigroup family."""
from heapq import heappop, heappush

def apery_by_dijkstra(a, A, B):
    d=[None]*a
    d[0]=0
    heap=[(0,0)]
    while heap:
        z,r=heappop(heap)
        if z!=d[r]:continue
        for b in (A,B):
            u=(r+b)%a
            if d[u] is None or z+b<d[u]:
                d[u]=z+b
                heappush(heap,(z+b,u))
    return d

def predicted(h,a):
    R=h*h-h+1
    A=h*a+1
    B=h*h*a+R
    q,t=divmod(a-1,R)
    w=[(r//R)*B+(r%R)*A for r in range(a)]
    if q==0:
        pf=[w[-1]-a]
    elif t==R-1:
        pf=[w[-1]-a]
    else:
        pf=sorted({(q-1)*B+(R-1)*A-a,q*B+t*A-a})
    gen_num=R*q*(q-1)*B+(2*(t+1)*q)*B+(R*(R-1)*q+t*(t+1))*A-a*(a-1)
    assert gen_num%(2*a)==0
    genus=gen_num//(2*a)
    frob=max(pf)
    return w,pf,genus,frob

def independent_pf(d, a, gens):
    def member(x):return x>=0 and x>=d[x%a]
    return sorted(w-a for w in d if all(member(w+g-a) for g in gens))

def run():
    checked=0;gapcount=0;near=0
    for h in range(4,12):
        R=h*h-h+1
        a0=(h-3)*R+h+1
        for a in range(a0,a0+R+25):
            A=h*a+1;B=h*h*a+R
            expected,pf,g,f=predicted(h,a)
            d=apery_by_dijkstra(a,A,B)
            assert d==expected,(h,a,'Apéry')
            assert sorted(pf)==independent_pf(d,a,(a,A,B)),(h,a,'PF')
            assert f==max(d)-a,(h,a,'F')
            q,t=divmod(a-1,R)
            U=(q-1)*B+(R-1)*A-a
            V=q*B+t*A-a
            assert f==(U if t<=(h-1)**2-2 else V),(h,a,'F branch')
            direct_g=sum((d[r]-r)//a for r in range(a))
            assert g==direct_g,(h,a,'g')
            assert (len(pf)==1)==(a%R==0),(h,a,'type')
            checked+=1
        a=a0-1
        A=h*a+1;B=h*h*a+R
        r=R-h
        assert (h-2)*B<(R-h)*A and (h-2)*B%a==r%a
        d=apery_by_dijkstra(a,A,B)
        assert d[r]<(R-h)*A
        gapcount+=1
    for a in range(4,200):
        h=3
        A=h*a+1;B=h*h*a+7
        w,pf,g,f=predicted(h,a)
        d=apery_by_dijkstra(a,A,B)
        assert w==d
        assert pf==independent_pf(d,a,(a,A,B))
        near+=1
    print(f'PASS {checked} stable pairs h=4..11, {gapcount} sharp boundary failures, {near} h=3 boundary checks')
if __name__=='__main__':run()
