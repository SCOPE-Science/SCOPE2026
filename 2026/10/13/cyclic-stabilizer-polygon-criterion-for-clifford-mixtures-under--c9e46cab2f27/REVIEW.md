# Self-review

## Correctness — PASS

The result is an exact equivalence for all unit Bloch vectors, all proper rotations, and all probabilities in the closed interval. The proof reconstructs the Bloch matrix, uses its unit-norm input-output direction to force each Clifford summand into a single coset, then identifies the transverse restriction of that coset with a cyclic polygon. Sufficiency is explicit because any point of the polygon supplies convex weights on the corresponding Clifford matrices. Stabilizer orders and the signed-plane inequalities have been checked directly, including both endpoints and the threefold boundary. The phase-gate corollary uses a discrete azimuth classification and is correctly restricted to \(0<p<1\). Independent finite polytope membership optimizations corroborate 88 cases but are not treated as an infinite proof. **Scientific risk:** Incorrectly identifying the Bloch orientation would affect signs; the right-handed transverse-basis formula fixes the orientation, and the polygon is invariant under the representative choice.

## Originality — PASS (with residual indexing risk)

Fioroni–Ferrari–Tirrito, arXiv:2609.16160v1, Appendix C Lemmas 7 and 8, already establish pure-axis rigidity and the continuous circle-moment description. Their Section IV C explicitly leaves the full tilted-dephasing optimization without a closed analytic solution and reports numerical cost plots; this classification is not claimed there. Virmani–Huelga–Plenio, arXiv:quant-ph/0408076, Section IV, establishes aligned-axis stabilizer-octahedron noise thresholds, which are credited rather than claimed new. Buhrman et al. (FOCS 2006) establish the 24-vertex Clifford polytope and depolarizing thresholds, but do not specialize its rigid exposed sections to the four regular polygons. Searches for rotated-axis dephasing, exact Clifford-only mixtures, subgroup-face reductions, and equivalent convex-geometry conditions did not reveal a stronger theorem that implies the all-axis/all-rotation result. **Residual risk:** An unindexed convex-polytope face theorem may subsume the geometric criterion; unsuccessful searches cannot establish absolute novelty.

## Value — PASS

Clifford-only stochastic decompositions are a mathematically motivated boundary for stabilizer-based qubit simulation, not an arbitrary parameter census. The complete decision rule handles the continuous family of axes and preceding rotations with just a finite coset test and one of four inequalities. It converts the source's numerical tilted-dephasing behavior into an exact no-go throughout the strict noise interior and reveals a distinct, nontrivial threefold-axis noise threshold. This goes beyond repeating the known aligned-axis threshold, and specifies sharply the endpoint limitation. It does not claim a general complexity lower bound or optimize nonzero cost.

## Closest literature and limits

Primary source: Fioroni–Ferrari–Tirrito, arXiv:2609.16160v1, especially Sec. IV C and Appendix C (read as a full primary source). Additional primary comparisons: Virmani–Huelga–Plenio, arXiv:quant-ph/0408076, Sec. IV; Buhrman et al., FOCS 2006, Secs. 2–3. The theorem concerns exact mixtures of unitary Clifford channels, not the larger class of Clifford instruments; residual originality uncertainty is limited to possible differently indexed subgroup/polytope results.

Self-review: passed. Independent audit: not yet performed.
