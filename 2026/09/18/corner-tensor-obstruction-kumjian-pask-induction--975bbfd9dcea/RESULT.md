# Corner tensor reduction obstructs hereditary-subgraph freeness in Kumjian–Pask induction

## Result

Let \(A\) be a unital ring, let \(p\in A\) be an idempotent, and put \(B=pAp\), with identity \(p\). For every unital left \(B\)-module \(V\), multiplication gives a natural isomorphism of left \(A\)-modules
\[
A\otimes_B V\;\cong\;Ap\otimes_B V,
\qquad a\otimes v\longmapsto ap\otimes v.
\]
Consequently, if \(a p=0\), then \(a\otimes v=0\) for every \(v\in V\). Moreover, if \(p\ne1\), then \(A\), with the right \(B\)-action induced by inclusion, is not a unital right \(B\)-module and cannot be a free right \(B\)-module. The correct unital corner adjunction is
\[
Ap\otimes_B -\;\dashv\;p(-),
\]
and the induction functor is exact precisely when the right \(B\)-module \(Ap\) is flat.

Applied to finite-vertex Kumjian–Pask algebras, this gives a direct obstruction to Theorem 3.5 of Bich Van Nguyen, *Induced and Restricted Representations of Kumjian–Pask Algebras of Higher-Rank Graphs*, arXiv:2609.20230v1. Let
\[
A=KP_K(\Lambda),\qquad B=KP_K(\Lambda|_H)\cong p_H A p_H,
\qquad p_H=\sum_{v\in H}s_v,
\]
where \(K\) is a field, \(\Lambda^0\) is finite, and \(H\subsetneq\Lambda^0\) is nonempty, hereditary, and saturated. Then \(p_H\ne1\), so \(A\) cannot be free as a right \(B\)-module. In particular, for every vertex \(v\notin H\),
\[
s_vp_H=0,
\]
so the elements \(s_v\) that occur in the proposed transversal of Theorem 3.5 have zero right \(B\)-orbit and satisfy
\[
s_v\otimes_B V=0
\]
for every unital left \(B\)-module \(V\). Thus they cannot be free basis elements.

This correction does **not** show that hereditary-subgraph induction is non-exact. Rather, it identifies the relevant bimodule: exactness of the tensor induction is equivalent to flatness of \(Ap_H\) as a right \(B\)-module. The freeness argument for \(A_B\) in arXiv:2609.20230v1 does not establish that flatness.

## Idempotent-corner lemma

Let \(V\) be a unital left \(B=pAp\)-module. Define
\[
\Phi:A\otimes_BV\to Ap\otimes_BV,
\qquad
\Phi(a\otimes v)=ap\otimes v.
\]
This is balanced: for \(b\in B\), since \(bp=b\) and \(pb=b\),
\[
\Phi(ab\otimes v)=abp\otimes v=ab\otimes v
=apb\otimes v=\Phi(a\otimes bv).
\]
The inclusion \(Ap\hookrightarrow A\) induces
\[
\Psi:Ap\otimes_BV\to A\otimes_BV.
\]
Since \(v=pv\),
\[
\Psi\Phi(a\otimes v)=ap\otimes v=a\otimes pv=a\otimes v,
\]
while \(\Phi\Psi\) is immediate. Hence \(\Phi\) is a natural isomorphism.

For a unital left \(A\)-module \(M\), the usual tensor–Hom argument gives
\[
\operatorname{Hom}_A(Ap\otimes_BV,M)
\cong
\operatorname{Hom}_B(V,pM),
\]
so the correct unital restriction along the corner is \(M\mapsto pM\). If \(p\ne1\), then \(1_A\cdot p=p\ne1_A\); therefore \(A\) with the right multiplication action of \(B\) is nonunital. Every free right \(B\)-module is unital, so \(A_B\) cannot be free. Finally, because \(A\otimes_B-\cong Ap\otimes_B-\), exactness is equivalent to flatness of \(Ap_B\).

## Explicit Kumjian–Pask counterexample

Take the rank-one graph that is the disjoint union of two one-loop components, with vertices \(v,w\). It is row-finite and has no sources. Let \(H=\{w\}\), which is hereditary and saturated. Over a field \(K\),
\[
A\cong K[x,x^{-1}]\oplus K[y,y^{-1}],
\qquad
B\cong K[y,y^{-1}],
\qquad
p_H=(0,1).
\]
The entire first summand has zero right \(B\)-action. Thus \(A_B\) is not free. For every unital left \(B\)-module \(V\),
\[
A\otimes_BV\cong Ap_H\otimes_BV\cong V,
\]
and the outside vertex satisfies \(s_v\otimes_BV=0\). This is a concrete counterexample to the freeness/transversal assertion of Theorem 3.5. Notice that induction is exact in this example, so the example separates failure of the claimed freeness theorem from the independent question of flatness of \(Ap_H\).

## Two further corrections in the same induction setup

### Vertex corners are not generally scalar

Section 3.1 of arXiv:2609.20230v1 states that \(s_vAs_v\cong K\) by (KP3). This is false in general. For the one-vertex one-loop graph,
\[
A\cong K[t,t^{-1}],\qquad s_v=1,
\]
so
\[
s_vAs_v=A\cong K[t,t^{-1}]\ne K.
\]
The paper itself later uses this Laurent-polynomial description in its rank-one example. Vertex-corner induction should therefore be formulated over the actual corner algebra \(C_v=s_vAs_v\):
\[
As_v\otimes_{C_v}N,
\]
not over \(K\) without an additional hypothesis identifying \(C_v\) with \(Ks_v\).

### The unrestricted family of standard monomials is not a basis

Section 2.2 of arXiv:2609.20230v1 states that all monomials \(s_\lambda s_{\mu^*}\) form an \(R\)-basis. The standard construction of Kumjian–Pask algebras gives a spanning family, but the Cuntz–Krieger relation (KP4) creates linear relations among such monomials. For the one-vertex graph with two loops \(e,f\),
\[
s_v=s_es_{e^*}+s_fs_{f^*},
\]
and the three displayed terms are distinct standard monomial elements. Hence the unrestricted monomial family is linearly dependent. The original 2013 Kumjian–Pask paper states a spanning result and uses normal forms; later work obtains bases only after choosing more carefully constrained normal forms in special classes of \(k\)-graphs.

## Consequences for arXiv:2609.20230v1

The following statements in the current v1 require correction:

- Theorem 3.5 is false as stated for proper finite hereditary corners: \(KP_K(\Lambda)\) is not a free right \(KP_K(\Lambda|_H)\)-module under the inclusion action.
- The proposed transversal contains outside-vertex elements whose entire right \(B\)-orbit is zero.
- The proof of exactness in Corollary 3.6 cannot follow from the stated freeness theorem. The general exactness question reduces instead to flatness of \(Ap_H\) over \(p_HAp_H\).
- Under the paper's convention that modules are unital unless stated otherwise, restriction along the nonunital corner inclusion should be \(M\mapsto p_HM\), not all of \(M\).
- The scalar vertex-corner assertion in Section 3.1 and the unrestricted monomial-basis assertion in Section 2.2 are false in general.

No claim is made here that Corollary 3.6 is false for every hereditary saturated \(H\), nor that unrelated results of the paper fail. The correction isolates the algebraic points on which the stated freeness proof and the unital corner formalism depend.

## Prior literature and originality boundary

The identity \(A\otimes_{pAp}V\cong Ap\otimes_{pAp}V\), the adjunction \(Ap\otimes_{pAp}-\dashv p(-)\), and the standard Kumjian–Pask relations are classical ring-theoretic facts and are not claimed as new. Aranda Pino, Clark, an Huef, and Raeburn's foundational construction gives the standard spanning/normal-form framework for Kumjian–Pask algebras. Preusser later studied explicit bases for standard \(k\)-graphs.

The novelty claim is restricted to the application of the corner-tensor reduction to arXiv:2609.20230v1: the universal obstruction to its Theorem 3.5 for proper finite corners, the explicit disjoint-loop counterexample, and the resulting corrected induction/restriction formulation. To the best of our knowledge, targeted searches by title, arXiv identifier, theorem terminology, and equivalent corner/freeness formulations located no prior correction or erratum containing this observation.

## Limitations

The source paper is a recent v1 and may be revised. The correction does not determine whether \(Ap_H\) is flat for every Kumjian–Pask hereditary corner; it only shows that the stated freeness theorem for \(A_B\) is impossible and identifies \(Ap_H\) as the relevant module. The 2018 basis paper was used only as contextual evidence that basis questions require additional normal-form choices; the elementary KP4 relation already suffices to disprove the unrestricted basis assertion.

## References

1. Bich Van Nguyen, *Induced and Restricted Representations of Kumjian–Pask Algebras of Higher-Rank Graphs*, arXiv:2609.20230v1 (2026).
2. Gonzalo Aranda Pino, John Clark, Astrid an Huef, Iain Raeburn, *Kumjian-Pask algebras of higher-rank graphs*, arXiv:1106.4361; Trans. Amer. Math. Soc. 365 (2013).
3. Raimund Preusser, *Bases for Kumjian-Pask algebras over standard k-graphs*, arXiv:1801.00722 (2018).
