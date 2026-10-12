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

The symbolic argument in `RESULT.md` proves the claims for every complex general-position line arrangement with \(n\ge4\). Its central exact identity is the germwise coordinate change \(z_j=y_j/(1-\alpha_jy_j)=u/L_j\); independence of the complete Veronese system follows from evaluation at the \(n-1\) distinct zeros of the binary linear forms. The known resolution is the blowup of the ordinary base points; the contractible line curves have self-intersection \(-(n-2)\). This global construction is cited as established prior work. Class groups, indices, and discrepancies follow from the resulting cyclic quotient germ.

`check.py` uses only Python's standard library and exact rational arithmetic. Run `python3 check.py` and compare stdout with `check_output.txt`. For each \(n=4,\ldots,11\), all \(n\) chart coordinate decompositions of the explicit general-position arrangement \(\ell_i=u+iv+i^2w\) were tested; the polynomial-basis determinants were nonzero and the nonlinear substitution identities held at exact rational evaluation points. It also recomputes the canonical-index and intersection-count formulas.

These \(60\) finite chart checks are supplementary evidence, not a proof of any infinite assertion or an independent audit. The singular-support and tangent-cone classification is credited to prior literature; equivalence to the stronger completed-local-ring statement was not located in the inspected sources, but remains subject to unindexed-literature risk.
