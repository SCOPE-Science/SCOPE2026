---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For monic Q in Z[X] rational irreducible degree d>=2 splitting into d distinct mod-p linear factors, Hensel gives distinct irrational p-adic conjugate roots α_i. At each j, exactly d residue kernel subsequences are g_{i,j}(n)=j+ν_p(n-β_{i,j}); unmatched residues are constant, and a constant 1 first appears at depth 2. Affine rigidity precludes coincidences between all α_i and tails β_{i,j}: an irrational root cannot have a finite orbit under nontrivial positive p-power rational-affine action. Independent coefficient-isolation via nonnegative integers n approaching one p-adic irrational point shows valuation sequences and constant are Q-linearly independent. Consequently rank depth0=1, depth1=d+1, depth e>=2=de+2 for all e, with no finite-precision extrapolation. Independently calculated sample rational ranks 1,3,6 for Q=x²+1,p=5 at e=0,1,2.

## originality

PASS

Best-of-knowledge PASS for exact rational p-kernel span rank at EVERY finite depth in the completely split irreducible case. Bell 2007 Proposition 3.2 already proves irrational-root valuations are not p-regular, including example ν_5(n²+1); no novelty is claimed for nonregularity. The inspected Bell proof uses runaway p-adic tails but does not supply the cumulative rank de+2, the constant-at-depth-two adjustment or the global affine-distinctness argument. Related Medina/Moll/Rowland and Sobolewski establish qualitative valuation criteria.

## value

PASS

This degree-sensitive finite-depth rational rank is a canonical quantitative refinement of p-regularity: it identifies exact linear dimension growth rather than only non-finite generation. The irreducible totally split class is structurally natural, and such exact kernel ranks inform automata/regular-sequence complexity despite infinite rank in the limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
