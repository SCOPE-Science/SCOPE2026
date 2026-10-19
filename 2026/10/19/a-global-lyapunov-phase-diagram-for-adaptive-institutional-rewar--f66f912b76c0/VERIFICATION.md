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
# Verification and limitations

**Analytic proof.** The public-goods payoff difference is \(-k+a\delta S_N(x)\). Differentiate the geometric sum to obtain strict monotonicity of \(A_\delta(x)=k/[\delta S_N(x)]\), then insert the five selected equilibrium coordinates in the exact Lyapunov formula (1) of `RESULT.md`. Expand the derivative to identity (2); the cases show each term is nonpositive, and strict monotonicity plus the second ODE isolates the unique invariant zero-derivative point. The integrals have precisely the endpoint singularities described in the proof, so LaSalle applies to compact sublevel sets. This proves the infinite-time statements analytically, including the four critical boundaries and arbitrary \(\varepsilon>0\).

**Executable check.** Run `python verify.py` with any recent Python 3 version; only the standard library is used. It checks source-versus-factorized vector-field equivalence numerically, the rearranged Lyapunov derivative identity, all five phase selectors and four critical thresholds, sign of the derivative on fixed-seed parameter sweeps over multiple group sizes and timescale ratios, and monotonicity of selected endpoints. The script should print `PASS` on completion. Tests use floating-point tolerances and finite samples; they do **not** independently prove the theorem, cover all parameters, or constitute a certified interval check.

**Scope and risk.** All claims require \(N\ge2\), \(1<r<N\), \(c,\delta,u,\varepsilon>0\), \(0<\alpha<\beta\), and strictly interior initial data. There are other stationary corner solutions when started on invariant boundary faces. The result does not cover stochastic or spatial games, changing \(\delta\), alternate feedback laws, or rates at critical nonhyperbolic equilibria. Independent scientific validation is not performed.
