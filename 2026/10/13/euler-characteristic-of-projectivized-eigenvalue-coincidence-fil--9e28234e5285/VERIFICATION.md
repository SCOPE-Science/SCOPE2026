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
The checker uses the cocharacter weights
\[
w_j=2^{j-1}
\]
and verifies for
\[
2\le n\le50
\]
that every ordered off-diagonal difference \(w_a-w_b\) is nonzero and distinct.

It then checks the fixed-locus count
\[
\chi(\mathbb P^{n-1})+n(n-1)=n^2.
\]

For every off-diagonal matrix unit it verifies that both the full matrix and the upper-left cutoff are nilpotent, hence have common spectral multiplicity \(n-1\). It also checks sample diagonal matrices, for which the cutoff spectrum is a submultiset of the full spectrum.

For matrix sizes through \(8\), the checker independently constructs characteristic polynomials and computes exact polynomial greatest common divisors for all off-diagonal matrix units and a finite family of diagonal points, confirming gcd degree \(n-1\).

These checks are finite regression evidence only. The all-parameter proof is the symbolic fixed-locus and Euler-localization argument in `RESULT.md`.
