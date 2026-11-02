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

PASS. For independent Poisson input and batch gates, finite-array stationary first moments solve mu_i E Xi=lambda; stationary generator on Xi Xj gives a triangular moment recurrence, including the crucial j=i+1 exclusion of the incoming j-1 product term. Its substitution produces exactly H(0,j)=0, H(i,i)=1 and (mu_i+mu_j)H(i,j)=mu_i H(i-1,j)+mu_j H(i,j-1); first-event conditioning of two independent death chains yields the same recursion and strict 0<H<1. For fixed p and all positive rates, grouping exponential holding times into periods gives mean p a_bar and variance p b_bar, so the inverse renewal FCLT for jump counts yields relative-position diffusivity 2 b_bar/a_bar² over physical time a_bar L. The initial separation s sqrt L and lower-chain absorption time ->1 lead by reflection to erfc(s a_bar/(2 sqrt b_bar)). Independently recomputed H recursion at L=100,250,500 for rate patterns (1),(1,3),(1,2,4) and verified approach to stated periodic erfc coefficient. No Pearson/dynamic covariance claim.

## originality

PASS

PASS best-of-knowledge with explicit prior coverage. Reuveni-Hirschberg-Eliazar-Yechiali 2014 develop exact consecutive interval laws and homogeneous error-function scaling, with an inhomogeneous finite-array algorithm; the full primary conclusion explicitly identifies occupation correlations of disjoint intervals and nonhomogeneous rate effects as further work. Finite covariance recurrences may already be indirectly derivable; novelty is restricted to precise two-death-chain interpretation and periodic spatial √L normalized covariance limit with b_bar/a_bar² heterogeneity factor. Yeger et al 2024 studies extended ASIP moments and special cases and might imply part of finite identities; full-text comparison remained bounded.

## value

PASS

PASS. The normalized covariance across separated sites is a natural stationary correlation invariant of a standard transport/coalescence process. The exact periodic diffusivity factor quantifies a nontrivial broadening that cannot be read off from the homogeneous formula by merely substituting mean gate rate. This resolves a motivated universality/inhomogeneity question and gives a sharp asymptotic boundary layer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
