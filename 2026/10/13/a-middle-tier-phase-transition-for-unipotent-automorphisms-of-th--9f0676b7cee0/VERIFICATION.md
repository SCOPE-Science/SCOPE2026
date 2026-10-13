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

# Reproducibility and verification

The proof is symbolic for every \(a,b\ge2\) and \(c\ge1\). The finite exact-arithmetic regression script `check_chain_roots.py` constructs all primitive coordinate rays and maximal-chain rays, enumerates the integer box \(\{-1,0,1\}^{a+b+c}\) for eleven triples, and compares the resulting root sets to the theorem. It separately computes the nonzero Lie root brackets and their lower central series. Run `python3 check_chain_roots.py`; the expected console text is in `check_output.txt`. Both artifacts are included.

The eleven cases comprise six with one middle element and five with two or three middle elements, totaling \(30{,}861\) tested vectors. Bounded enumeration is a check of the exact formula, not an exhaustive computation of every character in the infinite lattice. Exhaustiveness is furnished by the facet-inequality proof in RESULT.md. Group classification also uses the standard Demazure theorem on complete toric automorphisms.

Self-review: passed. Independent audit: not yet performed.
