---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For a generic Gaussian normal, all crossed-edge hyperplane vertices are ±vij with norm sqrt(Xi²+Xj²)/(Xi+Xj). Thus min vertex radius R=(1/sqrt2)sqrt(1+Z²) for minimum normalized gap Z, while known section diameter is from min and max half-normal Xi. Small-gap pair probability is 4δ/π+o(δ); factorial-moment overlap graphs decay as O(n^-1), proving n²Z converges to Exp(2/π). Conditioning on minimum Xi>t/n retains iid truncated half-normals and the same asymptotic Poisson rate, establishing independence from n minXi. Gaussian max normalization and Taylor/Slutsky yield independently E~Exp(1/sqrtπ) for n sqrt(log n)(2-D) and W²/(2sqrt2) for n^4(R-1/sqrt2), W~Exp(2/π). Checked constants algebraically; no bounded simulation offered as asymptotic proof.

## originality

PASS

Published Resultary exact diameter result already gives the first marginal and geometry, not smallest section vertex radius or their joint independence. Nagaraja–Bharath–Zhang treats local spacings about an order statistic, not a global relative-gap minimum coupled to the sample minimum. General diameter works supply motivation and bounds, not the two-component joint law. This is best-of-knowledge originality, not a proof of historical priority.

## value

PASS

A sharp fourth-order geometric vertex-radius extreme and its independence from the diametral first-order fluctuation gives a structurally informative joint limit beyond the prior diameter marginal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
