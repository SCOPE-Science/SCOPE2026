---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

The combinatorial distance formula d(A,B)=min{2(5−|A∩B|),2|A∩B|+1} yields distance classes 0..5 and intersection array {6,5,5,4,4;1,1,2,2,3}. The inclusion filtration gives adjacency eigenvalues (6,−5,4,−3,2,−1) with multiplicities (1,10,44,110,165,132). Independently recomputing the distance-polynomial recurrence gives nonconstant coefficient rows exactly (−5,19,−35,40,−20), (4,10,10,−5,−20), (−3,3,3,−12,8), (2,−2,−7,−2,8), (−1,−5,5,10,−10). Fourth branch derivative positive for all p>=0 by 5^8>2^6·3^7, crosses zero in rational bracket (71/200,89/250), and independently high-precision root≈0.355636232374. The source exact rational-power integer certificate is inspectable and establishes all four competitor branches negative throughout the bracket, a genuinely finite exact sign test rather than sampled values. Fractional-power closure extends negative type downwards; Schoenberg equivalence to all-bandwidth Gaussian PSD and distinct squared-Euclidean point Fourier argument give Gaussian strict PD. At alpha only the multiplicity-165 harmonic vanishes on zero-sum vectors, so centered rank 461−165=296. The independent recurrence and numerical signs corroborate; large-graph BFS/numerical eigen checks in original script were inspected but not replayed separately here.

## originality

PASS

Known odd/Kneser graph distance-regular and Johnson-scheme diagonalization, the vertex-transitive generalized-roundness determinant test, and Schoenberg kernel correspondence are classical. The unique fourth-level first crossing for KG(11,5), rigorous strict comparison with all four competitors and its embedding dimension do not follow as a stated conclusion of inspected general results. A related prior published finding focuses on the top odd-graph harmonic and a different smaller graph; its full mathematical text has not been independently inspected in this run, so strong-coverage risk remains bounded but real.

## value

PASS

The exact maximal negative-type exponent and Gaussian kernel positivity frontier are canonical metrics of a natural vertex-transitive odd graph. The first failure at the fourth rather than top Johnson harmonic is a meaningful structural warning against simpler top-mode heuristics; endpoint embedding rank is exact and potentially reusable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
