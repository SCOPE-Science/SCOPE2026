# Review: Exact amplitude energy obstructs the claimed Hopf–Langford torus bifurcation

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** Direct cylindrical reduction gives \(\dot\theta=\beta\) and an autonomous planar amplitude system. For the positive off-axis equilibrium corresponding to the periodic orbit, the exact transverse trace is
\[
T=(2\gamma+1)\mu-2\gamma\alpha.
\]
The transformation \(w=r^\gamma\) gives a scalar constant-damping equation with exact energy law \(\dot E=T\dot w^2\). Thus, for \(T\ne0\), the full angular return map strictly raises or lowers \(E\) away from the fixed point, excluding a compact invariant circle by an extremum argument. For \(T=0\), the positive equilibrium is a strict minimum of the potential and is surrounded by closed amplitude levels, producing a continuum of suspended invariant tori. The Jacobian/Floquet calculation independently gives the same unit-modulus surface.

The explicit family \(\alpha=\varepsilon\), \(\beta=1\), \(\gamma=1\), \(\mu=\nu\varepsilon\) satisfies the source hypotheses near \(\nu=2/3\). The source's displayed equation (7) yields first correction \((8\pi^2-2)/27\), while the exact trace condition yields zero. Symbolic verification reproduces the reduction, energy identity, Floquet condition, source-hypothesis values \(1/9\) and \(-8/9\), and the curve discrepancy.

## Originality

**PASS, qualified to the best of our knowledge.** The general polar reduction, exact periodic solutions, and integrable/center mechanisms are prior and are not claimed as new. In particular, Vassilev–Nikolov (2025) explicitly derive an amplitude reduction for a broader Hopf–Langford family, and one of their integrability conditions maps to the trace-zero surface used here. Yang–Yang (2018) and Nikolov–Vassilev (2021) are also highly relevant older references.

The new claim is restricted to the source-specific correction of arXiv:2609.18010v1: its stated generic Neimark–Sacker theorem and displayed bifurcation curve conflict with the exact amplitude energy law and exact Floquet surface. Searches by source identifier, title, equivalent dynamical terminology, and the SCOPE repository found no public correction covering this contradiction.

Residual risk remains because the full texts of Yang–Yang (2018) and Nikolov–Vassilev (2021) were not inspected. They may contain an equivalent broad no-cycle or center statement, which would reduce novelty of the mechanism but not by itself establish that the 2026 theorem and its curve were previously corrected.

## Value

**PASS.** The result changes the interpretation of the main torus-bifurcation theorem of a current preprint. For the stated vector field, a perturbative generic Neimark–Sacker picture is replaced by an exact dichotomy: strict energy monotonicity off a codimension-one surface and conservative center dynamics on it. The explicit admissible parameter family directly identifies the first-order displacement of the source curve from the exact unit-modulus surface.

## Limitations

The result applies to the four-parameter system of arXiv:2609.18010v1 with \(\gamma>0\), \(\beta\ne0\), and positive off-axis amplitude. It does not automatically extend to generalized Hopf–Langford systems with additional terms, nor does it classify the symmetry axis or \(\gamma\le0\). No claim of independent validation is made.
