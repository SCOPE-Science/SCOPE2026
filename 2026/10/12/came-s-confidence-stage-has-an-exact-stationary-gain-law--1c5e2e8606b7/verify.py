import math
import numpy as np

def cyclic_mask(n, k):
    B = np.zeros((n,n), dtype=float)
    for i in range(n):
        for j in range(k):
            B[i,(i+j)%n] = 1.0
    return B

def h_closed(t,b1,b3,eps2):
    base = (1.0-b3)*sum((b3**(t-i))*(b1**(2*i)) for i in range(1,t+1))
    return base + eps2*(1.0-b3**t)

def replay(n,k,g,b1,b2,b3,eps2,T):
    B = cyclic_mask(n,k)
    signs = np.where(B>0, np.where((np.indices((n,n)).sum(axis=0)%2)==0,1.0,-1.0), 0.0)
    G = g*signs
    r = np.zeros(n)
    c = np.zeros(n)
    m = np.zeros((n,n))
    R = np.zeros(n)
    C = np.zeros(n)
    out = []
    for t in range(1,T+1):
        r = b2*r + (1.0-b2)*(G*G).sum(axis=1)
        c = b2*c + (1.0-b2)*(G*G).sum(axis=0)
        V = np.outer(r,c)/r.sum()
        U = np.divide(G,np.sqrt(V),out=np.zeros_like(G),where=V>0)
        rms_u = math.sqrt(np.mean(U*U))
        Uh = U/max(1.0,rms_u)
        m = b1*m + (1.0-b1)*Uh
        E = (Uh-m)**2
        R = b3*R + (1.0-b3)*(E+eps2).sum(axis=1)
        C = b3*C + (1.0-b3)*(E+eps2).sum(axis=0)
        S = np.outer(R,C)/R.sum()
        D = m/np.sqrt(S)
        out.append((B,signs,Uh,m,S,D))
    return out

for n,k in [(4,1),(5,2),(7,3),(8,8)]:
    p = k/n
    b1,b2,b3,eps2,g = 0.9,0.999,0.97,1e-6,2.3
    rows = replay(n,k,g,b1,b2,b3,eps2,40)
    for t,(B,Q,Uh,m,S,D) in enumerate(rows,1):
        active = B>0
        target_u = Q/math.sqrt(p)
        assert np.max(np.abs(Uh-target_u)) < 3e-12
        target_m = (1.0-b1**t)*target_u
        assert np.max(np.abs(m-target_m)) < 3e-12
        h = h_closed(t,b1,b3,eps2)
        assert np.max(np.abs(S-h)) < 3e-12
        target_D = target_m/math.sqrt(h)
        assert np.max(np.abs(D-target_D)) < 2e-10
        rms = math.sqrt(np.mean(D*D))
        assert abs(rms-(1.0-b1**t)/math.sqrt(h)) < 2e-10

# Density ratio against the dense reference.
n=12
b1,b2,b3,eps2,g = 0.8,0.95,0.99,1e-8,1.7
dense = replay(n,n,g,b1,b2,b3,eps2,25)[-1][-1]
dense_amp = np.max(np.abs(dense))
for k in (1,2,3,4,6):
    p=k/n
    D = replay(n,k,g,b1,b2,b3,eps2,25)[-1][-1]
    amp = np.max(np.abs(D))
    assert abs(amp/dense_amp - 1.0/math.sqrt(p)) < 2e-10
    assert abs(math.sqrt(np.mean(D*D))-math.sqrt(np.mean(dense*dense))) < 2e-10

# Positive confidence floor.
b1,b3,eps2 = 0.9,0.9999,1e-6
t=300000
h = h_closed(t,b1,b3,eps2)
rms = (1.0-b1**t)/math.sqrt(h)
assert abs(rms-1.0/math.sqrt(eps2)) < 2e-6

# Zero-floor closed forms and divergence.
for b1,b3 in [(0.9,0.9999),(0.9,0.5),(0.8,0.64)]:
    for t in (2,5,20):
        h = h_closed(t,b1,b3,0.0)
        if abs(b3-b1*b1) > 1e-14:
            hc = (1.0-b3)*b1*b1*(b3**t-b1**(2*t))/(b3-b1*b1)
        else:
            hc = t*(1.0-b3)*b1**(2*t)
        assert abs(h-hc) < 2e-13

print("verification passed")
