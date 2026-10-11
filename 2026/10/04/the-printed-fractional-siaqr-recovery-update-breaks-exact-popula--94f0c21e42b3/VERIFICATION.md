---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Adding the five printed continuous Caputo SIAQR fields cancels exactly, so total population is conserved. Equation (5.22) uses the recovered state R in its first g5 history term but the quarantine state Q in the two higher g5 differences, destroying the componentwise cancellation. For the exact invariant submodel I=A=Q=0, N=1, delta=omega=1/2 and gamma=1/2, R(t)=exp(t) erfc(sqrt(t)). An independent 50-digit replay gives the first fully affected m=2 population defect -0.492078936843788976989587439259416..., matching the inspected verifier. Replacing the two Q histories by the corresponding R histories restores exact cancellation.

## originality

PASS

The primary article contains the continuous closed SIAQR system and the printed component recurrences, but targeted source, correction and Resultary searches located no published notice of the Q-for-R substitution or its conservation defect. Earlier SIAQR work concerns a different stochastic-delay model, while generic Newton-polynomial Caputo expositions keep the same scalar component function throughout its history interpolation. Neither prior line implies the explicit source-specific 49.2 percent population loss.

## value

PASS

Population conservation is a defining structural constraint of the closed model, and the printed update loses about 49.2 percent of total population on a simple exact admissible history. The finding therefore supplies a strong reproducibility diagnostic and a precise minimal repair, well beyond a cosmetic notation observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
