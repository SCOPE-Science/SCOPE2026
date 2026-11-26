---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For the unit-rate directed cycle the geometric resolvent and the squared resolvent group powers modulo n; summing (j+kn+1)s^(kn) gives the stated c_(n,j). A_n,B_n>0 for h>0, so the displayed integer numerators preserve signs. The Taylor coefficient of Q^k is 2(k+1)/2^k−1; k=3 vanishes and k=4 gives −3/8. The displacement four is distinct from all earlier powers for n≥5. Q annihilates the all-ones vector and E_n(0)=I_n. Independently replayed the exact certificate using integer polynomials and signed rational Sturm division; see evidence/4/replay_exact.py and evidence/4/replay_exact.log. Every numerator for n=2–4 has nonnegative coefficients and is nonzero. The diagonal numerators begin positive and have zero positive roots for n=2–13, and exactly two at n=14, with Sturm variations (19,17). Exact evaluation gives a strictly negative diagonal at h=6 for n=14–16; for n≥17 the verified base inequality 7(n+1)(3/4)^n < (1−(3/4)^n)^2 persists because its left side decreases and its right side increases, proving the strict sign for the infinite tail. For n=14, off-diagonal indices 1–3 are positive; 4–12 have exactly one positive root below 3; and index 13 has exactly one root α∈(3,4). The diagonal roots are β∈(5,6) and γ∈(6,9), with signs +,−,+. The intersection is {0}∪[α,β]∪[γ,∞), including all endpoints; exact rational bisection corroborates the printed decimals. Strict positivity at positive h for small n does not include h=0. The supplied verifier was inspected, not executed; no proof-assistant or n≥15 complete timestep classification is claimed.

## originality

PASS

Pass for the distinct minimum diagonal-failure dimension, the uniform h=6 witness, and the complete fourteen-state nonnegative-step set. The later 2026/11/8 Resultary record independently exhibits exact statement overlap for items 1–2 and the general cyclic kernel; those are not distinct content relative to that entry. Its different n=5 classification does not cover the new diagonal and n=14 sign assertions. The displayed chronology is not used to establish independent discovery or historical priority.

## value

PASS

The first negative diagonal is a meaningful departure from earlier off-diagonal small-step loss, and classification exactly at its onset shows two disjoint nontrivial safe ranges separated by genuine sign failure, despite exact mass conservation. The cycle is a canonical test family for distinguishing Markov positivity from scalar stability. The result is not merely a sign sample or a numerical choice of timestep.

The dated certificate retains the supplied scientific assessment, sources and limitations.
