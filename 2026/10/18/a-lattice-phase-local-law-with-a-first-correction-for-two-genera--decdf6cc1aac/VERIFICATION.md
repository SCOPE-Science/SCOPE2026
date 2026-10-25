---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

Canonical union-irreducible singleton/doubleton generators yield exact weights C(n,s)2^{-s(s−1)/2}. Ratios w_{s+1}/w_s=((n−s)/(s+1))2^-s anchor uniquely at q solving (q+1)2^q=n. For centered j the oriented products expand log(w_{m+j}/w_m)=(ln2)F_theta(j)+F_theta(j)/(m+1)+uniform second-order error on a central window. Monotone ratios give uniform quadratic tails and summable remainder, while normalization replaces F by F−mu, proving global ℓ1 O((m+1)^-2). Independently compared exact weights at n=4096,65536,1048576: leading ℓ1 errors about .0661,.0493,.0414 versus corrected .0112,.00459,.00438. Finite checks corroborate; the uniform tail estimates prove the asymptotic.

## originality

PASS

The finite coefficient binomial sum, graph correspondence and theta-oscillating normalizing polynomial are already known (OEIS and Paris/Gawronski--Neuschel). The accepted new result is a uniform signed first correction in ℓ1 for the coefficient-index distribution of a natural labelled union-closed team model, not a new count or leading normalization.

## value

PASS

The intrinsic singleton-generator count is a natural size statistic for union-closed team families. Its bounded-width, phase-dependent, non-Gaussian local law and precise first correction are independently useful for sampling and probabilistic structural analysis; it is not an arbitrary finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
