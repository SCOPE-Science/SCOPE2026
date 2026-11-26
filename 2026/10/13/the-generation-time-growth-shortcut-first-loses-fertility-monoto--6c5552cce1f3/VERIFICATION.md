---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Euler–Lotka has the unique positive factor λ=(a+√(a²+4b))/2, strictly increasing in each positive contribution, and r=log λ preserves that ordering. For S=a+b, the denominators of the shortcut before and after the unit increment are 2S−a and 2S+2−a. Cross-multiplication gives a strict decrease exactly when D(S,a)=S(2S+2−a)log S−(S+1)(2S−a)log(S+1)>0, equivalently the stated integer-power comparison. D is affine and strictly increasing in a, with slope (S+1)log(S+1)−Slog S>0 for S≥2. Thus check a=S−1 for S=2,3,4,5 and a=4,5 for S=6. Independently certified rational log brackets give signs −,−,−,−,−,+, respectively, using the convergent log series at z=(S−1)/(S+1) and a geometric tail bound; see /workspace/audit_evidence/replay.py (demography). This exhausts the stated grid since S=1 has no positive pair. The decrease is from 1.5357938308 to 1.5134856715 while the true rates increase from 1.6472311464 to 1.6812526457; decimal checks agree. Differentiation yields the stated continuous mechanism, and strict Jensen for at least two ages at R₀>1 gives the lower approximation without implying monotonicity. The boundary is for one-unit later-age additions with positive integer contributions and the cohort mean, not a universal biological threshold.

## originality

PASS

Credit the cohort-mean approximation, the exact Euler–Lotka equation and general reproductive-timing effects as known. The distinct claim found here is a direction reversal under added late fertility, with the exact first integer boundary and its unique witness. The closest inspected indexed timing result holds R₀ and the cohort mean fixed, whereas the perturbation here changes both. The inspection establishes no absolute priority.

## value

PASS

A common lower approximation for growth can misrank a plain increase in fertility, not just miss the size of its effect. Two reproductive ages and a one-unit later-age increase give a minimal transparent test, and the exact cutoff identifies when the failure first becomes possible on that grid. The witness is useful as a stress test of the approximation and does not represent typical conditions, a universal cutoff, or a reason to reject use near replacement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
