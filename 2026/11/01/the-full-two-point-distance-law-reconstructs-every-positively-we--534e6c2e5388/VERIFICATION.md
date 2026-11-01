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

# Verification
The proof uses exact same-arm distance integration, bounded-convolution integration for distinct arms, distributional differentiation and finite induction on sorted positive lengths. Every cross-arm pair sum involving a yet-unrecovered arm is strictly larger than its least length, so cancellation by the known pairs is handled exactly. No numerical calculations are required for the arbitrary-real theorem.

The included `verify.py` requires only Python 3 standard library. Execute `python3 verify.py`. The completed local execution returned:

`VERIFY_OK 77483 exact independent density identities, inverse reconstructions and normalization checks`

All calculations are exact rational arithmetic and deterministic seeded tests. The script uses distinct direct-integration and normalized-spline implementations, and independently checks inversion from signed atoms; nevertheless, any finite collection of computations is not a proof of universal recovery.

The claim excludes one- and two-arm path subdivisions, arbitrary nonstar graphs, noisy observed laws and reconstruction stability. Historical novelty is assessed provisionally; no independent audit has been conducted.
