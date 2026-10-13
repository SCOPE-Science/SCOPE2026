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

The proof is analytic. The critical checks are: (1) exact reduction of the source criterion under \(x=(\theta+\theta^{-1})/2\); (2) strict positivity of \(H_k'(x)\) for every integer \(k\ge2\) and \(x\ge1\); (3) the endpoint signs \(H_k(1)=-3\) and \(H_k(x)\to+\infty\); and (4) the comparison \(H_{k+1}(x_k)>0\), which forces \(x_{k+1}<x_k\).

The bundled `verify.py` checks the reduction exactly over rational inputs and performs finite numerical regression checks for the source's \(k=3\) and \(k=4\) values and for nesting through \(k=200\). These finite checks are corroborative only.

Limits: no conclusion is drawn at the equality endpoints, and no converse to the source's sufficient extremality criterion is asserted.
