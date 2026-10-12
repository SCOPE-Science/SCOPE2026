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

The verification uses only exact integer arithmetic. For \(A=xH+yC\), it checks
\[
p=3x+8y,\qquad q=37x+8y,
\]
\[
x=(q-p)/34,\qquad y=(37p-3q)/272,
\]
and
\[
2176A^2=p^2+66pq+q^2.
\]
For \(A^2\le16\) and \(p,q>0\), the inequality \(pq\le527\) makes enumeration finite. The script enumerates all such pairs, imposes integrality and primitivity, and confirms exactly the four square levels \(2,4,8,16\), with no primitive ample class of square \(6,10,12,14\). It also verifies the involution pairing \((x,y)\mapsto(-x,5x+y)\).

The computation does not test any claim beyond square \(16\), and it does not substitute finite experimentation for an unbounded assertion: the proof supplies the explicit finite bound before enumeration.
