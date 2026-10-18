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

The proved claim concerns arbitrary (possibly infinite) dynamic preorders with a total monotone temporal map. The formal obstruction is in `RESULT.md`; the external two-atom observation is cited as a source and the one-atom decoding is independently supplied.

Run `python CHECK.py` with Python 3. On the actual packaged checker the expected final line is:

`ONE_ATOM_DTL_VERIFY_OK decoding=1024 grid_obligations=576 preorders=34 monotone_maps=390 finite_models=3058`

The exhaustive component enumerates every reflexive transitive relation on one through three named worlds; for each, every monotone temporal self-map and every one-variable valuation. It evaluates the full substituted formula using recursive Boolean, reflexive spatial possibility, next, and eventuality semantics. The infinite component checks finite coordinate windows but is not an infinite certificate. Mathematical correctness beyond the finite tests follows only from the proof's explicit unbounded grid and finite-upset contradiction. No independent audit has been performed.
