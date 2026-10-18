---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For crown graph Cr_n=K_n,n-M_n, constrained neighborhood sums are x_i+Y-y_i at a_i and y_i+X-x_i at b_i if their own label is 0 or 1. Synchronized x_i=y_i=z_i with sum_i z_i=3 gives a feasible weight-6 function. If total <6, a shore has weight <=2; at a zero coordinate the opposite lower bound forces a contradiction. At equality, the detailed 0,1,2 side-total case split excludes X<=2 and Y<=2 for n>=4; X=Y=3 then forces x_i=y_i on low coordinates and equality of totals forces the remaining high coordinate to agree. Thus precisely binom(n+2,3) optima. Independent exhaustive bounded-weight label searches yielded Cr_4:20, Cr_5:35, Cr_6:56, Cr_7:84, all synchronized; Cr_3 had 18 optima of which only 10 synchronized, confirming the excluded boundary. These finite checks are not the all-n proof.

## originality

PASS

Primary Hao–Jalilolghadr–Mojdeh (2023) establishes the perfect DOUBLE Italian closed-neighborhood interval definition and broad extremal/complexity facts. Its accessible search-index sections contain no claim implying crown synchronization or the binomial minimizer census; complete PDF could not be inspected after open access failed and authorized Oxford retrieval returned VPN-disconnected. Relevant published Resultary perfect ROMAN domination of crown graphs computes a different exact-one-2-neighbor invariant with weight 4; restrained-domination and complete-multipartite perfect Italian results likewise use different constraints/graphs. The exact fixed graph and scalar value PLUS full optimizer synchronization remain unimplicated in inspected mathematics; PASS is best-of-knowledge subject to named primary full-text risk.

## value

PASS

Crown graphs are canonical dense regular bipartite perturbations; the missing matching causes a nontrivial rigid equality phenomenon n>=4 distinct from the hexagonal n=3 boundary. The exact complete optimizer family and binomial count are reusable structural graph-domination invariants, not just one brute-force number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
