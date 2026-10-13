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

# Reproduction and limits

Run `python verify.py` using Python 3 with the dependencies in `requirements.txt`. The program reconstructs both conditional coordinate-update matrices, checks exact-rational second-moment propagation for several dimensions and parameters, exhaustively enumerates every binary selection string through five steps, and tests the small-parameter spectral splitting against direct numerical eigenvalues. The execution returned:

```
VERIFY_OK exact_finite_identities=168 spectral_cases=12
```

An additional analytic computation expands \(M_d(t)\) to quadratic order in \(t\): its order-\(t\) entries in positions \((1,2)\), \((2,3)\), and order-\(t^2\) entry in \((3,1)\) multiply to \(2(d-1)t^4/d^4\). The leading-order characteristic equation after the shift \(1-2t/d\) is therefore cubic with the claimed constant. The proof establishes separation and overlap of the dominant eigenvalue using asymptotic left and right eigenvectors. None of the finite computations proves an infinite-dimensional, arbitrary-Hessian, or uniform-in-parameter statement. No independent audit was conducted.
