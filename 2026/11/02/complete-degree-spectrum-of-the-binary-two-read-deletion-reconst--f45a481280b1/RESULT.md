# Complete degree spectrum of the binary two-read deletion-reconstruction graph

## Finding
For every integer \(n\ge1\), let \(G_n\) be the graph whose vertices are all binary words of length \(n\). Distinct words \(x,y\) are adjacent precisely when their sets \(D_1(x),D_1(y)\) of **distinct** length-\(n-1\) one-deletion descendants have at least two elements in common. Let \(d_n(x)\) denote the degree of \(x\) in this graph. Put
\[
R(z,u)=\sum_{h\ge1}z^h u^{\binom{h+1}{2}}.
\]
The **complete degree distribution** over every blocklength is the formal identity
\[
\boxed{\sum_{n\ge1}z^{n-1}\sum_{x\in\{0,1\}^n}u^{d_n(x)}
=\frac{2(1+R(z,u))}{1-z-zR(z,u)}.}
\]
More explicitly, put \(\Delta(x)=(x_1\oplus x_2,\ldots,x_{n-1}\oplus x_n)\), and let \(h_1,\ldots,h_r\) be the lengths of its maximal runs of ones. Then
\[
\boxed{d_n(x)=\sum_{i=1}^{r}\binom{h_i+1}{2}.}
\]
Equivalently, if \(N_{n,d}=|\{x\in\{0,1\}^n:d_n(x)=d\}|\), put \(m=n-1\), \(H=h_1+\cdots+h_r\), and \(T_h=\binom{h+1}{2}\). Then, for all \(d\ge0\),
\[
N_{n,d}=2\mathbf1_{\{d=0\}}+2\sum_{r=1}^{m}\ 
\sum_{\substack{h_1,\ldots,h_r\ge1;\ H+r-1\le m\\\sum_{i=1}^{r}T_{h_i}=d}}
\binom{m-H+1}{r}.
\]
The inner sum is over ordered positive run-length lists and is empty if the conditions cannot hold.

For a uniformly chosen binary word \(X_n\), for every \(n\ge1\),
\[
\boxed{\mathbb E\,d_n(X_n)=n-2+2^{1-n},}
\qquad
\boxed{\operatorname{Var}(d_n(X_n))=
6n-30+\frac{2n^2+6n+17}{2^{n-1}}-4^{1-n}.}
\]
Consequently, \(\operatorname{Var}(d_n(X_n))\sim6n\) and the degree divided by \(n\) converges in probability to \(1\). For \(n\ge2\), exactly two vertices (the constant words) have degree zero, and exactly two (the alternating words) have maximum degree \(\binom n2\).

## Assumptions and scope
A one-deletion ball is a **set**, rather than a multiset: two deletion positions producing the same word give one descendant. The two-read adjacency rule is the condition \(|D_1(x)\cap D_1(y)|\ge2\). Its size is at most two for distinct binary words, so this is equivalent to equality with two. The generating function is a formal power series in \(z\) with polynomial coefficients in \(u\): the coefficient of \(z^m\) only uses \(h\le m\). All claims include \(n=1\), for which \(G_1\) consists of two isolated vertices. The logarithmic and probability limits concern uniformly chosen vertices; no independent-edge model is assumed.

## Proof
**Step 1: exact neighbors.** The Type-A intersection characterization of Cai--Kiah--Nguyen--Yaakobi (Proposition 9 in [1], including its Hamming-distance-one case) says: for distinct binary length-\(n\) words, two distinct one-deletion descendants are shared if and only if the words agree outside an interval of length at least two, and inside that interval are the two complementary phases of an alternating word. The first and last mismatching coordinates uniquely fix this interval. Conversely, choosing any alternating interval of length at least two in \(x\) and complementing all its symbols gives one neighbor, with the two common descendants obtained by deleting its opposite ends. Different intervals have different first-and-last mismatch coordinates, so give different neighbors. This establishes a one-to-one correspondence between neighbors and alternating intervals of length at least two in \(x\).

**Step 2: run formula.** The binary difference sequence \(\Delta(x)\) has a one at position \(i\) exactly when \(x_i\ne x_{i+1}\). An interval \([i,j]\) in \(x\) of length \(j-i+1\ge2\) is alternating precisely when the \(j-i\) consecutive differences from \(i\) through \(j-1\) are all ones. In a maximal difference-one run of length \(h\), there are \(\sum_{k=1}^{h}(h-k+1)=\binom{h+1}{2}\) nonempty consecutive subintervals. Different maximal runs contribute disjointly. This proves the displayed degree formula, including zero and maximal degrees. The difference map, together with the first bit of \(x\), is bijective with \(\{0,1\}\times\{0,1\}^{n-1}\).

**Step 3: full spectrum.** A maximal run of \(h\ge1\) ones in a difference string carries length weight \(z^h\) and degree weight \(u^{\binom{h+1}{2}}\), so its generating function is \(R\). Every binary difference string is uniquely a string of initial zeros, followed by zero or more blocks consisting of a positive one-run and a positive zero-run, followed optionally by a final positive one-run. The respective generating functions are \((1-z)^{-1}\), \((1-zR/(1-z))^{-1}\), and \(1+R\). Their product simplifies to \((1+R)/(1-z-zR)\). Choosing the initial bit doubles each coefficient, proving the bivariate identity. For the finite coefficient expression, fix an ordered list of \(r\) positive one-run lengths with total \(H\). Their \(r-1\) internal intervening zero-runs must be nonempty; distributing the remaining \(m-H-r+1\) zeros over \(r+1\) nonnegative gaps gives \(\binom{m-H+1}{r}\) possible difference words, each with two lifts. The case of no one-runs gives the two constant words. This coefficient identity, not an asymptotic approximation, determines the count of every possible degree at every length.

**Step 4: exact moments.** Write \(F(z,u)=(1+R(z,u))/(1-z-zR(z,u))\), so \([z^{n-1}]F\) is the degree enumerator of difference strings. At \(u=1\),
\[
R=\frac z{1-z},\qquad R_u=\frac z{(1-z)^3},\qquad
R_{uu}=\frac{6z^2}{(1-z)^5}.
\]
Differentiating the rational expression for \(F\) while treating \(R\) as an inner function gives
\[
F_u(z,1)=\frac{z}{(1-z)(1-2z)^2},
\qquad
F_{uu}(z,1)=\frac{2z^2(3-5z)}{(1-z)^3(1-2z)^3}.
\]
With \(m=n-1\), partial fractions or direct coefficient extraction yield
\[
[z^m]F_u(z,1)=(m-1)2^m+1,
\]
\[
[z^m]F_{uu}(z,1)=(m^2+3m-22)2^m+2m^2+12m+22.
\]
Since there are \(2^m\) equally likely difference strings and these derivatives count first and second factorial moments, respectively, one obtains
\[
\mathbb E[d_n(X_n)]=m-1+2^{-m},
\]
\[
\operatorname{Var}(d_n(X_n))=
6m-24+(2m^2+10m+25)2^{-m}-4^{-m}.
\]
Putting \(m=n-1\) gives the announced formulas. At \(m=0\), the formulas give mean and variance zero as required. Chebyshev's inequality and \(\mathbb E[d_n(X_n)]/n\to1\), \(\operatorname{Var}(d_n(X_n))/n^2\to0\) prove convergence in probability. Finally, a nonempty run contributes positive degree, so only an all-zero difference string gives degree zero; among words of fixed length it has exactly two lifts. The maximum \(\binom n2\) arises only from the all-one difference string, again with two lifts: for a run partition, the sum of triangular numbers is at most the triangular number of their total length, with strict inequality unless one run uses all \(m\) positions.

## Verification
Run `python verification/check.py` using Python 3 standard libraries. The script builds distinct one-deletion descendant sets and directly computes graph degrees independently of the difference-run formula for **all** binary center words of lengths \(1\) through \(9\), thereby checking 174,251 unordered center pairs. A separate coefficient recurrence derived from \((1-z-zR)F=1+R\) verifies all bivariate coefficients through length \(14\); the same all-word counts check the mean, variance and extreme-degree multiplicities at those lengths. The deterministic output is in `verification/output.txt`. Finite checks cannot prove the universal assertions; those follow from the exact Type-A theorem and formal generating-function derivation above.

## Relationship to prior work
Cai, Kiah, Nguyen and Yaakobi [1] establish the Type-A characterization, a pairwise condition for two common one-deletion descendants. Chrisnata, Kiah and Yaakobi [2] use precisely this graph for reconstruction-code clique-cover bounds. A public 2026 exact edge-enumeration result [3] counts all edges and gives the average degree \(n-2+2^{1-n}\) in the binary case; its statement explicitly leaves the **degree distribution** undetermined. Our mean agrees with it, but a graph's edge count or mean does not determine its degree distribution or variance. The new all-length bivariate generating function, exact degree-by-word formula and exact variance fill that specific gap. Wang, Li and Fu [4] study higher-deletion intersection extrema for \(q\)-ary channels, not this local degree spectrum.

## Limitations
The result covers binary one-deletion balls and the two-read confusability graph, not \(q\)-ary degree distributions for \(q>2\), graph independence numbers, or multi-deletion error balls. The structural Type-A theorem is invoked as a published result; a new proof of its full generality is not claimed. The finite checks are corroborative, not infinite certificates. No exhaustive guarantee of publication priority or independent mathematical validation is claimed. The 2026 edge-count note was compared through its full public result text; other unindexed equivalences remain possible.

## References
1. K. Cai, H. M. Kiah, T. T. Nguyen, E. Yaakobi, *Coding for Sequence Reconstruction for Single Edits*, arXiv:2001.01376, first public January 6, 2020, Proposition 9. https://arxiv.org/html/2001.01376v2
2. J. Chrisnata, H. M. Kiah, E. Yaakobi, *Correcting Deletions With Multiple Reads*, IEEE Transactions on Information Theory 68 (2022), 7141--7158, Section III, Lemma 2, and Section IV. https://doi.org/10.1109/TIT.2022.3184868
3. *Exact edge count of the finite-alphabet two-read single-deletion reconstruction graph*, publicly available 2026 mathematical result. https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-edge-count-of-the-finite-alphabet-two-read-single-deletion--737fed325e91
4. X. Wang, H. Li, F.-W. Fu, *On Sequence Reconstruction Problem for q-ary Deletion Channels*, first submitted September 15, 2026, arXiv:2609.16837. https://arxiv.org/abs/2609.16837
