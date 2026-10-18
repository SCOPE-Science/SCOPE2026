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

# Reproducible verification

Execute `python3 verify_tree_outbreak.py` with Python 3 and compare its one-line sorted JSON output exactly against `certificate.json` (ignoring only the final newline if a text viewer strips it). There are no third-party runtime dependencies, randomized steps, network calls, or external data files.

The code enumerates unrooted-tree classes of orders \(1\) through \(11\) by complete leaf addition and canonical center-rooted representations, obtaining \(1,1,1,2,3,6,11,23,47,106,235\). For every class it enumerates all nonempty vertex subsets and their exact induced-connectivity/edge-boundary pairs. Histogram collision sizes are empty for orders at most ten and exactly \([2]\) at order eleven. It then independently enumerates all \(1024\) bond-state subsets for each witness, verifies the identity converting boundary-subtree counts to open-edge-state coefficients, and checks all exact coefficients coincide. The certificate records the two edge sets, their canonical codes, the common 42-term boundary-subtree profile, all 56 nonzero common edge-state coefficients, and the exact distribution at transmission probability \(1/2\). The result is an exhaustive finite proof only because coverage of the generator and exactness of each profile test are independently justified in `RESULT.md`.

An additional independent census using NetworkX's nonisomorphic-tree generator agreed with all profile collision counts through eleven vertices; the delivered standalone verifier does not depend on NetworkX. All algebra and assertions use integers. No general-network, larger-tree, stochastic-SIR, or noisy-inference extension is verified here. Independent audit has not been performed.
