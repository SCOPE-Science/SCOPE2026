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

## Mathematical checks
The affine conjugacy was expanded exactly. The finite-field identity \(\sum_{r=0}^{p-1}r^2\equiv0\pmod p\) follows from \(p(p-1)(2p-1)/6\) for every prime \(p\ge5\). The return-shift induction uses the verified derivative relations \(G_n'\equiv1\pmod p\), \(G_n''\equiv0\pmod p\), and \(\sum_{j=0}^{p-1}\lambda^j\equiv p\pmod{p^2}\) whenever \(\lambda\equiv1\pmod p\). The specialization \(p=5,c=-1\) agrees with the formula modulo \(25\) and \(125\); this finite check is not used as an infinite proof.

## Scope and limits
The result is restricted to \(p\ge5\), \(v_p(1-4c)=1\), and the invariant ball \(\frac12+p\mathbb Z_p\). It does not classify the complement. The general minimality consequence is already implied by a published ergodicity criterion; the retained claim is the exact return-shift coefficient. The literature search was bounded. Independent audit and external validation have not been performed.
