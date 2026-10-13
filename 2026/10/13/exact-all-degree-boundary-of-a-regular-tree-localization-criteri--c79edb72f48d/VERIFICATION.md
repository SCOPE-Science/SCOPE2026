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

The analytic proof reduces the defining feasibility condition to the unique crossing of
\[
A(\varepsilon)=\varepsilon-\gamma\varepsilon^d
\quad\text{and}\quad
B(\varepsilon)=\frac{1-2d\gamma\varepsilon^{d-1}}{2d\varepsilon^d}
\]
on \(0<\varepsilon<(2d\gamma)^{-1/(d-1)}\). Their derivative signs are proved symbolically for every integer \(d\ge2\). Substitution of \(x=\gamma\varepsilon^{d-1}\) yields the stated \(\Gamma_d\) and \(\Delta_d\), and the derivative of \(\log\Gamma_d\) has numerator
\[
2d(d+1)x^2-6dx+d+1,
\]
which stays positive on the full parameter interval.

`verify.py` was replayed from the packaged path. It numerically reconstructs the crossing for degrees \(2\) through \(40\), verifies strict interior witnesses, checks the derivative numerator, reproduces the source's binary-tree quartic, and checks the large-\(\gamma\) coefficient in representative degrees. These computations are corroborative only. The proof does not rely on exhaustive enumeration or on the numerical tests.

The verified statement is limited to the source's sufficient region \(G_d\). No necessity statement for a physical phase boundary is claimed.
