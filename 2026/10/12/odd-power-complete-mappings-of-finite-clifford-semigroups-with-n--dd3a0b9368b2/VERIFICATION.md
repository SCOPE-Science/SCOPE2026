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

# Verification record

The symbolic proof in `RESULT.md` has four checkable steps: semilattice-grade preservation for any positive \(k\), conversion of an ordinary complete mapping on a finite \(2\)-group for odd \(k\), simultaneous coprimality via CRT on odd-order group exponents, and a projected-product contradiction for a cyclic nontrivial Sylow-\(2\) group.

`verify.py` was run using the Python standard library. It constructs and independently evaluates \(45\) actual finite group witnesses for odd exponents \(3,5,7\), including products with the nonabelian dihedral group of order \(8\) and a nonabelian Heisenberg group of order \(27\). It also exhaustively tests \(8\) cyclic-group obstruction instances; enumerates all permutations in \(4\) two-fiber Clifford examples, verifying subgroup preservation for every successful mapping; and tests \(765\) arithmetic CRT cases.

```text
PRODUCT_WITNESSES=45 CYCLIC_OBSTRUCTIONS=8 CLIFFORD_EXHAUSTIVE=4 CRT_CASES=765 VERIFY_OK
```

The finite checks establish only the enumerated instances, not a universal claim. Hall--Paige is an external established theorem cited explicitly; its proof is not replicated here. No independent audit has been conducted.
