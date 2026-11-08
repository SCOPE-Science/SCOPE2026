# Independent mathematical audit

## correctness

PASS

The exact ODE is p_dot=alpha(2p-p²)+(1-alpha)Pr(Bin(k,p)>=m)-p with m=ceil(k/(u+1)), u>1, 0<alpha<1, sample ties to a. If k<=2(u+1), m<=2. For m=1 drift>0 on (0,1); for m=2 the odds-coordinate positive prefactor yields polynomial 2alpha-1+sum_{j=1}^{k-2}[C(k-2,j)+(1-alpha)C(k-2,j+1)]y^j, all nonconstant coefficients strictly positive, so any interior zero repels. If k>2(u+1), m>=3 and m<=k-1. Let C=binom(k,3), eps=1/(4C), alpha=1/2+eps²/8. Union bound Pr(Bin>=m)<=Cp³ makes drift negative at eps, while leading 2alpha-1 makes drift positive sufficiently near zero and m<=k-1 yields drift positive near1. Crossing yields at least one attracting interior stationary point and another separator, for every real u>1 and integer k including tie boundaries. Independently checked all-degree odds polynomial k=3..17 and exact drift sign witnesses. Finite checks supplement exact uniform proof.

## originality

PASS

The source Arigapudi–Heller–Schreiber treats the exact sampled best response and establishes qualitative existence under heterogeneous sample sizes. The present fixed {2,k} if-and-only-if k>2(u+1), explicit k_min and all-payoff tie staircase is not implied by its quoted sufficient theorem. Classical binomial tail and 1D stability tests are ingredients rather than the exact global budget. Search found no dominating Resultary finding.

## value

PASS

The least large-sample observation budget needed for stable miscoordination is a motivated exact threshold within the published heterogeneous sampling dynamics. The all-payoff infinite staircase, precise tie transitions, and explicit mixture construction strengthen qualitative existence and let one distinguish feasible from impossible sample budgets; not an arbitrary slice because one sample size of two is the smallest nontrivial heterogeneous mixture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
