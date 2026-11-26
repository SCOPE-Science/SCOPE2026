---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For p not dividing b, normalization gives independent digit contributions in directions (b^j,b^-j). These lie on y=x modulo p^u; v_0 and v_1 generate that entire subgroup since v_1-b^-1 v_0 generates its first-coordinate difference ideal. This includes the diagonal case u=a. Unrestricted positions contain linearly many periods of directions; every nontrivial subgroup character contracts on at least one occurring direction by the availability of digits 0 and 1. The possibly length-dependent leading-digit contribution has modulus at most one. Fourier inversion gives exponential mixing for fixed b,p,a (also when b=1 modulo p^a and the period is one). The zero pair is unchanged by removing normalization. For p dividing b, h=ceil(a/e) digits at each end suffice and are disjoint as soon as ell>=2h. The low block is uniform modulo p^a. Reverse divisibility requires the leading digit to be a multiple of p^min(a,e); there are b/p^min(a,e)-1 such permitted digits. If a>e, the next h-1 digits then meet one uniform congruence modulo p^(a-e), since b/p^e is a unit and p^(a-e) divides b^(h-1). The valuation pmf follows by subtracting adjacent tails, including t=0 and t=tau. An independently implemented raw-residue exact DP confirmed 27 stabilization cases and seven support/total-variation comparisons.

## originality

PASS

Best-of-knowledge pass for the all-base fixed-prime-power law: exponential joint mixing on the exact subgroup in the unit case and an exact arbitrary-prime-power cutoff in the nonunit case. Known decimal divisibility rules and binary squarefree/local examples are not credited as novel.

## value

PASS

The dependence of an integer and its reversal is essential for local gcd factors. This computes the exact dependence subgroup, the transition in the valuation tail, and a concrete finite-length rule for the potentially nonuniform leading digit in the nonunit case. It replaces an independence heuristic with explicit joint probabilities for every fixed prime power.

The dated certificate retains the supplied scientific assessment, sources and limitations.
