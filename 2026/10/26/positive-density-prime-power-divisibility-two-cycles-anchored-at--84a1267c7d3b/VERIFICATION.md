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

Exact checks: run `python3 verify.py`, expected prefix `VERIFY_OK`. Independently check 4^4=256=24 (mod 29), H_5(3)=13021=29*449 and H_29(2)=683705=5*136741. Algebraic argument: K=Q(zeta_40, fourth_root(-5)) is Galois and 29 is unramified. Frobenius at 29 fixes its fourth root, acts as 29 on zeta_40, and its conjugates retain those properties. Chebotarev then gives positive density. For each such q, q=5 mod 8 and -5 is a fourth power, so the order d of -5 is odd and >=3, giving a=(d-1)/2. The converse 5|H_q(2) uses q=-1 mod 5. Tests cannot replace Chebotarev, and mutual prime divisibilities do not imply integrality of the reciprocal-gcd sum.
