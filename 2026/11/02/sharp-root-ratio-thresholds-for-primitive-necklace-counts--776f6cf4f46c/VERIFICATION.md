---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For integer alphabet q>=2 and n>=4, set g_n=log(M_n(q))/n. Möbius inversion yields M_n=(q^n/n)(1+r_n), with |r_n| bounded by a geometric series of proper-divisor terms. The exact second-difference inequality D_n=g_(n+2)-2g_(n+1)+g_n< -L(n)+E(n,q), L=(2log n-3)/(n+2)^3 and E=[2q/((q-1)n q^(n/2))]*(1+2q^(-1/2)+q^-1), proves all n>=6 for q>=9 and all n>=23 for q>=2 by two strict ratio inductions. Exact small signs D_3>0, D_4<0, D_5<0 for q>=6; independently recomputed all 115 missing strict sign tests q=2..8, n=T(q)..22 and seven reverse witnesses D_(T-1)>0 by integer powers. Thus T(2)=14,T(3)=8,T(4,5)=6,T(q>=6)=4 are genuine smallest infinite tails; q restricted to integer, finite certificate used only for finite remainder.

## originality

PASS

Sun 2012 Remark 1.1 proposed these exact thresholds explicitly but supplied no proof, and Theorem 1.1 only provides large-index eventual monotonicity. Chebolu et al 2026 establish unrooted log-convexity, not the rooted negative second difference. The new exact proof appears to solve the proposed four-case cutoff conjecture; priority qualified by possible equivalent unpublished or unindexed proof.

## value

PASS

Resolves a named finite-field irreducible-degree/root-ratio threshold conjecture with exact smallest indices and a uniform all-integer necklace extension; analytic-infinite and finite-exact components are independently useful for monotonicity of enumerative sequences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
