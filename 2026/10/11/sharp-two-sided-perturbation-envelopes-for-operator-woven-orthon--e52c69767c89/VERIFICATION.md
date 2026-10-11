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

Fix an integer \(m\ge2\), set \(r=m-1\), and take \(H=\mathbb C^m\) with basis \((e_j)_{j=1}^m\). Put
\[
h=\frac1{\sqrt r}\sum_{j=1}^r e_j,\qquad P_h=|h\rangle\langle h|.
\]
For \(\epsilon\in\{+1,-1\}\), \(a\ge0\), define
\[
U_1=I,\qquad U_{j+1}=I+\epsilon a|h\rangle\langle e_j|\quad(1\le j\le r).
\]
Each difference is rank one and has norm \(a\). The partition
\[
\sigma_1=\{m\},\qquad \sigma_{j+1}=\{j\}
\]
is nonempty in every class and has synthesis operator
\[
T_\sigma=I+\epsilon a\sqrt r\,P_h.
\]
This follows by checking columns: \(T_\sigma e_j=e_j+\epsilon a h\) for \(j\le r\) and \(T_\sigma e_m=e_m\). Thus
\[
T_\sigma h=(1+\epsilon a\sqrt r)h,
\qquad T_\sigma v=v\quad(v\perp h).
\]
The exact frame-operator spectrum consists of \(|1+\epsilon a\sqrt r|^2\) and \(1\). For each individual source operator the rank-one update formula gives determinant \(1+\epsilon a/\sqrt r\). With \(a=t\) and the plus sign, this is positive for any \(t\ge0\), and the upper envelope is attained. With the minus sign and \(0\le t<1/\sqrt r\), all source operators remain invertible and the lower envelope is attained. If \(r\ge2\), choose \(a=1/\sqrt r\), giving invertible sources of determinant \(1-1/r\) but singular synthesis. If \(r=1\), let \(a\uparrow1\) while \(a<1\).

For general separable \(H\), let \(C_0\) be the orthonormal-basis coefficient map. The coefficient differences on disjoint partition blocks obey
\[
\|(C_\sigma-C_0)f\|^2
\le\sum_{i=2}^m\|(U_i-I)^*f\|^2
\le rt^2\|f\|^2,
\]
which supplies both universal inequalities and establishes that the constructed equalities are globally sharp.

Exact symbolic checks for \(r=1,2,3,4\) at half-critical perturbation produced squared singular values \(1/4\) and \(1\); at the critical value the synthesis rank was \(r\) in dimension \(r+1\), while individual source determinants equaled \(1-1/r\) for \(r\ge2\). These finite checks are supplementary and do not substitute for the all-\(m\) proof.

No numerical approximation, exhaustive infinite search, or external proof certification is used. The exact primary source and closely related operator-perturbation proofs were independently inspected.
