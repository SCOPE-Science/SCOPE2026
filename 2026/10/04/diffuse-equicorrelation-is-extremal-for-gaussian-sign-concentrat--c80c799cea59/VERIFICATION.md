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

The proof requires only exact algebra and a classical Gaussian identity.

1. For \(\Sigma=(1-\rho)I+\rho\mathbf1\mathbf1^{\mathsf T}\), direct multiplication verifies the displayed inverse. Its diagonal is scalar, so \(D=dI\), and the eigenvalues immediately give \(\kappa_\star=(1+(n-2)\rho)/(1-\rho)\).
2. Substitution of \(\rho=(K-1)/(K+n-2)\) gives \(\kappa_\star=K\) and \(\kappa=K+(K-1)/(n-1)\) exactly.
3. The Gaussian sign arcsine identity gives the off-diagonal sign covariance \((2/\pi)\arcsin(\rho)\); the top eigenvalue of the resulting equicorrelation matrix is therefore the stated \(L_{K,n}\).
4. With \(a=K-1\), \(t=n-1\), and \(r=a/(a+t)\), differentiation gives \(F'(t)=\arcsin(r)-r\sqrt{(1-r)/(1+r)}>0\). The limit follows from \(\arcsin(r)/r\to1\) as \(r\downarrow0\).
5. For any moment-generating-function variance proxy, differentiating at zero yields \(\operatorname{Var}\langle u,Y\rangle\le s^2\) for every unit \(u\), hence \(s^2\ge L_{K,n}\). The published Gaussian Hamming-Lipschitz sign bound supplies \(s^2\le K\).

No finite experiment is used as evidence for an infinite statement. The unresolved point is the exact value of the optimal proxy between the displayed lower and upper bounds.
