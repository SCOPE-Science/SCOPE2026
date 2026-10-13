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

The universal proof is contained in `RESULT.md`. It uses exact finite-dimensional matrix identities and does not extrapolate from finite data.

For an arbitrary split of size \(k\) versus \(n-k\), set
\[
\kappa=(e^{i\theta}-1)2^{-n/2},\quad
\nu^2=1-2^{-k},\quad
w^2=1-2^{-(n-k)}.
\]
The split-Schmidt coefficient matrix is
\[
H=\begin{pmatrix}
1+\kappa\alpha\beta&\kappa\alpha w\\
\kappa\nu\beta&\kappa\nu w
\end{pmatrix}.
\]
One has \(\det H=H_{11}=\kappa\nu w\), and hence
\[
\det\left((\rho^{T_B})_{4\times4}\right)
=-p^3|\kappa|^4\nu^4w^4.
\]

The packaged standard-library Python file `artifacts/verify.py` checks the pure-state partial-transpose cofactor, compares the determinant with the exact formula across multiple integers \(2\le n\le8\), probabilities, phases, and cuts, and checks the active block against direct full-space partial transposition for smaller systems. The rank-two product-ray argument and the PPT-mixture exclusion are analytic, not machine-inferred. The sign criterion is strict only when \(p>0\) and the phase is nontrivial.

The proof uses the standard fact that positive partial transpose is sufficient for separability in a \(2\otimes2\) local subspace. It makes no independent certification claim.
