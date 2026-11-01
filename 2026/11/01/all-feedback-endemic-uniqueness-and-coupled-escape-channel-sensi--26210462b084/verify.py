"""Standalone numerical checks of the maximal-reinfection SIRCm equilibrium identities.
Analytical inequalities and global uniqueness require the accompanying proof.
"""
from math import isfinite
from fractions import Fraction


def formulas(mu, alpha, beta, delta, gamma, e1, e2, z):
    k=(mu+alpha)/beta; a=1-k; U=mu*a; V=mu+gamma; g=gamma*e2
    C=(beta*z-U)/(V+g*z); S=k-C; I=z/S; R=a-I
    G=(beta-U/z)*(1+beta*z/(S*(V+g*z)))/R
    eq=G-delta*(1/z+e1)
    return S,I,R,C,eq,G


def solve(mu, alpha, beta, delta, gamma, e1, e2):
    k=(mu+alpha)/beta; a=1-k; z0=mu*a/beta
    lo=z0; hi=k*a
    # z<ka for all interior equilibria; invalid intermediate states are above the R=0 frontier.
    for _ in range(180):
        mid=(lo+hi)/2
        g=gamma*e2;V=mu+gamma;U=mu*a
        C=(beta*mid-U)/(V+g*mid);S=k-C
        if S<=0: hi=mid;continue
        I=mid/S;R=a-I
        if R<=0: hi=mid
        else: lo=mid
    zmax=lo
    lo=z0;hi=zmax
    for _ in range(160):
        mid=(lo+hi)/2
        S,I,R,C,eq,G=formulas(mu,alpha,beta,delta,gamma,e1,e2,mid)
        if eq>=0:hi=mid
        else:lo=mid
    z=(lo+hi)/2
    S,I,R,C,eq,G=formulas(mu,alpha,beta,delta,gamma,e1,e2,z)
    G1=1+e1*z; G2=1+e2*z
    residuals=[mu*(1-S)-beta*S*I+gamma*G2*C,
               beta*I*(S+C)-(mu+alpha)*I,
               alpha*I-(mu+delta*G1)*R,
               delta*G1*R-(beta*I+mu+gamma*G2)*C]
    assert all(v>0 and isfinite(v) for v in (S,I,R,C,z))
    assert abs(S+I+R+C-1)<1e-9
    assert max(abs(v) for v in residuals)<1e-8, (residuals,z)
    assert abs(I-a*(mu+delta*G1)/(alpha+mu+delta*G1))<1e-9
    return z,I,(S,I,R,C),residuals


def exact_identities():
    for mu,alpha,beta,delta,gamma,e1,e2,z in [
       tuple(map(Fraction, seq)) for seq in [
          ('1','2','6','3','4','0','0','1/10'),
          ('1/3','7/5','4','1/7','1/2','2','11','1/12'),
          ('1/10','1/2','2','10','1','1/7','100','1/20'),
        ]]:
        k=(mu+alpha)/beta;a=1-k;U=mu*a;V=mu+gamma;g=gamma*e2
        C=(beta*z-U)/(V+g*z);S=k-C;I=z/S;R=a-I
        # The S and I equilibrium equations are exact rational identities.
        assert mu*(1-S)-beta*S*I+gamma*(1+e2*z)*C==0
        assert beta*I*(S+C)-(mu+alpha)*I==0
        left=C*(beta*I+mu+gamma*(1+e2*z))/(z*R)
        right=(beta-U/z)*(1+beta*z/(S*(V+g*z)))/R
        assert left==right
    print('EXACT_STEADY_STATE_AND_REDUCTION_IDENTITIES_PASS 3')


def main():
    exact_identities()
    configs=[(.02,120.,600.,.625,.35),(.12,1.2,4.,.9,.3),(.001,.01,.09,9.,5.),(2.,7.,21.,.08,3.),(.3,.7,2.5,8.,.01)]
    cases=0
    for mu,alpha,beta,delta,gamma in configs:
        if beta<=mu+alpha:continue
        for e1 in (0.,.1,5.,100.):
            rows=[]
            for e2 in (0.,.5,20.,2000.):
                z,I,v,r=solve(mu,alpha,beta,delta,gamma,e1,e2)
                rows.append((z,I))
                cases+=1
            assert all(rows[i+1][0]>rows[i][0]+1e-14 for i in range(3)),rows
            if e1==0.:
                assert max(abs(row[1]-rows[0][1]) for row in rows)<1e-10
            else:
                assert all(rows[i+1][1]>rows[i][1]+1e-13 for i in range(3)),rows
        for e2 in (0.,.5,20.,2000.):
            rows=[solve(mu,alpha,beta,delta,gamma,e1,e2)[:2] for e1 in (0.,.1,5.,100.)]
            assert all(rows[i+1][0]>rows[i][0]+1e-13 for i in range(3))
            assert all(rows[i+1][1]>rows[i][1]+1e-13 for i in range(3))
    print('EQUILIBRIUM_RESIDUAL_AND_COMPARATIVE_STATICS_PASS',cases)
    print('INFINITE_PARAMETER_AND_ALL_POSITIVE_RATES_REQUIRE_ANALYTIC_PROOF')

if __name__=='__main__':main()
