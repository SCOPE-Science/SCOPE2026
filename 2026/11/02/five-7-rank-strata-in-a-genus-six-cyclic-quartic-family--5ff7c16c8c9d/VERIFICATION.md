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
# Verification and scope

The two standalone programs `verify_symbolic.py` and `verify_primefield.py` were executed with Python 3. The first additionally requires SymPy. They returned, respectively:

```
CYCLIC4_G6_SYMBOLIC_OK
CYCLIC4_G6_PRIMEFIELD_OK {0: 1, 1: 1, 2: 4, 3: 9, 4: 29}
```

The first check constructs the polynomial Cartier coefficient matrix from powers of the defining quintic, verifies the exact discriminant and the key intersection identities modulo \(7\), and proves uniqueness of the quartic's singular point using a Gröbner basis. The second independently expands coefficient powers using standard-library integer arithmetic, checks stable and ordinary Cartier ranks for all \(44\) discriminant-nonzero parameter pairs over \(\mathbb F_7\), and verifies independent point-count trace congruences.

The mathematical proof is in `RESULT.md`, including semilinearity and the normalization-genus calculation. The finite-field program does not check arbitrary extension-field parameters and cannot replace the symbolic argument. The result does not determine Newton polygons or quotient the marked family by geometric isomorphism. Independent external validation has not been performed.
