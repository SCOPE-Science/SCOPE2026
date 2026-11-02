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

# Reproducible exact checks

With Python 3 and no third-party dependencies, in the same directory run:

```text
python3 verify_geometry.py snub_edges.txt
python3 verify_field_census.py snub_edges.txt
```

The geometry check derives all 60 edges through exact equality in the cubic ring \(\mathbb Z[t]/(t^3-t^2-t-1)\), verifies degrees and 32 triangles, and compares with `snub_edges.txt`. Decimal approximations are used only to validate a wide distance gap, not to choose graph edges.

The first census traverses the entire \(2^{24}\)-state hypercube in Gray order, updating a cut when one bit toggles. The second independently traverses all masks using the lowest-element deletion recurrence, storing exact cuts as bytes (bounded above by 60). Both yield all 25 maximum cuts and their multiplicities. The field check computes the rational lower envelope of every affine sector energy and confirms there are no additional positive transition fields, with exact coexistence counts. The supplied `verification_output.txt` was produced by running both programs on the supplied edge file.

The result is specific to a finite 24-vertex graph; no extrapolation to infinite thermodynamic systems is verified. Independent review was not performed.
