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
# Reproduction and boundaries

Run `python3 verify.py` with Python 3. The bundled standalone checker performs exact finite-field arithmetic for \(\mathbf F_{3^m}\), \(m\in\{1,2,3,4\}\). For each displayed parameter pair it checks geometric smoothness by the nonzero polynomial gcd of the degree-five polynomial and its formal derivative; it separately applies the discriminant-based smoothness criterion and asserts agreement. It computes the Cartier–Manin matrix and successive Frobenius twists, then compares ranks with the theorem's strata. It directly enumerates the rational points of \(C_{0,0}\) over \(\mathbf F_{81}\).

Observed output:
```
F_3: irreducible=(0, 1) smooth=3 strata={(0, 2): 1, (4, 0): 2}
F_9: irreducible=(1, 0, 1) smooth=57 strata={(0, 2): 1, (2, 2): 6, (4, 0): 50}
F_27: irreducible=(1, 0, 2, 1) smooth=651 strata={(0, 2): 1, (2, 2): 24, (4, 0): 626}
F_81: irreducible=(1, 0, 1, 1, 1) smooth=6321 strata={(0, 2): 1, (2, 2): 78, (4, 0): 6242}
F_81: #C_(0,0)(F_81)=154 (Hasse-Weil maximum)
VERIFY_OK
```

The four tested finite fields are a finite consistency check, not a proof for all extensions. The exact general proof uses the discriminant factorization, Cartier–Manin calculation and stable-rank argument, and the Hermitian-curve quotient. No independent mathematical audit was performed.
