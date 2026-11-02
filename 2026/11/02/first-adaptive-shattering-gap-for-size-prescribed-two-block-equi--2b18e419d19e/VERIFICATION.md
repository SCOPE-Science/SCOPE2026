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

# Verification and scope

Execute `python3 check_balanced_partitions.py` using Python 3.9 or later, with no additional packages. The program regenerates `balanced_five_certificate.json` deterministically and prints the same lines as `verification_output.txt`. It enumerates the entire finite two-block hypothesis spaces for orders two through five, evaluates VC dimension by testing fixed query supports, and evaluates Littlestone dimension by recursive binary-branching of exact version spaces. It separately checks every one of the 120 possible three-edge supports for the five-point \((2,3)\) profile, identifies the four underlying support-graph types, and validates every edge and leaf of a complete depth-three adaptive mistake tree.

The unrestricted \(s\)-block statement is proved analytically by independence and dimension additivity. No exhaustive computation on all \(s\) is claimed. The finite program is a cross-check and explicit certificate, not an external or independent scientific audit.
