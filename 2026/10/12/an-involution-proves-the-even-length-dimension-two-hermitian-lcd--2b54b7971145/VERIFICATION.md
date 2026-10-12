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
and the five projective points of
\[
\operatorname{PG}(1,4).
\]

The verifier enumerates every matrix in
\[
\operatorname{GL}(2,4)
\]
and obtains exactly \(60\) induced permutations of the five projective points.

For all \(32\) parity patterns it constructs the Hermitian Gram matrix directly and verifies that it is nonsingular exactly for parity weights \(2\) and \(3\), matching
\[
\binom t2\pmod2.
\]

For every even
\[
4\le n\le20,
\]
all five-part multiplicity vectors are enumerated. They are reduced to projective-linear orbits, and the parity-flip map is checked to be well defined, invertible on orbits, and to map exactly onto the odd-length Hermitian LCD classes with minimum distance at least \(2\).

The replay additionally checks
\[
d=N-\max_i m_i
\]
for the projective multiplicity model and confirms the equality of the source's two class counts at every tested length.

Successful replay prints `VERIFY_OK`.
