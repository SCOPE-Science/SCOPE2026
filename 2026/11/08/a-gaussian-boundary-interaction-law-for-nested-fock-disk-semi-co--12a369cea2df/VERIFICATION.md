---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For concentric disk Toeplitz indicators at squared radii tL and t(L+eta sqrt L), radial monomials diagonalize both: Q_y(n)=P(Pois(y)≥n+1). The semi-commutator has diagonal eigenvalues -d_n where d_n=Q_{L_-}(n)(1-Q_{L_+}(n)), so the formula lists *all* singular values, not merely bulk approximations. With n=L+eta sqrt L/2+x sqrt L, the Poisson CLT gives w_a(x)=Phi(x-a/2)Phi(-x-a/2), a=|eta|. Uniform compact-window convergence and two-sided Poisson Chernoff bounds permit dominated Riemann sums for each p>0, norm convergence and count for 0<s<Phi(-a/2)^2. Nonnegative Tonelli gives exact sum_n d_n=E[(X-Y)_+], and independent-normal difference N(0,2) yields C1(a)=exp(-a²/4)/sqrt(pi)-a Phi(-a/sqrt 2). The function is even in centered x and strictly decreasing for x>0. The companion finite checker was inspected but is only corroborative.

## originality

PASS

PASS for the joint full nested two-disk singular-spectrum and arbitrary Schatten-p/counting law, with explicit **partial prior coverage** credited: the earlier collapsing-annulus Fock paper P4 yields an equivalent scalar trace coefficient, via C1(a)=1/sqrt(pi)-B(a/2)/2 where its B(c) is the annulus defect coefficient. That overlap does not supply the product profile w_a, all p moments/counting nor the exact Poisson positive-part identity for nested two disks. The inspected Qin fixed-symbol semi-commutator theorems do not handle moving t-dependent second boundary; Apredoaei fixed-domain asymptotic does not itself establish this critical two-boundary crossover. The scalar trace C1 is not independently original.

## value

PASS

The sqrt(t)-separated boundary interaction is a natural critical regime for Gaussian Fock quantization. Complete singular-value profile, exact finite-scale Poisson representation, all quasi-Schatten moments, spectral counting and norm law provide more mathematical content than a recycled trace coefficient; intrinsic value persists notwithstanding partial prior coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
