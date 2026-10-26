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

# Verification details

The included self-contained Python file `verify_quota.py` uses exact `fractions.Fraction` arithmetic and no random simulation. It independently computes all masses \(\Pr(T=t,L=i)\) by coefficient extraction and an absorbing-state recurrence for all positive integer weight vectors with components in \(\{1,2,3,4\}\) when \(m\in\{2,3,4\}\), or \(\{1,2,3\}\) when \(m=5\), across \(r\in\{2,3,4\}\). All 1,737 profiles agree cell by cell; all sum to one. Each unequal probability pair satisfies the strict adjacent-time likelihood-ratio determinant and both exact odds endpoints. A third exhaustive enumeration of surviving words cross-checks smaller profiles. The deterministic terminal output is embedded in `verify_quota.out`.

To reproduce, run `python3 verify_quota.py` next to the proof; compare the printed result with `verify_quota.out`. No nonstandard packages are needed. The code tests finitely many rational profiles and is not a proof for arbitrary real weights or unbounded quotas. The separate analytic argument in RESULT.md proves the general statement.

The reviewed literature encompasses the publicly available full texts of the 1998/2000 Camarri–Pitman unequal-birthday paper, the 1998/1999 Camarri multiple-repeat paper and the 2005 Aston–Martin competing-pattern paper. A plausible 1982 quota paper was available only in abstract; that priority uncertainty has not been erased.

Independent audit: not performed.
