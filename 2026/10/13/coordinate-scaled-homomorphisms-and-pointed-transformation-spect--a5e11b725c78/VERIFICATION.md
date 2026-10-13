---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

## Executed check

`python3 verify.py`

Observed output:

`VERIFY_OK 2593 independent exact comparisons; 11064 scalar maps; 9033 small downset-pair maps; 1444 rectangular pairs; homogeneous endomorphism/retract spectra m<=4`

The standalone script requires Python 3 standard library only. It constructs nonempty coordinate downsets in small grids, independently exhausts all zero-preserving mappings from small source diagrams to scalar targets and small arbitrary downset targets, checks every ordered input pair under the positive-part difference operation, and compares the resulting complete hom sets with the proposed normal forms. These tests involve **11,064 candidate scalar maps**, **9,033 candidate general downset-pair maps**, and **2,593 exact predicted-versus-observed comparisons** (including 1,444 box-pair count comparisons and homogeneous box rank-spectrum comparisons). It independently checks all endomorphism-image, idempotent-image, and embedded-retract rank coefficients for homogeneous boxes in dimensions through four, at multiple side lengths. The attached source file includes every loop, filter, and assertion.

## Why this tests the difficult steps

The scalar brute force enumerates candidate maps as arbitrary tables, rather than assuming coordinate projections, and screens them operation-by-operation. The arbitrary downset-pair test independently screens all maps within its small search domain, not merely projected ones. This directly tests whether nonrectangular targets allow unexpected couplings; no such exceptions occur in the tested finite cases. Separate homogeneous-box tests check the exact coefficients and distinct retract *sets*, not only the total endomorphism counts.

## Mathematical proof and limits

The proof in `RESULT.md` establishes the normal form for every finite diagram by the identities involving distinct standard unit vectors and adjacent integer vectors. The box and rank/retract formulas then follow by exact combinatorial counting. Finite checks do not establish these infinite families; they are consistency and regression tests. The script does not claim exhaustive verification of arbitrary large diagrams, unbounded dimensions, or all prior literature. Independent mathematical audit has not been performed.
