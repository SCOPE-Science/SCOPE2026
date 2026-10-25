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

Run the standard-library-only programs `python artifacts/verify.py` and `python artifacts/verify_f4.py` from this package's root directory. Both use exact finite arithmetic and the defining Rota–Baxter equation, rather than a database of precomputed valid operators.

The first program enumerates normalized image lines and nonzero covectors over the prime fields \(\mathbb F_2\) and \(\mathbb F_3\), tests all sixteen ordered basis pairs, computes full algebra-automorphism groups, and checks each predicted orbit is exactly the corresponding invariant stratum. Actual output:

```text
q= 2 rank1= 25 orbit_sizes= [1, 3, 3, 6, 6, 6] automorphisms= 24
q= 3 rank1= 122 orbit_sizes= [2, 8, 16, 24, 24, 48] automorphisms= 432
VERIFY_OK
```

The second program uses independent \(\mathbb F_4\) arithmetic with reduction modulo the irreducible binary polynomial \(t^2+t+1\); it enumerates rank-one operators, tests the equation and constructs every conjugacy orbit under all \(2880\) algebra automorphisms. Actual output:

```text
q= 4 rank1= 363 orbit_sizes= [3, 15, 45, 60, 60, 180] automorphisms= 2880
VERIFY_F4_OK
```

An additional direct image/covector count at prime fields of sizes \(2,3,5,7\) returned \(25,122,844,3030\). These checks are finite and cannot certify the theorem for all finite fields; the full proof in `RESULT.md` establishes the quantified statement. The published \(\mathbb F_2\) enumeration is prior literature rather than a claimed discovery here. Independent mathematical audit status remains not performed.
