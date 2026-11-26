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

Independently, for a retraction with image J and kernel K, H_q=JK and J∩K=1. If K is contained in the center Z, J surjects onto H_q/Z and its commutators fill Z; hence Z⊆J and K=1, giving the identity. Otherwise K contains a noncentral element, whose commutators with H_q fill Z, so Z⊆K. Then J is abelian, is disjoint from Z, and projects to an F_p-subspace U with zero determinant pairing; any nonzero vector in U forces all of U into its unique F_q-line. In the stated odd-characteristic coordinates a lift is a linear graph, and for each lift the retractions are exactly compositions of projection modulo Z and an F_p-linear projection onto U with that graph embedding. Each U has p^(er) lifts and p^[r(2e−r)] complementary subspaces; the unique containing line gives (q+1)[e choose r]_p choices of U. A nontrivial such graph cannot be normal since commutators of one noncentral element fill Z. For s=e−r, the Gaussian binomial contributes p^[s(e−s)] and the normalized projection-and-graph factor contributes p^[−es−s²], giving p^(−2s²) times the displayed product ratio. The product denominator has a strictly positive infinite limit, giving summable domination and the normalized defect law. This verifies all ranks, including the two exceptional maps and fixed-p limit. VERIFICATION.md and verify.py report prime-field calibration and a projection census plus sampled group identities over F_9, not exhaustion of all extension-field maps; no replay is necessary for the independent analytic proof. For example the formulas give 40 possible rank-one U and 10 rank-two U at q=9, leading to 9720 and 65610 retractions, respectively.

## originality

PASS

The in-scope result is the census of group idempotents, not F_q-linear Lie idempotents, and the defect law as the extension degree grows at fixed characteristic. The prime-field calibration and the general projection-counting technique are not credited as new. The closest inspected literature and indexed findings do not give the in-scope result or a stronger theorem implying it directly.

## value

PASS

This is a complete census of the split quotients of a natural nonextraspecial finite p-group family, distinguishing subgroups from maps realizing them and proving the absence of normal proper retracts. The rank law quantifies how uniform splitting idempotents behave when extension degree rather than prime grows; the bounded but nondegenerate rank defect is useful information not supplied by just the leading total count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
