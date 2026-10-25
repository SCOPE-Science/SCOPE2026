# Independent mathematical audit

## correctness

PASS

Poissonization of the discrete one-coordinate Bernoulli refresh chain makes coordinate update clocks independent rates w_i. Starting all zero, target probability q^m prod_i(1-e^{-w_i t}); starting all one, q^m prod_i(1+r e^{-w_i t}) with r=p/q. Strong Markov first-passage convolution at the all-one target implies exact Laplace-resolvent ratio, whose inclusion-exclusion expansion gives the claimed PGF for s=(1-z)/z. Both transforms have 1/s poles; the finite constant terms yield E N=Σ_{S!=∅}(r^|S|-(-1)^|S|)/w_S, including p=0. Independent m=3 nonuniform rational absorbing-chain solution at weights (1/2,1/3,1/6), p=2/5 yielded mean 919/54 matching direct subset sum. For fixed t, log(1+r e^{-w_i t}) is convex (constant if r=0), while log(1-e^{-w_i t}) is strictly concave for w_i>0; Karamata gives strict Schur-convexity of integrand and expected hitting time, so uniform unique minimizer. The geometric success-block lower bound proves finiteness for positive weights. This covers all finite m, positive weights, 0<=p<1; does not claim stochastic order of the law.

## originality

PASS

Aggarwal–Garoni 2025 note and Attrill–Garoni arXiv:2605.14206 use uniform selection. Long arXiv:2605.14511 Section 4 likewise uniform selected-type refresh; its nonuniform Section 3.6 is a different global-reset model. Anceaume et al arXiv:1504.03878 prove weight optimization for MONOTONE collector, which does not directly imply strict balancing under loss. Compared nonuniform heat-bath product chains, nonmonotone coupon models and monotone analogues; same basic process with unequal weights is not covered by named uniform papers. General Markov/Poissonization techniques are classical and credited; no inspected dominating prior theorem provides ratio-of-resolvents and strict majorization for all p>0 and nonuniform w.

## value

PASS

In a natural actively nonmonotone coupon collection system the sampling probabilities are controllable, and the theorem supplies the exact hitting-time transform and a strict all-parameter balancing optimum rather than an arbitrary small instance. It distinguishes genuine selected-coordinate erasure from monotone or global-reset collection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
