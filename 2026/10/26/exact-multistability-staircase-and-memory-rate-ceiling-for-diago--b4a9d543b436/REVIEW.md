# Independent mathematical audit

## correctness

PASS

I rechecked the complete repaired RESULT.md and SLOGAN.txt in /workspace/repairs/1/. Scalar opposite-sign returns satisfy a memory consistency relation ruling out unequal magnitudes; each crossed coordinate contributes zero or ±(h/2−ε/a) and the global sign quotient gives the credited census, with no additional coordinate option at equality. The active half-return block has determinant β and trace s=−1+3β+2(1−β)/q, q=ha/(2ε)>1; conjugation by the sign flip gives its square as the return derivative. The three strict Schur inequalities hold on 3β−1<s<1+β. At zero the relative derivative follows from the O(|x|√v⁺) error term, so the frozen text's 'every cycle' smoothness description is corrected: only all-active cycles have strictly positive memory in all coordinates. The repaired proof supplies the two zero-coordinate multipliers, a local expansion/contraction argument in the actual state space, and the product count of 2^(k−1) attracting cycles off threshold equalities. At their positive-memory states the implicit function argument persists under small symmetric Hessian perturbations. The determinant lower bound is attained exactly at |s|≤2√β; monotone s(q) gives the stated q_− and q_+ (finite upper edge only when β<1/9). The intersection of the rescaled bands is precisely the inclusive curvature cutoff; if empty, the spectral radius stays strictly above β even at the infimum by its endpoint limits and continuity. Replay: python /workspace/checks/1.py (SymPy symbolic Jacobian and exact samples). At β=1/16 it gives endpoints 10/7 and 6, ratio 21/5; a mixed cycle with h=3, ε=1 and curvatures 1 and 3/5 has radius 16/25 even though its nonzero block is on the plateau. Frozen verify.py and its output were read, not executed. The spectral optimum concerns all-active cycles, not critical boundary stability, a mixed-orbit global optimum, or a uniform pure-power norm estimate.

## originality

PASS

The frozen originality assessment was too broad: the exact total orbit census is already covered as an immediate corollary of Loh et al. Theorem 5.2, even if the specialized formula is not printed. The complete repair explicitly credits that result, the sign-symmetry factorization and the prior near-threshold and large-step branches, and claims only the surviving exact diagonal full-step stability and sharp all-active spectrum/curvature gate. These were not supplied or subsumed by the strongest inspected statements. PASS applies to that repaired contribution, not to the original novelty claim for the census.

## value

PASS

The repair isolates the exact attractor count at all noncritical stepsizes and the sharp attainable local linear rate for the diagonal family. The coupled condition-number bound gives an actionable distinction between an individual block's optimal rate and joint attainability at a single stepsize. This remains useful beyond known existence and near-threshold stability, without counting the prior orbit census as an independent contribution or implying global attraction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
