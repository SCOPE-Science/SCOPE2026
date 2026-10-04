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
# Verification

The mathematical proof is symbolic and valid for every integer \(n\ge3\). The critical deductions are:

1. Reduced strict reversal implies \(r_{i+1}-r_i\ge1\).
2. Full strict order implies \(w_i-w_{i+1}\ge1\).
3. Since \(w_i=r_i+q_i\), these imply \(q_i-q_{i+1}\ge2\), hence \(q_i\ge2(n-1-i)\).
4. Summing the forced victory counts gives \(M\ge3\binom{n-1}{2}\), while summing the \(q_i\) gives at least \((n-1)(n-2)\) matches involving the deleted player.
5. The explicit construction has \(r_i=i-1\) and \(q_i=2(n-1-i)\), so every lower bound is attained; the \(n=3\) maximum-load case is checked separately in the proof.

`verify.py` reconstructs this family for \(3\le n\le100\) and checks the exact rankings, total matches, and maximum match load. A successful replay prints `VERIFY_OK`.

The finite replay is not an exhaustive search over all tournaments and is not used to infer the all-\(n\) lower bounds. No claim is made about uniqueness of equality cases or about ranking methods other than the stated Borda rule.
