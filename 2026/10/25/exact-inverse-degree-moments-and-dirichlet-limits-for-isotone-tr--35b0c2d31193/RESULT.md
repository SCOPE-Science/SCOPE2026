# Exact inverse-degree moments and Dirichlet limits for isotone transformation monoids

## Finding
Fix an integer \(r\ge2\). Let \(\mathcal O_n\) be the monoid of all nondecreasing maps from the finite chain \([n]\) to itself, and draw \(\alpha\) uniformly among the rank-\(r\) elements (\(n\ge r\)). Let
\[
V(\alpha)=\{\beta\in\mathcal O_n:\alpha\beta\alpha=\alpha,\;\beta\alpha\beta=\beta\},\qquad X_{n,r}=|V(\alpha)|.
\]
Here juxtaposition denotes composition in either fixed convention; both displayed inverse identities are convention-invariant.

**Exact local degree and all finite moments.** If the consecutive nonempty kernel intervals of \(\alpha\) have lengths \(\lambda_1,\ldots,\lambda_r\), and its increasing image is \(b_1<\cdots<b_r\), then
\[
|V(\alpha)|=\Bigl(\prod_{i=1}^{r}\lambda_i\Bigr)\Bigl(\prod_{i=1}^{r-1}(b_{i+1}-b_i)\Bigr).
\tag{1}
\]
For every integer \(k\ge0\), define \(H_k(z)=\sum_{j\ge0}(j+1)^kz^j\). Then
\[
\mathbb E[X_{n,r}^k]=\frac{[z^{n-r}]H_k(z)^r\;[z^{n-r}](1-z)^{-2}H_k(z)^{r-1}}{\binom{n-1}{r-1}\binom nr}.
\tag{2}
\]
In particular,
\[
\mathbb E[X_{n,r}]=\frac{\binom{n+r-1}{2r-1}^{2}}{\binom{n-1}{r-1}\binom nr}.
\tag{3}
\]
This determines all moments for every finite \(n,r\) without enumerating the transformations.

**Distributional limit, with explicit moments.** Let \(P=(P_1,\ldots,P_r)\) have the uniform Dirichlet law on the \((r-1)\)-simplex; independently let \(Q=(Q_0,\ldots,Q_r)\) have the uniform Dirichlet law on the \(r\)-simplex. Then, as \(n\to\infty\) with \(r\) fixed,
\[
\frac{X_{n,r}}{n^{2r-1}}\Longrightarrow
Y_r=\prod_{i=1}^r P_i\prod_{j=1}^{r-1}Q_j,
\tag{4}
\]
and all nonnegative integer moments converge, with
\[
\mathbb E[Y_r^k]=
\frac{(r-1)!(k!)^{r}}{(r+kr-1)!}\cdot
\frac{r!(k!)^{r-1}}{(r+k(r-1))!}.
\tag{5}
\]
The law is nonconstant and positive almost surely; its support has supremum \(r^{-r}(r-1)^{-(r-1)}\). In particular,
\[
\mathbb E[X_{n,r}]\sim \frac{(r-1)!r!}{((2r-1)!)^2}\,n^{2r-1}.
\tag{6}
\]
For \(r=2\), \(Y_2\) has the explicit product representation \(U(1-U)W\), where \(U\) is uniform on \([0,1]\), \(W\) has the \(\operatorname{Beta}(1,2)\) law, and these variables are independent. Its mean is \(1/18\).

**Sharp finite maximum.** Write \(n=ru+s\), \(0\le s<r\), and \(n-1=(r-1)v+t\), \(0\le t<r-1\). Then
\[
\max_{\operatorname{rank}(\alpha)=r}|V(\alpha)|=
 u^{r-s}(u+1)^s\,v^{r-1-t}(v+1)^t.
\tag{7}
\]
The maximizers are exactly maps with kernel lengths differing by at most one, image endpoints \(1,n\), and successive image gaps differing by at most one. The statement is meaningful for every \(n\ge r\ge2\), including \(n=r\).

## Assumptions and scope
The semigroup is the full monoid of *all* weakly order-preserving self-transformations of a linearly ordered \(n\)-element set. The inverse set is the semigroup-theoretic inverse set (not inverse functions). Rank means image cardinality. The restriction \(r\ge2\) avoids the degenerate constant-map limit; at rank one the inverse count is identically \(n\). The asymptotic fixes \(r\) before sending \(n\) to infinity; no conclusion for growing \(r\) is asserted. The Dirichlet distributions above have all concentration parameters equal to one.

## Proof
**1. Parameter space and inverse criterion.** Every rank-\(r\) isotone map is specified uniquely by its ordered kernel intervals \(A_1<\cdots<A_r\), of positive lengths \(\lambda_i\) summing to \(n\), and its ordered image \(b_1<\cdots<b_r\), with \(\alpha(A_i)=b_i\). There are \(\binom{n-1}{r-1}\) choices for the composition \((\lambda_i)\) and independently \(\binom nr\) choices for the image. Thus these parameters are independent and uniform when \(\alpha\) is uniform at rank \(r\).

An inverse \(\beta\) must have rank \(r\). Its image is an ordered transversal of the intervals \(A_i\), since \(\alpha\beta\alpha=\alpha\) forces \(\alpha(\beta(b_i))=b_i\), and \(\beta\alpha\beta=\beta\) together with monotonicity forces the output values of \(\beta\) to meet every \(A_i\). Conversely, a rank-\(r\) isotone map \(\beta\) is a mutual inverse if its image is an ordered transversal of the kernel of \(\alpha\) and the image \(\{b_1,\ldots,b_r\}\) is an ordered transversal of the kernel of \(\beta\). Indeed, the first condition makes \(\alpha\) bijective on the image of \(\beta\), and the second makes \(\beta\) bijective on the image of \(\alpha\); these bijections are inverses to one another, establishing both semigroup identities. This is the crossed-transversal criterion for combinatorial regular Green classes, specialized here directly to isotone maps.

The image of \(\beta\) can be chosen in \(\prod_i\lambda_i\) ways. To choose the kernel of \(\beta\), take a cut after \(c_i\) for \(i=1,\ldots,r-1\). The condition that \(b_i\) belongs to the \(i\)-th interval is exactly \(b_i\le c_i<b_{i+1}\). The cut choices are automatically strictly increasing and independent, giving \(\prod_{i=1}^{r-1}(b_{i+1}-b_i)\) kernels. Their ordered images and kernels specify \(\beta\) uniquely. This proves (1).

**2. Exact moments.** For each fixed positive integer composition \((\lambda_i)\) of \(n\) into \(r\) parts, the length product raised to the \(k\)-th power contributes \(\prod_i\lambda_i^k\). Its sum over all compositions is \([z^{n-r}]H_k(z)^r\), since a part \(\lambda_i=1+j_i\) contributes \((1+j_i)^kz^{j_i}\).

For an image \(b_1<\cdots<b_r\), use the nonnegative endpoint gaps \(h_0=b_1-1\), \(h_r=n-b_r\), and nonnegative internal gaps \(h_i=b_{i+1}-b_i-1\) for \(1\le i<r\). These satisfy \(h_0+\cdots+h_r=n-r\), while the image-gap product equals \(\prod_{i=1}^{r-1}(h_i+1)\). Summing its \(k\)-th power over all images gives the second coefficient in (2). Independence of the kernel and image parameters proves (2). For \(k=1\), the identity \(H_1(z)=(1-z)^{-2}\) makes both numerator coefficients equal to \([z^{n-r}](1-z)^{-2r}=\binom{n+r-1}{2r-1}\), proving (3). The same computation for \(k=0\) yields the denominator and confirms normalization.

**3. Limit law.** The uniform weak composition of \(n-r\) into \(r+1\) parts, divided by \(n\), converges to uniform Lebesgue probability on the \(r\)-simplex. To see this without a probabilistic limit theorem, for every continuous test function the normalized sum over the integer simplex is a Riemann sum; boundary cells are negligible. Likewise, the uniform positive composition of \(n\) into \(r\) parts, divided by \(n\), converges to uniform probability on the \((r-1)\)-simplex. Their finite-\(n\) independence implies independent limits \(P,Q\). The product map is continuous, while replacing the normalized internal gaps \(h_i/n\) by \((h_i+1)/n\) changes them by \(1/n\). This proves (4) by the continuous mapping theorem.

The random variables \(X_{n,r}/n^{2r-1}\) are bounded by one, so convergence in law also implies convergence of every nonnegative integer moment. For a \(d\)-component Dirichlet\((1,\ldots,1)\) vector \((Z_i)\), elementary simplex integration gives \(\mathbb E\prod_i Z_i^{a_i}=(d-1)!\prod_i a_i!/(d-1+\sum_i a_i)!\) for nonnegative integers \(a_i\). Apply this to \(P\) with \(r\) exponents \(k\), then to \(Q\) with \(r-1\) exponents \(k\) and two exponents zero; independence gives (5). At \(k=1\), it gives (6); the same follows from (3).

**4. Support and exact extremizers.** AM–GM bounds \(\prod_iP_i\le r^{-r}\) and \(\prod_{j=1}^{r-1}Q_j\le(r-1)^{-(r-1)}\); the second supremum occurs at the boundary where the two unused components \(Q_0,Q_r\) vanish. Dirichlet laws have full support on the relative interior of their simplices. Hence the product distribution is nondegenerate and positive almost surely, with the stated support supremum. For finite \(n\), the product of positive integer kernel lengths at fixed sum \(n\) is maximized exactly when their sizes differ by at most one, by repeated transfers from any part at least two larger than another. The sum of internal positive image gaps is at most \(n-1\), with equality only for \(b_1=1,b_r=n\); balancing the \(r-1\) gaps gives the second factor. Since kernel lengths and image are independent free choices, both maxima are attained simultaneously. This proves (7) and the complete characterization of maximizers.

## Verification
The standalone file `verify_inverse.py` enumerates all weakly increasing self-maps in dimensions \(1\) through \(6\) (respectively \(1,3,10,35,126,462\) maps). For each map it counts inverses directly by testing both composition identities against every map, independently of the kernel-image formula. It checks (1), exact moments (2) for \(k=0,1,2,3\), the expected number (3), and all ranks. Its completed output ends with `VERIFY_OK`. This is a finite check, not a proof of the all-dimensional formulas or convergence.

## Relationship to prior work
Higgins (2026) proves the existence of permutation matchings for \(\mathcal O_n\) by a balanced weighting of the kernel–image transversal matrix. Its proof describes the crossed-square inverse relation but does not enumerate local inverse degrees, compute their rank-conditioned moments, or study their random asymptotic laws. The general inverse-graph and Green-class framework is due to earlier semigroup theory, including Higgins (2014, 2024), and is fully credited. The product criterion in Step 1 should be understood as an explicit specialization of that framework, not as an independent invention. The new object of study is the **entire quantitative rank-conditioned inverse-degree profile**: the explicit all-moment coefficient identity, a nondegenerate Dirichlet-product limit and the finite extremal geometry. A square identity for the total number of ordered mutual-inverse pairs follows formally in arbitrary combinatorial Green classes and is not presented as a standalone novelty claim. No claim about existence of involution matchings follows.

## Limitations
The theorem treats a uniformly chosen map conditioned on fixed rank; it does not handle simultaneous growth of rank and chain size or arbitrary transformation semigroups. The limiting law is given by an explicit product of Dirichlet coordinates, not by a closed elementary density. The literature comparison covers directly relevant full-text sections and targeted indexed searches but cannot establish absolute uniqueness: an unindexed paper may already derive this statistic. Independent validation is not supplied.

## References
1. P. M. Higgins, *Balanced weightings and permutation matchings applied to the monoid of order-preserving mappings*, arXiv:2610.01912, first posted 2026-10-01, Sections 1–3, especially Definition 3.1, Remark 3.2, and Theorem B.
2. P. M. Higgins, *Finite regular semigroups with permutations that map elements to inverses*, Semigroup Forum 109 (2024), 141–147, doi:10.1007/s00233-024-10430-0, Sections 1–2.
3. P. M. Higgins, *Permutations of a semigroup that map to inverses*, Semigroup Forum 89 (2014), 169–182, especially Lemma 2.13 on crossed kernel–image transversals.
