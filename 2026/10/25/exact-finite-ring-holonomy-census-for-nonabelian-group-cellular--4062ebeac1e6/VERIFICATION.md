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

## Checked analytically
The finite index-set permutation decomposes by internal permutation cycles. Each has exactly \(g_C=\gcd(N,V_C)\) orbits, each of length \(L_C=\ell_C N/g_C\); the return automorphism is conjugate to \(H_C^{N/g_C}\). Each power-\(t\) orbit breaks into \(\gcd(L_C,t)\) loops, and their return map is the specified power of the original monodromy. Fixed-element choices independently propagate on each loop. A fixed-count comparison at \(t=1\) proves the necessity of trivial holonomy for untwisted conjugacy; the coordinate gauges provide sufficiency. Bi-infinite index orbits exist when all \(V_C\ne0\), allowing unrestricted gauge removal.

## Direct finite checks
Run `python checker.py` with Python 3, standard library only. The checker constructs the 60-element alternating group \(A_5\), applies conjugation automorphisms, follows index arrows for every tested parameter combination, and counts all fixed group elements of the composed maps. It compares that result with the closed expression across 1,320 instances and checks the odd/even involution example for 11 ring sizes. The exact output is bundled in `checker_output.txt`.

## Limits of verification
The checks are exact finite arithmetic but are not an exhaustive enumeration of all simple groups, lattice sizes, local rules, or time powers. The universal statements rest on the proof, not on those samples. No independent mathematical audit or literature-priority audit is claimed.
