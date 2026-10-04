# Same-model review

## Correctness
PASS. Invariance of the second coordinate gives the exact marginal identity
\[
(y)_\#\mu=(bx)_\#\mu.
\]
Invariance of the first coordinate gives
\[
a\mathbb E[x^2]+(1-b)\mathbb E[x]-1=0.
\]
Vieta's formulas for the two fixed-point roots then yield
\[
\operatorname{Var}(x)
=(r_+-\mathbb E[x])(\mathbb E[x]-r_-).
\]
Endpoint equality gives a fixed-point atom. If the fixed-point polynomial vanishes on the whole support, support invariance and \(0<b<1\) make the next \(x\)-coordinate a strict convex combination of the two roots unless the previous and current roots agree, so the support reduces to the two fixed points. Otherwise zero expectation of the polynomial forces both signs on positive-measure sets, proving strip crossing.

Risk: the support-rigidity step uses invertibility for \(b>0\) and strict convexity for \(b<1\), which is why the theorem is not stated outside this range.

## Originality
PASS. The complete foundational paper was inspected and gives the map, inverse, fixed points, trapping region, and numerical attractor but no invariant-measure moment theorem. The full open first-bifurcation preprint explicitly studies all invariant Borel probability measures through thermodynamic formalism; targeted searches found no mean-variance, moment, or strip-crossing formulation. Searches over direct and equivalent forms found no same-object implication. The closest indexed statement of similar algebraic shape is a variance-gap theorem for a different continuous-time system.

Risk: the 1991 and 1993 classical rigorous Hénon papers were not available as stable complete text in the inspected paths, and the short expectation identity could have appeared incidentally in older numerical literature.

## Value
PASS. The theorem ties every compact invariant measure to the map's own fixed-point geometry, gives an exact moment consistency curve, classifies its endpoints, and forces every genuinely non-fixed recurrent statistical state to occupy both sides of a natural vertical-strip partition. This is directly applicable to periodic-orbit measures and chaotic invariant measures of a canonical benchmark map.

Same-model review: passed. Independent audit: not yet performed.
