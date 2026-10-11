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

For an \(m\)-fold great circle,
\[
L_m=2\pi m,
\qquad
A_m\equiv2\pi m\pmod{4\pi}.
\]
Choosing \(A_m=0\) for even \(m\) and \(A_m=2\pi\) for odd \(m\) gives
\[
z_m=
\begin{cases}
im/2,&m\text{ even},\\
(1+im)/2,&m\text{ odd}.
\end{cases}
\]

The lattice determinant is
\[
\det
\begin{pmatrix}
2\pi&A_m/2\\
0&\pi m
\end{pmatrix}
=
2\pi^2m.
\]
The Hopf--elastic identity gives the same value for the Willmore energy, and the profile-cover density formula gives the same multiplicity factor for the varifold mass.

The unique exceptional modular collision is checked exactly:
\[
-\frac1{(1+i)/2}=-1+i,
\]
and translation by \(1\) gives \(i=z_2\).

For every even \(m\ge2\),
\[
z_m=im/2
\]
lies in the standard closed fundamental domain. For every odd \(m\ge3\),
\[
z_m=\frac12+\frac{im}{2}
\]
lies on its vertical boundary and strictly outside the unit circle. Standard fundamental-domain uniqueness then implies that two such representatives have the same modular class only when their imaginary parts, and hence their multiplicities, agree.

The bundled checker replays the exact lattice, energy, and exceptional-transform identities. It does not replace the global modular fundamental-domain argument by finite enumeration.
