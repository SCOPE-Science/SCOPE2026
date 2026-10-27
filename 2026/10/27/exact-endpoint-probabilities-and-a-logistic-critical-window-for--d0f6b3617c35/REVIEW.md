# Scientific review

## Correctness
**PASS.** Alternating independent coupon streams give an exact event identity, and two independent finite constructions (inclusion-exclusion and first-step state recursion) agree on all tested small parameters. The balanced correction follows from a strict \(\ell^2\) convolution bound and a Gumbel/Parseval dominated-convergence argument. The logistic window follows from joint independent coupon limits and the continuous logistic difference law. The two-vertex closed form follows from the coupon completion-time product transform. All boundaries \(a,b\ge1\), \(m=2\), positive near-balanced sizes, and the meaning of 'last new vertex' are explicitly specified. The finite checker passed 190 exact assertions. The limits rely on proofs, not computation.

## Originality
**PASS, subject to priority uncertainty.** The 1993 and 2022 cover-tour papers provide a uniform-endpoint classification rather than an explicit two-part endpoint law. Myers and Wilf (2003) already give the equal-coupon-collector tie probability, and the classical Gumbel limit is prior; these **are not claimed as separate novel facts**. The candidate's subject is the combined exact endpoint law for all \(K_{a,b}\) with a sharp imbalance window and balanced correction. Searched mathematical records and inspected primary text did not exhibit that combined result. The 1993 primary paper was available at the abstract level but not in accessible full text, leaving explicit residual priority risk.

## Value
**PASS.** The endpoint distribution is a natural observable in the cover-tour uniformity question. The rational formula gives every finite opposite-part probability, the logistic limit identifies the first nondegenerate part-size imbalance scale, and the balanced correction quantifies how a highly symmetric, non-complete graph approaches side-uniformity. The two-vertex-part formula gives a complementary sharp finite extreme. This is a graph-wide probability law rather than a relabeling or isolated small-example calculation.

## Closest literature and limitations
Buchanan–Horn–Rombach (arXiv:2209.08079v1) and Lovász–Winkler (1993) address which graphs have uniform last-vertex probabilities, not the explicit complete-bipartite profile. Myers–Wilf (arXiv:math/0304229v1, §2.1) evaluates the equal-collector tie input. The finite full-text comparison for the 1993 paper could not be completed; available abstract and the 2022 citation were checked, but stronger implicit coverage remains possible. No general finite-sample inequality for unequal parts is claimed.

Self-review: passed. Independent audit: not yet performed.
