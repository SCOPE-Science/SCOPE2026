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

# Reproduction and limitations

Two standalone Python 3 scripts constitute exact finite certificates. Run them from a directory containing `verify_kneser.py` and `verify_classical.py`, using only the Python standard library:

```
python verify_kneser.py
python verify_classical.py
```

Each script terminates normally only after all exact assertions succeed; the success markers are `KNESER_CERTIFICATE_PASS` and `CLASSICAL_CERTIFICATE_PASS`. The first enumerates every one of the 32,768 binary initial sets, computes simultaneous forcing closure, all 21 orbits of the natural 120-element label-permutation action, and all weighted shortest-path counts. The second constructs the line graph using the independent outer-five-cycle/inner-star/spoke description, exhaustively tests individual sequential forcing, constructs the entire one-token exchange graph from pair comparisons, and performs all 2,280 BFS shortest-path searches.

The checks and expected exact counts were executed directly from these source files and passed. Their finite exhaustive scope proves the specific labelled graph's counts; neither code nor evidence claims an unbounded graph-family theorem. The published zero-forcing minimum seven is credited. No independently performed scholarly audit or external certificate is claimed.
