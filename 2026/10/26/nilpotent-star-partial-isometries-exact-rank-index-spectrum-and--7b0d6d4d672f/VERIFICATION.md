---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

A metric-preserving partial injection of rank>=3 either stays in leaf-to-leaf symmetric inverse monoid or fixes hub; a hub-fixed map cannot be nilpotent. At rank2, hub crossings are directed i->0->j paths with i!=j, while hub 2-cycles are excluded; rank1 adds 2m single hub-leaf arrows. The remaining nilpotent leaf partial injections are exactly disjoint oriented directed paths, including isolated vertices. A j-chain contributes x^j u^{j-1} to a labeled EGF, so E_l=exp(sum_{j<=l}x^j u^{j-1}) and E_l-E_{l-1} extracts maximum chain size l (nilpotency index). This proves the exact joint polynomial and m![x^m]exp(x/(1-x))+m(m+1) total. Independently enumerated every partial injection on m+1 vertices and checked star metric/nilpotent powers for m=1..5, totals (3,9,25,93,531); the full original rank/index script was also read, but bounded counts do not prove m arbitrary. The Gumbel limit follows from independent Poisson chain counts with means rho_m^j conditioned on total size m, where rho/(1-rho)^2=m and rho=1-m^-1/2+O(m^-1). At L=floor(sqrt(m)(0.5logm+s)), tail Poisson mean rho^(L+1)/(1-rho)->e^-s; a Fourier lattice local CLT for total size has scale m^3/4 and truncated-tail mean/variance o(scale/scale^2), giving conditioning ratio1. The source provides the Fourier small/large arc estimates; the hub correction m(m+1) is negligible compared with at least m! leaf chains. The proof asserts weak convergence only, not a finite error bound.

## originality

PASS

Fernandes–Paulista original full star monoid paper classifies all elements and gives monoid cardinality, Green classes, rank and presentation; its Proposition2.1 supplies the structural split, but does not treat nilpotent rank/index distribution or a Gumbel limit (relevant source sections and entire PDF search checked). Stark 2021 component counts of random injections uses fixed domain/codomain and allows cycles, not uniform nilpotent star maps; generic assembly extremes may nevertheless imply the Gumbel mechanism. Given original algebraic object and explicit distribution, best-of-knowledge originality passes with a genuine general-assembly priority risk.

## value

PASS

The star partial-isometry inverse monoid is a natural algebraic object whose full cardinality/rank and presentation were known. The exact joint *nilpotent* rank/index spectrum and uniform-element extremal index behavior are distinct meaningful invariants, with nontrivial low-rank hub corrections and a probabilistic extreme-value transition. Specific exact spectrum supports further semigroup and random-transformation comparisons; the Gumbel centering/scaling supplies information absent from the total order.

The dated certificate retains the supplied scientific assessment, sources and limitations.
