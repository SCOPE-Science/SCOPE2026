---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Every 4-distinct-coordinate support translates to 0 plus three binary differences of rank two or three, producing respectively the four (1,x,y,xy) types or the eight (1,x,y,z) cube vertices with equal multiplicities. The first set spans iff all four types occur. In the cube, every deficient set has at most four vertex types, and the only deficient four-subsets are its 6 coordinate faces and 6 diagonal planes; all 5-sets span. Inclusion-exclusion over occupied types proves P0=4(3/4)^m-6(1/2)^m+4(1/4)^m and P1=12(1/2)^m+8(3/8)^m-68(1/4)^m+72(1/8)^m, and hypergeometric replacements C(jN/v,m)/C(N,m). Max deficient row counts are 3N/4 and N/2 exactly. Rank is invariant under nonzero column signs and rescaling. Direct rational matrix calculations and occupancy tests independently passed 590 cases, including sharp finite thresholds; all-d,m quantifiers follow from proof not tests.

## originality

PASS

PASS best of knowledge: classical Walsh characters, affine-cube coplanarity, coupon-collector inclusion-exclusion, and general SRHT embeddings are prior. Inspected Balabanov et al. gives probability bounds and algorithms, not the two exact support-dependent rank-loss distributions and row-count guarantees. Resultary related four-sparse Walsh spectra concern Fourier support sizes, not sampled-row rank. A specialized cube-submatrix enumeration not indexed could cover the formulas; no exhaustive priority certification.

## value

PASS

Injectivity is a fundamental necessary property for structured-sketch least squares. This all-support four-coordinate classification separates failure exponents and sharp deterministic sampling thresholds by Θ(N) despite identical leverage scores 4/N; it provides a meaningful exact benchmark and demonstrates coherence statistics can conceal affine dependence. It makes no claims on conditioned spectral distortion or larger supports.

The dated certificate retains the supplied scientific assessment, sources and limitations.
