# Independent mathematical audit

## correctness

PASS

After coordinate complements, a real hyperplane with k nonzero normal entries cuts out a level antichain of strictly positive subset weights on those k coordinates. Sperner gives 2^(n−k) times the central binomial coefficient; the central binomial fraction for k≥3 is at most 3/8 (it stays constant from odd k to the next even k and then strictly decreases). For k=1 only the two coordinate sides have half the cube; for k=2 only equal positive weights after complementing can repeat a level, yielding the equality/complement traces. Thus there are exactly K=2n+2 binom(n,2)=n(n+1) dominant hyperplanes. Their binary traces are nonzero linear parity equations, whose distinct pairs have either conflicting right sides or two independent equations, so intersect in at most N/4 vertices. The use of parity is only on the trace; all sampled affine ranks are real. Every deficient set, including the empty set, has an affine basis extendible to n affinely independent cube vertices, giving at most binom(N,n) candidate hyperplanes. For a fixed H the containment event has probability q^(N−|H∩cube|). The one- and two-term Bonferroni bounds on the dominant events and the nondominant trace bound give the two claimed errors without assuming event independence. After division by Kq^(N/2) they decay exponentially in N, since binom(N,n)≤exp(n² log 2); for example c_p=−log(q)/16 works for all sufficiently large n. Each dominant trace is affinely a full (n−1)-cube. Independently retaining its vertices gives exactly q^(N/2)(1−ρ_(n−1)) for the event that the affine hull equals that hyperplane. These events are disjoint. The same finite hyperplane union bound gives ρ_(n−1)≤binom(N/2,n−1)q^(N/4), so the disjoint equal masses exhaust the rank-failure event up to exponentially small relative error. The exact pair-type fraction within the family is n(n−1)/K=(n−1)/(n+1); outside-family mass accounts for the claimed overall error.

## originality

PASS

Best-of-knowledge pass for the finite error bound, fixed-p rare-event equivalent, and exact and asymptotic conditional geometry taken together. The strongest same-model archive match conditions on full dimension and measures decomposition; same-model papers bound typical edge expansion or locate a sparse center-containment threshold. Littlewood–Offord concentration and real rank arguments are standard inputs and do not get separate novelty credit. The verified primary and indexed comparisons did not yield the leading factor with a relative error and the disjoint conditional affine-hull law in this model. This is not an exhaustive priority claim.

## value

PASS

For a canonical random Boolean polytope, the result quantifies a basic geometric degeneracy far beyond a high-probability full-dimension statement. The prefactor and conditional split explain why diagonal equalities or complements, not missing coordinate sides, dominate the rare event. Exact conditional uniformity over both geometrically different types and a rigorous gap to the exceptional events give usable structural information beyond the textbook slice-size bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
