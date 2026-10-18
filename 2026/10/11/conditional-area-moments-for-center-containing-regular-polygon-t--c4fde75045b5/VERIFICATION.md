---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-11.md",
      "INDEPENDENT_AUDIT_2026-10-11.json"
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

Uniform distinct triples correspond to positive cyclic compositions \(a+b+c=n\), counted with \(n/3\) initial-vertex multiplicity; strict origin inclusion holds precisely when each cyclic gap is smaller than \(n/2\), excluding diameter boundaries. The admissible composition count is \((n^2-1)/8\) for odd \(n\), \((n-2)(n-4)/8\) for even \(n\). For such a triangle, \(A/R^2=2\sin(a\pi/n)\sin(b\pi/n)\sin(c\pi/n)=[\sin(2a\pi/n)+\sin(2b\pi/n)+\sin(2c\pi/n)]/2\). Weighted one- and two-gap sine sums yield \(\mu_n=3H_n/(2N_n)\) and \(q_n=(3U_n+6C_n)/(4N_n)\); their listed finite geometric-series evaluations reproduce both parity formula families. Independent direct gap enumeration for n=3..99 (n=4 has empty event) confirmed probabilities, first and second moments and parities, while the all-order proof follows from the exact sum identities. The asymptotic expansions give common variance \(3/8-3/\pi^2\) but corrections \(-(12/\pi^2+5/8)/n^2\) for odd n and \(-3/(4n)\) for even n.

## originality

PASS

Best-of-knowledge closed forms for conditional first and second regular-polygon triangle areas and sharp parity-dependent variance convergence do not follow from inspected unconditional expectations or known containment probabilities. The exact 2006 primary PDF remains unread and is a genuine priority risk, not an automatic rejection.

## value

PASS

The regular-polygon triangle is a canonical discrete geometric probability model, and conditional area variance given center containment is a natural precise invariant not determined by known unconditional formulas. The sharp even/odd boundary correction makes the exact n-dependent moment result independently useful to geometric probability and discrete-to-continuum comparisons; it is not an arbitrary slice or recomputation of the known unconditional table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
