# Independent mathematical audit

## correctness

PASS

For x^prime=-a x - b x(t-tau)-c x(t-2tau), with b≠0,c>0,c<a<3c,b²=8c(a-c), frequency elimination has the unique double positive z=(a-c)(3c-a)=omega². Phase equations determine only tau_n=(theta+2πn)/omega. The identities b*exp(-i theta)+2c exp(-2i theta)=-2c and f_lambda=1+2c*tau_n>0 show a simple imaginary pair. Implicit differentiation gives Re lambda^prime(tau_n)=0 and Re lambda^doubleprime=2omega²(a-3c)/(1+2c tau_n)^3<0, proving left-side quadratic contact. At tau->0 all RHP roots would be uniformly bounded by |lambda+a|<=|b|+c and tend to -a-b-c<0, contradiction; roots cannot enter RHP from infinity at finite tau. With no other imaginary frequencies and no crossovers, zero RHP count persists for all tau>0. Independent exact SymPy checked the derivative and three sample parameter sets; analytic proof establishes the continuum result.

## originality

PASS

Qualified PASS: Hata–Matsunaga 2022 explicitly leave this exact discriminant-zero positive-frequency stability case without a criterion in Remark 1.4. The new contact curvature plus global root count closes that gap, though Mahaffy–Busken 2015 covers related R=1/2 D-partition tangency geometry and remains a possible implication risk.

## value

PASS

The explicitly excluded repeated-frequency locus is a meaningful missing boundary of published necessary-and-sufficient linear stability criteria. Quadratic leftward root tangency rigorously distinguishes isolated neutral delays from instability intervals, a structural answer missed by ordinary transversality tests.

The dated certificate retains the supplied scientific assessment, sources and limitations.
