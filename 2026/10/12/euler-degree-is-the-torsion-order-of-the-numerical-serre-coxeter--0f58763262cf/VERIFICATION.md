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

The replay script constructs the five published representative Euler matrices
\[
A=
egin{pmatrix}
1&a&e&d\
0&1&b&f\
0&0&1&c\
0&0&0&1
\end{pmatrix}
\]
from their parameter tuples and uses exact integer arithmetic only.

For each matrix it reconstructs \(B=A+A^{\mathsf T}\), computes the integral inverse of the unitriangular matrix \(A\), constructs \(T=-A^{-\mathsf T}A\), and checks
\[
T-I=-A^{-\mathsf T}B.
\]
It then enumerates every minor of sizes \(1,2,3,4\). From the determinant divisors it derives the Smith invariant factors of both \(B\) and \(T-I\), checks that they agree, and verifies that the product of the nonzero factors is the published Euler degree.

The expected Smith forms are
\[
\operatorname{diag}(1,1,22,0),\quad
\operatorname{diag}(1,1,40,0),\quad
\operatorname{diag}(1,3,18,0),\quad
\operatorname{diag}(2,2,16,0),\quad
\operatorname{diag}(1,1,72,0).
\]

The finite replay verifies the five classified representatives. The uniform identity
\[
\left|\operatorname{tors}\operatorname{coker}(T-I)ight|=D(A)
\]
for every positive matrix in the classified setting is justified in `RESULT.md` from the source adjugate identity and primitivity of its kernel generator, not by extrapolation from the five computations.

The stored output in `verification_output.txt` ends in `VERIFY_OK`.
