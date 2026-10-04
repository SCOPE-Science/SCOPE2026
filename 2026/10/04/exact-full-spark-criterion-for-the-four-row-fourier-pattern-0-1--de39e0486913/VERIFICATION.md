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

The proof was checked along four independent exact routes supplied by `verify_pattern_0134.py`:

1. Symbolic sparse-polynomial expansion verifies the determinant factorization into the Vandermonde factor and \(e_2\).
2. Exact residue counting verifies the divisor-uniformity criterion for every \(5\le N\le5000\).
3. For every \(N\le120\) with \(\gcd(N,6)=1\), every normalized four-column choice is tested in finite fields containing primitive \(N\)-th roots. Several suitable primes are available so that a nonzero algebraic determinant is not misclassified because of a single modular reduction; \(2{,}693{,}520\) normalized quadruples are covered.
4. The explicit even-order and three-divisible singular constructions are checked through \(N=500\).

The replay ends with `VERIFY_OK`. These finite checks do not replace the infinite proof. The nonvanishing implication for arbitrary \(N\) relies on the published Lam--Leung weight theorem for vanishing sums of roots of unity; the converse uses explicit elementary witnesses.
