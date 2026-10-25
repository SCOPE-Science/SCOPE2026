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

# Reproducible mathematical checks

Run `python3 verify_exterior_jordan.py` with Python 3 and no external packages. This code constructs each wedge-multiplication map from bitmask monomials, computes modular ranks of every positive power, and compares both graded and ungraded ranks and resulting Jordan multiplicities with the binomial formulas. Tested all characteristic–dimension–rank triples with characteristic \(3,5,7\), \(2\leq n\leq8\) and \(0\leq r\leq\lfloor n/2\rfloor\): **69** full matrix-power cases. Independently enumerated all \(729\) four-dimensional bivectors over \(\mathbb F_3\) and all \(15{,}625\) over \(\mathbb F_5\), checking their ranks and the orbit-frequency predictions. Verified the dimension-eight modular Jordan partitions. Expected success marker: `VERIFY_OK_EXTERIOR_QUADRATIC_JORDAN 69 matrix-power cases`.

Proof dependencies are explicitly identified in RESULT.md: exterior Darboux form, squarefree module decomposition, the published integral diagonal form of Boolean inclusion matrices, and the classical alternating-form orbit formula. The verifier checks finite cases only, uses prime fields (not all extensions), and cannot certify either infinite-parameter correctness or historical novelty. Independent audit has not been performed.
