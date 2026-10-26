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

The accompanying `verify_mobius.py` uses exact `fractions.Fraction` arithmetic. For each \(3\le n\le13\) it constructs the \(2n\)-vertex, \(3n\)-edge incidence matrix and grounded Laplacian, inverts that Laplacian exactly, reconstructs every cut-projection column, checks projector symmetry and \(\|Qe_j\|_2^2=Q_{jj}\), and compares both edge-orbit cut and cycle column sums with the positive-part formulas obtained from an independently solved rational recurrence. The test covers \(\sum_{n=3}^{13}3n=264\) exact columns and passed. It also checks strict rim dominance for \(n\ge4\) and orbit equality at \(n=3\).

The source file is the complete standalone test, with no data files or third-party dependencies. Run `python verify_mobius.py` from the directory containing the extracted source file.

This finite reconstruction does not certify an asymptotic theorem or all graph orders. The mathematical proof uses an explicit antiperiodic Green kernel, exact current signs, a closed-form pairwise absolute-value identity, inequalities for the two edge orbits, and a cutoff asymptotic. No external audit or independent validation has been performed.
