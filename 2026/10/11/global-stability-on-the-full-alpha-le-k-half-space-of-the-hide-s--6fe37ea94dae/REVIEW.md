# Same-system scientific review

## Correctness

**PASS.** The proof was reconstructed directly from the stated HSA vector field. For
\[
V=\alpha x^2+\left(y-\frac{\alpha}{k}\right)^2+\alpha\beta z^2,
\]
the cubic terms and the \(xz\) terms cancel identically, leaving
\[
\dot V=-\frac{2\alpha(k-\alpha)}{k}x^2
-2k\left(y-\frac{\alpha}{k}\right)^2
-2\alpha\beta b z^2.
\]
For \(0<\alpha<k\) this is negative definite. At \(\alpha=k\), the largest invariant subset of \(\{y=1,z=0\}\) is the equilibrium because \(\dot z=x\) there. Properness of \(V\) gives compact forward-invariant sublevel sets, so the global LaSalle argument is complete.

## Originality

**PASS.** The closest primary source, Li (2022), proves global stability only under \(k>\alpha\) together with
\[
k(\alpha\beta-1)^2+4\alpha b(\alpha-k)<0.
\]
The new weight \(\alpha\beta\) on \(z^2\) removes the cross term responsible for that restriction. Same-system integrability and bifurcation papers were compared at the level of their statements and do not dominate this result. The original 1996 model paper was not available for whole-document inspection, which remains a stated residual literature risk.

## Value

**PASS.** Replacing a parameter-dependent quadratic-form condition by the full closed half-space \(0<\alpha\le k\) materially sharpens the global stability map. It also supplies an immediate exclusion of periodic or chaotic attractors throughout that region and covers the boundary omitted by the published theorem.

## Closest literature and limitations

The 2022 stability theorem is the closest result and is strictly weaker as a sufficient condition. The 2007 work emphasizes bifurcation transitions and coexistence of attractors, while the 2014 and 2025 same-system papers concern integrability, invariant algebraic surfaces, and related global structure. The new theorem does not claim necessity and says nothing about the global dynamics for \(\alpha>k\).

Same-model review: passed. Independent audit: not yet performed.
