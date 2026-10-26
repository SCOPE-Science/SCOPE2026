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

# Verification record

The proof establishes the full claim for every finite candidate set at committee size \(2\). The necessary reduction is to two disjoint committees, hence four distinguished candidates; the complete six-row total-swap table and four direct signed-swap arguments exclude all profiles with fewer than five voters. The integer-count contradiction eliminates the only other possible five-voter strict-improvement type; the remaining pattern is unique up to two within-pair candidate permutations. The exhibited profile attains all required inequalities.

Run `python VERIFY.py` in the same directory. It uses exact doubled harmonic scores \((0,2,3)\) and enumerates every Pareto-compatible ballot multiset on the four distinguished candidates for \(1\) through \(5\) voters. Expected successful output: `Counts for voter numbers 1..5: {1: 0, 2: 0, 3: 0, 4: 0, 5: 2}`; two labeled instances are one orbit. The program also checks the six-row table, both committee scores, and the four swap differences. This finite census corroborates but does not substitute for the proof across arbitrary numbers of candidates. No separate independent review or proof-assistant certificate has been performed.
