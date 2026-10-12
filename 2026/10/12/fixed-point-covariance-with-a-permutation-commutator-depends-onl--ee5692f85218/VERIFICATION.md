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

# Verification

The exact covariance follows from conditional uniform probabilities for one or two pinned images of a permutation, as detailed in `RESULT.md`. Its proof applies to every integer \(n\ge3\) and every deterministic \(\eta\in S_n\), including fixed-point-free and identity boundaries. No infinite theorem is deduced from finite computation.

`verify_commutator_covariance.py` is a standalone Python 3 script with no nonstandard dependencies. Run `python3 verify_commutator_covariance.py` to enumerate every permutation pair for each \(3\le n\le6\), plus three reference permutations at sizes seven and eight. The program checks exact rational means, cross covariances, the sharp integer envelope for each \(3\le n<200\), and a concrete uncorrelated-but-dependent witness. The verified output reads:

`PASS: 876 exact permutation-pair distribution cases, 669492 individual pairs; mean, covariance, maximum, and nonindependence checks`

The finite enumeration and moment tests are consistency checks and do not establish novelty, global independence, an infinite proof, or independent validation. The analytic proof in `RESULT.md` supplies the infinite-domain argument.
