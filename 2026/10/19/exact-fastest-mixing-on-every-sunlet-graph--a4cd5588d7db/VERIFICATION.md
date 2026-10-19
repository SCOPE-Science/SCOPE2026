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
# Reproduction and limits

Run `OPENBLAS_NUM_THREADS=1 python check_sunlet.py` with Python 3, NumPy and SymPy. The program verifies the identities \(p_n+2q_n=1\), \(1-\mu_n^*=x_n^2/(x_n^2+2x_n+2)\), the scalar first-order condition, the lower-negative-eigenvalue inequality and the isolated zero-frequency eigenvalue comparison. It independently constructs \(2n\)-by-\(2n\) matrices for 33 graph orders (\(3\) through \(30\), plus \(32,40,48,64,90\)) and another 200 matrices on \(n=4\). It tests 4950 random feasible orbit-parameter pairs against the theorem's lower bound.

In the recorded run: `PASS symbolic identities; 233 independent full-matrix spectra; 4950 random Fourier lower-bound tests`. The exact proof is the five-step argument in `RESULT.md`; the finite checks are not exhaustive over all graph sizes or real parameters. The only global uniqueness assertion in the finding is among dihedrally invariant chains. Unknown unindexed prior statements remain an originality risk, and no independent audit has been conducted.
