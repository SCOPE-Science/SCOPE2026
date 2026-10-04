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
For
\[
A=C_{p^a}\oplus C_{p^b},
\]
the checker enumerates every matrix
\[
\begin{pmatrix}
\alpha&\beta\\
p^{b-a}\gamma&\delta
\end{pmatrix}
\]
with unit diagonal entries.

For each matrix it forms the six \(2\times2\) minors of the cokernel presentation of \(\varphi-I\). Their gcd is the fixed-subgroup order. The checker compares the exact number of matrices with gcd \(p^2\) against each displayed formula branch.

The tested branches include
\[
a=1,\ b\ge4;
\quad
a=2,\ b=4;
\quad
a=2,\ b\ge5;
\quad
a\ge3,\ b=a+2;
\quad
a\ge3,\ b\ge a+3.
\]

For the smallest examples it also applies every automorphism to every group element and checks that the direct number of fixed points equals the presentation-minor value.

Finally, it evaluates the excluded pair
\[
(a,b)=(1,3)
\]
and recovers the published boundary formula.

The packaged checker returns `VERIFY_OK`.

Finite enumeration is not used to prove the universal formulas.
