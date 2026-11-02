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

Run `python3 verify.py` using Python 3.9 or newer; no third-party dependencies. The script computes the source and target transposition-quandle multiplication tables directly from conjugation, traverses every homomorphism by propagating products of assigned elements, and compares full rank histograms to the proposed count. It checks \(26\) complete source-target parameter combinations: \(3\le n\le6\), \(2\le m\le7\), and the two larger cases \((7,7)\), \((7,8)\). No sampling is used for these finite cases. The additional four-vertex endomorphism check computes all \(24\) rank-three maps, identifies the four rank-three idempotents, and verifies the image multiplication law for their \(576\) ordered products.

Actual execution result: `VERIFY_OK 26 independent source-target censuses; 24 exceptional maps; 4 rank-3 idempotents; all 576 products`.

This supplies independent finite corroboration of the stated full classification but not proof for arbitrary source and target sizes. The abstract edge-intersection argument in `RESULT.md` carries the infinite-parameter proof. The stated classification does not include quandles associated with arbitrary conjugacy classes or arbitrary group homomorphisms. Independent mathematical audit has not been performed.
