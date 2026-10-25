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

# Finite verification and proof checks

Run `python3 verify.py` with the unmodified Python 3 standard library. The script constructs all \(n\times n\) matrices over several small prime fields, retains only invertible matrices, forms the full Leibniz constraint system for all \(n^2\) entries of a derivation, computes its kernel dimension by modular Gaussian elimination, and checks its distribution against independently implemented exact formal-series coefficients. It also checks the first two nontrivial larger-degree coefficient rows without exhaustive matrix enumeration.

Exhaustive configurations: \((p,n)=(3,1),(3,2),(3,3),(5,1),(5,2),(7,1),(7,2),(2,1),(2,2),(2,3)\); the sum of invertible input matrices is \(13{,}963\). See `test_results.txt` for exact counts and the successful completion marker.

The mathematical proof of all \(n\), including prime-power extension fields, is the derivation-equation reduction plus the finite-field cyclic-grading and exponential-component arguments. The checker directly verifies only prime fields and small dimensions; it is not evidence that a finite search proves an infinite statement. It does not verify originality or constitute independent scholarly review.
