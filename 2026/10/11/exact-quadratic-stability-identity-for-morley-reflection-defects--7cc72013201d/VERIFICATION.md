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

The exact linear-algebra core is the Gram matrix of the \(n-1\) vectors
\[
w_k=M_k-\frac{M_i+M_j}{2},
\qquad
k\notin\{i,j\},
\]
inside the perpendicular bisector of one edge of a regular \(n\)-simplex:
\[
w_k\cdot w_k=\frac{3L^2}{4},
\qquad
w_k\cdot w_\ell=\frac{L^2}{4}\quad(k\ne\ell).
\]
Thus
\[
G=\frac{L^2}{4}(2I+J)
\]
and
\[
G^{-1}
=
\frac2{L^2}
\left(I-\frac1{n+1}J\right).
\]

If
\[
r_k=(n_i-n_j)\cdot w_k,
\]
then
\[
|P_{v^\perp}(n_i-n_j)|^2=r^TG^{-1}r.
\]
The source's reflection-defect formula gives independently
\[
|P_{v^\perp}(n_i-n_j)|^2
=
(q-1)^2\varepsilon_{ij}.
\]
Equating these expressions is exactly the claimed quadratic identity.

The bundled checker uses exact rational arithmetic to verify the Gram inverse for every \(3\le n\le80\), verifies the quadratic-coordinate identity on deterministic rational vectors, and checks the eigenvalue inequalities for the quadratic form.

These finite checks are supplementary. The theorem follows for every \(n\ge3\) from the displayed inverse formula and the source's exact projection identities.

The verification does not address near-regular Morley simplices, because no such extension is claimed.
