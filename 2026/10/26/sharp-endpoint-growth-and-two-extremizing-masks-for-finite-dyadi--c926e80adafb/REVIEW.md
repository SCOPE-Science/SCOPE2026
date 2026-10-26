# Review of the finite dyadic level-projection extremal theorem

## Correctness

PASS. Uniform dyadic conditional expectations make the level differences mutually orthogonal projections. Their explicit kernel has a common row distribution and yields an exact absolute row-sum formula. Scaling its prefix sums produces a two-branch Bellman recurrence, whose piecewise-affine solution is proved by induction for all horizons and states. The recurrence gives the closed norm bound and forces exactly two optimizers from depth three onward; depth one and two are handled separately. A separate exact-arithmetic implementation reconstructed kernel rows, maximized all masks through depth twelve, and verified the Bellman envelope independently on a rational grid.

## Originality

PASS within the inspected mathematical sources, subject to stated priority risk. Semenov–Uksusov (2012) proves boundedness criteria with norm-equivalence constants for Haar multipliers, and Osękowski (2013) establishes sharp restricted weak-type inequalities for Haar projections. Neither inspected theorem states the present exact *strong endpoint finite-depth* maximum or classifies its optimizing whole-level masks. Choi (1992) concerns the interior \(L^p\) range. General Walsh spectral projection calculations on other spaces do not imply this binary dyadic tree problem. The full text of parts of the Semenov–Uksusov source remained inaccessible, and historical equivalence under another name is possible.

## Value

PASS. Choosing which resolution levels to retain in a finite multiscale orthogonal decomposition is a natural stability decision. The theorem optimizes over every one of the \(2^n\) binary whole-level selections, identifies every worst selection, and gives an exact finite-size law with a linear growth rate. This is a structurally meaningful distinction: a single level has endpoint norm one, retaining all levels has norm below two, yet alternating levels have unbounded amplification as depth increases. It is a natural complete extremal classification, not a chosen isolated numerical value.

## Scientific limits

The measure is the uniform binary product measure; level masks are constant across every level. Arbitrary Haar-node masks, irregular splitting, and other function-space endpoints are not addressed. Priority is only supported by the material genuinely inspected, not by exhaustive historical certification.

Self-review: passed. Independent audit: not yet performed.
