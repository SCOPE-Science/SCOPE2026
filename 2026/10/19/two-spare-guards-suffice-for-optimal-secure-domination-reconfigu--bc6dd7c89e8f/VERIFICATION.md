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

# Finite computational verification

The certificate fixes the lexicographic order of ten two-subsets followed by ten three-subsets of the point set \([5]\). It contains all 155 minimum secure dominating masks, all 750 two-exchange pairs, explicit automorphism-orbit representatives, a 154-edge spanning tree, and a disjoint pair witnessing the lower bound on move count. No data are sampled.

Reproduce from the extracted directory:

```sh
python3 checks/verify_incidence.py checks/certificate.json > incidence-replay.out
diff -u checks/verify_incidence.output.txt incidence-replay.out
c++ -O2 -std=c++17 checks/verify_petersen.cpp -o verify_petersen
./verify_petersen > petersen-replay.out
diff -u checks/verify_petersen.output.txt petersen-replay.out
python3 checks/crosscheck.py checks/certificate.json petersen-replay.out
```

The first checker constructs the two/three-subset incidence graph, exhausts all \(\binom{20}{k}\) masks for \(0\le k\le8\), checks the 240 explicit automorphisms and the entire 155-state exchange graph, and matches the complete certificate exactly. The second checker constructs \(P(10,3)\), exhausts all subsets of size at most eight from scratch using a separately coded secure predicate, validates an explicit graph isomorphism, and computes all exchange distances independently. The cross-check verifies that the 155 resulting minimum masks coincide exactly after transporting along the isomorphism.

The original run produced exact outputs in the two included output files. Replaying from the embedded source is necessary if stronger assurance is desired. The finite checks establish only the asserted results for this fixed 20-vertex graph. Neither these files nor their execution provide an external independent scientific audit.
