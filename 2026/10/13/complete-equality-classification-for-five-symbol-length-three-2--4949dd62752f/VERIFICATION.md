---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For five symbols and exactly seven length-three words, rederived the IPP1 triple condition (35 label triples) and IPP2 disjoint-pair condition (105 pairings), from the primary theorem. A fresh independent partition search over all 855 partitions of seven labels into at most five blocks found exactly 210 coordinate-unordered valid triples; Hamming graph signatures split them 105/105 into distinct classes with nine vs seven distance-two pairs, and the displayed two representatives occur. Each class has 105 distinct labeled equality triples and stabilizer 48; assigning five symbols per coordinate and three coordinate orders gives 210*6*(5!)^3/7!=432000 literal maximum codes, 216000 each class. Primary Tô–Safavi-Naini Theorem 34 gives the separate upper bound F(3,5)=7. Complete finite enumeration is exhaustive, not a probabilistic sample.

## originality

PASS

Best-of-knowledge: known optimum seven is not original; exhaustive classification into two distinct exact equality classes, 432000 literal codes and stabilizer 48 was not present in inspected direct full text or returned nearby semantic corpus. The original source studies a partial-order-minimal maximum graph, which cannot imply all equality types.

## value

PASS

The five-symbol seven-word optimum is a natural tight fingerprinting bound, and distinguishing both algebraically different equality graphs identifies every optimal code structure and symmetries. Equality cases are not supplied by the known size theorem and can inform exact code search and extremal construction; finite classification is intrinsically relevant rather than arbitrary numerical slicing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
