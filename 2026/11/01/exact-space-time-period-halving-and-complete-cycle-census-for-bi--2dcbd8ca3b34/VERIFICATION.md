---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For n=2^m>=4 over F2 and nearest-neighbor C=S+S^{-1}, factor M=L^2 with L=[[0,I],[I,C]] invertible, M-I=D L=L D, D=diag(C,C) commuting. In characteristic two, M^{2^j}-I=(M-I)^{2^j}, and C^{2^j}=S^{-2^j}(S^{2^{j+1}}+I), giving the all-j equality of fixed subspaces Fix(M^{2^j})=Fix(S^{2^{j+1}} on both q,p). Because (S+I)^n=0 when n is a power of two, M is unipotent, and odd factors of t do not change fixed subspaces. Thus each state has temporal period max(1,d/2), where d is its common spatial period. The fixed-state counts 2^{2 min(n,2^{j+1})}, 16 fixed states, primitive E_j difference, and maximal map order n/2 follow exactly. Independent exhaustive direct bit-level evolution over all 256 n=4 and 65536 n=8 states confirmed the statewise identity and censuses. Finite checks complement, not replace, the universal algebraic proof.

## originality

PASS

Prior coupled-cat-map papers supply the matrices and order algorithms but not the all-state equality between temporal and spatial periods for dyadic binary nearest-neighbor rings. A published Resultary all-to-all cat-map order law has a different graph and only full permutation order. Specialized linear cellular automata literature remains a live alias priority risk.

## value

PASS

The precise relation between spatial and temporal periods is a natural structural invariant of reversible finite lattice dynamics, and it determines every orbit length and number for an unbounded family of ring sizes. The dyadic binary choice is forced by nilpotent shift algebra, not a decorative parameter slice. The all-state census is materially stronger than a mere matrix order calculation and mathematically motivated by periodic-orbit studies of coupled cat maps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
