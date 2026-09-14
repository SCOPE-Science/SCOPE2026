# No beyond-skeleton Gal-equivariant verticial-break tempered invariant for the rigid K4 skeleton over Q5

## Context

Let K = Q5 with ring of integers OK = Z5 and residue field k = F5.
Let Gamma0 be the genus-3 trivalent metric graph of K4 combinatorial type whose
six edges have pairwise distinct lengths 1, 2, 3, 4, 5, 6 in normalized
valuation units. The target asks: for smooth projective genus-3 Mumford curves
X over K with Berkovich skeleton isometric to Gamma0, does the outer
Gal(bar K / K)-action on the geometric tempered fundamental group distinguish
K-isomorphism classes through verticial decomposition groups together with
upper-numbering ramification breaks along incident annuli, beyond the metric
skeleton? Either exhibit X1, X2 with isometric skeleta but non-isomorphic
special fibers and a distinguishing Gal-equivariant break invariant, or prove
no such invariant exists.

## Definitions

- Pi^temp(X_bar): geometric tempered fundamental group (Andre-Mochizuki).
- Verticial subgroup: conjugacy class of maximal compact subgroup, corresponding
  to a vertex (irreducible component) of the stable reduction.
- Edge/annulus decomposition group: stabilizer of an edge (node), carrying an
  inertia filtration whose upper-numbering breaks at a split node of thickness
  L in residue characteristic 5 depend functorially only on (L, 5).
- Split totally degenerate fiber: all components P1, all nodes rational.
- Labelled dual graph: dual graph with thickness labels L_e on edges.

## Result

No. There is no Gal-equivariant decomposition-plus-break invariant going beyond
the metric skeleton for this rigid Gamma0.

(i) The hypothesized pair (X1, X2) with isometric skeleta Gamma0 but
non-isomorphic special fibers over F5 does not exist: the split totally
degenerate genus-3 K4 special fiber over F5 is unique up to k-isomorphism.

(ii) For every Mumford curve X/K with skeleton isometric to Gamma0, the
verticial decomposition data plus incident-annulus upper-numbering breaks are
canonically determined by the fixed labelled metric graph (Gamma0, p = 5)
alone, hence identical across all such X.

Sharp boundary: the literal strengthening that any two such curves have
G_K-equivariantly isomorphic geometric tempered groups is false. Distinct
Schottky unit parameters give non-K-isomorphic curves with the same Gamma0 and
same special fiber; the full outer Galois action sees those units. The extra
information lives outside verticial-break data.

## Proof / evidence

Lemma 1 (metric rigidity, computed): with edges labelled 1..6, the stabilizer
in S4 is trivial and the four vertex incident-length signatures
{1,2,3}, {1,4,5}, {2,4,6}, {3,5,6} are pairwise distinct. Hence
Aut_met(Gamma0) = 1; every vertex and edge is canonically identified.
Verified by exhaustive enumeration in check_rigidity.py.

Lemma 2 (split reduction): lengths are integral so no ramified extension is
needed; the Deligne-Mumford stable model over OK exists uniquely with labelled
dual graph Gamma0. G_K acts by metric isometries, hence trivially, so every
component and node is fixed, nodes are k-rational, and each component is P1_k
with three rational marked points.

Lemma 3 (fiber uniqueness): each component P1 with ordered triple of rational
nodes is rigid (M_{0,3} is a point; Aut(P1, {0,1,infty}) = 1) and gluing at
ordinary double points adds no moduli. Any two split K4 fibers are
k-isomorphic; the labelled curve with distinct thickness labels has trivial
labelled automorphism group.

Theorem 4: by reconstruction, verticial subgroups and edge inertia groups are
canonically matched to labelled vertices/edges; by functoriality the break
filtrations depend only on fixed (L_e, 5). The whole package is a functor of
the fixed labelled graph.

Proposition 5 (sharpness): the labelled deformation base Z5[[t_1..t_6]] with
parameters s_e = 5^{L_e} u_e gives Mumford curves X_u with skeleton Gamma0 and
fiber C0. A K-isomorphism extends to stable models and induces a labelled
automorphism of C0, hence identity, so parameters coincide: distinct units give
distinct K-curves. Tempered anabelian recovery then implies full outer actions
cannot all coincide. Supporting computation: Jacobian period pairing matrix has
det 571 (odd, prime to 5); unit 2 has order 4 in F5^x.

## Limitations

Uses cited standard facts without reproof: tempered vertex/edge reconstruction,
break functoriality, stable-model uniqueness, miniversal deformation with
3g-3 parameters, tempered anabelian theorem (only for sharpness). No global
plane-quartic equations; local miniversal models plus algebraization suffice.

## Reproducibility

Run `python3 output/artifacts/check_rigidity.py`: checks S4 stabilizer
triviality, vertex signatures, det M = 571 odd and prime to 5, and order of 2
in F5^x. Output reference in `output/artifacts/rigidity_output.txt`.

## References

- E. Lepage, Tempered fundamental group and metric graph of a Mumford curve
  (arXiv:0811.3169).
- S. Mochizuki, tempered anabelian graph-of-anabelioids reconstruction.
- J. Poineau, D. Turchetti, Berkovich curves and Schottky uniformization.
- Deligne-Mumford stable reduction; Gerritzen-Herrlich-VanderPut on pointed
  trees of projective lines.
