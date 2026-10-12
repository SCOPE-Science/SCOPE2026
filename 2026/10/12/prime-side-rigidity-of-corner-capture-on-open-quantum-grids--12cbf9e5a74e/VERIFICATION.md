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

# Verification and limits

The analytical proof in `RESULT.md` verifies the following separately: (1) path eigenvalues and nonzero endpoint components; (2) equivalence between the corner cyclic rank and the number of distinct grid eigenenergies; (3) linear independence over the rationals of the real cyclotomic cosine representatives; (4) the complete enumeration for equal odd primes; (5) field disjointness and field-trace restrictions for different primes; and (6) exponential decay on the bright space with unitary survival on the dark space.

`verify.py` builds the two path matrices independently, compares the predicted count of distinct eigenenergy sums against direct numeric spectra for all \(25\) ordered pairs of primes in \(\{3,5,7,11,13\}\), and checks selected corner overlaps and dissipative spectra. It also checks survival against finite-time matrix exponentials for three small grids. The actual run of this packaged file reports:

`VERIFY_OK prime_pairs=25 independent_operator_tests=7 long_time_survival=3`

These are finite, floating-point consistency tests. Numerical coincidences cannot establish algebraic equality in arbitrary dimension; the field argument supplies the infinite proof. The semigroup limit is an exact asymptotic result and does not assert uniformity of decay rates across sizes or loss strengths. Publication priority and experimental realization have not been independently established.
