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

The verifier checks the closed four-weight frequencies for several odd primes and dimensions, verifies that they sum to
\[
p^{2m+1},
\]
and confirms that
\[
p^{m-1}(p^m-p^{m-1}-2)
\]
is the smallest nonzero weight.

It independently constructs
\[
\mathbb F_9=\mathbb F_3[u]/(u^2-2)
\]
and
\[
\mathbb F_{25}=\mathbb F_5[u]/(u^2-2),
\]
rebuilds both defining sets, applies
\[
X=x+\beta/\alpha,
\]
and checks the parameter change
\[
c'=c-\operatorname{Tr}(a\beta/\alpha)
\]
coordinate by coordinate for every parameter triple. All codewords are enumerated, and the direct distributions agree exactly with the closed formula.

For \(p=3\) and \(m=2,3,4\), the formula reproduces the weight enumerators printed in the source's Table III.

Finally, the verifier computes the first three dual MacWilliams coefficients and checks
\[
A_1^\perp=A_2^\perp=0
\]
and
\[
A_3^\perp
=
\frac{
p^{m-1}(p-1)(p-2)(p^{2m-2}-1)(p^m-1)
}{6}.
\]
Successful replay prints `VERIFY_OK`.
