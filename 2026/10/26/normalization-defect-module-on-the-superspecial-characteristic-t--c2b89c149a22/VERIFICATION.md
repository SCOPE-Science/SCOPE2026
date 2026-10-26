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

# Verification

Claim checked: the normalization-defect quotient on the superspecial characteristic-two Kummer partial resolution is the pushforward of the pullback of \(\mathcal O_{\mathbb P^1}(-1)\) from the reduced exceptional line.

Checks performed:
- Compared the displayed quotient-surface equation and blow-up ideal with Schröer’s §7 chart presentations.
- Verified the normalization extension \(S_x=R_x[t]\), \(t^2=q\), \(xt=y\).
- Verified that \([t]\) is annihilated by \(x\) and \(r^2\), and that reduction modulo \(x\) gives the even-subring inclusion \(k[q,r]/(r^2)\hookrightarrow k[t,r]/(r^2)\).
- Checked the symmetric-chart transition \([s]=q^{-1}[t]\), which is the transition of \(\mathcal O_{\mathbb P^1}(-1)\).
- Derived the filtration and \(h^1=1\) using the cohomology of \(\mathcal O_{\mathbb P^1}(-2)\) and \(\mathcal O_{\mathbb P^1}(-1)\).

Limits:
- The proof is a hand-checked local algebra argument; no independent computer-algebra certificate was used or needed.
- Historical priority checking is not exhaustive.
- Independent audit and independent validation have not been performed.
