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

The verifier reconstructs the Stanley--Reisner complex on vertices
\[
\{a,b,c\}\sqcup\{d,e,f\}
\]
with forbidden pairs inside each three-element part. Its maximal faces are exactly the nine cross-pairs, so the projective tangent cone is the coordinate realization of \(K_{3,3}\).

It then applies Hochster's formula to all \(64\) induced subcomplexes. The resulting nonzero Betti numbers are
\[
\beta_{0,0}=1,\quad
\beta_{1,2}=6,\quad
\beta_{2,3}=4,\quad
\beta_{2,4}=9,\quad
\beta_{3,5}=12,\quad
\beta_{4,6}=4.
\]
These agree with the tensor product of the two Hilbert--Burch resolutions.

The alternating Betti numerator is checked to be
\[
1-6t^2+4t^3+9t^4-12t^5+4t^6
=(1+4t+4t^2)(1-t)^4.
\]
After division by \((1-t)^6\), this gives
\[
H_R(t)=\frac{1+4t+4t^2}{(1-t)^2}.
\]
The script separately enumerates standard monomials through degree \(12\) and checks their counts against the coefficient formula. It checks multiplicity \(9\), the Hilbert polynomial \(9n-3\), and therefore arithmetic genus \(4\).

The verifier is finite and combinatorial. It does not replace Wan's analytic Kuranishi theorem or the standard commutative-algebra theorems used to infer Cohen--Macaulayness and type from the minimal resolution.

The saved replay output ends in `VERIFY_OK`.
