import math

def f(z, R2):
    return (2.0*math.sqrt(R2-4.0*z)
            + math.sqrt(3.0)*math.sqrt(R2-3.0*z)
            + math.sqrt(R2-z) - math.sqrt(3.0))

R2=math.sqrt(3.0)/(2.0*math.pi)
R=math.sqrt(R2)
lo=R2/8.0
hi=R2/4.0
assert f(lo,R2)>0.0 and f(hi,R2)<0.0
for _ in range(100):
    mid=(lo+hi)/2.0
    if f(mid,R2)>0.0:
        lo=mid
    else:
        hi=mid
z=(lo+hi)/2.0
q=math.sqrt(z)
d2=math.sqrt(R2-4.0*z)
s=math.sqrt(R2-3.0*z)
t=math.sqrt(R2-z)
assert abs(2*d2+math.sqrt(3.0)*s+t-math.sqrt(3.0))<2e-14
ells=[math.sqrt(R2-d2*d2),math.sqrt(R2-s*s),math.sqrt(R2-t*t)]
rat=[ells[0]/2.0,ells[1]/math.sqrt(3.0),ells[2]]
assert max(rat)-min(rat)<2e-14
assert abs(s-0.3719164279770188862100673)<2e-15
assert abs(t-0.4794617554511785131491672)<2e-15
verts=[(0.0,0.0),(1.0,0.0),(0.0,math.sqrt(3.0))]
for x,y in verts:
    assert (x-s)**2+(y-t)**2>R2

def cap(d):
    return R2*math.acos(d/R)-d*math.sqrt(R2-d*d)
out=cap(d2)+cap(s)+cap(t)
alpha=4.0*out/math.sqrt(3.0)
assert abs(alpha-0.5168009538789127383)<2e-14
# Positive cap Hessian weights and nonparallel normals imply positive definiteness.
weights=[2*d2/math.sqrt(R2-d2*d2),2*s/math.sqrt(R2-s*s),2*t/math.sqrt(R2-t*t)]
normals=[(-math.sqrt(3)/2,-0.5),(1.0,0.0),(0.0,1.0)]
H=[[0.0,0.0],[0.0,0.0]]
for w,(x,y) in zip(weights,normals):
    H[0][0]+=w*x*x; H[0][1]+=w*x*y; H[1][0]+=w*y*x; H[1][1]+=w*y*y
assert H[0][0]>0 and H[0][0]*H[1][1]-H[0][1]*H[1][0]>0
print('VERIFY_OK')
