---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For B=I-G*G positive with ||G||=1, the estimate epsilon||Q_epsilon x||²≤1-||Gx||²<2delta-delta² for near-norming x shows p_G(Q_epsilon)=0. Under universal p_G=essential, each Q_epsilon is compact and hence finite rank; B=norm-lim BQ_epsilon compact. Any kernel unit x gives a rank-one projection R_x with p_G(R_x)=1 but essential norm zero, contradiction. Conversely, if B is compact injective, Q_epsilon finite rank and P_epsilon=I-Q_epsilon strongly tends to zero; two-sided near-norming estimates show p_G(T)=lim||TP_epsilon||. Finite-rank TQ_epsilon gives the lower bound essential≤limit, and compact K times P_epsilon tends to zero in norm, giving the upper bound. Injective compact operator has separable dense image, so only separable H possible; diagonal compact positive B and G=(I-B)^1/2 supply examples. All real/complex infinite-dimensional H, all bounded T; equality for only one T is not asserted.

## originality

PASS

Compared the SAME relative G-seminorm in Kadets et al (universal equality to the full norm) and Dey–Pal (norm attainment and seminorm comparisons). Their statements do not identify the essential norm for every T; for finite-rank T, full and essential differ. The present iff compact injective defect is not covered on inspected evidence. A 2025 operator-essential-norm text was only abstract-accessible and remains a documented overlap risk.

## value

PASS

Exact universal operator-ideal identification gives a geometrically defined seminorm the Calkin quotient norm, complete spectral iff conditions, a compact-kernel characterization and separability obstruction. This is structural and reusable in operator theory, not merely an instance of the compact tail norm formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
