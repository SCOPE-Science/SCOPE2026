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

Contracting each color's demanded equivalences gives exactly B_(n-d)/B_n for identification rank d; independent colors multiply. An uncolored tree of four worlds has three nonredundant colored demands, so the larger-component probability is O_r(m^4 rho_n^3)=o(1). On a triple, an all-one-color path closes by transitivity; a two-color path gives a wedge, with six center/leaf choices for a given color pair on each unordered triple. Extra internal identifications or outside attachments cost another Bell-ratio factor. In joint factorial moments the disjoint configurations yield the product Poisson moments; a connected overlap on v>3 worlds costs at least v-1 total rank, hence O(m^v rho_n^(v-1))=o(1), and distinct motifs on three worlds cost at least rank three. The same extra-demand bounds control the expected difference between open motif and component counts. Pair coincidences concentrate around their diverging means by the fixed Bell ratios, and only tight many are in triples. To complete the monochromatic-pair step explicitly, multiple colors on a named pair contribute in expectation binom(r,2) binom(m,2) rho_n^2=o(1); thus those pairs can be discarded. Nonisolated vertices are o_P(m). At quantifier rank q, match touched components by isomorphism, reserving a fresh one when needed; q abundant components of each type suffice while rare counts match exactly. This gives the relational first-order limit by discrete convergence of rare counts, with no nontrivial announced predicate. Below the window, all two-link witnesses have vanishing expected count. Above it, a monochromatic triple count has diverging mean with disjoint-pair moments asymptotically factorized; relative overlap terms are O(1/m + 1/(m^2 rho_n))=o(1). The finite restriction formula follows by selecting the omitted vertices attached to surviving blocks and independently partitioning the complement. Independent bounded enumeration at n=5,m=4 gives exact open motif numerators 20 and 5400 and checks one restricted partition probability (/workspace/review_checks.py, partitions). The supplied checker was inspected, not executed; it checks finite identities, not asymptotic independence or logical convergence.

## originality

PASS

Pass for the joint typed common-knowledge component theorem and its explicit first-order mixture, not the individual birthday-collision mechanism, the one-pair wedge intensity by itself, the Bell identities, or the finite-rank method. The strongest matched fixed-alphabet result covers the wedge marginal by occupancy transfer, but does not cover the requisite joint geometry.

## value

PASS

The joint law distinguishes two ways for knowledge to connect three worlds, even when no single agent observes a triple. It yields a nontrivial limiting absence probability and identifies the limit for every fixed first-order sentence. Classical marginal birthday counts alone do not supply that information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
