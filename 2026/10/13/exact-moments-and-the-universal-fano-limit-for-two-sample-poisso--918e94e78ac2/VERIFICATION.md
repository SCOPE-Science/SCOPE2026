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

The analytic verification uses four identities valid for every \(\lambda>0\):

1. The symmetric Skellam mass function for \(D=X-Y\).
2. The telescoping Bessel recurrence, which gives \(\mathbb E|D|=2\lambda q_\lambda\).
3. The Poisson score identity \(\operatorname{Cov}(X+Y,f(X-Y))=\lambda\,d\mathbb Ef(X-Y)/d\lambda\).
4. The Bessel derivative identity giving \(d\mathbb E|D|/d\lambda=2r_\lambda\).

Substitution yields the displayed exact means and variances without truncation. Fixed-order Hankel expansions for \(I_0\) and \(I_1\) then yield the Fano limit and its first correction.

The accompanying Python checker was replayed from the finalized package path. For \(\lambda\in\{0.1,1,5,20\}\), independently truncated double-Poisson sums agreed with the Bessel formulas to the stated numerical tolerance. It also checked the scaled large-\(\lambda\) Fano corrections at \(\lambda=100,400,1600\), approaching \(\pm(1/2-1/\pi)/\sqrt\pi\). These finite checks detect algebraic or transcription errors but do not establish the infinite identities or asymptotic theorem.
