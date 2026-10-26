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

# Reproducible checks and limits

Compile and run from the unpacked finding directory:

```
c++ -std=c++17 -O2 checks/verify_dihedral.cpp -o check_d
./check_d 1
./check_d 3
c++ -std=c++17 -O2 checks/verify_local.cpp -o check_l
./check_l
```

`verify_dihedral.cpp` independently enumerates all binary group-algebra elements for dihedral groups of orders 8 and 24. For each it multiplies actual group basis elements, verifies \(x^2=0\), and determines the left regular rank by exact binary elimination. For \(m=1\) the rank counts are \(0:1,1:1,2:6,4:40\) (total \(48\)). For \(m=3\), they are \(0:1,1:1,2:15,3:9,4:172,5:78,6:996,7:168,8:4512,9:384,10:9024,12:15360\) (total \(30720\)). These agree with the stated products.

`verify_local.cpp` independently enumerates \(\mathbb F_4[D_8]\) and all \(2^{16}\) two-by-two matrices over \(\mathbb F_2[t]/t^4\), using exact finite-field and polynomial-ring arithmetic and direct linear rank. The observed counts are \(D_8\) over \(\mathbb F_4\): \(0:1,1:3,2:60,4:1728\); and the matrix block: \(0:1,2:9,4:78,6:168,8:384\). The checks completed successfully.

These are finite tests only. The unbounded theorem uses explicit crossed-product descent and exhaustive symbolic valuation cases in the written proof; neither numerical tests nor a software log is an infinite proof. No independent audit has been performed. The claim is limited to characteristic two and odd \(m\).
