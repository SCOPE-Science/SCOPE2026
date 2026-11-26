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

Exact evolution scales the input by exp(-cs²/2); Euler at s=0 does nothing and the second step scales by M=1-ct(1-t). For centered scalar Gaussian laws, including the zero-variance point mass, W2 is the absolute distance between standard deviations, which uses |M|. The attainable multiplier interval is [1-c/4,1). If +r is not attainable, the interval is wholly above +r and the midpoint is optimal. Roots for +r and -r exist exactly when their respective quadratics have nonnegative discriminant; +r and -r roots are disjoint and the merged roots are counted once. The two threshold functions are respectively strictly convex with negative derivative at zero (and positive eventually) and strictly increasing; their indicated endpoint signs yield the claimed phase counts. At a negative root the shared-input particle discrepancy is 4r². For the residual, material acceleration is (lambda'+lambda²)x and is already a Wasserstein gradient; its half-norm is |lambda'+lambda²| sigma/2. Dilation to the terminal law scales a standard-deviation perturbation by sigma(1)/sigma(s), giving the stated propagated weight. At c=4 the unique equal-mass split satisfies 1/2<q<2/3: the first half has mass pi/8, smaller than the chord bound sqrt(3)/4 for the second half; the mass up to 2/3 is bounded below by pi/8+sqrt(7)/36>4/9, which is an upper Jensen bound on the remaining mass. Therefore the surrogate has strictly positive exact terminal error while the interior quadratic roots attain zero. For the perturbation, the exact roots at epsilon=0 are simple, hence persist by the implicit function theorem. Simultaneous small epsilon and positive delta give uniform convergence of weights and cumulative masses; strict increase of the limiting cumulative mass gives continuity of the median. The positive error persists, even though delta regularizes only the weight and not the ODE. No explicit uniform perturbation interval or finite-N failure of the source's local-surrogate theorem is asserted. Independent replay: python3 /workspace/reproductions/frozen_checks.py gaussian evaluates an exact primitive on the upper half, giving q about 0.63916669265747 and error about 0.05786580985574. Frozen verification code and notes were inspected, not executed.

## originality

PASS

The Gaussian W2 identity, Euler scheme and propagated-residual quantile minimization of a local surrogate are known. The distinct findings are the variable-split phase classification with signed multipliers and the terminal-W2 noncompetitiveness witness at fixed budget including the strictly contractive perturbations. The source's surrogate theorem expressly does not compare against the best full endpoint grid; this result does not contradict it.

## value

PASS

At a motivated fixed step budget, a simple exact witness separates a source-motivated local allocation from a law-level terminal objective, even with contraction and positive allocation weights. The sign-sensitive phases show a genuine distinction from strong paired-particle accuracy. The witness and its robustness are more substantive than evaluating an error formula on a single grid.

The dated certificate retains the supplied scientific assessment, sources and limitations.
