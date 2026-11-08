---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Rooted Cayley tree EGF T=ze^T and arrival-time conditioning yield dF/dt=ze^{T-F} and F=log(1+tT). Marking only edges incident to the distinguished root produces A(z,q)=z e^{qT} int_0^1(1+tT)^(-q)dt. Differentiation gives H=T log(1+T)-log^2(1+T)/2. Since accepted vertices form an independent set, B_n=n-1-sum_{accepted}degree exactly. Singular transfer at T=1 gives leading (1-log2)n/2 and constant -9/16+log2/8, while fixed-degree coefficient transfer and two-root local convergence yield the empirical law. Independently enumerated all Prüfer trees and all priority permutations for n=2..6, reproducing E B4=3/16, B5=8/25, B6=305/648 and finite joint degree counts; infinite concentration rests on decreasing-time path bound/local limit, not finite enumeration.

## originality

PASS

Contat 2021 determines the exact total accepted-cardinality distribution but loses degree-weighted and edge-neighbor statistics. Krivelevich–Mészáros–Michaeli–Shikhelman 2019 has local-limit greedy density 1/2 and likely implies some limiting degree fractions, which are NOT treated as a standalone new general law. The distinct contribution is the all-finite-n marked-degree EGF with residual blocked-edge coefficient and finite-size correction. General Penrose–Sudbury parking equations could specialize implicitly; this remains a historical risk.

## value

PASS

For a uniform labeled tree, the residual edges joining two rejected vertices are a natural structural statistic distinct from the accepted set cardinality. An exact bivariate law answers joint acceptance/degree questions at every size, and its finite-size correction distinguishes local blocking from ordinary occupancy. This is not merely recomputing the known density 1/2.

The dated certificate retains the supplied scientific assessment, sources and limitations.
