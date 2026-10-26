# Mathematical review

## Correctness — PASS
The claim follows from the exact subgradient formula for the two proximal maps, strict synchronous-coupling contraction in Wasserstein distance, an attained finite-word clipping bound in the intermediate regime, an explicit infinite sequence of distinct positive-mass alternating-word images, and a maximal-atom argument in the unclipped regime. The boundary cases \(a=s\) and \(a=b\) are assigned by their actual map formulas. The support/attractor assertion for the standard Bernoulli convolution uses the elementary open-set-condition geometry. Verified code checks algebraic identities but does not stand in for infinitely quantified proof.

## Originality — PASS (qualified by bibliographic uncertainty)
The closest full-text sources concern general randomized proximal last-iterate bounds (Vaidyan–Friedlander–Alacaoglu, 2026), stochastic forward–backward invariant-measure convergence (Hermer–Luke–Sturm, 2023), and incremental proximal methods (Bertsekas). None of their inspected results states the complete three-type clipped proximal phase classification or the least uniform reset word. The affine Bernoulli-convolution support and dimension formulas are classical and explicitly excluded from novelty claims. Search overlap remains a risk because specialized clipped affine iterated-function systems may contain the classification under different terminology.

## Mathematical value — PASS
For a natural Lipschitz component regularizer decomposition of a strongly convex nonsmooth objective, the theorem provides a sharp qualitative invariant-law phase diagram and a computable regeneration length. Stationary probability may be finitely atomic, countably atomic, or nonatomic under the same algorithmic template. Fixed-objective tuning across the explicit two-atom threshold is possible by stepsize alone; the infinite-atom regime represents a nontrivial renewal phenomenon invisible in expected objective rates.

## Limits and closest sources
The classification is scalar, symmetric, iid and exact arithmetic, with deterministic initial states in \([-a,a]\). It is not a theorem for arbitrary proximal schemes or a novelty claim about Bernoulli convolutions. See the primary paper comparison and original references in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
