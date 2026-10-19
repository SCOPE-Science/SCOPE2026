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

## Reproducibility and logical scope

Run `python verify.py` with Python 3 and SymPy. The program uses exact symbolic rational operations to check stationary generator recurrences up to total degree four for a scalar harmonic filter, a separately derived random-variance renewal perpetuity, the resulting positive fourth cumulant, and a signed two-exponential filter built from two stable modes. The packaged program reports 22 passed exact assertions and their exact rational values. The stationary distribution, all-input positivity, and equality of full two-time covariance laws follow analytically from the proof in `RESULT.md` and are not inferred from finite computation.

## Checks performed

The executable was run against its packaged source. The analytic normalization of the resetting Brownian reservoir was checked against the stationary generator formula and the full covariance kernel. The nonstandard strictness lemma uses a Poisson add-one identity and a gap-splitting calculation; the finite symbolic examples are corroborative only.

## Boundaries

No infinite-network extension, complete uniqueness-of-priority determination, machine-checked formal proof, or independent scientific audit is claimed. The previously published scalar low moments are used as a cross-check, not advanced as a novel finding.
