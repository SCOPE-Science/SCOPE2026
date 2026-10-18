---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS: Inspected frozen RESULT.md and checker.py. Uniform binary pooled labels imply B_j=NA_j-mj and the bridge-area sum ΣB_j=−NQ; Anderson's T equals ΣB_j²/(mnN²). Independent exact Fraction enumeration over all m,n>=1 with m+n<=10 reconstructed E(Q²), E(S), E(Q²S) and the stated covariance. For general m,n the fourth mixed moment follows from the proven sampling-without-replacement factorial indicator moments E∏_{i∈J}X_i=(m)_{|J|}/(N)_{|J|}, |J|<=4; expansion and elementary sums supply the closed polynomial. Positive sign follows mn>=N−1 and numerator≥N²−4; N=2 exactly zero. Limit 1/5 from mn~lambda(1-lambda)N². The finite checks do not alone prove the all-N identity.

## originality

PASS

PASS (best of knowledge): Anderson's 1962 finite null distribution and Pettitt's 1979 component decomposition involve exactly these rank statistics but the materially accessible primary abstracts do not state the all-(m,n) mixed second/fourth moment or covariance. Independent Resultary semantic comparison found no published stronger identity implying this explicit coefficient. Pettitt is an unusually plausible source whose full text was inaccessible after the protected institutional attempt; novelty is provisional, not a proof of historical absence.

## value

PASS

PASS: The exact dependence between standardized squared location rank component and the omnibus CvM statistic is a natural power/calibration diagnostic; strict sign for every nondegenerate sample and universal proportional-sampling 1/5 are mathematically interpretable invariants, not a random numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
