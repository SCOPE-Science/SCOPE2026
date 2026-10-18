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

# Verification and limits

Reproduce the finite checks by running `python3 verify_biclique.py` using the included standalone Python 3 script. No additional packages or files are required.

For every pair of positive integers \(a,b\le8\), the program independently constructs all three projection matrices from rational arithmetic; verifies their orthogonality, idempotence, sum, and the exact edge-covariance formula; constructs every candidate norming vector using the analytic weights; checks its designated edge value and its maximum edge difference; and checks the Gram operator of the norming family against the analytic projection \(P_A+P_B+P_C\). The script uses rational arithmetic for projection identities and floating-point comparisons for expressions involving square roots. It checks singleton blocks, balanced cases, and strong asymmetry.

The program is a finite regression of essential proof identities, not an infinite-domain proof, a uniqueness certificate, an independently audited result, or a comprehensive novelty search. The rigorous proof for arbitrary positive integer parameters is contained in `RESULT.md`.
