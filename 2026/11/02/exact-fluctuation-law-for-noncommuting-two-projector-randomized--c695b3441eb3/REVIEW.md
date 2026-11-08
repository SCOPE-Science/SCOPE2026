# Independent mathematical audit

## correctness

PASS

For 0<c<1, T>0, h=T/N and rank-one 2P_u,2P_v samples, (I+2hP)^{-1}=I-2hP/(1+2h) gives sign-symmetric coordinates in the eigenbasis w_+,w_- of A=P_u+P_v. Conditioning gives exact mean (m_+^N,0), zero cross moment, and H=[[m_+²,g²],[g²,m_-²]] for second moments; Cayley-Hamilton gives E Y_N²=g²(rho_+^N-rho_-^N)/(rho_+-rho_-). The fast component fluctuates at L² order h and has O(h) bias; the slow component is L²-close after scaling sqrt(h) to an independent bounded triangular Rademacher sum, whose Riemann variance is V=(1-c²)(exp[-2(1-c)T]-exp[-2(1+c)T])/(4c)>0. Lindeberg and Slutsky establish the one-direction Gaussian limit, and positive limiting squared error/h proves sharp RMS 1/2. Independent rational path enumeration and second-moment convergence checks agree.

## originality

PASS

The exact strong-order 1/2 lower bound in the specific noncommuting two-projection test case and the explicit finite-time covariance and Gaussian one-direction fluctuation law are distinct from Eisenmann–Stillfjord’s general at-least-1/2 error estimate. The prior paper defines the randomized scheme, which is not claimed new. Other exact random product matrix asymptotics are a priority risk.

## value

PASS

The two-projector model is a minimal genuinely noncommuting example in which sampling noise moves error into a slower eigenspace. Giving a strictly positive sharp constant and limiting law determines when a general convergence-rate guarantee cannot be improved, a concrete and reusable numerical-analysis diagnostic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
