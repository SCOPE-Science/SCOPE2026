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

# Verification scope and reproduction

Run `python3 verify_examples.py` from this directory using Python 3 and no external packages. Exact rational row reduction validates the maximal-isotropic circuit construction in every rank \(4\le m\le12\) and for every projective dimension \(2\le d\le m\), including all \(d\)-line subfamilies; the program also checks representative matching/nonmatching graphs. The actual program was run and printed `EXACT_TESTS_OK: ranks 4..12, every projective obstruction dimension 2..rank`.

These finite checks cover only their enumerated matrices. The infinite proof relies on the linear representation of orthogonal maximal tori, splitting off pairwise orthogonal hyperbolic planes, Witt extension for independent isotropic vectors, and the rank bound on independent totally isotropic sets. The toric-bundle existence and splitting corollary explicitly invokes Proposition 5.1 of arXiv:2610.11340v1, whose hypotheses (smooth toric fan and local compatibility) hold for the complete fan of projective space. Full independent mathematical audit has not been carried out.
