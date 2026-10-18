---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

PASS. Actual RESULT.md defines F8 using α³+α+1 and evaluates Tr(xy)+Norm(x+y)=0 at 28 distinct pairs. An independently implemented finite-field construction yields 28 distinct length-7 generator columns with first coordinate 1. Support(U)=28−|G∩U^perp| is a bijective orthogonality identity for the full rank-seven code. Separately from the packaged RREF verifier, enumeration by growing vector-space spans and deduplicating 128-bit membership masks exhausts all subspaces of F₂⁷. Dimension counts 127,2667,11811,11811,2667,127,1 and computed maximum intersections 1,2,4,7,10,16,28 with multiplicities 28,378,315,64,336,63,1 yield all claimed weights (12,18,21,24,26,27,28) and subcode counts (63,336,64,315,378,28,1). This is genuinely exhaustive finite proof for the fixed code, not a sample; it does not prove a claim about all [28,7,12] equivalent classes.

## originality

PASS

PASS, best of knowledge for the NEW exact minimum-support subcode multiplicities, not the pre-existing generalized weight values. Relevant original 2026 construction gives the [28,7,12] code and the ordinary weight enumerator 1+63z¹²+63z¹⁶+z²⁸. Earlier classification of four self-complementary classes and optimum-distance-profile work do not, in inspected material, count every r-subcode attaining each generalized Hamming weight. The complete affine-section counts are a stronger invariant than the parameter and nested-distance-profile data. Residual risk of older unpublished or indexed table explicitly retained.

## value

PASS

PASS. The specified code is a natural extremal few-weight subfield code; counts of all minimal-support subcodes quantify its higher-support geometry, strictly refining both its known [28,7,12] parameters and generalized weight hierarchy. The 64 three-dimensional-section maximizers are an exact nontrivial incidence datum valuable for comparative code geometry and design calculations, not an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
