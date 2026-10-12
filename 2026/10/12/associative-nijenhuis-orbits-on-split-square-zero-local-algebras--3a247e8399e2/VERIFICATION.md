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

# Reproducible checks

`verify.py` runs with a standard Python 3 interpreter and no external packages. It constructs the finite fields of orders \(2\), \(3\), and \(4\), enumerates every linear endomorphism of the respective unital square-zero algebra, and directly evaluates the Nijenhuis identity on all basis pairs. It compares each such identity evaluation with the proposed normal form \(N(1)=\alpha 1+u\), \(N|_V=T\), \(Tu=\alpha u\). It separately enumerates every member of \(\mathrm{GL}(V)\) and forms the exact conjugation orbits, and then obtains the claimed orbit-count formula by exhaustive similarity-class enumeration.

The tested pairs \((q,n)\) and resulting (operators, orbits) are \((2,1)\mapsto(6,6)\), \((3,1)\mapsto(15,12)\), \((4,1)\mapsto(28,20)\), \((2,2)\mapsto(56,18)\), \((3,2)\mapsto(459,48)\), \((4,2)\mapsto(1984,100)\), and \((2,3)\mapsto(1920,46)\). Successful execution ends with `VERIFY_OK`.

The checker tests only these finite cases; it does not verify every field size or every dimension. The proof of the arbitrary-dimensional theorem is in `RESULT.md`. Independent mathematical audit and validation remain unperformed.
