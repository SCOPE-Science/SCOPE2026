# Exact multiple-commutator fibers of radical-square-zero quiver algebras

## Finding

Let \(Q=(V,E)\) be a finite directed multigraph with nonempty vertex set, allowing isolated vertices, loops and parallel arrows. Over \(\mathbb F_q\), let \(A=\mathbb F_q Q/J^2\), with \(J\) the arrow ideal in the path algebra. For any integer \(t\ge2\), let \(R_t(c)\) count ordered \(2t\)-tuples \((a_i,b_i)_{i=1}^t\) of elements of \(A\) whose sum of additive associative commutators is \(c\). If \(c\) has a nonzero vertex or loop coefficient, then \(R_t(c)=0\). Otherwise, with \(S\) the set of arrows on which \(c\) is nonzero and \(m=|E|\),
\[
R_t(c)=q^{(2t-1)m}
\sum_{\substack{\kappa:V\to\mathbb F_q^{2t}\\
\kappa(s(e))\ne\kappa(t(e))\ (e\in S)}}
q^{\#\{e\in E:\kappa(s(e))=\kappa(t(e))\}}.
\]
Here \(s(e),t(e)\) denote the endpoints; the exponent counts individual arrows, including every loop. The same result can be written as a single mixed Potts evaluation with \(q^{2t}\) vertex states: expand the equal-color factor for each arrow in \(E\setminus S\) as \(1+(q-1){\bf1}_{\kappa(s(e))=\kappa(t(e))}\). Then
\[
R_t(c)=q^{(2t-1)m}\sum_{F\subseteq E\setminus S}(q-1)^{|F|}\chi_{(G/F)[S]}(q^{2t}),
\]
where \(G\) is the undirected multigraph of all arrows, the contractions identify all vertices in each component of \((V,F)\), and \((G/F)[S]\) retains all resulting vertices and just the edges in \(S\). A loop among those retained edges makes the coloring count zero. In particular the weight \(q-1\) is fixed as the number of pairs grows; replacing \(q\) by \(q^t\) in a single-pair formula would give a different weight and prefactor.

## Proof

Write the diagonal coefficients of \(a_i,b_i\) as \(d_{i,v},f_{i,v}\) and their arrow coefficients as \(x_{i,e},y_{i,e}\). Diagonal products commute and products of two arrows vanish. Thus the coefficient of the sum on \(e:u\to v\) is
\[
\sum_{i=1}^t\big[(d_{i,u}-d_{i,v})y_{i,e}-(f_{i,u}-f_{i,v})x_{i,e}\big].
\]
It vanishes identically on loops; all vertex coefficients also vanish. Collect the diagonal coefficients into the color \(\kappa(v)=(d_{i,v},f_{i,v})_{i=1}^t\). Conditional on the colors, different arrows use disjoint blocks of \(2t\) variables. Equal endpoint colors give all \(q^{2t}\) lifts for a zero target coefficient and none for a nonzero coefficient. Unequal colors give a nonzero linear functional, hence exactly \(q^{2t-1}\) lifts for any specified coefficient. Multiplication and summation give the first expression. In the expansion over \(F\), equality on every edge of \(F\) makes the coloring constant on its components. Inequalities on \(S\) then impose precisely proper coloring of the stated contraction. This proves the second expression in every finite characteristic.

## Scope, use, and prior work

The finding concerns the explicit graph-polynomial count for **multiple** ordered pairs, not the already available chromatic length or one-pair law. The loopless single-pair coloring and contraction formulas, and the minimum-length criterion, are in the indexed findings [Chromatic commutator length and nonzero fibers](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-chromatic-commutator-length-and-nonzero-fibers-of-radical-square--f660f871aa43/RESULT.md) and [Chromatic commutator length and Tutte fibers](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-chromatic-commutator-length-and-tutte-fibers-of-square-zero-quiv--b7fb936d5d53/RESULT.md). The [Kronecker fiber calculation](https://github.com/Resultary/2026/blob/main/2026/10/4/SCOPE-commutator-fibers-and-commuting-probabilities-of-finite-kronecke--75cb49b6c27d/RESULT.md) gives the two-vertex single-pair case, and the Potts expansion is standard (Sokal, arXiv:math/0503607). Adding loops has a simple central direct-factor effect and is not a separate originality claim.

Counting repeated representations by convolution of the single-pair distribution is always possible. The point of the formula here is to evaluate the repeated fiber directly, without traversing intermediate additive targets, by the same support-constrained graph sum as the number of pairs varies. For example, for an orientation of \(K_5\) over \(\mathbb F_2\), any full-support target has one-pair fiber zero but two-pair fiber \(2^{30}\cdot16\cdot15\cdot14\cdot13\cdot12\), since all five diagonal labels must differ and every arrow has three free coefficient bits. The method is an exact expression, not a polynomial-time algorithm for arbitrary graphs. It does not apply to path algebra quotients in which products of arrows need not vanish.

## Verification

Run `python3 verify.py`. The checker independently tabulates every one-pair fiber by multiplying elements in the truncated algebra, performs exact additive convolution to count two- and three-pair fibers, and compares those counts on a small loop-and-parallel-arrow example with direct coloring. It also checks the total tuple counts. The all-parameter claim is proved by the linear equations above, not by the finite check.
