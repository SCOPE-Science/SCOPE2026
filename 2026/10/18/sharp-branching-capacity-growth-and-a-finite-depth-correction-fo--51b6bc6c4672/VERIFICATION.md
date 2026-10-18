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

The accompanying `verify_tree_hardy.py` is a standalone Python 3 standard-library program. From the directory containing it, execute `python3 verify_tree_hardy.py`. The actual execution returned `PASS: 195 finite numerical consistency assertions.`

The finite tests compare the norm obtained from repeated application of \(H^*H\) on an explicit root-child branch with the spectral norm computed from the high-precision secular relation. They test several branching factors and finite depths; additional tests verify the residual size of the sharp \(p=2\) expansion and the consistency of both \(\ell^p\) inequalities and their limiting constants for multiple exponents.

The reproducible analytic basis is the pair of levelwise upper/lower inequalities, positivity and radiality of the branch inverse, the exact leaf-boundary secular equation, and Taylor expansion with controlled remainder. The finite checks neither exhaust all parameter values nor independently certify those proofs. Independent verification has not been performed.
