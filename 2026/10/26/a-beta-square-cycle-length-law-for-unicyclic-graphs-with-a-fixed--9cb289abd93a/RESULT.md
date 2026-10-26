# A beta-square cycle-length law for unicyclic graphs with a fixed number of leaves

## Finding
Fix an integer \(r\ge 1\). Let \(G_n\) be uniform among the simple connected labelled unicyclic graphs on \(\{1,\ldots,n\}\) that have exactly \(r\) degree-one vertices, for \(n\ge r+3\). Let \(K_n\) be the length of their unique cycle. Then
\[
(K_n/n)^2\ \xrightarrow{d}\ \operatorname{Beta}(1/2,r)\qquad(n\to\infty,\ r\text{ fixed}).
\]
In particular the limiting density of \(K_n/n\) on \((0,1)\) is
\[
\frac{2}{B(1/2,r)}(1-y^2)^{r-1}.
\]
There is also an exact all-size enumeration. For integers \(3\le k\le n-r\), put \(s=n-k\) and \(F(z)=(e^z-1)/z\), with \(F(0)=1\). The number \(N_{n,k,r}\) of such graphs with cycle length \(k\) is
\[
N_{n,k,r}=\frac{n!}{2}\frac{(s-1)_{r-1}}{r!}
[z^{r-1}]\,e^{kz}F(z)^{s-r},
\]
where \((s-1)_{r-1}=(s-1)(s-2)\cdots(s-r+1)\) is a falling factorial, and \((s-1)_0=1\). For \(k\) outside that range, the count is zero. Thus \(\Pr(K_n=k)=N_{n,k,r}/\sum_{j=3}^{n-r}N_{n,j,r}\).
Two explicit cases are:
\[
N_{n,k,1}=n!/2\quad(3\le k\le n-1),
\]
so the cycle length conditional on exactly one leaf is *exactly uniform* on \(\{3,\ldots,n-1\}\), and
\[
N_{n,k,2}=\frac{n!}{8}(s-1)(2n-s-2)\quad(3\le k\le n-2).
\]

## Assumptions and scope
All graphs are finite, undirected, simple, connected, and labelled. A unicyclic graph contains exactly one simple cycle, necessarily of length at least three. A leaf has degree one. The conditioning class is nonempty exactly when \(n\ge r+3\). The limit keeps \(r\) fixed as \(n\to\infty\); it does not claim an analogous law when the number of leaves grows with \(n\). The beta distribution uses shape parameters \((1/2,r)\).

## Proof
Write \(k\) for cycle length and \(s=n-k\) for the number of off-cycle vertices. Choose the \(k\) cycle labels and arrange them in an unoriented cycle, in \(\binom nk(k-1)!/2\) ways. The remaining graph is a forest rooted at these \(k\) cycle vertices, oriented toward the roots. Each nonroot vertex has one parent. Its graph degree is one exactly when it has no children.

For a fixed root set \(R\) of size \(k\), assign formal variables \(x_v\) and weight each rooted forest by the product of \(x_v\) over all parent endpoints. The directed matrix-tree determinant for the \(s\) nonroot vertices is
\[
\det\!\left[X I_s-\mathbf 1(x_v)_{v\notin R}^{\mathsf T}\right]
=\left(\sum_{v\in R}x_v\right)X^{s-1},\quad X=\sum_{v=1}^n x_v.
\]
Indeed its diagonal entries are \(X-x_v\) and its off-diagonal entries are \(-x_w\); the matrix determinant lemma gives the displayed factorization. Set root variables equal to one. The remaining child-count generating polynomial becomes \(k(k+\sum_{v\notin R}x_v)^{s-1}\). Consequently, after dividing by the total number \(k n^{s-1}\) of forests, nonroot child counts have the same joint distribution as occupancies of the \(s\) specified bins after \(s-1\) independent uniform throws into \(n\) bins. Exactly \(r\) leaves means exactly \(r\) of those \(s\) bins are empty.

For fixed \(r\) empty bins, the other \(s-r\) specified bins must receive at least one throw, while the \(k\) root bins receive arbitrary throws. The number of assignments is
\[
(s-1)!\,[z^{s-1}]e^{kz}(e^z-1)^{s-r}.
\]
Choosing the \(r\) empty bins and then the cycle gives
\[
\binom nk\frac{(k-1)!}{2}\,k\binom sr(s-1)!
[z^{s-1}]e^{kz}(e^z-1)^{s-r}.
\]
Cancel \(k\), rewrite the coefficient after extracting \(z^{s-r}\), and simplify \(\binom sr/s=(s-1)_{r-1}/r!\). This is precisely the exact formula claimed. For \(r=1\) the coefficient equals one. For \(r=2\), it equals \(k+(s-2)/2\), proving the two special cases.

For the limit, let \(d=r-1\), \(y=k/n\), and \(s=n-k\). Since \(\log F(z)=z/2+O(z^2)\) near zero, fixed-degree coefficient extraction gives, uniformly for all \(3\le k\le n-r\),
\[
[z^d]e^{kz}F(z)^{s-r}
=\frac{n^d}{d!}\left(\frac{1+y}{2}\right)^d+O_r(n^{d-1}).
\]
Also \((s-1)_d=n^d(1-y)^d+O_r(n^{d-1})\). Therefore, uniformly on the admissible lattice,
\[
\frac{N_{n,k,r}}{n!\,n^{2r-2}}
=\frac{(1-(k/n)^2)^{r-1}}{2^r r!(r-1)!}+O_r(n^{-1}).
\]
Summing and normalizing these weights is a Riemann sum on \([0,1]\). Since
\[
\int_0^1(1-y^2)^{r-1}\,dy=\tfrac12 B(1/2,r),
\]
\(K_n/n\) has the stated weak limit, and applying the continuous map \(y\mapsto y^2\) gives the beta-square law.

## Verification
The included standalone program `verify_unicyclic_leaves.py` computes the graph count independently through two exact integer/rational formulas and directly enumerates every simple labelled unicyclic graph with \(n\) vertices for \(4\le n\le7\). Its recorded run passed 455 cross-formula comparisons and 34 raw-graph crosschecks. These finite checks corroborate, but do not replace, the matrix-tree and coefficient-asymptotic proof.

## Relationship to prior work
The classical unicyclic-component generating function, as recalled by Noy, Rasendrahasina, Ravelomanana and Rué, is \(\sum_{k\ge3}T(z)^k/(2k)\) for the rooted-tree series \(T\). Their work studies cycle counts in sparse random graphs rather than cycle lengths conditioned on a fixed positive number of leaves. Zhang and Zhang study the same combinatorial classes indexed by leaf count and girth, but their results concern extremal Laplacian coefficients, not uniform labelled counting and this weak limit. Janson studies cycle sizes and unicyclic components in an unconditioned random-graph regime. The rooted-forest determinant and tree-cycle decomposition are standard ingredients; neither is claimed as new. This work's contribution is their combined fixed-leaf exact enumeration and beta-square conditional limit.

## Limitations
The result is an exact calculation for uniform labelled connected unicyclic graphs, not for a uniformly selected unicyclic component in \(G(n,p)\). Historical priority is not independently certified; an older multivariate counting formula might imply the displayed result. Janson's complete 2003 paper was not accessible in the available review. No limit with \(r\) growing with \(n\), and no independence assertion, is made.

## References
1. S. Janson, “Cycles and Unicyclic Components in Random Graphs,” *Combinatorics, Probability and Computing* 12 (2003), 27–52, doi:10.1017/S0963548302005412 (online 28 January 2003).
2. J. Zhang and X.-D. Zhang, “Laplacian coefficients of unicyclic graphs with the number of leaves and girth,” arXiv:1311.1987 (8 November 2013).
3. M. Noy, V. Rasendrahasina, V. Ravelomanana and J. Rué, “Cycles of Given Lengths in Unicyclic Components in Sparse Random Graphs,” arXiv:2003.03552 (7 March 2020).
