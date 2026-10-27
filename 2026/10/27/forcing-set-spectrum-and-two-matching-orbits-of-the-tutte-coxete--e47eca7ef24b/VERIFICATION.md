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
Reproduce the duad–syntheme exact census with `python3 verify_forcing.py` and `python3 verify_independent.py`. The first program checks two 144-element orbits and all 32,768 subsets of each representative by complete superset enumeration; the second uses 30-vertex exact-cover matchings and direct tests for subset sizes four through six. Outputs are included as text. The finite computation exhausts the whole stated graph; it does not establish any extension to other graphs.
