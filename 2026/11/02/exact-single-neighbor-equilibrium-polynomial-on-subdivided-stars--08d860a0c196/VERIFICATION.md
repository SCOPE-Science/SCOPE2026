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

Under the strict unique best response specified in the assumptions, an internal arm vertex satisfies x[j+1]=x[j−1] XOR x[j]. With hub value c and first-arm value a the arm repeats c,a,c XOR a. The leaf equation x[ℓ]=x[ℓ−1] forces a=0, a=c, or c=0 for residues 0, 1, or 2 respectively, including a one-edge arm. For c=0 only residue-two arms can activate, each with exactly 2(ℓ+1)/3 producers; the hub excludes singleton activated-arm subsets and no others. For c=1 no residue-two arm is allowed and the hub requires exactly one residue-one arm. Then the determined words and the hub contribute 2+2Σ⌊ℓᵢ/3⌋ producers in total. This exhausts labeled equilibria, including equal arm lengths or equal subset weights; setting z=1 gives the count and the nonzero criterion. An independent bitmask enumeration checked 398,160 profiles over 125 arm multisets with at most 13 vertices and degrees 3–5 (/workspace/branches/frozen_math_replay.py, argument 4); the uploaded script was inspected, not executed. Finite tests corroborate the coefficients without establishing the unbounded formula.

## originality

PASS

The result's distinct content is the all-arm-length, labeled producer-weight polynomial and its hub residue restriction, not the exact-one rule or the period-three path recurrence. Closest inspected primary results cover the local path structure or algorithms for finding one equilibrium; closest indexed results differ in graph, response, or equilibrium notion. The pass is for the bounded comparison, not proof of literature priority.

## value

PASS

The spider is a natural next tree family beyond paths, where a genuine branching constraint appears. The exact distribution by number of producers, not just feasibility or the total count, distinguishes families with repeated/unbalanced arms and shows how the hub can forbid an otherwise viable single arm or enable a uniquely hub-active profile. It provides an explicit classification without enumerating profiles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
