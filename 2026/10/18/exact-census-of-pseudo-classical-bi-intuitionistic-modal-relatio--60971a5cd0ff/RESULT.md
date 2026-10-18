# Exact census of pseudo-classical bi-intuitionistic modal relations on finite rooted stars

## Finding

**Theorem.** Let \(m\geq 2\). On the rooted-star partial order \(P_m=\{r\}\cup L\), where \(|L|=m\), the only strict comparabilities are \(r<\ell\) for \(\ell\in L\). Let \(R\subseteq P_m\times P_m\) satisfy the forth–up and forth–down confluence conditions of pseudo-classical bi-intuitionistic modal frames. There is a three-case row normal form described below. The exact number of relations on this fixed, leaf-labelled order is

\[
\mathcal L_m=2^m+(2^{m+1}-1)^m+2^m\bigl((1+2^m)^m-2^{m^2}\bigr).
\]

There is also an explicit partition-indexed Burnside formula for the number \(\mathcal U_m\) of isomorphism classes, with isomorphisms preserving the order and the accessibility relation. For a partition \(\lambda=(d_1,\ldots,d_c)\vdash m\), put

\[
g_i=\sum_{j=1}^c\gcd(d_i,d_j),\qquad G=\sum_{i=1}^c g_i,\qquad z_\lambda=\prod_{a\geq1}a^{b_a}b_a!,
\]

where \(b_a\) is the multiplicity of part \(a\) in \(\lambda\). Then

\[
\mathcal U_m=\sum_{\lambda\vdash m}\frac{1}{z_\lambda}\left[2^c+\prod_{i=1}^c\bigl(2^{1+g_i}-1\bigr)+2^c\left(\prod_{i=1}^c\bigl(1+2^{g_i}\bigr)-2^G\right)\right].
\]

For \(m=2,3,4,5,6\), the corresponding labelled counts are \(89,5119,1211297,1171027327,4624635403649\), and the isomorphism counts are \(50,940,53170,9968880,6472894706\), respectively.

## Assumptions and scope

A frame is a triple \((P_m,\leq,R)\). Write \(R(x)=\{y:xRy\}\) for the successor row. The relation \(R\) is **forth–up confluent** when

\[
x\leq x'\ \land\ xRy\quad\Longrightarrow\quad \exists y'\geq y\ (x'Ry'),\]

and **forth–down confluent** when

\[
x\leq x'\ \land\ x'Ry\quad\Longrightarrow\quad \exists y'\leq y\ (xRy').\]

The theorem imposes no reflexivity, seriality, symmetry or transitivity condition on \(R\). In particular this counts the base \(\mathbf{KbI}\) frame class, not one of its stronger modal extensions. The root and all leaves are distinguishable only as dictated by the order: in the labelled count, each leaf has its own fixed label; in the isomorphism count, leaf permutations are allowed.

Define \(S=R(r)\) and \(U=S\cap L\). The complete, disjoint normal form is as follows.

1. If \(r\notin S\), choose any \(U\subseteq L\), take \(S=U\), and set \(R(\ell)=U\) for every leaf.
2. If \(S=\{r\}\), choose independently a **nonempty** subset \(R(\ell)\subseteq P_m\) for every leaf.
3. If \(r\in S\) and \(U\ne\varnothing\), choose any nonempty \(U\subseteq L\), take \(S=\{r\}\cup U\), and independently choose \(U\subseteq R(\ell)\subseteq P_m\) for every leaf.

## Proof

**Row normal form.** The only nontrivial source-order comparisons are \(r\leq\ell\). For a leaf target \(u\in U\), the only world above \(u\) is \(u\) itself. Forth–up applied to \(rRu\) therefore forces \(\ell Ru\) for every leaf \(\ell\), so \(U\subseteq R(\ell)\). If \(r\in S\), forth–up applied to \(rRr\) requires each \(R(\ell)\) to be nonempty. For forth–down, an edge \(\ell Ry\) is covered by a target \(y'\leq y\) in \(S\): if \(r\in S\) this is automatic because \(r\leq y\); otherwise \(y\) cannot be the root, and for a leaf target we must have \(y\in S=U\). Thus, when \(r\notin S\), all leaf rows equal \(U\). Conversely, each of the three specified families satisfies both confluence conditions by the same checks. The families are disjoint and exhaustive.

**Labelled count.** Case 1 admits \(2^m\) choices for \(U\). Case 2 admits \((2^{m+1}-1)^m\) independent nonempty successor rows. In case 3, a fixed nonempty \(U\) of size \(u\) leaves \(m+1-u\) optional target worlds in each leaf row; hence it gives \(2^{m(m+1-u)}\) relations. Summing over \(u=1,\ldots,m\) gives

\[
\sum_{u=1}^m\binom{m}{u}2^{m(m+1-u)}
=2^m\left((1+2^m)^m-2^{m^2}\right).
\]

Adding all three cases proves the labelled formula.

**Isomorphism classes.** Every order automorphism fixes \(r\) and permutes \(L\), so the automorphism group is \(S_m\). Fix a permutation \(\sigma\) with leaf-cycle lengths \(d_1,\ldots,d_c\). Its invariant root rows are unions of leaf cycles, together with an optional root. Case 1 therefore gives \(2^c\) fixed relations. In case 2, the row at the first leaf of a cycle of length \(d_i\) must be a nonempty subset invariant under \(\sigma^{d_i}\); the other rows in that cycle are forced equivariantly. On the target set \(P_m\), the map \(\sigma^{d_i}\) has one root orbit and \(\sum_j\gcd(d_i,d_j)=g_i\) leaf orbits. This yields \(2^{1+g_i}-1\) choices per source cycle and thus the product in the formula.

In case 3, let \(U\) be the union of a nonempty collection \(I\) of leaf cycles. For a source cycle of length \(d_i\), the invariant leaf row must include \(U\) and has \(2^{1+g_i-\sum_{j\in I}\gcd(d_i,d_j)}\) possibilities. Multiplying over source cycles gives \(2^{c+G-\sum_{j\in I}g_j}\). Summing over the nonempty selections \(I\) gives

\[
2^c\left(\prod_{j=1}^c(1+2^{g_j})-2^G\right).
\]

These three terms constitute the number of relations fixed by \(\sigma\). Burnside's lemma sums them over all leaf permutations. Grouping permutations by cycle type \(\lambda\), whose conjugacy class has size \(m!/z_\lambda\), establishes the claimed partition-indexed formula. This holds for every \(m\geq2\) and does not depend on finite experimental extrapolation.

## Verification

The standalone, standard-library-only script `verify.py` independently checks the original confluence quantifiers for **every** relation on \(P_m\) when \(m=1,2,3\); it also directly canonizes those relations under every leaf permutation and compares with the formulas. A separate checker enumerates the invariant root rows and all admissible leaf-row choices under each permutation, using the original quantifiers rather than the closed formula, through \(m=5\). The symbolic formulas are then evaluated through \(m=6\). Run `python verify.py` using Python 3.9 or later; success prints `VERIFY_OK`. The proof, not the finite checks, establishes the formulas for arbitrary \(m\).

## Relationship to prior work

Fernández-Duque, McLean and Zenger (2023, Definition 4 and Definition 5) introduce the two confluence requirements and the \(\mathbf{KbI}\) class and establish soundness, strong completeness, decidability and the finite-frame property for related logics. They do not give the above rooted-star row classification, labelled census or orbit formula in the inspected article. Stell, Schmidt and Rydeheard (2016, Definition 5) use the different stability condition \(H;R;H\subseteq R\) for their bi-intuitionistic modal framework; that condition is not the pair of forth-confluence conditions counted here. Previously published finite-chain frame enumerations likewise concern different underlying posets and cannot imply the branching-star orbit formula from their chain-specific statements. These comparisons concern the stated results; absence of an indexed matching result is not a proof of global novelty.

## Limitations

This theorem concerns finite rooted stars with one least point and \(m\) incomparable maximal points, for the base two-forth-condition relation class only. It does not enumerate modal relations satisfying additional seriality, reflexivity or transitivity, and does not enumerate arbitrary finite partial orders. All finite exhaustive verification is bounded to the specified sizes; no independent external mathematical audit has been performed. The possibility of an equivalent classification under other terminology or in sources not indexed by the searches remains open.

## References

1. D. Fernández-Duque, B. McLean and L. Zenger, *A Family of Decidable Bi-intuitionistic Modal Logics*, Proceedings of KR 2023, pp. 262–271, DOI: 10.24963/kr.2023/26. Open paper: https://proceedings.kr.org/2023/26/kr2023-0026-fernandez-duque-et-al.pdf.
2. J. G. Stell, R. Schmidt and D. Rydeheard, *A Bi-Intuitionistic Modal Logic: Foundations and Automation*, Journal of Logical and Algebraic Methods in Programming **85** (2016), 500–519, DOI: 10.1016/j.jlamp.2015.11.003. Author-accepted full text: https://eprints.whiterose.ac.uk/id/eprint/91427/8/1-s2.0-S2352220815001406-main.pdf.
