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

For fixed reference R and nonempty target s, a joined-history optimal first phrase cannot cross R/target join because target history initially empty. Every later joined-history phrase has source entirely in R or decoded prefix, or crosses the boundary once and splits into at most two legal source phrases; hence P<=A<=2P-1. Greedy longest-available-match optimality follows from a suffix-of-existing-source exchange that preserves decoded source availability. With pairwise distinct letters R=a1...am, recursively T1=R, Tj=Tj-1(a_j...a_m)Tj-1, the joined parse takes one phrase per stage; unique new a_m a_(j-1) backward adjacency forces two longest split-source phrases at each later stage, so P=m, A=2m-1, length (m-1)2^m+1. Independently recomputed exact dynamic-programming optimum for m=1,...,5: (P,A)=(1,1),(2,3),(3,5),(4,7),(5,9). Proof, not finite search, covers every m.

## originality

PASS

Marteau, arXiv:2610.26021, defines exactly the split-versus-preset-history comparison, proves weaker A<=2P (Theorem IV.10) and in Remark IV.11 explicitly states factor-two attainability unknown with finite binary search maximum 5/3. Its greedy exchange theorem is preexisting. The additional additive -1 bound and exact extremizing recursive family for every P=m answer the stated sharpness question. Kosolobov–Shur compare different LZ overlap/encoding variants with superficially similar integer bounds, not identical source boundary.

## value

PASS

Settles explicitly open finite sharpness question for a natural two-source compression model: every optimal joined-phrase count has exact maximal separated-source cost 2m-1, with factor two a strict unattained supremum. The bound is sharper than a numerical table and informs nonoverlap dictionary design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
