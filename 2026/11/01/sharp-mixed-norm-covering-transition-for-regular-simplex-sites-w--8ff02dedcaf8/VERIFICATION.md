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

# Reproducibility and limits

Run `python3 verify_simplex_phase.py` using Python 3 standard library. This execution returned: `PASS 456 deterministic mathematical parameter checks (not a universal proof)`. The checks cover dimensions 3, 4, 5, 8, 15, 30; multiple exponents on either side of the critical value; positivity of explicit uncovered-ball radius; near- and above-threshold radial inequalities; and the equal-distance facet path. The mathematical proof in RESULT.md—not the finite numerical tests—establishes the all-dimensional quantifiers. No formal proof assistant, independent audit, or external certification has been performed.
