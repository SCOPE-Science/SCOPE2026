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

The included `verify.py` was executed with Python 3 and passed all assertions. It reconstructs the sixteen Cartier coefficient polynomials using multinomial expansion; checks the rank formulas and the characteristic-seven polynomial identities, the degree-three irreducibility condition and coprimality with the smoothness discriminant; and exhaustively checks each of the 37 smooth rational parameter pairs in \(\mathbf F_7^2\) against fourth powers of the Cartier matrix.

On rational parameters the computed stratum sizes, in order \((4,0),(3,1),(2,2),(1,2)\), were 29, 4, 2 and 2. The general five-point assertion depends additionally on the proved factorization of the twisted-rank scalar and the irreducibility of its cubic factor. This is a symbolic proof supported by finite calculations, not a census over arbitrary extensions; the latter is unnecessary for the stated polynomial argument.

No independent audit or independent validation has been conducted. The assertions do not determine the Newton polygon or the full Ekedahl–Oort type.
