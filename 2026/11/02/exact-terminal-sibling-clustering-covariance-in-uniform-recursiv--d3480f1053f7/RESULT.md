# Exact terminal-sibling clustering covariance in uniform recursive trees

## Finding

Let \(T_n\) be the **rooted** uniform random recursive tree on labels \(1,\ldots,n\), where vertex \(j\ge2\) independently chooses a uniformly random parent in \(\{1,\ldots,j-1\}\). A terminal vertex is a vertex having no children. Let \(L_v(n)\) be the number of terminal children of vertex \(v\), and define
\[
X_n=\sum_{v=1}^n L_v(n),\qquad
Y_n=\sum_{v=1}^n\binom{L_v(n)}2.
\]
Thus \(X_n\) counts terminal vertices, while \(Y_n\) counts **unordered pairs of terminal siblings**, allowing a parent with three terminal children to contribute three pairs. For every integer \(n\ge5\), the exact (not just asymptotic) mean vector and covariance matrix are
\[
\boxed{\quad
\mathbb E\binom{X_n}{Y_n}=n\binom{1/2}{1/6},\qquad
\operatorname{Cov}\binom{X_n}{Y_n}
=n\begin{pmatrix}1/12&1/8\\1/8&59/180\end{pmatrix}.
\quad}
\]
Consequently the correlation is identically \(3\sqrt{15}/(2\sqrt{59})\) for every \(n\ge5\), and the covariance matrix is strictly positive definite, with determinant \(101n^2/8640\). Both normalized counts converge in \(L^2\) to their corresponding mean densities.

The structural ingredient is an entire exact family: with \(F_{n,r}=\sum_v\binom{L_v(n)}r\), for every integer \(r\ge1\) and \(n\ge r+1\),
\[
\boxed{\mathbb E F_{n,r}=\frac{n}{(r+1)!}.}
\]
In particular, \(F_{n,1}=X_n\), \(F_{n,2}=Y_n\), and \(\mathbb E F_{n,3}=n/24\) for \(n\ge4\). The third count is needed to close the second moment of the sibling-pair statistic. The first-moment family is included as a proof ingredient; the main finding is the exact second-order joint law.

## Assumptions and scope

The probability space consists of independent attachment choices \(P_j\sim\operatorname{Unif}\{1,\ldots,j-1\}\) for all \(2\le j\le n\). The root is vertex \(1\); all other vertices have exactly one parent. A vertex is terminal precisely when its number of children is zero. These *rooted* terminal vertices must not be conflated with the degree-one vertices of the underlying unrooted tree: for instance, the root can have graph degree one while still having a child. The result holds without asymptotic limits, for all integers \(n\ge5\), and it makes no assertion of a central limit theorem or a full distribution for \(Y_n\).

## Proof

Write \(\mathcal F_n=\sigma(P_2,\ldots,P_n)\). For a nonnegative integer \(r\), set \(F_{n,r}=\sum_{v\le n}\binom{L_v(n)}r\), with \(F_{n,0}=n\). When a new vertex attaches to a parent \(u\), its new terminal-child relationship increases \(L_u\) by one. If \(u\) was itself terminal, it simultaneously ceases to be a terminal child of its own parent, decreasing that parent's terminal-child count by one. These are the only possible changes; this also handles a root with one child because the root is not a terminal child for \(n\ge2\).

For any fixed \(r\ge1\), the increase of \(\binom{L_u}{r}\) on direct attachment is \(\binom{L_u}{r-1}\). The decrease when one of a vertex's \(L_v\) terminal children is chosen is \(\binom{L_v-1}{r-1}\). Summing over the \(n\) equally likely attachment choices yields, for \(n\ge2\),
\[
\mathbb E\big[F_{n+1,r}-F_{n,r}\mid\mathcal F_n\big]
=\frac{F_{n,r-1}-rF_{n,r}}n,
\tag{1}
\]
because \(L\binom{L-1}{r-1}=r\binom Lr\). For \(r=1\), \(F_{n,0}=n\) and \(F_{2,1}=1\) give \(\mathbb E F_{n,1}=n/2\) for \(n\ge2\). Inductively for \(r\ge2\), \(F_{r,r}=0\), while the previous moment at size \(r\) equals \(r/r!\). Thus (1) gives \(\mathbb E F_{r+1,r}=1/r!\). Substitution into (1) then proves \(\mathbb E F_{n,r}=n/(r+1)!\) for all \(n\ge r+1\). This proves the stated factorial-moment family.

Now abbreviate \(X=X_n\), \(Y=Y_n\), and \(Z=F_{n,3}\). Denote one-step changes by \(\Delta X=X_{n+1}-X_n\) and \(\Delta Y=Y_{n+1}-Y_n\). For a chosen terminal parent, \(\Delta X=0\); otherwise \(\Delta X=1\). Hence
\[
\mathbb E[\Delta X\mid\mathcal F_n]=1-X/n,
\qquad \mathbb E[(\Delta X)^2\mid\mathcal F_n]=1-X/n.
\tag{2}
\]
For a chosen nonterminal parent \(v\), \(\Delta Y=L_v\). For a chosen terminal child of \(v\), \(\Delta Y=-(L_v-1)\). These cases are disjoint and exhaust the choices. Since \(\sum_vL_v=X\), \(\sum_vL_v(L_v-1)=2Y\), and \(\sum_vL_v(L_v-1)^2=6Z+2Y\), summing increments and their products over possible parents gives
\[
\begin{aligned}
\mathbb E[\Delta Y\mid\mathcal F_n]&=(X-2Y)/n,\\
\mathbb E[\Delta X\Delta Y\mid\mathcal F_n]&=X/n,\\
\mathbb E[(\Delta Y)^2\mid\mathcal F_n]&=(X+4Y+6Z)/n.
\end{aligned}
\tag{3}
\]
The \(X+4Y+6Z\) term accounts for multiple terminal children sharing the same parent; treating sibling-pair appearances as independent would omit this indispensable overlap term.

Set \(A_n=\mathbb E X_n^2\), \(B_n=\mathbb E[X_nY_n]\), and \(C_n=\mathbb E Y_n^2\). Expanding squares and products with (2)--(3), and writing \(x_n=\mathbb E X_n\), \(y_n=\mathbb E Y_n\), \(z_n=\mathbb E Z_n\), yields the **exact triangular recurrence**
\[
\begin{aligned}
A_{n+1}&=(1-2/n)A_n+2x_n+1-x_n/n,\\
B_{n+1}&=(1-3/n)B_n+A_n/n+y_n+x_n/n,\\
C_{n+1}&=(1-4/n)C_n+2B_n/n+(x_n+4y_n+6z_n)/n.
\end{aligned}
\tag{4}
\]
The small-tree initial values are \(A_3=5/2\), \(B_4=11/6\), and \(C_5=7/3\). They follow directly from (2)--(4) starting with the deterministic two-vertex tree and can also be enumerated over the \((n-1)!\) recursive trees. With \(x_n=n/2\), \(y_n=n/6\), \(z_n=n/24\) in their respective ranges, direct substitution and induction in (4) give
\[
A_n=n^2/4+n/12\quad(n\ge3),\qquad
B_n=n^2/12+n/8\quad(n\ge4),\qquad
C_n=n^2/36+59n/180\quad(n\ge5).
\tag{5}
\]
Subtracting the products of the means proves the covariance matrix. Its determinant is \(n^2(59/2160-1/64)=101n^2/8640>0\). The stated correlation follows by dividing \(n/8\) by the square root of \((n/12)(59n/180)\). The \(L^2\) limits follow from dividing the exact variances by \(n^2\). Every identity has been proved for the entire stated integer range, not extrapolated from finite sampling.

## Verification

A standalone standard-library checker is included as `checker.py`. It enumerates **every** rooted recursive tree for each \(2\le n\le8\), checks the factorial-moment family, first and second moments, and tests each conditional-increment identity on every tree of sizes \(2\le n\le7\). It also verifies the closed second-moment polynomials against the recurrences for every integer \(5\le n\le200\), using exact rational arithmetic, and checks positive definiteness. It completed 5,017 assertions successfully. This finite checker supports, but does not replace, the inductive proof of (1)--(5).

## Relationship to prior work

Hartle and Krapivsky, *Statistics of leaves in growing random trees* (2025), give the limiting one-vertex leaf-degree distribution and its factorial moments, and study the marginal leaf count. Their leaf degree counts leaf neighbors in the **unrooted** graph; our terminal-child count is root-oriented and removes the primordial boundary discrepancy. Their marginal formulas imply the leading expectation \(\mathbb E Y_n\sim n/6\), but not the global exact variance \(59n/180\) or its covariance \(n/8\) with terminal count: these involve dependence between different vertices' leaf-child counts. Hartle and Krapivsky, *Leaves of preferential attachment trees* (2026), compute related one-vertex joint degree/leaf-degree laws and selected count fluctuations for **preferential attachment**, but not the present recursive-tree aggregate variance. Stepanyants et al., *The rank and layer distributions in random recursive trees* (2026), study rank/layer means and self-averaging, not unordered terminal sibling-pair fluctuations. Gopaladesikan, Mahmoud, and Ward (2013) derive covariance and central limits for **fringe motif counts**; sibling pairs in this finding can occur at parents with arbitrary additional children, so they are not a single fixed fringe motif, and their paper does not give this exact covariance. More general additive-functional results could conceivably subsume parts of the argument; no definitive global historical-priority claim is made.

## Limitations

The proof treats the uniform-parent, one-child-per-arrival rooted recursive tree; it does not cover preferential attachment, unrooted degree-one leaf counts without a root correction, or alternative cherry statistics in binary phylogenetic trees. It establishes exact means, variances, and covariance, not a Gaussian limit or a full generating function for the pair count. The finite checker is supplementary and not a certificate for an infinite theorem. Historical originality remains subject to independent literature review; the formulas are not claimed to be unpublished in every possible source.

## References

1. Harrison Hartle and P. L. Krapivsky, *Statistics of leaves in growing random trees*, arXiv:2511.04085v1 (first public posting 2025-11-06), https://arxiv.org/html/2511.04085v1 .
2. Harrison Hartle and P. L. Krapivsky, *Leaves of preferential attachment trees*, arXiv:2602.01021v1 (2026-02-01), https://arxiv.org/html/2602.01021v1 .
3. Huck Stepanyants, P. L. Krapivsky, Harrison Hartle, and Dmitri Krioukov, *The rank and layer distributions in random recursive trees*, arXiv:2608.04303 (2026-08-05), https://arxiv.org/abs/2608.04303 .
4. Mohan Gopaladesikan, Hosam Mahmoud, and Mark Daniel Ward, *Asymptotic Joint Normality of Counts of Uncorrelated Motifs in Recursive Trees*, Methodology and Computing in Applied Probability 16 (2014), 863--884; online 2013-03-29, https://doi.org/10.1007/s11009-013-9333-z .
