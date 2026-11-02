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

# Analytical and finite verification

The principal infinite-dimensional checks are included as complete arguments in RESULT.md. They rely on the 2026 source's norm estimates, eigenfunction membership, and predual identifications; these are precisely named and verifiable from that source. In the irrational case the key Fredholm singular-sequence assertion follows from local-uniform decay after normalization, not merely from approximate eigenvalues. In the rational case an infinite-dimensional kernel is exhibited at every interior nonzero eigenvalue before using closure.

The optional script `checks/spectral_sanity.py` uses only Python's standard library and checks the finite semigroup monomial identity, upper-radius inequality for sampled eigenvalues, and the rational phase obstruction at sample points. Run `python checks/spectral_sanity.py` after extracting the files. The script is a numerical consistency check; it does not prove density of an irrational torus flow, a Fredholm statement, or an exact continuum classification. No independent audit or external certification was performed.
