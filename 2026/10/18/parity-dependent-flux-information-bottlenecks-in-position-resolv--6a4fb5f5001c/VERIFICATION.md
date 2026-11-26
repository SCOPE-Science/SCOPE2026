---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The replacement retains the theorem and fixes the odd-ring remainder argument. The frozen proof's exact p_±=A(x)±B(x,φ) formula incorrectly makes the average flux independent; even winding harmonics are allowed there (already for n=3, the farthest-site cos(2φ) coefficient begins at −x^6/40). In the replacement, complex conjugation and reflection instead give p_j(φ,−t)=p_{−j}(φ,t) and the same exchange for flux derivatives. Each farthest-site FI quotient extends analytically at t=0 after factoring its x^{2r} denominator; the sum is even, so the order-2r+3 Taylor term vanishes. The winding phase (−i)^{nℓ} establishes the all-time blind sets. Shortest-path interference yields the stated coefficients, with all nearer-site terms bounded using |q|+|q'|≥n for distinct windings. The leading constants prove the converse at fixed nonexceptional flux. Commutation gives the QFI as 4t² times the variance of ∂φH in the input; the two distinct one-hop sites give variance 2J²/n² even for n=3. The repaired analysis applies to the pointwise ordinary score and not to limiting information at support zeros.

## originality

PASS

Best-of-knowledge pass for the joint all-time ordinary position-blindness classification and sharp short-time position information law. Neither the winding technique nor the standalone commuting-generator QFI formula is claimed independently novel. The repaired symmetry proof does not change the observation model or conclusion. Luppi is the closest verified literature overlap and provides an earlier return-only parity law, not these resolved-site statements.

## value

PASS

Resolved positions are a natural experimentally accessible readout. The exact blind fluxes and coefficient-bearing latency penalty distinguish that readout from rooted returns and from fixed-encoding QFI. The opposite parity powers and their farthest-site carriers quantify which outcomes matter before long-time dynamics, while the support-zero caution avoids claiming that first-order blindness prevents all inference.

The dated certificate retains the supplied scientific assessment, sources and limitations.
