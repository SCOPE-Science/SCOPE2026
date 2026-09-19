# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.** In a one-vertex-separating chamber, the central section is the simplex whose vertices are the intersections of the separating hyperplane with the \(n\) edges incident to the isolated vertex. The pyramid-volume computation gives
\[
A(a)=\frac{\sqrt{n+1}}{(n-1)!}
\frac{a_0^{n-1}}{\prod_{i=1}^n(a_0-a_i)}.
\]
The angular decomposition about the facet normal forces the tangent vector to have zero isolated-vertex coordinate, zero sum on the other coordinates, and unit squared norm. This yields the exact product identity (10) in `RESULT.md`.

At fixed angle, the product factors have fixed arithmetic mean \(1\) and fixed variance. Rodin's sharp variance refinement of AM--GM gives the stated maximal product and equality pattern, so inversion of the product yields the sharp lower profile. The equality vector has \(n-1\) equal positive tangent coordinates and one negative coordinate and is exactly the tangent direction toward a Webb normal. The endpoint, monotonicity, and angle range follow by direct algebra. Differentiating the logarithmic product identity at the facet normal gives the direction-independent second derivative \((2n+1)/(n+1)\).

Independent numerical sanity checks of the geometric section formula and the profile were consistent across dimensions \(2\) through \(8\); these checks support but are not used in the proof.

## Originality

**PASS, to the best of our knowledge.** Ambrus--Gárgyán prove the global minimum and identify facet-parallel minimizers. Webb proves the global maximum. Myroshnychenko--Tang--Tatarko--Tkocz provide stability for Webb's **maximum**, not for the newly solved minimum. Dirksen gives general section formulas and partial lower-bound results. Rodin's sharp fixed-variance AM--GM theorem supplies the finite-dimensional product optimization and is explicitly treated as prior work.

Searches for minimum/minimal central simplex slices, facet-parallel stability, angular stability, fixed-angle section profiles, one-vertex separating chambers, variance/geometric-mean formulations, and the exact motivating arXiv identifier did not locate the theorem in `RESULT.md`. The current Ambrus--Gárgyán preprint is especially relevant and recent. Its indexed abstract and metadata were inspected and describe the exact minimum theorem and proof strategy, but the full text was not available through the sources inspected. Consequently, an equivalent observation in its body, a later revision, or an unindexed parallel result is the principal residual originality risk.

The novelty claim is therefore deliberately limited to the exact chamber-wise fixed-angle profile, its equality arcs and endpoint interpolation, and the isotropic local Hessian. The chamber section formula, ordinary AM--GM, Rodin's product theorem, and the global minimum and maximum theorems are not claimed as new.

## Value

**PASS.** The result adds a sharp quantitative layer immediately adjacent to the newly settled minimum-slicing theorem. It does more than give a nonsharp deficit estimate: for every angular distance allowed by a one-vertex chamber it determines the exact least possible section volume and all equality directions. The equality family geometrically connects the facet-parallel global minimum to the classical Webb global maxima on the chamber boundary. The isotropic Hessian gives an explicit second-order rigidity constant at each facet minimizer.

## Limitations

- The profile is chamber-wise, not global across every sign pattern of the hyperplane normal.
- It does not provide a new proof of the global minimum theorem.
- Rodin's fixed-variance AM--GM extremizer is a prior ingredient.
- The full text of the very recent Ambrus--Gárgyán preprint was not inspected, leaving a concrete originality risk from an equivalent statement in that source or a later revision.
- Cross-model review has not been performed.
