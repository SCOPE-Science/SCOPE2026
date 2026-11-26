---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible mathematical checks

Run `python3 verify.py` with Python's standard library. It asserts the generator differences, two divisibility identities, pair gcd bounds and the relevant strict inequalities on 644 sampled triples. It separately computes the Frobenius number and genus for the square triples starting at 193 and 194, just above the sufficient cutoff 192, by shortest paths in the residue graph modulo the smallest generator. It tests nonsymmetry for both instances via \(2g\ne F+1\). The expected last line begins `VERIFY_OK`.

These are bounded checks. The all-parameter result is the symbolic proof in `RESULT.md`; the checker neither classifies the region under the bound nor checks priority. The known triangular boundary is cited for context only.
