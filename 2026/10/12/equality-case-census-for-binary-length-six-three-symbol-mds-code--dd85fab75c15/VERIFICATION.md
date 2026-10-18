---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The exact parameter is cyclic 3-symbol distance d_3>=5 for unrestricted binary words of length six, no linearity assumption. Agreement on any four consecutive bit coordinates forces two equal consecutive length-three windows and d_3≤4, so projection injectivity gives |C|≤2^4=16. An independent adjacency computation on all 64 words found 1,632 d_3-compatible unordered pairs; independent Bron–Kerbosch exhaustive maximal-clique enumeration reported exactly 100,772 maximal cliques with size distribution 8:10712,9:33216,10:23936,11:19200,12:10688,13:2304,14:640,16:76. The 76 maximal size16 cliques are all possible labeled equality cases; no larger clique exists by the projection bound and enumeration. From these exact codebooks, 64 XOR translations plus D_6 (six rotations, six reflections) give 768 distance-preserving transformations with maximum-code orbit sizes 4,4,12,24,32, and exactly 44 affine translates of 4-flats; the 32 nonlinear maxima comprise the unique 32-element orbit. Full metric-isometry group is NOT claimed. The two algorithms were independently constructed from inspected definitions and cross-check the finite census; the finite result is exhaustive because all vertices and all maximal cliques are enumerated, not sampled.

## originality

PASS

Ding–Zhang–Ge establish the b-symbol Singleton bound and analyze especially linear code constructions; the sharp number 16 itself is prior work and not original. The assigned extra assertions quantify over all nonlinear codebooks and classify orbit structure, not supplied by the cited general size bound. Searches for aliases via b-symbol read vectors, cyclic b-symbol MDS codes, small n6 binary equality and finite tables, and the Resultary catalogue identified no exact 76 codebook orbit census. Best-of-knowledge PASS, with unindexed table/finite catalogue risk.

## value

PASS

The length-six cyclic three-symbol equality problem has a standard Singleton optimum, but the unrestricted codebooks are not classified by the size bound or by linear MDS constructions. Exact 76-code census, five translation-dihedral orbits, and the separate 44 affine versus 32 genuinely nonlinear equality cases are natural sharpness and symmetry data for the first small nontrivial cyclic read-channel parameter; researchers constructing or classifying non-linear b-symbol MDS codes can reuse this exact classification. Finite dimension is scientifically motivated by the sharp Singleton equality and nonlinear orbit phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
