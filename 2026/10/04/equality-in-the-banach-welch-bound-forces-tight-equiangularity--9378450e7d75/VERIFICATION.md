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
The theorem is proved analytically, with no finite experiment used as a substitute for a universal argument.

The proof was checked against the actual rank-one operator identities
\[
S=\sum_j \tau_j\otimes f_j,
\qquad
\operatorname{tr}S=\sum_j f_j(\tau_j)=n,
\]
and
\[
\operatorname{tr}(S^2)=\sum_{j,k}f_j(\tau_k)f_k(\tau_j).
\]
The endpoint arithmetic was also checked:
\[
n(n-1)\frac{n-d}{d(n-1)}=\frac{n^2}{d}-n.
\]
Therefore equality in the maximum-correlation bound makes the lower and upper ends of the proof chain coincide. Equality in the eigenvalue Cauchy--Schwarz step forces all eigenvalues to equal \(n/d\), and equality in the termwise bound forces every ordered off-diagonal product to have modulus \(M^2\). This yields both tightness and constant off-diagonal modulus.

The boundary \(n=d\) is included separately: \(\gamma=0\), so equality means every off-diagonal pairing vanishes, while the same trace equality gives \(S=I_X\).

No claim is made beyond the source hypotheses of diagonalizability and nonnegative spectrum, and no continuous or higher-order equality statement is asserted.
