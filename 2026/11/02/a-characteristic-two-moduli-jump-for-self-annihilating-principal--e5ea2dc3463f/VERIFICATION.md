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

The proof is algebraic and uniform in the field and number \(d\) of variables. As a separate finite check, the standard-library program `verify.py` exhaustively enumerates each element with nonzero linear initial part for the cases \((d,q)=(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4),(4,2)\). It directly tests square-zero multiplication, computes the principal-ideal row space, verifies its half-dimensionality and compares canonical distinct ideals to the theorem's formula. The eight resulting counts are respectively \(3,2,5,2,14,3,84,240\). In finite-dimensional local algebras, the half-dimensionality plus \(f^2=0\) gives \((f)=\operatorname{Ann}(f)\). Verification command: `python3 verify.py`. Expected final line: `EXACT_SELFANNIHILATOR_IDEALS_OK 8 direct exhaustive enumerations`.

The checker treats all elements in the specified finite cases, but its cases are not a proof for arbitrary fields or dimensions. The proof establishes the universal result. No independent mathematical audit has been performed.
