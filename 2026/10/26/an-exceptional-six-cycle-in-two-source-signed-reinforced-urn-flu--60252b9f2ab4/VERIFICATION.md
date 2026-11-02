---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

PASS: Reconstructed P Q=−Q P for even d, B=Q(P−P²)/2, 4B²=P⁴−P². Fourier pairs z,−z diagonalize B² and give the stated real-part formula; for d≥8 the nearest π/2 angle yields rho_d>1/2 from cos(π/8)(1+sin(π/8))>1. d=2,6 are subcritical, d=4 supercritical. Eigenvalues satisfy |lambda|≤1/√2<1, giving stable Lyapunov drift and a.s. convergence, with limiting innovation covariance I/4. In d=2,6 the bounded-noise SA martingale CLT gives the stated positive covariance integral even with nilpotent zero blocks. For dominant lambda, the explicit gamma product Pi_t removes drift and makes M_t=T_t/Pi_t a square-integrable martingale: increment L² sum finite since Re(lambda)>1/2. Initial fair Bernoulli innovations give E|M∞|²≥||u||²/(4|2+lambda|²)>0, thus amplitude genuinely nondegenerate and sharper than a mere big-O rate. Finite 14 even-size spectral checks were independently reproduced for even 2..28; not extrapolated to the infinite d range.

## originality

PASS

PASS: The general spectral and SA expressions are equivalent background and are fully credited; equality of structural matrices fails for the prior one-neighbor cycles, so no identified source supplies the d=6 exception and nonzero amplitude specifically. General SA theorems cover the standard limit method, not the arithmetic classification or the positive random-amplitude lower bound; the result claims only those additional conclusions. The claim is an all-even-d theorem and not an exact finite table lookup; finite spot checks by themselves would not establish it. The prior methods plus a fresh special-model analysis can form a proof, but no inspected prior claim implies the d=6 exception and positive-amplitude assertion without the nontrivial two-tap spectral computation.

## value

PASS

PASS: A minimal two-input alternating signed urn network exhibits the unusual nonmonotone finite-size threshold d=2,6 versus every other even size, with a *nonzero* random leading fluctuation. This identifies an exact structural spectral boundary beyond the general stochastic-approximation rate theorem and supplies a precise example of Gaussian behavior returning at a larger cycle size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
