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

# Reproducible verification

Run `python3 verify.py` from the directory containing the files; only Python's standard library is required. The verifier recomputes finite hypergeometric pair moments directly from exhaustive distinct fixed-histogram color assignments rather than using the spectrum as an oracle. Across all positive integer class-size compositions of \(N=4,5,6,7,8\), it checks the formulas for the two nonconstant eigenvalues and the constant-mode zero, and compares the weighted-graph variance formula with the exact sample variance for seven disparate integer weight patterns, including signed weights. It additionally examines all graphs of orders four and five for the claimed zero-variance classification. Output:

`VERIFY_OK 60 class-size compositions; 108879 exhaustive assignments; 7488 graph classifications; 8268 exact assertions`

These checks are finite. Correctness for all \(N\ge4\) follows only from the spectral decomposition, the elementary additive-Boolean graph lemma, and the graph-specific kernel argument detailed in `RESULT.md`. No probabilistic or numerical convergence test is presented as an infinite proof. Independent audit was not performed.
