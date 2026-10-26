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

# Verification of stated mathematics

The mathematical proof has four independently inspectable parts: (1) a right-special factor at every length follows from the deterministic-suffix-state obstruction to aperiodicity; (2) complement closure gives a distinct pair, yielding \(p(n)\ge2n\); (3) complement is a weight-changing free involution on the subgroup-orbit classes when \(n\) is odd; (4) the numerical gap \(p^{\mathrm{ab}}(n)+1\le n+2\le2n\) works at every odd \(n\ge3\). The small-length sharpness check exhausts all subgroups of \(S_1\) and \(S_2\).

Execute `python3 verification.py` from these files; `verification_output.txt` records its actual result. The program checks finite factors of Thue--Morse for lengths through ten, and enumerates every subgroup of \(S_2\) and \(S_3\), including exactly two subgroup values \(2\), three values \(4\), one value \(6\) at length three. This finite check is not an infinite proof, and no equivalence or independent audit is claimed from it.

The closest published source already records a Thue--Morse parity counterexample, and the complete 2026 primary manuscript was not inspectable here; an unindexed or uninspected class-wide equivalent theorem remains a priority risk.
