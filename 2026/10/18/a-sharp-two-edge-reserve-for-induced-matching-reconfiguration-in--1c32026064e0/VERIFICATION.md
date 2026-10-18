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

# Verification notes

Both standalone Python programs use only the standard library and the included JSON certificate. Run `python3 verify_incidence.py` and `python3 verify_lcf.py` in the containing directory. Both executions must end with `VERIFY_OK`. The programs independently construct graph edges in affine-incidence and LCF coordinates, verify the graph isomorphism, enumerate all induced matchings through size six, check all legal transitions, and perform exact breadth-first traversals. The affine program additionally confirms the complete line-graph isomorphism and the all-pairs compressed-metric equality.

The output text files record the executions made from these exact included programs. The certificate is supplementary data: the programs regenerate and compare its states, transitions, and mappings rather than simply trusting stored numerical logs. No infinite graph class, independent external audit, or novelty certification is established by these finite checks.
