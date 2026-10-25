# Protected roots increase global path length by a logarithmic amount in uniform recursive trees

## Finding
Consider a uniformly random recursive tree on labels \(1,\ldots,n\). Define its total path length \(P_n\) to be the sum of all depths from root \(1\); let \(R_n\) be the event that root \(1\) has no child that is a leaf. For every integer \(n\ge3\), put \(N=n-1\), \(H_k=\sum_{r=1}^{k}1/r\) (with \(H_0=0\)), and \(f_k=\sum_{r=0}^{k}(-1)^r/r!\). Then

\[
\Pr(R_n)=f_N,\qquad \mathbb E[P_n]=(N+1)H_N-N,
\]

\[
\mathbb E[P_n\mid R_n]=N+\frac{1}{f_N}\sum_{s=2}^{N}(H_s-1)f_{N-s},
\]

and consequently

\[
\boxed{\Delta_n:=\mathbb E[P_n\mid R_n]-\mathbb E[P_n]
=\frac{1}{f_N}\sum_{j=0}^{N-2}(H_{N-j}-1)(f_j-f_N)>0.}
\]

The strict inequality holds for all \(n\ge3\). Its precise asymptotic form is

\[
\boxed{\Delta_n=H_{n-1}-1+\frac{1}{2(n-1)}+O(n^{-2})}
=\log n+\gamma-1+o(1).
\]

In particular, \(\operatorname{Cov}(P_n,\mathbf1_{R_n})=f_N\Delta_n>0\), with the covariance asymptotic to \(e^{-1}\log n\).

## Assumptions and scope
For each \(j\in\{2,\ldots,n\}\), vertex \(j\) chooses an independent, uniformly random parent from \(\{1,\ldots,j-1\}\). The root has depth zero. A leaf has no children. A root is *protected* precisely when every direct child has at least one child; for \(n\ge3\) this event has positive probability. All conditional expectations are under the uniform recursive-tree distribution, not under the uniform Cayley-tree or binary-search-tree law. The finite identities are exact, without asymptotic assumptions.

## Proof
**Root-forest decomposition.** Delete the root and its incident edges. The remaining components form an unordered collection of increasing rooted trees on a partition of the remaining \(N\) labels. An increasing tree on a fixed \(s\)-element label set has exactly \((s-1)!\) possibilities: each nonminimal vertex chooses a smaller parent. Therefore the exponential generating function of a single component is \(z^s/s\), and the unrestricted forest has generating function \(\exp(\sum_{s\ge1}z^s/s)=1/(1-z)\). The root is protected exactly when no component has size one, giving

\[
F(z)=\exp\!\left(\sum_{s\ge2}\frac{z^s}{s}\right)
=\frac{e^{-z}}{1-z}=\sum_{N\ge0}f_N z^N.
\]

There are \(N!\) recursive trees of size \(N+1\), so \(\Pr(R_n)=f_N\). In particular \(f_N>0\) for \(N\ge2\).

**Marked internal path length.** Each vertex outside the root has its depth in the full tree equal to one plus its depth within its root branch. The expected total internal path length of a size-\(s\) recursive tree is \(s(H_s-1)\), since a label at rank \(k\) has expected depth \(H_{k-1}\). Marking a component with that additive cost contributes \((s(H_s-1))/s=H_s-1\) to the component generating function. Consequently the weighted protected-forest generating function is

\[
F(z)\sum_{s\ge2}(H_s-1)z^s.
\]

Coefficient extraction and division by \(f_N\) give

\[
\mathbb E[P_n\mid R_n]=N+
\frac{\sum_{s=2}^{N}(H_s-1)f_{N-s}}{f_N}.
\]

Without the size-one prohibition, \(\mathbb E[P_n]=N+\sum_{s=2}^{N}(H_s-1)=(N+1)H_N-N=n(H_n-1)\). Subtracting and setting \(j=N-s\) yields the stated finite expression for \(\Delta_n\).

**Strict positivity.** Let \(a_j=f_j-f_N\) and \(w_j=H_{N-j}-1\) for \(0\le j\le N-2\). The alternating-series bounds imply \(a_j>0\) for even \(j\) and \(a_j<0\) for odd \(j\) in this range. Also \(w_j>w_{j+1}>0\). For each even \(j\) with \(j+1\le N-2\), \(f_N\le f_{j+2}\), and hence

\[
a_j+a_{j+1}\ge f_j+f_{j+1}-2f_{j+2}
=\frac{j}{(j+2)(j+1)!}\ge0.
\]

The inequality is strict for \(j=0\) when \(j+1\le N-2\), because in that case \(N\ge3\) and \(f_N<f_2\). Thus each such pair contributes

\[
w_ja_j+w_{j+1}a_{j+1}
=(w_j-w_{j+1})a_j+w_{j+1}(a_j+a_{j+1})>0.
\]

If an index is unpaired, it is even and contributes positively. Therefore \(\sum_jw_ja_j>0\) for every \(N\ge2\).

**Sharp logarithmic asymptotic.** Set \(\varepsilon_j=f_j-e^{-1}\). The alternating-series remainder gives \(|\varepsilon_j|\le1/(j+1)!\), and its generating function is

\[
\sum_{j\ge0}\varepsilon_jz^j
=\frac{e^{-z}-e^{-1}}{1-z}.
\]

Evaluating this function and its derivative at \(z=1\) shows

\[
\sum_{j\ge0}\varepsilon_j=e^{-1},\qquad
\sum_{j\ge0}j\varepsilon_j=-\frac{e^{-1}}2.
\]

For \(j\le N/2\), harmonic-number differences obey \(H_{N-j}=H_N-j/N+O((j+j^2)/N^2)\). Terms with \(j>N/2\) contribute less than any power of \(1/N\), by the factorial bound. Moreover \(f_N=e^{-1}+O(1/(N+1)!)\). Substituting these three estimates in the finite formula yields

\[
\Delta_n=\frac{e^{-1}(H_N-1)+e^{-1}/(2N)+O(N^{-2})}{e^{-1}+O((N+1)!^{-1})}
=H_N-1+\frac1{2N}+O(N^{-2}).
\]

Finally \(\operatorname{Cov}(P_n,\mathbf1_{R_n})=\Pr(R_n)\bigl(\mathbb E[P_n\mid R_n]-\mathbb E[P_n]\bigr)\).

## Verification
Run the standalone `verify.py` file with Python 3 and `mpmath`. It independently enumerates every parent map at sizes \(3\) through \(8\), recomputes root protection and total path length directly, and matches all finite formulas using exact rational arithmetic. It also compares the two algebraically different displacement expressions for \(2\le N\le125\), checks strict positivity, and tests the asymptotic remainder at four sizes. The package produced `PASS 282 exact/sign/asymptotic checks; recursive trees exhaustively enumerated n=3..8`. Enumeration does not establish the infinite-size claims; the displayed proof does.

## Relationship to prior work
Dobrow and Fill (1999) established the mean total path length and root-subtree decomposition for uniform recursive trees, including the classical expectation \(n(H_n-1)\). Mahmoud and Ward (2015) studied protected-node counts and obtained the root-protection probability, but not the expectation of global total path length conditional on that root event. Devroye and Janson (2013) analyzed protected nodes and fringe-subtree limits, but did not report the mixed conditional path-length statistic. The present result derives the exact mixed quantity and the strict positive logarithmic displacement. Earlier general tree recurrences could imply it after a separate computation, so independent historical-priority assessment remains necessary.

## Limitations
The result concerns *only* a uniform random recursive tree and root protection; it is not a theorem for uniform labeled Cayley trees or all protected vertices. A strictly positive difference between conditional means is not a stochastic dominance statement. The result is established by analytic proof plus finite checks, not independent external validation. A fully exhaustive bibliographic priority check has not been performed.

## References
- R. P. Dobrow and J. A. Fill, *Total Path Length for Random Recursive Trees*, Combinatorics, Probability and Computing 8 (1999), 317–333, https://doi.org/10.1017/S0963548399003855 (published online 1999-07-01).
- H. M. Mahmoud and M. D. Ward, *Asymptotic Properties of Protected Nodes in Random Recursive Trees*, Journal of Applied Probability 52 (2015), 290–297, https://doi.org/10.1239/jap/1429282623.
- L. Devroye and S. Janson, *Protected nodes and fringe subtrees in some random trees*, arXiv:1310.0665 (2013), https://arxiv.org/abs/1310.0665.
