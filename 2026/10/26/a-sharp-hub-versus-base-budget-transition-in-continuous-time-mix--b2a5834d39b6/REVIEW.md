# Independent mathematical audit

## correctness

PASS

For nonnegative symmetric rates with each undirected edge counted once, λ₂ is the minimum over unit vectors perpendicular to the constants of the linear weighted sum of edge squared differences. It is concave even on allocations with a disconnected positive-rate graph. Averaging over the base automorphism group extended to fix the hub leaves the objective no smaller, and gives exactly two rate classes. For their common rates s,t the hub/base constant contrast has eigenvalue (n+1)s and the base mean-zero eigenvectors, extended by a zero hub entry, have eigenvalues s+tλ_j(L_H). Consequently the gap is min{(n+1)s, βB/n+(1−β)s} on 0≤s≤B/n after eliminating t. If β<1 both lines increase and the invariant maximizer is the all-spoke endpoint. If β=1 the flat line is active from s=B/[n(n+1)] to B/n. If β>1 the lines cross in the interior at s=βB/[n(n+β)]; substitution gives the stated t and gap. In the strict low regime an arbitrary optimum must average to the all-spoke endpoint; it cannot have any positive base rate because the averaging preserves the total base rate. The cyclic and cube characters give g=4 sin²(π/n) and g=2 respectively, so the integer boundaries follow. The two-orbit assertion is for automorphisms fixing the designated hub, as used in the proof; for a clique base the full automorphism group has one edge orbit, but the stated unique invariant solution then has s=t and also obeys the full symmetry. No classification of every asymmetric optimizer at or above the threshold is needed. The frozen notes and cone_verify.py were inspected, not executed; global optimality follows from the analytic reduction.

## originality

PASS

Credit the general connected, vertex- and edge-transitive base theorem: a single base-spectral criterion gives the exact gap, invariant optimizer regimes and forced loss of all base edges in every strict low-regime optimum. Do not credit the wheel specialization as new for rim size n≥4: the earlier priced-wheel record gives exactly that specialization at unit spoke price, with a stronger rigidity result. The general cone result and application beyond cycles are not covered by that wheel theorem or by the inspected general optimization machinery. This is a scoped best-of-current-knowledge decision.

## value

PASS

For an entire natural class of augmented networks, the result tells when one should spend none of the rate budget on existing base edges, even if asymmetric allocations are allowed, and when including those edges improves the gap over the all-spoke design. A base-only scalar replaces an edge-dimensional optimization and gives the critical plateau and the optimum on either side. The value is in the cross-family support and allocation law, not in recalculating the known wheel case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
