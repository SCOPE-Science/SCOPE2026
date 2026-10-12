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

The proof is analytic for every \(n\ge2\).

`checker.py` performs two exact supplementary replays. For many \(n,k,\ell\), it enumerates assignments of the four signed frequencies to sample indices and verifies that the expected product count is \(n^2\) for distinct harmonics and \(2n^2-n\) for equal harmonics. Commensurate cases such as \(\ell=2k\) are explicitly included.

The checker also evaluates Watson's usual ordered-sample formula and the equivalent periodic Bernoulli-kernel formula on rational samples using exact rational arithmetic. This verifies the normalization of the Fourier representation without truncating an infinite series.

The zeta evaluations and the universal covariance formulas are proved symbolically in `RESULT.md`; finite checks are not used as evidence for an infinite statement.
