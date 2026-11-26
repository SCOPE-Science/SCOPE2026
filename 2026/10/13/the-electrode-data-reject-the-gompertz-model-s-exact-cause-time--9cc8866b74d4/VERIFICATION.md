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

The joint subdensity is the cause-specific hazard times the joint survival; dividing by the sum leaves a constant label probability. For independent units and label-neutral observation, removal and stopping, fixing observed times and counts leaves the same likelihood for every placement of the observed labels. Independently recomputed from the frozen Table 8 transcription at verify_gompertz_cause_time.py:21–31 without executing it: order times, assign doubled midranks (two observations at .328 each get 71), and expand the product of (1+x*y^r) over ranks r, retaining degree 19 in x. R_E=219, U=29, doubled mean 874. Grouping the tie with multiplier 2 for selecting one, the coefficients at doubled sums <=438 total 22,633 and those >=1310 total 22,179 (the latter by reflection r→92−r); their sum over choose(45,19) gives 1.837790973889128e−8. The result is a conditional model check, not a test distinguishing all possible alternatives or a check on the latent marginal fits. The published Table 8 layout and the article's printed likelihood could not be independently read; the numerical replay uses the supplied article-specific transcription.

## originality

PASS

The supported distinct claim is the electrode-specific conditional exact rank diagnostic and the resulting observed failure of the common-shape restriction. The hazard-ratio factorization and the permutation method themselves are not novel. No inspected counterpart covered the exact application and result.

## value

PASS

The application matters independently of the standard mark-factorization: cause–time ordering very strongly violates a structural restriction of the fitted model even without estimating parameters. This checks a feature that separate cause-wise curve fits to selected minima cannot validate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
