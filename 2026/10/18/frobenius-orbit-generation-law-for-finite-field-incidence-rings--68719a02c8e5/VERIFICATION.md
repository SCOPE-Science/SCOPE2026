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

# Verification and reproduction

The mathematical proof is in `RESULT.md`, Steps 1–4. The key logical test is the distinction between a tuple generating an incidence algebra over its entire field of scalars and generating the same underlying unital ring from the tuple and the identity alone.

Run `python3 verifier.py` with Python 3.10 or later. The program independently closes the unital prime-field additive span of each tuple under matrix multiplication and compares its size with the full incidence algebra. The code does not use the Frobenius criterion to decide generation. It exhaustively processes all ordered tuples for \((q,n,k)=(2,2,2),(3,2,2),(4,2,1),(4,2,2),(2,3,2)\) on chains, for a three-vertex fork over \(\mathbb F_2\) with two matrices, and for a two-vertex discrete poset over \(\mathbb F_4\) with two matrices. Polynomial-basis arithmetic handles \(\mathbb F_4\); modular arithmetic handles prime fields.

The expected generated-tuple counts are \(24,432,0,1440,384,96,120\), respectively. A successful execution prints `VERIFY_OK`. The checks cover chains, a fork, and a discrete poset; the theorem for all finite posets and all finite fields is established symbolically rather than by finite experiment.

The mathematical argument invokes the classical Wedderburn–Malcev splitting/conjugacy theorem for finite-dimensional associative algebras over perfect fields. It does not provide a computer-formal proof of that standard theorem. The paper-level novelty comparison is necessarily bibliographic, not a proof of uniqueness. Independent validation and external auditing have not been performed.
