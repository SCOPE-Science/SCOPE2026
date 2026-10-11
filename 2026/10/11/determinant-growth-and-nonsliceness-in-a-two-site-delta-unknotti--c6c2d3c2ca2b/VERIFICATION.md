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

The exact determinant proof uses the published Montesinos formula and symbolic arithmetic. For \(b\ge-1\), the factors \(8b+13\) and \(24b+41\) are positive and odd, their greatest common divisor is \(1\), and \(24b+41\equiv2\pmod3\). This proves nonsquareness for the full infinite range. The strict first-difference formula is \(384b+832>0\).

A standalone verifier checks these arithmetic identities for \(-1\le b\le19\) as a reproducibility sanity test. That finite run does not certify the infinite theorem; the displayed symbolic equalities do. The local-move properties \(u(K_b)=u^{\Delta}(K_b)=1\) and the existence of two unknotting delta-moves are taken from the cited source construction and were inspected in the source text.
