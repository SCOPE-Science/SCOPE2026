# Mathematical review

## Correctness — PASS

The theorem is reconstructed for every integer \(d\ge1\) and every \(0<a\le1/2\), with a full-support Bernoulli-product stationary distribution. Convex orbit averaging reduces any reversible feasible kernel to three transition parameters, without asserting asymmetric uniqueness. Walsh characters give the exact \(2\)-by-\(2\) eigenblocks. A pair of positive-semidefinite sandwich constraints yields the quadratic necessary bound, and a derivative argument excludes every larger vertical flow at a smaller proposed spectral radius. The explicit kernel meets the bound with valid positive holdings and exact detailed balance. The symbolic verifier reproduces the quadratic and determinant identities, and sampled full matrices confirm the formulas. No finite test is used as a proof for all dimensions.

## Originality — PASS on inspected evidence, qualified

The general reversible-chain semidefinite program of Boyd–Diaconis–Xiao (2004) is prior, not new. Boyd–Diaconis–Parrilo–Xiao (2009), §3.2.2, already give the uniform-stationary Boolean-cube optimum, which the current formula recovers at \(a=1/2\); that endpoint is not a novel claim. The added claim is an all-parameter biased-coordinate formula, an explicit state-dependent fair-coordinate transition rule and strict spectral interpolation with a fixed-dimensional rare-layer limit. The consulted Fill–Kahn work addresses order-based/path mixing comparisons; the Collevecchio–Griffiths paper addresses iid Bernoulli-product cube walks and different cutoff objectives, not an unrestricted one-exceptional-coordinate spectral minimax. Indexed record matches on general mixing, hypercubes or Bernoulli products have different objectives or parameter sets. Unindexed specialist overlap remains a genuine possibility, not ruled out solely by search absence.

## Mathematical value — PASS

This is a complete natural parameter-family solution of a semidefinite network design problem, not a single test case. The formula quantifies the full transition between the previously known uniform-cube optimum \(d/(d+2)\) and the effective \(d\)-coordinate cube limit \((d-1)/(d+1)\), and proves every nonzero stationary bias changes the optimal rate strictly. The optimal kernel must adapt its fair-coordinate move probabilities to the biased bit; fixed coordinate-independent flip rates do not exhibit that mechanism. The formula gives directly usable transition probabilities and a sharp spectral benchmark for product-target local samplers.

## Closest evidence and residual scope

- S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph* (2004), https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf: general reversible optimization, especially §§6–7, but not the all-bias hypercube closed form.
- S. Boyd, P. Diaconis, P. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries* (2009), https://web.stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf: §3.2.2 gives the uniform hypercube as a known boundary case, not the nonuniform target.
- J. Fill and J. Kahn, arXiv:1109.6075: comparison order and path-chain results, not this SLEM optimum.
- A. Collevecchio and R. Griffiths, arXiv:2002.09059: iid target and longer-range/time-dependent walks, not the single biased coordinate nearest-neighbor minimax.

The new statement does not classify all nonsymmetric optimal kernels or address nonreversible chains, further biased coordinates or time-specific total-variation distance. An independently performed mathematical audit is absent.

Self-review: passed. Independent audit: not yet performed.
