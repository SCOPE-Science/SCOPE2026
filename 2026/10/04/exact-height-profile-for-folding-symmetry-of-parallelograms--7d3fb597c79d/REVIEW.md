# Review

## Correctness

PASS. The published corrected parallelogram formula reduces the problem at fixed normalized height to
\[
\max\left\{
\frac1{1-d+\sqrt{1-h^2}},
\sqrt{d^2+h^2},
1-d
\right\}.
\]
The first two terms increase with \(d\), while the third decreases, so the unique minimum is the first crossing of the decreasing term with either increasing term. Both crossings are solved exactly. Their order changes precisely when
\[
s^3-2s^2-4s+4=0,
\qquad
s=\sqrt{1-h^2},
\]
whose derivative is negative throughout \((0,1)\), giving a unique threshold. The branch formulas, uniqueness, strict increase, and quadratic expansion follow directly.

The packaged checker independently re-evaluates the three fold terms at the claimed optimizer, verifies the phase balance, compares against fine shear-grid minimization, and checks the asymptotic coefficient. The analytic monotone-crossing argument proves the continuum result.

## Originality

PASS with a stated residual risk. The current primary source was inspected through its three-case parallelogram analysis, corrected exact formula, and golden-ratio extremal argument. It fixes the shear and sends the height to zero; it does not state a fixed-positive-height profile, a unique optimal shear depending on height, or the three-way transition.

The earlier parallelogram paper was inspected through its definition, normalization, and two-candidate formula. The later paper itself documents that an omitted third fold invalidates the older sharp constant. Neither inspected paper contains the profile proved here.

Targeted semantic-index and public searches used fixed-height, normalized-height, golden-ratio stability, exact branch expressions, and folding-symmetry terminology. No equivalent statement was located.

## Value

PASS. The sharp parallelogram lower bound is unattained and is approached only through degeneration, so a natural next question is how symmetry deteriorates when degeneracy is quantitatively forbidden. Normalized altitude is the canonical similarity-invariant thickness parameter for this family. The result gives the full sharp stability curve, the unique optimal shape at every height, and a nontrivial phase transition between active fold mechanisms. Its small-height expansion supplies the optimal quadratic stability scale around the known golden-ratio infimum.

Same-model review: passed. Independent audit: not yet performed.
