# Independent mathematical audit

## correctness

PASS

For lambda>1, beta>0, 0<gamma<1 with gamma<=(lambda-1)/(2lambda) and R=beta*gamma*(lambda-1)<1, t=Y(1+cY) gives a bijective equilibrium parameterization X=A+B exp(-t), Y=F(t)=beta*gamma*(1-exp(-t))*(A+B exp(-t)). Since A>=B>0, F is a positive sum of exponentials with 0<F'(t)<=R<1. The exact derivative C'=F'K/F^2 of C=(t-F)/F^2 and the independently verified K''>0 formula imply exactly one positive zero of K: K(0)=0, K'(0)=R-1<0, K(infinity)>0. Thus C has a unique nondegenerate positive minimum and diverges at both ends, proving exactly 0/1/2 strictly positive fixed points below/at/above c*. Inverse branch derivatives give opposite Y monotonicities and asymptotic expansions. Independent SymPy differentiation reproduced the nonstandard convexity identity; numeric bisection gave c*=2.319323453738189 for lambda,beta,gamma=3,4,0.1 and reconstructed map residuals. Neither sampling nor threshold logs are the global proof.

## originality

PASS

Best-of-knowledge originality for the precise final mathematical claim; generic tools and starting formulae are acknowledged as prior. The fixed-point nullcline reduction uses the same map as Jang–Yousef, but its Theorem 2.4 gives only a sufficient nonexistence condition and an upper bound of two solutions; the unique all-parameter c-fold and inverse branches are stronger.

## value

PASS

A coexistence threshold below predator-invasion one is directly motivated by a discrete prey-refuge predator model. The result upgrades a sufficient no-coexistence condition and numeric fold into a sharp necessary-and-sufficient global fixed-point count in a genuinely nonempty parameter region; the branch limits are useful to bifurcation analysis. It does not assert dynamics or stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
