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

Run `python3 check_disagreement.py` using Python 3 and no external dependencies. The program enumerates all ordered Walsh profiles for electorates \(1\le n\le8\), compares the two strict singleton election winners with the closed multinomial event formula, and independently checks the first disagreement at \(n=4\). It also enumerates further compressed counts, checks the exponential tilt numerically, and reports finite-size deviations from the asymptotic expression. Successful execution ends with the exact line `ALL EXACT COMBINATORIAL CHECKS PASSED`.

The unbounded claim is supported analytically by score inequalities, the Radon–Nikodym exponential tilt, an exponentially small conditional constraint-error bound, and the aperiodic lattice local-limit theorem proved via Fourier inversion. The code is a reproducibility aid for finite instances, not independent validation, a proof of a local-limit theorem, or a substitute for the analysis. The result intentionally ignores profiles where either election rule ties; no tie-breaking prescription has been assumed.
