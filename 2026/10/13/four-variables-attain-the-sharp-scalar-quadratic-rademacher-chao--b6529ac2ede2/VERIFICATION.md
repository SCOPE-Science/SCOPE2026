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

The proof is analytic. The finite checker is used only to verify the Walsh bookkeeping and equality-orbit classification.

For the reduction \(u=\varepsilon_1\varepsilon_2\), \(v=\varepsilon_1\varepsilon_3\), \(w=\varepsilon_1\varepsilon_4\), `verify.py` builds the exact integer evaluation matrix of the six characters \(u,v,w,uv,uw,vw\). It verifies that every coefficient basis vector has zero sum on each parity class \(uvw=1\) and \(uvw=-1\).

It then enumerates the three partitions of four coordinates and the four sign choices for each product \(c(\varepsilon_i+s\varepsilon_j)(\varepsilon_k+t\varepsilon_l)\), confirming that all twelve patterns have ratio \(\|h\|_2/\|h\|_1=2\) and correspond exactly to the twelve unordered pairs of reduced cube points lying in a common parity class.

The finite enumeration does not prove the norm inequality for arbitrary real coefficients. That inequality follows from the zero-sum four-vector lemma in `RESULT.md`. No independent audit has been performed.
