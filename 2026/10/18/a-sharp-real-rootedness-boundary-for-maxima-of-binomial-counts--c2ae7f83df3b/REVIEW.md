# Independent mathematical audit

## correctness

PASS

The exact order-statistic probability mass is P(M=k)=F_k(p)^m-F_(k-1)(p)^m, with F the Bin(n,p) CDF. At n=2, the quadratic discriminant is q^(2m)*([(1-p)^m+(1+p)^m]^2-4)>0 by strict convexity for m>=2, and all coefficients are positive, so the roots are strictly negative. For any fixed n>=3,m>=2, coefficientwise convergence of G(t/p) at p->0 gives m(1+t)^n-(m-1) with a simple nonreal zero; fixed-degree root continuity supplies a genuine positive-p failure interval. For n=3,m=2, exact sympy re-expansion of the CDF squared verifies Disc_z G=108 p^6(1-p)^12 Q(p), Q=4p^6+8p^3+3p^2+6p-1. Q increases strictly from -1 to 20 and has a unique positive root; positive PGF coefficients exclude nonnegative real roots, so sign of the discriminant yields the precise iff. At equality its simple discriminant zero implies exactly one double negative root. Crosschecks verify polynomial factorization and sampled signs; the universal n>=3 statement uses analytic root continuity, not a finite grid.

## originality

PASS

Qualified best-of-knowledge originality for the precise final theorem and its stated parameter domain. The four named implication comparisons discriminate known mathematical inputs from the sharp new increment; an unindexed equivalence remains possible. Generic characterization cannot supply root locations for these maxima. The proof exhibits a nonreal root for all n>=3 small p, excluding any generic stronger max-preservation result without contradicting its own hypotheses.

## value

PASS

Real-rootedness/Poisson-binomial factorization is a strictly stronger natural invariant than log concavity for maxima of familiar binomial counts. The largest trial size universally preserving it and the exact first failing probability threshold are meaningful familywise boundary facts rather than a generic counterexample; the rare-event polynomial mechanism identifies the obstruction for every n>=3.

The dated certificate retains the supplied scientific assessment, sources and limitations.
