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

The theorem is proved for all finite connected simple cubic graphs by the short-time fourth-moment criterion, the unit-triple equilateral lemma, the odd-cycle obstruction, and the explicit bipartite edge-colouring construction. The standalone checker is finite corroboration only.

Run in the directory containing the embedded files:

```sh
python3 verify_swift_subdiv.py
```

Expected deterministic output:

```text
VERIFY_OK examples=5 exact_phase_profiles=36 K33_colorings=12 cube_colorings=24 component_counts=4,8 fourth_moment_checks=5 max_taylor_error=1.388e-17
```

It enumerates all labelled proper three-edge-colourings for two bipartite cubic examples, checks all row sums exactly in the Eisenstein integer ring, verifies direct integer fourth moments for five cubic graphs, and constructs independent finite-dimensional Taylor evolutions from two bipartite examples to check the claimed quantum probabilities. Its nonbipartite examples test bipartition detection and fourth moments, not global nonexistence by brute force. No finite test proves an all-orders quantum identity or absence of arbitrary continuous phase solutions; those facts follow from the written proof.

The matrix-exponential Taylor truncation is to 89 orders and uses only Python's standard library. Numerical tolerances are explicit in the checker. The first public source dates are verified from arXiv submission histories, not journal dates.
