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

With bipartition-oriented tree edges, K=B^T B is positive definite and (Kd)_uv=S_u+S_v. Connectedness forces constant signed sums s on A and t on B, |A|s=|B|t=Σ_e d_e; for c=s+t>0 these are positive. The unique solution to Jd=f on a tree is exactly the cut flow D_e, proving iff |D_e|=1. For mixed d, the invariant circle p+u1 satisfies u↦u+(s+t)h sin(u); positive definite KΔ is similar to the symmetric K^(1/2)ΔK^(1/2), with positive/negative inertia determined by d. Its positive subspace E+ is unstable at p and stable at p+π1, coincides along the heteroclinic, and is proper, thus violates transversality. If unequal s,t with r>=1 negative, q=n-1-2r<=n-3 is divisible by lcm(|A|,|B|), excluding n<=8. At n=9 only (|A|,|B|)=(6,3), (s,t)=(1,2), r=1 survive; parity and degree counts force unique signed tree. Constructive b odd, k>=2 family meets sums and extends indefinitely. Independent 32 checks of cuts, nine-vertex construction, lcm exclusions support analytic proof; no inference of arbitrary Morse–Smale behavior from criterion failure.

## originality

PASS

The exact invariant-line nontransversality mechanism and equal vertexwise signed-sum one case are established by Buescu–D’Aniello–Oliveira (arXiv:2610.10993v1) Propositions 5.11–5.12, including a six-vertex example. The present theorem explicitly restricts sharp nine-vertex minimality to unequal incident sums and derives the exact arbitrary tree cut criterion, uniqueness, and a new unbalanced family. Inspected complete HTML §5.4 does not state the unequal-class sharp onset, although the prior argument suggests extension. Qualified novelty for this exact signed-flow classification, not the underlying heteroclinic idea.

## value

PASS

A precise combinatorial criterion and sharp minimal example for a physically motivated nontransversality obstruction, extending the known balanced-sign mechanism to unequal bipartition classes. The nine-vertex threshold and unique signed topology are natural exact structural facts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
