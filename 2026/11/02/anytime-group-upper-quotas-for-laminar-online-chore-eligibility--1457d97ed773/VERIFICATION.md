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
# Reproducibility

Unpack `verify_laminar.py` alongside this file. Run `python3 verify_laminar.py` with a standard Python 3 interpreter; it requires no nonstandard libraries, external data, web access, or random state from outside the file. Its deterministic tests use exact `fractions.Fraction` arithmetic and fixed pseudorandom seed. A successful replay prints `VERIFY_OK histories=50983 group_inequalities=2198655`.

The program checks the laminar tree construction, proper-child partition identity, selection threshold, full group excess, and individual one-chore deletion condition after each allocation. It enumerates short input words for representative hierarchies and checks many longer deterministic pseudorandom examples. The computation is necessarily finite: it does **not** validate all hierarchy sizes or all input lengths. Those quantifiers are proved by the induction in `RESULT.md`. The mathematical claim does not require computer-assisted exhaustive certification.
