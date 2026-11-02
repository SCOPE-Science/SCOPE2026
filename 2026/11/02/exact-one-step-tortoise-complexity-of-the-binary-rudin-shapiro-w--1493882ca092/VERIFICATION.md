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

# Verification record

Run `python3 verify_rudin_tortoise.py` with Python 3 standard library from the same directory. The source file is complete and does not import external packages. The accompanying output is an actual execution record and ends in `ALL_FINITE_CERTIFICATES_PASSED`.

The finite generator enumerates every factor of length L via all two-block images under a fixed uniform substitution, where the complete adjacency closure is eight listed pairs. It verifies: all length-five four-letter left-special factors and preceding two-letter contexts; injectivity of length-eight coding; that `00000` is absent; all ordinary and tortoise image counts for lengths 1–12; and the exact eight length-12 doubleton collisions. Longer checks through length 128 are illustrative only.

The extension to all n≥12 is proved by uniqueness of the four-letter lift, exact context structure, the cited factor-complexity theorem of Berthé and the collision-prefix inheritance lemma. None of the finite checks is misrepresented as an infinite certification. No independent mathematical audit was performed.
