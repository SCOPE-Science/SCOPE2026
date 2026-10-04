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

The proof was replayed from the explicit unit ball.

1. The four strip constraints defining \(K_w\) give the exact support inequalities for every centered ellipse \(E_Q\subset K_w\).
2. Adding the support inequalities yields \(\operatorname{tr}Q\le2q_*\), where \(q_*=\min\{1,(1+w)^2/2\}\).
3. The eight vertex matrices average exactly to \((1+w^2)I/2\), so \(K_w\subset\lambda E_Q\) forces \(\lambda^2\ge(1+w^2)\operatorname{tr}(Q^{-1})/2\).
4. For the two positive eigenvalues of \(Q\), \(\operatorname{tr}(Q^{-1})\ge4/\operatorname{tr}Q\). Hence \(\lambda^2\ge(1+w^2)/q_*\).
5. The circle \(\sqrt{q_*}B_2\) lies in \(K_w\), and every vertex lies on the Euclidean circle of radius \(\sqrt{1+w^2}\); this attains the same dilation.
6. Differentiating the two squared branches shows strict decrease before \(\sqrt2-1\) and strict increase after it, so the minimizer is unique.

No finite search, numerical fit, or symmetry assumption about the optimal ellipse is needed for the proof. Numerical sampling performed during exploration was only a sanity check and is not evidentiary.
