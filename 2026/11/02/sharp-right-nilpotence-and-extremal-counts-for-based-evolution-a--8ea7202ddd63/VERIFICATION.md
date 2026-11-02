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

The included executable `verify.py` directly creates finite-chain-ring evolution algebra products, iterates right-power generators, and exhaustively tests every structure matrix in the ten documented configurations. It does not use the path valuation formula to determine the right nilindex. Candidate nil tables are identified separately through the acyclicity condition proved in the accompanying result, and within those tables all indices are directly computed. The code checks the full tally of nil tables and of maximum-index tables against the formulas. Nine rings are of the form \(\mathbb Z/p^s\); the tenth is the extension-field dual-number ring \(\mathbb F_4[\varepsilon]/(\varepsilon^2)\). Its residue multiplication is explicitly defined by the irreducible polynomial \(t^2+t+1\). Outputs and pass markers are in `verification_output.txt`.

The mathematics additionally verifies edge cases \(n=1\) and \(s=1\) without taking undefined negative ring powers. Tests are finite and do not establish the universal result independently. The formal proof depends on the field nilness/triangularity theorem cited in the result; the other steps are explicit. No independent audit has occurred.
