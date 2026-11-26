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

For a fixed first order there are n−ℓ windows; contracting each specified directed block gives probability 1/(n)_ℓ of its occurrence in the other order. For displacement d≤ℓ the union is one block of ℓ+d edges (including d=ℓ, where they touch at one label); otherwise two disjoint contractions consume 2ℓ edges, and there are binom(n−2ℓ,2) such window pairs. This gives the exact mean μ and factorial second moment β=O_ℓ(n^(−ℓ)+n^(2−2ℓ)). Independent enumeration of the 720 second orders at n=6 gives (μ,β)=(2/15,1/30) for ℓ=2 and (5/6,1/3) for ℓ=1. The frozen checker was inspected but not executed; these checks do not prove the limit. The pair-incidence event has probability p with 0≤μ−p≤β. Dependence neighborhoods consist of pairs sharing an order, but any two distinct such incidences are exactly independent: conditioning on their common order gives two independent events with constant conditional probability p by relabelling. Both dependency-neighborhood sums are O(r³p²), with external term zero. Coupling counts and matching Poisson means cost at most 2 binom(r,2)β. At r≤C n^((ℓ−1)/2) the error has the stated order and the intensity tends to c²/2. Subsampling proves supercritical existence, while Markov excludes longer runs at criticality. Shorter runs exist by supercriticality at ℓ−1, or for ℓ=2 because a disjoint pair has a single-edge event of probability at least 1/2−o(1). The order-sharing expectation is O(r³p²); run multiplicities have expectation bounded by binom(r,2)β. Equivariantly chosen witnesses in disjoint order pairs have independent uniform label tuples conditional on existence, so the remaining label-intersection expectation is O_ℓ(r⁴p²/n). The successor formula expresses the run event since a directed path in a linear order cannot repeat vertices. The boundary caveat concerns failure of the same c²/2 law at fixed r, not non-Poisson behavior per se: for r=2, the common-edge count has factorial moments (n−1)_k/(n)_k→1 (any k prescribed edges of the fixed order contract into paths), giving Poisson(1). This is outside the stated ℓ≥2 theorem.

## originality

PASS

The supported distinction is the growing-family law for fixed-length literal directed labelled blocks in order pairs, including its TV bound, adjacent two-point maximum and critical order/label isolation. It is not a new Poisson approximation method, a one-edge limit, or a logic satisfiability theorem. The strongest inspected neighboring results change the coincidence object or the number of orders per witness and do not establish these claims.

## value

PASS

For independently sampled orders on a common label set, the result identifies when the longest exactly shared directed run jumps by one edge, provides an explicit probability and approximation error at the transition, and shows that the rare witnesses can be separated in both the sampled orders and the labels. Those statements distinguish the multi-order structure from a mere first moment or an isolated fixed parameter. The logic interpretation is useful within its stated growing-signature scope, not a claim about FO².

The dated certificate retains the supplied scientific assessment, sources and limitations.
