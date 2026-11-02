---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

A minimum edge cover of K_{n+1,n} must have n+1 edges and be the graph of a surjective word from n+1 labeled positions to n colors; exactly one color occurs twice. Replacing either duplicate with a blank gives the endpoints of a unique edge of the permutation star-transposition Cayley graph S_{n+1}. One-coordinate changes correspond exactly to incident root edges, hence X_n=L(S_{n+1}). Root S is n-regular bipartite with (n+1)! vertices, giving |V|=n(n+1)!/2, degree 2n-2, edges n(n+1)!(n-1)/2, triangles (n+1)! binom(n,3), chi=omega=n and independence (n+1)!/2. Classical star-factorization distance (central cycle length-1 plus off-center cycle length+1) yields diameter floor(3n/2), and the line-graph endpoint distance formula plus explicit conjugating extremal permutations attain this bound. In K_{n,n} the n! perfect matchings are isolated under one-edge replacement. Independent Python enumerated all surjective words, direct one-coordinate adjacency and full BFS distances n=2..5, reproducing (6,3),(36,4),(240,6),(1800,7) vertex/diameter pairs. The proof, not finite enumeration, is all n>=2.

## originality

PASS

PASS for the exact optimum-cover exchange-graph identification and consequent all-parameter graph census; the diameter of the permutation star Cayley graph and factorization formula are established background and not independently novel. A known line-graph representation under alternate surjective-word terminology remains the key bibliographic risk.

## value

PASS

Single-edge reconfiguration of minimum edge covers is a natural discrete optimization state graph. The exact identification with a classical Cayley-network line graph yields connectivity, diameter, coloring, independent-set and triangle counts, and a sharp structural discontinuity between K_{n,n} and K_{n+1,n}. This classification is a motivated infinite family, not simply a known restatement of star graph diameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
