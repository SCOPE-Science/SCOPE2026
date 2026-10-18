---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For crown graph Cr_n=K_{n,n}-M_n (n>=3), at any stage each a_r has |J|-1_{r in J} white neighbors and b_r has |I|-1_{r in I}. If |I|>2 or |J|>2 the corresponding side cannot shrink, so a set skew zero-forces iff both white-index sets have size<=2. Sufficiency uses white forcers across missing diagonal to clear an opposite side, then the other. Hence all-set polynomial [x^n+n x^(n-1)+C(n,2)x^(n-2)]^2, Z^-=2n-4, minimum coefficient C(n,2)^2. Ordinary forcing excludes exactly sets I=J of size2; precisely C(n,2) additional skew sets at minimum degree. Independently simulated all 2^(2n) initial blue subsets for n=3,4,5,6, including ordinary process and every predicted coefficient. This is a symbolic all-n proof, finite tests corroborative only.

## originality

PASS

DeAlba 2014 establishes skew forcing definitions, general matching/graph results and potential scalar minimum, and Boyer et al. 2018 introduce the ordinary zero-forcing polynomial. Resultary hits for all skew forcing sets of chain graphs do not dominate: a crown graph for n>=3 is not a chain graph (has induced 2K2). The exact crown all-cardinality skew enumerator and one-coefficient difference against ordinary forcing are not obtained from the inspected primary statements; scalar Z^- itself is not claimed separately novel.

## value

PASS

An exact polynomial counting every skew zero-forcing initial set, not just minimum cardinality, is a natural graph-control invariant. The surprising one-coefficient mismatch against ordinary zero forcing isolates precisely the effect of permitting white vertices to force, and supplies an infinite-family combinatorial classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
