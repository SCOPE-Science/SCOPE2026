# Corner units obstruct the claimed Kumjian–Pask freeness theorem

## Result

Let \(A\) be a nonzero unital ring, let \(e\in A\) be an idempotent, and put
\[
B=eAe,
\]
viewed as a unital ring with identity \(e\). If \(e\neq 1_A\), then the ambient ring
\(A\), with its natural right action by \(B\), is **not** a unital right
\(B\)-module and therefore cannot be a free right \(B\)-module in the usual
unital module category.

More precisely,
\[
AB=Ae,\qquad (1-e)B=0,
\]
and \(Ae\neq A\) whenever \(e\neq 1_A\). Consequently the correct induction
bimodule attached to the corner is \(Ae\), not all of \(A\).

Applied to a finite-vertex row-finite \(k\)-graph \(\Lambda\) with no sources,
a nonempty hereditary saturated subset \(H\subsetneq\Lambda^0\), and
\[
A=KP_R(\Lambda),\qquad
e=p_H=\sum_{v\in H}s_v,\qquad
B=KP_R(\Lambda|_H)\cong eAe,
\]
this gives a universal obstruction to Theorem 3.5 of
B. V. Nguyen, *Induced and Restricted Representations of Kumjian--Pask
Algebras of Higher-Rank Graphs*, arXiv:2609.20230v1. That theorem claims, over
a field, that \(A\) is a free right \(B\)-module. For every proper nonempty
\(H\) in the finite-vertex setting above, \(e\neq1_A\), so the claimed
freeness is impossible.

The sharp finite-vertex boundary is therefore:
\[
A_B\text{ can be a unital free right }B\text{-module}
\quad\Longleftrightarrow\quad
H=\Lambda^0,
\]
apart from the degenerate zero-ring case.

## Proof of the corner obstruction

For \(b\in B=eAe\),
\[
ab=aeb\in Ae,
\]
so \(AB\subseteq Ae\). Conversely, \(ae=a\cdot e\in AB\), hence
\[
AB=Ae.
\]
Also
\[
(1-e)b=(1-e)eae=0,
\]
so \((1-e)B=0\).

If \(Ae=A\), then \(1_A=ae\) for some \(a\in A\). Multiplying by \(e\) on the
right gives
\[
e=1_Ae=(ae)e=ae=1_A,
\]
a contradiction when \(e\neq1_A\). Thus \(Ae\neq A\).

A unital right \(B\)-module \(M\) must satisfy \(Me=M\). Here
\[
Ae=AB\neq A,
\]
so \(A_B\) is not unital. In particular it cannot be a free right module over
the unital ring \(B\), because every ordinary free \(B\)-module is unital.

## Correct corner induction and restriction

Although \(A_B\) is not the correct unital bimodule, tensor induction written
with \(A\) automatically discards the offending summand. For every unital
left \(B\)-module \(V\), there is a natural isomorphism
\[
A\otimes_B V\;\cong\;Ae\otimes_B V
\]
given by
\[
a\otimes v\longmapsto ae\otimes v.
\]
Indeed \(v=ev\), so in the balanced tensor product
\[
a\otimes v=a\otimes ev=ae\otimes v.
\]
The inverse is induced by the inclusion \(Ae\hookrightarrow A\).

For every unital left \(A\)-module \(M\), the corresponding unital corner
restriction is
\[
M\longmapsto eM,
\]
and the standard corner adjunction is
\[
\operatorname{Hom}_A(Ae\otimes_B V,M)
\;\cong\;
\operatorname{Hom}_B(V,eM).
\]
The forward map sends an \(A\)-map \(F\) to
\(v\mapsto F(e\otimes v)\); the inverse sends a \(B\)-map \(\psi:V\to eM\) to
\[
ae\otimes v\longmapsto a\psi(v).
\]
Thus the induction object in the source paper can be repaired canonically,
but the restriction functor should land in \(eM\), not in the whole \(M\),
when one works in the stated category of unital modules.

This corrected formulation is also consistent with the paper's later Morita
equivalence discussion, which uses \(Ap_H\) for induction and \(p_H(-)\) for
restriction.

## A minimal rank-one counterexample

Take the \(1\)-graph consisting of two disjoint vertices \(v,w\), with one
loop at each vertex. Over a field \(k\),
\[
A\cong k[x,x^{-1}]\oplus k[y,y^{-1}].
\]
Let \(H=\{w\}\). It is hereditary and saturated, and
\[
B\cong k[y,y^{-1}],\qquad e=s_w=(0,1).
\]
Then
\[
s_vB=0,\qquad s_ve=0,
\]
so \(A_B\) is not even unital and cannot be free. This already contradicts
the asserted theorem within the rank-one subclass of Kumjian--Pask algebras.

The source paper's own two-vertex example displays the same corner effect.
For its \(H=\{w\}\) and the unital \(B\)-module \(V=R\), an alleged induced
basis vector is written as \(s_v\otimes1\). But \(1=e\cdot1\) in \(V\), while
orthogonality of distinct vertex idempotents gives \(s_ve=s_vs_w=0\). Hence
\[
s_v\otimes1=s_v\otimes(e\cdot1)
=(s_ve)\otimes1=0.
\]
So that displayed vector cannot be part of a basis.

## A second diagnostic in the freeness proof

The same preprint states that all monomials
\(s_\lambda s_{\mu^*}\) form an \(R\)-basis. In general they only give a
spanning family: the Kumjian--Pask relation
\[
s_v=\sum_{\lambda\in v\Lambda^n}
s_\lambda s_{\lambda^*}
\]
is already a nontrivial linear dependence whenever \(v\Lambda^n\) has more
than one path. Thus an argument for a transversal basis cannot infer linear
independence merely from distinct monomials.

This observation is not needed for the corner-unit contradiction above; it
independently identifies why the proposed transversal proof cannot establish
the stated freeness theorem as written.

## What is and is not corrected

The obstruction disproves the freeness assertion for every proper nonempty
finite-vertex hereditary saturated corner. It also shows that restriction of
an arbitrary unital \(A\)-module to all of \(M\) along \(B\hookrightarrow A\)
does not, in general, produce a unital \(B\)-module; \(eM\) is the canonical
repair.

The argument does **not** show that the induced functor is non-exact. Since
\[
A\otimes_B-\cong Ae\otimes_B-,
\]
exactness is controlled by the right \(B\)-module \(Ae\). The present result
does not determine whether \(Ae\) is flat or free for every hereditary
saturated \(H\); consequently it does not by itself refute any exactness
statement that might admit a different proof.

Likewise, no claim is made here about infinite vertex sets, where \(p_H\) may
have to be handled with local units rather than as a single global
idempotent.

## Literature and originality boundary

The corner identity \(B=eAe\), Peirce decomposition, the bimodule \(Ae\), and
the adjunction
\[
Ae\otimes_{eAe}-\dashv e(-)
\]
are standard ring and Morita theory; they are not claimed as new. Related
graph-algebra Morita theory is also established in L. O. Clark,
A. an Huef, and P. Luiten-Apirana, *Subsets of vertices give Morita
equivalences of Leavitt path algebras*, Bull. Aust. Math. Soc. 96 (2017),
212--222, arXiv:1701.03178.

The new claim here is narrowly the application of this corner-unit
obstruction to arXiv:2609.20230v1: its Theorem 3.5 cannot hold for any proper
nonempty hereditary saturated corner in the finite-vertex setting, its
displayed rank-two induced basis contains a zero vector, and the natural
unital correction is to use \(Ap_H\) and \(p_HM\). To the best of our
knowledge, no public correction or erratum stating this obstruction was
located as of the publication date. The preprint currently lists only v1.

Because the source is recent and the correction follows from standard corner
theory once the unit mismatch is noticed, an independent or subsequent
author correction remains a significant originality risk.

## References

1. B. V. Nguyen, *Induced and Restricted Representations of Kumjian--Pask
   Algebras of Higher-Rank Graphs*, arXiv:2609.20230v1.
   https://arxiv.org/abs/2609.20230v1
2. L. O. Clark, A. an Huef, P. Luiten-Apirana, *Subsets of vertices give
   Morita equivalences of Leavitt path algebras*, Bull. Aust. Math. Soc. 96
   (2017), 212--222, arXiv:1701.03178.
   https://arxiv.org/abs/1701.03178
