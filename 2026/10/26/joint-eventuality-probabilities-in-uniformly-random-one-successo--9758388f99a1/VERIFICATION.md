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

# Reproducibility

Execute `python3 verify_joint_liveness.py` using the Python standard library only. The code directly enumerates each uniform function and atomic labelling and separately calculates the EGF coefficient with exact fractions. The 2-label cases with state counts 1–4 and 3-label cases with state counts 1–3 match exactly. The program also compares the 2-label birthday formula through n=8 and tests size monotonicity in those finite cases, and tests the 1-label n-invariance through n=6. Expected terminal marker: `JOINT_RANDOM_MAPPING_LIVENESS_OK`.

# Proof boundaries

No finite exhaustive run establishes all-size claims; the proof's exponential generating function and elementary cycle factorial moments establish the general identity and asymptotic limit. The tail estimate is uniform in the finite state size. The sample-size strictness for two labels follows from the analytical survival function of the cyclic-vertex/birthday variable and applies to all positive n, not just the tested n. Other label-count monotonicity is not asserted. Independent audit has not been performed.
