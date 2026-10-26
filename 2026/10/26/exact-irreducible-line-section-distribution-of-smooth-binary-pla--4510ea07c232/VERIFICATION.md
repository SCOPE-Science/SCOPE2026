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

# Exact computational checks

Run `python census.py` with Python 3 and SymPy 1.14.0 in the directory containing the source and certificate; it traverses every nonzero quartic bitmask, generates the full projective-coordinate group and every coefficient orbit, decides geometric smoothness by three affine Jacobian Gröbner bases over GF(2), and writes a CSV containing each of the 279 orbit representatives, its size, geometric-smoothness bit and count of irreducible rational line restrictions. It asserts the 78 smooth orbits, their total 10,920 equations and all eight distribution bins.

Run `python factor_check.py` in the same directory. Independently it expands each line restriction as a binary quartic in two homogeneous variables and recognizes the three irreducible quartic polynomials via exact bit signatures 19, 25 and 31. It checks all 279 orbit representatives against the supplied certificate and recomputes the weighted smooth-quartic histogram. Its smoothness and orbit weights originate with the primary computation and are **not** independently certified by this second check.

The supplied `census_output.txt` and `factor_check_output.txt` are the actual stdout of successful local executions. The 279-row `orbit_certificate.csv` is an explicit output; no external certificates, randomized searches or unbounded computation are needed. The proof's inference is only for degree four over GF(2). The scientific self-review is reported separately; no independent audit has been performed.
