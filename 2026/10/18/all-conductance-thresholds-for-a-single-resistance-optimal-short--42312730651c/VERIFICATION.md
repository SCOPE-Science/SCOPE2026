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

# Reproduction of analytical and exact-arithmetic checks

Execute `python verify.py` with Python 3.11 or later and SymPy 1.13 (or compatible 1.x release). The output verified from the embedded source is:

```
VERIFY_OK 67122 exact symbolic, rational placement, tie, and direct-matrix checks
```

The script symbolically reduces polynomial difference identities, the balanced-tail formula and the odd-parity amplitude inequality. It exhaustively compares every nonadjacent shortcut for path orders \(4\) through \(32\), using exact rational arithmetic at and around every predicted transition and over additional conductor values. It also independently obtains Kirchhoff indices from rational matrix inverses for orders \(4\) through \(9\). These finite computations support the proof and permit error detection; they are not an exhaustive proof for unbounded path order. Infinite quantifiers, optimality and strict cutoff ordering are justified in the analytical argument in RESULT.md.

The accompanying files provide source, dependencies and exact output sufficient to rerun these checks. No external or independent mathematical validation has been performed.
