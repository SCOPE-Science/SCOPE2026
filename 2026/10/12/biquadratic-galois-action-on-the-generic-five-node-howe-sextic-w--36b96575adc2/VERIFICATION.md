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

# Reproduction and finite/infinite distinction

With Python 3 and `sympy==1.14.0`, run `python verify_howe_nodes.py`. The independent script forms the two cubic polynomials over the exact integers \((2,3,4,5,6)\), calculates their Sylvester resultant, checks the reduced Jacobian critical ideal in \(\mathbb Q[u,v]\), the nonzero Hessian, all five node positions, and square-class factorization. It separately enumerates all projective \(\mathbb F_p\)-rational singular points for 18 small good primes and compares to the quadratic-residue criterion.

Successful execution prints:

`VERIFY_OK resultant exact, unique rational squared-node pair, nondegenerate nodes, independent square classes, 18 finite-field checks`

The program tests the displayed specialization and finitely many primes. The proof of the generic Galois group uses the normal-local specialization argument in `RESULT.md`; the infinite natural density uses Chebotarev and finite étale good reduction, and is not being inferred from the 18 sample primes. No independent audit or external mathematical certification was performed.
