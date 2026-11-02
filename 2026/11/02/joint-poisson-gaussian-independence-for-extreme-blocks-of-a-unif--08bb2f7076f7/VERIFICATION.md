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

# Reproducible finite checks

Run `python verify.py` with Python 3 and its standard library from a directory containing the standalone supplied file. The script exhaustively generates and filters set partitions for each \(1\le n\le8\), checks their Catalan counts, verifies first and second falling-factorial identities for all admissible block sizes, and checks the Narayana block-count distribution. It independently enumerates weak compositions for \(2\le m\le9\) and \(1\le t\le9\), verifying the conditional count-of-positive-entries formula. It performs 824 integer/rational exact finite assertions and 6 numerical scale comparisons; output reports both categories separately.

The main infinite convergence claim is not verified by enumeration alone: its proof uses the exact all-size factorial-moment formula, hypergeometric central limit theorem under \(O(\log n)\) parameter perturbations, determinacy of the Poisson factorial moments, and a uniform tail bound for larger blocks. These steps, the discrete lattice subsequence condition, and scientific limitations are detailed in RESULT.md. Independent validation has not been performed.
