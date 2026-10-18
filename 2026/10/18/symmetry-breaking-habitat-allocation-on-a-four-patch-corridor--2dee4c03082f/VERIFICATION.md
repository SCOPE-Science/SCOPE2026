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

# Verification and reproducibility

Run `python3 verify.py` from this package with Python 3 and no third-party dependencies. The program constructs the exact fractions \(8116/10000\), \(8117/10000\) and \(161/250\), tests the polynomial bracket on the unique positive root of \(t+t^8=1\), and verifies the strict symmetric upper bound after raising both sides to the fourth power. It independently assembles the positive witness \(r=(5,10,11,10)\), checks the integer totals \(S=414749506\) and \(Q=781049340000000\), and tests the exact strict fourth-power gap. All checks ran successfully from the package path.

The root-uniqueness and global-maximizer arguments are analytical and appear in `RESULT.md`, not inferred from numerical enumeration. The small-path minimum is proved there by two- and three-patch formulas; the script performs only illustrative arithmetic checks for small-path cases. The software does not enumerate every area allocation, and no finite test is treated as an infinite-domain proof. The result is not independently audited and makes no stochastic extinction claim.
