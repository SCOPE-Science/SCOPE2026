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

PASS. For p>=q>=3, deleting two edges leaves connected K_pq; Laplacian eigenspaces for the two parts and their contrast yield explicit r,k,c,d. Rank-two Woodbury inversion on the constant-orthogonal subspace gives Delta=2(p+q)[k(1-r)+cd]/[(1-r)^2-c²], and all denominators are strictly positive. Substitution for the three edge motifs gives positive pairwise interactions, Delta_A>Delta_D, Delta_A-Delta_B proportional to p-q, and Delta_B-Delta_D opposite in sign to cubic H_q(p). Descartes plus H_q(q)<0, H_q(T-1)<0, H_q(T)>0 with T=q(q-1)^2 establishes the sole p>=q crossover strictly inside (T-1,T), hence integer threshold with no tie. Independently checked all symbolic difference and bracket identities and 54 rational finite sign comparisons, including q=3 and boundary T-1,T; finite tests are not a substitute for the all-p,q proof.

## originality

PASS

PASS, best-of-knowledge. Ge and Dong explicitly evaluate effective resistances and Kirchhoff index for deletion of an arbitrary matching from K_mn, covering the D motif (which is credited), but not incident two-edge motifs or their sharp ranking with D. Yang gives general bipartite Kirchhoff extrema without this fixed-part-size deletion comparison. Jiang–He–Liu–Li give diameter-three bipartite extrema; only title/abstract were available, and its complete text remains an access risk, so no unsupported whole-document noncoverage claim is made. The finite sharp cubic crossing is additional to generic spectral rank-two update tools.

## value

PASS

PASS. Kirchhoff damage after two link failures measures network robustness, with three natural complete-bipartite edge motifs. The exact discontinuous integer threshold p=q(q-1)^2 at which the least damaging type flips from disjoint to a high-degree shared endpoint, alongside strict positive interactions, is a meaningful explicit structural vulnerability classification beyond known single-link or matching deletions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
