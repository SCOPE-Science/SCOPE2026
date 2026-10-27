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

# Computation and proof checks

`verify.cpp` is a standalone C++17 program. Compile with `g++ -std=c++17 -O2 verify.cpp -o verify` and run `./verify`. The completed invocation reported:

```
ZERO degree=9 coefficients_low_to_high=0,2,0,0,0,0,0,0,0
N2=10 N4=10
smooth_degree9=13122 smooth_degree10=39366 zero_degree9=1 zero_degree10=0 min_B4_degree9=0 min_B4_degree10=2
VERIFY_OK
```

The two irreducible field moduli are explicitly checked, and all monic coefficient vectors are traversed. The counted smooth forms agree with the independent finite-field identity that the number of monic squarefree polynomials of degree \(d\) over \(\mathbb F_3\) is \(3^d-3^{d-1}\).

`check_witness.py` independently implements multiplication in \(\mathbb F_{81}\) and checks that the nine \(\mathbb F_9\) elements have exactly one point each and every other affine \(x\) has a nonsquare curve right-hand side. Its completed invocation reported `WITNESS_VERIFY_OK N2=10 N4=10 B4=0`.

The universal assertion for all odd \(q\) is not extrapolated from these finite runs; it is proved algebraically from Frobenius antisymmetry and the published bound. The uniqueness claim is only within hyperelliptic genus-four curves over \(\mathbb F_3\). Neither external audit nor independent validation has been performed.
