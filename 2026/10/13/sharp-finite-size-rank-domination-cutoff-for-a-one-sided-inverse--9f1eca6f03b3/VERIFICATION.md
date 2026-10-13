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
# Reproduction and limits

Use `python3 verify.py` with Python 3 and no nonstandard dependencies. It recomputes primary-polynomial products over \(\mathbb F_2\) and \(\mathbb F_3\), enumerates all invertible matrices up to sizes \(N=1,2\), checks vanishing of the canonical annihilator and its sharp Laurent lift, and verifies explicit failure at the next size. It also checks the rank equality of \(XY-I\) and \(YX-I\) and the predicted truncated rank inequality for every pair at sizes at most two in the stated prime-field cases.

Expected final marker: `VERIFY_OK`. The run reports 6839 exhaustively tested full matrix pairs: 260 at \((q,N)=(2,2)\), 9 at \((3,1)\), and 6570 at \((3,2)\). It also checks four groups of invertibles and the \(D_{2,3}=11\) degree count.

The finite checks are not certificates for unbounded matrix sizes or arbitrary extension fields. The proof establishes the full prime-power and arbitrary-size assertion by rational canonical form, Laurent support, and finite rank inequalities. No independent audit or external validation has been performed.
