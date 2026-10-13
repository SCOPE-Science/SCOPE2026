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

It works in the source's length-three model
\[
x^3-1=(x-1)(x^2+x+1)
\]
over \(\mathbb Z_4\), whose CRT factor degrees are \(1\) and \(2\).

The script reduces the source seeds
\[
g=x^2+x+3
\]
and
\[
g'=2x^2+2x
\]
modulo the lifted factors. It verifies that \(g\) has both factors active, while \(g'\) has only the degree-two factor active.

Every residue of
\[
\mathbb Z_4[x]/(x^3-1)
\]
is represented by its three coefficients, so there are exactly \(64\) residues. For each
\[
\ell\in\{1,2,3\},
\]
the verifier exhausts all \(64^\ell\) ordered multiplier tuples.

For each tuple, it independently tests the source's local unit condition after reduction modulo \(2\), then compares the brute-force count with
\[
4^{3\ell}\prod_{i\in S}(1-2^{-\ell d_i}).
\]
It performs this check for all three nonempty active sets.

The script separately enumerates the whole-polynomial joint-coprimality condition and verifies its count and the comparison ratios. Successful replay prints `VERIFY_OK`.
