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

# Verification notes

The claim is an exact analytic consequence of the conditional Haar conjugation second moment. The critical identity is
\[
\mathbb E_V |\langle y,V^\dagger A Vx\rangle|^2
=\frac{d(1-|\lambda|^2)}{d^2-1}
+\frac{d^2|\lambda|^2-1}{d^2-1}|\langle y,x\rangle|^2,
\]
for unit \(x,y\), unitary diagonal \(A\), and \(\lambda=\operatorname{tr}(A)/d\). It gives a closed affine recursion and the final formulas. The boundary \(|\lambda|=1\) is handled separately, and the time parameter is every integer \(t\ge0\).

The supplementary `verify.py` uses NumPy/QR Haar samples with an explicit fixed seed to compare the first and second moments for dimensions two, three and four, including a case of negative \(\gamma\). Command: `python verify.py`. Its finite Monte Carlo tolerances are not certificates; every displayed identity and asymptotic limit rests instead on the preceding proof. No automated external validation, independent audit or global originality certification is claimed.
