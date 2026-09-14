# Parity versus perversity and decomposition-number purity for the 3-Kronecker KLR algebra at (2,2) over F2

## Context

Let Q be the 3-Kronecker quiver (vertices 0,1 with three arrows 0 -> 1) and nu = (2,2).
Let R_{nu,k} be the affine Khovanov-Lauda-Rouquier (quiver Hecke) algebra attached
to (Q,nu) over a field k. Lusztig's geometric construction realizes R_{nu,k} as an
Ext-algebra of pushforwards L_{y,k} = pi_{y*} k[dim F_y] along proper maps
pi_y : F_y -> E_V from flag varieties to the representation space E_V, equivariant
for G_V = GL_2 x GL_2 (Maksimau, J. Algebra 2015, Thm 1.1/2.20). The indecomposable
parity complexes E(lambda,k) categorify a p-canonical-type basis, while in
characteristic zero the Lusztig intersection-cohomology complexes E(lambda)
categorify the canonical basis. Maksimau Lemma 3.7 reduces evenness of pi_{y*} k
to vanishing of odd cohomology of every fibre, and Section 3.10 shows evenness
forces the Lusztig and parity categories to coincide. Prior evenness theorems cover
Dynkin quivers (type A proved; D/E via later work) and at most the 2-arrow affine
Kronecker quiver, not the wild 3-arrow case. The target asks whether purity holds
at nu = (2,2) over F2.

## Definitions

- E_V = M_2^3 (dimension 12): triples A = (A_1,A_2,A_3) of 2x2 matrices.
- G_V = GL_2 x GL_2 acting by (g_0,g_1).(A_i) = g_1 A_i g_0^{-1}.
- Y_nu: flag types (i,a) with total dimension nu; |Y_nu| = 14, of which 6 are
  complete-flag types.
- pi_y : F_y -> E_V: Lusztig-type proper map; L_{y,k} = pi_{y*} k[dim F_y].
- E(lambda): characteristic-zero Lusztig IC complexes (canonical basis).
- E(lambda,k): indecomposable parity complexes over k (p-canonical-type basis).
- d_{lambda,mu}(t) = sum_n dim Hom(P(lambda),L(mu)<n>) t^n: graded decomposition numbers.
- For M in M_2 and lines L_0 = span(x), L_1 = span(y): f_M(x,y) = det(Mx,y),
  a bihomogeneous (1,1)-form on P^1 x P^1.

## Result

For the 3-Kronecker quiver at dimension vector nu = (2,2) over k = F2:

1. Every fibre of every Lusztig map pi_y (all 14 y in Y_nu) has vanishing odd
   cohomology over every field and torsion-free (free abelian) integral cohomology.
2. Hence every pi_{y*} F2 is even, every indecomposable parity complex
   E(lambda,F2) is perverse and is the modular reduction of E(lambda), and every
   graded decomposition number d_{lambda,mu}(t) of R_{nu,F2} equals its
   characteristic-zero canonical-basis value. No differing d_{lambda,mu}(t) exists.

## Proof / evidence

Master isomorphism: M |-> f_M is a linear isomorphism M_2 ~= H0(P^1 x P^1, O(1,1)).
Since V_0 = V_1 = C^2, every flag involves at most one line per vertex, so every
mixed-flag fibre is Z(W) = Z(f_{A_1},f_{A_2},f_{A_3}) in P^1 x P^1 with
W = span{f_{A_i}}, r = dim W; remaining Grassmannian fibres (common kernels,
common images) are linear conditions in P^1, hence empty, a point, or all of P^1.

Classification: r = 0 gives P^1 x P^1; r = 1 gives a smooth (1,1)-curve (~= P^1 iff
det M != 0) or a wedge of two rulings (rank-1 M); r >= 2 gives at most one
horizontal plus at most one vertical ruling plus a finite residual, or a finite
set. The r >= 2 step is characteristic-free: a smooth (1,1)-curve C has
h0(O_C(2)) = 3 < h0(O(1,1)) = 4, so forms vanishing on C form a 1-dimensional
space (likewise for a reducible H+V divisor); two independent forms share no
(1,1)-curve. Distinct rulings in one direction force W = 0. All listed types have
H^odd = 0 with free integral cohomology by Mayer-Vietoris.

Computation: exhaustive check of all 16^3 = 4096 matrix triples over F2
(rank distribution {0:1,1:105,2:1470,3:2520}; types whole 1, wedge 63,
smooth 42, ruling+finite 252, finite 3738) plus 8000 F5 samples passed
(output/artifacts/verify_fibres.py, exit 0, verify_log.txt). The F2 rationality
argument (two F2-points force the whole P^1 line) closes the extension-field gap
for rulings. Free integral stalks give identical even-degree ranks over F2 and Q
by universal coefficients; connected stabilisers imply only trivial local systems,
so parity summands are the Lusztig IC complexes. Lemma 3.7 then yields the
purity conclusion.

## Limitations

Proved only for nu = (2,2) over F2 (integral freeness gives the same rank pattern
over Q). Relies on Maksimau Lemma 3.7 and the Section 3.10 evenness mechanism as
cited method. No claim for larger dimension vectors such as (3,3), other
characteristics, or the wild Kronecker quiver in general.

## Reproducibility

Run `python3 output/artifacts/verify_fibres.py` (exit 0 on success; regenerates
verify_log.txt). It enumerates Y_nu, exhausts all 4096 F2 triples, checks
kernel/image Grassmannians, samples 8000 F5 triples, and records the
restriction-degree lemma check.

## References

- R. Maksimau, Canonical basis, KLR-algebras and parity sheaves, J. Algebra 2015
  (arXiv:1301.6261v2): Thm 1.1/2.20, Lemma 3.7, Sec 3.10.
- R. Maksimau, Flag versions of quiver Grassmannians for Dynkin quivers have no
  odd cohomology (arXiv:1909.04907): Dynkin scope, 2-arrow Kronecker extension.
- McNamara et al., Stratifying quiver Schur algebras via ersatz parity sheaves
  (arXiv:2504.17430): 2-arrow Kronecker semicuspidal/Schur results, distinct object.
