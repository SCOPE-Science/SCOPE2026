---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Reconstructed the 15-monomial coefficient-mask representation of all 32767 nonzero homogeneous ternary quartics over GF(2), the geometric smoothness condition F=Fx=Fy=Fz=0, GL3(2) projective action, and rational theta-line square test: restricted binary quartic has odd terms zero and nonzero Q(s,t)^2; n_i counts number of GF(2) rational zeros of Q. A new independent exact finite-field evaluator tested projective points over GF(2),GF(4),GF(8),GF(16) and found singular first-witness counts 20174,1015,616,42, exactly 21847 total, leaving 10920. Independently reconstructed all 168 GL3(2) polynomial substitution actions; the 78 source-listed representatives generate disjoint projective orbits covering all 10920 remaining masks with no overlaps. For each of 78 reps, independent exact GF(2) Groebner unit-ideal tests on all three affine charts gave (1), excluding singularities over the entire algebraic closure, not merely finite extension samples. Independently recomputed all seven line-restriction contact splitting counts and rational point counts for each orbit representative; after orbit weighting obtained EXACTLY the same 40 table rows, 10920 forms, 78 classes and rational theta-line frequency (0:3072,1:5278,2:2352,3:105,4:112,7:1), including 218 forms with >=3 theta lines, in five orbits. The singular-vs-smooth partition is exhaustive because witnesses exclude 21847 and symbolic ideal certificates cover all remaining 10920. Inspected primary RESULT, five algorithm/certificate sources and both published tables at exact frozen Git blob IDs.

## originality

PASS

Nart–Ritzenthaler full 2004 arXiv manuscript explicitly classifies all plane quartic isomorphism types over finite characteristic-two fields and supplies normal models, automorphism counts and bitangent-number/2-rank information; thus the 78 classes and raw seven-bitangent exceptional curve are already known, and cannot be claimed original. Pacini–Testa complete 2022 accepted open-access manuscript analyzes geometric theta-hyperplane/bitangent multiplicities in characteristic two; its Theorem 4.11 addresses generic characteristic-two multiplicity, not the finite F2 arithmetic 40-cell joint distribution including Galois splitting of contact quadratics and N. The exact simultaneous (N,n0,n1,n2) frequency and orbit table is extra arithmetic data that can be computed from known normal models but is not directly given in the inspected full papers. Extensive exact independent reconstruction makes this a real complete classification rather than an arbitrary unexplained collection of numbers.

## value

PASS

This complete joint invariant over the smallest finite field quantifies rational theta-line contact divisors (conjugate pair, repeated rational point, two distinct rational points) together with rational point count and embedded projective orbit multiplicity for every smooth plane quartic. It refines the natural known 78-class census in a way relevant to arithmetic bitangents and rational theta characteristics. Exact self-contained finite complete classification remains mathematically valuable without a general theorem over all finite fields; the exhaustive certificates make the scope precise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
