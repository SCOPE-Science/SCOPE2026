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

A hypothetical 7x7 defining matrix with no zero entries or zero 2x2 minors can be normalized by row/column scaling; discrete logarithms in F_9^*=Z_8 turn every row-pair minor condition into seven distinct coordinatewise differences, giving a CDPA(7,7;8). In any normalized CDPA(k,7;8), a nonzero row is (0,r_1,...,r_6) using six distinct nonzero residues, so there are exactly 7*6! candidates. After fixing one nonzero row, a permutation of the last six columns yields one of seven canonical missing-residue forms. The full verifier enumerates all 5040 rows; each canonical form has 64 compatible neighbors, whose compatibility graph has 24 edges and no triangle. A five-row CDPA would require the zero row, the canonical row and three pairwise compatible neighbors, so it is impossible. The explicit four-row CDPA proves sharpness. The same exact-arithmetic verifier checks the published 6x6 F_9 lower-bound matrix has nonzero determinant, entries and every 2x2 minor. This is exhaustive finite proof, not a failure-to-find argument.

## originality

PASS

Nasr Esfahani--Stinson explicitly leave the parameter at 6 <= M_R([1,2],9) <= 7, with a size-six construction; thus their theorem does not imply the submitted equality. Yin's complete 2005 paper defines CDPAs, proves the even-order column bound and constructs four-row arrays near the maximum column length, but does not determine the maximum number of rows for CDPA(k,7;8) or exclude k=5. Resultary search found no earlier resolution. Yin's 2004 predecessor could not be recovered after public/OA attempts and two same-job authorized institutional attempts timed out; that inaccessible plausible source is retained as a residual risk rather than treated as novelty evidence.

## value

PASS

The result closes an explicit one-unit open parameter gap in linear strong AONTs and determines the exact row extremum of the finite cyclic difference-packing obstruction responsible for it. This is a natural exact finite classification tied directly to a published cryptographic construction problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
