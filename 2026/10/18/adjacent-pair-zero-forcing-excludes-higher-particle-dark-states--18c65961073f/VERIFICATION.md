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
# Verification record

The scientific result was reconstructed from its hypotheses, not inferred from experiments. The all-size proof uses the minimum cyclic gap, the two-outward-neighbor identity, and cyclic propagation anchored by at least one spectator particle. Each of these steps is described in `RESULT.md`.

Run the two attached standard-library scripts in a directory retaining their `artifacts/` paths:

```
python3 artifacts/verify_zero_forcing.py
python3 artifacts/verify_induction_boundary.py
```

The first script checked 35 finite graphs with three to five particles on cycles of five to sixteen sites and eight boundary examples with two particles. The second checked 7,633 local induction equations. Both runs passed. These exact finite checks are supporting evidence only; the proof establishes the full unbounded assertion. The result does not assert independent mathematical validation, infinite machine certification, or a characterization of mixed stationary states.
