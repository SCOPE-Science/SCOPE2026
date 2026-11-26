---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The bilinear cocycle gives the displayed central extension; the square of (x,z) has central coordinates x_i x_j. In a fixed edge-character sector the twisted group algebra has commuting-basis radical R=ker W: vanishing after trace for every test vector is equivalent to vanishing over k by nondegeneracy and scaling. Its center has the basis indexed by R, and the full algebra is free over this center on the coset representatives of R in k^n. Semisimplicity then gives |R| simple factors each of dimension |k^n/R|=q^(2s), hence |R| irreducibles of degree q^s even if the edge subgroup is not the whole center. The square is scalar in each sector, giving the displayed FS average. If Q is nonzero on R, scaling a vector by a makes its value a^2 Q(r), so some value has trace one and translation cancels the sum. Otherwise quotienting by R leaves a nondegenerate quadratic form and gives its normalized positive or negative Gauss sum. In a bipartition Q is bilinear across the parts and summation over one part gives q^(n-s). The part projection conjugates to the inverse by an involution, with a nonidentity vertex involution available for the identity since n>=1. For a nonbipartite graph take an odd cycle, constant trace-one edge weights on that cycle only, and its all-one vector. It lies in R, including when the cycle has chords in the graph, and Q has trace one there. This yields a nonreal irreducible and excludes reality, thus also strong reality. Independently, inverting a full-support vertex vector would require h_i/x_i+h_j/x_j=1 on all edges, impossible around an odd cycle. The K4 F2 Gauss sum -4 checks the degree-four quaternionic sector. An independent bounded F4 check enumerated scalar sectors and vertex-vector commutators on the triangle, square, K4 and an edgeless four-vertex graph. The degree/indicator weighted sums matched the direct square-identity counts; the triangle and K4 have zero sectors, the square and edgeless graph have only +1, and K4 also has degree-16 negative sectors. This was a consistency check, not a substitute for the algebraic proof. The frozen replay path is python3 check_graphical_fs.py in the source package; the uploaded script was inspected, not executed.

## originality

PASS

Credit existing quadratic-map criteria for reality, strong reality, total orthogonality, and radical-based enumeration of real special 2-group irreducibles. The supported distinct result is their uniform graph-theoretic equivalence with bipartiteness for this family over every finite field of characteristic two, with an explicit odd-cycle zero-indicator sector and a complete graph-weighted spectral description including nonreal sectors. The general tests are substantially overlapping background; their novelty is not credited to the frozen record. The same-family indexed hit gives the commutator and involution invariants but not the connection among these four properties.

## value

PASS

Bipartiteness is an elementary graph decision that resolves three group-theoretic properties at once in a family where generic special-group criteria allow these properties to differ. An odd cycle gives an explicit nonreal sector, not just an existential obstruction. The weighted spectral formula distinguishes the three representation types with multiplicities, including negative sectors in suitable graphs, and is useful beyond the binary property test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
