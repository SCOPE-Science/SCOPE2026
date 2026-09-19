# Review: Exact amplitude energy obstructs the claimed Hopf–Langford torus bifurcation

Same-model review: passed. Cross-model review: not yet performed.

## Correctness

**PASS.** The source vector field is rotationally symmetric. Direct substitution of \(x=r\cos\theta\), \(y=r\sin\theta\) gives the exact equations \(\dot r=r(\mu-\alpha+z)\), \(\dot\theta=\beta\), and \(\dot z=\mu z-\gamma(r^2+z^2)\). The claimed small periodic solution is therefore represented by an exact amplitude equilibrium whenever \(b^2>0\).

For \(\gamma>0\), the change \(w=r^\gamma\) converts the planar amplitude system into
\[
\ddot w-T\dot w=\gamma^2b^2w-\gamma^2w^{1+2/\gamma},
\]
with \(T=(2\gamma+1)\mu-2\gamma\alpha\). The displayed potential gives \(E'=T\dot w^2\) identically. For \(T\ne0\), this strict sign law contradicts compact invariant circles of the angular Poincaré map by an extremum argument. For \(T=0\), the positive-amplitude equilibrium is a nondegenerate minimum of the potential, giving a continuum of nearby closed amplitude curves and hence suspended invariant tori. The Jacobian and Floquet formulas independently give the same exact unit-modulus condition \(T=0\).

The concrete family \(\alpha=\varepsilon\), \(\beta=1\), \(\gamma=1\), \(\mu=\nu\varepsilon\) satisfies the source hypotheses near \(\nu=2/3\). Substitution into the source's displayed equation (7) yields \((8\pi^2-2)/27\) for its first curve correction, while the exact trace condition gives zero. Symbolic verification reproduces these identities and the hypothesis values \(1/9\) and \(-8/9\).

Adversarial checks considered whether a stroboscopic invariant circle might survive even though the continuous amplitude flow has no periodic orbit. The stronger energy increment formula for the full time map excludes this: on any invariant circle away from the fixed point, \(E\) would have to increase (or decrease) strictly after every iterate, contradicting its maximum (or minimum) on the compact circle.

## Originality

**PASS, qualified to the best of our knowledge.** The general dimensional reduction is prior. In particular, Vassilev–Nikolov (Axioms 2025) explicitly derive an autonomous amplitude system plus \(\dot\theta=\beta\), and one of their integrability conditions maps exactly to the trace-zero surface used here. Yang–Yang (2018) and Nikolov–Vassilev (2021) are also highly relevant older Hopf–Langford papers and discuss exact periodic solutions, amplitude centers/annuli, or integrable cases. These are explicitly excluded from the novelty claim.

The reviewed source arXiv:2609.18010v1 nevertheless states a generic Neimark–Sacker theorem for this specific four-parameter subfamily, with a unique torus on one side of a computed curve and a strictly positive first Lyapunov coefficient. Searches by the arXiv identifier, exact title, Hopf–Langford/Neimark–Sacker terminology, torus bifurcation, first integrals, and equivalent amplitude-system language found no public correction of that theorem and no SCOPE record covering the same source-specific contradiction. The new claim is limited to the exact obstruction and counterfamily showing that the stated theorem and displayed curve are incompatible with the exact dynamics.

Residual risk remains because the full texts of Yang–Yang (2018) and Nikolov–Vassilev (2021) were not inspected. They may contain an equivalent no-cycle or center statement in broader notation. That would reduce novelty of the mechanism, but not the source-specific observation that the 2026 theorem's curve and nonzero Neimark–Sacker coefficient conflict with the exact reduction unless an earlier publication already makes precisely that correction.

## Value

**PASS.** The result changes the mathematical interpretation of the main theorem of a current preprint. It replaces a perturbative generic Neimark–Sacker picture by an exact dichotomy: strict energy monotonicity off a codimension-one surface and conservative center dynamics on it. It also gives exact periodic-orbit and Floquet formulas and an explicit parameter family satisfying the paper's hypotheses for which the claimed curve is asymptotically displaced from the true unit-modulus surface. This is directly actionable for correction of the theorem and numerical examples.

## Limitations

The proof addresses the four-parameter system written in arXiv:2609.18010v1 with \(\gamma>0\), \(\beta\ne0\), and a positive off-axis amplitude. It does not extend automatically to generalized Hopf–Langford systems with extra polynomial terms, nor does it classify dynamics on the symmetry axis or for \(\gammma\le0\). No claim of independent validation is made.
