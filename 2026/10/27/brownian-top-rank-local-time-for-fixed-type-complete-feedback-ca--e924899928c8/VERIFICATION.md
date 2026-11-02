---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For a deck with n fixed types each of multiplicity m, the pathwise identity T-m=count of correct predictions at multi-maximal ties follows by telescoping the maximum remaining count. The exact score compensator is S=sum_k W_k/(nm-k). Centered hypergeometric counts have the n-bridge martingale FCLT; on intervals away from endpoints, bounded jumps and quadratic variation give joint convergence with the noise. Martingale-integrand convergence for argmax requires smoothing: Gaussian pairwise near-tie occupation tends to zero and Itô-isometry bounds control the approximation. Endpoint hypergeometric sqrt(1-u) estimates control the compensator tail; qv controls the martingale tail. Brownian rank Tanaka yields 1/2 symmetric local time of the top two coordinate gap; n=2 yields the Rayleigh law. Direct independent finite-deck enumeration verified exact pathwise score-tie identity and compensator equality for five small n,m, but does not prove weak convergence. A specialist proof check of selector smoothing remains a stated risk.

## originality

PASS

The same card-guessing model is studied by Dey–Manthripragada in 2026; their accessible result is the fixed-n predictable compensator bridge integral, and the cited primary account says n>=3 actual-score law remained open. Kuba–Panholzer n=2 Rayleigh is prior. A general semimartingale rank/local-time decomposition is prior, but its application requires discrete-score martingale functional convergence, not supplied by that identity. The relevant Dey full text was inaccessible and an institutional retrieval attempt safety-blocked; best-of-knowledge originality is expressly qualified.

## value

PASS

The actual greedy score, unlike only its predictable compensator, is the natural statistic in a sequential-feedback guessing game. Identifying its fixed-type non-Gaussian distributional limit by top-rank collision local time answers a concrete statistical probability question, with an exact known two-type normalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
