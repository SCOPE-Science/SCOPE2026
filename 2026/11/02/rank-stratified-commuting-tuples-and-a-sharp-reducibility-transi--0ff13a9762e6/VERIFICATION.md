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

# Reproducibility and checks

The standalone `verify_commuting.py` uses only Python's standard library. Its independent direct enumerator builds all first-superdiagonal row blocks and second-superdiagonal rectangular blocks in each small test, calculates each required commutator entry in the field, and counts zero-commutator tuples. Its predicted count instead uses the Gaussian product for the number of matrices at each rank; both routes are compared exactly. It separately enumerates rank matrices to check that product. Central coordinates contribute a free factor.

Run `python3 verify_commuting.py`. Tested field sizes are \(2\), \(3\), and \(4\), with genuine polynomial arithmetic over \(\mathbb F_4\). Ten configurations passed, including \(m=0\), \(m=1\), two- and three-tuples, middle block dimensions one through three and final block dimensions one and two. Expected final line: `THREE_BLOCK_RANK_STRATIFIED_COMMUTING_OK 10`.

This finite enumeration does not establish arbitrary tuple lengths, dimensions, field sizes, or geometric irreducibility. Those follow from the rank-normal-form argument and closure proof in `RESULT.md`. No independent audit was performed.
