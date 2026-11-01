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

# Analytic verification and finite diagnostics

The complete claim has a proof in `RESULT.md`. Its critical checks are: (i) the minimax infimum enforces each two-sided expectation box, including the zero-budget boundary, (ii) trace-one plus at most two independent active inequalities give no more than four real constraints on supported Hermitian perturbations, and (iii) the only positive integer ranks satisfying the bound are both one. The finite-dimensional dual minimum is attained because the image of the parameter map in the spectral-spread-plus-absolute-value norm is a closed linear subspace.

The optional `CHECK.py` uses only the Python standard library. Invoking `python CHECK.py` checks a reproducible finite set of numerical equalities and inequalities for the two-Pauli example. It completed 2,540 assertions in the tested environment. Its random samples and ten error-budget comparisons cannot establish a general theorem and are not used as proof.

The originality comparison is best-knowledge rather than independently certified. The zero-budget special case was previously established. The present positive-error formula is the sole new mathematical claim; no assertion of independence has been made.
