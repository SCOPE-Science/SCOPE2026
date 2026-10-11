# A sharp two-orientation spectral trichotomy for the Cartwright–Steger nodal twists
## Finding
Let \(F\) be the genus-\(19\) Albanese fiber in Akhmedov–Yeung's Cartwright–Steger fibration, let \(S\) be its order-three symmetry, and let \(c\) be the vanishing cycle considered there. Put
\[
v_i=S_*^i[c],\qquad m=v_0\cdot v_1\in\mathbb Z,
\]
so cyclic symmetry gives \(v_0\cdot v_1=v_1\cdot v_2=v_2\cdot v_0=m\). Define the two cyclicly ordered products
\[
M_+=T_{v_0}T_{v_2}T_{v_1},\qquad
M_-=T_{v_0}T_{v_1}T_{v_2}
\]
on \(H_1(F;\mathbb Q)\). Then their nontrivial quadratic characteristic factors have traces
\[
a_+(m)=2-3m^2-m^3,\qquad a_-(m)=2-3m^2+m^3.
\]
There is an exact integer trichotomy.

If \(|m|\le1\), both quadratic factors have all roots on the unit circle. If \(|m|\in\{2,3\}\), exactly one of the two quadratic factors has all roots on the unit circle and the other has a real reciprocal pair off the unit circle. If \(|m|\ge4\), both quadratic factors have real reciprocal roots off the unit circle, and each associated spectral radius is at least
\[
9+4\sqrt5.
\]
The lower bound is sharp: for \(m=4\), the \(M_-\) factor has trace \(18\), while for \(m=-4\), the \(M_+\) factor has trace \(18\).

Equivalently, using Akhmedov–Yeung's identity
\[
m=1+\operatorname{tr}(S_*T_{[c]}),
\]
both orientations are unit-circle exactly when \(\operatorname{tr}(S_*T_{[c]})\in\{-2,-1,0\}\); exactly one is unit-circle when that trace belongs to \(\{-4,-3,1,2\}\); and both have spectral radius at least \(9+4\sqrt5\) on the nontrivial quadratic factor for every other integral trace value.

## Assumptions and scope
The statement uses exactly the cyclic ordering and homological conventions of Proposition 5.1 of arXiv:2610.01467v1. The integer \(m\) is the algebraic intersection number of the source's transported vanishing-cycle classes. The conclusion concerns only the eigenvalues of the induced action on rational first homology. It does not assert that either mapping class is pseudo-Anosov, finite order, or semisimple in the repeated-root cases.

The source does not determine the actual value of \(m\). Accordingly, this is a conditional classification of every possible integral value of the unresolved intersection parameter, not a determination of which row occurs for the Cartwright–Steger fibration.

## Proof
Proposition 5.1 of arXiv:2610.01467v1 gives
\[
\det(zI-M_+)=(z-1)^{36}\bigl(z^2-a_+(m)z+1\bigr),
\]
with \(a_+(m)=2-3m^2-m^3\), and states that reversing the cyclic product replaces \(m\) by \(-m\). Therefore
\[
\det(zI-M_-)=(z-1)^{36}\bigl(z^2-a_-(m)z+1\bigr),
\]
where \(a_-(m)=a_+(-m)=2-3m^2+m^3\).

For a real number \(a\), the roots of \(z^2-az+1\) lie on the unit circle exactly when \(|a|\le2\). When \(|a|>2\), they are real reciprocal numbers and the larger modulus is
\[
\rho(a)=\frac{|a|+\sqrt{a^2-4}}2.
\]
Thus it remains to classify the integral values of \(m\) for which \(|a_\pm(m)|\le2\).

For \(a_+\), direct evaluation gives
\[
(a_+(-3),a_+(-2),a_+(-1),a_+(0),a_+(1))=(2,-2,0,2,-2).
\]
For \(m\ge2\),
\[
a_+(m)=2-m^2(m+3)\le2-4\cdot5=-18.
\]
For \(m\le-4\), write \(n=-m\ge4\). Then
\[
a_+(m)=2+n^2(n-3)\ge2+16=18.
\]
Hence \(|a_+(m)|\le2\) exactly for \(m\in\{-3,-2,-1,0,1\}\). Replacing \(m\) by \(-m\) shows that \(|a_-(m)|\le2\) exactly for \(m\in\{-1,0,1,2,3\}\). Their intersection is \(\{-1,0,1\}\), and their symmetric difference is \(\{-3,-2,2,3\}\), proving the first two cases of the trichotomy.

If \(|m|\ge4\), both absolute traces are at least \(18\). Since \(\rho(a)\) is increasing in \(|a|\) for \(|a|>2\),
\[
\rho(a_\pm(m))\ge\rho(18)=\frac{18+\sqrt{18^2-4}}2=9+4\sqrt5.
\]
At \(m=4\), one has \(a_-(4)=18\), and at \(m=-4\), one has \(a_+(-4)=18\), so the bound is sharp. Proposition 5.2 of the same source gives \(m=1+\operatorname{tr}(S_*T_{[c]})\), which translates the three integer ranges into the stated trace criterion.

## Verification
The proof is symbolic and reduces the source's characteristic polynomial to elementary inequalities in one integer parameter. The bundled script `artifacts/verify_spectral_gap.py` is a finite regression check, not the proof: it checks the exceptional sets over a large symmetric interval, the sharp \(|a|=18\) boundary at \(m=\pm4\), and the exact numerical identity \(\rho(18)=9+4\sqrt5\). It prints

`VERIFY_OK both_unit=-1,0,1 exactly_one=-3,-2,2,3 gap=9+4sqrt(5) equality=-4,4`

The infinite statement follows from the monotone inequalities in the proof, not from the finite loop.

## Relationship to prior work
Akhmedov–Yeung derive the two characteristic-polynomial formulas and the trace formula for \(m\), but leave \(m\) undetermined and do not classify the possible spectra as \(m\) ranges over the integers. Their discussion explicitly presents the homological data as a starting point for determining the marked monodromy. The result above extracts a sharp consequence of those formulas: after the seven small values \(-3\le m\le3\), there is no gradual transition. Once both cyclic orientations leave the unit-circle regime, the nontrivial homological spectral radius jumps immediately to at least \(9+4\sqrt5\).

Targeted searches for the Cartwright–Steger monodromy, cyclic products of three Dehn twists, the characteristic polynomial in Proposition 5.1, and the constant \(9+4\sqrt5\) did not locate a published statement of this trichotomy. A separate computation based on the same source gives the eigenspace multiplicities of the order-three symmetry \(S_*\); that statement does not determine \(m\) or imply the spectrum of either nodal-twist product.

## Limitations
The exact geometric value of \(m\) remains unresolved. The theorem therefore does not decide which spectral regime occurs for the actual fibration. At \(|a_\pm(m)|=2\), the quadratic factor has repeated roots; the result makes no claim about Jordan blocks. Spectral information on first homology alone does not determine the Nielsen–Thurston type of the corresponding mapping class.

## References
D. Akhmedov and S.-K. Yeung, *A monodromy relation for the Cartwright–Steger fibration*, arXiv:2610.01467v1, first posted 2026-10-01, especially Propositions 5.1 and 5.2.
