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

# Reproducibility

Execute `python3 verify.py` in the directory containing the accompanying script. The program computes \(x^3\bmod 3^n\) for every \(x\), builds the complete frequency distribution, and uses exact integer cyclic convolution to recover the ordered representation count for every target \(r\). It compares each value with the claimed recursive law for \(1\le n\le8\), verifies that all target counts total \(3^{2n}\), and tests \(N_n(1)=2\cdot3^n\) for \(n\ge2\).

Expected terminal line: `PASS total_target_checks=9840`.

The verifier is finite corroboration, not a proof for unrestricted \(n\). Universal correctness comes from the unit-group cube-root lemma, the nonzero derivative of the opposite-unit parameter map, and the exact scaling of the nonunit branch. No independent external audit was performed.
