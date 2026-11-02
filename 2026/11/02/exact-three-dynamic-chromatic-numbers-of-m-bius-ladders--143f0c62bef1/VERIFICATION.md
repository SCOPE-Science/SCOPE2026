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

# Verification instructions and limits

Run `python3 verify.py` in the folder containing that script. The program uses only the Python standard library, constructs each Möbius ladder with the edges defined in the theorem, and directly computes its graph square by two-step adjacency expansion. It checks the four explicit seeds (including the six-color exception), the three length-four insertion series through 30 extensions each, and the period-four constructions for \(m=6,10,\ldots,202\). It verifies that the graph squares for \(m=3,4\) are complete, then independently enumerates the four-vertex independent-set candidates of the sixteen-vertex graph, finding none; there are 48 independent triples. The final output on a successful replay is `VERIFY_OK`.

These finite tests confirm explicit constructions and small obstructions, not the theorem for all lengths. The infinite conclusion uses the local square constraint equivalence, four-color rigidity, the exceptional independent-set argument, and the length-four insertion proof in `RESULT.md`. Historical priority and independent mathematical audit are not established by running this script.
