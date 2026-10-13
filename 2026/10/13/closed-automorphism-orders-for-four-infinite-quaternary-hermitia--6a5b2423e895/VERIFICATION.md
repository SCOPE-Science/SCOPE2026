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
`artifacts/verify.py` uses only the Python standard library.

It realizes
\[
\mathbb F_4=\mathbb F_2[\omega]/(\omega^2+\omega+1)
\]
and the five normalized points of
\[
\operatorname{PG}(1,4).
\]

The verifier first checks that the sum of the five Hermitian rank-one Gram contributions is the zero \(2\times2\) matrix. Thus adding one full projective line preserves the Hermitian Gram matrix.

For the four source seed vectors and sample values
\[
s=6,7,10,
\]
it constructs the dimension-two generators, verifies Hermitian LCD nonsingularity, enumerates all \(16\) codewords, and compares the exact weight enumerators with the four closed formulas.

It then enumerates all \(180\) matrices in
\[
\operatorname{GL}(2,4),
\]
computes their induced permutations on the five projective points, and confirms that the distinct projective permutations number \(60\). For each of the four multiplicity colorings it calculates the projective stabilizer and checks the orders
\[
2,\ 1,\ 3,\ 2.
\]

Finally it evaluates
\[
3\left(\prod_i m_i!\right)|\operatorname{Stab}_{\operatorname{PGL}(2,4)}(m)|
\]
and compares the results with the four factorial automorphism formulas.

Successful replay prints `VERIFY_OK`.
