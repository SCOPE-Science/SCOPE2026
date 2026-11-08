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

Fix the source recurrence (1/d)Σ_facets[facet (d−1)-volume / orthogonal central-section (d−1)-volume] W_{d−1}(section), and W1=2. The section of the 4-cross-polytope by Σx_i=0 is the 12-vertex cuboctahedron C=conv{(e_i−e_j)/2:i≠j}, ordinary 3-volume 5/6. Its eight equilateral triangular facets each have area √3/8, orthogonal section regular hexagon of area 3√3/4 and W2=3; six square facets have area 1/2, square central section area 1 and W2=4. The contributions to 3W3(C) are 4 and 12, so W3(C)=16/3. The sixteen tetrahedron facets of B each have Euclidean 3-volume 1/3 and section C volume 5/6, so W4(B)=16·(1/4)·(1/3)·(16/3)/(5/6)=128/15. The four-cube polar has coordinate facets parallel to equal-volume central cubical sections and W4=16 by recursion. Exact independent rational cancellation confirms 8/15; all facet counts and geometry are given explicitly, and numerical hull code is corroboration, not a proof of a global property.

## originality

PASS

Wolansky’s defining paper states the recurrence and calculates standard cubes and balls; its inspected example sections do not evaluate the 4-cross-polytope or intermediate cuboctahedral section. Classical planar hexagon/parallelogram self-perimeters are prior work. The polar ratio 8/15 is an explicit diagnostic for the stated recurrence, and is notably inconsistent with a naive universal equality of polar pairs suggested in source prose; it does not claim to disprove a different precisely qualified duality theorem.

## value

PASS

The 4-cross-polytope and its polar cube are natural first nontrivial test bodies for a recently defined higher-dimensional recursive functional. The cuboctahedron is a genuine two-facet-orbit intermediate geometry, so evaluating W3=16/3 is not merely plugging into the cube formula. The exact polar ratio 8/15 clarifies structural interpretation of the recurrence and gives a benchmark for future extremal or polarity questions. A narrow exact self-contained invariant has clear future mathematical use without needing a new general theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
