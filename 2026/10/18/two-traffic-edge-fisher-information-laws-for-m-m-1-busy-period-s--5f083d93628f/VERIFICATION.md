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

At known fixed μ, differentiating the busy-period Bessel density cancels its apparent 1/λ score singularity, giving S=−y+y√(μ/λ)I₂/I₁. Positive series give I₂/I₁≤z/4, hence |S|≤y+μy²/2; for λ≤μ/4 the series also give g≤μ exp(−μy/4). Dominated convergence to the exponential density and score μy²/2−y gives 2/μ². At the other endpoint, z|I₂/I₁−1| is bounded on the positive axis by the small- and large-z expansions and continuity. Thus S=(√(μ/λ)−1)Y plus a uniform bounded remainder for λ≥μ/2. With d=μ−λ the first two Laplace derivatives are E[Y]=1/d and E[Y²]=2μ/d³; the cross term and bounded remainder square are Oμ(1). The leading term is 2μ/[λ(√μ+√λ)²d], which is 1/(2μd)+Oμ(1), not just a relative equivalence. Substitution into the fixed-parameter constants proves both pairs of limits and the stated ratios, with the observation-horizon limit taken first. The derivation does not use the originating paper's incorrect Y|X argument: conditional on X=k, there are 2k−1 queue jumps, and their holding times are Exp(λ+μ), so the conditional law is Erlang(2k−1,λ+μ), not a λ-independent Erlang(k,μ). Only the marginal formulas are used. Frozen verify.py and verification notes were inspected, not executed. Fresh fixed-order scaled Gauss–Laguerre quadrature at μ=1 gave I_Y=1.99900141683 at ρ=10⁻⁴ and (1−ρ)I_Y=0.50054863 at ρ=0.99; these are finite checks only. Replay: /workspace/branches/f5020988-408b-447c-931e-bfe551b376c8/duration_fisher_laguerre_check.py.

## originality

PASS

Best-of-knowledge pass for the two duration-only Fisher-information evaluations and their consequence for the comparative endpoint behavior. The likelihood, fixed-parameter square-root constants, and the substitution giving both count endpoints were in or immediate from the prior work and are not credited as novel. The originating paper explicitly left these traffic asymptotics open. Its asserted KL ordering in §IV is not a valid route to the critical coefficient: Y|X depends on λ. The frozen proof instead controls the marginal score uniformly and supplies the bounded absolute remainder.

## value

PASS

The duration limits answer a stated gap about two natural busy-period observations and distinguish a divergent light-traffic ratio from near-equality at criticality. Uniform control of the duration score as its distribution develops a heavy tail gives a quantitative absolute error and hence a relative ratio rate. The count substitutions by themselves would not warrant this verdict.

The dated certificate retains the supplied scientific assessment, sources and limitations.
