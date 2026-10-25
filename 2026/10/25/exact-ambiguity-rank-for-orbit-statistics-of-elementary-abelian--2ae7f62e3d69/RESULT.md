# Exact ambiguity rank for orbit statistics of elementary abelian group actions

## Finding
Let \(G=(C_p)^r\), where \(p\) is prime and \(r\ge2\). For a finite \(G\)-set \(X\), record the number \(M_H(X)\) of \(H\)-orbits for every subgroup \(H\le G\), and the number \(a_d(X)\) of \(G\)-orbits of size \(d\) for every divisor \(d\mid |G|\). Over \(\mathbb Q\), the joint linear statistic on the Burnside group has kernel dimension
\[
\sum_{j=2}^{r}\left(\begin{bmatrix}r\\j\end{bmatrix}_p-1\right),
\]
where \(\begin{bmatrix}r\\j\end{bmatrix}_p\) counts \(j\)-dimensional subspaces of \(\mathbb F_p^r\). Its image has dimension \(\frac{p^r-1}{p-1}+r\).

Moreover, for each \(j\in\{2,\ldots,r-1\}\), choose one reference \(j\)-space \(W_j\). For every other \(j\)-space \(U\), the integral virtual-set relation
\[
R_{U,W_j}=p^{j-1}([G/U]-[G/W_j])
-\sum_{L\le U,\ \dim L=1}[G/L]
+\sum_{L\le W_j,\ \dim L=1}[G/L]
\]
annihilates **all** the recorded statistics. The displayed relations form a \(\mathbb Q\)-basis of the kernel. The positive and negative parts of any such nonzero relation give two explicit nonisomorphic finite \(G\)-sets with identical statistics.

For \(G=(C_2)^3\), the kernel dimension is \(6\), while for \(G=(C_2)^4\) it is \(48\).

## Assumptions and scope
Only finite \(G\)-sets are considered. All subgroups of an elementary abelian group are vector subspaces. The rational Burnside group has basis \([G/K]\) indexed by subspaces \(K\le G\). A virtual relation means a rational linear combination of these basis vectors. Multiplying to clear denominators produces an integral relation; separating positive and negative coefficients produces actual finite \(G\)-sets. The theorem is about the rank, full rational kernel, and explicit integral witnesses, not minimal cardinality of witnesses or integral Smith invariants.

## Proof
Write \(F_H(X)=|X^H|\). Burnside's lemma, together with the fact that all nonidentity elements of \(G\) generate lines, gives
\[
M_H(X)=\frac{F_0(X)+(p-1)\sum_{L\le H,\dim L=1}F_L(X)}{|H|}.
\]
Conversely \(F_0=M_0\), and for each line \(L\), \(F_L=(pM_L-F_0)/(p-1)\). Hence all subgroup-orbit counts are equivalent to the \(1+\begin{bmatrix}r\\1\end{bmatrix}_p\) fixed-point marks for the zero subgroup and the lines. These marks are independent because on \([G/0]\) and \([G/L]\) their matrix is triangular with nonzero diagonal.

Write \(x_K\) for the coefficient of \([G/K]\), and \(j=\dim K\). The orbit-size statistics are precisely \(A_j=\sum_{\dim K=j}x_K\) for \(0\le j\le r\), since \(|G/K|=p^{r-j}\). On the joint kernel, \(A_j=0\) for every \(j\ge2\). Conversely, choose any values \(x_K\) in dimensions at least two satisfying these separate zero-sum conditions. The line fixed-point equations uniquely determine
\[
x_L=-\sum_{K\supseteq L,\ \dim K\ge2}p^{1-\dim K}x_K.
\]
The trivial-subgroup mark then uniquely determines \(x_0\); in fact it forces \(x_0=0\), because each \(j\)-space contains exactly \(\begin{bmatrix}j\\1\end{bmatrix}_p\) lines and \(A_j=0\) for each \(j\ge2\). Therefore the higher-dimensional coefficients may be chosen freely subject only to one sum constraint in each dimension \(j\ge2\). This proves the stated kernel dimension, and subtracting from the total number \(\sum_{j=0}^r\begin{bmatrix}r\\j\end{bmatrix}_p\) of subspaces gives the image dimension.

For the explicit relations, a transitive set \([G/K]\) has \(p^{r-j}\) fixed points under a line \(L\) exactly when \(L\le K\), and otherwise has zero. Consequently \(p^{j-1}([G/U]-[G/W_j])\) has line marks \(p^{r-1}(\mathbf1_{L\le U}-\mathbf1_{L\le W_j})\), precisely canceled by the displayed line-orbit terms. Its total cardinality also vanishes because both \(j\)-spaces contain the same number of lines. All \(A_j\) vanish: the two \(j\)-space coefficients cancel, as do the two sums of line-orbit coefficients. Thus every statistic vanishes. Independence is immediate by examining the distinct nonreference \(j\)-space coordinates, and their number equals the previously computed kernel dimension.

## Verification
The standalone script `checker.py` constructs all subgroups of \((C_p)^r\), exactly computes every orbit-count row using \(M_H(G/K)=|G|/|H+K|\), and checks the joint rank and an explicit relation. It successfully checks \((p,r)=(2,2),(2,3),(2,4),(3,2),(3,3)\); all calculations use integer matrices and exact rational rank. These finite cases are corroboration, not a replacement for the proof for all primes and dimensions.

## Relationship to prior work
Gull, Illidge, Mudrak, Park and Phagan (arXiv:2610.16880, first publicly posted 2026-10-12) establish a qualitative injectivity criterion for precisely these two families of orbit statistics across finite abelian groups. The present result is restricted to elementary abelian groups and supplies a complete *quantitative* rational ambiguity space, its exact dimension, and a uniform explicit basis of integral relations. Classical Burnside-ring and Brauer-relation theory already identifies the cyclic-subgroup fixed-point character, used here as an input rather than asserted as new.

## Limitations
The full text of arXiv:2610.16880 was not accessible during this comparison; the qualitative conclusion is verified from its public abstract, but it remains possible that its proof or appendices already imply or state this exact rational basis. The result does not compute the saturated integral lattice, Smith invariants, or minimum witness sizes. This is not an independent certification.

## References
1. C. Gull, A. Illidge, B. Mudrak, J. Park, S. Phagan, *On a Combinatorial Characterization of Abelian Group Actions*, arXiv:2610.16880 (2026-10-12), https://arxiv.org/abs/2610.16880.
2. Standard Burnside-ring fixed-point/character correspondence: https://ncatlab.org/nlab/show/permutation+representation.
3. A. Bartel and T. Dokchitser, *Brauer relations in finite groups II*, arXiv:1110.6618, https://arxiv.org/abs/1110.6618 (comparison with general character-kernel theory).
