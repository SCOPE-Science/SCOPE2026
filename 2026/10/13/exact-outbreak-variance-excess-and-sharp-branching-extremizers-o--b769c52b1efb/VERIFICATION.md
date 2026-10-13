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

Run `python3 verify_tree_variance.py` with standard Python 3. The executable performs exact rational calculations of two full finite probability measures, not Monte Carlo estimates. It enumerates all increasing-parent tree encodings on \(1\)–\(7\) vertices, with counts \(1,1,2,6,24,120,720\), and checks equality of epidemic and bond-percolation means, their variance difference against the weighted incomparable-pair polynomial, and both sharp extremal values when branches exist. For the two-point test law \(Q\in\{1/4,3/4\}\) with equal probabilities, \(q=1/2\) and \(v=1/16\). Rational-rate Poisson-contact/exponential-recovery checks are also included. The observed terminal line is `VERIFY_OK`.

Scope of the computation: only the specified finite encodings and one discrete transmissibility distribution are enumerated, so computation alone cannot establish the all-tree or all-law assertions. The universal results follow from the exact indicator-product, lowest-common-ancestor and rooted-tree bounds in `RESULT.md`. No independent scientific audit has been performed. The code is self-contained and reads no files other than its own program text.
