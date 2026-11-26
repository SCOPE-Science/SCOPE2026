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

Each minimum set has k+1 selected vertices and cyclic gaps ≤3; the one-unit deficit from 3(k+1) forces exactly one 2-gap. Its start determines one of the 3k+2 distinct translates. The pair {0,2} has trace multiplicities 1,k,k,k+1. For any triple appearing together, the arc carrying the 2-gap has length 2 modulo 3; any hypothesis containing its two endpoints must place its 2-gap on that arc. The third point lies in the complementary uniformly spaced arc, forcing one missing trace. The logarithmic adaptive lower bound follows from balanced splitting of the specified threshold restriction, whose modular traces were checked; the eight listed witness shifts give the fixed depth-three tree. The size of the whole class gives the upper bound, and the k=2 root-positive side has only three hypotheses, ruling out depth three. The cardinality and VC bounds give k=1 and the depth-three tree and cardinality give k=3. As a separate check, in cyclic order with step 3 the family becomes all translates of a single length-(k+1) interval. After any root query each side contains a consecutive block of k+1 hypotheses, and on each block translated intervals implement all prefix/suffix cuts, since the unused arc prevents wraparound into that block. This yields 1+floor(log2(k+1)) as a check on the weaker asserted lower bound, with a matching upper bound from the root-positive size. Independent direct domination enumeration and memoized version-space ranks for k=1,…,6 produced class sizes 5,8,11,14,17,20, all VC ranks 2, and online ranks 2,2,3,3,3,3. Replay: python3 /workspace/branches/ebf03e9c-fb18-4ff3-8432-1a49435c9dbc/independent_check.py (0.046 s for the six cases; output beside the script). The shipped script was inspected rather than executed, and C11_TREE.json matches the proof. No finite test is used to establish the infinite bounds.

## originality

PASS

The cycle domination enumeration is prior work and the static dimension is also covered by a distinct archive entry with a stronger VC support polynomial. The supported contribution is the quantitative online separation, including its first occurrence in this residue class. The closest domination/online archive hit is for all inclusion-minimal dominating sets, not the minimum-cardinality concepts. The strongest interval comparison inspected concerns unrestricted lengths or switch counts, not the fixed-length translate class. Best of available evidence; no priority claim for general thresholds, cardinality bounds, or the static enumeration.

## value

PASS

The result realizes unbounded adaptive/static separation within the full family of optimum solutions on connected vertex-transitive graphs of fixed degree two. The separation is not obtained by arbitrarily declaring a subclass of hypotheses; the graph fixes all concepts. Quantitative growth and the exact first boundary at C11 distinguish this from the generic observation that threshold classes can have a large online rank.

The dated certificate retains the supplied scientific assessment, sources and limitations.
