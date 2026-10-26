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

## Reproducibility
Run `python checks/check_ajr_boundary.py` from the root of this research package (Python standard library only). The program exhaustively derives the six-dimensional covariance using the eight equally likely ballots, checks its exact entries, checks the two-dimensional marginal yielding the fixed-committee limit, and compares all small labelled profiles (two, three and four voters) against the exact AJR coalition definition after removing precisely stated exponentially unlikely exceptional profile types. Results observed: covariance checked; \(5/8\) fixed-committee marginal checked; for \(n=2,3,4\), respectively \(64,512,4096\) labelled preference profiles were enumerated with no mismatch on the nonexceptional event.

## Proof versus computation
The all-electorate argument relies on an exact ordered-prefix lemma, Hoeffding's inequality and the multivariate central limit theorem. Exact finite enumeration alone would not prove the limit. The displayed six-dimensional orthant is an exact mathematical probability; a separately estimated decimal \(0.9840\) is illustrative and not a computer-assisted interval certificate. Gaussian-moment positive definiteness follows analytically from \(\det\Sigma=2^{-16}\) together with the covariance's positive eigenvalues, or from the explicitly listed eigenvalues \(1/4\) (twice), \((7\pm3\sqrt5)/16\) (each twice).
