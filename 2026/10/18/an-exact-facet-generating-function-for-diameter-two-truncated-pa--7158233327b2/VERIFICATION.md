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

# Verification details

Run `python verify_capped_path.py` under Python 3 with the standard library. The program enumerates every normalized ternary word for point-set sizes two through ten (86,525 words), independently checks all pairwise metric inequalities, constructs the saturated-edge graph and tests its connectivity, separately recognizes the claimed run-language, and computes the rational generating coefficients from an integer recurrence. It verifies 5,314 extreme words across the nine sizes, with no discrepancies. A separate SciPy/Qhull halfspace-intersection check returned counts 4, 12, 32 and 84 in dimensions corresponding to sets of sizes three to six.

The checker only establishes these finite cases and does not certify the all-dimensional theorem. The latter uses the exact connectivity classification and block/runs generating-function proof in `RESULT.md`. The proof of asymptotics uses elementary simple-pole coefficient extraction. The initial source dates and scope were checked against the initial arXiv records; incomplete access to all mathematical literature leaves ordinary bibliographic uncertainty. No independent scientific audit has been carried out.
