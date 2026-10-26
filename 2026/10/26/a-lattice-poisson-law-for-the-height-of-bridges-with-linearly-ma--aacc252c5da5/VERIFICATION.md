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

# Reproducible checks and limits

Run `python3 verify.py` using standard Python 3; no third-party libraries or network access are required. The script enumerates all \(2n\)-step bridges for \(1\le n\le8\), verifies the exact return-count formula, checks each restricted-height coefficient for \(2\le h\le n+1\), and verifies the tilted excursion-height formula as rational identities at four distinct algebraic parameter selections and nine height thresholds. It completed with **320 exact assertions passed**.

The script also evaluates three larger exact coefficient ratios and compares them with their predicted lattice-window asymptotic approximations. Those numerical comparisons illustrate convergence but are not used to infer an infinite statement. The analytic local central limit argument in `RESULT.md` is the proof for arbitrary large \(n\); a finite enumeration or asymptotic numerical comparison is not a substitute for that proof.

The exact coefficient ratio remains valid for every integer \(n\ge1\), \(1\le k\le n\), and \(h\ge2\). The Poisson convergence requires \(k_n/n\to\rho\in(0,1)\) and integer thresholds with \(k_n(1-k_n/n)^{h_n}\to\tau\in[0,\infty)\). The theorem does not claim a continuous centered Gumbel limit.
