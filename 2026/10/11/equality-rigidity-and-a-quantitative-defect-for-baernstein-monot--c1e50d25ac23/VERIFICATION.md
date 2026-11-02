---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Analytical verification of the high-exponent derivative gap

In Zhang's notation, \(r=2a\), \(g=q^a\) and \(B=q^*/q\). For simple unit-circle roots, Proposition 2.2 gives \(B(0)=0\), hence \(|B(z)|\le|z|\). Proposition 3.4 gives
\[
\mathcal P_r=\frac{M_{Q_n}(r)}{an}\int_{\mathbb D}\operatorname{Re}H_a(B)|g'|^2\,dA.
\]
Theorem 3.5 and equation (4.2) yield positive harmonic \(\operatorname{Re}H_a\) with center value \(1/(a+1)\). Disk Harnack therefore gives
\[
\operatorname{Re}H_a(B(z))\ge\frac{1-|z|}{2(a+1)}.
\]
Proposition 2.4 supplies the nonnegative entropy remainder and \(r\mathcal P_r/M_p\); Lemma 2.3 identifies their total with \(r^2F_p'(r)\). Thus the exact constant multiplying \(\int(1-|z|)|g'|^2dA\) in \((M_p/M_Q)F_p'\) is
\[
\frac1{anr}\frac1{2(a+1)}=\frac{2}{nr^2(r+2)}.
\]
With normalized area measure, the exact mode integral is
\[
2k^2\int_0^1(1-\rho)\rho^{2k-1}d\rho=\frac{k}{2k+1}.
\]
For \(m_0\) the first nonzero intermediate coefficient, \(c_{m_0}(r)=(r/2)(1-m_0/n)a_{m_0}\). Its positive contribution produces the stated coefficient bound. The proof is analytic and applies for all \(r>0\); only the \(r>2\) portion is asserted as new relative to the prior quantitative comparison.

No Lean or independent external expert verification is claimed. The existing verification-channel statuses remain `not_performed`.
