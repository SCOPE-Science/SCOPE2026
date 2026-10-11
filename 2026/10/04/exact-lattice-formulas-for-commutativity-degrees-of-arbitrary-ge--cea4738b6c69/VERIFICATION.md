---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Every subgroup of the abelian kernel \(A\) is normal because conjugation by the extra generator acts by inversion. Every subgroup outside \(A\) is uniquely \(H(B,x)=\langle B,x\gamma\rangle\) with \(Y=\langle y\rangle\le B\le A\) and \(x\in A/B\). Direct multiplication shows two such subgroups permute exactly when \((xz^{-1})^2\in BC\). For fixed \(B,C\), the map \(A/B\times A/C\to A/BC\) sending \((xB,zC)\) to \(xz^{-1}BC\) is surjective with fiber size \(|A:B\cap C|\), so counting images in the two-torsion of \(A/BC\) gives the displayed double lattice sum. The cyclic-subgroup formula is the specialization \(B=C=Y\). The inspected verifier independently builds the finite groups and complete subgroup lattices for several cyclic and mixed kernels and matches both formulas exactly.

## originality

PASS

The primary Lazorec--Tărnăuceanu paper explicitly limits generalized-dicyclic calculations to selected kernels and ends with the open problem of computing both degrees for an arbitrary abelian kernel. The audited subgroup parametrization and quotient two-torsion criterion solve that arbitrary-kernel problem directly. Resultary searches for generalized dicyclic subgroup commutativity returned the assigned theorem plus neighboring graph-theoretic and generalized-dihedral results, but no prior arbitrary-kernel formula. The source's special cyclic and \(C_2\times C_n\) formulas are recovered as specializations rather than duplicated as the main claim.

## value

PASS

The theorem answers a published open problem for the entire natural generalized-dicyclic family and exposes the exact two-torsion obstruction controlling subgroup permutability. The formulas are reusable for arbitrary finite abelian kernels and recover known special cases, so the contribution is structural rather than a collection of computations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
