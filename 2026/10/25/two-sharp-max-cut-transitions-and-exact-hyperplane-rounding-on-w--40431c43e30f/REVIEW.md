# Self-review

## Correctness (C): PASS

The finite weighted graph and the ordinary elliptope SDP are normalized edge by edge. The Fourier eigenvalues are exactly \(2\cos(\pi k/n)+t(-1)^k\), the trace eigenvalue bound is attained by explicit real unit Gram factors, and equality characterizes the Gram matrix when the smallest eigenspace is one- or two-dimensional. The cycle-cut parity argument proves the integer optimum for every integer \(n\ge3\), including \(t=0\). At the spectral transition uniqueness is deliberately not asserted. A discrete-circle halfspace count proves the all-generic-hyperplanes statement; monotonic ratio comparisons give the sharp worst parameter. The included separate brute-force, Fourier and rounding checks passed.

## Originality (O): PASS with identified prior coverage and residual risk

Van Dam and Sotirov already prove the spectral-SDP equivalence for walk-regular graphs. The SDP spectral component is not independently new, and this has been disclosed explicitly. The substantive combined result includes the exact parametric integer optimum, separated spectral and integer transitions, uniqueness of the two-dimensional optimal Gram, exact rounding outcome for every generic hyperplane, and the uniquely worst multiplicative ratio. Goemans–Williamson gives the general SDP and random hyperplane rule; the inspected Möbius-ladder benchmark literature provides unweighted cases and broad polynomial-time solvability, not these joint sharp statements. Specific specialized coverage remains possible, especially among older optimization papers on circulants or Möbius ladders.

## Mathematical value (V): PASS

This is a natural parametric benchmark family, appearing in Ising and Max-Cut testing. It distinguishes failure of exactness of a relaxation from failure of its canonical rounding algorithm: for an open weight interval every hyperplane of the unique optimal factor is suboptimal, yet at and beyond the integer support threshold every generic hyperplane is optimal even while a strict SDP gap persists. The gap maximizer and the two different sharp thresholds give useful exact test data, beyond a bare numerical enumeration or re-expression of a general spectral bound.

## Remaining limitations

No arbitrary individual-edge weights, stronger cut inequalities, or robust floating-point rounding guarantee is claimed. The novelty judgment is based on inspected primary texts and actual claim searches, not an exhaustive proof that no earlier equivalent theorem exists. The script tests finite cases; the infinite-family proof is analytic.

Self-review: passed. Independent audit: not yet performed.
