---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For the 4-site open XX Lindblad chain with coherent hopping normalised J=1, uniform tilt U and boundary coupling G, the source reconstructs the exact stationary Pauli-string 16-equation reduction giving R=1/j=(16+G²+6Gg)/(16G)+z P/(8Q), z=U² and positive Q. I independently re-expanded the displayed P,Q with exact symbolic polynomial algebra. W1=P Q_g-P_g Q contains precisely 85 positive nonzero integer monomials and W2=P_gg Q²-P Q_gg Q-2 P_g Q_g Q+2P(Q_g)² exactly 224, all positive (smallest coeffs 1 and 2), so R_g has strictly increasing derivative for U>0. Exact expansion verifies R_g(0)=-G² Φ_G(z)/(8Q0²). Every nonconstant z coefficient of Φ is positive and its constant is negative, giving unique positive threshold z_c. With R_g→3/8 as g→∞, strict convexity yields the complete global optimizer trichotomy including equality at U_c. Dominant balance gives U_c~√(3/140)G as G→0, U_c~8√3/G as G→∞, and at G=1 independent unique-root evaluation U_c=0.148539003114375. At U=0 resistance is linear, and no strict convexity is claimed there. The finite coefficient certificate alone does not validate the quantum 16-equation premise; the published model/closure and source construction were also inspected.

## originality

PASS

Jacob et al. 2407.21715 provide the same Lindblad model and exact length-2/3 currents, while their longer-chain treatment is an approximation. The length-4 exact full-coherence resistance, positive-coefficient convexity certificate and all-boundary-coupling threshold are not stated in the inspected full primary text. Disordered chains exhibit different dephasing response; no claim that all long or disordered chains are unimodal. Possible other exact four-site diagonalizations remain a residual risk.

## value

PASS

Whether adding local dephasing improves steady current is a physical design question. A rigorous exact threshold separating no-enhancement from unique optimal nonzero dephasing for all G>0, and its nonmonotone coupling limits, is a meaningful sharp small-chain spectral-transport result rather than a table or numerical crossover.

The dated certificate retains the supplied scientific assessment, sources and limitations.
