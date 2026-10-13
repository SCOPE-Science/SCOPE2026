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

It reconstructs \(\mathbb F_{q^2}\) for the prime fields
\[
q=3,5,7,11
\]
using an irreducible quadratic polynomial, finds a primitive element, and builds the Theorem 6 generator columns from
\[
\operatorname{Tr}_{q^2/q}
\left(a\gamma^{(q-1)e_1i}+b\gamma^{e_2i}\right).
\]

For every tested exponent representative, every nonzero projective message vector is enumerated. A codeword is declared minimal exactly when its zero generator columns have rank \(3\), the projective spanning criterion used in the proof.

The verifier checks the full published five-weight distribution and the following minimal-weight sets:
\[
q=3:\ \{4,5\},
\]
\[
q=5:\ \{16,19,21\},
\]
\[
q=7:\ \{36,41,43\},
\]
\[
q=11:\ \{100,109,111\}.
\]

For \(q=7\) and \(q=11\), representatives from distinct exponent-ratio classes modulo \(q+1\) are tested, not only the canonical class.

The finite replay checks the nonstandard geometric interpretation and representative exponent variation. The all-prime-power theorem is established by the symbolic projective argument in `RESULT.md`.

Successful replay prints `VERIFY_OK`.
