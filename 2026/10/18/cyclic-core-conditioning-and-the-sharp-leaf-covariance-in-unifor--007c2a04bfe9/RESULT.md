# Cyclic-core conditioning and the sharp leaf covariance in uniform random mappings

## Finding

For each integer \(n\ge2\), take a uniformly random function \(f:[n]\to[n]\). Let \(K_n\) count vertices on directed cycles of its functional digraph and let \(L_n\) count vertices of indegree zero. The following complete conditional law, exact negative dependence and sharp covariance asymptotic hold simultaneously.

For \(1\le k<n\), put \(m=n-k\). For every integer \(0\le r\le m\),
\[
\mathbb E[(L_n)_{\underline r}\mid K_n=k]=(m)_{\underline r}\left(1-\frac r n\right)^{m-1}.
\]
Here \((a)_{\underline r}=a(a-1)\cdots(a-r+1)\), with \((a)_{\underline0}=1\). This determines the complete distribution; equivalently, it is the empty-box count among \(m\) specified boxes when \(m-1\) balls are placed independently and uniformly into \(n\) boxes. For \(k=n\), \(L_n=0\) deterministically.

Consequently, \(\mathbb E[L_n\mid K_n=k]=(n-k)(1-1/n)^{n-k-1}\) for \(k<n\), and zero for \(k=n\). This conditional mean is strictly decreasing in \(k\); in particular,
\[
\operatorname{Cov}(K_n,L_n)<0\qquad(n\ge2).
\]
More precisely,
\[
\operatorname{Cov}(K_n,L_n)
=-\frac{\sqrt{\pi/2}}{2e}\sqrt n+o(\sqrt n).
\]
Since \(\operatorname{Var}(K_n)/n\to(4-\pi)/2\) and \(\operatorname{Var}(L_n)/n\to e^{-1}-2e^{-2}\), the correlation is asymptotic to \(-c/\sqrt n\), with
\[
c=\frac{\sqrt{\pi/2}/(2e)}{\sqrt{[(4-\pi)/2](e^{-1}-2e^{-2})}}.
\]
These are statements about natural terminal (indegree-zero) vertices, not vertices having no outgoing functional edge (each vertex has exactly one).

## Assumptions and scope

The mapping is sampled uniformly from all \(n^n\) functions. Self-loops are permitted. Each functional component has a unique directed cycle. A cyclic vertex has a predecessor along its cycle, including when its cycle is a self-loop; it therefore cannot have indegree zero. All claims are finite-sample statements for \(n\ge2\) or ordinary limits as \(n\to\infty\), with no conditional-independence or stochastic-order assertion beyond the explicitly established conditional mean ordering.

## Proof

**Conditional rooted-forest law.** Fix an integer \(1\le k<n\) and a specified cyclic set \(S\subset[n]\) of cardinality \(k\), and put \(m=n-k\). The restriction of the mapping to \(S\) is a permutation, while every vertex of \([n]\setminus S\) belongs to a directed forest with edges pointing toward \(S\). For a fixed permutation on \(S\), every forest directed to these specified roots has the same mapping probability. The number of these forests is
\[
F(n,k)=k n^{m-1}.
\]
One direct proof is the all-minors matrix-tree theorem: the Laplacian minor for the \(m\) nonroot vertices of the complete directed graph is \(nI_m-J_m\); its eigenvalues are \(n\) (multiplicity \(m-1\)) and \(k\) (multiplicity one), giving the determinant. For \(m=1\), the count is \(k\). The case \(m=0\) is treated separately.

**Prescribed terminals.** Fix \(r\) distinct noncyclic vertices, where \(0\le r\le m\). Require each to have no children in the rooted forest; then delete them. The remaining \(n-r\) labeled vertices form a rooted forest with the same \(k\) roots, counted by \(k(n-r)^{m-r-1}\), and each deleted vertex can independently select its parent among the \(n-r\) remaining vertices. Thus there are exactly \(k(n-r)^{m-1}\) admissible original forests. This formula remains meaningful at \(r=m\): the remaining root-only forest is unique and the powers cancel. The probability that a fixed \(r\)-set of noncyclic vertices consists of terminals is therefore
\[
\frac{k(n-r)^{m-1}}{kn^{m-1}}=\left(1-\frac r n\right)^{m-1}.
\]
Summing over ordered \(r\)-tuples proves the asserted conditional factorial moments. For \(m=0\), the original mapping is a permutation and there are no terminals. The factorial moments are exactly those of the number of unhit cells in \(m\) selected boxes after \(m-1\) uniform throws among \(n\) boxes. Because \(0\le L_n\le m\), moments up to order \(m\) determine the law. Explicit inclusion-exclusion gives, for \(0\le\ell\le m\),
\[
\mathbb P(L_n=\ell\mid K_n=k)
=\binom m\ell\sum_{j=0}^{m-\ell}(-1)^j\binom{m-\ell}j
\left(1-\frac{\ell+j}{n}\right)^{m-1}.
\]

**Strict negative covariance.** Put \(q=1-1/n\). For \(m\ge1\), the conditional mean as a function of noncyclic count \(m\) is \(g(m)=m q^{m-1}\), with \(g(0)=0\). Clearly \(g(1)>g(0)\), and, for \(1\le m\le n-2\),
\[
g(m+1)-g(m)=q^{m-1}\left(1-\frac{m+1}{n}\right)>0.
\]
Therefore \(k\mapsto\mathbb E[L_n\mid K_n=k]\) decreases strictly for all \(1\le k\le n\). By total covariance, \(\operatorname{Cov}(K_n,L_n)=\operatorname{Cov}(K_n,\mathbb E[L_n\mid K_n])\). For an independent copy \(K_n'\), twice this covariance equals the expectation of \((K_n-K_n')(g(n-K_n)-g(n-K_n'))\), which is strictly negative on an event of positive probability, since \(K_n\) has at least two possible values for \(n\ge2\).

**Distribution of the cyclic core.** Choosing the \(k\) cyclic vertices, placing an arbitrary permutation on them, and attaching a rooted forest gives
\[
\mathbb P(K_n=k)=\frac{k(n)_{\underline k}}{n^{k+1}},\qquad
\mathbb P(K_n\ge k)=\frac{(n)_{\underline k}}{n^k},
\quad 1\le k\le n.
\]
The survival function follows either by telescoping or by direct first-repeat exposure. In particular, \(K_n/\sqrt n\Rightarrow R\), where \(R\) is standard Rayleigh: \(\mathbb P(R>x)=e^{-x^2/2}\) for \(x\ge0\). The exact survival product is bounded by \(\exp[-k(k-1)/(2n)]\), ensuring convergence of all fixed moments. Thus \(\mathbb ER=\sqrt{\pi/2}\), \(\mathbb ER^2=2\), \(\mathbb ER^3=3\sqrt{\pi/2}\) and \(\operatorname{Cov}(R,R^2)=\sqrt{\pi/2}\).

**Sharp mixed asymptotic.** Let \(h_n(k)=(n-k)(1-1/n)^{n-k-1}\) for \(k<n\), and \(h_n(n)=0\). Uniform Taylor expansion for \(1\le k\le n^{3/5}\) gives
\[
h_n(k)=\frac n e+\frac{1-k^2/n}{2e}
+O\!\left(\frac{k+1}{n}+\frac{k^3+1}{n^2}+\frac{k^4+1}{n^3}\right).
\]
The survival bound makes the complementary event \(K_n>n^{3/5}\) exponentially unlikely in a positive power of \(n\); all moments of \(K_n/\sqrt n\) are uniformly bounded. Because \(0\le h_n(k)\le n\), the remainder evaluated at \(K_n\) is \(O(n^{-1/2})\) in \(L^2\). Hence Cauchy-Schwarz implies
\[
\operatorname{Cov}(K_n,L_n)
=-\frac{1}{2en}\operatorname{Cov}(K_n,K_n^2)+O(1).
\]
Moment convergence yields \(n^{-3/2}\operatorname{Cov}(K_n,K_n^2)\to\operatorname{Cov}(R,R^2)=\sqrt{\pi/2}\), proving the main asymptotic.

**Correlation normalization.** The Rayleigh convergence gives \(\operatorname{Var}(K_n)/n\to(4-\pi)/2\). For the terminal count, the raw mapping images are \(n\) independent uniform choices: \(\mathbb EL_n=n(1-1/n)^n\) and
\[
\operatorname{Var}(L_n)=n p_0(1-p_0)+n(n-1)(p_{00}-p_0^2),
\quad p_0=(1-1/n)^n,\quad p_{00}=(1-2/n)^n.
\]
Expansion gives \(\operatorname{Var}(L_n)/n\to e^{-1}-2e^{-2}>0\). Division proves the stated correlation asymptotic.

## Verification

The standalone `verify.py` exhaustively enumerates all maps on \(n\in\{2,3,4,5,6\}\), computes cyclic cores and terminal sets directly, and compares exact rational conditional mass functions, factorial moments, core-size probabilities, monotonicity and negative covariances. It additionally checks the scaled covariance numerically at \(n=100,1000,10000\). Its finite tests support, but cannot establish, the general or asymptotic proofs above. Run with `python3 verify.py` (Python standard library only).

## Relationship to prior work

The conditional decomposition of a uniform random mapping into a permutation on cyclic vertices and a uniform rooted forest is classical, and is explicitly discussed by Pitman (2001) and Hansen–Jaworski (2006, 2010); it is not new here. Flajolet–Odlyzko (1990) develop the separate cycle and terminal statistics for random mappings. Mylläri (2002) studies leaf-count limits in conditioned Galton–Watson forests. The specific joint cyclic-core/terminal-count law and the sharp \(\sqrt n\)-order mixed-covariance coefficient are the claims assessed here, rather than the underlying mapping decomposition, isolated marginals, or a general tree census.

## Limitations

The theorem is restricted to the uniform mapping law, with all vertex images independent uniform. The conditional mean is strictly ordered, but no full stochastic ordering of conditional terminal counts is claimed. The occupancy representation is a law identity, not a coupling of mappings at different core sizes. The historical-priority comparison is not exhaustive; in particular, the full 2002 leaf-forest paper and several older papers on mapping strata could not be materially inspected. The connection to the known rooted-forest law means earlier implicit derivations are possible. The proof and executable checks provide mathematical evidence, not an independent scientific audit.

## References

1. J. Pitman, *Random mappings, forests, and subsets associated with Abel-Cayley-Hurwitz multinomial expansions*, Technical Report 593, University of California Berkeley (8 June 2001), https://statistics.berkeley.edu/sites/default/files/tech-reports/593.pdf.
2. P. Flajolet and A. M. Odlyzko, *Random Mapping Statistics*, EUROCRYPT 1989 / LNCS 434 (1990), https://scispace.com/pdf/random-mapping-statistics-yjuqfvoh87.pdf.
3. J. C. Hansen and J. Jaworski, *A new random mapping model*, arXiv:math/0603529 (22 March 2006), https://arxiv.org/pdf/math/0603529.
4. J. C. Hansen and J. Jaworski, *Random mappings with a given number of cyclical points*, Ars Combinatoria 94 (2010), 341–359, https://combinatorialpress.com/article/ars/Volume%20094/volume-94-paper-34.pdf.
5. T. Mylläri, *Limit distributions for the number of leaves in a random forest*, Advances in Applied Probability 34 (2002), 904–922, https://doi.org/10.1239/aap/1037990959.
