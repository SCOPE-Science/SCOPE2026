# Scientific review

## Correctness — PASS
The exact Gramian is diagonal for coordinate inputs under a cyclic permutation, and grouping powers by residues gives the two geometric eigenvalue blocks without approximation. Strict monotonicity in the shorter cyclic gap proves the extreme-eigenvalue and condition-number results; the nonstandard determinant inequality is proved using the positive, strictly concave integral \(\int_0^c\tanh(sx)\,ds\), while the inverse-trace inequality follows from the exact strict convexity of \((1+e^{yx})^{-1}\) on positive arguments. The argument handles odd dimensions, all positive damping strictly below one, every full-cycle finite horizon, and the infinite horizon. The independent exact-rational checker performed 2,210 cases, including direct summation. Finite cases test algebra but are not the infinite proof.

## Originality — PASS, subject to historical risk
Summers and Lygeros (arXiv:1306.2491) prove the general modularity of the Gramian trace; Cortesi, Summers, and Lygeros (arXiv:1403.6351) give general submodularity of control-energy metrics. Enyioha et al. (arXiv:1410.1830, Section IV) explicitly study a closely related directed ring and empirically illustrate why spaced leaders improve minimum-eigenvalue control as the number of nodes grows. Their examined formulation does not contain the simultaneous finite-\(n\) determinant, inverse trace, spectral-condition formulas and unique balanced optimizer classification proven here. Fitch and Leonard (doi:10.1109/ECC.2016.7810511, Section V) optimize a different undirected continuous-time Laplacian model with incompatible Gramian geometry. The earlier qualitative observation of spreading leaders is fully credited. Research searches and examination of these primary texts did not identify a statement covering the proposed exact four-objective theorem; that absence is not a proof of global novelty, and less discoverable specialized results remain a risk.

## Value — PASS
Placement of scarce independent control channels is a natural design question. The classification gives one non-asymptotic placement decision for four inequivalent energy and conditioning objectives, independent of damping and admissible horizon, and provides all exact metric values, not merely a numerical optimizer. The contrast with trace-invariance and with undirected consensus-ring placement reveals genuine structure not contained in the general-purpose selection formulations. A complete natural, sharp class merits use as an exact benchmark even without a broader-network theorem.

## Remaining limits
The finite-horizon assertion assumes a whole number of cyclic traversal periods; arbitrary partial-cycle horizons are excluded. Control columns must be distinct unit coordinate vectors. An equivalent historical specialization cannot be ruled out, and the proof has not received independent audit.

Self-review: passed. Independent audit: not yet performed.
