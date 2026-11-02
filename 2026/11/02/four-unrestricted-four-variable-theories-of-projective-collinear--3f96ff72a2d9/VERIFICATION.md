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

# Reproducibility and limits

Run `python3 verify.py` using Python 3 with no third-party dependencies. `verify_output.txt` is the actual output from the included program, not a theoretical prediction. The program enumerates normalized homogeneous coordinates over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), and \(\mathbb F_5\), performs exact Gaussian elimination to decide inclusive collinearity, and exhaustively checks every stationary ordered triple and all its fourth-point atomic extension patterns.

Executed projective dimensions/orders: \((d,q)=(1,2),(1,3),(1,4),(1,5),(2,2),(3,2),(2,3),(3,3),(2,4),(2,5)\), containing a total of 109,399 ordered stationary triples. The program reports exactly four distinct support templates, each invariant within its class, matching the two-bit classification. This checks the finite instances; all-orders and non-Desarguesian assertions instead follow from the separate proof using exact line counts and the geometric plane spanned by three noncollinear points. The five-variable skew-line separation is proved geometrically, not inferred from the script.

The logical validity additionally uses the standard noncounting pebble-game correspondence, whose source is Grohe and Otto, arXiv:1204.1990, §2. The verification makes no claim of external or independent mathematical certification.
