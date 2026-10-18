---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Integer circle maps preserve Haar measure and their transfer operators satisfy total-variation contraction by 1/m. On centered BV, P_epsilon=(1-epsilon)P_a+epsilon P_b has uniform geometric norm contraction; h=(I-P)^-1 phi exists with bounded BV norm. The Green–Kubo variance is ||h||_2^2-||P h||_2^2; the reversed stationary Markov chain gives a bounded martingale-coboundary CLT with ergodic conditional variance. At positive mixing weights zero conditional variance implies a common value on every inverse branch, yielding H(ax)=H(bx) a.e. Writing a/gcd=r,b/gcd=s coprime, Fourier frequency comparison c_k=0 unless s divides k, else c_k=c_{rk/s}; repeated s-divisibility forces every nonzero Fourier coefficient zero and H constant. Therefore only phi=0 has zero variance. For phi=psi-U_a psi, telescoping gives h0=-U_a psi and P_a h0=-psi; differentiating the Poisson resolvent/variance at epsilon=0 cancels h0 derivative terms and gives exactly ||U_a psi-U_b psi||_2^2>0. Exact Fourier cosine computations independently confirmed sigma^2=epsilon for (a,b)=(2,3),(3,2),(6,10) and sigma^2=epsilon-epsilon^2 for (4,2) over rational test probabilities. These finite tests are diagnostics; the BV/CLT conclusion is analytic.

## originality

PASS

Abstract annealed CLT, zero-variance common-coboundary criterion, density stability and general variance differentiability are preexisting. The surviving addition is complete arithmetic no-degeneracy for any distinct integer slopes (including divisibility) and evaluated endpoint variance response for every deterministic BV coboundary.

## value

PASS

This cleanly characterizes noise-induced destruction of deterministic zero-variance obstructions for the natural Bernoulli random-beta family, with a positive exact linear coefficient and an arithmetic resonance boundary. The coefficient quantifies sensitivity of CLT fluctuations rather than merely invoking generic differentiability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
