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

From the binary payoff average \(\bar u=xu_1+(1-x)u_2\), exact expansion gives \(x(u_1-\bar u)=x(1-x)(u_1-u_2)\). For the government coordinate this is exactly the complement factor removed between the source's Eq. (7) and Eq. (19).

At \((x,y,z)=(1,0,1)\), every \(yz\) and \(1-z\) term in Eq. (19) vanishes. The source's baseline values give \(3-2.5+1.5=2\), an outward normal velocity at the face \(x=1\). The unreduced equation multiplies the same payoff difference by \(1-x=0\), so its normal velocity is zero.

The bundled `verify.py` checks these algebraic identities and the exact rational baseline witness. No independent audit has been performed.
