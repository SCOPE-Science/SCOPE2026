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

# Verification and reproducibility

The analytic proof in `RESULT.md` covers all real Banach spaces and all bounded injective operators, with no finite-dimensional approximation assumptions. Its critical steps are the finite-codimensional near-kernel lemma, the factor-four monotonicity calculation, weak convergence against every continuous linear functional, and the sharp normality/closed-range equivalence.

The standalone Python 3 script `CHECK.py` uses only the standard library and exact fractions; run with `python3 CHECK.py` in the unpacked folder. Observed result:

`VERIFY_OK rational_profiles=64 annihilator_tests=128 exact_order_pairs=746 infinite_net_proof_is_analytic=True`

This finite stress test checks sample scalar functional annihilators, norm bounds and comparable cone increments for the weighted diagonal operator. It is **not** exhaustive and does **not** prove weak convergence of the entire infinite net; those facts are established solely by the analytic argument. The theorem has undergone same-model review, not an independent audit.
