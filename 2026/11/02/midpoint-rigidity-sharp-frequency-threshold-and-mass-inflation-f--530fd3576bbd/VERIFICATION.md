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

# Verification of the three-node trigonometric SBP classification

Run `python verify_fsbp.py` with SymPy installed. The program builds the nodal evaluation and derivative matrices from \(\{1,\cos(\omega x),\sin(\omega x)\}\), calculates \(D=V'V^{-1}\), and compares its entries with the claimed closed form. It checks all nine entries of \(PD+D^{\mathsf T}P=\operatorname{diag}(-1,0,1)\) and the exact basis-derivative identities. It also checks symbolic formulas for norm mass, its gap derivative, Simpson limits, the leading mass error, and both blowup coefficients.

The general off-center cardinal derivative is verified symbolically and seeded off-center frequencies/nodes are tested for the forced nonzero center diagonal. Additional seeded samples test exact sign regions and overintegration. The script reports **668 passed checks**. The full theorem and uniqueness, strict inequalities for every frequency and nonexistence outside the feasible range are proved in `RESULT.md`; finite tests cannot replace these arguments. No external or independent audit was performed.
