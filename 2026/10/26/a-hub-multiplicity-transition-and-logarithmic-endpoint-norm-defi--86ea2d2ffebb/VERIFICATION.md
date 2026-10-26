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

Run `python3 clique_cycle_checker.py` from this directory. The checker uses only the Python standard library. It constructs each full graph Laplacian, grounds one vertex, inverts it exactly over rational numbers, and enumerates all edge columns of both orthogonal projections. Separately, it inverts the smaller cyclic resolvent over rational numbers, computes all six claimed expressions, and asserts agreement for every edge in every tested configuration.

The certificate prints `CLIQUE_CYCLE_JOIN_CERTIFICATE_OK cases=31 exact_columns=1205` on success. The checked cases are all combinations of hub counts 2–5 and rim sizes 4–10, plus (2,15), (3,13) and (5,12). These cover only finite instances. The analytic argument in RESULT.md supplies arbitrary integer sizes and the fixed-h asymptotics; finite numerical or rational tests alone cannot prove them.

The originality comparison inspected source texts for the previously known graph-join resistance formula and the canonical cycle-space projection framework. A general join effective-resistance formula does not by itself assert these endpoint norms; earlier publications may still contain an equivalent absolute-current sum, so independent bibliographic confirmation is outstanding.
