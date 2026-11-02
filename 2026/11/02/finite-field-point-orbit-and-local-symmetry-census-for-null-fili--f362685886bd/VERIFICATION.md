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
# Reproduction and checks

Run `python3 verify.py` with the Python standard library. The checker enumerates every linear map on the tested finite-dimensional vector spaces and, independently of the proposed normal form, checks the full multiplication-preserving identities to discover the genuine automorphisms. It then explicitly constructs every point orbit and checks every linear map against the pointwise-local condition. It compares all orbit sizes, stabilizers, orbit numbers, local matrix conditions and local-map counts with the formulas in `RESULT.md`.

Complete test configurations: \((2,2),(2,3),(2,4),(3,2),(3,3),(4,2)\), where each pair is \((q,n)\). The program reported the expected counts and ended with `NULL_FILIFORM_FINITE_LOCAL_AUT_OK 6 exhaustive matrix configurations`.

Finite exhaustive tests are not proofs for arbitrary dimensions or arbitrary fields. Those quantifiers are justified by the triangular-recursion argument in `RESULT.md`. The checks do not establish literary priority, which is subject to the limits in the mathematical review. Independent audit: not performed.
