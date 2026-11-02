from fractions import Fraction as Q
from collections import Counter

def convex_hull(points):
    p=sorted({(Q(x),Q(y)) for x,y in points})
    if len(p)<3: return tuple(p)
    def cr(a,b,c):
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    low=[]
    for x in p:
        while len(low)>=2 and cr(low[-2],low[-1],x)<=0:low.pop()
        low.append(x)
    top=[]
    for x in p[::-1]:
        while len(top)>=2 and cr(top[-2],top[-1],x)<=0:top.pop()
        top.append(x)
    return tuple(low[:-1]+top[:-1])

def clip(vertices,k,s):
    if not vertices:return ()
    pp=[]
    for a,b in zip(vertices, vertices[1:]+vertices[:1]):
        ua=s*a[k];ub=s*b[k]
        if ua>=0:pp.append(a)
        if (ua<0<ub) or (ub<0<ua):
            pp.append(tuple(a[i]+ua/(ua-ub)*(b[i]-a[i]) for i in (0,1)))
    return convex_hull(pp)

def image(vertices,sx,sy):
    return convex_hull([(sx*x-y-3, x-sy*y+1) for x,y in vertices])

def step(polys):
    result=set()
    for P in polys:
        for sx in [-1,1]:
            C=clip(P,0,sx)
            for sy in [-1,1]:
                D=clip(C,1,sy)
                if D:result.add(image(D,sx,sy))
    return result

def ingraph(x,y):
    return (y==-1 and -5<=x<=5) or (y==x+2 and -2<=x<=3) or (y==-x-2 and -2<=x<=3)

if __name__=='__main__':
    P={convex_hull([(-93,-93),(-93,93),(93,-93),(93,93)])}
    for n in range(1,10):
        P=step(P)
        print('step',n,'pieces',len(P),'sizes',dict(sorted(Counter(map(len,P)).items())))
    assert len(P)==18
    assert Counter(map(len,P))=={1:5,2:13}
    for p in P:
        assert len(p)<=2
        assert all(ingraph(x,y) for x,y in p)
        if len(p)==2:
            (x,y),(u,v)=p
            assert ((y==v==-1 and -5<=x<=5 and -5<=u<=5) or
                    (y==x+2 and v==u+2 and -2<=x<=3 and -2<=u<=3) or
                    (y==-x-2 and v==-u-2 and -2<=x<=3 and -2<=u<=3))
    print('CERTIFICATE PASS: nine images of [-93,93]^2 contained in G')
