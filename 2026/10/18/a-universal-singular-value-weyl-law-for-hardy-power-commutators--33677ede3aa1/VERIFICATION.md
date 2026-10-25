---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The kernel k_alpha(x,t)=(t^alpha-x^alpha)/x for 0<t<x has exact HS norm squared alpha/[(alpha+1)(2alpha+1)]. On [delta,1], factor -k=(x-t)q(x,t) with positive diagonal q(x,x)=alpha x^(alpha-2); splitting q=h+(x-t)r reduces the singular Weyl constant to M_h J^2, since remainder maps L2 to H3 with s_n=O(n^-3). Piecewise constant squeeze and explicit regular double-integration beam spectrum yield sqrt(t)N(T;t)→(1/pi) integral sqrt(h). Splitting at delta has rank<=2 cross block and low-low block unitary equivalent to delta^alpha K; the resulting counting equation N(t)=N(t/delta^alpha)+N(K_delta;t)+O(1) iterates geometrically to 2/(pi sqrt(alpha)), hence n²s_n→4/(pi²alpha). Since leading constant positive, S_p iff p>1/2 and weak critical membership; Volterra triangular eigenproblem yields no nonzero spectrum and Lidskii trace=0. An original independent checker verified seven integer-alpha HS identities and cross block 3x3 determinants zero. Boundary alpha→0 nonuniform explicitly excluded.

## originality

PASS

Crucial direct prior Deng–Fischer–Hofmann Theorem 1 proves only s_n(CJ) ASYMPTOTIC ORDER n^-2, not exact limit for alpha=1. Earlier Resultary record gives complete implicit singular spectrum of the exact same alpha=1 Hardy–Volterra commutator (opposite sign), but explicitly DOES NOT prove sharp asymptotic coefficient; the present family gives constant for all positive real alpha. Tuan–Gorenflo 1996 supplies weighted-Volterra order results and an exactly quantified unweighted fractional integral special case; it remains an unresolved possible implicit theorem overlap for part of the alpha range, recorded, but no accessible statement decisively covers full leading coefficient and all alpha. Best-of-knowledge PASS with substantial priority risk.

## value

PASS

Identifies the exact strong/weak Schatten threshold and sharp n^-2 Weyl coefficient for a nontrivial all-alpha compact commutator with singular endpoint. It upgrades known alpha=1 order estimates to a leading constant, proves it for every positive alpha by self-similar recursion, and clarifies nonuniform alpha→0; this is a meaningful spectral invariant even if other general Volterra theorems might offer an alternate route.

The dated certificate retains the supplied scientific assessment, sources and limitations.
