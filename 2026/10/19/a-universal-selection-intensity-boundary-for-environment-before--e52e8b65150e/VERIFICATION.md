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

With two independent partners and cooperator probability x per partner, the expected extra return from the focal contribution in the conditional environment is E[(1±δ)^j]−1=(1±δx)²−1, since r/3=1 and j is the number of cooperating partners. The stated protocol feeds these conditional mean gaps to the Fermi map, giving the weighted tanh drift. The sign reduces to p>q_s(t). In particular the exact identity 1/2−q_s(t)=sinh(st²)/(2 sinh(2st)) follows from the tanh addition/subtraction identities. For t>0 its right side strictly decreases in s since u coth u is strictly increasing on u>0 and st²<2st. The minimizer of q_s on [0,δ] cannot be zero; comparison at a minimizer for the larger intensity proves strict increase after minimization. Strict positive drift at a right endpoint implies strict positive drift just inside it. Uniform normalized-sinh expansion proves the weak limit. With z=st, the scaled gap converges locally uniformly to z²/(2 sinh(2z)) and is bounded above by z² cosh(δz)/(2 sinh(2z)), which tends to zero at both scaled endpoints. The positive value at a fixed z therefore confines the optimizers away from both endpoints. Strict concavity of tanh(2z)−z for z>0, positive derivative at zero and negative value at z=1 give the unique positive maximizer. This verifies the strength asymptotic and localization of every optimizer. Strict monotonicity and continuity give the finite critical strength in the stated open p interval; above it strict negative drift forces each interior orbit down to 0. At t=2/3 the ratio sign is controlled by 1−3 tanh²(4s/9), and the average-first gap is 8/45. Independent bounded replay: /workspace/branches/independent_replay.py, selection(), recomputes the numerical constants, not the uniform limit. Read the source's equal-sampling wording as independent partner sampling with Bernoulli(x) strategies, not strategies equiprobable regardless of x; the explicit ODE and conditional gaps specify the theorem unambiguously.

## originality

PASS

The distinct theorem is the global monotone strength boundary and the optimized strong-selection asymptotic for the specified three-player update. Credit Zhu et al. for the underlying public-goods game and the average-first comparator, and Traulsen–Nowak–Pacheco for applying the nonlinear comparison before averaging stochastic realized payoffs. Neither the stochastic Fermi principle nor an observation that averaging and Fermi do not commute is novel here.

## value

PASS

The exact optimized boundary shows not merely that nonlinear averaging alters a rate but that it can remove every positive interior cooperation drift as selection becomes strong, while the averaged-payoff protocol retains a positive region. The sharp constant, localized frequency scale and exact witness give usable benchmarks for a natural modeling choice. This does not assert universal cooperative fixation below the boundary or a result for individual realized payoff samples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
