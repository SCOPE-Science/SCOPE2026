# Finite modal measurable quotients are exactly partial-function frames
## Finding

Let
\[
\mathcal F=(X,R,\Sigma,N)
\]
be a finite marked modal measurable space in the sense of Bezhanishvili, de Groot, and Moss. Let \(Z\) be the union of all sets in the modal sigma-ideal \(N\). Since \(\Sigma\) is finite, \(Z\in N\), and
\[
N=\{A\in\Sigma:A\subseteq Z\}.
\]
Let \(Y\) be the set of Boolean atoms of \(\Sigma\) not contained in \(Z\).

For atoms \(P,Q\) of \(\Sigma\), write \(P\rightsquigarrow Q\) when
\[
P\subseteq \Diamond Q.
\]
This is the atom-level relation induced by \(R\). Then:

1. no \(P\in Y\) points to a null atom;
2. every \(P\in Y\) points to at most one atom of \(Y\).

Thus the relation on \(Y\) is the graph of a partial function
\[
f:Y\rightharpoonup Y.
\]
Moreover the quotient complex algebra is canonically isomorphic to
\[
(\Sigma,\Diamond)/N\cong (\mathcal P(Y),f^-1).
\]

Conversely, every finite partial function \(f:Y\rightharpoonup Y\) gives a marked modal measurable space
\[
(Y,\operatorname{graph}(f),\mathcal P(Y),\{\varnothing\})
\]
whose complex algebra is \((\mathcal P(Y),f^-1)\).

Equivalently, a finite modal Boolean algebra has a finite marked-modal-measurable representation exactly when its normal additive operator \(\Diamond\) also preserves binary meets:
\[
\Diamond(a\wedge b)=\Diamond a\wedge\Diamond b.
\]

This gives a smallest finite obstruction. On the four-element Boolean algebra with atoms \(a,b\), define
\[
\Diamond 0=0,\qquad
\Diamond a=a,\qquad
\Diamond b=a,\qquad
\Diamond 1=a.
\]
It is a finite measurable sigma-modal algebra, but
\[
\Diamond a\wedge\Diamond b=a\ne0=\Diamond(a\wedge b).
\]
Therefore it has no finite marked-modal-measurable representation. The modal Loomis-Sikorski representation theorem nevertheless represents it by a marked modal measurable space, so every such representation is necessarily infinite. No two-element algebra is an obstruction.

## Assumptions and scope

A modal measurable space \((X,R,\Sigma)\) has a sigma-field \(\Sigma\) for which \(\Diamond A=\{x:R[x]\cap A\ne\varnothing\}\) is measurable whenever \(A\) is measurable. A marked modal measurable space additionally carries a modal sigma-ideal \(N\) such that for every countable family \((A_n)\),
\[
\bigcap_n A_n\in N
\quad\Longrightarrow\quad
\bigcap_n\Diamond A_n\in N.
\]

The theorem concerns finite \(X\), hence finite \(\Sigma\). The quotient is taken in the modal sigma-algebra sense of the cited paper. The induced partial function acts on the non-null Boolean atoms of \(\Sigma\), not necessarily on the original points of \(X\).

“Finite representation” means a representation by a marked modal measurable space with finite underlying set. The final obstruction statement uses the paper's general modal Loomis-Sikorski representation theorem only for existence of some representation; the finiteness impossibility is proved here.

## Proof

Because \(\Sigma\) is finite, the union \(Z\) of all members of \(N\) is itself in \(N\), and downward closure gives
\[
N=\{A\in\Sigma:A\subseteq Z\}.
\]

Every \(\Diamond Q\) is measurable. Hence for Boolean atoms \(P,Q\), either
\[
P\subseteq\Diamond Q
\]
or
\[
P\cap\Diamond Q=\varnothing.
\]
This makes the atom relation \(\rightsquigarrow\) well-defined.

If \(Q\subseteq Z\), then \(Q\in N\). Since \(N\) is modal, \(\Diamond Q\in N\), so \(\Diamond Q\subseteq Z\). Therefore no non-null atom \(P\in Y\) can satisfy \(P\rightsquigarrow Q\). This proves that non-null atoms have no null successors.

Suppose next that some \(P\in Y\) has two distinct non-null successors \(Q_0,Q_1\in Y\). Set
\[
A_0=Q_0,\qquad A_1=Q_1,\qquad A_n=X\quad(n\ge2).
\]
Since distinct Boolean atoms are disjoint,
\[
\bigcap_n A_n=\varnothing\in N.
\]
But \(P\subseteq\Diamond Q_0\cap\Diamond Q_1\), and the existence of either successor gives \(P\subseteq\Diamond X\). Hence
\[
P\subseteq\bigcap_n\Diamond A_n.
\]
The right-hand side is therefore not in \(N\), contradicting the defining countable-intersection condition. So every \(P\in Y\) has at most one successor in \(Y\). Call it \(f(P)\) when it exists.

Define
\[
\theta:\Sigma/N\longrightarrow\mathcal P(Y)
\]
by
\[
\theta([A])=\{P\in Y:P\subseteq A\}.
\]
Two measurable sets have the same image exactly when their symmetric difference is contained in \(Z\), so \(\theta\) is a Boolean isomorphism. For \(P\in Y\),
\[
P\in\theta([\Diamond A])
\]
holds exactly when \(P\rightsquigarrow Q\) for some atom \(Q\subseteq A\). Such a \(Q\) cannot be null and, by uniqueness, must equal \(f(P)\). Therefore
\[
\theta([\Diamond A])=f^-1(\theta([A])).
\]
This proves the quotient representation.

Conversely, let \(f:Y\rightharpoonup Y\) be finite and use the discrete sigma-field with trivial ideal. If
\[
\bigcap_n A_n=\varnothing
\]
and a point \(y\) belonged to every \(f^-1(A_n)\), then \(f(y)\) would be defined and would belong to every \(A_n\), a contradiction. Thus
\[
\bigcap_n f^-1(A_n)=\varnothing,
\]
so the marked-space condition holds.

For the algebraic characterization, inverse images under a partial function preserve unions, the empty set, and binary intersections. Hence every finite marked-modal-measurable quotient has meet-preserving \(\Diamond\). Conversely, let a finite Boolean algebra carry a normal additive \(\Diamond\) preserving binary meets. On its atoms define \(P\rightsquigarrow Q\) by \(P\le\Diamond Q\). If one atom \(P\) had distinct successors \(Q_0,Q_1\), then
\[
P\le\Diamond Q_0\wedge\Diamond Q_1
=\Diamond(Q_0\wedge Q_1)
=\Diamond0
=0,
\]
impossible. Thus the atom relation is partial-functional, and the preceding discrete construction gives a finite marked-modal-measurable representation.

Finally, a two-element Boolean algebra has only one atom, so every normal additive modal operator is partial-functional. The displayed four-element algebra fails meet preservation and is therefore the smallest obstruction.

## Verification

The argument is symbolic and covers every finite marked modal measurable space.

A bundled checker independently exhausts all binary relations and all principal null ideals on sets of one, two, and three atoms. For each pair it checks the marked-space countable-intersection condition directly: because the measurable algebra is finite, every countable family has the same intersection as a finite family of distinct measurable sets. The checker confirms that the marked-space condition holds exactly when no non-null point reaches a null point and every non-null point has at most one non-null successor.

The exhaustive counts of admissible relation/null-set pairs are
\[
4,\qquad41,\qquad1176
\]
for one, two, and three atoms respectively. The checker also confirms that the explicit two-atom branching relation fails the marked-space condition and that its modal operator fails binary-meet preservation.

These finite computations corroborate the structural proof; they are not used as a substitute for it.

## Relationship to prior work

Bezhanishvili, de Groot, and Moss introduce marked modal measurable spaces and define their complex algebras as quotients \((\Sigma,\Diamond)/N\). Their defining extra condition is exactly the countable-intersection implication used above. They prove a modal Loomis-Sikorski theorem representing every measurable sigma-modal algebra by such a quotient and then derive completeness for their infinitary modal logic.

Their paper also gives a measure-preserving dynamical-system example in which the relation is the graph of a function and \(\Diamond\) is inverse image. The present theorem shows that, in the finite case, this deterministic behavior is not merely an example: after quotienting null atoms it is forced.

The source develops the general representation theorem and infinite measurable semantics, but does not state the finite partial-function classification, the meet-preservation criterion, or the four-element minimal obstruction. Targeted searches for finite marked modal measurable spaces, functional relations, meet preservation, branching obstructions, and finite modal Loomis-Sikorski representations found no equivalent statement.

## Limitations

The collapse is a finite phenomenon. In an infinite sigma-field the null ideal need not be principal, and a non-null measurable region need not contain a non-null Boolean atom, so the atom argument does not extend directly.

The theorem classifies finite marked-modal-measurable quotients, not arbitrary modal measurable spaces without the marked ideal condition. It also does not say that every infinite representation of the four-element obstruction has any particular cardinality beyond being infinite.

The literature search cannot rule out an equivalent observation under different terminology; this is the main residual originality risk.

## References

[1] Nick Bezhanishvili, Jim de Groot, and Lawrence S. Moss, “Modal Measurable Logics via a Modal Loomis-Sikorski Representation Theorem,” *Electronic Proceedings in Theoretical Computer Science* 447 (2026), 158–172. arXiv:2606.31862. DOI:10.4204/EPTCS.447.9.
