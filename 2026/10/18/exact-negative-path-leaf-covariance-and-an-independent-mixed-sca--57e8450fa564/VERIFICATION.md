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

# Verification evidence and limits

`CHECK.py` runs with Python 3 and its standard library. The actual packaged checker was run and returned `EXACT_OK 2530 assertions; enumerated n=2..9, 499 recurrence transitions`.

It compares expectations of total path length, leaf number, product, and leaf-depth sum with their closed expressions in every uniform random recursive tree through nine vertices. It checks exact leaf variance and replays five rational recurrence assertions for each integer from two to 499. These are independent finite diagnostics for the formulas printed in `RESULT.md`.

The claims for all tree sizes and the mixing limit are mathematical consequences of the conditional moment recursion, Eulerian descent representation and finite-history approximation in `RESULT.md`. The checker is not a proof of a central limit theorem, infinite-dimensional mixing, or source uniqueness. A historical joint-limit theorem beyond the material inspected may still affect priority.
