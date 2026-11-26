---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The known projection formula reduces the question to the cubic sign-sum polynomial (S^3-(3N-2)S)/6. Marking negative signs gives the signed generating polynomial binom(N,3)(1-z)^3(1+z)^(N-3); one cumulative sum removes one factor (1-z). Splitting the positive-S half at the strict outer-root threshold and then doubling establishes the finite identity, including on-lattice roots and zero. The normalized first local Stirling correction is -H4/(12N); the central remainder is integrably summable and the tails follow from binomial concentration. Expanding the absolute value in 2t/N leaves a discrepancy only within O(1/N) of the outer roots, contributing O(N^(-3/2)) to the normalized lattice sum; replacing the first-order perturbation by its integral costs the same order by bounded variation. The continuum coefficient is (8 phi_a-4 phi_0) - (144 phi_a-18 phi_0)/12. The derivative jumps are 6 phi_0 at zero and 12 phi_a at each outer root. Integrating against the periodic B2 gives the coefficient -h^2/2 times the jumps, with smooth remainder O(h^3) from the bounded periodic primitive. This gives a uniform O(1) after restoring N^(3/2)/6. The extrema follow from the exact Bernoulli range and are approached on N=12m^2+1 (odd, phase tending to 1/2) and N=12m^2 (even, integral phase), respectively.

## originality

PASS

Credit the projection-kernel reduction and the leading Gaussian–Hermite limit to Defant et al. The supported increment is the quantitatively uniform cubic lattice-phase expansion and its exact oscillatory limits and finite boundary identity. There is a distinct catalogue record with exactly the same phase coefficient, extrema and boundary identity, plus parity bands; it is listed later and only states an o(sqrt(N)) remainder. This is demonstrable equivalent coverage of the second-order law, not evidence that it preceded the assigned record, and not an independent priority determination. No inspected earlier source establishes the cubic correction.

## value

PASS

The leading projection-constant scale masks a real, order-sqrt(N) obstruction to a constant second coefficient. Resolving the independent parity and outer-root phases with a bounded error gives sharp dimension-sensitive information about a natural norm invariant; this is not just a more accurate evaluation of its Gaussian limit. The finite identity also treats root-on-lattice dimensions without asymptotic assumptions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
