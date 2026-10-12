import math
import random
import numpy as np

def outer_matrix(s,tau,alpha,beta):
    q=(1.0-s)**tau
    delta=alpha*(1.0-q)
    return np.array([[1.0+beta-delta,-beta],[1.0,0.0]]), q, delta

def analytic_stable(s,tau,alpha,beta):
    q=(1.0-s)**tau
    delta=alpha*(1.0-q)
    return 0.0 < delta < 2.0*(1.0+beta)

random.seed(350083)

# General analytic condition versus direct spectrum.
for _ in range(12000):
    s=10**random.uniform(-3,1)
    tau=random.randint(1,15)
    alpha=10**random.uniform(-3,1)
    beta=random.uniform(0.0,0.999)
    M,q,delta=outer_matrix(s,tau,alpha,beta)
    rad=max(abs(z) for z in np.linalg.eigvals(M))
    exact=analytic_stable(s,tau,alpha,beta)
    if min(abs(delta),abs(delta-2*(1+beta)))>1e-8:
        assert (rad<1.0)==exact

# Direct source update versus eliminated recurrence.
for _ in range(1000):
    lam=10**random.uniform(-1,1)
    gamma=10**random.uniform(-2,0)
    tau=random.randint(1,8)
    alpha=random.uniform(0.1,1.5)
    beta=random.uniform(0.0,0.95)
    x_prev=random.uniform(-2,2)
    x=random.uniform(-2,2)
    u=(x_prev-x)/(alpha*gamma)
    q=(1-gamma*lam)**tau
    u_next=beta*u+(1-q)*x/gamma
    x_next=x-alpha*gamma*u_next
    rec=(1+beta-alpha*(1-q))*x-beta*x_prev
    assert abs(x_next-rec)<2e-12*max(1.0,abs(x_next),abs(rec))

# Alpha=1 parity boundaries.
for beta in (0.0,0.2,0.5,0.8,0.95):
    for tau in range(1,11):
        if tau%2==0:
            bound=2.0
        else:
            bound=1.0+(1.0+2.0*beta)**(1.0/tau)
        assert analytic_stable(0.5*min(bound,1.0),tau,1.0,beta)
        assert analytic_stable(bound*(1-1e-7),tau,1.0,beta)
        assert not analytic_stable(bound*(1+1e-7),tau,1.0,beta)
        M,_,_=outer_matrix(bound,tau,1.0,beta)
        vals=np.linalg.eigvals(M)
        target=1.0 if tau%2==0 else -1.0
        assert min(abs(z-target) for z in vals)<2e-7

# Positive slow momentum strictly extends the odd-period fast-step limit.
for beta in (0.1,0.5,0.9):
    for tau in (1,3,5,7,9):
        bound=1+(1+2*beta)**(1/tau)
        assert bound>2
        s=0.5*(2+bound)
        assert s>2
        assert analytic_stable(s,tau,1.0,beta)

print("verification passed")
