---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The certificate is the included, executable `verify.py` program. Run `python3 verify.py` using an ordinary Python 3 interpreter. The program exhaustively computes the orbit partition of every subset of \(\mathbb F_2^k\setminus\{0\}\) for each \(k=1,2,3,4\), checking the complete rank-full Hamming-spectrum map for injectivity. The dimension-four step traverses 32768 candidate subsets and yields exactly 36 distinct rank-full orbit signatures.

For dimension five it checks all 352 normalized rank-full configurations at lengths five, six and seven, each against a canonical orbit label formed by exhaustive ordered-basis normalization, so the 1/4/8 spectral-class counts are exhaustive rather than sampled. It checks the two length-eight matrices, their 31 nonzero word weights, the weight-two preimage rank difference and the 31 rational weight ratios for the explicit isomorphism. The last line of a successful run is `PROJECTIVE_ISOSPECTRAL_DISTORTION_VERIFY_OK`.

The infinite-sounding dimension bound is only through four, where the point set is finite (at most 15 points); no extrapolation beyond that dimension is used. The global length-seven reduction for higher dimensions is a direct MacWilliams/codimension-one argument. The lower distortion bound follows analytically from the distinct dimensions of the minimum-weight spans; enumerating all invertible maps is unnecessary. Independently checking the source-catalogue completeness or priority is outside this computational certificate. No independent audit has been performed.
