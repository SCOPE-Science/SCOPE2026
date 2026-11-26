---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The repaired theorem retains the mathematically correct full topology classification and explicit endpoints and gap. For fair independent antiphase states, the Möbius maps are conjugate in log coordinates to shifted H_delta with Lipschitz bound |delta|<1 and bounded images. Contraction gives unique stationarity and weak convergence, and positive branch weights make the support the unique invariant compact set. Inversion swaps the two signs, and replacing theta by 1/theta postcomposes each map with inversion, proving the stated reciprocal-law identity as background. For tau<1, the maps increase, and invariance of the symmetric support gives R=F_(tau,+)(R) for its maximum. The positive root of a*tau*R²+(1-a)*R-tau=0 is >1 and yields the displayed formula. The hull images are [1/R,X] and [1/X,R]; they meet exactly when R>=a, equivalent by the polynomial sign at a to tau<=a/(a²+a+1). Touching counts as interval, strict separation gives a Cantor set by injective coding on shrinking cylinders, and tau=1 is the constant-map case. Solving for q yields the two critical fractions bracketing Q_0. Separate bounded checks reproduced (2/9,1/2,7/9) for a=2,s=1 and (4/11,2/3,7/8) for a=2,s=1/2, and reproduced overlap, separation and a lossy reciprocal pair (q=1/3 and 8/9 at s=1/2, giving theta=1/4 and 4). The uploaded checker was inspected, not executed; its recorded 2383 assertions are not a proof for all parameters.

## originality

PASS

For the frozen scope as originally presented, originality does not pass on the separately advertised full-law duality: it is directly implied by the prior Möbius recursion and its reciprocal stationary symmetry. This is coverage by implication, not a claim that the identical q-dagger formula was printed, and not a correctness defect. The complete replacement files under repairs/2 reassess the narrower contribution, namely the exact nondegenerate support transitions, critical migration fractions, and explicit endpoints and gap. They credit the singleton and reciprocity as prior tools. That distinct claim passes on the inspected evidence, not on a certification of priority.

## value

PASS

The repaired claim gives a quantitative answer to where a canonical two-patch ratio can occur, including when ratios near equal abundance are impossible and exactly where they become accessible again. Both nondegenerate transitions and the open central gap distinguish the full geometry from the known qualitative self-similarity or point collapse. The result describes stationary support only, not growth, survival or density.

The dated certificate retains the supplied scientific assessment, sources and limitations.
