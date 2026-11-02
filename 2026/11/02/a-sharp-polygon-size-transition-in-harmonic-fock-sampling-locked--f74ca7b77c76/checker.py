"""Independent numerical diagnostics for regular-polygon harmonic-Fock sampling.
The analytical arguments do not depend on these finite tests.
"""
import math
import numpy as np
from scipy.optimize import brentq

checks = 0

def check(condition, description):
    global checks
    assert condition, description
    checks += 1

def probabilities(k,t):
    # Stable Poisson summation at moderate t.
    p=np.zeros(k)
    term=math.exp(-t)
    n=0
    while n< max(100, int(t+25*math.sqrt(t)+100)):
        p[n%k]+=term
        n+=1
        term*=t/n
    return p

def predicted(k,t):
    p=probabilities(k,t)
    a=np.array([p[j]+p[(-j)%k]-(math.exp(-t) if j==0 else 0) for j in range(k)])
    return a

def direct(k,t):
    omega=np.exp(2j*np.pi*np.arange(k)/k)
    z=np.sqrt(t)*omega
    gram=np.empty((k,k))
    for a in range(k):
        for b in range(k):
            gram[a,b]=(2*math.exp(-t)*np.real(np.exp(z[a]*np.conj(z[b])))-math.exp(-t))/k
    return gram

for k in range(2,15):
    for t in [0.02, 0.15, 0.7, 1.4, 3.5, 8.1, 22.0, 53.0]:
        a=predicted(k,t)
        g=direct(k,t)
        check(np.min(np.linalg.eigvalsh(g))>0,(k,t,'positive'))
        check(np.allclose(sorted(a),np.linalg.eigvalsh(g),rtol=1e-8,atol=1e-12),(k,t,'spectra'))
        check(abs(sum(a)-(2-math.exp(-t)))<2e-10,(k,t,'trace'))
        check(max(abs(a[j]-a[-j]) for j in range(1,k))<1e-12,(k,t,'mirror'))

for k in [2,3]:
    if k==2:
        critical=math.log(2)
    else:
        critical=brentq(lambda t: 2*math.exp(-t/2)*math.cos(math.sqrt(3)*t/2)-1,0,2*math.log(2))
    check(predicted(k,critical)[0]-predicted(k,critical)[1]<1e-9,(k,'cross upper'))
    check(abs(predicted(k,critical)[0]-predicted(k,critical)[1])<1e-9,(k,'cross lower'))
    for t in (critical*0.2, critical*0.7):
        check(predicted(k,t)[0]>predicted(k,t)[1],(k,t,'pre-cross'))
    for t in (critical*1.1,critical+0.8,critical+5,critical+12):
        check(predicted(k,t)[0]<predicted(k,t)[1],(k,t,'post-cross'))

# Witnesses for endlessly alternating least-sampled cyclic modes.
for k in range(4,16):
    if k==4:
        tpos=2*math.pi*3
        tneg=3*math.pi
    else:
        s=math.sin(2*math.pi/k)
        tpos=2*math.pi*50/s
        tneg=(2*50+1)*math.pi/s
    # At extreme large t, float cancellation hides exponentially small splitting;
    # test at moderately large witnesses for direct-order comparison.
    if k>=5:
        s=math.sin(2*math.pi/k)
        tpos=2*math.pi*2/s
        tneg=5*math.pi/s
    amin=predicted(k,tpos)
    bmin=predicted(k,tneg)
    check(int(np.argmin(amin))!=0,(k,'positive cosine nonzero mode'))
    check(int(np.argmin(bmin))==0,(k,'negative cosine symmetric mode'))

print('PASS',checks,'deterministic assertions; triple critical squared-radius',
      brentq(lambda t:2*math.exp(-t/2)*math.cos(math.sqrt(3)*t/2)-1,0,2*math.log(2)))
