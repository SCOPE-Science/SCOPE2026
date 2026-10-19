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

Run `python3 VERIFY.py` in the same directory as this document. The program is self-contained, uses only the Python standard library, and reports `PASS: 3727 rational and finite numerical assertions`.

The checks include both parameter regimes, their shared boundary, simplex normalization, numerical eigenvalue agreement, comparisons with independently varied probability vectors, local perturbations, exact rational coordinate-descent energy identities, and the invariant negative sign of an inverse off-diagonal triangle. Finite testing is not exhaustive and is not used as a proof of universal optimality.

The proof in `RESULT.md` independently establishes the exact energy Rayleigh quotient, spectral decomposition, unique one-dimensional optimum, boundary equality, and uniqueness across *all* distributions through symmetrization and eigenvector equality conditions.

The originality comparison includes complete accessible portions of the relevant open-access coordinate-probability paper and the published inverse-positive sampling theorem. The 1991 E-optimal design article was located but its full PDF could not be inspected; no claim of whole-document noncoverage is made about it. Independent validation has not been performed.
