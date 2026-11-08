---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For W_{q,n}=K1∨n K_{q-1} (q>=3,n>=2), no outer uncolored vertex can be forced before the hub receives a color, and no blade with >=2 originally uncolored outer vertices can subsequently be completed. Hence every blade initially seeds >=q-2 vertices; a hub-free start additionally requires all q-1 nonhub colors on seeded outer vertices, otherwise there is no legal first move. For a fixed proper coloring each blade contributes z^{q-2}(q-1+z), hub seeded adds z, and the hub-free failure event consists exactly of q-1 common omitted colors. Unique forced full extension prevents overcounting. Multiplying by q((q-1)!)^n gives the exact polynomial, minimum-size coefficient and probability formula for 0<=p<=1/q. Direct original-rule brute force independently matched q=3,n=2,3 and q=4,n=2, while structural counting proves all parameters.

## originality

PASS

Farr introduced the forced-colouring polynomial and its local rule. Published SCOPE complete-multipartite forcing counts use a non-isomorphic graph class; the published zero-forcing friendship polynomial uses a different propagation rule. The assessed contribution is the clique windmill family and synchronized-hub obstruction, not the general forcing polynomial definition or the n=1 complete graph boundary. Farr full primary PDF could not be obtained after arxiv and OA attempts and authorized download reported VPN disconnected; risk remains as to implicit clique-separator recurrences.

## value

PASS

The clique windmill is a natural vertex-sum of cliques with a shared hub. Its global forcing behavior is not the product of independent clique enumerators; an explicit subtraction for the common omitted color gives the full nontrivial distribution and sharp minimum seeds, useful as a test family for forced-coloring polynomials.

The dated certificate retains the supplied scientific assessment, sources and limitations.
