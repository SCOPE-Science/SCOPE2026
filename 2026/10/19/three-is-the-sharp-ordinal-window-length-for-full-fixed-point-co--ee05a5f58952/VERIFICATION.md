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

Conditioning on π(j)=j leaves a uniform injection into the other values. Off-window this leaves every pattern equiprobable. In-window, if j has prescribed rank r, choose r−1 smaller and k−r larger values; each choice has exactly one assignment consistent with the prescribed pattern, so division by (n−1) falling to k−1 and centering gives the displayed kernel. Length one is constant. For length two the scaled descent rows enforce (2i−n−1)a_i=(2(i+1)−n−1)a_{i+1} on a null vector. This gives exactly one free scalar when n is even and exactly one unconstrained middle coordinate when n is odd, including n=2,3. For length three, swapping ranks 1 and 2, and 2 and 3, at the first two positions while holding the third rank fixed yields a 2×2 system in the first two null coordinates. Expanding the two scaled rank contrasts at h gives (n−h)(n−3h+1) and (h−1)(2n−3h+2). The adjacent determinant is 2(n−2)[3(j−n/2)²+n²/4−1]>0. The third column cannot be identically zero: the contrasts cannot both vanish at an interior h, and one is nonzero at each boundary. Each consecutive triple annihilates only zero there, and the triples cover all columns. For longer windows, summing indicators of patterns extending the prescribed triple includes each three-window covariance row in the longer row span. This proves the full rank classification, not merely a finite check. Independent replay: python3 /workspace/independent_checks_oct19.py (permutation_check), enumerating 7658 joint-event cells for every k up to n for n=2,…,6 and testing maximal rank modulo 1009 on the scaled integer matrix (the exact zero and n−1 upper bounds follow analytically). The supplied checker was inspected, not executed.

## originality

PASS

The k=2 law is already known, and its rank follows mechanically from those entries. The supported distinct structural contribution is the all-length position-resolved calculation together with the sharp full-rank change at k=3 and its extension to every longer window. Later listed results give the same local kernel or length-four specialization but use it for summed covariances rather than rank. Priority is not claimed from catalogue dates alone.

## value

PASS

This gives a sharp minimal observation window for joint rank information about all labeled fixed points. Two-position comparisons leave a specific blind direction, while the full three-position pattern resolves it at every finite size and all longer lengths. The statement is stronger than a total fixed-point covariance and gives a useful benchmark for local ordinal observations, without promising conditioning bounds or samplewise recovery from rank alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
