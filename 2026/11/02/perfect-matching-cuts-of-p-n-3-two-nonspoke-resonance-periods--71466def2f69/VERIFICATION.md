---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For each n>=7 the cubic graph GP(n,3) has a perfect-matching cut iff a binary shore coloring has exactly one opposite-color neighbor at each vertex. Its outer bits a_i determine b_i uniquely by the 3-bit local rule; forbidden isolated outer bits have no extension. The inner condition is a check on nine outer bits, hence a length-n closed walk in the 8-bit de Bruijn overlap digraph. I reconstructed all 512 candidate nine-bit tests and confirmed precisely 90 arcs. Repeated in/out pruning retains exactly 42,20,16 states, with the final induced graph consisting solely of loops (0),(255), a 4-cycle (51,153,204,102), and two 5-cycles (24,140,198,99,49), (57,156,206,231,115). Each closed walk is a labeled cyclic outer coloring for any n, even when the nine-bit window wraps repeatedly; the inner bits are unique. Thus 2+4[4|n]+10[5|n] colorings, quotient by fixed-point-free global complement gives 1+2[4|n]+5[5|n] cuts. Direct independent enumeration of 2^(n-1) normalized outer colorings for n=7..11 returned counts (1,3,1,6,1) and exact crossing-spoke strata (n), (n and 0), (n), (n and n/5), (n). Finite samples corroborate, whereas the exhaustive state certificate and closed-walk bijection prove the universal claim.

## originality

PASS

The object is exactly a perfect two-coloring with neighbor-quotient matrix [[2,1],[1,2]] on cubic GP(n,3), not merely an analogous matching problem. Karami (2022) explicitly treats GP(n,3) perfect 2-coloring parameter matrices, including this A1 feasibility; hence generic existence must NOT be claimed as new. The assessed full number of edge-set cuts and primitive 4-,5-period/spoke spectrum are not displayed in the inspected published parameter-matrix classification. Le--Telle and Bonnet et al. formulate the same cut constraint but prove broad complexity/hardness, not this all-n enumeration. Resultary nearest named Petersen entries concern cut/matching complexes, not exact perfect-matching-cut counts. Originality PASS is qualified by possible further color-multiplicity tables in unindexed work.

## value

PASS

Perfect matching cuts partition a cubic graph into two induced 2-regular sides and are nontrivial to recognize generally. For the canonical GP(n,3) family, exact edge-set counts and a sharp classification of nonspoke periodic resonances at mod 4 and mod 5 are intrinsic extremal enumeration facts. The distinction between existence (known) and a full number/spoke distribution (claimed here) is mathematically substantive; this is neither a reformulation nor an arbitrary selected numeric instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
