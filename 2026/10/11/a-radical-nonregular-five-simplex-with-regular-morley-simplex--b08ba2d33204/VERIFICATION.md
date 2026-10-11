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
Let
\[
A=2\sqrt2-1,
\qquad
C=-\frac32+\sqrt2+\frac12\sqrt{-39+36\sqrt2}.
\]
The exact relations used by the proof are
\[
A^2+2A-7=0
\]
and
\[
A^2-AC-4A+C^2+2C+1=0.
\]
They imply
\[
A^3=11A-14,
\qquad
C^3=3C+58-32A,
\]
and hence
\[
\phi(1)+4\phi(A)+\phi(C)=0.
\]

For the first row \((1,A,A,C,A,A)\), the nonconstant eigenvalues of \(K\) are
\[
1-C,
\qquad
1-2A+C,
\qquad
1-C.
\]
With \(T=(C+2)/8\), the corresponding eigenvalues of \(H=\phi[K]\) satisfy
\[
h_k=4T\kappa_k^2.
\]
The middle equality follows from the exact factorization
\[
2h_2-(C+2)(1-2A+C)^2
=2(A-C)(A^2-AC-4A+C^2+2C+1).
\]

The packaged checker represents the number field exactly on the basis
\[
1,\sqrt2,\sqrt{-39+36\sqrt2},\sqrt2\sqrt{-39+36\sqrt2}
\]
with rational coefficients. It verifies the two quadratic relations, the Fourier identities, and the four entries of the source's equation (15) without floating-point arithmetic. Decimal evaluation is used only to display the strict inequalities
\[
1<C<A<2,
\qquad
T>0.
\]

The proof does not enumerate all solutions of the six-vertex system. No uniqueness claim is made.
