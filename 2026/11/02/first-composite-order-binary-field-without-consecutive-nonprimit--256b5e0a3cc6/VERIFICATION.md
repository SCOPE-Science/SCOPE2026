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

# Verification and reproducibility

Run `python3 check_np2048.py` in this directory. Python 3 standard library suffices; no third-party modules, external services, or downloaded artifacts are required. The verifier ran successfully with:

```
VERIFY_OK bezout=4 irreducible_degree=11 primitive_generator=yes nonprimitive=111 exhaustive_elements=2047 ordered_NP_pairs=0
```

The exact polynomial Bézout identities listed in `RESULT.md` are checked using binary carryless multiplication. Each proves a polynomial gcd equal to \(1\) over \(\mathbb F_2[T]\), and the four cases exhaust the possibilities for a translated nonprimitive pair in \(\mathbb F_{2048}\). As a separate cross-check, the verifier applies Rabin's criterion to \(T^{11}+T^2+1\), verifies that its residue class \(T\) generates the cyclic group of size \(2047\), constructs subgroups of orders \(23\) and \(89\), and independently enumerates all nonprimitive elements by exponent tests across the entire nonzero field.

The field enumeration is exhaustive because \(\mathbb F_2[T]/(T^{11}+T^2+1)\) contains exactly \(2048\) polynomial residue classes, represented uniquely by the integers from \(0\) through \(2047\). It is not a sample extrapolated to an infinite family. The smallest-field statement separately uses all proper-subfield cases for exponents below \(11\). No independent external validation or independent mathematical audit has been performed.
