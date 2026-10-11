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

# Verification of exact shell-visibility formulas

The accompanying standard-library Python file `verify_shell_visibility.py` is executable with `python verify_shell_visibility.py` in the same directory. It recomputes exact radial moments for dimensions three and five using finite binomial antiderivatives rather than taking the displayed polynomial formulas as inputs to the moment routine.

For each dimension \(d\in\{3,5\}\), after clearing the denominators, the difference between the independently recomputed moment formula and the proposed closed expression has a numerator polynomial of degree at most \(4d\). Checking equality at \(4d+1\) distinct *exact rational* values with `fractions.Fraction` is therefore a valid full polynomial-identity proof for those two formulas. The run prints `EXACT_IDENTITIES_OK d=3,5 common-denominator degree certificate`.

The script separately constructs independent uniform shell points in Euclidean three and five dimensions, computes the minimum squared norm along each joining segment, and compares sample visibility fractions to the formulas. A fixed pseudorandom seed makes these diagnostics reproducible; they are not relied upon for general mathematical correctness. A complete run ends with `VERIFY_OK`.

Analytical checks not delegated to the script include the tangent-angle equivalence, normalized spherical cap distribution, strict radial coupling, the general odd-dimensional square-root cancellation, and uniform thin-shell asymptotics. The limitations and earlier two-dimensional formula are acknowledged in `RESULT.md`. These materials document analytical and same-model checking only; an independent audit has not been performed.
