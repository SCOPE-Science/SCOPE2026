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

# Reproducibility and verification

`check.py` implements backward covariance propagation from the update \(e_{k+1}=(I-\alpha H)e_k-\alpha\xi_{k+1}\), and runs with NumPy using a fixed seed. Invoke `python check.py` in the directory containing the file.

A completed invocation returned `PASS: 7825 formula/risk checks; 6900 strict alternative-permutation inequalities`. The checks consist of all 24 permutations of four independent random positive steps across 60 trials for each dimension two through six; independent matrix comparisons for the exact adjacent covariance and trace identities; closed-form two-eigenvalue endpoint checks; and a positive-definite correlated-noise construction where the covariance difference is indefinite. The correlated-noise difference had eigenvalues approximately \(-0.12974899\) and \(2.10505763\). At condition number \(10\), the expected squared-error noise factors for the descending and ascending reciprocal steps are \(0.83\) and \(2.81\), respectively.

The numerical experiments cannot certify the theorem for all dimensions or all parameter choices. The all-dimensional result follows by exact covariance algebra, positivity of trace products of positive-semidefinite matrices, and a finite adjacent-interchange argument. The derivative-free strictness and two-dimensional formulas follow from direct algebra. The stated originality comparison is literature-based, not an independent audit or complete publication search.
