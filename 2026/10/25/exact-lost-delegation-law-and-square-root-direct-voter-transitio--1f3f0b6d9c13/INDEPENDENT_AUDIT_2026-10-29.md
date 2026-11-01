# Independent mathematical audit

## correctness

PASS

On two-way K_m,n, m,n>=2, independent direct vote q in (0,1), fixed uniform opposite-part delegates otherwise, a path is represented exactly if it encounters a direct voter before first repeat. Independence of unrevealed choices gives survival A_2j=(n)_j(m-1)_j/(n^j m^j) and A_(2j+1)=(n)_(j+1)(m-1)_j/(n^(j+1)m^j), hence H_mn(q)=q sum_{t>=0}(1-q)^t A_t and R=mH_mn+nH_nm. Birthday bound log A_t approx -kappa t²/N gives q sqrt(N)->c and represented fraction F=c integral exp(-ct-kappa t²) dt, kappa=(alpha^-1+beta^-1)/8, endpoints 0,1. Summing disjoint first-repeat hazards with geometric dominated convergence at fixed q gives L->r²[2+r(rho+rho^-1)]/[q²(1+r)²]. Independent exhaustive delegation profiles for K2,2,K2,3,K3,3 at q=1/2 reproduce source-part expectations and K3,3 H=1123/1296, lost=173/216.

## originality

PASS

Existing delegation voting-power and epistemic work studies different outcomes and mostly one-way bipartite or complete-graph structures; directed one-way bipartite proxy graphs have no alternating cycles. The birthday-collision technique is classical, but the concrete exact bipartite two-way lost-mass law and two asymptotic regimes are not implied by inspected work.

## value

PASS

Lost effective vote weight is an intrinsically motivated fairness/systems observable in liquid democracy. The all-size exact law and universal square-root direct-voting crossover quantify how cyclic delegation destroys votes; the fixed-density finite limit is a non-obvious, independently useful exact invariant rather than a routine counting table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
