# Isolated-unit criterion for isotropy embeddings in Steinberg algebras

Let \(\mathcal G\) be a Hausdorff ample groupoid, let \(R\neq 0\) be a commutative ring with identity, let \(A=A_R(\mathcal G)\), and fix \(x\in\mathcal G^{(0)}\). Write \(G_x=\mathcal G_x^x\) for the isotropy group and \(B=R[G_x]\).

## Theorem

The singleton-function assignment
\[
\delta_\gamma\longmapsto \mathbf 1_{\{\gamma\}}\qquad(\gamma\in G_x)
\]
lands in \(A\) for every \(\gamma\in G_x\), and hence defines an injective \(R\)-algebra homomorphism \(B\to A\), **if and only if \(x\) is isolated in \(\mathcal G^{(0)}\)**.

When \(x\) is isolated, put \(e_x=\mathbf 1_{\{x\}}\). Then the image is exactly the corner
\[
B\cong e_xAe_x.
\]
Moreover
\[
Ae_x\cong R[s^{-1}(x)]
\]
as an \(A\)-\(B\) bimodule, and \(Ae_x\) is a free right \(B\)-module. Consequently the correct unital corner adjunction is
\[
Ae_x\otimes_B-\ \dashv\ e_x(-),
\]
i.e.
\[
\operatorname{Hom}_A(Ae_x\otimes_B W,M)
\cong
\operatorname{Hom}_B(W,e_xM).
\]
The induction functor \(Ae_x\otimes_B-\) is exact over every coefficient ring \(R\), not only over fields.

## Proof

If the displayed singleton assignment lands in \(A\), then in particular \(\mathbf 1_{\{x\}}\in A\). Steinberg-algebra elements are locally constant. Since \(R\neq0\), the values \(0\) and \(1\) are distinct, so the inverse image of \(1\) under \(\mathbf 1_{\{x\}}\) is the singleton \(\{x\}\), which must be open. Hence \(x\) is isolated.

Conversely, assume \(x\) is isolated. For any \(\gamma\in G_x\), choose an open bisection \(U\ni\gamma\). Because \(s|_U\) is injective and \(\{x\}\) is open,
\[
U\cap s^{-1}(\{x\})=\{\gamma\}.
\]
Thus \(\{\gamma\}\) is open; it is compact because \(\mathcal G\) is Hausdorff. Hence it is a compact-open bisection and \(\mathbf 1_{\{\gamma\}}\in A\). Convolution of these singleton functions is group multiplication, and distinct singleton functions are \(R\)-linearly independent, giving the embedding.

For the corner statement, left and right multiplication by \(e_x\) cuts a Steinberg function down to arrows with range and source both equal to \(x\). Thus every element of \(e_xAe_x\) is supported in \(G_x\). Because every element of \(G_x\) is isolated, compact support there is finite, so the corner consists exactly of finite \(R\)-linear combinations of isotropy singletons. This is \(R[G_x]\).

Similarly, \(Ae_x\) consists exactly of finitely supported functions on \(s^{-1}(x)\). The right action of \(G_x\) on \(s^{-1}(x)\) is free. Choosing one arrow from each right \(G_x\)-orbit gives a decomposition
\[
R[s^{-1}(x)]\cong\bigoplus_{i\in I} R[G_x]
\]
as right \(B\)-modules. Hence \(Ae_x\) is free, and the corner tensor-Hom adjunction follows by the standard maps
\[
\Phi\mapsto(w\mapsto\Phi(e_x\otimes w)),
\qquad
\psi\mapsto(ae_x\otimes w\mapsto a\psi(w)).
\]
Freeness gives exactness.

## Consequence for arXiv:2609.20230v1

Section 4.1 of B. V. Nguyen, *Induced and Restricted Representations of Kumjian--Pask Algebras of Higher-Rank Graphs*, defines for every boundary path \(x\)
\[
\iota_x(u^p)=\mathbf 1_{\{(x,p,x)\}}
\]
and Proposition 4.1 asserts that this gives an embedding of the isotropy group algebra into the Steinberg algebra. The paper itself defines its Steinberg algebra as locally constant, compactly supported functions. The theorem above shows that Proposition 4.1 is false for every nonisolated \(x\).

There is a second, independent corner issue even when \(x\) is isolated. The identity of \(R[G_x]\) maps to \(e_x\), not generally to the identity or a global local unit acting as the identity on an arbitrary unital \(A\)-module. Therefore the paper's Definition 4.2, which takes the whole module \(M\) as a unital \(R[G_x]\)-module by restriction along \(\iota_x\), is not well-defined in its stated unital module category unless \(e_xM=M\). The natural corner restriction is \(M\mapsto e_xM\), and its left adjoint is \(Ae_x\otimes_B-\).

Accordingly, the inclusion-based restriction framework of Section 4 requires an isolation hypothesis and a corner correction. Statements depending on the unrestricted map \(\iota_x\) require reformulation; this observation does not by itself assert that every later conclusion is false.

## Explicit rank-one counterexample

Let \(E\) be the directed graph with one vertex and two loops \(a,b\), and let \(\mathcal G_E\) be its boundary-path groupoid. Take
\[
x=aaaa\cdots.
\]
Then \(G_x\cong\mathbb Z\), since every shift of \(x\) equals \(x\). But \(x\) is not isolated: every cylinder \(Z(a^n)\) also contains, for example, \(a^nbaaaa\cdots\). Therefore
\[
\mathbf 1_{\{(x,0,x)\}},\quad \mathbf 1_{\{(x,1,x)\}}
\notin A_R(\mathcal G_E).
\]
Thus the proposed embedding already fails for the Leavitt path algebra of the two-loop graph.

The criterion is sharp. For the one-vertex one-loop graph there is a unique infinite path, hence it is isolated, and the construction reduces to the familiar identification with \(R[t,t^{-1}]\).

The unital-module issue is also visible in a finite graph: take the disjoint union of two one-loop graphs. For the infinite path \(x\) in the first component,
\[
A\cong R[t,t^{-1}]\oplus R[s,s^{-1}],\qquad
B\cong R[t,t^{-1}]\cong e_xAe_x.
\]
On the regular unital \(A\)-module \(M=A\), the identity of \(B\) acts as \(e_x=(1,0)\), not as the identity on the second summand. Thus the whole \(M\) is not a unital \(B\)-module, whereas \(e_xM\) is.

## Relation to established isotropy induction

The obstruction concerns realizing an isotropy group algebra as a singleton-supported subalgebra of the Steinberg algebra. It does **not** obstruct the standard Steinberg induction construction. For arbitrary \(x\), one uses the free module on the source fibre \(R[s^{-1}(x)]\), which is an \(A_R(\mathcal G)\)-\(R[G_x]\) bimodule, and forms
\[
R[s^{-1}(x)]\otimes_{R[G_x]}V.
\]
This source-fibre induction is established prior literature and does not require \(x\) to be isolated. The 2020 paper of Q. L. Nguyen and B. V. Nguyen explicitly studies the graded form of Steinberg's isotropy induction, and Demeneghi's work also develops isotropy induction for Steinberg algebras. The new point here is the sharp isolation criterion for the singleton embedding and its application to the inclusion-based framework of arXiv:2609.20230v1.

## Limitations and originality scope

The singleton criterion is elementary once the locally constant definition of a Steinberg algebra is used, and it may be implicit in foundational groupoid-algebra literature. The originality claim is therefore deliberately narrow: to the best of our knowledge, no prior source located in the literature search identifies the failure of Proposition 4.1 of arXiv:2609.20230v1, gives the exact isolated-unit boundary for that claimed embedding, and separates it from the additional unital corner issue in Definition 4.2.

No claim is made here about the correctness of the paper's independent induction results from vertex corners or hereditary subgraphs. For nonisolated isotropy, the appropriate general theory is the established source-fibre bimodule construction rather than a singleton subalgebra inclusion.

## References

1. B. V. Nguyen, *Induced and Restricted Representations of Kumjian--Pask Algebras of Higher-Rank Graphs*, arXiv:2609.20230v1 (2026), especially Sections 2.5 and 4.1--4.2. https://arxiv.org/abs/2609.20230v1
2. Q. L. Nguyen and B. V. Nguyen, *On induced graded simple modules over graded Steinberg algebras with applications to Leavitt path algebras*, arXiv:2006.09931 (2020). https://arxiv.org/abs/2006.09931
3. P. Demeneghi, *The Ideal Structure of Steinberg Algebras*, Advances in Mathematics 352 (2019), 777--835; arXiv:1710.09723. https://arxiv.org/abs/1710.09723
