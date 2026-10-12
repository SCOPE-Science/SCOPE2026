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

The analytic proof partitions all double Roman dominating functions on \(S_{r,n}=K_r\vee\overline{K_n}\), for \(r,n\ge2\), into three mutually exclusive cases according to the number of clique vertices labeled \(2\) and \(3\). Necessity and sufficiency of the allowed independent labels are checked directly from the double Roman definition in each case.

`verify.py` independently constructs each complete split graph and tests every labeling in \(\{0,1,2,3\}^{r+n}\) for all \((r,n)\in\{2,3,4\}^2\). It compares the entire brute-force coefficient dictionary with the stated polynomial, checks \(\gamma_{dR}=3\), checks that the coefficient of weight \(3\) equals \(r\), and checks the specialization at \(x=1\).

The finite computation does not prove the formula for arbitrary \(r,n\); that is supplied by the symbolic case proof. Boundary cases \(r=1\) or \(n=1\) are not covered by the theorem or checker claim.
