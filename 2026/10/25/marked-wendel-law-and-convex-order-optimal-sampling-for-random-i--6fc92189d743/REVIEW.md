# Self-review: marked Wendel law and optimal radial sampling

## Correctness — PASS

The event that the sampled convex hull misses the center is equivalent, in the planar strictly convex symmetric model, to a unique circular spacing exceeding half a full turn. Conditional on its unique first endpoint, the remaining samples have the exact truncated angular law; its maximum produces the displayed exponential angular shortfall. The chord between the extremal endpoints is a support edge and, in the small-shortfall regime, is the nearest part of the hull. Its signed distance has first-order coefficient \(r(\theta)/2\). A uniform exponential bound on the angular shortfall proves uniform integrability and all fixed moment limits. Conditional Jensen's inequality, plus the normalization of \(f\), proves the unique convex-order optimizer. The proof handles the normalization, scale and boundary cases; finite checker results are corroboration only.

## Originality — PASS relative to checked material

Wendel's full 1962 article gives the binary probability of being in a halfspace/hemisphere, not the conditional clearance distance. Liu and Yang's full 2014 note gives an exact nonzero clearance probability when sites are sampled in the **interior of a Euclidean disk**; its Theorem 3.1 does not imply the general symmetric-oval boundary model, sampling-density-invariant conditional mean, or its sharp convex-order sampling optimizer. Tikhomirov's 2023 theorem strengthens Wendel-style containment under discrete-coordinate distributions, not the distance-conditioned geometry. A public research-index search on center clearance, noncontainment margins, angular overshoots, the exact circle tail and optimal radial sampling disclosed no stronger or equivalent statement. The accessible historical claims of related random cyclic-polygons, near-boundary hull containment, optimal perimeter/area sampling and regular-polyhedron sections do not imply this theorem. Remaining risk: another paper could develop a marked planar Wendel law under different terminology; historical priority is not certified.

## Mathematical value — PASS

The exact Wendel probability measures only the frequency of center exclusion. The new conditional law quantifies *how far* the hull misses the center at its natural inverse-sample scale. It identifies a nontrivial geometry-dependent exponential mixture, proves an unexpected density-invariant mean, and finds a unique sampling law minimizing every convex risk functional of the limit. The result is a full theorem across smooth centrally symmetric convex ovals, rather than a numerical special case or routine threshold computation.

## Scientific limitations

The theorem assumes \(C^2\) strict convexity, central symmetry, and a positive \(C^1\) angular density satisfying antipodal symmetry. It is not an interior-point or higher-dimensional theorem. The included exact circle tail and Wendel miss probability are calibration facts, not claims of priority. Independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
