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

Exact formula D_jk=1_{k<=j}(H_j-H_{k-1}-log(j/k))/j splits as (R_j-S_k)/j with |R_j|=O(1/j), |S_k|=O(1/k). Dyadic diagonal block compression B_m is two weighted triangular-ones matrices; s_r(L_N)<=CN/r via rank-r interval decomposition, hence s_r(B_m)<=C/(2^m r). Summing min(2^m,C/(2^m t)) gives N_B(t)=O(t^-1/2). Far rectangles m>ell separate into two rank-one matrices whose singular-value p powers are summable over all blocks for each p>0, so F is in every Schatten quasi-ideal and D=B+F has s_n(D)=O(n^-2). D is trace class; triangular diagonal j^-2 gives Tr(D^k)=ζ(2k) and sine Fredholm determinant, hence simple nonzero eigenvalues j^-2. Weyl eigenvalue/singular p-majorization excludes p<=1/2. Independent rational/finite matrix calculations corroborated decomposition and sample spectrum, but infinite counting argument is the proof.

## originality

PASS

Best-of-knowledge: Sharp transition in quasi-Banach Schatten scale for the first nontrivial discrete Mellin multiplicativity defect is natural beyond previously proved Hilbert–Schmidt/trace class. The dyadic rank-two off-block decomposition provides a reusable structural explanation and sharp weak endpoint; the known trace and immediate determinant corollary alone are not treated as independent novelty. Prior-art comparison is based on distinct theorem implications. See four structured checks and material source inspections; not exhaustive historical priority.

## value

PASS

Sharp transition in quasi-Banach Schatten scale for the first nontrivial discrete Mellin multiplicativity defect is natural beyond previously proved Hilbert–Schmidt/trace class. The dyadic rank-two off-block decomposition provides a reusable structural explanation and sharp weak endpoint; the known trace and immediate determinant corollary alone are not treated as independent novelty.

The dated certificate retains the supplied scientific assessment, sources and limitations.
