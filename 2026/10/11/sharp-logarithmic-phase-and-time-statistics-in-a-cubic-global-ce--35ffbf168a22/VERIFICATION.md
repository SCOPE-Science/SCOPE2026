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

# Verification of the mathematical claim
The derivation is analytic; the auxiliary checker is corroboration, not an infinite-proof certificate.

**Exact identities checked:** the elliptic parameter notation is \(K_{\mathrm{par}}(m)=\int_0^{\pi/2}(1-m\sin^2\theta)^{-1/2}\,d\theta\); \(H=(1+\kappa x^2)(1+\kappa y^2)\) is constant; \(dt=Lh_L(w)dw/(2\sqrt Q)\) in absolute value on a quarter; \(T=2LI_L/\sqrt Q=4K_{\mathrm{par}}(-\kappa A^2)\); and the normalized full-time distribution has density \(h_L/I_L\). Symmetry fixes four equal-time quarters without a change of time variable.

**Uniform and sharp asymptotics:** the integrable endpoint excess \(q(z)=(1-e^{-z})^{-1/2}-1\) has exactly \(\int_0^\infty q=2\log2\); its two boundary copies give \(I_L=1+4\log2/L+o(L^{-1})\). A unique mean crossing \(w_L\) tends to zero while \(Lw_L\) diverges, so \(L\max(F_L-w)\to2\log2\). Exactly \(d_{\mathrm{TV}}=2\max(F_L-w)\), giving the claimed \(4\log2\) constant. No numerical computation substitutes for these steps.

**Reproduce the auxiliary checks:** install dependencies in `requirements.txt` and run `python CHECK.py`. The checker compares independent forms of the physical period, evaluates finite amplitudes, and checks the mean-crossing sign and total variation. Its `CHECK_OK` output is limited to those finite evaluations and is not proof of an asymptotic bound.

**Limits:** only \(\kappa>0\) and \(A\to\infty\) at fixed \(\kappa\); the complete-elliptic-integral period expansion is classical, and global originality priority over all sources is not established.
