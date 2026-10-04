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

The connected-graph upper bound is a deductive argument, not a finite experiment. Its critical accounting is: the first edge-special line contains at least three configuration points; an additional retained line shares at least one old configuration point by connectedness; if it shares at least two, it is already contained in the old affine span; if it shares exactly one, it introduces at least two new points and can increase affine dimension by at most one. Hence \(d\le\lfloor(n-1)/2\rfloor\).

The tree lower bound is likewise deductive. `verify.py` only stress-tests its combinatorial reduction. It enumerates every nonisomorphic tree of orders \(3\) through \(12\), chooses a diametral endpoint, performs exactly the two deletion cases used in the proof, checks that the remainder stays a tree of order two smaller, and checks that the number of restoration steps gives \(\lfloor(n-1)/2\rfloor\). The recorded check covers \(985\) tree types and reports `ALL CHECKS PASSED`.

No finite enumeration is used to infer the theorem for larger orders, and the script does not attempt to certify arbitrary real point configurations. The geometric upper bound and the existence of a new transverse line in the inductive construction are proved in `RESULT.md`.
