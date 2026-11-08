# Independent mathematical audit

## correctness

PASS

For iid N(0,1) entries, ordered first-column absolute values have density 2 f(p)f(u), 0<u<p, while pivoted second-column magnitudes B,D remain independent half-normal. Only reinforcing Gaussian sign configuration (probability 1/2) permits growth beyond 1, and the updated trailing magnitude is D+(u/p)B. For the near-2 event stratify by unique M=max(p,B,D). On M=B, two deficits v=1-D/B,w=1-u/p obey v+w<epsilon; on M=D they obey v+w-vw<epsilon. Each region scales to a unit simplex of area 1/2, giving J/2 in the epsilon^-2 limit. M=p requires three O(epsilon) deficits and contributes O(epsilon^3). Dominated convergence is valid with exponentially decaying half-normal integrand. J=(4/pi^2)∫_0∞ te^-t² ∫_0^t pe^-p² dp dt=1/(2pi²). Hence lim epsilon^-2 P(rho>2-epsilon)=1/(2pi²), for exact-arithmetic real 2x2 GEPP only. Independent code re-derived the determinant/Schur complement for 100000 seeded Gaussian matrices and separately integrated the limiting J; simulation alone cannot establish the epsilon asymptotic.

## originality

PASS

The claim is the fixed n=2 near-boundary probability expansion, not the known deterministic bound or high-dimensional mean/tail behaviors. Closest primary work focuses on dimension scaling, average growth or different rare-event simulations; full Urschel manuscript was inspected by PDF and concerns high dimension. This does not exclude a buried exact two-dimensional calculation in older matrix-stability literature.

## value

PASS

The sharp near-worst-case tail exponent and coefficient for the smallest nontrivial Gaussian partial-pivoting system provide a natural exact baseline for a central numerical-stability statistic and rare-event studies; the probability law, not the classical deterministic 2 bound, is the new invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
