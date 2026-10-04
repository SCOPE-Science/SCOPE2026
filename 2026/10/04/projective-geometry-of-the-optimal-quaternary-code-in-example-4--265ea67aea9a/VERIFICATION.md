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

The verifier builds \(\mathbb F_{16}\) from \(X^4+X+1\), takes a primitive element \(\alpha\), and identifies
\[
\mathbb F_4=\{0,1,\omega,\omega^2\},\qquad \omega=\alpha^5.
\]
It reconstructs the \(4\)-cyclotomic defining set from Example 4.16, obtains complement exponents \(\{10,11,14\}\), derives
\[
h(x)=x^3+x+\omega,
\]
and divides \(x^{15}-1\) exactly to obtain the cyclic generator polynomial.

It checks that the generator vanishes exactly on the twelve defining exponents, forms the \(3\times15\) generator with rows \(g,xg,x^2g\), confirms rank \(3\) and Euclidean self-orthogonality, and enumerates all \(64\) codewords.

The verifier separately enumerates all \(21\) projective points and lines of \(\operatorname{PG}(2,4)\). It confirms that the generator columns are \(15\) distinct projective points and that the six missing points are exactly a line together with one point outside that line. This yields the line-intersection multiplicities \(0,3,4\) with counts \(1,5,15\), respectively.

Finally it enumerates all \(21\) two-dimensional subspaces of the \(3\)-dimensional message space and obtains support sizes \(14\) or \(15\), with minimum \(14\). Successful replay prints `VERIFY_OK`.
