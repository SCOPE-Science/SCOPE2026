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

Run `python verify.py` with Python 3.10+ and SymPy. The script reconstructs the four cardinal polynomials and three step interpolants, verifies the symmetric identities and both derivative formulas, and uses rational square-root enclosures to prove opposite signs of the branch difference at \(a=0.4458209224\) and \(a=0.4458209226\). Its output includes the two component excursions at representative grids. The analytical proof, not finite testing, establishes the reduction over every admissible data vector and every evaluation point.

The numerical random samples check only 1,500 points and are not exhaustive; no independent audit, formal theorem prover or numerical certification beyond the stated exact rational inequalities is claimed. The root has no asserted elementary radical closed form. Literature comparison is bounded by accessible records and may miss unindexed equivalents.
