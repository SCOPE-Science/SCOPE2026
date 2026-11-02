---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Encode each multiplicity s by nested binary indicators (1_{s>=1},1_{s=2}), so min intersection parity equals binary inner product; for k valid vectors RR^T=I_k. The strict k<2n follows from U_i dot V_i = V_i dot V_i, contradicting both columns being orthonormal in a square inverse. For k=2n-1, nondegenerate row subspace complement has z dot z=1 and projection R^TR=I+zz^T; the same nested column condition forces z=(0^n,1^n), hence n odd. Thus even n max 2n-2. Explicit families of 6 (n=4) and 10 (n=6) independently verified pairwise. For n<=5 independently enumerate ALL maximal cliques in the complete compatibility graph on eligible odd-parity vectors; counts 1,2,14,266,21574 and maxima 1,2,3,6,7. n=6 exact from bound+witness. Disjoint-coordinate union gives 10q+b_r. Finite exhaustive enumeration is only for n<=5, not infinite.

## originality

PASS

Banerjee and Dewan introduce precisely this bounded multiset minimum-intersection definition but their main theorem solves Eventown (even diagonal), not the odd-diagonal family. Standard binary Oddtown on the nested 2n layers only yields 2n, not the stronger even-n correction. Set modulo composite integer and lattice-path Oddtown results have different objects. No matching original 2-bounded Oddtown rank improvement and n=4,5,6 extrema found in targeted published searches. Best-of-knowledge PASS with possible unindexed older coding equivalence.

## value

PASS

This is the smallest nontrivial multiplicity extension of Oddtown and asks a natural parity-extremal question left by bounded-multiset Eventown. The even-n codimension-one obstruction is genuinely structural; explicit first counterexample n=4, sharp n=6, and amplification to super-unit density 5/3 give meaningful boundary and asymptotic information, not an arbitrary small table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
