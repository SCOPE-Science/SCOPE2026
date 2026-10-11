---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The exact two-deletion sphere identity in run statistics was checked independently against literal deletion sets for every binary word through length nine. Writing transition bits as independent Bernoulli variables gives a quadratic polynomial whose Walsh expansion has every linear coefficient \((m-1)/4\) and every quadratic coefficient of magnitude \(1/4\); orthogonality then gives \(m(m-1)(2m-1)/32\), i.e. \((n-1)(n-2)(2n-3)/32\). The package verifier independently checks the per-word run formula through length twelve and the closed Walsh variance through \(n=200\).

## originality

PASS

PASS. Swart and Ferreira's full primary paper supplies the exact per-word two-deletion subsequence count in run statistics, which is the necessary starting identity, but it does not study the random-center mean/variance distribution. The submitted Walsh calculation converts that structural formula into an exact variance law. Resultary searches returned nearby random-string and deletion-code work, not this moment formula.

## value

PASS

The variance of a deletion-sphere size is a natural quantitative measure of channel irregularity. The exact cubic polynomial gives a clean fluctuation scale and the Walsh proof exposes a reusable structural simplification, rather than merely enumerating a finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
