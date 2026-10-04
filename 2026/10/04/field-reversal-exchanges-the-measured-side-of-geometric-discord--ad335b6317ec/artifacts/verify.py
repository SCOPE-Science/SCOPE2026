import numpy as np
from scipy.linalg import expm

sx=np.array([[0,1],[1,0]],complex)
sy=np.array([[0,-1j],[1j,0]],complex)
sz=np.array([[1,0],[0,-1]],complex)
I=np.eye(2,dtype=complex)
S=np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]],complex)
Xs=np.kron(sx,sx)
pa=[sx,sy,sz]

def H(J,Jz,B,b):
    return 0.5*(J*(np.kron(sx,sx)+np.kron(sy,sy))+Jz*np.kron(sz,sz)+(B+b)*np.kron(sz,I)+(B-b)*np.kron(I,sz))

def thermal(J,Jz,B,b,T):
    E=expm(-H(J,Jz,B,b)/T)
    return E/np.trace(E)

def discord(r,side):
    x=np.array([np.trace(r@np.kron(s,I)).real for s in pa])
    y=np.array([np.trace(r@np.kron(I,s)).real for s in pa])
    C=np.array([[np.trace(r@np.kron(a,b)).real for b in pa] for a in pa])
    if side=='A':
        K=np.outer(x,x)+C@C.T
        return 0.25*(x@x+np.sum(C*C)-np.linalg.eigvalsh(K)[-1])
    K=np.outer(y,y)+C.T@C
    return 0.25*(y@y+np.sum(C*C)-np.linalg.eigvalsh(K)[-1])

rng=np.random.default_rng(20261003)
max_state=max_A=max_B=max_hom=0.0
for _ in range(80):
    J,Jz,B,b=rng.normal(size=4)
    T=0.15+2.85*rng.random()
    r=thermal(J,Jz,B,b,T)
    rm=thermal(J,Jz,-B,b,T)
    expected=S@Xs@r@Xs@S
    max_state=max(max_state,float(np.linalg.norm(rm-expected)))
    max_A=max(max_A,abs(discord(rm,'A')-discord(r,'B')))
    max_B=max(max_B,abs(discord(rm,'B')-discord(r,'A')))
for _ in range(40):
    J,Jz,B=rng.normal(size=3)
    T=0.15+2.85*rng.random()
    max_hom=max(max_hom,abs(discord(thermal(J,Jz,-B,0.0,T),'A')-discord(thermal(J,Jz,B,0.0,T),'A')))
assert max_state < 5e-13
assert max_A < 5e-13
assert max_B < 5e-13
assert max_hom < 5e-13
print('VERIFY_OK')
print(f'max_state_covariance_error={max_state:.3e}')
print(f'max_DA_to_DB_error={max_A:.3e}')
print(f'max_DB_to_DA_error={max_B:.3e}')
print(f'max_homogeneous_DA_evenness_error={max_hom:.3e}')
print('random_state_covariance_checks=80')
print('random_directional_discord_checks=160')
print('homogeneous_field_evenness_checks=40')
