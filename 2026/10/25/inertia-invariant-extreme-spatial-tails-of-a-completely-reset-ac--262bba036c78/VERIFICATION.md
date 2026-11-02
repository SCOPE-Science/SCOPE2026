---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Reconstructed reset-free velocity convolution with (1-exp(-(t-s)/tau)), exact Gaussian variance 2Dg_tau(t), uniform finite-time angular correction <=v_0*tau and -3tau/2<=g_tau(t)-t<=0. These give positive two-sided multiplicative comparison of excursion MGFs with overdamped Feynman-Kac growth e^{t(Dk^2+Lambda(k))}. Positivity-improving angular semigroup has positive principal eigenfunction coefficient for deterministic and uniform heading, so exponential Poisson age mixture has MGF domain Psi(k)<r, with divergence exactly at equality. Lambda even, convex, nonnegative, and Psi strictly increasing for positive k yields unique root. A tilted exponential concentration at k_star and integrating ages t~x/Psi'(k_star) supplies both log-tail lower bounds; Markov supplies upper bounds. Perturbative Lambda(k)=v_0^2 k^2/(2D_r)+O(k^4), Lambda<=v_0|k|, and exact exponential-age integration give both k_star endpoints and 4D/(tau^2 r^3). Our independent 37-mode Fourier matrices recover two roots and exact thermal renewal identities at six (r,tau) points. Finite matrix checks are not the infinite proof.

## originality

PASS

The inertia-independent principal-Mathieu all-rate active far-tail root is beyond the fourth-order stationary moment and high-rate r^-3 variance results for this same resetting model. Passive underdamped and overdamped active resetting precedents are distinct hypotheses; abstract Feynman-Kac/renewal principles underlie rather than automatically provide a checked specialized formula. No exact dominating result surfaced in targeted Resultary/literature searches. Priority remains qualified because some prior active resetting full technical results were not exhaustively inspected.

## value

PASS

Exact far-tail localization versus r^-3 core-width is a motivated distinction for interpreting rare active-particle excursions. The principal Mathieu root characterizes all positive reset rates, not only a numerical special value; its independence of finite inertia is a nontrivial stable structural property. The result is limited to complete Poisson resetting and coordinate logarithmic tails.

The dated certificate retains the supplied scientific assessment, sources and limitations.
