---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

In RESULT.md lines 43–78, the cube is invariant and the nonnegative cross-derivatives give comparison with the two homogeneous scalar extremal solutions, also for reducible W and mixed-side starts. The scalar field g(y)=tanh(2y)/2−y is restoring on either side. Its cubic and quintic terms give (y⁻²)'=8/3−64/(15 y⁻²)+O(y⁴); first y⁻²=(8/3)t+O(log t), then the derivative after subtraction of the linear and log terms has an integrable O(log t/t²) residual. Only strictly one-sided starts bound all inverse squares by the two scalar envelopes. For irreducible W the stationary left-vector projection removes the simple Perron eigenvalue; every remaining eigenvalue has real part <1 even when W is periodic, so W−I on that subspace is exponentially stable under the vanishing transverse perturbation. The weighted mean has quadratic transverse error, hence its inverse-square derivative has at most O(t^{3/2} exp(−2ηt)) additional error; all node inverse squares differ from the mean's by o(1). W=I really can retain distinct constants: same-sign distinct scalar starts are nonzero time translates, shifting the constant by 8/3 times the time shift. In the nonstationary homogeneous variational equation all matrices commute. As an independent check, a(t)−1=g'(y(t)) and its integral is log|g(y(t))/g(y(0))|, giving exactly the −(3/2)log t term and a finite constant. This is a matrix factorization, not nonlinear mode decay, and works for Jordan blocks. Ran python3 /workspace/audit_checks.py, check 3, reproducing all decisive rational coefficients using the differential recurrence h'=1−4h² with h=tanh(2y)/2; the proof, not finite tests, establishes the quantifiers. The frozen verifier was inspected, not executed. Its narrative miscounts the sample matrices: verify.py lines 19–24 contain two irreducible and two reducible examples; this does not affect the proof.

## originality

PASS

The model, cusp, scalar embedding and equilibrium spectra are background, and the simple attraction and scalar leading law alone are not the basis of the pass. The distinct content supported at the frozen publication is the precise one-sided logarithmic law across arbitrary row-stochastic W, irreducible common-constant matching, and the quantified time-dependent mode factors. The Nov. 1 indexed result demonstrably covers the matching irreducible asymptotic (indeed a wider basin), not just a similar exponent. It is dated later and does not establish antecedent coverage or settle provenance; it also does not supply the nonstationary variational factor in the inspected statements. The strongest same-day match gives a diameter envelope rather than these claims; no within-day order is inferred.

## value

PASS

At the natural equality boundary of a published contraction criterion, the new quantitative content is the logarithmic renormalization of critical delay and the distinction between topology-independent bulk coefficients and an irreducibility-dependent common phase. The mode response also resolves how the algebraic corrections depend on a graph eigenvalue when equilibrium-only rates are insufficient. These are useful exact benchmarks in the deterministic model, not claims about finite-amplitude modes or animal data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
