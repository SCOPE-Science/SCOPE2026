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

# Verification and reproducibility

The proof of the universal parameter characterization is the exact two-by-two identity for the symmetric part of the generator, followed by Sylvester's criterion and the Euclidean logarithmic-norm equivalence. The root count uses Descartes' rule of signs and four exact rational sign evaluations. The diverging numerical abscissa follows from the displayed limiting matrix and its exact eigenvalues; the bounded mass conditioning follows directly from the exact two mass eigenvalues.

`verify.py` independently assembles local piecewise-linear finite-element contributions and uses Python's `fractions.Fraction`, without external dependencies. Run `python3 verify.py` alongside the packaged files. The checker reports 10,623 exact-rational checks, including the assembled symmetric-part identity for many independent mesh pairs, positive generator entries, exact witness vectors, and the two rational root brackets.

Finite checks do not certify the real-parameter theorem by enumeration; they are independent arithmetic spot checks of the displayed identities and examples. The analytical argument is the proof. No independent audit has been performed.
