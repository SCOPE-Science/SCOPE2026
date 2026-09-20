# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The source no-hint attack explicitly searches affine pairs \((a,b)\) such that \(ag_i+b\) lies in the value set of a degree-two elliptic function. For a non-2-torsion normalization point, eliminating the curve coordinate gives a quadratic fibre equation whose discriminant is the displayed cubic \(H\). Its polynomial discriminant simplifies to a nonzero scalar multiple of the elliptic-curve discriminant, so \(H\) is squarefree.

For distinct tested values \(h_i\), two translated cubics \(H(ah_i+b)\) and \(H(ah_j+b)\) share a root for at most six nonzero scalings \(a\) per unordered pair. Outside those scalings, every nonempty subproduct is squarefree, so the standard quadratic-character Weil bound applies. Expanding the value-set indicators and treating branch values separately gives
\[
M_m\le q^2 2^{-m}+\tfrac32m q^{3/2}+3m^2q.
\]
The degree-two fibre bound guarantees enough distinct \(g_i\)-values. Summing candidate counts over the first \(L=\lceil\frac12\log_2q\rceil\) sequential tests and then bounding all subsequent work by \(nM_L\) gives the stated deterministic complexity.

A standalone finite verifier checks the exact cubic value-set characterization and exhaustive affine-pair counts for several prime fields. These checks are supplementary; the proof is analytic.

## Originality

**PASS, to the best of our knowledge.** The motivating preprint proves a worst-case \(O(nq^2)\) affine-pair enumeration bound and separately gives an \(O(q^2)\) average estimate under a heuristic independence assumption, explicitly noting that the assumption is not a consequence of its previous statements. The present result replaces that gap with a deterministic character-sum bound. The source does not state the survivor estimate or the \(O(q^2+nq^{3/2}\log q)\) worst-case filter.

Quadratic-character Weil bounds, value sets of low-degree maps, and pseudorandomness results for quadratic residues are prior mathematics and are not claimed as new. Searches by the source title/arXiv identifier and by McEliece/elliptic-code affine-pair, value-set, quadratic-character and Weil-bound formulations found no inspected prior application giving this attack bound. No inaccessible paper was identified as especially likely to contain the same refinement. The source preprint is extremely recent, so contemporaneous or not-yet-indexed work remains a residual originality risk.

## Value

**PASS.** The result converts a specifically heuristic part of a newly proposed structural cryptanalysis into a rigorous worst-case guarantee and improves the proved dependence of that stage on \(q\) by a square-root factor up to logarithms when the code length is large. It also exposes the exact finite-field pseudorandom object governing the search: an affine pattern inside the quadratic-character value set of a cubic.

The contribution is deliberately not advertised as a universal improvement to the full attack, because other algebraic stages can dominate for some parameter choices.

## Limitations and residual risks

The clean theorem is stated in characteristic greater than \(3\), matching the main practical case treated by the source, and uses a non-2-torsion normalization point. The full attack's filtration and second-divisor recovery costs are unchanged. The survivor estimate is an upper bound and may be far from sharp; experiments suggest much smaller counts in typical examples. No optimal lower bound for the affine search is proved. Originality remains only to the best of our knowledge.
