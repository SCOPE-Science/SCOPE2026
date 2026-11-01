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
Run `python3 VERIFY.py` with the standard library. It builds all thirteen canonical projective points, determines the 52 forbidden collinear triples, enumerates all simplices, constructs the exact integer top-boundary matrix, obtains independent ranks of 168 modulo primes 101 and 1009, enumerates all 5616 distinct projective collineations, and compares signed Lefschetz and exterior-square characters for every element. The recorded output is `VERIFY_OUTPUT.txt` and ends `VERIFY_OK`.

## Mathematical limits of checks
The proof's exact rank over \(\mathbf Q\) uses modular rank as a **lower** bound plus the proved chain-complex kernel upper bound. The verifier does not determine integral Smith invariants, torsion or homotopy type. Character equality yields rational, not necessarily integral, module isomorphism. Independent external validation has not been performed.
