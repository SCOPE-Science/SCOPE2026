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

The signed permutations of (1,1,1+sqrt(2)) give the regular rhombicuboctahedron up to normalization: the one-coordinate and two-coordinate supporting planes give square faces and three-coordinate supporting planes give triangles; their edge lengths agree at this ratio. The reproducing kernel for probability-normalized spherical surface measure is (2l+1)P_l(x dot y), so evaluation rank equals the normalized Gram rank. Exact products using d=5+2sqrt(2) give the stated six signed off-diagonal values when antipodes are removed, with maximum absolute value less than 3/4. Independent finite replay: python3 /workspace/reproduction.py 5 checks all ranks for l=0..119 without modular specialization, using the eight coordinate-sign characters of the full orbit. Exactly four characters have the matching parity; the others are zero. Each matching character gives a 3-by-3 block, and their ranks are determined by exact minors in Z[sqrt(2)] after uniformly scaling the Gram by l!17^l. The initial rank sequence is 1,3,5,7,9,11,12,12,12,10,12,12,12. At degree 9 the all-sign character block has a single nonzero rank with all entries equal; the other three matching blocks have rank three. Its kernel is the layer-sum-zero coefficient space, hence the two differences of the signed layer sums annihilate the image on the twelve lines. The relations are independent and are exactly the codimension-two image constraints. Antipodal parity transfers both rank and constraints to any representative choice. This finite calculation is not used to extrapolate: DLMF 18.14.7 with lambda=1/2 gives |P_l(u)|<sqrt(2/[pi(l+1/2)sqrt(1-u^2)]). At l>=120 each row off-diagonal sum is bounded by 11 sqrt(8/[pi*120.5*sqrt(7)])<1, proving strict diagonal dominance and full rank. No perturbation or conditioning claim is verified.

## originality

PASS

A later Resultary record is demonstrably equivalent in both the full rank law and the two layer constraints, and another later record restates the rank law. They are credited as exact overlaps, not as evidence of prior coverage. The strongest earlier inspected source passages supply design or analytic tools but not the node-specific harmonic rank defect or its isolation. The supported claim is the law and explicit image constraints for this one canonical orbit; this is not a claim of absolute priority.

## value

PASS

Exact-degree fitting of harmonic data at the vertex lines of a canonical solid is a natural interpolation problem. The result identifies a nonmonotone, isolated rank loss in degree nine after full sampling is possible, and specifies exactly which two data combinations cannot be fit. It gives the whole degree profile and describes the obstruction by symmetry, information a researcher fitting fixed-degree harmonic modes could use. Its value does not rest on merely reusing the diagonal-dominance bound at large degree.

The dated certificate retains the supplied scientific assessment, sources and limitations.
