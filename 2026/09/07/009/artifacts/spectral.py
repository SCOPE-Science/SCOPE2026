"""Spectral analysis + coupling simulation for canonical P*."""
import numpy as np

# Canonical P*: p0=1/4,r0=3/4; interior p=1/4,q=3/4,r=0; q7=1/4,r7=3/4
P=np.zeros((8,8))
P[0,0]=0.75; P[0,1]=0.25
for i in range(1,7):
    P[i,i-1]=0.75; P[i,i+1]=0.25
P[7,6]=0.25; P[7,7]=0.75

print("P*=")
print(P)
w,v=np.linalg.eig(P.T)
print("eig(P.T):", sorted(w, key=lambda z:(z.real,z.imag), reverse=True))
w2,v2=np.linalg.eig(P)
print("eig(P):", sorted(w2, key=lambda z:(z.real,z.imag), reverse=True))
# sort by magnitude
mags=sorted([(abs(x),x) for x in w2], reverse=True)
print("by magnitude:", mags)
lam_star=max(abs(x) for x in w2 if abs(x-1)>1e-8)
print("lambda* =", lam_star)
gamma=1-lam_star
print("gap =",gamma,"t_rel =",1/gamma)
# stationary: left eigenvector for eig 1
idx=np.argmin([abs(x-1) for x in w])
pi=np.real(v[:,idx]); pi=pi/pi.sum()
print("pi =",pi, "sum",pi.sum(),"min",pi.min())
# check detailed balance pi_i*1/4 vs pi_{i+1}*3/4
for i in range(7):
    print(i, pi[i]*0.25, pi[i+1]*0.75)
# lower bound on tmix(1/4): smallest t with lam_star**t <= 2*eps = 0.5
import math
eps=0.25
t_low=math.log(2*eps)/math.log(lam_star)
print("t_low (lam^t<=1/2):",t_low,"ceil:",math.ceil(t_low))
# Levin-Peres upper via t_rel*log(1/(eps*pi_min))
print("LP upper t_rel*log(1/(eps*pi_min)):", (1/gamma)*math.log(1/(eps*pi.min())))
