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

The exact finite-capacity claims are certified by `certificates.json` and checked by the standard-library-only `verify.py`. The verifier reconstructs the complete search domain from the prefix/suffix and reverse-complement definitions, validates every proposed codebook witness, validates each conflict clique and its integer multiplicity, and checks that every orbit is covered at least its cardinality. Equal primal and dual totals prove exact optimality at all lengths from two through sixteen. The all-length existence statement follows from the explicit constructions and the run argument in `RESULT.md`. Finite checks do not replace that proof, and no external or independent audit has been performed.

Reproduce with `python3 verify.py certificates.json`. The verifier has no external package requirements; it does not depend on a saved optimization log or a third-party black-box optimality claim. The source and data files are included together in this package.
