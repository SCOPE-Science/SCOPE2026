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

# Verification of Jordan-stratum formulas

The proof is in `RESULT.md`; the following are additional reproducible finite checks, not a replacement for the proof. Execute `python3 CHECKER.py` from the extracted directory with an ordinary Python 3 interpreter. No network access or third-party packages are required.

The checker constructs the path multiplication table from the directed cycle and builds both full regular-action matrices of dimension \(3n\), rather than using the derived three-block normal form. Gaussian elimination computes \(\operatorname{rank}L_x\), \(\operatorname{rank}R_x\), \(\operatorname{rank}L_x^2\), \(\operatorname{rank}R_x^2\). These are compared elementwise against the predicted support invariants. A separate polynomial matrix-power implementation computes the two-state transfer polynomial, and all counts are compared exactly. Every radical element is enumerated in the eight listed configurations. Extension-field checks use explicit arithmetic in \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\). The checker verifies that the number of observed Jordan types is \(\binom n2+3\), that \(n-1\) length-three blocks are impossible, and that the total number of elements is \(q^{2n}\).

Expected final output: `NAKAYAMA_LOEWY3_REGULAR_JORDAN_OK 8`. Full recorded output is in `CHECKER_OUTPUT.txt`.

The finite cases do not establish the motivic identity or the all-field assertion, both of which follow from the coordinate-cell proof. They do not independently establish originality, scheme-level closures or any of the explicitly excluded extensions.
