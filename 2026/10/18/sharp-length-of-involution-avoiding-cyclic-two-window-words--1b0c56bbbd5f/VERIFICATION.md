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

The reproducible checker in `verify.py` constructs the directed edge selection in the proof for \(1\le t\le15\) and \(0\le f\le8\), and verifies pair-orbit uniqueness, missing-pair count, edge count, degree balance, connectivity, an Eulerian circuit, and its exact cyclic windows. The complete output is in `verification_output.txt`.

Four additional small parameter pairs are exhaustively tested by enumerating all cyclic words up to the claimed optimum and checking each cyclic two-window. These checks are independent finite confirmations of the explicit construction and upper bound; neither the computer checks nor their logs prove the infinitely quantified formula. The written cut-parity argument and block construction establish the general theorem.

No independent external validation has been performed.
