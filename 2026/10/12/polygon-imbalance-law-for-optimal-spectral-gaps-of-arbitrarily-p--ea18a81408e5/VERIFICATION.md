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

# Reproducibility and limits

The analytic proof in `RESULT.md` supplies: (1) the polygon-resultant geometry, (2) a global Rayleigh certificate for *all* admissible prices and rates, (3) explicit attainment and positive edge rates, (4) a closed-form nonnegative quadratic identity that proves the candidate is the actual spectral gap, and (5) uniqueness via equality in the same Rayleigh certificate.

Run `python3 verify_star.py` using a standard Python 3 interpreter. The checker uses only `fractions`, `itertools`, and the standard library. It enumerates all 1,360 ordered integer-length lists with between two and five leaves and length entries from one through four, meaning integer square prices. It tests exact budget identities, positivity, leaf eigenrelations, and 77,488 exact rational specializations of the quadratic decomposition; its expected summary is `VERIFY_OK 1360 exact cost/eigenvalue cases; 77488 exact PSD-factorization tests`. These are finite regression checks, not exhaustive verification of all real price vectors or all leaf counts.

The previous mathematical literature provides the general duality and the uniform-cost star comparison, not an independently audited novelty certificate. No independent mathematical audit has been performed; specialized historical overlap remains possible.
