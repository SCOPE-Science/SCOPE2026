---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

The orthogonal block Hadamard Q maps L to sqrt2 S, so each pure 24-cell gives 48 maximal 4-simplices by the original exact finite classification. At t=sqrt2, transitivity of signed permutations on long roots reduces all mixed five-generator configurations to 178365 anchored combinations. Actual verify.py computes integer cofactors and compares all determinants exactly as pairs u+v sqrt2; independent verify.cpp uses distinct signed-permutation determinants. Read both source codes. Independently enumerated all 178365 anchored combinations by NumPy determinants and recovered k=0,1,2,3,4 cardinalities 8855,42504,69828,46552,10626 and maxima 1/2,sqrt2/3,(128+32sqrt2)/384,(128+32sqrt2)/384,sqrt2/3, corroborating the exact certificates. The complete certificate shows 10 anchored pure-long global maximizers, 24+6 anchored extremal mixed patterns and no two pure-max five-sets sharing four roots. Affinity of the signed simplex determinant in each vertex extends vertex maximality to any inscribed simplex, and no shared-four-face forces rigidity of all maximizers. Inclusions K_t⊂K_sqrt2 for t<sqrt2 and K_t⊂(t/sqrt2)K_sqrt2 above give exact M(t) and strict support arguments exclude the other type. Finite enumeration is exhaustive for the discrete 48-point configuration, not a proof of arbitrary convex geometry without separate affinity step.

## originality

PASS

The exact pure 24-cell largest-simplex volume and 48 optimizers are earlier published and credited; F4 and 288-cell root geometry are classical. The assessed novelty is the strict exact mixed-root determinant cap sqrt2/3 at equal radius and resulting all-real t transition with unrestricted optimizer rigidity and 288 secondary mixed-root maximizers. The inspected Dechant original constructs root/polytope geometry but does not assert that mixed-root volume classification. Results for any five points on S3 do not impose F4 discrete allowed vertices and thus do not prove the classified equality families. Unindexed 288-cell simplex tables may nevertheless cover secondary counts; explicit residual risk.

## value

PASS

A sharp global optimization and exact symmetry-phase transition in a canonical two-orbit root-system family, with a nontrivial complete mixed configuration enumeration and rigidity of arbitrary continuous optimizers. It determines a natural exact volume invariant of the F4 radial interpolation beyond a recomputation of the known single 24-cell case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
