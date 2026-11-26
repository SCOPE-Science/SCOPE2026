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

Independently recomputed all 32 stored cycle-distance entries over Q(h) using Euclidean inversion in the circulant polynomial ring Q(h)[x]/(x^n-1), not the frozen matrix-inversion script. Replay: set ell=2-x-x^(n-1), invert 6+4h ell+h^2 ell^2 modulo x^n-1, multiply by 6-2h ell, reduce, and take the coefficient of x^d. Exact cross multiplication matched coefficients.json in every case. All reduced denominators have positive coefficients, and every numerator except (10,5) has nonnegative coefficients and is nonzero. At (10,5) the numerator is 2h^5 times the stated quintic over the stated positive product, with witness -3544/384641341535 at h=1/10. The quintic is strictly increasing on h>=0 and changes sign strictly between 1/10 and 1/9; the unique root is 0.10872339507099547297354235092584205 to the shown precision. Thus at the root exactly the ten ordered antipodal entries vanish. At h=0 the step is I. The denominator spectrum is strictly positive and the constant mode has gain one. Scalar Taylor division gives +1/108 at fifth order in R(-x); earlier powers cannot join vertices at distance five and each shortest length-five walk contributes -1 to (L^5)_{uv}. This proves the required small-step negative sign for every fixed larger n, while R(-h lambda) tends to zero on every fixed nonconstant mode, giving eventual strict positivity. The finite certificate does not cover arbitrary larger-order positivity sets, weighted cycles, or internal stages. Inspected VERIFICATION.md, verify.py, requirements.txt and the entire coefficient certificate by structured comparison; the frozen executable was not run.

## originality

PASS

The supported contribution is the exact all-step C10 reentry set, critical entry, and explicit quintic, with all-step positivity proved for C3 through C9. The cutoff for arbitrarily small steps, the fifth-distance mechanism, and large-step recovery were already proved for identical dynamics in the Oct. 13 Resultary record and are not credited as discoveries here. A later-dated record also gives all-step positivity through C9 but not the C10 positive threshold or its full timestep set. Display dates alone do not establish priority.

## value

PASS

The first small-step failing periodic order is motivated by a known sharp obstruction. Knowing that order alone leaves the practical and mathematical question of whether the first failing matrix ever becomes nonnegative and whether it later loses positivity again. An exact connected positive half-line separated from the zero step, with the unique root and the exact vanishing entries, resolves that gap and provides a benchmark that the earlier asymptotics cannot supply.

The dated certificate retains the supplied scientific assessment, sources and limitations.
