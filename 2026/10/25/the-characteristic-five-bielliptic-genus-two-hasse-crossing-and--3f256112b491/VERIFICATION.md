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

# Reproduction and limits

Run `python3 check.py` using Python 3 and its standard library. Successful execution ends with `VERIFY_OK`. The script checks a characteristic-five coefficient identity for the cubic discriminant, enumerates every normalized parameter pair over \(\mathbb F_5\), \(\mathbb F_{25}\), and \(\mathbb F_{125}\), independently recomputes the relevant coefficients of \(f(x)^2\), and counts singular models, Hasse intersections, and the three rank strata. Expected rank-zero/rank-one/rank-two counts are `(1,6,14)`, `(1,42,558)`, and `(1,246,15254)` respectively.

The script is a finite exact arithmetic regression and does not prove the assertions for every extension degree. The universal justification is the symbolic Cartier--Manin computation, the discriminant identity, and the repeated-root argument in `RESULT.md`. The classification is of marked coefficient pairs only. No external or independent audit is asserted.
