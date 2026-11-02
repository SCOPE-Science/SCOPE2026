# Scientific review

## Correctness — PASS

The Gram matrix is exactly the cyclic tridiagonal matrix \((4I+S+S^{-1})/6\); the periodized Green sequence \(\sqrt3(-r)^{|j|}\) solves the cyclic inverse system. The local kernel is affine on each cell, so its exact absolute integral is the stated \(F\), and convexity moves the endpoint norm to a knot. The infinite Green kernel has exactly \(L^1\) norm \(2\). Periodization gives the universal upper bound, opposite-sign alias contributions give a strict finite-period inequality, and the geometric tail proves convergence with a quantitative rate. Kernel sign functions establish attainment. The supplied exact arithmetic checker passed 1,041 finite checks; the proof covers every integer \(n\ge3\) independently.

## Originality — PASS, with specific residual risk

Passenbrunner, *Orthogonal projectors onto spaces of periodic splines* (2016 arXiv), Theorem 1.4 and its proof, provides existence of a degree-dependent uniform constant for arbitrary periodic knots, not a finite-size value or the sharp constant \(2\). Shadrin (2001) provides general interval bounds; Foucart (2008) discusses the nonperiodic variable-knot supremum, citing Malyugin's resolution for linear splines; Kayumov (2004) reports the unrestricted linear-spline benchmark \(3\). These imply neither the exact periodic equispaced \(L_n\) nor strictness and exponential convergence in knot count. Searches in the available mathematical record and accessible local claims found no matching statement. Risk: an earlier specialized circulant finite-element mass-matrix or cardinal-spline calculation might be equivalent, and Kayumov's complete text was not accessible for inspection.

## Mathematical value — PASS

The \(L^\infty\) norm of an \(L^2\) spline projector is the sharp stability coefficient governing near-best uniform approximation and worst-case pointwise amplification. The result identifies the exact rational constant for every mesh size, proves a strict improvement from the classical unrestricted-knot benchmark to the equispaced periodic geometry, and quantifies the mesh-size defect exponentially. Sharp sign extremizers and exact positivity loss make the assertion more informative than a general uniform-boundedness result or a tridiagonal-inverse identity alone.

## Closest literature and limitations

The decisive comparison is with Passenbrunner's periodic boundedness Theorem 1.4 (arXiv:1608.06720), together with Foucart's discussion of the nonperiodic degree-one case and Shadrin's general result. The exact bound is not claimed for unequal knots, higher degree, or other sampling measures. Independent examination of older specialized uniform-spline literature remains desirable.

Self-review: passed. Independent audit: not yet performed.
