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

# Verification evidence and limits

The binary tortoise operator is implemented independently in `verify_local.py` and `verify_rotations.py`; each implementation removes the leftmost \(1\) and appends it. Both programs need only Python 3's standard library and can be run with `python3 verify_local.py` and `python3 verify_rotations.py` from the directory containing the scripts.

The local exhaustive program checks the dichotomy \(T^k(u01v)=T^k(u10v)\) exactly when \(k\ge |u|_1+1\), and strict lexicographic order otherwise. It also checks \(T^k(u0)<T^k(u1)\) for finite binary contexts. Its result was `PASS local_swap=266253 terminal_change=26611`.

The independent rotation test computes integer-exact mechanical periodic words at all reduced rational slopes with denominator at most 96, compares every attainable factor of tested lengths to the formula, and verifies all images through the tested iteration bound. Its result was `PASS exact_rational_mechanical_cases=973080`.

These scripts verify the finite local operation and numerous rational comparison instances. They do *not* certify that the irrational rotation coding has exactly \(n+1\) factors or prove the infinite-scope enumeration. Those statements follow from the proof in `RESULT.md`, relying on pairwise distinct irrational discontinuity phases and strict monotonicity of the image at each surviving crossing.

The externally performed independent audit remains unperformed. Nothing here claims exhaustive computer verification of an infinite parameter range.
