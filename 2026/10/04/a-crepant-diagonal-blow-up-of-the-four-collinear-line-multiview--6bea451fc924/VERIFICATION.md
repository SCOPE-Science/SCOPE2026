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

The bundled `verify_crepant_resolution.py` was executed from the packaged path with exact SymPy arithmetic. It reconstructs the cross-ratio numerator, changes to difference coordinates, checks
\[
\det\operatorname{Hess}(q)=2\prod_{i<j}(v_i-v_j),
\]
and, after the normalization \((v_1,v_2,v_3,v_4)=(0,1,2,3)\), obtains
\[
q=-3ab+4ac-bc,\qquad \det\operatorname{Hess}(q)=24.
\]
It then checks all three standard blow-up charts of the transverse origin and verifies that the only critical point of each chart equation lies off the strict transform. The execution prints `VERIFY_OK`.

The script does not certify the global line-bundle identities or canonical divisor formula. Those steps are proved in `RESULT.md`: \(N_{\Delta/(\mathbb P^1)^4}\cong\mathcal O(2)^{\oplus3}\), \(D_v|_\Delta\cong\mathcal O(4)\), the normal quadratic is therefore constant, and the codimension-three discrepancy \(+2B\) cancels the multiplicity-two strict-transform term \(-2B\).

No independent audit has been performed.
