# Same-model scientific review

## Correctness
PASS. The upper bound reduces every Banach-space witness to its pair of component norms and uses only the triangle inequality plus coordinatewise monotonicity of absolute norms. The lower bound reconstructs scaled almost-diametral witnesses from octahedrality using norming functionals, with the needed range \(0\le c,d\le1\) supplied by domination of the \(\ell_\infty\)-norm. For the cut-square norm, the positive-sphere optimization collapses exactly to \(\max\{1+\min(c,d),(1+c+d)/(1+t)\}\); the two independent bounds on \(\min(c,d)\) and \(c+d\) are simultaneously attained at the diagonal point. The branch crossing and minimum are elementary consequences of \(t^2+2t-1=0\). The exact-rational checker replays the scalar optimization on rational boundary grids.

Risk: the scalar reduction is specific to the two canonical axis points and should not be read as a formula for arbitrary finite subsets.

## Originality
PASS. The closest primary source, Haller--Langemets--Nadel (arXiv:1702.03140), gives the qualitative equivalence between octahedrality of an absolute sum and positive octahedrality of the two-dimensional absolute norm, and explicitly reduces positive octahedrality to simultaneous equality at the two axis points. The inspected theorem and proof do not provide the exact supremal common value below \(2\), nor do they evaluate the cut-square family. Haller--Pirk--Veeorg (arXiv:2001.06197) reformulates the endpoint condition as a special case of \(A\)-octahedrality but remains qualitative in the inspected material. Targeted published-finding corpus and web searches for the family, the exact formula, the crossing \(\sqrt2-1\), and the value \(1+1/\sqrt2\) found no covering statement.

Risk: an equivalent quantitative lemma may exist under different notation or in unindexed lecture notes/theses.

## Value
PASS. The 2017 preservation theorem leaves a natural quantitative question whenever positive octahedrality fails: how close can the same two endpoint tests come to \(2\)? The theorem answers that question exactly on a simple nested interpolation from \(\ell_1^2\) to \(\ell_\infty^2\), revealing a non-monotone obstruction with a sharp interior worst point. The general scalar reduction is reusable for other absolute norm families, so the result is more than a one-off numerical evaluation.

Risk: the invariant is deliberately local to a distinguished two-point test and is not asserted to control every other quantitative octahedrality notion.

## Closest literature and limitations
The primary comparison is R. Haller, J. Langemets, and R. Nadel, arXiv:1702.03140, especially Section 3, the definition and remark on positive octahedrality, and Theorem 3.2. A later comparison is R. Haller, K. Pirk, and T. Veeorg, arXiv:2001.06197, especially Definition 2.1 and the discussion identifying property \((\beta)\) with \(\{(0,1),(1,0)\}\)-octahedrality. The present result does not claim a full modulus for arbitrary absolute sums or arbitrary finite configurations.

Same-model review: passed. Independent audit: not yet performed.
