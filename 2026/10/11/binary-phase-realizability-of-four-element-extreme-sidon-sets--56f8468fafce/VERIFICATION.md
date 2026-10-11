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

The proof is analytic. The bundled `verify.py` provides finite regression checks only. It verifies the \(\mathbb Z_7\) witness by exact integer autocorrelation; exhausts all \(16\) binary sign patterns on the \(\mathbb Z_5\) and exceptional \(\mathbb Z_4\times\mathbb Z_2\) prototypes; and samples the universal rectangle identity on \(1560\) cyclic instances.

Replay command: `python verify.py`

Observed output:

`VERIFY_OK rectangle_cases=1560 z7=1 z5_binary_solutions=0 exceptional_binary_solutions=0 max_rectangle_err=7.994e-14`

The floating-point rectangle sweep is not used as proof. The rectangle formula is proved symbolically by splitting on the order-two character value. Exhaustiveness over all four-point extreme supports comes from the cited published classification.
