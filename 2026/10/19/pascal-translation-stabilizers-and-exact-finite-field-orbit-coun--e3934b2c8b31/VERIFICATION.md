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

# Reproducibility and evidence

Run `python3 verify.py`. The program uses only the Python 3 standard library. It checks by direct matrix-unit evaluation that the canonical formula satisfies the weight-zero Rota–Baxter identity for prime orders two, three and five in dimensions two through five. It tests every Pascal parameter, every nonzero diagonal scalar parameter, the maximum nilpotent power witness, and exhaustive stabilizers for \((n,q)=(2,2),(3,2),(2,3),(3,3)\). The group orders and stabilizer counts in these exhaustive tests are respectively \((6,2),(168,2),(48,6),(11232,6)\).

The universal proof in `RESULT.md` is algebraic, uses no division by an integer, and covers arbitrary fields, including prime powers not checked by the program. Finite tests alone cannot certify those universal statements. The orbit-counting formula counts two constructed orbits and makes no claim of their positive-characteristic exhaustion. An independent audit has not been performed.
