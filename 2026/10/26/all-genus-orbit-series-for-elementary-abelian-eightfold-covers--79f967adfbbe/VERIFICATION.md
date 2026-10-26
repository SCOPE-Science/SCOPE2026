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

Run `python3 verify_orbit_series.py`. The test uses only the Python 3 standard library. It generates all \(168\) automorphisms of \(\mathbb F_2^3\), all sixteen subspaces, and their five permutation cycle types. It performs exact coefficient arithmetic for the Burnside–Möbius expression and the stated rational function through degree \(70\). The symbolic common denominator \(E(t)\) is explicitly the product over all five full-cycle denominators and has degree \(70\); each term's denominator divides \(E(t)\). The stated degree-\(27\) denominator divides \(E(t)\) exactly, and its numerator after clearing \(E(t)\) has degree \(63\). Agreement of all \(71\) coefficients proves the identity of rational functions. A separate actual brute-force orbit enumeration for \(3\le r\le12\) is included.

Expected exact output:

```
VERIFY_OK GL3_order=168 conjugacy_types=5 subspaces=16 denominator_degree=70
VERIFY_OK rational_identity_exact=true coefficients_0_to_70=true independent_orbits_r3_to_r12=true
first_coefficients [1, 1, 3, 4, 8, 9, 17, 20, 34, 39, 61, 72, 106, 123, 174, 204, 277]
```

The computation certifies the finite rational identity; the geometric equivalence and pole analysis are established in the accompanying written proof. It does not constitute independent validation, an exhaustive priority search or a statement about other signatures.
