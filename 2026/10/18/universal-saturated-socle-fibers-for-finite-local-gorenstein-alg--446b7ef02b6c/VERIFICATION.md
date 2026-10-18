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

# Reproducibility

The included `verify_socle.py` is a standalone Python 3 script. Run `python3 verify_socle.py` without dependencies. It enumerates all bit-coded matrices over \(\mathbb F_2\) in dimensions three and four; compares \(T^2=C\) and \(T^3=C\) fibers with the universal formula for the appropriate truncated polynomial rings; and enumerates all commuting square-zero pairs \((X,Y)\) in dimension four with \(XY=C\). It checks precisely one representative rank-one square-zero target; conjugation makes other targets equivalent. All three exhaustively computed cardinalities agree: \(2\), \(24\), \(24\). Integer orbit-stabilizer identities are also checked for algebra lengths \(2,3,4,5,6,8\) and field orders \(2,3,4,5\). The program ends with `VERIFY_OK_SOCLE_UNIVERSALITY` if every assertion holds.

Only finite small fields and specific algebra presentations are directly enumerated. The proof of the general claim is the socle-intersection lemma and the explicit stabilizer/centralizer calculation in RESULT.md, not the experimental output. Independent audit is not performed.
