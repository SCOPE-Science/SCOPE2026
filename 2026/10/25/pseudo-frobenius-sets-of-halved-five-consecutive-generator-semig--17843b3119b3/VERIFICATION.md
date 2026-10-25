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

The included independent `verify.py` implements a shortest-path calculation of every least semigroup element in a residue class and derives pseudo-Frobenius elements from edge maximality. It passed for every integer \(4\le x\le500\) (497 complete Apéry sets and pseudo-Frobenius sets). This is a finite stress test; the unrestricted theorem is supplied by the normal-form and maximality proof in `RESULT.md`. The parameter \(x=4\) is checked despite one redundant generator. No independent audit has been performed.
