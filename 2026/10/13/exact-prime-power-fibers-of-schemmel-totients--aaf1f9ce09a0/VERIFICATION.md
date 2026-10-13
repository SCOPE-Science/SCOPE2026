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

The proof in `RESULT.md` is exact and unrestricted in \(r\), \(\ell\), and \(t\).

The attached checker independently evaluates the Schemmel totient from prime factorizations for every
\[
1\le n\le50000.
\]
For each
\[
1\le r\le8,
\]
each prime
\[
\ell\le19,
\]
and each
\[
1\le t\le3,
\]
it constructs the predicted preimages from the subset-sum theorem and asserts equality with all directly observed preimages lying in the finite window.

It also verifies
\[
\varphi^{-1}(2)=\{3,4,6\},
\quad
\varphi^{-1}(4)=\{5,8,10,12\},
\]
and
\[
S_2^{-1}(3)=\{5,9,15\},
\quad
S_2^{-1}(9)=\{11,27,33,45\}.
\]

No floating-point arithmetic or probabilistic primality test is used. The finite stress test does not prove the theorem; completeness follows from the factor-by-factor argument in `RESULT.md`.
