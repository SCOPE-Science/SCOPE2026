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

The proof is the all-size two-sided unfolding induction in `RESULT.md`. It establishes reconstruction from globally comparable, relation-wise colour multisets after \(n+1\) rounds for a universe of \(n\) elements, with no appeal to finite enumeration.

**Executable finite cross-check:** `python verify_two_equivalence_forests.py 8` uses the original source file included here. It enumerates every partition of the universe for the second relation and a representative of each block-size profile for the first, hence covering every pair of partitions up to relabelling. Codes are interned exactly at every refinement depth; a cryptographic digest is not used as an equality oracle. An independent union-find acyclicity check classifies incidence forests, and a canonical rooted coloured-tree representation checks forest isomorphism. Cyclic equivalence signatures are retained whether they are encountered before or after their forest comparison targets.

Results by universe size: \(n=1\): 1 configuration, 1 forest, 1 forest type; \(n=2\): 4, 3, 3; \(n=3\): 15, 9, 6; \(n=4\): 75, 35, 15; \(n=5\): 364, 140, 31; \(n=6\): 2,233, 658, 75; \(n=7\): 13,155, 3,207, 164; \(n=8\): 91,080, 17,378, 388. Every case returned zero failures. The finite check does not establish that cycles are impossible to mimic at arbitrarily large orders; that follows from the depth-growth proof in `RESULT.md`.

**Limits:** The automorphism-orbit and quantifier-rank consequences are deductive corollaries and were not independently audited. No expert or formal proof assistant certification is claimed.
