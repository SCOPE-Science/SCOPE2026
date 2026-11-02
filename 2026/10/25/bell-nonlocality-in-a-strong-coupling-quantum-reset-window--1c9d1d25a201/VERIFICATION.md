---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

PASS: Actual RESULT.md reconstructs the nine Pauli correlations from the stationary Lindblad-reset commutator system, with D=(1+R²)²+4alpha²R² and F=4alpha²+R²+4. Horodecki singular-value formula plus the two-column Ky Fan lower bound yields (CHSH/2)²>=Txy²+Tzz². At alpha>=2, R=1/(2alpha), Tzz>=9/10 and |Txy|>=256/545, whose squared sum exceeds one. The R down-to-zero correlation limit has only two singular values c and 1-c with c=1/(2(1+alpha²)), so CHSH<2; the large-R expansion gives 2-2/R²+O(R^-4)<2 for fixed alpha. Direct scaling of T gives diag limit with off-diagonal magnitude 2s/(1+4s²), uniquely maximal at s=1/2. Independently reconstructed 4x4 Hamiltonian spectral Poisson integral and checked its correlation against the exact formula at six numeric pairs, including alpha=2,3,10 at their witness rates; these finite calculations do not certify the universal quantifiers.

## originality

PASS

Best-of-knowledge comparison of the precise claim against related primary statements, algebraic implications, four named searches, and inspected published records; prior building blocks acknowledged, with explicit limitations for inaccessible full texts.

## value

PASS

PASS: Bell-CHSH activation is a stronger operational quantum-correlation property than the previously calculated concurrence. The theorem gives a uniform strict witness throughout alpha>=2 and a distinct singular strong-coupling optimum, while proving reset extremes local. This is motivated by a physical model and is not a mere algebraic normalization test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
