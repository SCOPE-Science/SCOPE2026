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
# Reproduction

Run `python3 verify.py` without additional packages. It directly counts scattered subsequences of lengths zero, one and two and compares those counts with the one-count/first-moment signature on every binary word through length eight. It generates the Thue–Morse prefix both by the defining morphism and by binary digit parity, verifies explicit even-root constructions, and searches for forbidden odd roots and tests the exact length-one/three location criteria.

Observed finite results: every even root from \(2\) to \(512\) has an explicitly verified witness; all odd root lengths from \(5\) through \(259\) are absent from the first \(32768\) letters; the two odd-root criteria match at \(6000\) source positions each. The empirical root-three frequency is \(2730/32763\), approaching the proved \(1/12\).

These calculations are finite cross-checks only. The unrestricted theorem uses the complementary-pair structure, exact moment equations and constructive binary digit identities; density uses primitive-substitution frequency existence and exact fixed-point equations. Historical priority and independent validation have not been established.
