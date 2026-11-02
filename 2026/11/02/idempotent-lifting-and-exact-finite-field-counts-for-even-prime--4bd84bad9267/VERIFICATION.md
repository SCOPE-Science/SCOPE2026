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

# Computational and symbolic verification

The proof in `RESULT.md` provides the general algebraic argument. Independently, `verify.cpp` implements the multiplication table \(e_i e_j=e_{2j-i\bmod 2p}\) directly, enumerates coefficient vectors, and tests all \(2p\) coordinates of \(x^2=x\). It does not implement Fourier transforms, Frobenius orbits, or a predetermined family of idempotents. Compile and run with `c++ -O3 -std=c++17 verify.cpp -o verify && ./verify`.

Actual complete enumeration results:

| Prime \(p\) | Field order \(q\) | Enumerated count | Predicted count |
| ---: | ---: | ---: | ---: |
| 3 | 3 | 28 | 28 |
| 3 | 5 | 96 | 96 |
| 3 | 7 | 176 | 176 |
| 5 | 3 | 184 | 184 |
| 5 | 5 | 626 | 626 |
| 7 | 3 | 760 | 760 |

The checker prints `VERIFY_OK`. These enumerations are exhaustive for their finite domains; they do not certify the infinite parameter family. Necessary algebraic steps for the unrestricted proof are: verification of the algebra section and right-annihilator kernel; identification of lift eigenspaces with \(Z\mapsto\iota(Z)Y\); reciprocal Fourier-pair propagation and Frobenius descent; in modular characteristic, the nilpotent-local-group-ring argument and conjugation of the involution. Field-extension dimension preservation is standard for vector spaces defined by linear equations over \(\mathbb F_q\).

Independent audit has not been performed. No external formal proof certificate is claimed.
