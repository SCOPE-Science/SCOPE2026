# Unbounded collapse of linking data on realized Nielsen classes
## Finding
Let \(n\ge 2\), let \(C=C_1\sqcup\cdots\sqcup C_n\) be a trivial link in the interior of \(\mathbb B^3\), and set
\[
M=\operatorname{Int}(\mathbb B^3)\setminus C.
\]
For every integer \(m\ge 1\), there is an orientation-preserving homeomorphism \(f\) of \(\mathbb B^3\), equal to the identity on a collar of the boundary and preserving \(C\), with trivial loop braid \(b_{f,C}=1\), and with fixed points \(p_1,\ldots,p_m\in M\) such that:

1. every \(p_j\) has linking-number vector \(0\in\mathbb Z^n\) with the components of \(C\); and
2. the points \(p_1,\ldots,p_m\) belong to pairwise distinct Nielsen fixed-point classes.

Thus the linking-number map on realized Nielsen classes has fibers of unbounded finite cardinality already in the trivial-loop-braid sector.

## Assumptions and scope
The setting and notation are those of Makri, arXiv:2610.04382v1. For a fixed point \(p\in M\), its Reidemeister coordinate is denoted \(R(p)\in F_n\), where \(F_n=\pi_1(M)\). The source proves that the abelianization
\[
\operatorname{Ab}:F_n\longrightarrow H_1(M;\mathbb Z)\cong\mathbb Z^n
\]
records the linking numbers of \(p\) with the components of \(C\). The source also proves that, for loop braid \(\beta\), Nielsen equivalence is the same as \(\phi_\beta\)-twisted conjugacy of Reidemeister coordinates.

The claim concerns realized fixed-point classes, not essential classes. It gives no lower bound for the Nielsen number and does not say that the constructed homeomorphism has only the displayed fixed points.

## Proof
Choose two free generators \(x_1,x_2\) of \(F_n\) and set
\[
c=[x_1,x_2]=x_1x_2x_1^{-1}x_2^{-1}.
\]
For \(1\le j\le m\), define \(u_j=c^j\). Apply Proposition 5.1 of arXiv:2610.04382v1 with \(\beta=1\) and with the prescribed coordinates \(u_1,\ldots,u_m\). It produces one homeomorphism \(f\), equal to the identity near the boundary, with \(b_{f,C}=1\), and fixed points \(p_j\) satisfying
\[
R(p_j)=u_j=c^j.
\]

Each \(u_j\) lies in the commutator subgroup of \(F_n\), hence
\[
\operatorname{Ab}(u_j)=0.
\]
By the linking-number identification in Section 5.1 of the source, every displayed fixed point therefore has zero linking number with every component of \(C\).

It remains to separate the Nielsen classes. Since \(\beta=1\), the induced automorphism \(\phi_\beta\) is the identity. Theorem 4.6 of the source therefore says that two displayed fixed points are Nielsen equivalent exactly when their coordinates are ordinarily conjugate in \(F_n\).

The word \(c\) is cyclically reduced of length \(4\), and for every positive \(j\), the power \(c^j\) is cyclically reduced of length \(4j\): there is no cancellation inside a copy of \(c\), at the cyclic ends, or between consecutive copies. Cyclically reduced word length is invariant under conjugacy in a free group. Hence \(c^i\) and \(c^j\) cannot be conjugate when \(i\ne j\), because their cyclically reduced lengths are \(4i\) and \(4j\). Thus \(p_1,\ldots,p_m\) lie in pairwise distinct Nielsen classes.

Since \(m\) was arbitrary, the zero linking vector occurs on arbitrarily large finite collections of distinct realized Nielsen classes. This proves the unbounded-fiber statement.

## Verification
The proof uses two explicit results from arXiv:2610.04382v1. Proposition 5.1 simultaneously realizes any finite list of prescribed elements of \(F_n\) as Reidemeister coordinates of fixed points for a single homeomorphism with a prescribed loop braid. Theorem 4.6 identifies Nielsen equivalence with \(\phi_\beta\)-twisted conjugacy; at \(\beta=1\), this is ordinary conjugacy.

The only additional group-theoretic step is elementary and exact: the commutator powers \(c^j\) all abelianize to zero, while their cyclically reduced lengths are \(4j\), so they are pairwise nonconjugate. No finite experiment is used to infer the statement for arbitrary \(m\).

The March 2026 predecessor arXiv:2603.06233v2 explains that abelianized generalized Lefschetz data groups Nielsen classes by their linking vectors. The October source then gives a two-class example with identical zero linking data. The present argument upgrades that finite witness to an unbounded-fiber theorem.

## Relationship to prior work
Makri's arXiv:2610.04382v1 proves the simultaneous realization theorem and the loop-braid characterization of Nielsen classes. In Remark 5.2 and Example 5.3 it explicitly observes that linking data is not complete and realizes two non-equivalent fixed points with zero linking data, using the coordinates \(1\) and \([x_1,x_2]\). The paper does not state an unbounded multiplicity result; full-text searches for “arbitrarily”, “unbounded”, and “finite bound” found no such formulation.

Makri's earlier arXiv:2603.06233v2 gives the abelianized generalized Lefschetz formula and explicitly groups Nielsen classes having the same linking-number vector into one abelianized term. Guaschi's two-dimensional braid-theoretic work gives criteria for distinguishing Nielsen classes of punctured-disc homeomorphisms, but does not imply the three-dimensional simultaneous realization statement used here.

The new point is quantitative and structural: noninjectivity of linking data is not confined to a two-class collision. There is no finite upper bound on the size of a fiber among realized Nielsen classes, even when the ambient loop braid is trivial.

## Limitations
The constructed classes are not proved essential. Accordingly, the claim does not imply that the Nielsen number is at least \(m\), does not give a minimum fixed-point count, and does not assert that the abelianized generalized Lefschetz polynomial has a coefficient of magnitude \(m\); fixed-point indices may vanish or cancel after abelianization. The construction also requires \(n\ge 2\), because it uses a nontrivial commutator in \(F_n\). No statement is made about a single homeomorphism realizing infinitely many distinct Nielsen classes.

## References
1. Stavroula Makri, “Mixed configuration spaces, fixed points and Loop braid groups,” arXiv:2610.04382v1, 2026. Relevant items: Theorem 4.6, Proposition 5.1, Remark 5.2, Example 5.3.
2. Stavroula Makri, “The generalized Lefschetz number and loop braid groups,” arXiv:2603.06233v2, 2026. Relevant items: Section 4.4 and Lemma 4.2.
3. John Guaschi, “Nielsen theory, braids and fixed points of surface homeomorphisms,” Topology and its Applications 117 (2002), 199–230, DOI 10.1016/S0166-8641(01)00019-0.
