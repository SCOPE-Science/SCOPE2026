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

For unit-positive cross edges and strictly positive-gain earliest-created tie-breaking, the initial monochromatic run r creates r singletons; the first opposite-color arrival joins the earliest singleton, and thereafter that mixed coalition remains earliest and gives a maximizing positive gain to every arrival. Hence exactly r-1 early vertices remain stranded and Q=1-(r-1)/a (or symmetric). Hypergeometric run probabilities sum to one; separator symmetry proves mean 1-1/(a+1)-1/(b+1)+2/(a+b); strict convexity yields star minima and balanced maxima for fixed N; extreme-order statistics give Beta(a,1) as the other part grows, and bounded deficit gives the both-growing limit. Independently simulated direct greedy choices on all side-arrival words in tested small parts and verified rational means; proof covers every positive a,b.

## originality

PASS

Bullinger and Romen model online additively separable coalition formation under random arrival and show generic approximation guarantees, not exact distribution or Beta limit on unit-positive bicliques. Flammini et al. 2021 address related adversarial online coalition formation; only the accessible article summary was inspected and full-text noncoverage is not asserted. Exact tie-breaking is pivotal.

## value

PASS

The biclique is a canonical dense positive coalition network; this exact all-size distribution and fixed-size limit exhibit persistent random-order welfare loss at stars despite concentration at balanced growing networks. The explicit tie-breaking dependence makes the invariant precise and practically interpretable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
