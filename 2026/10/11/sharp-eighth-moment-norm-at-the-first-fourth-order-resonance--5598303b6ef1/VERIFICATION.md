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

Run `python verify.py` in this package. The script reconstructs the degree-four convolution for frequencies \(\{0,1,4\}\), verifies the unique collision, derives the normalized moment quotient and both stationary polynomials, factors the exact resultant, performs rational Sturm root counts, checks the linear-subresultant sign pattern, verifies the boundary value \(35/8\) and the interior witness \(647/81\), and numerically evaluates the unique positive algebraic optimizer.

The numerical decimal values are reported only after the exact algebraic uniqueness checks. The proof does not infer an infinite statement from finite sampling. The remaining scientific limitation is bibliographic: an older equivalent exact calculation could exist under different terminology despite the recorded searches.
