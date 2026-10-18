---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For each d>=2 take |Phi_d>=d^{-1/2}sum_j|jj>. The normalized Choi state of any unitary U is the rank-one projector onto (I⊗U)|Phi_d>, hence every such channel has eigenvalues (1,0,...,0), independent of U. The target-relative entanglement fidelity equals |Tr(U)|^2/d^2; the Haar-average identity F_avg=(d F_e+1)/(d+1) therefore yields F_avg(U)=(|Tr U|^2+d)/(d(d+1)). U=I gives 1; U=diag(1,omega,...,omega^{d-1}) with omega=e^{2πi/d} gives 1/(d+1). Source Appendix B.4 instead uses (d+sum λ_i²)/(d(d+1)), producing 1/d with normalized pure Choi and producing 1 with the unnormalized Choi spectrum (d,0,...), so neither convention rescues the formula. This is a universal algebraic contradiction, not an inference from dimensions 2–12. Verified actual appendix and its separate correct identity in main section and pseudocode.

## originality

PASS

The Horodecki/Nielsen fidelity theorem and distinction between overlap and purity are classical, not original. The remaining specific claim diagnoses the incorrect Appendix B.4 expression of a paper released in 2026, under both Choi normalizations. The anchor paper itself states the correct overlap identity in Section 7.4/pseudocode but does not flag or reconcile its appendix; no full-text earlier published diagnosis of this precise discrepancy was found in targeted Resultary and external searches. A source-specific criticism is not a new gate-fidelity theorem, and the possibility of independent corrections remains.

## value

PASS

The appendix misidentifies target-relative fidelity as spectral purity, yielding a wrong performance score even for the identity operation under one normalization and declaring all unitary coherent errors perfect under the other. This would materially mislead process-tomographic characterization; the two contradictory cases pinpoint exactly why diagonalizing the Choi state loses the target overlap. Value is limited to the localized correction, not to the elementary classical fidelity formula, and does not presume that the paper’s numerical tables used the incorrect expression.

The dated certificate retains the supplied scientific assessment, sources and limitations.
