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

# Verification scope

The stand-alone `verify.py` program checks the exact angular and triangular-height moment integrals through the sixth Euclidean distance moment. It symbolically checks all inversion and involution identities and tests exact rational counterexamples to two-moment injectivity. It also uses independent numerical integration of the original angular/height pair-distance integral for sixteen positive radius/height combinations and three moment orders (48 quadratures).

To reproduce, run `python verify.py` in an environment with Python 3, SymPy and SciPy. Recorded result:

`VERIFY_OK: exact moment/inversion/involution identities, 48 independent quadratures, 5 exact noncongruent moment pairs`

The proof of global feasibility, multiplicities, and the sharp separation constant is analytic and appears in `RESULT.md`. These finite checks are not independent certification, do not establish historical originality, and give no finite-sample statistical bounds.
