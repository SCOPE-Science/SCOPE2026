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

Run `python3 verify_ps_reversal_three.py` using Python 3 without third-party packages. The script independently constructs the continuous-eating PS assignment with exact rational capacities and the lottery on serial-dictatorship orders with exact weights, comparing all matrix entries for 216 three-agent profiles and four two-agent profiles. It checks reversal symmetry of every selected lottery and pairwise decomposition envy probabilities, canonically computes all ten three-agent relabeling classes and their orbit sizes, verifies the two exceptional classes of size 36 each and total-variation distance \(1/12\), and separately checks the 12 reversal pairs of the already published four-agent obstruction. The last output line must be `ALL EXACT CHECKS PASSED`.

Exact finite enumeration proves only the enumerated two-/three-agent domain; no experiment is claimed to prove an unrestricted theorem. The four-agent negative result is prior literature. Independent scientific validation has not been performed.
