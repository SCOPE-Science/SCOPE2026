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

The standalone program `verify.py` uses only the Python standard library. Run it beside `verify_output.txt` with:

```sh
python3 verify.py
```

The output should conclude with `VERIFY_OK`, as preserved in `verify_output.txt`.

It checks the six-period coloring and all 30 residue positions in each of the six explicitly named covering classes; verifies the exact finite packing spacing on a set containing several periods; recomputes the finite-window contradiction (2201 allowable broadcast incidences versus 2202 necessary); and checks the rational capacity inequality \(88/15<6\) with exact rational arithmetic.

The periodicity arguments in `RESULT.md` extend the finite residue checks to every vertex of the two-way infinite path. The lower bound is proved for **arbitrary** four-color packings, regardless of a coloring's periodicity. The program corroborates, rather than substitutes for, the mathematical proof. The published five-color upper construction is credited; independent external audit has not been performed.
