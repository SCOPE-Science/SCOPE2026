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

# Reproducible checks and their boundaries

Run `python code/verify_brandt.py` using Python 3 with no third-party packages. A record of a successful execution is embedded as `verification/verify_output.txt`.

The program (i) evaluates the explicit threshold formulas on the entire semigroup for indices 1 through 7; (ii) independently constructs all atomic diagrams of triples in the named-zero relational multiplication language, then derives quantifier-rank-three types recursively for indices 1 through 6; and (iii) checks extension-profile saturation of all 20 canonical two-element orbit types at indices 5, 6, and 7.

Expected classification: five types with representatives of indices 1, 2, 3, 4, and 5; the last class starts at index 5 and has a minimal member with 26 elements.

**Unproved by computation:** Exhaustive finite enumeration does not certify the infinite family, nor does a successful run establish novelty. The mathematical proof of stabilization is the explicit three-round strategy in `RESULT.md`. No independent scientific audit has been performed.
