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

# Finite reproducibility checks

Run `python3 verify_denumerant.py` with Python 3's standard library. The script computes exact denumerants by a coin-change dynamic program and separately by total-coin-count enumeration. It compares the two in the local critical range and tests the predicted multiplicity, membership witnesses and gap for all integer parameters from 7 through 100. Actual result: `PASS 5969 formula-and-DP comparisons and invariant checks, a=7..100`. The full prefix from zero up to the claimed multiplicity is checked by the dynamic program.

# Proof limits

The formula for all coin counts, monotonicity, the exact boundary census, and the standard Apéry implication establish the universal theorem. Finite computations have no claim to exhaustive treatment of unbounded parameters. Source inspection was limited to the accessible primary literature and targeted searching. An independent audit has not been performed.
