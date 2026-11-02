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
# Reproducible checks and limits

Run `python3 verify_crown_superdom.py` from this directory. The script uses Python 3.9+ and standard-library modules only. It recomputes original graph adjacency from \(a_i\sim b_j\) exactly when \(i\ne j\), and independently checks the witness definition of super domination for every subset in the cases \(4\le n\le8\). It compares each cardinality count and every minimum configuration with the symbolic predictions.

For \(4\le n\le10\), it builds the entire minimum-configuration token-jump graph, verifies the vertex number and degree, and checks breadth-first-search distances from one fixed configuration to every target against the exact formula. Simultaneous ground-index permutations give vertex transitivity, so these checks cover all pairs in each tested order. At \(n=4\), it explicitly verifies six isolated states; for \(5\le n\le10\), it verifies diameter five and a single distance-five state. Successful execution ends with `VERIFY_OK`.

Finite enumeration cannot by itself prove the infinite classifications or exclude unseen publications; those are addressed, respectively, by the separate mathematical proof and the qualified literature comparison.
