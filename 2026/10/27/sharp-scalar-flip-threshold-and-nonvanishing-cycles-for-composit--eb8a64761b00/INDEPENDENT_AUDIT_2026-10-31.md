# Independent mathematical audit

## correctness

PASS

The precise deterministic update is F(x)=(x-tau(x)(x-1))/(1+alpha lambda), where tau(x) is the source truncated nonnegative proximal Polyak step computed with exact C=0 for f=.5(x-1)^2 and ridge phi=lambda x^2/2, lambda in (0,1); tau(1)=alpha by the zero-gradient convention. On invariant [0,1], the cap decision yields continuous affine branches F=(1+x)/2 and F=((1-alpha)x+alpha)/(1+alpha lambda), slopes 1/2 and q=(1-alpha)/(1+alpha lambda). For alpha<2/(1-lambda), both slopes have modulus <1 and Banach contraction proves all initial points converge to x*=1/(1+lambda). At alpha_c=2/(1-lambda), capped slope is -1 and the exact interval [(3-lambda)/(3(1+lambda)),(3+lambda)/(3(1+lambda))] is invariant under reflection x->2x*-x, giving nontrivial two-cycles. Above alpha_c, explicit x_-=(1+alpha)/(1+alpha+2alpha lambda), x_+=(1+alpha+alpha lambda)/(same) straddle the switching threshold, and exact branch substitution gives F(x_-)=x_+, F(x_+)=x_-. The fixed point has derivative q<-1; the cycle return multiplier is q/2, locally attracting exactly when alpha(1-2lambda)<3, repelling when >3, only linearly neutral at equality. Independent exact rational checks cover critical intervals and multiple supercritical parameters; algebra and branch inequalities prove all quantifiers. No claim about all real starting states or every postcritical orbit.

## originality

PASS

Statement/implication comparison of actually read primary theorems and direct published mathematical-finding search supports best-of-knowledge originality for the final narrow claim, with precisely documented broader prior formulas and residual historical risks. Neither a failed search nor literature inaccessibility is treated as a proof of novelty.

## value

PASS

The scalar strongly-convex composite is the minimal natural test bed for evaluating cap robustness in a specified optimization algorithm. Its exact convergence frontier, critical continuum of reflected cycles, and nonvanishing nonoptimal cycle show a structural limitation of a popular safeguarding choice; analytic thresholds are useful for adaptive-step design. This is not merely a small isolated counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
