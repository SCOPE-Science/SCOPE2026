"""Independent numerical checks for nearest-facet shell probabilities.
No external packages required; all curves evaluated in the stable-combinatorics region.
"""
import math

def shell_face_probabilities(vertices,t):
    v=vertices; m=len(v)
    ls=[math.dist(v[i],v[(i+1)%m]) for i in range(m)]
    s=[]
    for i in range(m):
        a=(v[(i-1)%m][0]-v[i][0],v[(i-1)%m][1]-v[i][1]);b=(v[(i+1)%m][0]-v[i][0],v[(i+1)%m][1]-v[i][1]);
        cosine=(a[0]*b[0]+a[1]*b[1])/(math.hypot(*a)*math.hypot(*b))
        alpha=math.acos(max(-1,min(1,cosine)))
        s.append(1/math.tan(alpha/2))
    Lt=[ls[i]-t*(s[i]+s[(i+1)%m]) for i in range(m)]
    assert min(Lt)>0,(vertices,t,Lt)
    return [x/sum(Lt) for x in Lt]

samples={
 'scalene_triangle':([(0,0),(5,0),(.3,3)],.12,True),
 'square':([(0,0),(4,0),(4,4),(0,4)],.5,True),
 'non_square_rectangle':([(0,0),(4,0),(4,2),(0,2)],.25,False),
 'rhombus':([(0,0),(math.sqrt(5),0),(math.sqrt(5)+1,2),(1,2)],.15,True),
 'oblique_parallelogram':([(0,0),(4,0),(5,2),(1,2)],.15,False),
 'non_tangent_trapezoid':([(0,0),(6,0),(4,2),(2,2)],.15,False),
}
for name,(v,t,tangential) in samples.items():
    q0=shell_face_probabilities(v,0)
    qt=shell_face_probabilities(v,t)
    delta=[round(a-b,12) for a,b in zip(qt,q0)]
    eps=1e-10
    assert (max(abs(x) for x in delta)<eps)==tangential,(name,delta)
    if len(v)==4 and not tangential:assert all(abs(x)>eps for x in delta),name
    print(f'{name:28} t={t:.4f} q(0)={q0} q(t)={qt} deltas={delta}')

# Exact rectangular box shell densities, three-dimensional check.
for a,b,c in [(2,2,2),(4,2,3),(4,2,2)]:
    t=.25
    areas0=[b*c,b*c,a*c,a*c,a*b,a*b]
    areast=[(b-2*t)*(c-2*t)]*2+[(a-2*t)*(c-2*t)]*2+[(a-2*t)*(b-2*t)]*2
    qs0=[v/sum(areas0) for v in areas0]
    qst=[v/sum(areast) for v in areast]
    tangential=(a==b==c)
    assert (max(abs(v-w) for v,w in zip(qs0,qst))<1e-10)==tangential
    print('box',a,b,c,'q0',qs0,'qt',qst)
print('PASS: all polygon and 3D-box shell checks')
