---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

The Kneser graph on n-subsets of [2n] is exactly a complement matching, giving the join of N=binom(2n,n)/2 two-point complexes. Its label action is an orthogonal signed permutation on pair coordinates; fixed coordinates are one per orbit precisely when its pair stabilizer does not exchange the halves, proving the PL fixed-sphere statement including d=0. For a transposition, all fixed pairs have positive sign (n>=2), and the b/2 remaining swapped-pair blocks have determinant -1, b=binom(2n-2,n-1). Legendre gives v2(b)=number of ones in n-1, hence b/2 odd iff n-1 is a binary power. Degree gives integral top character; rational transfer plus Armstrong using fixed-point transpositions proves the quotient statements. Independently reconstructed signed permutation matrices and verified all 41064 elements of S4,S6,S8 and fixed transposition dimensions for n=2,3,4; finite checks corroborate but are not the universal proof.

## originality

PASS

The known nonequivariant cross-polytope sphere is explicitly credited to Feng–Wang; the audited conclusion instead computes its full group orientation, arbitrary-subgroup fixed PL spheres and full quotient topology. Searches under signed middle-subset, complement-pair and Kneser aliases and two relevant primary sources did not identify an implication covering these new equivariant statements. Generic signed determinant/Legendre/Armstrong tools are not claimed new.

## value

PASS

A complete natural S_{2n}-equivariant classification of the zero-excess Kneser sphere, including all subgroup fixed spaces and a sparse binary-power orientation boundary, supplies group and quotient invariants unavailable from nonequivariant sphere Betti ranks; an independently useful structural symmetry result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
