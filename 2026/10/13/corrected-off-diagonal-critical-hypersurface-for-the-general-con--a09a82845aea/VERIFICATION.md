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
The check starts from the two exact Jacobi parameters in equations (4.6a)–(4.6b) of arXiv:2207.03713v1.

For \(\beta>0\), write \(g=|\gamma|^2\) and
\[
\Delta^2=(\alpha\beta+g-4)^2+16g.
\]
At a transition \(\mu_j=1\), one must have
\[
\Delta=\left|4+\alpha\beta+g-2\sqrt2\beta\right|.
\]
Squaring and simplifying gives
\[
-4\beta\bigl(\sqrt2\alpha\beta-4\alpha-2\beta+\sqrt2g+4\sqrt2\bigr)=0.
\]
Thus, away from \(\beta=2\sqrt2\), the only finite candidate is
\[
\alpha_c=\frac{2\beta-\sqrt2(g+4)}{\sqrt2\beta-4}.
\]
The unsquared sign at this point is
\[
4+\alpha_c\beta+g-2\sqrt2\beta
=-\frac{2((\beta-2\sqrt2)^2+2g)}{\sqrt2\beta-4},
\]
which is positive below \(2\sqrt2\) and negative above it. Hence no extraneous solution was introduced by squaring, and the selected channel is \(\mu_1\) below the threshold and \(\mu_2\) above it.

Differentiating the selected reciprocal parameter gives
\[
\left.\frac{d}{d\alpha}\mu_j^{-1}\right|_{\alpha_c}
=\frac{1}{\sqrt2}\frac{(\beta-2\sqrt2)^2}{(\beta-2\sqrt2)^2+2g}>0.
\]
This proves that the left limit has \(\mu_j\to1^+\).

The expression printed in Theorem 7.3 reduces against \(\alpha_c\) to
\[
\widehat\alpha-\alpha_c=\frac{7g}{2\beta(\sqrt2\beta-4)},
\]
so the two centers agree exactly when \(g=0\) (for \(\beta\ne2\sqrt2\)). At \(\beta=2\sqrt2\), the squared crossing condition reduces to \(g=0\), proving the separate endpoint statement.

The included `verify.py` evaluates these identities at high precision on representative parameter values and checks the left-hand direction. It is a corroborative replay, not the basis of the all-parameter proof.

Unproved limits: the package does not independently re-derive the Jacobi spectral theorem or the eigenvalue-count asymptotic cited by the source, and it does not establish whether the inaccessible publisher full text silently corrected the displayed formula.
