---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Each link is PSD precisely when a,c,d>=0, a+c+d=1, |w|^2<=ad, and support has zero |01>. Direct contraction of middle qubits on Phi+ maps two such states to half of rho(a'a,a'c+c'd,d'd,w'w) in the specified orientation. This matches the upper-triangular 2x2 matrix product T_new T_old, and induction over L-1 projections yields normalization factor 2^(1-L) and W product. The partial transpose contains 2x2 block [[0,W],[conj(W),C]]/Z with eigenvalue (C-sqrt(C^2+4|W|^2))/(2Z)<0 iff W!=0; standard X-state concurrence likewise 2|W|/Z. Every entangled input on this face has w!=0, forcing a*d>0 and hence positive success probability for finite L. An independent exact Fraction direct contraction for 3 distinct real links gave (A,C,D,W)=(6/125,14/125,2/25,3/200), branch probability 3/50 and concurrence 1/8, matching induction. The specialization c=a-d returns the homogeneous 2026 paper family; finite checks corroborate, not prove all lengths.

## originality

PASS

Best-of-knowledge PASS. The assessed object is NOT merely an L=2 special case or a homogeneous two-parameter family; it is a composition for all finite heterogeneous lengths. A general X-state single-swap formula is an ingredient, but its statement does not itself enumerate this invariant face or articulate the all-length persistence. Trinh full text is inaccessible and might contain hidden equivalent results; priority risk retained rather than claiming it lacks them. The general two-link physics underpins the proof; the claimed contribution is the exact associative oriented invariant face, arbitrary heterogeneous finite depth, and all-length entanglement condition. Full Trinh paper was not available; no whole-text NOT_COVERING claim is made and possible broader prior coverage is a material risk. Residual priority/access caveats explicitly included; no search absence alone is interpreted as novelty.

## value

PASS

Identifies a natural entire rank-deficient X-state face closed under a physically defined postselected Bell-swap operation, with an exact associative triangular-matrix composition and a heterogeneous finite-length entanglement-persistence criterion. It extends the isolated homogeneous rank-three example and supplies a reusable route-level calculation, while clearly distinguishing conditional survival from deterministic or all-branch transport.

The dated certificate retains the supplied scientific assessment, sources and limitations.
