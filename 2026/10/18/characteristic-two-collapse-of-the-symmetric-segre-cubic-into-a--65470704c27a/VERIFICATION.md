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

# Exact verification and proof boundaries

Run `python verify_segre_reduction.py` in the directory containing this file and the script. The script has no nonstandard Python dependencies. It enumerates every projective point and projective line over \(\mathbb F_4\), not an unspecified sample: \(85\) ambient points and \(357\) ambient lines. Exactly \(45\) points and \(27\) lines satisfy the Hermitian cubic equation; precisely three of those lines pass through each of the \(45\) points, yielding \(135\) intersecting pairs and \(216\) skew pairs. It also checks that the four characteristic-two Jacobian quadrics are an invertible linear transform of the four squares, and enumerates the ten singular points for each of characteristics five and seven. The expected terminal marker is `VERIFY_OK`.

The characteristic-two vertex Tjurina length is \(2^4=16\); its graded dimensions are \((1,4,6,4,1)\). The exhaustive finite calculation and the known \(27\)-line theorem together establish that no non-\(\mathbb F_4\) geometric lines were missed. No finite test establishes the assertion for arbitrary primes: the all-prime ten-node and characteristic-three statements follow from the symbolic Jacobian, Hessian, and Frobenius calculations in the proof. The proof makes no claim about the integral normalization or the intrinsic six-point GIT model.

The package includes the exact checker source rather than relying on execution logs. Checks may be repeated in any Python 3 environment; no external database is required for their arithmetic replay.
