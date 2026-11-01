"""Independent checks for a planar-section near-maximum law of the three-cube.
No network or external data used. Python 3; numpy and scipy are required.
"""
import itertools
import math
import random
import sys
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import quad
from scipy.spatial import ConvexHull

MAX_AREA=4*math.sqrt(2)
K_QUAD=3/(8*math.pi*math.sqrt(2))
K_HEX=3*(math.pi+2)/(16*math.pi*math.sqrt(2))
K_TOTAL=3*(math.pi+4)/(16*math.pi*math.sqrt(2))

def section_formula(normal):
    n=np.array(normal,dtype=float)
    n=n/np.linalg.norm(n)
    a,b,c=sorted(abs(x) for x in n)[::-1]
    base=4/a
    correction=0 if c==0 or a>=b+c else ((b+c-a)**2)/(a*b*c)
    return base-correction

def section_polygon(normal):
    n=np.array(normal,dtype=float)
    n=n/np.linalg.norm(n)
    E=[]
    for i in range(3):
        other=[j for j in range(3) if j!=i]
        for sn in itertools.product([-1,1], repeat=2):
            p=np.zeros(3);q=np.zeros(3)
            p[other]=sn; q[other]=sn
            p[i]=-1; q[i]=1
            x=float(np.dot(n,p)); y=float(np.dot(n,q))
            if x*y < -1e-14:
                E.append(p + (q-p)*(-x)/(y-x))
    if len(E)<3: return 0,len(E)
    i=int(np.argmin(np.abs(n)))
    v=np.zeros(3);v[i]=1
    u1=v-n*np.dot(v,n);u1=u1/np.linalg.norm(u1)
    u2=np.cross(n,u1)
    proj=np.array([[float(np.dot(x,u1)),float(np.dot(x,u2))] for x in E])
    hull=ConvexHull(proj)
    return float(hull.volume),len(E)

def area_ratios(s,beta):
    alpha=1-s
    q=math.sqrt(1+alpha*alpha+beta*beta)
    if beta<=s or beta==0:
        return 4*q
    return q*(4-(beta-s)**2/(alpha*beta))

def density(s,beta):
    return (1+(1-s)**2+beta*beta)**(-1.5)

def exact_chamber_prob(eps):
    threshold=MAX_AREA-eps
    sm=brentq(lambda s:4*math.sqrt(1+(1-s)**2+s*s)-threshold,0,.25)
    def quadr(s):
        t2=(threshold/4)**2-1-(1-s)**2
        b0=math.sqrt(max(0,t2))
        return quad(lambda beta:density(s,beta),b0,s,epsabs=1e-14)[0] if b0<s else 0
    def hexa(s):
        if s>=sm: return 0
        upper=.4
        root=brentq(lambda beta:area_ratios(s,beta)-threshold,s,upper,xtol=1e-15)
        return quad(lambda beta:density(s,beta),s,root,epsabs=1e-14)[0]
    aq=quad(quadr,0,sm,epsabs=1e-12,limit=200,points=[0,sm])[0]
    ah=quad(hexa,0,sm,epsabs=1e-12,limit=200,points=[0,sm])[0]
    fac=48/(4*math.pi)
    return aq*fac,ah*fac

rng=random.Random(2649)
maxerr=0
samples=0
for _ in range(2000):
    v=np.array([rng.uniform(-1,1) for i in range(3)])
    if np.linalg.norm(v)<.2: continue
    if min(abs(x) for x in v)<.003: continue
    if abs(max(abs(x) for x in v)-(sum(abs(x) for x in v)-max(abs(x) for x in v)))<.003: continue
    a,k=section_polygon(v)
    b=section_formula(v)
    assert abs(a-b)<1e-9,(a,b,v)
    assert k in (4,6)
    sortedabs=sorted(abs(x) for x in v)[::-1]
    assert k==(4 if sortedabs[0]>sortedabs[1]+sortedabs[2] else 6)
    maxerr=max(maxerr,abs(a-b));samples+=1
print('independent polygon checks',samples,'max absolute error',maxerr)

# Verify polar area identity and coefficient split by deterministic integration.
from scipy.integrate import quad as iquad
I1=1/32
I2=iquad(lambda t:1/(8*(1+t*t)**2),0,1,epsabs=2e-15)[0]
assert abs(I2-(math.pi/64+1/32))<3e-15
assert abs((I1+I2)*48/(4*math.pi*math.sqrt(2))-K_TOTAL)<3e-15
assert abs(I1/(I1+I2)-2/(math.pi+4))<3e-15
print('limiting angular integrals',I1,I2,'coefficient',K_TOTAL)

for eps in [.15,.10,.06,.03,.015,.008]:
    pq,ph=exact_chamber_prob(eps)
    print('eps',eps,'quad_ratio',pq/(eps*eps),'hex_ratio',ph/(eps*eps),'total_ratio',(pq+ph)/(eps*eps),'conditional_quad',pq/(pq+ph))
    assert pq>0 and ph>0
assert (abs(exact_chamber_prob(.008)[0]/.008**2-K_QUAD) < .004)
assert (abs(exact_chamber_prob(.008)[1]/.008**2-K_HEX) < .004)
print('PASS: independent checks')
