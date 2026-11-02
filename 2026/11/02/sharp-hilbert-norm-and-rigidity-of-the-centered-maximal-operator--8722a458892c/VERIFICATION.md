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

The standalone file `petersen_verifier.py` uses only Python 3 standard-library integers, fractions, enumeration, combinations, permutations, and hashing. Execute it in the same directory as this document using:

```sh
python3 petersen_verifier.py
```

Its successful completion prints:

```text
CERTIFICATE_OK selections=59049 automorphisms=120 orbits=792 strict=791 winning_orbit_size=20
winning_rep 5089 representatives_sha256 64b5f805f915480abdc0d7fb4557bea9899b3d3712b917e6d650a7e7e2e38134
```

The program verifies every adjacency-preserving permutation, exactly partitions all 59049 radius assignments, and tests the strict separator matrix by fraction-free exact Sylvester elimination for each of 791 nonwinning orbit representatives. The nonwinning bound is strictly \(741/500\) for the **squared** operator norm. It reconstructs the full exceptional orbit of size 20 as an explicitly defined set of ordered-pair patterns, checks the isolated cubic root by rational signs and derivative bounds, checks the eigenvector equations in the quotient ring \(\mathbb{Q}[z]/(200z^3-355z^2+87z-1)\), and checks that the claimed radii are uniquely active using exact interval arithmetic. An unrestricted conclusion for other graphs is not asserted. The result is independently reproducible computationally but has not undergone an external scientific audit.
