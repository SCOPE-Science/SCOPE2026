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

# Reproducibility and verification

Run `python3 VERIFY.py` with an ordinary Python 3 interpreter (standard library only). The deterministic program constructs the required Eulerian tours and tests \(3\le k\le18\). It verifies that every permissible length-\(k\) word occurs once except the specified words which occur twice, that no other factors occur, that the host is itself circularly run-two, and that lengths equal \(2(F_{k+1}+F_{k-1})-2\).

The program checks mandatory-plus-extra degree balance and the equality of its tight-edge potential certificate for the same range. For \(3\le k\le14\), it additionally enumerates **every** binary length-\(k\) edge and verifies the potential difference never exceeds one. A separate minimum-cost-flow calculation on the unrestricted full binary overlap graph reproduced the theoretical extra-edge optimum for \(3\le k\le13\), including paths through forbidden factors; this independent check is recorded as a result but is not required for replay of the included standalone script.

Successful execution concludes with `VERIFY_OK`. All-order correctness rests on the explicit proof in `RESULT.md`, not on these finite instances. No external independent audit is asserted.
