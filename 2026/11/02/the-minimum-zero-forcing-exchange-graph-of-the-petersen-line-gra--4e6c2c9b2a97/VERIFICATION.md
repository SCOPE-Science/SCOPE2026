---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Using vertices of Petersen graph as disjoint 2-subsets of five labels, its 15 edges are vertices of the degree-4 line graph. A 15-bit mask is zero-forcing exactly when iterative unique-white-neighbor closure is all ones; parallel eligible forces cannot inhibit success, so exhaustive closure is complete. Independent independently coded enumeration of all 2^15 masks found minimum size seven, exactly 2280 minimum sets, and under one-token exchange 28650 edges. All S5 relabelings give 21 orbits, 17 of size120 and four of size60. BFS weighted by those orbit sizes yields eccentricities 600 at 6 and 1680 at 7, radius6 diameter7, degree spectrum 22:180,23:480,24:240,25:240,26:660,27:240,28:60,29:180, and unordered distance counts 28650,234120,765570,1004640,483480,78540,3060 for distances1..7. Comparison to Hamming/Johnson lower bound |A\B| gives only 18540 detour pairs (3180 at h2,11640 at h3,3720 at h4) and d in {h,h+1}. Inspected pinned verify_kneser.py provides complete 32768 mask and 21-orbit exact BFS certificate; a separate alternative Petersen representation verify_classical.py is supplied. This precisely fixed finite result is supported by exhaustive combinatorial search, not extrapolation.

## originality

PASS

Fallat–Soltani already prove the minimum Z(L(P))=7 for line graphs of traceable G; only the 2280-state orbit/degree/distance and Johnson detour distribution is evaluated here. Geneson–Haas–Hogben introduced these reconfiguration graphs and studied general examples, but their full paper includes no Petersen case or this line graph. Search of published results/databases yielded no matching exact metric table; best-of-knowledge PASS with possible unindexed computation.

## value

PASS

An exact natural configuration-space census for the line graph of a canonical nonhamiltonian graph, including a near-isometric Johnson embedding with a classified one-step defect, is a substantive finite structural invariant rather than a routine restatement of the already-known minimum forcing number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
