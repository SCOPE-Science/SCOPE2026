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

# Verification

The bundled `verify.py` uses two independent finite descriptions of a one-point extension. The first directly checks every four-set containing the new point. The second builds the mixed-rank conflict hypergraph and tests independence. For every legal labelled parameter 3-graph on at most five vertices, the two resulting weight polynomials must agree exactly.

The same replay checks coefficientwise domination by the empty-parameter-structure polynomial and strict loss at degree two whenever an old hyperedge exists. Finally, it enumerates labelled triangle-free graphs independently through seven vertices and requires the totals
\[
1,1,2,7,41,388,5789,133501.
\]

Run:

```text
python3 verify.py
```

A successful replay ends with `VERIFY_OK`. These computations test finite instances and the translation between the two combinatorial descriptions; the infinite theorem rests on the proof in `RESULT.md`, not on extrapolation from the enumeration.
