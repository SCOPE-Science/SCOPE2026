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

Run `python3 verify.py` in a directory containing this file and the verifier. Standard-library Python 3 is sufficient. The script tests 641 exact rational cyclic-jump identities, including all coprime numerators through denominator 14, nonunit jump supports of every admissible size on single orbits, and selected two-orbit sums. Reported result: `PASS 641 exact rational jump-identity instances; q=2..14`.

The universal theorem is an analytic proof, not a computer-assisted exhaustion. The verifier does not independently enumerate all circle homeomorphisms, verify the literature's full historical priority, or assess independent audit status. The crucial geometric step is the explicit positive step-function integral in the proof; consistency follows from total product one. No external certificate is asserted.
