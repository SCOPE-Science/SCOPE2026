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

The proof uses exact combinatorial descriptions, the published integral homology/connectivity theorems of Caputi--Collari--Smith, and Hurewicz plus Whitehead. The new top-cycle structural lemma has no unverified numerical prerequisites. The supplied `verify.py` independently enumerates finite multipath faces and checks the top facet characterization and an acyclic lexicographic discrete-Morse matching on \(n+1=7,8,9,10,11,12,13,14\) vertices. Its real terminal output is provided in `verification_output.txt`. The finite checks are supplementary; no infinite range is certified by enumeration.

The two embedded pure-orientation \(S^{n-1}\) subcomplexes contain all top facets, and have disjoint integral boundary supports. For \(n\ge6\), published connectivity is at least one and the Hurewicz argument realizes the lower classes; hence Whitehead applies to the wedge map.

Scientific limitations: reliance on the published general homology/connectivity calculations, no equivariance, no independent external audit, and potential unindexed bibliographic overlap.
