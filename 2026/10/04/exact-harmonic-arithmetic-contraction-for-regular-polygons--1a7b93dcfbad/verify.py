from math import cos, sin, pi, hypot

def regular(n,R=1.0):
    return [(R*cos(2*pi*j/n),R*sin(2*pi*j/n)) for j in range(n)]

def cross(o,a,b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])

def hull(points):
    pts=sorted(set((round(x,14),round(y,14)) for x,y in points))
    if len(pts)<=1: return pts
    lo=[]
    for p in pts:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=1e-11: lo.pop()
        lo.append(p)
    hi=[]
    for p in reversed(pts):
        while len(hi)>=2 and cross(hi[-2],hi[-1],p)<=1e-11: hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1]

def diffmean(P):
    return hull([((x-u)/2,(y-v)/2) for x,y in P for u,v in P])

def polar(P):
    P=hull(P); out=[]
    for p,q in zip(P,P[1:]+P[:1]):
        px,py=p; qx,qy=q
        det=px*qy-py*qx
        out.append(((qy-py)/det,(px-qx)/det))
    return hull(out)

def containment_factor(K,C):
    # C is a CCW polygon containing 0.  Each edge is normalized to u·x<=1.
    C=hull(C); vals=[]
    for p,q in zip(C,C[1:]+C[:1]):
        px,py=p; qx,qy=q
        det=px*qy-py*qx
        ux=(qy-py)/det; uy=(px-qx)/det
        vals.append(max(ux*x+uy*y for x,y in K))
    return max(vals)

for n in range(3,52):
    P=regular(n)
    A=diffmean(P)
    H=polar(diffmean(polar(P)))
    beta_num=containment_factor(H,A)
    if n%2==0:
        beta=1.0
    else:
        s=1/cos(pi/n)
        beta=4*s/(s+1)**2
        c=cos(pi/(2*n))
        assert len(A)==2*n and len(H)==2*n
        assert max(abs(hypot(x,y)-c) for x,y in A)<2e-11
        assert max(abs(hypot(x,y)-cos(pi/n)/(c*c)) for x,y in H)<3e-11
        reverse_num=containment_factor(A,H)
        assert abs(reverse_num-(s+1)/2)<4e-11
    assert abs(beta_num-beta)<5e-11, (n,beta_num,beta)
print('VERIFY_OK regular polygon harmonic-arithmetic contraction n=3..51')
