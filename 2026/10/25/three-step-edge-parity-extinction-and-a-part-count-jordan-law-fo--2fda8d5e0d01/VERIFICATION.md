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

# Computational checks and limits

`verify.py` is a standalone Python 3 program requiring only the standard library. Run from the directory containing it:

```sh
python3 verify.py
```

Expected exact diagnostic:

```text
LINE_GRAPH_EVEN_PARTS_VERIFY_OK graphs= 164 rank_checks= 492 exhaustive_graphs= 6 exhaustive_states= 12816
```

The script constructs the line graph's XOR matrix from shared endpoints directly, not from the proof's incidence factorization. For all 164 ordered part profiles with two through six parts, even sizes selected from 2, 4, 6, and underlying total vertex count at most 16, it verifies predicted binary ranks at powers one, two, three, and zero third powers. It also exhaustively simulates all bit configurations for six graphs whose line graphs have at most 12 vertices, checking all cumulative extinction populations. The 12,816-state count is a finite enumeration, **not** an infinite proof. The unrestricted proof relies on incidence-image, kernel and part-sum calculations in RESULT.md. Independent audit has not occurred.
