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

**Analytic checks.** For a block of \(m\) observations, differentiate \(\sum_i\operatorname{sgn}(x_i-m_p(x))|x_i-m_p(x)|^{p-1}=0\) at nonzero residuals to recover the normalized weights \(\alpha_i\). Compute the induced rank-one derivative norm \(m^{1/p}\|\alpha\|_q\). For \(p>2\), use scalar balance and subadditivity to establish \(\max_i\alpha_i\le1/2\). For \(1<p<2\), simply use \(\|\alpha\|_q\le1\). Verify that the active-equality blocks of any fitted order satisfy their scalar mean equations, and that a continuous finite choice of \(L\)-Lipschitz branches remains \(L\)-Lipschitz. For sharpness, check stationarity with the vector of strictly positive graph edge multipliers and let the small multipliers tend to zero according to the proof.

**Code replay.** Run `python verify_isotonic.py` from the directory containing this document. It requires only the Python standard library. It checks the stationarity identities and evaluates the derivative norms for finite path, star and diamond examples at \(p=3/2,3,4\). The terminal message is `FINITE_DIAGNOSTICS_OK` if assertions pass.

**Verification limits.** The executable performs finite floating-point diagnostics and does not establish universal graph coverage, global Lipschitz bounds, the infinite-parameter limits, or originality. Those rely on the written proof and literature comparison. A 1998 general approximation article was available through a bibliographic abstract but not through a directly inspected full text. No independent audit has been performed.
