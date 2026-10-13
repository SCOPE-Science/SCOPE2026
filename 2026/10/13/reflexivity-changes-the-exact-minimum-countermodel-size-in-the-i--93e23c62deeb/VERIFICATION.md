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

Let
\[
B=(\Box a\to\bot)\wedge((a\to\bot)\to\bot).
\]
On the two-world chain \(w\le v\) with universal modal relation and \(V(a)=\{v\}\), neither world forces \(\Box a\) and neither forces \(a\to\bot\). Therefore both implications occurring in \(B\) are true at both worlds, so \(B\) is true everywhere and \(\Box B\) is true at the root. Hence \(\Box B\to\bot\) is false there.

For a one-world \(\mathsf{IS4}\) frame, modal reflexivity is mandatory. If \(a\) is true then \(\Box a\to\bot\) is false; if \(a\) is false then \(a\to\bot\) is true and its negation is false. Thus \(B\) is false under both possible valuations. Reflexivity then makes \(\Box B\) false, so the target implication is true. This exhausts all one-world \(\mathsf{IS4}\) cases.

For a one-world \(\mathsf{IK4}\) frame, choosing empty modal accessibility is allowed. The outer box is then vacuously true, so the target implication is false.

No finite search, timeout, or numerical approximation is used to justify the theorem. The result is limited to the displayed formula and does not provide a general countermodel-size bound.
