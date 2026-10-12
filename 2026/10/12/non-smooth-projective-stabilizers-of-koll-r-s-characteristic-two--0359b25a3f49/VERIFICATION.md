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

## Reproducible checks
Run `python3 check_stabilizers.py` using Python 3 with no nonstandard dependencies. The expected success marker is `STABILIZER_CHECK_OK` followed by \((q,\#\mathbb F_{q^2},\#\text{stabilizers})=(2,4,12),(4,16,5),(8,64,9)\).

The program enumerates normalization changes \(t\mapsto at+b\) and explicitly checks preservation of the pulled-back plane linear series. Its finite-field arithmetic is implemented without external packages; the modulus polynomials are \(u^2+u+1\), \(u^4+u+1\) and \(u^6+u+1\). It also checks that the five exponent vectors in the infinitesimal variation are distinct for the tested degrees.

## Logical boundaries
The proof of completeness uses the unique cuspidal normalization preimage and classification of automorphisms of \(\mathbb P^1\) fixing it, not exhaustive enumeration. The all-degree constraints on \(a,b\) and the dimension-three tangent-space computation are symbolic identities in characteristic two. Finite checks cannot establish them for all \(n\). The full nonreduced group scheme, including its nilpotent structure, has not been computed; only its geometric reduced subgroup and tangent dimension are determined.
