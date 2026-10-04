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

The recent source gives the exact algebraic reduction
\[
N_n=
N/
\left\langle\!\left\langle
\phi^n(g)g^{-1}:g\in N
\right\rangle\!\right\rangle,
\qquad
\pi_1(M_n)\cong N_n\rtimes C_n.
\]
For the odd-\(k\) family,
\[
N=H_k=\operatorname{UT}_3(\mathbb Z_k).
\]

The classical source was inspected for the precise meridional action:
\[
\phi(A)=B,
\qquad
\phi(B)=A^{-1}B.
\]
The class-two relation \(C=[A,B]\) then gives \(\phi(C)=C\), and direct iteration gives \(\phi^6=1\).

The six coinvariant cases were derived symbolically. Their kernel orders are
\[
k^3,\quad 1,\quad \gcd(k,3),\quad 1,\quad \gcd(k,3),\quad 1
\]
for residues \(0,1,2,3,4,5\pmod6\), respectively. In the two \(C_3\) cases, \(\phi\) descends to inversion.

The bundled exact finite checker independently constructs the Heisenberg groups, normal closures of the coinvariant relations, and descended action. It reports:

`VERIFY_OK k=3,5,7,9,11,15 residues=0..5 quotient_sizes=[k^3,1,gcd(k,3),1,gcd(k,3),1] inversion_action=true`

The finite check does not establish the infinite theorem; it only verifies representative instances of the symbolic proof.

No independent audit has been performed.
