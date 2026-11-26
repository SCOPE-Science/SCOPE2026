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

Anchoring leaves at most one moving coordinate, so there are no cells above degree one. Every vertex of the configuration graph has one double anchor; the orbit over each graph vertex consists of n!/2 configurations with transposition stabilizer. An oriented edge has one moving label and a bijection of the remaining labels to the anchors, giving a free orbit of n! lifts per edge and no orientation reversal. For connectivity, interpret one label as the spare and all others as stationary at uniquely assigned anchors. The spare can move along any graph path. Moving it to an anchor and then taking that anchor's previous label as the spare implements a transposition of the spare slot with the anchor slot. Such swaps generate all assignments; a final spare move reaches the prescribed double anchor. Connected cellular homology gives [H1]=e[Q[S_n]]−v[Ind_H 1]+[1]; semisimplicity, the decomposition of Q[H] and Frobenius reciprocity give the displayed rational module and Specht multiplicities. A transposition fixes exactly (n−2)! configurations per vertex orbit and none of the edges, giving the claimed character. The invariant edge-lift sums and vertex-orbit sums are integral bases, with twice ordinary incidence because either of the doubled labels can be the moving label at each endpoint. There are no two-cells, so the invariant H1 is exactly the cycle kernel of this matrix. After quotienting, every edge lift projects with degree one, sending the invariant cycle lattice to n! times the graph cycle lattice, of index (n!)^(e−v+1). Fixing stationary labels and moving only the spare gives a continuous section of the quotient and proves unrestricted surjectivity.

## originality

PASS

The nonequivariant ranks and freeness are covered by a stronger earlier Resultary record and are not credited as new. The distinction is the full rational label module and the exact integral image of its fixed lattice under the canonical quotient, with no inspected matching statement or theorem giving both.

## value

PASS

The rational module gives all label-symmetry multiplicities, which cannot be recovered from the previously known rank. Integrally, the quotient is split surjective before imposing invariance but the invariant lattice has a factorial-index image. Their contrast isolates concrete arithmetic information that rational transfer misses and motivates this natural one-spare regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
