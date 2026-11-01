# Independent mathematical audit

## correctness

PASS

Independent full-rank second-difference rows ensure every subset of active constraints has a strictly complementary KKT input and local Jacobian P_A=I−D_A^T(D_AD_A^T)^−1D_A. Piecewise-linearity of convex-cone Euclidean projection yields global ℓ∞ Lipschitz L_n=max_A max_j Σ_k |(P_A)_(jk)|, with all faces locally attainable. Independent exact rational matrix calculations enumerate all active sets n=2..8: L2=1,L3=4/3,L4=7/5,L5=11/7; at n=5 the unique max is A={1,3}, output index j=3, matrix exactly the displayed 1/35 integer matrix. A strict KKT finite-distance pair gives ratio 11/7, not merely a limiting derivative. Embedding only constraints first and third in any n≥5 provides uniform L_n≥11/7; no sharp equality claimed above 5.

## originality

PASS

Established convex regression research studies Euclidean risk and geometry, but its ℓ² contraction does not determine the sharp mixed-metric ℓ∞ amplification 11/7 or first interior/disconnected active-pattern boundary. The closest exact max-norm projector result operates on a different linear simplex object. Exact active-set computation and finite-distance attainment give a nontrivial new sharp optimization in a natural projection family; best-of-knowledge with older approximation-operator alias risk.

## value

PASS

The first sample size at which sharp convex-regression ℓ∞ error amplification arises at an interior index from separated active constraints is a natural structural cutoff. The exact five-point norm, unique maximizing face and finite-distance witness supply useful deterministic stability information unavailable from standard statistical squared-risk or Euclidean contractivity results. The persistence bound in larger dimensions shows this is not an isolated accident of five samples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
