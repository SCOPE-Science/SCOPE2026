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

# Verification and limits

The proof establishes the theorem for **all** integers \(k\ge1\) and **all** feasible symmetric nonnegative stochastic matrices. The certificate is the single Rayleigh vector with hub entries \(\pm1\) and leaf entries \(\pm(1+\sqrt2)\); row stochasticity bounds its quadratic energy by 4. Equality forces every hub diagonal to vanish, while the leaf eigen-equations force all edge weights. The constructed spectrum controls the negative eigenvalue and verifies the SLEM. These steps, not tests, establish global optimality and uniqueness.

To independently reproduce the supplementary computational checks, install the pinned packages in `requirements.txt` under Python 3 and run `python verify.py` from the folder containing those two files. The actual successful output was:

`VERIFY_OK: exact radical identities for 12 graph orders; 2000 fully nonuniform feasible competitors; stochasticity, 2k+2 eigenvalue comparisons and Metropolis asymptotic comparison`

The code uses exact symbolic arithmetic for \(1\le k\le12\) to verify hub saturation, the left hub/leaf eigenvector equations, and the antisymmetric quadratic. It builds all matrix entries and independently checks their numeric spectra. It further constructs 2,000 distinct feasible non-orbit-invariant random chains and verifies they do not undercut the formula. These experiments are finite checks, not exhaustive enumeration, not a proof of infinite-dimensional statements, and not independent scientific audit.

No proof is claimed beyond balanced double stars or outside symmetric nonnegative stochastic matrices. Specialized historical sources not surfaced by the documented search may exist. Independent audit: not performed.
