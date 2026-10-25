---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The 16 coefficients of bidegree (3,3) over F2 encode all 65535 nonzero sections. A rational base fibre is a rational triple point iff its binary cubic mask is 1,8,15 (cubes of linear forms); this directly computes t_1,t_2. The obstruction to t_1+t_2>=4 enumerates 1128 masks: 1110 rationally singular; remaining 18 form one order-18 orbit represented by mask 6854 with an explicit singularity at (alpha,alpha+1) in F4. For full smoothness, finite-extension rational singular witnesses through degree six cover exactly 49515 masks; the remaining 16020 candidates split into 252 orbits of the 72-element split-quadric automorphism group. Each representative satisfies Groebner unit ideal (f,df/dx,df/dy) on each of 4 affine charts, establishing geometric smoothness beyond bounded-point tests. Audited C++ nullspace and Python orbit/Groebner code and recompiled/reproduced finite-field enumeration: smooth counts after degrees 1..6 were 18674,17984,16524,16308,16164,16020, and 252 orbits. All 1008 local Groebner unit-ideal checks passed. Independently reconstructed both binary outputs with exact matching Git blob IDs SHA1 ad56f5a... and ac915ea..., and matched all six weighted orbit census totals (5856/103,6912/96,1224/19,48/2,1620/27,360/5). The degree-4 zeta count derivation from Newton sums and reciprocal functional equation is valid and supported by the separate exact F2^d point checks for masks 6335 and 10685.

## originality

PASS

The mathematical object (smooth split (3,3) canonical genus-four curves over F2) is already classified by Xarles 2020, so counting 252 is not new by itself. The claimed new invariant is joint numbers of rational scheme-theoretic triple fibres for BOTH natural trigonal projections, exact six-pair histogram, sharp combined bound t1+t2<=3, and distinct profiles for a pair with identical Weil numerator. Xarles primary PDF and public Magma project concerns classification/field point counts and does not state this paired ramification distribution; Looijenga complex-characteristic trigonal pencils do not furnish the finite-field arithmetic census. Best-of-knowledge PASS with potential unpublished computation residual.

## value

PASS

Joint rational total-ramification for the two intrinsic degree-three projections of a split canonical genus-four curve is a natural arithmetic-geometric invariant. Six exhaustive strata, a sharp ≤3 obstruction and a same-zeta/different-ramification example provide a motivated independent refinement of a previously known F2 genus-four census, not a meaningless re-tabulation of previously known point counts. The complete positive and negative smoothness certificate makes a finite exact classification mathematically usable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
