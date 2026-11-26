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

The adjacent jump bound implies all Lipschitz inequalities by the triangle inequality, and no intermediate integer between the smallest and largest images can be skipped. Idempotency is equivalent to fixing the whole image interval. For a fixed rank-r interval, each outer tail can be read outward from the corresponding fixed endpoint; its admissible values form a walk on the r-vertex path with a loop at every vertex. Conversely two such walks and the fixed interval give a unique full contraction and retraction. Reflection equates the two endpoint-started counts; summing over tail lengths with sum n-r proves the convolution and squared resolvent for every 1≤r≤n, including constants and the identity. At rank 3 the endpoint and middle start series F,H satisfy F=1+z(F+H), H=1+z(2F+H), so F=(1-2z-z²)^(-1). The independently authored repro/review4.py tested every map at n≤7 with pairwise metric inequalities and equality of fixed set and image. It obtained rank counts (7,192,131,46,14,4,1), total 395, and per-interval rank-three counts (29,24,25,24,29). This checks 131 versus 130 from the exact formula and coefficients transcribed in the frozen record. The 2021 primary conjecture wording was not independently retrieved, so the bibliographic identification of that formula and scope remains a limitation, not part of the arithmetic confirmation. The frozen checker was inspected but not executed.

## originality

PASS

The supported distinct claim is the all-image-rank enumeration of full (not necessarily monotone) contractions and its exact rank-three discrepancy with the prediction recorded in the source package. The known structural and boundary results are credited. A separately indexed, later-dated loopless path record is mathematically equivalent for the rank counts after adding flat steps, as detailed below; it is not evidence that this count was already available before the frozen finding, and no independent rediscovery or priority claim follows from archive dates.

## value

PASS

The complete image-rank polynomial for a standard finite-chain transformation monoid answers a natural enumeration question beyond its boundary ranks. The structural reason is that arbitrary nonmonotone retractions split into two independent constrained exterior walks around a forced fixed interval. It explains the interior-rank figure 131 exactly, including the middle interval's 25 possibilities rather than 24, and makes the recorded rank-three prediction testable. This is not a purely finite brute-force comparison or a claim about partial contractions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
