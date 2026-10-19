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

# Reproducibility and limitations

The analytic argument in `RESULT.md` proves the all-weight, all-frequency, all-radius asymptotic statement. The finite supplemental checker is `checker.py` and requires Python's standard library only. Execute it with `python checker.py` from the package directory.

Its computations use exact rational arithmetic for signed-period conditions, lattice point membership, coset disjointness, and vanishing-factor scale counts. Floating-point evaluations are limited to sine-rule weights, approximate mask cancellation, and comparisons with a rigorous lattice-counting asymptotic. Tested resonances are \(\omega=(1/3,2/3)\) with period one, \((1/5,3/5)\) with period two, and \((1/7,4/7)\) with period three. At radius \(140\), each ten-scale union equals the first-period union exactly; the point counts are \(30{,}790\), \(38{,}502\), and \(40{,}424\) respectively. Tested order lower bounds at scale \(24\) are \(24\), \(12\), and \(8\). The three triangle-boundary phase roots and one irrational root are also tested.

Finite point enumeration does not certify the infinitely many scales, the full density formula, or originality. These rely on the explicit disjointness and convergence proofs. Independent mathematical audit has not been performed.
