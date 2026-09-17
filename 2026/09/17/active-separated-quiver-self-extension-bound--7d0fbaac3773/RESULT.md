# An active-separated-quiver refinement of the \(3s+1\) self-extension bound

## Result

Let \(A\) be a basic split finite-dimensional \(k\)-algebra, let \(J=\operatorname{rad}A\), and assume
\[
J^3=0.
\]
Choose primitive orthogonal idempotents \(e_1,\ldots,e_s\), and write
\[
S_i=Ae_i/Je_i,\qquad B=A/J^2,\qquad \mathfrak r=J/J^2.
\]
Thus \(B\) is basic split with radical square zero.

Define the radical-incidence matrix
\[
E_{ji}=[\,\mathfrak r(Be_i):S_j\,].
\]
Let
\[
\kappa=\#\{i:\text{column }i\text{ of }E\text{ is nonzero}\},
\qquad
\rho=\#\{j:\text{row }j\text{ of }E\text{ is nonzero}\}.
\]
Equivalently, \(\kappa+\rho\) is the number of non-isolated vertices of the separated quiver of \(B\).

Because \(J^3=0\), each \(J^2e_i\) is semisimple. Form a bipartite graph \(\Gamma_2(A)\) with left vertices \(1,\ldots,s\), right vertices the isomorphism classes of nonprojective simple \(A\)-modules, and an edge
\[
i\longdash j
\quad\Longleftrightarrow\quad
[\,J^2e_i:S_j\,]>0.
\]
Let \(\nu=\nu(\Gamma_2(A))\) be its maximum matching number.

### Theorem

If \(M\in{}^\perp A\), meaning
\[
\operatorname{Ext}_A^q(M,A)=0\qquad(q>0),
\]
and
\[
\operatorname{Ext}_A^q(M,M)=0
\qquad
(1\le q\le \kappa+\rho+\nu+1),
\]
then \(M\) is projective.

Equivalently, every nonprojective semi-Gorenstein-projective \(A\)-module has a nonzero self-extension in some degree
\[
1\le q\le \kappa+\rho+\nu+1.
\]

Since \(\kappa,\rho,\nu\le s\),
\[
\kappa+\rho+\nu+1\le 3s+1.
\]
Thus this is an algebra-sensitive refinement of the \(3s+1\) bound of Zhang--Zhou. It is strict whenever
\[
\kappa+\rho+\nu<3s.
\]
It is not a new smaller worst-case constant: when all three parameters equal \(s\), it reproduces \(3s+1\).

For an arbitrary split finite-dimensional algebra, the same statement applies after passing to a basic Morita equivalent algebra; the orthogonality and self-extension conditions, as well as projectivity, are preserved by the equivalence.

## Proof

Assume, toward a contradiction, that \(M\in{}^\perp A\) is nonprojective and that
\[
\operatorname{Ext}_A^q(M,M)=0
\qquad
(1\le q\le L),
\qquad
L=\kappa+\rho+\nu+1.
\]

Zhang--Zhou, Proposition 2.3, gives pairwise nonisomorphic indecomposable nonprojective modules
\[
X_0,\ldots,X_{L-1}
\]
such that
\[
X_0\mid\Omega_A M,\qquad
X_{i+1}\mid\Omega_A X_i,
\]
each \(X_i\) belongs to \({}^\perp A\), each inherits the same self-extension vanishing range, and
\[
\underline{\operatorname{Hom}}_A(X_j,X_i)=0,
\qquad
\operatorname{Ext}_A^1(X_j,X_i)=0
\quad(j>i).
\]
Moreover \(J^2X_i=0\), so every \(X_i\) is naturally a \(B=A/J^2\)-module.

We first add one more syzygy term. Choose an indecomposable nonprojective summand
\[
X_L\mid\Omega_A X_{L-1}.
\]
Such a summand exists because \(X_{L-1}\in{}^\perp A\) is nonprojective. The modules
\[
X_0,\ldots,X_L
\]
are still pairwise nonisomorphic. Indeed, for \(i<L\),
\[
X_L\mid\Omega_A^{L-i}X_i,
\]
and \(L-i\le L\). Dimension shifting gives
\[
\underline{\operatorname{Hom}}_A(\Omega_A^{L-i}X_i,X_i)
\cong
\operatorname{Ext}_A^{L-i}(X_i,X_i)=0.
\]
If \(X_L\cong X_i\), the projection from the indicated direct summand would force the identity of \(X_i\) to factor through a projective, contradicting the nonprojectivity of \(X_i\).

Now count the terms among \(X_0,\ldots,X_{L-1}\) that are projective as \(B\)-modules. Let their number be \(p\). Each such term has the form
\[
X_i\cong Be_{a(i)}.
\]
Because the \(X_i\) are pairwise nonisomorphic, the vertices \(a(i)\) are distinct. Since \(X_i\) is not projective over \(A\), one has \(J^2e_{a(i)}\ne0\), and the natural map
\[
Ae_{a(i)}\twoheadrightarrow Be_{a(i)}
\]
is its projective cover. Hence
\[
\Omega_A X_i\cong J^2e_{a(i)}.
\]
The chosen successor \(X_{i+1}\) is therefore an indecomposable nonprojective summand of the semisimple module \(J^2e_{a(i)}\). Consequently
\[
X_{i+1}\cong S_{b(i)}
\]
for a nonprojective simple \(S_{b(i)}\), and \(a(i)\longdash b(i)\) is an edge of \(\Gamma_2(A)\).

The extra module \(X_L\) is essential when \(i=L-1\). Because the entire list \(X_0,\ldots,X_L\) is pairwise nonisomorphic, the right vertices \(b(i)\) belonging to distinct \(B\)-projective terms are distinct. The left vertices \(a(i)\) are also distinct. Thus these edges form a matching in \(\Gamma_2(A)\), and
\[
p\le\nu.
\]

Retain from \(X_0,\ldots,X_{L-1}\) only the terms that are nonprojective over \(B\). Their number \(R\) satisfies
\[
R\ge L-\nu=\kappa+\rho+1.
\]

Let \(H\) be the separated algebra of \(B\). Its separated quiver has vertices
\[
1^+,\ldots,s^+,\;1^-,\ldots,s^-,
\]
with arrows \(i^+\to j^-\) according to the entries \(E_{ji}\). A plus vertex \(i^+\) is isolated exactly when column \(i\) of \(E\) is zero, and a minus vertex \(j^-\) is isolated exactly when row \(j\) is zero. Deleting all isolated vertices gives a hereditary algebra \(H_{\mathrm{act}}\) with exactly
\[
\kappa+\rho
\]
simple modules.

For every retained indecomposable nonprojective \(B\)-module \(X\), the separated-algebra functor \(F\) of Zhang--Zhou sends \(X\) to an indecomposable nonprojective \(H\)-module. Such an \(F(X)\) has zero component on every isolated vertex. Indeed, \(H\) is the direct product of the path algebra of the active subquiver and one copy of \(k\) for each isolated vertex; a nonzero isolated component would split off a projective simple summand, contradicting indecomposability and nonprojectivity. Hence the retained \(F(X)\)'s may be regarded as modules over \(H_{\mathrm{act}}\).

Inflation from \(B\) to \(A\), followed by Zhang--Zhou Proposition 3.3 and Corollary 3.7, transfers the triangular vanishing relations to the retained modules \(Y_0,\ldots,Y_{R-1}\):
\[
\operatorname{Ext}_{H_{\mathrm{act}}}^1(Y_j,Y_i)=0
\quad(j\ge i),
\qquad
\operatorname{Hom}_{H_{\mathrm{act}}}(Y_j,Y_i)=0
\quad(j>i).
\]
Zhang--Zhou Lemma 3.8 says that over a finite-dimensional hereditary algebra with \(N\) simple modules, a sequence of nonzero modules with these relations has length at most \(N\). Therefore
\[
R\le\kappa+\rho,
\]
contradicting \(R\ge\kappa+\rho+1\). Hence \(M\) is projective.

## A companion refinement beyond Loewy length three

The same active-separated-quiver count also sharpens Zhang--Zhou Proposition 4.3.

Let \(A\) now be any basic split finite-dimensional algebra, with no assumption \(J^3=0\). Put \(B=A/J^2\), define \(\kappa,\rho\) from the radical-incidence matrix of \(B\), and set
\[
\delta=\#\{i:J^2e_i\ne0\}.
\]
Suppose \(M\in{}^\perp A\) and there is \(n_0\ge0\) such that
\[
J^2\Omega_A^nM=0\qquad(n\ge n_0).
\]
If
\[
\operatorname{Ext}_A^q(M,M)=0
\qquad
(1\le q\le \kappa+\rho+\delta+1),
\]
then \(M\) is projective.

Indeed, apply the finite orthogonal-sequence construction to a sufficiently high syzygy, exactly as in Zhang--Zhou Proposition 4.3. Among the resulting pairwise nonisomorphic \(B\)-modules, a \(B\)-projective term \(Be_i\) can fail to be \(A\)-projective only when \(J^2e_i\ne0\). Hence at most \(\delta\) terms are lost before passing to the separated algebra. At least \(\kappa+\rho+1\) nonprojective \(B\)-terms remain, while the active separated algebra has only \(\kappa+\rho\) simple modules, yielding the same contradiction.

This companion statement improves the source bound \(3s+1\) whenever
\[
\kappa+\rho+\delta<3s.
\]

## Relation to prior work

Zhang and Zhou, *The Auslander--Reiten conjecture for algebras with radical cube zero* (arXiv:2609.08679v1, submitted 8 September 2026), prove the uniform bound \(3s+1\). Their proof discards at most \(s\) terms that become projective over \(A/J^2\), then applies a hereditary length bound to a separated algebra with \(2s\) simple modules. They explicitly state that \(3s+1\) is not claimed optimal and leave improvement of the estimate as a question.

The refinement above tightens both counts appearing in that argument:

1. the hereditary rank is the number \(\kappa+\rho\) of non-isolated separated-quiver vertices, rather than all \(2s\) vertices; and
2. for \(J^3=0\), the number of discarded \(A/J^2\)-projective terms is bounded by the matching number \(\nu\) of the second radical layer, rather than by \(s\).

The matching step uses one additional nonprojective syzygy summand so that a projective term in the final position of the length-\(L\) sequence also has a controlled successor.

This result does not supersede sharper theorems in special classes. Ringel--Zhang prove that a nonprojective semi-Gorenstein-projective module over a short local algebra already has a nonzero self-extension in degree one. Ringel--Xiong give a stronger projectivity criterion for connected non-self-injective radical-square-zero rings under finite vanishing against the regular module. Xu and Hoshino establish other special radical-cube-zero cases.

## Originality and limitations

To the best of our knowledge, the specific bound
\[
\kappa+\rho+\nu+1
\]
and its active-separated-quiver/second-layer-matching proof do not appear in the literature checked. The closest source is the very recent Zhang--Zhou preprint, whose proof supplies the ingredients refined here but uses the coarser counts \(s\) and \(2s\).

The result is an algebra-sensitive refinement, not a uniform reduction below \(3s+1\): the worst case \(\kappa=\rho=\nu=s\) gives the original bound. Existing special classes can have substantially sharper bounds.

The full text of Hoshino's 1989 paper *On algebras with radical cube zero* was not inspected. Accessible bibliographic and later-source descriptions indicate related radical-cube-zero results, but they do not rule out unnoticed overlap with an older formulation. Because arXiv:2609.08679 is also very recent, contemporaneous independent discovery remains a residual originality risk.

## References

- X. Zhang and P. Zhou, *The Auslander--Reiten conjecture for algebras with radical cube zero*, arXiv:2609.08679v1 (2026). https://arxiv.org/abs/2609.08679
- C. M. Ringel and B.-L. Xiong, *On radical square zero rings*, Algebra and Discrete Mathematics 14 (2012), 297--306; arXiv:1112.1422. https://arxiv.org/abs/1112.1422
- C. M. Ringel and P. Zhang, *Gorenstein-projective modules over short local algebras*, Journal of the London Mathematical Society 106 (2022), 528--589. https://doi.org/10.1112/jlms.12577
- D. M. Xu, *A Note on the Auslander--Reiten Conjecture*, Acta Mathematica Sinica, English Series 29 (2013), 1993--1996. https://doi.org/10.1007/s10114-013-1428-5
- M. Hoshino, *On algebras with radical cube zero*, Archiv der Mathematik 52 (1989), 226--232. https://doi.org/10.1007/BF01194384
