# Vanishing of the mod-2 cup pairing H^1 x H^1 -> H^2 on Conf_4(Theta_(2,3,4))

## Context

The admitted target asked whether the mod-2 cohomology ring of the unordered
4-point configuration space of the theta graph Theta_(2,3,4) has cup-length at
least 2, i.e. whether there exist degree-1 classes a, b with a cup b != 0 in
H^2(-; F2). Such a witness would separate homotopy type beyond Betti numbers
and constrain formality of the associated graph braid group. The computation
resolves the question in the negative with a complete pairing matrix.

## Definitions

- Theta_(2,3,4): graph with two branch vertices A, B joined by three internally
  disjoint paths of 2, 3, 4 edges.
- G': subdivision with branch lengths (3,3,4): vertices A=0, B=1 plus branch
  vertices; |V|=9, |E|=10 (model.json edge list).
- Conf_4(Theta_(2,3,4)): unordered configuration space of 4 distinct points.
- D_4(G'): Abrams cubical model (disjoint-closure product cells). G' satisfies
  the (k=2,n=4) sufficient-subdivision condition (A-B paths use 4,4,5 vertices
  >= n-k+2 = 4; every essential cycle uses >= 6 vertices >= n-k+3 = 5), so
  D_4(G') is homotopy equivalent to Conf_4(G').
- Coefficients F2 throughout. Cup product via the simplicial Alexander-Whitney
  diagonal on the barycentric subdivision Sd(D_4); the induced cohomology
  pairing is independent of the diagonal approximation.

## Result

The mod-2 cohomology is H^*(Conf_4(Theta_(2,3,4)); F2) = F2 in degree 0,
F2^3 in degree 1, F2 in degree 2, and 0 in degree 3 (hence >= 3).
The entire cup pairing H^1 x H^1 -> H^2 vanishes identically: for every
a, b in H^1, a cup b = 0 in H^2. The H^2 summand is genuine (rank 1), so the
vanishing is not vacuous. Consequently no pair a, b witnesses cup-length 2;
the admitted nonzero-cup claim is FALSE. H^1 x H^2 -> H^3 vanishes for
dimension reasons (H^3 = 0).

## Proof / evidence

Finite F2 linear algebra, replayed by `python3 output/artifacts/verify.py`
(prints VERIFY_OK):

1. Abrams cells (unordered disjoint-closure 4-tuples): C_0..C_4 =
   [126, 350, 320, 108, 11] (cubes.pkl, cells dict).
2. Barycentric subdivision Sd(D_4): n0 = 915 vertices, n1 = 6948 edges,
   n2 = 15440 triangles, n3 = 13632 tetrahedra.
3. Simplicial coboundary ranks over F2: rank d0 = 914, rank d1 = 6031,
   rank d2 = 9408, giving H^0 = F2, H^1 = F2^3, H^2 = F2.
4. Three explicit 1-cocycles z_0, z_1, z_2 (H1_basis.pkl, edge weights
   438/387/539) span H^1: each is a cocycle and rank(B_1 + span{z_i}) = 917
   = dim Z_1 (B_1 = row space of d0, rank 914).
5. All 9 Alexander-Whitney products z_i cup z_j (front-face/back-face:
   (u cup v)(a,b,c) = u(a,b) v(b,c)) recomputed and matched to cups.pkl;
   each equals d(w_ij) for explicit 1-cochain witnesses w_ij
   (witnesses.pkl). Bilinearity kills every H^1 x H^1 cup.
6. A 25-triangle 2-cocycle g (h2gen.pkl) is closed and reduces nonzero modulo
   im(d1), certifying H^2 = F2.

The audit additionally re-enumerated the Abrams cells from the graph ([126,
350, 320, 108, 11]) and validated all 915 face-lattice entries against the
cubical face relation with zero mismatches.

## Limitations

F2 coefficients, n = 4, graph Theta_(2,3,4), pairing H^1 x H^1 -> H^2 only.
No claim about other coefficient systems, other particle numbers, other
graphs, or Massey products.

## Reproducibility

Stdlib-only replay: `python3 output/artifacts/verify.py` -> VERIFY_OK.
Artifacts: cubes.pkl (cube cells + face lattice + subdivision chains),
H1_basis.pkl, cups.pkl, witnesses.pkl, h2gen.pkl, model.json, verify.py.

## References

- Ko-La-Park, Graph 4-braid groups and Massey products, arXiv:1407.3723.
- Farley-Sabalka, Discrete Morse theory and graph braid groups, math/0410539.
- Drummond-Cole, Betti numbers of unordered configuration spaces of small graphs, arXiv:1906.00692.
- Baranovsky-Sazdanovic, Graph homology and graph configuration spaces, arXiv:1208.5781.
- Alvarado-Garduno/Gonzalez, Abrams' stabilization theorem for no-k-equal configuration spaces, arXiv:2407.07854.
- An-DrummondCole-Knudsen, Asymptotic homology of graph braid groups, arXiv:2005.08286.
