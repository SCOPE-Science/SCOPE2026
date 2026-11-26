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

The strict one-site comparison gives d>|h_i| for a vacancy, and sigma h_i>d for a sign sigma, where h_i is the sum of the two neighboring spins. Thus at d=0 only the uniform signs survive. At 0<d<1 a mixed state consists exactly of isolated vacancies separating alternating sign-runs of length at least two: a zero needs opposite or both zero neighbors, a sign cannot neighbor its opposite, and a sign at a vacancy needs a same-sign neighbor on its other side. A vacancy block of length at least two cannot border a sign. The alternating runs require even k; the k run lengths sum to n-k with all lengths at least two. Counting a marked labeled vacancy and first sign, then removing the k choices of mark, yields (2n/k) binomial(n-2k-1,k-1), in addition to the three uniform states. At d=1 a single matching neighbor with a vacancy opposite is no longer sufficient; at d=2 even two matching neighbors are no longer sufficient. This confirms both transition equalities under the neutral-move convention. With f=zx^3/(1-x), the even-run-length sum is 2x f f_x/(1-f^2). For fixed positive z near 1, f(r,z)=1 gives a unique simple dominant pole: equality of absolute values on |x|=r would require x^3 and x^4 and every subsequent power to have the same phase, forcing x=r. The pole has principal part x/(r-x); the uniform states are exponentially negligible there. The equation for lambda(z)=1/r yields the entropy and the derivative in log z gives 1/(lambda^2+3). Exponential Markov bounds with small fixed positive/negative log z prove concentration from the limiting log moment generating function, without requiring differentiation of a pointwise limit. Replay: RESULT.md lines 23–41; separate bounded exact-rational enumeration matched all 25 cases n=3 through 7 and d in {0,1/2,1,3/2,2}. The uploaded verify_blume.py and VERIFICATION.md were inspected, not executed; neither finite check proves asymptotics.

## originality

PASS

The evidence supports the model-specific strict absorbing-state classification and full vacancy polynomial for all labeled periodic rings and all nonnegative fields in scope. There is no originality credit for the underlying composition count or the simple-pole method in isolation.

## value

PASS

Vacancies create isolated strictly absorbing interfaces although opposite signs cannot form a direct stable interface. The proof identifies the only field window with nonuniform traps and explains the fate of all configurations at neutral-move boundaries. The exact labeled polynomial supplies more than the entropy: it counts the traps at every vacancy number and yields a concrete macroscopic vacancy density under uniform sampling of the traps, without implying dynamical sampling probabilities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
