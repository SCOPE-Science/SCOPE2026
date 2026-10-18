---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification details

The included `verify_friendship.py` is a dependency-free executable finite test. Its implementation constructs the one-dimensional friendship graph from incidence lists, derives induced strong-gradient pairs from unique preceding neighbors, and checks that **every face** agrees with the proposed combinatorial decomposition (not merely the f-vector). For \(1\le n\le4\), it enumerates every ordering of all graph vertices; for \(n=5\), subset dynamic programming computes all reachable matching masks with the same local rule without enumerating full permutations. It also computes simplicial mod-two boundary ranks by binary column reduction.

The expected output and a true execution transcript of the public verifier appear in `verification_output.txt`. Results: \(n=1\): six isolated vertices; \(n=2\): first Betti number 13; \(n=3\): second Betti number 33; \(n=4\): third Betti number 89; \(n=5\): fourth Betti number 253, with no other reduced mod-two homology in those cases.

The infinite classification does **not** follow from testing these values: it follows from the proof's exhaustive case split for an arbitrary vertex order, the realization of all permitted maximal choices, and the explicit nullhomotopy of each cone attachment. No independent mathematical audit has been performed.
