---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For every fixed k>=1, N>=3 and identical Brownian motions with generator D d²/dx², one collective reset at the first +L crossing has a finite-mean regenerative stationary age law: S(t)=erf(sqrt(a/t)), q(t)=[erfc(sqrt(a/t))-erfc(3sqrt(a/t))]/2 for an uncrossed particle below -L, and joint mass (1/mu_N) C(N,k)q^k(S-q)^(N-k)dt. With y=a/t, y_N=[erfc^{-1}(1/N)]²~log N and mu_N~a/y_N, the moving layer y=y_N+w gives Nq->exp(-w)/2 and N(1-(S-q))->3 exp(-w)/2. The resulting fixed-k integral is 1/(2^k k!) int_0^infty f(z) z^(k-1)e^(-3z/2) dz. Bounding layers on each side, plus direct Frullani evaluation for the all-positive-count probability, gives 1/(k3^k), log(3/2) and the log-series conditional law without illegitimately interchanging an infinite k sum. Reconstructed the killed-kernel image integral and all exponent constants. Independently numerically integrated original finite-N renewal formulas, obtaining log(N)P(K_N=1) ~0.3368 at N=10^3 and ~0.3385 at N=10^5, consistent with slow convergence to 1/3; finite quadrature is NOT the infinite proof. Noncompact bounded continuous f is controlled via the stated y-region tail envelope; N=2 is excluded because mu_N diverges.

## originality

PASS

Best-of-knowledge PASS for the sharp rare endpoint crossing law (conditional count distribution and trigger-age Gamma profile), NOT for the resetting model, killed density, renewal stationarity or leading extreme scaling. The closest primary work computes full central-interval counting and a limiting extreme density whose support has endpoint -L, but the nonuniform probability of *crossing* that endpoint and the joint logarithmic age layer are not its displayed results. The exact finite-N stationary representation implies these quantities in principle, but does not automatically imply the singular asymptotic theorem; unspecified older endpoint corrections remain priority risk.

## value

PASS

The mirror -L is a natural sharp endpoint of the leading stationary minimum law, making its beyond-endpoint probability a mathematically motivated rare-event correction rather than an arbitrary threshold. The exact logarithmic-series conditional occupation law, Gamma trigger-age localization and sharp logN coefficient provide independently usable edge statistics inaccessible from the leading bulk law. They can inform subsequent boundary point-process asymptotics, though no full process theorem is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
