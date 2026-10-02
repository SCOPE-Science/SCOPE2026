---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-02.md",
      "INDEPENDENT_AUDIT_2026-10-02.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

Complete RESULT proof read end-to-end, with Chu Theorem 3 and Lemmas 8-10 checked in the primary PDF. LTE and the monotone geometric-sum bounds make the residual ranges exhaustive: p=1 mod 4 is excluded; p=7 leaves only beta=2; for other p=3 mod 4, v<=4, q<3*2^(v-1), alpha<=lambda+v. The v=1 Mersenne case and beta=4 factor constants are excluded analytically. An independently written exact-integer replay obtains respectively 8,62,33 tuples and maximal valuations 1,1,2 in the remaining (v,beta)=(2,12),(3,8),(4,16) cases, all below beta-1. The finite calculation follows the analytic bounds; it is not an unbounded experiment.

## originality

PASS

Chu's primary paper explicitly leaves the general beta-greater-than-one statement as Conjecture 5 after proving only k=5. Current Resultary search found the assigned k=7 theorem but no earlier or stronger published k=7 resolution. Originality therefore appears to pass to the best of current knowledge, conditional on correctness being resolved.

## value

PASS

Resolving the next Mersenne-exponent case of an explicit published conjecture is a motivated arithmetic advance, and the claimed proof uses exceptional-prime and finite-reduction work rather than a tiny numerical check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
