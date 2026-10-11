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

The proof was reconstructed from the exact derivative equation
\[
P_t'(z)=nz^{n-1}+tQ'(z).
\]
For \(Q'(0)\ne0\), set
\[
\rho_t=(t|Q'(0)|/n)^{1/(n-1)},\quad
\theta=\arg(-Q'(0))/(n-1).
\]
After \(z=\rho_t u\), the critical equation tends to the polynomial whose distinct simple roots are \(e^{i\theta}\omega_{n-1}^k\). Thus all \(n-1\) critical points have uniform expansions \(\rho_t e^{i\theta}\omega_{n-1}^k+O(\rho_t^2)\).

The root implicit-function theorem gives \(n\) expansions \(\omega_n^j+O(t)\). This proves \(\sigma_2=1+O(t)\). Because \(n\ge4\), \(t=O(\rho_t^3)\) and the full finite distance matrix is
\[
|a_j-\zeta_k|=1-\rho_t\cos\left(\frac{2\pi j}{n}-\theta-\frac{2\pi k}{n-1}\right)+O(\rho_t^2).
\]
Taking first the minimum over \(k\) and then the maximum over \(j\) is valid with uniform finite-index remainders. This yields the proposed defect and no hidden extremizing branch.

Modulo \(T=2\pi/(n-1)\), the \(n\) zero angles form exactly an \(n\)-point equally spaced grid. The farthest nearest-grid distance lies between \(\pi/n\) and \(\pi/(n-1)\); the two explicit directions \(Q(z)=z\) and \(Q(z)=e^{-i\pi/n}z\) realize its two endpoints.

As a nonessential independent numerical check, complex polynomial root computations for \(n=4,5,7,10\) and \(Q(z)=e^{0.43i}z+(0.37+0.30i)z^2-0.19iz^3\) at \(t=10^{-5},10^{-7},10^{-9}\) gave scaled defects moving toward the predicted values \(0.618578,0.778893,0.899605,0.947000\), respectively. The first two degrees show especially clear numerical convergence; larger degrees converge more slowly because \(\rho_t\) decreases slowly with \(t\). These tests were not used to infer the infinite asymptotic.

Unproved limits: no result is given for \(Q'(0)=0\), no uniform remainder over varying \(Q\), no classification of all equality cases of the global variance inequality, and no result for higher \(p\)-variance deficits.
