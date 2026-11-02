---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Every S3 permutation is affine z->eps z+a over F3; for each of four sign assignments the product coefficients are fixed by N0 mod6 and three signed prefix sums T,U,V. Equality under all 36 two-letter substitutions is equivalent to equality of these four residues, because translation parameters vary independently. The derived append-zero/append-one maps are bijections on the full 6*3^3=162 signature space. Independently enumerated all binary words of length 0..13 and direct evaluations for all 36 S3 substitution pairs; recovered exactly (1,2,4,8,15,26,41,60,84,108,133,148,159,162). Independently replayed all 162 length-13 CERTIFICATE.tsv witnesses and verified no incorrect or duplicate signatures. Full reachability at 13 and bijective transition prove all n>=13, while 159 at 12 proves sharpness; not an infinite inference from samples.

## originality

PASS

The contribution is the entire equal-length quotient-growth sequence for binary positive words under every S3 substitution and its first full 162-type realization at length 13. It is not the affine model of S3 itself, a shortest positive identity, or an asymptotic separation bound. Full accessible relevant texts and published-record searches were compared by implication. The inaccessible 2021 closely related paper remains an explicit priority risk, not assumed to be irrelevant.

## value

PASS

The quotient of binary words by all substitutions into S3 is a natural finite-state automata invariant. This exact full length profile, constructive complete 162-type signature and sharp first saturation length 13 settle a meaningful finite analogue of word separation, beyond detecting one shortest identity. The result is small-group specific but complete and not an arbitrary computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
