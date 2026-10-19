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

# Exact verification of the null-polynomial module presentation

All finite-field arithmetic is exact. Run `python3 verify.py` from the directory containing that file; no third-party modules are needed. The verifier implements the ring by seven-bit vectors and the multiplication \((A,B)(C,D)=(AC,AD+BC)\).

The supplied proof gives the seven proposed module generators. The program evaluates each on all \(128\) ring elements, reconstructs the thirty normal monomials, and checks a fully specified \(30\times30\) minor. Its rows are indexed by the ordered \((r,k)\) pairs printed in the proof; \(r\) is the seven-bit encoding of the ring input and \(k\) is an output-coordinate index. The checker verifies that the minor has rank \(30\) over \(\mathbb F_2\), equivalently determinant \(1\). Hence it is an exhaustive finite certificate for the independence needed by the proof. The algebraic leading-term reduction then handles all degrees, not merely those enumerated.

The program also tests all \(128\) possible constant right multipliers against the seven module generators, confirming that the \(64\) stabilizing constants are exactly those whose two diagonal entries in the first block coincide. It tests the degree-six null witness against an explicit nonstabilizing multiplier and input.

The module decomposition follows from an exact Smith-normal-form calculation of a two-by-two polynomial matrix; the code does not need to assume a bound on the degrees of all null polynomials. These checks do not establish any claim about other finite rings or about the full polynomial right idealizer. No independent external audit has been carried out.
