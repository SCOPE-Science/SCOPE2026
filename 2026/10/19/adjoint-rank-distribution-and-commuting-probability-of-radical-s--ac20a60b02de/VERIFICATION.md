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

# Verification and reproducibility

The included Python 3 program `verify.py` constructs multiplication in a \(2n\)-dimensional basis, then constructs the complete linear map \(\operatorname{ad}_x\) for each \(x\) by independent pairwise multiplication. Its Gaussian elimination is over the actual field, including the quotient-field realization \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\). It exhaustively checks \((q,n)=(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(4,2),(4,3),(5,2)\). All computed histograms agree with the closed formula and sum to \(q^{2n}\); the program terminates with `VERIFY_OK`.

The general theorem relies on a separate proof by commutator rows, incidence-forest independence, one full-cycle linear dependence, and a weighted transfer trace. Finite experiments neither prove infinite parameter formulas nor establish uniqueness in the literature. No independent external mathematical audit was performed.
