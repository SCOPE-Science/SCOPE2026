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

Run `python verify.py` using Python 3.10+ with SymPy installed (`pip install -r requirements.txt`). The verifier constructs the full 32-vertex graph and 196227 independent sets, independently repeats all size counts by cyclic transfer, constructs an explicit matching with 98087 pairs and 52 critical cells, and topologically sorts the full nonempty-face directed Hasse graph. It then reconstructs the oriented 24-by-27 Morse differential by exact gradient-path recursion, computes its integer Smith invariants, and checks a 21-by-21 determinant of minus one. A successful run ends in `ALL_VERIFY_OK`.

The checker is a finite exhaustive proof certificate for this precise graph and relies on correct Python/SymPy execution; it does not prove any result for other cycle lengths or color counts. Self-review was performed; independent audit has not been performed.
