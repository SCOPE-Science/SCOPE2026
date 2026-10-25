---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Inspected the frozen finite-incidence and polynomial-census code without executing opaque repository code. Independently generated all 13 normalized points and lines of PG(2,3) and independently exhaustively checked its 8192 point subsets: exactly 13 four-point lines and 234 six-point vertexless triangles are inclusion-minimal blockers. The no-rational-line-factor assumption excludes the line blockers, so every relevant cubic contains a triangle. For a fixed triangle, six point evaluations leave a four-parameter vector space of degree-three forms; requiring no extra rational zeros forces ABC!=0, after sign normalization the unique g=GABC=1, giving 4 projective cubics per triangle. An independent direct evaluation of all (3^10-1)/2=29524 projective cubics found 4940 blocking, exactly 936 with no rational linear factor, and every such curve has exactly six rational points. Those counts match 234*4, so there is no double counting. Coordinate diagonal signs and PGL3 transitivity on nonconcurrent line triangles give one orbit; PGL3(F3) order 5616 gives stabilizer size 6, realized by full S3 coordinate permutations. Geometric smoothness has a separate characteristic-three gradient argument: grad F*=0 implies all coordinates equal ±S and sum constraint forces one negative, where F*≠0; finite rational enumeration alone is not the smoothness proof.

## originality

PASS

Asgarli–Ghioca–Yip explicitly exhibit a smooth blocking cubic over F3 and rule out larger fields; that precursor does not on inspected full text count all cubic equations or classify their PGL3 orbit/stabilizer. Coolsaet–Botteldoorn–Fack classify small-plane minimal blocking point sets, which is crucial prior combinatorial input, not automatically cubic equation interpolation, smoothness or stabilizer. The resulting 936-equation single-orbit classification is an independently nontrivial refinement with precise remaining risk that an unaccessed full curve-classification appendix may already contain the count.

## value

PASS

PG(2,3) is the extremal exceptional field admitting irreducible blocking cubics in the published broader field theorem. A complete exact classification of its smooth blocking cubic equations, rational point support and PGL3 stabilizer is a natural finite-geometric invariant, not an arbitrary parametric slice. The result combines a complete point-incidence reduction with polynomial interpolation and geometric smoothness, and could be used directly in finite-field curve/blocking-set classifications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
