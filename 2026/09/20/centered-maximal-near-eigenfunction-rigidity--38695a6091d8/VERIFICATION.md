---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-01.md",
      "INDEPENDENT_AUDIT_2026-10-01.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

The proof reconstructs. The one-sided rising-sun level-set identity gives ||M_±f||_p^p = p'∫f(M_±f)^(p-1). Since M_c f <= (M_+f+M_-f)/2, a centered deficit δ forces each one-sided norm to be at least p'-2δ. Normalizing h=M_+f/||M_+f||_p converts this to near equality in Hölder; the L^p modulus of convexity with power max{2,p} then gives ||M_+f-p'f||_p=O(δ^(1/max{2,p})), and likewise for M_-. The centered estimate follows from pointwise domination and (A-B)^p<=A^p-B^p for 0<=B<=A. Exact saturation forces a distribution tail F(t)=C t^-p, contradicting L^p integrability unless f=0. The dyadic-radii and noncompactness consequences follow from domination, equality of the sharp norm and L^p continuity. No finite experiment is used as an infinite proof.

## originality

PASS

Best-of-knowledge originality survives. Madrid's accessible primary abstract states the exact centered norm p/(p-1) but not nonattainment or quantitative near-extremizer rigidity. The closest earlier Resultary record, scale-thinning rigidity, preserves the norm under sparse radius sets and constructs near-extremizers but does not imply the simultaneous one-sided approximate-eigenfunction estimate. Colzani--Pérez Lázaro concern the one-dimensional uncentered maximal operator with a different sharp constant. No prior inspected statement implies the centered stability theorem, while the inaccessible Madrid body remains an explicit residual risk.

## value

PASS

The result gives a quantitative structural description of every near-extremizer for a newly sharp centered inequality, proves nonattainment and an affine-symmetry compactness obstruction, and transfers the rigidity to the sparse centered-radii operator. This is a motivated stability/boundary theorem rather than a routine numerical sharpening.

The dated certificate retains the supplied scientific assessment, sources and limitations.
