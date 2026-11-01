---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Reconstructed distinct one-deletion descendant sets for weight-two words. For fixed first one i, pairs with second one j and j+1 share two distinct descendants: weight-one word with one at i, and weight-two word obtained by deleting an appropriate zero. Hence at most ceil((n−i−1)/2) choices; sum floor(n²/4). For proposed odd-gap pairs, weight-one descendant positions i,j−1 share parity i; three possible weight-two descendant position pairs have three mutually distinct parity patterns. Same-parity i groups have no shared weight-two descendants; opposite-parity groups cannot have two distinct shared weight-two descendants. Thus all intersections ≤1. Independent full reconstruction graph exhaustive maximum independent-set search for n2..11 confirms formula, including small n=2 boundary, and direct parity witness validity. Infinite theorem based on discrete graph/path argument, not this bounded check.

## originality

PASS

Cai–Kiah–Nguyen–Yaakobi (2020) gives exactly the two-read error-ball intersection model for arbitrary binary sequences and asymptotic redundancy; its accessible complete HTML does not report the sharp constant-weight-two floor(n²/4) optimum. Cullina–Kulkarni–Kiyavash treats constant-weight **one-read deletion correcting** graph coloring, not the two-read threshold intersection≥2. Levenshtein (2001) established reconstruction-coverage framework but its complete source remained inaccessible and is a priority risk. A previously tabulated weight-two induced graph independence number remains possible.

## value

PASS

For the natural first nontrivial constant-weight slice, the two-read deletion model changes forbidden edges and yields an exact all-length capacity and simple systematic optimal construction. It is a meaningful sharply solved coding case rather than a redundant one-read coloring bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
