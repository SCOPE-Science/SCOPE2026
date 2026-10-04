# Exact finite-volume rung kernel and boundary-bulk split for weighted ladder spanning trees

## Finding

Let \(L_n=P_2\square P_n\) have columns \(1,\ldots,n\). Give every horizontal rail edge weight \(1\) and every vertical rung weight \(c>0\), and sample a spanning tree with probability proportional to the product of its edge weights. Define
\[
\alpha=c+1-\sqrt{c^2+2c}\in(0,1),\qquad
\rho=\frac{1-\alpha}{1+\alpha}.
\]
If \(X_i\) records whether rung \(i\) is present, then the entire finite rung process is determinantal. Its symmetric kernel is, for \(1\le i\le j\le n\),
\[
K^{(n)}_{ij}
=\rho\,\alpha^{j-i}
\frac{(1+\alpha^{2i-1})(1+\alpha^{2(n-j)+1})}{1-\alpha^{2n}},
\qquad K^{(n)}_{ji}=K^{(n)}_{ij}.
\]
Consequently, for every \(S\subseteq\{1,\ldots,n\}\),
\[
\Pr(X_i=1\ \hbox{for all }i\in S)=\det K^{(n)}_S.
\]
In particular,
\[
\Pr(X_i=1)=
\rho\frac{(1+\alpha^{2i-1})(1+\alpha^{2(n-i)+1})}{1-\alpha^{2n}},
\]
and for distinct rungs
\[
\operatorname{Cov}(X_i,X_j)=-(K^{(n)}_{ij})^2.
\]

The one-rung probabilities are symmetric under \(i\mapsto n+1-i\) and strictly decrease from either boundary toward the center; when \(n\) is even the two central values coincide. The two natural thermodynamic limits differ:
\[
\lim_{n\to\infty}K^{(n)}_{11}=1-\alpha,
\qquad
K^{(n)}_{ii}\longrightarrow \rho
\quad\hbox{if }i\to\infty\hbox{ and }n-i\to\infty.
\]
For the unweighted ladder \(c=1\), \(\alpha=2-\sqrt3\), so the endpoint limit is \(\sqrt3-1\), while the bulk density is \(1/\sqrt3\). The exact finite kernel therefore makes explicit the boundary/bulk distinction that is hidden if only one limiting regime is considered.

## Assumptions and scope

The graph is the ordinary finite two-rail ladder \(P_2\square P_n\), \(n\ge1\). Rail weights are \(1\), rung weights are the common positive number \(c\), and the tree law is the standard weighted spanning-tree law. The statement concerns only rung indicators. It does not claim a new transfer-current theorem, a new infinite-volume ladder process, or a new formula for the total weighted number of spanning trees.

## Proof

Orient every rung from the lower to the upper rail. Inject one unit of current at the upper endpoint of rung \(j\) and remove one unit at its lower endpoint. By reflection antisymmetry, if \(d_k\) is the upper-minus-lower voltage difference in column \(k\), then for \(n\ge2\)
\[
B_n d=2e_j,
\]
where \(B_n\) is tridiagonal with off-diagonal entries \(-1\), endpoint diagonal entries \(1+2c\), and interior diagonal entries \(2+2c\). The current through rung \(i\) is \(c\,d_i\), so the rung transfer-current kernel is
\[
K^{(n)}=2c\,B_n^{-1}.
\]

The parameter \(\alpha\) obeys
\[
\alpha+\alpha^{-1}=2(c+1),
\qquad
2c=\frac{(1-\alpha)^2}{\alpha}.
\]
Let \(p_0=1\), and for \(k\ge1\) let \(p_k\) be the determinant of the leading \(k\times k\) block before the right endpoint is imposed. Then
\[
p_1=1+2c,\qquad
p_k=(2+2c)p_{k-1}-p_{k-2},
\]
hence
\[
p_k=\frac{\alpha^{-k}+\alpha^{k+1}}{1+\alpha}.
\]
The full determinant is
\[
D_n=\det B_n
=\frac{(1-\alpha)(1-\alpha^{2n})}{\alpha^n(1+\alpha)}.
\]
The standard inverse formula for a symmetric tridiagonal matrix gives, for \(i\le j\),
\[
(B_n^{-1})_{ij}=\frac{p_{i-1}p_{n-j}}{D_n}.
\]
Multiplying by \(2c\) and simplifying yields the claimed kernel. For \(n=1\), the single rung is present with probability one, and the same closed formula equals one.

The transfer-current theorem for weighted spanning trees now gives every principal-minor inclusion probability. For two distinct rungs, the \(2\times2\) determinant immediately yields
\[
\operatorname{Cov}(X_i,X_j)=-(K^{(n)}_{ij})^2.
\]

For the marginal profile, apart from the positive constant \(\rho/(1-\alpha^{2n})\),
\[
K^{(n)}_{ii}\propto
1+\alpha^{2n}+\alpha^{2i-1}+\alpha^{2n-2i+1}.
\]
This expression is invariant under \(i\mapsto n+1-i\), and
\[
K^{(n)}_{ii}-K^{(n)}_{i+1,i+1}
\propto
(1-\alpha^2)
\left(\alpha^{2i-1}-\alpha^{2n-2i-1}\right)>0
\]
whenever \(i<n/2\). This proves the boundary-to-center monotonicity. Taking endpoint and bulk limits in the explicit kernel gives \(1-\alpha\) and \(\rho\), respectively.

## Verification

The proof is exact and does not depend on computation. As an independent finite check, `verify_ladder_kernel.py` enumerates every weighted spanning tree for \(1\le n\le5\) at rung weights \(c=1\), \(c=2\), and \(c=3/2\). For every nonempty subset of rungs it compares the exact weighted inclusion probability, using rational arithmetic, with the corresponding principal determinant of \(2cB_n^{-1}\). It also compares every kernel entry with the closed \(\alpha\)-formula. The replay returns `VERIFY_OK`.

## Relationship to prior work

Burton and Pemantle's transfer-current theorem supplies the general determinantal law for spanning-tree edges; that theorem is used here rather than claimed anew. Panova and Wilson (arXiv:1407.3748, first posted 14 July 2014) develop exact spanning-tree probability formulas in a statistical-mechanics setting and list \(82B20\) as a primary MSC classification.

Lyons and Peres, *Probability on Trees and Networks* (2016), use the finite unweighted ladder as an introductory example: the bottom-rung probabilities begin \(1\), \(3/4\), \(11/15\), \(41/56\) and converge to \(\sqrt3-1\). Klenke (arXiv:1704.00182) later gives the infinite weighted-ladder rung process explicitly: with the same parameter \(\alpha\), its stationary determinantal kernel is
\[
K^{(\infty)}_{ij}=\rho\,\alpha^{|i-j|},
\]
and he also gives the total weighted spanning-tree count for a finite ladder. The formula above is the finite-volume transfer-current kernel with both endpoint corrections retained. It specializes to the Lyons--Peres endpoint limit and converges in the bulk to Klenke's stationary kernel.

The inspected sources did not state the displayed finite-volume kernel, its exact multiplicative two-boundary correction, or the resulting boundary/bulk split as one theorem.

## Limitations

The novelty claim is deliberately narrow. The result is an exact finite-volume completion of known general transfer-current theory and known ladder limits, not a new spanning-tree framework. The derivation uses the special two-rail symmetry and common rung weight; nonuniform rung weights or wider strips require a different inverse problem. A residual literature risk remains because the formula is short enough to be derivable from standard tridiagonal Green-function methods even if it has not been explicitly recorded in the sources inspected.

## References

1. R. Burton and R. Pemantle, “Local Characteristics, Entropy and Limit Theorems for Spanning Trees and Domino Tilings Via Transfer-Impedances,” *Annals of Probability* 21 (1993), 1329–1371, DOI: 10.1214/aop/1176989121.
2. G. Panova and D. B. Wilson, “Pfaffian formulas for spanning tree probabilities,” arXiv:1407.3748; *Combinatorics, Probability and Computing* 26 (2017), 118–137, DOI: 10.1017/S0963548316000183.
3. R. Lyons and Y. Peres, *Probability on Trees and Networks*, Cambridge University Press, 2016, DOI: 10.1017/9781316672815.
4. A. Klenke, “The Random Spanning Tree on Ladder-like Graphs,” arXiv:1704.00182 (2017).
5. N. Gantert and A. Klenke, “Biased Random Walk on Spanning Trees of the Ladder Graph,” arXiv:2210.07859; *Journal of Statistical Physics* 190, 83 (2023), DOI: 10.1007/s10955-023-03091-w.
