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

# Verification details

The theorem is proved in `RESULT.md` for all integer parameters in the stated domain. `verify_spider.py` is a finite corroboration: it enumerates valid induced vertex subsets, computes complete augmented simplicial boundary ranks over \(\mathbb F_2\), and evaluates signed Lefschetz traces on every branch permutation for the indicated small parameters. Its actual run reports 45 exact Betti-vector matches and 1436 symmetry trace matches. These checks do not establish arbitrary-size acyclicity, integral torsion-freeness, or infinite-parameter homotopy claims; those follow from the complete nerve, join, Mayer–Vietoris, and skeleton proof.

Run with `python3 verify_spider.py` from the directory containing the script; compare standard output with `verify_output.txt`. The program uses only Python's standard library. The original graph vertices and all induced components are rebuilt rather than read from a table.

Independent scientific validation was not performed.
