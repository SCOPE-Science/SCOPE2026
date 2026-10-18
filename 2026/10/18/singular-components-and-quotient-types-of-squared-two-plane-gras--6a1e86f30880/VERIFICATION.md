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

# Reproducibility and limits
Run `python3 verify.py` in the directory containing this file. The script uses only Python's standard library, finishes with `VERIFY_OK`, and reports:

- Every projective sign assignment compatible with the Plücker equations for explicit generic rank-two matrices over \(\mathbb F_{1009}\) at \(n=4,5,6\): respectively \(8,16,32\) fibers.
- The fixed-component tangent negative dimensions for \(4\le n\le12\), together with their dimension, component-count, and Gorenstein-parity predictions.
- Exact ranks modulo \(101\) of the Jacobian of all \(4\times4\) hollow symmetric minors at a generic smooth point (rank \(3\)) and representatives of the zero-row and two mixed-split strata of \(\operatorname{sGr}(2,5)\) (ranks \(2,0,0\)).

The tests use finite fields only to catch implementation/algebra errors, not to establish characteristic-zero assertions or exhaustive singular-locus classification. The infinite proof uses invariant-theoretic normality, generic orbit fibers, tangent representations of every sign involution, and quotient-singularity criteria. There are no external data dependencies or unprovided certificates. The listed degree values are the published formula, not a finding asserted to be new.
