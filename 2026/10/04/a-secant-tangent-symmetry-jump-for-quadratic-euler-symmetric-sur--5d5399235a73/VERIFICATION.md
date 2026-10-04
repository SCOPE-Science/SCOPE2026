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

The exact checker uses coordinates
\[
[t:x:y:a:b]
\]
with Euler weights
\[
(0,1,1,2,2).
\]

For the binary-quadratic discriminant
\[
B^2-4AC,
\]
restriction to the secant normal form
\[
\langle X^2,Y^2\rangle
\]
gives
\[
-4uv,
\]
while restriction to the tangent normal form
\[
\langle X^2,XY\rangle
\]
gives
\[
v^2.
\]

The checker substitutes the two rank-\(2\) parametrizations into their claimed ideals. It also verifies that the three tangent equations are exactly the \(2\times2\) minors of
\[
\begin{pmatrix}
t&x&y\\
x&a&b
\end{pmatrix}.
\]

Exact Gröbner-basis standard-monomial counts give Hilbert-function second differences \(4\) and \(3\), agreeing with the quartic and cubic degree proofs.

For infinitesimal cone automorphisms, a generic \(5\times5\) matrix is required to carry every quadratic ideal generator back into the quadratic ideal. Solving that rational linear system gives dimensions
\[
5
\]
and
\[
7.
\]
Intersecting the exact nullspace with the Euler-weight blocks gives
\[
3,\ 2
\]
in secant weights \(0,1\), and
\[
1,\ 4,\ 2
\]
in tangent weights \(-1,0,1\).

The saved replay output ends in `VERIFY_OK`.
