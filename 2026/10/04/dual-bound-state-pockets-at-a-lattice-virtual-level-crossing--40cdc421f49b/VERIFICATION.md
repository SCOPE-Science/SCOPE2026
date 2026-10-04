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

The proof was checked from the operator and Fredholm-determinant definitions in the primary source. The critical source facts used are: at \(\gamma=6\) and \(\mu=\mu_0\), \(\Delta_6(k;0)\) has its unique minimum \(0\) at \(k=0\), \(\Delta_6(k;18)\) has its unique maximum \(0\) at \(k=\boldsymbol\pi\), and the lower threshold expansion is
\[
\Delta_6(k;z)=C\sqrt{\frac65|k|^2-2z}+O(|k|^2)+O(|z|),
\qquad C=\frac{32\pi^2\mu_0^2}{5\sqrt5}.
\]

The following identities were independently reconstructed from the stated dispersion:
\[
\varepsilon(k+\boldsymbol\pi)=6-\varepsilon(k),
\]
\[
w_1(k+\boldsymbol\pi,p+\boldsymbol\pi)=18-w_1(k,p),
\]
\[
\Delta_{6+\eta}(k+\boldsymbol\pi;18-z)=-\Delta_{6-\eta}(k;z).
\]
The last identity gives the exact lower/upper pocket and eigenvalue reflection.

For the lower pocket, strict decrease of \(\Delta_{6-\eta}(k;z)\) in \(z<0\), together with its limit \(+\infty\) as \(z\to-\infty\), shows that a negative eigenvalue exists exactly when \(\Delta_6(k;0)<\eta\). The source expansion at \(z=0\) becomes
\[
\Delta_6(k;0)=\frac{|k|}{R}+O(|k|^2),
\qquad
R=\frac{25}{32\pi^2\mu_0^2\sqrt6}.
\]
This yields the two-sided ball sandwich for every prescribed relative radius error and therefore the Hausdorff and volume limits.

For \(k=\eta q\) and \(z=-\eta^2E\), division of the determinant equation by \(\eta\) gives
\[
1=C\sqrt{\frac65|q|^2+2E}+O(\eta).
\]
On compact subsets of \(|q|<R\), monotonicity brackets the unique zero in a fixed positive \(E\)-interval, so the error is uniform and the stated parabolic profile follows.

No finite numerical experiment is used as evidence for the infinite-domain theorem. No statement is made about the boundary-layer scaling at \(|q|=R\), embedded spectrum, or other perturbation directions.
