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

A separate exact verifier reconstructed the line graph of GP(10,2), verified the degree-seven integer annihilating polynomial, and row/column rank over Q agrees with complex rank for these integer matrices. Independent column elimination over the rationals gives all 435 pairs: (distance, number of length-three walks if distance three, rank, multiplicity) equal to (1,–,13,60), (2,–,13,120), (3,1,13,60), (3,2,12,60), (4,–,13,120), (5,–,8,15). All 30 one-site ranks are seven. Since the polynomial is monic, degrees 0 through 6 span the full Krylov space. At distance three length-three walks are exactly geodesics. The frozen verify.py was inspected but not run; independent replay is python3 /workspace/branches/a9f86d26-6ae3-4c8a-99f5-2c7afcf15e8a/independent_rank_check.py, with rank_check_output.txt in that directory. The analytic absorption limit also checks: the Krylov space reduces A by Hermiticity and contains both site vectors, so its complement is unaffected by the absorbers and evolves unitarily. The imaginary part of a bright eigenvalue is nonpositive; equality forces vanishing at both sites because the rates are strictly positive. The eigenvector would then be an A-eigenvector orthogonal to both full Krylov spans, a contradiction. Bright evolution therefore decays even with Jordan blocks. The trace limit is the initial dark weight, giving absorption tr(Πρ₀), and for I/30 the fractions are 8/30,12/30,13/30. The dark dimensions and rate independence follow within the stated homogeneous single-excitation model.

## originality

PASS

Pass for the graph-specific two-site ranks, placement counts and geometry, not the standard spectral accessibility and dissipation principle. The strongest same-day comparison is an essentially parallel exact classification on the related truncated icosahedron. It uses the same proof template but does not supply the asserted 30-vertex ranks. The primary work on the icosidodecahedron supplies adjacency spectral context, not the pairwise rank data in the passages compared.

## value

PASS

The icosidodecahedron is a standard finite kagomé network with an established spectral motivation, and the accessible dimension is exactly the observable determining long-time mixed-state capture. No distance-only placement rule could give the result: the two distance-three classes have different ranks, while antipodal placement adds only one bright direction over a single sink (unlike complete antipodal redundancy on C60). The sharp ceiling and exact exceptional placements give actionable geometry for the stated model. The scientific value lies in this classification, not in the size or runtime of the exact enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
