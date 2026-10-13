# Review of A rational-point correction to an affine-complement criterion

## Correctness
**PASS.** The explicit example is self-contained. The quadratic graph map has no base point, the collision determinant is \(u^3+uv^2+v^3\), the cubic \(t^3+t+1\) is irreducible over \(\mathbf Q\), and its discriminant is \(-31\). Therefore the one closed collision point over \(\mathbf Q\) splits into three reduced complex points. Compactly supported Euler characteristic then gives \(3\) for the complement, excluding \(\mathbf A^2\).

For the general necessity, base change preserves an affine-space isomorphism, while the collision-count inclusion-exclusion formula makes the geometric Euler characteristic equal to the number of geometric collision points. In characteristic zero, one geometric collision point is necessarily rational. For sufficiency, once that point is rational, the ruled-surface blowups and the subsequent affine-bundle trivializations in the initiating proof are defined over the base field.

## Originality
**PASS.** The closest source is arXiv:2608.27341v2 itself. Its inspected statement gives the condition \(e=d\pm1\) and \(r=1\), with \(r\) introduced from the support of the collision torsion sheaf, but the inspected text does not state a rational-point qualification or the cubic graph counterexample. Searches for the exact source, closed-versus-geometric point aliases, ruled-surface formulations, and the explicit cubic example returned no equivalent published finding. The available prior findings also contain no overlapping claim.

The main residual risk is terminological: if the author's word “point” is intended to mean geometric point, this result should be read as an explicit descent clarification rather than as a contradiction of the intended theorem.

## Value
**PASS.** The distinction is mathematically consequential because the theorem is presented over arbitrary fields. A single non-rational closed collision point can satisfy the literal closed-support count while producing several geometric intersections and a complement with the wrong Euler characteristic. The corrected characteristic-zero condition is directly usable and the example is minimal enough to serve as a test case.

## Closest literature and limitations
The initiating source is Remy van Dobben de Bruyn, “Divisors in projective bundles over the projective line whose complement is affine space,” arXiv:2608.27341v2. The present claim does not challenge its algebraically closed case or its Jacobian-counterexample application. It proves the corrected equivalence only in characteristic zero and leaves imperfect positive-characteristic descent open.

Self-review: passed. Independent audit: not yet performed.
