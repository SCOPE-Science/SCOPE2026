"""Finite-sample diagnostics for perimeter loss of perimeter-sampled convex polygons.
Standard-library Python. Empirical tests are supplementary, not the proof.
"""
import math,random

def length(points):
    return sum(math.dist(points[i],points[(i+1)%len(points)]) for i in range(len(points)))

def exterior_angles(poly):
    ans=[]
    for i in range(len(poly)):
        x0,y0=poly[(i-1)%len(poly)];x1,y1=poly[i];x2,y2=poly[(i+1)%len(poly)]
        a=(x1-x0,y1-y0); b=(x2-x1,y2-y1)
        det=a[0]*b[1]-a[1]*b[0];dot=a[0]*b[0]+a[1]*b[1]
        z=math.atan2(det,dot)
        assert 0<z<math.pi
        ans.append(z)
    return ans

def h(beta):
    s=math.sin(beta/2)
    return 1-(1-s*s)*math.atanh(s)/s

def sample(poly,n,rng):
    edge=[math.dist(poly[i],poly[(i+1)%len(poly)]) for i in range(len(poly))]
    starts=[0.]
    for e in edge: starts.append(starts[-1]+e)
    values=sorted(rng.random()*starts[-1] for _ in range(n))
    out=[];j=0
    for v in values:
        while j+1<len(poly) and starts[j+1]<v: j+=1
        t=(v-starts[j])/edge[j]
        a=poly[j];b=poly[(j+1)%len(poly)]
        out.append((a[0]*(1-t)+b[0]*t,a[1]*(1-t)+b[1]*t))
    return out

def main():
    polys=[[(0,0),(1,0),(1,1),(0,1)],[(0,0),(3,0),(2,2),(-1,1)],
           [(0,0),(3,0),(1.5,2.598076211353316)]]
    rng=random.Random(442891)
    for vertices in polys:
        L=length(vertices)
        c=L*sum(h(x) for x in exterior_angles(vertices))
        for n in (20,50,100,200):
            prediction=c/(n+1)
            observed=sum(L-length(sample(vertices,n,rng)) for _ in range(2000))/2000
            print(len(vertices),n,round(prediction,8),round(observed,8))
            assert abs(observed-prediction)< max(.02*L,.25*prediction)
    print('PASS numeric tests')
if __name__=='__main__':main()
