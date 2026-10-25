---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

For 2n cyclic vertices, each non-diameter candidate length class is 2-regular with 2n chords; the diameter class is a 1-regular perfect matching with n chords. A prescribed edge occurs with p=1/(2n-1); disjoint edge pair with q=1/[(2n-1)(2n-3)]; overlapping edges cannot co-occur. Counting ordered shared-endpoint pairs (4n within a short class, 8n between shorts, 4n short-diameter, zero diameter-diameter) gives covariance A=4n(n-1)/(2n-1)², B=-8n(n-1)/[(2n-3)(2n-1)²], C=-4n(n-1)/same denominator, D=4n(n-1)²/same denominator. Since sum L_j=n, constant eigenvector eigenvalue0; short-class sum-zero vectors eigenvalue A-B=4n(n-1)/[(2n-3)(2n-1)] multiplicity n-2; diameter contrast eigenvalue D-C=4n²(n-1)/[(2n-3)(2n-1)²]. Weighted-variance isometry follows by orthogonal projection. Independent exact full matching enumerations n=2,..,6 verified all entries and null row sums; n=2 empty short-difference eigenspace handled. Formula for arbitrary n is proved combinatorially.

## originality

PASS

Acan has the same length notion and formula for mean and variance of prefix sums Z_k; this supplies partial 2nd-moment data and is credited as substantial overlap. Acan and Paguyo do not give the individual full covariance block matrix, diameter contrast, two positive eigenvalues or all-weight variance identity in inspected results.

## value

PASS

A complete exact covariance operator for the natural entire length histogram, including diameters, with strict negative off-diagonal entries and an all-weight sharp variance isometry, is a reusable finite-sample statistical invariant; even if derived from elementary indicators, it captures more than a one-length mean or a routine scalar substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
