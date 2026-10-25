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

Run `python3 verify_monotone.py` with standard Python 3. The script enumerates every permutation at each size from 3 through 8, independently counts its cycles and monotone consecutive triples, and compares the resulting covariances using exact fractions against both positional formulas. The verified output is `VERIFY_OK 42 exact enumerative assertions`. This finite calculation checks the claimed formulas only at the tested sizes. The unrestricted proof is the directed-chain contraction lemma and exact count of already completed directed cycles in `RESULT.md`.

Independence and historical novelty are not certified by this script.
