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

# Verification of the mixture Zak-zero theorem

The analytic proof establishes the exact zero location and two strictly negative Jacobian diagonal entries for every admissible positive scale measure, not just discrete measures. Its nonstandard step is a heat-equation boundary-sign argument: the one-dimensional heat equation on a unit interval has strictly positive imaginary part because one boundary value is positive and the other is zero. At half-frequency the analogous half-interval Dirichlet problem has a positive source, and the Hopf boundary lemma makes the zero simple. The mixed conclusion uses pointwise positive integration, not an unjustified assertion that zero sets behave continuously under addition.

To reproduce the finite supplementary tests, run `python verify.py` using Python 3 with no external modules. The checker performs 4,296 comparisons across several discrete scale measures and confirms strict sector signs, the half-frequency sign transition, boundary positivity, the central zero, nonvanishing Jacobian, derivative identity, and a two-scale non-log-concavity witness. The finite suite does not exhaust all measures or prove the theorem.

The complete text of the 2017 averaged-totally-positive article was not inspected; its abstract alone cannot establish noncoverage. The full open 2003 Janssen paper was read at the class-defining passage, and the 2026 Gaussian and 2014 totally-positive sources were examined at their main theorems. The evidence supports a self-review only; no independent audit was performed.
