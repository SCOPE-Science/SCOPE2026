# Independent mathematical audit

## correctness

PASS

For e=x−x*, exact pair minimization subtracts the orthogonal projection in the G^{1/2}e coordinates, so the sharp one-step improvement is the smallest eigenvalue of the projector average. Concavity and leaf-permutation symmetry justify optimizing the orbit mixture without assuming all optimizers are symmetric. The contrast eigenspace and the hub/uniform-leaf block give the stated L, trace T and determinant K; the displayed characteristic polynomial is strictly negative at L for θ>0 (the affine bracket is positive at both endpoints), so the two block roots are distinct and the lower root controls. Its endpoint derivatives are nk>0 and tk/(k−1)<0, and concavity and interior analyticity give a unique interior optimum in this family. Substituting the stationary θ into the polynomial preserves the λ derivative at stationarity, which is negative at the lower block root; this selects the smaller eliminated root. Rationalizing gives Λ/k=2/(2/n+t+2u(n−1)/(n√δ)); the limit gives the stated mass and order. The n=3, u=1/2 example also follows by exact substitution. This is a proof check; the frozen numerical script was inspected, not run, and its endpoint-limit examples are printed comparisons, not asserted tests.

## originality

PASS

The projector formulation and probability-design framework are standard; inspected statements do not cover the star-specific solution of the sharp one-step pair-law problem for n≥3 leaves, including its interior mass and singular-limit scaling.

## value

PASS

The family isolates the effect of one correlated hub on an exact optimal pair design. It answers a quantitative question not settled by symmetry alone: how far to bias the hub and how that preference scales at the positive-definiteness boundary. The n^{-1/2} versus n^{-1} comparison shows an order change, without implying runtime or multistep optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
