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

The source protocol yields exactly the frozen two-state kernel for emitted signed gross works: use its equations (6)–(7), take the positive initial heading, and count each new sign, not the initial one. Information-erasure cost is not counted. Set A=√(ad), B=√(bc). The tilt at θ*=½ log(d/a) has diagonal A,A and off-diagonal product B², so its Perron eigenvalue is L=A+B and the other eigenvalue is A−B. The Perron eigenvalue at additional real tilt x is A cosh x + √(B²+A² sinh² x), giving zero slope and log-curvature A/B. The normalized projector paired with the stated initial and terminal vectors gives (1+√(ac/bd))/2. Conjugate at θ* to the symmetric Doob chain, divided by L, and write the complex perturbation as that chain times diag(e^{it},e^{−it}). The chain is a strict contraction off the constants; an eigenvector with eigenvalue of modulus one requires its phased vector to be constant and then itself constant. Thus only t=0,π modulo 2π attain spectral radius one. Gaussian inversion gives the factor of two on the even subsequence; odd return is impossible. Cauchy–Schwarz on the two square-root row vectors (swapping the second row's coordinate order) gives L<1 unless q=1. In fact L²=1−(1−q)²/(√(ab)+√(cd))², yielding the stated quadratic coefficient. At fixed p the saddle expansions and complementary spectral gaps can all be bounded uniformly for q in a compact neighborhood of 1, including 1, since the positive entries, simple Perron mode and positive limiting curvature persist. Thus n log L has the stated crossover limit. Equal stationary masses force the common flip probability φ; its entropy rate is −log L plus the binary relative entropy to φ*=B/L, including at the irreducible but periodic endpoint φ=1 by continuity (the proof's open interval omits this endpoint, which is strictly suboptimal). The Doob entries agree with that minimizer. The frozen files were inspected, not executed. Fresh run-counting code /workspace/audit_checks/02_work_returns.py uses binomial counts of alternating sign runs, not forward propagation or the asymptotic derivation; its ten fixed-q ratios were within 0.0012 of one, and its six crossover ratios within 0.0078, on the bounded parameter grid in the script. Those are corroborations, not the limiting argument.

## originality

PASS

Credit the explicit initial-state-dependent local return prefactor and the uniform near-symmetric crossover for the engine. The sign kernel, exact finite-time propagators, basic tilted eigenvalue method and general entropy/Doob prescription are antecedents, not distinct findings; the rate and symmetric kernel are explicit model consequences that explain the return result. No checked statement gives the local amplitude and uniform parameter-dependent profile. This is a bounded best-of-knowledge decision with a significant inaccessible-prior-work risk for the two-state occupation problem.

## value

PASS

A mean or a variance does not quantify the cycle probability of zero gross extraction once feedback is weak but nonzero. The precise parity-sensitive probability and near-symmetric crossover quantify the change from polynomial to exponentially small returns on the natural (1−q)⁻² scale. The explicit driven kernel interprets the balanced-work trajectories within the stated entropy minimization, without pretending to determine cost-adjusted work or general conditional path limits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
