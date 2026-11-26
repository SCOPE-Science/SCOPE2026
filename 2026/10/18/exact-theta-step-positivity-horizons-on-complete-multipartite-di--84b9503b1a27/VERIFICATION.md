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

The orthogonal splitting into constants, classwise zero-sum vectors, and class-constant global zero-sum vectors gives the diagonal resolvent at a vertex in class p as [1+Nt+(N-p)t²]/[(1+Nt)(1+(N-p)t)], t=θh. Subtraction for p>q gives the positive difference t(p-q)[1+(N-1)t]/[(1+Nt)(1+(N-p)t)(1+(N-q)t)]. The inverse is nonnegative: if (I+tL)x is nonnegative and x has a negative minimum at i, then [(I+tL)x]_i≤x_i<0. T=[R−(1−θ)I]/θ for θ>0, and T preserves constants. For finite h the diagonal resolvent is strictly above 1/N and tends to 1/N as h→∞; hence θ=1−1/N is included in the unbounded regime. Below that threshold, clearing positive denominators gives 1+Bh−Aθh²; the unique positive root for θ>0 is the stated radical. Euler gives the exact linear restriction and the same active classes, with equality allowed. The strict increase with s is in the finite-horizon regime, as in the proof, and the Crank–Nicolson specialization follows by substitution. At h=c/N the diagonal limit is 1/[1+θ(1−α)c], also for bounded s when α=0 since the nonconstant denominators coalesce. Bracketing the level 1−θ at two fixed c proves the scaled limit; Euler is direct. Independent replay: python3 /workspace/review_checks.py 1 checks 78 full rational step matrices, including exact roots and both sides, and a step at the critical θ; finite corroboration only. Frozen verification and checker were inspected, not executed.

## originality

PASS

The supported distinct result is the sharp fixed-graph all-θ horizon with smallest-part reduction, including its exact failure class and general scaled limit. Prior spectral-projector and diagonal-resolvent frameworks are credited. The overlap with the later Crank–Nicolson record is exact within that specialization; the complete-bipartite record overlaps a subfamily only. The date ordering is not used as proof of priority.

## value

PASS

For a diffusion integrator the precise loss of nonnegativity matters, not just stability or a sufficient step bound. The structural result replaces a full-matrix positivity test on arbitrary multipartite profiles by two graph parameters, identifies exactly which vertices cause failure, and determines the large-N scaling under arbitrary admissible profiles. The general resolvent framework alone does not supply that graph-level reduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
