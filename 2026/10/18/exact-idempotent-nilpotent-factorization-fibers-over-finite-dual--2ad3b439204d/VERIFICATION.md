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

Over R=F_q[epsilon]/(epsilon^2), nilpotence of a 2x2 matrix is equivalent to nilpotence of its residue and there are q^6 nilpotent matrices. Rank-one idempotents number q^3(q+1), including q^2 lifts per field projection. Conditioning on rank of the residue and determinant in R partitions target matrices exhaustively into eight cases. For primitive determinant-zero targets the residue constraints y=s x-a and (a s-b)x=a^2 give q or q-1 choices of s and q^3 lifts, yielding q^4+1 or (q-1)q^3. Radical and zero cases follow by rank-one projection geometry. Transposition preserves invariants and swaps order EN/NE. Independent FULL enumeration over F_2 dual numbers finds 26 idempotents, 64 nilpotents, 1664 pairs in each order, 112 positive targets and exact fiber multiplicities matching all predicted cases. This is one finite-field check, not an unrestricted proof.

## originality

PASS

The 2026 Dolzan finite-local-ring theorem proves coincidence of IN/NI image sets and their sizes, but its inspected general image-cardinality theorem does not give ordered factorizations for each target. An earlier published F_q 2x2 fiber census is over a field without radical; it does not imply the dual-number determinant and radical strata. Algebraic calculation independently establishes a genuinely finer ring-valued distribution. Risk: an unindexed ring-fiber identity or a calculation buried in the earlier source.

## value

PASS

The ordered fiber cardinalities of the canonical product map are a natural multiplicity refinement of the known support classification. The first nonreduced finite chain ring supplies meaningful new strata invisible over finite fields, with uniform all-prime-power formulas that can be used for exact random factorization laws and ring-matrix enumerations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
