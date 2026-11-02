# Scientific review

## Correctness

**PASS.** The homogeneous quartic is \(F=x_1x_2x_3x_4+Q^2\), where \(Q=\sigma_1^2+\sigma_2\). Its Jacobian equations are exactly \(\prod_{j\ne i}x_j=0\), giving twelve singular points with two nonzero coordinates and primitive cubic-root ratios. The exact completed local equation \(w^2+uv\) at each proves the ordinary-node assertion. On any noncoordinate contained line, evenness of the zeros of the product of the four restricted coordinate forms enforces two proportional pairs; coefficient comparison then forces both pair ratios to solve \(z^2+z+1=0\). This proves that the twelve paired lines and eight coordinate-plane lines exhaust **all geometric lines**, not only those over a finite field.

The four coordinate planes yield their two lines by factoring the ternary quadratic. The forty line-node incidences are determined explicitly (eight lines through three nodes, twelve lines through two nodes); twelve nodes each incident to four lines give seventy-two nodal line pairs. Every remaining finite incidence is checked by a standalone exhaustive algorithm over \(\mathbb F_4\): the checker constructs all 357 projective lines, selects exactly twenty, compares all 190 distinct pairs, and certifies twenty-two *distinct* smooth crossings, of which four are rational over \(\mathbb F_2\). Frobenius exchanges the twenty lines in ten conjugate pairs; because the reduced support is finite and the base field perfect, the reduced Hilbert scheme is ten copies of \(\operatorname{Spec}\mathbb F_4\). The computation confirms rather than replaces the infinite-field classification proof.

## Originality

**PASS, with residual historical-priority risk.** The motivating literature determines the symmetric quartic equation and its twelve-node singularities, while earlier related work determines singular schemes for general \(\prod_i x_i+Q^2\). Neither supplies, in the inspected material, a twenty-line classification or the precise pairwise incidence and Frobenius data for the specified prime-field symmetric member. Searches for the exact equation, quartic lines, characteristic-two 12-node line Fano schemes, geometric equivalences, and Frobenius orbits did not identify a dominating theorem. The distinctions are at the level of mathematical implications: classification of twelve isolated nodes places no determination on every line not passing through a node and does not determine the line-Hilbert support or intersections at smooth points. Coverage in unindexed old literature remains possible; no negative search result proves absolute priority.

## Mathematical value

**PASS.** Lines on nodal quartic K3 models are geometrically meaningful configurations of rational curves. On this canonical fully symmetric representative in the twelve-node boundary, the complete line-Hilbert support, incidences with singularities and at smooth points, and Frobenius descent are natural invariants for studying specializations, curve arrangements, and configurations on the minimal K3 resolution. The degree-two Frobenius orbit decomposition is arithmetic information absent from the twelve-node geometric singularity basket; the twenty-line incidence arrangement is structural rather than an arbitrary numerical slice.

## Closest literature and limitations

F. Catanese, *Singularities of normal quartic surfaces I (char=2)* (arXiv:2106.09988), §4, studies symmetric quartics and singular strata. Catanese–Schütt, *Part II* (arXiv:2110.03078), analyzes singularities and Gauss maps; *Part III* (arXiv:2206.03295), Example 19 and Remark 20, constructs the family as a quartic product plus a squared quadratic. Their node descriptions are prior results. The new assertion is about **contained lines**, not the prior node basket. Historical exhaustive searches are incomplete, and equivalent classical configurations may have been described under a different normalization.

The full possibly nonreduced Hilbert scheme, Picard lattice, and the complete surface automorphism group are not determined here. The finding makes no general claim for arbitrary twelve-node members. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
