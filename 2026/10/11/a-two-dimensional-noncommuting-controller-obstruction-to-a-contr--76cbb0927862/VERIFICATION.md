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

The source theorem was checked in both its earliest preprint and published forms. The published statement assumes that \(K\) commutes with \(T\) and \(U\) and that \(S_\Lambda T=T S_\Lambda\); it does not assume \(S_\Lambda U=U S_\Lambda\) or \(TU=UT\).

For the counterexample,
\[
S_\Lambda=\begin{pmatrix}4&0\\0&1\end{pmatrix},
\qquad
U=\begin{pmatrix}1&9/10\\9/10&1\end{pmatrix},
\qquad
T=K=I.
\]
The eigenvalues of \(U\) are \(1/10\) and \(19/10\). Hence \(U\) is positive invertible. For every \(f=(x,y)\),
\[
\|f\|^2\le4x^2+y^2\le4\|f\|^2.
\]
At \(f=(1,-2)\),
\[
Uf=(-4/5,-11/10),
\]
and direct multiplication gives
\[
\langle\Lambda_1Uf,\Lambda_1Tf\rangle=-1.
\]
Thus the ordinary frame exists while the controlled lower inequality fails.

For the repair, define
\[
c_-=\|T^{-1}\|^{-1}\|U^{-1}\|^{-1},
\qquad
c_+=\|T\|\,\|U\|.
\]
If \(T,U,S_\Lambda\) commute pairwise, then
\[
c_-I\le TU\le c_+I
\]
and therefore
\[
c_-S_\Lambda\le TU S_\Lambda\le c_+S_\Lambda.
\]
Combining this with either the ordinary or controlled frame-operator inequalities gives the two-way bound transfer recorded in the result.

The proof uses exact finite-dimensional algebra only. No numerical approximation, sampling, or incomplete enumeration is used.
