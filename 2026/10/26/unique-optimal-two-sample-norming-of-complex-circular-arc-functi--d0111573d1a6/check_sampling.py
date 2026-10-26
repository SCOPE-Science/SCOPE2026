import math,random,cmath

def samples(theta,u,v):
    x=(v-u)/4
    mid=(u+v)/2
    # exact maxima: center plus candidate endpoints and peak at mid +/- pi
    points=[-theta,theta,mid,u,v]
    if -theta<=mid-math.pi<=theta:points.append(mid-math.pi)
    if -theta<=mid+math.pi<=theta:points.append(mid+math.pi)
    vals=[]
    for t in points:
        L=(abs(cmath.exp(1j*t)-cmath.exp(1j*v))+abs(cmath.exp(1j*t)-cmath.exp(1j*u)))/abs(cmath.exp(1j*u)-cmath.exp(1j*v))
        vals.append(L)
    return max(vals)

def closed(theta,u,v):
    x=(v-u)/4
    m=(u+v)/2
    return max(1/math.cos(x), math.sin(min((theta+abs(m))/2, math.pi/2))/math.sin(x))

rng=random.Random(71224)
n=0
for theta in [0.001,.17,0.4,0.9,math.pi/2,2.1,3.,math.pi-.001]:
    a=2*math.atan(math.sin(theta/2))
    best=math.sqrt(1+math.sin(theta/2)**2)
    opt=samples(theta,-a,a)
    assert abs(closed(theta,-a,a)-best)<1e-12
    assert abs(opt-best)<1e-12,(theta,opt,best)
    for k in range(300):
        u=rng.uniform(-theta,theta)
        v=rng.uniform(u,theta)
        if v-u<1e-10:continue
        observed=samples(theta,u,v)
        formula=closed(theta,u,v)
        assert abs(observed-formula)<1e-10*max(formula,1)+1e-8,(theta,u,v,observed,formula)
        for j in range(33):
            t=-theta+2*theta*j/32
            grid=(abs(cmath.exp(1j*t)-cmath.exp(1j*v))+abs(cmath.exp(1j*t)-cmath.exp(1j*u)))/abs(cmath.exp(1j*u)-cmath.exp(1j*v))
            assert grid <= formula*(1+1e-10)+1e-8
        assert observed>=best-1e-11,(theta,u,v,observed,best)
        n+=1
print('CIRCULAR_ARC_SAMPLING_CHECK_OK', n)
