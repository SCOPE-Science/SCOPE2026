# Self-review

## Correctness — PASS
The claim is an asymptotic distribution for a Euclidean sample-diameter deficit, not a finite-sample equality. The proof conditions on fixed positive side lengths, makes the angle dependence explicit, verifies the four-corner Poisson scaling using multinomial probabilities, and applies deterministic localization to the two opposite-vertex pairs. The corner cost is the minimum of two weighted independent exponentials; its combined rate is exactly one for every aspect ratio. The two diagonal costs have disjoint corner processes and are independent shape-two gamma variables. The finite diagonal-length difference tends to the prescribed deterministic shift. A global nearest-arclength bound gives uniformly bounded moments of arbitrary positive order, justifying the limiting mean and second moment. Standalone tests verify the key algebraic normalization and sample-diameter reduction as corroboration.

## Originality — PASS, priority provisional
The primary full texts [1] and [2] concern boundary-sampled convex-polytopal volume/face counts and Hausdorff approximation, respectively. [2, Section 2, equation (9)] already obtains independent Poisson processes at distinct polygon corners; that prerequisite is credited, not claimed new. Its target is a maximum of corner-to-hull distances, whereas the new formula is a minimum of two sums of opposite-corner endpoint losses, with a deterministic near-degeneracy shift. The broader geometric-functional deviation bounds [3] include the diameter but do not give the proposed limiting distribution or angle crossover. No exact competing-diagonal counterpart was located in the searched records. Residual risk: a general extremal diameter theorem might imply this specialization, so independent historical verification remains necessary.

## Mathematical value — PASS
The exact limit law identifies a natural singular transition in a geometric statistic. At a rectangle both geometric diagonals compete, lowering the normalized expected loss from two to \(5/4\); leaving the rectangle by an angular perturbation of order \(1/n\) produces a continuous explicit distributional crossover. The striking cancellation of both side lengths in each corner's exponential rate is a geometric universality statement, and all limiting moments are determined. This is a motivated nonlinear extremal problem, not an arbitrary parametric computation.

## Evidence and limitations
See `RESULT.md` for precise hypotheses, complete analytic argument, source-level comparisons and references; `verify.py` supplies executable diagnostic checks, not proof of the limiting theorem. The result covers fixed side lengths and arclength-uniform independent boundary sampling; no uniformity over collapsing side-length ratios is claimed. The assessment is based on reviewed literature and mathematics and does not establish historical uniqueness.

Self-review: passed. Independent audit: not yet performed.
