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
# Verification record

Run `python3 verify_exact.py` using Python 3 and no nonstandard packages. Every computation uses `fractions.Fraction`. The check evaluates all mass vectors with entries from \(\{1,2,3\}\) and all data vectors from \(\{0,1,2\}\) on cycles of sizes \(3,4,5\), excluding only constant data from ratios. Each case checks the stronger additive inequality and the sharp multiplicative inequality. For every mass vector it also checks all single-site indicators against the exact mass-dependent delta ratio. The script printed: `PASS: 65286 nonconstant exact-rational profiles; 1620 exact delta ratios.`

These tests are finite implementation checks only. The universal proof is analytic and appears in `RESULT.md`: high-superlevel component inclusion, cycle-boundary coarea, mass lower bound, and atomic equality. There is no claim of an external certificate or independent validation. No result is asserted outside the stated cycle and mass scope.
