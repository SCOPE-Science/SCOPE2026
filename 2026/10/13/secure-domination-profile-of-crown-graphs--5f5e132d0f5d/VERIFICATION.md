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
The theorem was checked with `verify_secure_crown.py`. The program constructs \(\operatorname{Cr}_n\) directly, enumerates every vertex subset for \(3\le n\le8\), tests the secure-domination definition by trying every legal defender swap, and compares the result with the closed state predicate \(\Phi_A\wedge\Phi_B\).

It separately reconstructs the bivariate coefficient table from the multinomial sum over admissible \((a,b,c,d)\) and checks every coefficient against brute-force enumeration. It also checks the minimum-size and minimum-count formulas, including the \(n=3\) and \(n=4\) boundary cases and the closed \(n\ge5\) count.

Finite enumeration is not used as a proof for arbitrary \(n\). The general proof is the case analysis in `RESULT.md`; the computation is a boundary and implementation check. The 2016 same-object secure-restrained source was not fully accessible in this run, so originality retains that stated literature-access risk.
