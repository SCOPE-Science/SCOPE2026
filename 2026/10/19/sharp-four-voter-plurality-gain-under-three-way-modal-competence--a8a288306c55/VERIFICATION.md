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

# Verification

The program `VERIFY.py` is standalone and uses only Python's standard library. It computes each of the 256 vertex-assignment accuracy increments in exact rational arithmetic by two independent methods: direct plurality outcome averaging, and the \(2,1,1\) event decomposition. It also checks the deterministic 81-profile identity, the 35 exchangeability classes, the exact two accuracy values of the sharp witness, and a finite combinatorial consistency check of the uniform-subset identity.

The symbolic proof that the 35 types exhaust all modally competent independent probability vectors is in RESULT.md. It uses the explicit convex-combination coefficients and separately affine dependence of expected accuracy on each row. For \(N\geq4\), the universal extension is justified by the exact identity \((N-3)/(4\binom{N}{4})=1/\binom{N}{3}\), not by computation.

Run: `python VERIFY.py`. The program prints `VERIFY_OK` summary lines followed by a complete list of the 35 sorted vertex-type rational increments.

Limits: this is a self-review, with no independent audit; the program does not test strategic voters, dependence, more than three alternatives, or stronger unpublished theorems.
