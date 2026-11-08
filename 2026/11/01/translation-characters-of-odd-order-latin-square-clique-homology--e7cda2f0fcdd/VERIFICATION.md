---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

An odd-order abelian group table has no intercalate: the Latin 2x2 equations imply 2(c1-c2)=0 and hence c1=c2. The inspected Cioabă–Mim field-homology theorem therefore gives reduced homology only H2 with dimension (n-1)^3. Every nontrivial translation acts freely on cells with odd orbit length>=3; a setwise invariant clique contains such an orbit, forcing u=0 or v=0 or u+v=0, exactly one axis. An outside cell meets a preserved row/column/sum line in at most two positions, so every preserved clique lies wholly on one of n disjoint lines. A preserved full simplex has alternating oriented-face trace 1, hence Lefschetz L(t)=n on axes and 0 elsewhere, with H0 trace 1; at identity H2 dimension known. The resulting character is product of three augmentation characters and gives a rational isomorphism by characteristic-zero semisimplicity, with Fourier multiplicity n-|{1,alpha,beta}|. Independent exact n=5 clique enumeration yielded 515 nonempty faces, and representative translation characters (identity64, axes4, off-axes -1) matched formula.

## originality

PASS

The nonequivariant Latin-square homology ranks and even wedge-type information predate this claim. The explicit action of group translations, its augmentation-tensor module, and multiplicities of all characters are not forced by nonequivariant data and were not found in inspected primary work.

## value

PASS

The natural T=A×A symmetry is intrinsic to every group-table Latin square, and the complete H2 character supplies precise invariant subspace dimensions and every isotypic multiplicity. This is an interpretable equivariant refinement of the known nonequivariant homology theorem across all odd finite abelian groups, not mere relabeling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
