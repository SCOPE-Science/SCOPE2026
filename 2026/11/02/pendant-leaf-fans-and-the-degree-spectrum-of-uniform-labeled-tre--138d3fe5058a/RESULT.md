# Pendant leaf-fans and the degree spectrum of uniform labeled trees

## Finding

For a uniform labeled tree \(T_n\) on \([n]\), let \(\ell_v\) denote the number of degree-one neighbors of vertex \(v\). For an integer \(k\ge2\), define the pendant \(k\)-fan count \(S_{n,k}=\sum_{v=1}^n\binom{\ell_v}{k}\), counting unordered sets of \(k\) leaves with a common center (the center may have additional neighbors). Let \(D_{n,r}=|\{v:\deg(v)=r\}|\). For all integers \(n\ge k+2\), \(k\ge2\), and \(1\le r\le n-1\), define

\[
p_m(j)=\begin{cases}\displaystyle\binom{m-2}{j-1}\frac{(m-1)^{m-j-1}}{m^{m-2}},&1\le j\le m-1,\\0,&\text{otherwise,}\end{cases}\qquad m\ge2.
\]

In particular \(p_2(1)=1\). Then the following exact finite-order mixed moment identity holds:

\[
\boxed{\mathbb E S_{n,k}=\binom nk\frac{(n-k)^{n-k-1}}{n^{n-2}},}\tag{1}
\]
\[
\boxed{\operatorname{Cov}(S_{n,k},D_{n,r})
=\mathbb E S_{n,k}\left[k\mathbf1_{\{r=1\}}+(n-k-1)p_{n-k}(r)+p_{n-k}(r-k)-n p_n(r)\right].}\tag{2}
\]

For every **fixed** pair \(k\ge2\), \(r\ge1\), let \(n\) tend to infinity through integers \(n\ge k+2\). Then

\[
\boxed{\lim_{n\to\infty}\frac{\operatorname{Cov}(S_{n,k},D_{n,r})}{n}
=\frac{e^{-k}}{k!}\left[k\mathbf1_{\{r=1\}}-\frac{(k+1)e^{-1}}{(r-1)!}
+\mathbf1_{\{r\ge k+1\}}\frac{e^{-1}}{(r-k-1)!}\right].}\tag{3}
\]

Every constant in (3) is nonzero. The limit is **positive** for \(r=1\); **negative** for \(2\le r\le k\); and **positive** for \(r\ge k+1\) when \(k\ge3\). For \(k=2\), the negative interval instead extends through \(r=3\), and the limit is positive for \(r\ge4\). Thus the eventual covariance sign has a universal positive–negative–positive degree profile, with the unique boundary exception for two-leaf fans. Here "eventual" is pointwise for each fixed \((k,r)\), not uniform over degrees increasing with \(n\).

The exact generating-polynomial equivalent of (2), using \(m=n-k\), is

\[
\frac{\operatorname{Cov}(S_{n,k},\sum_{r=1}^{n-1}D_{n,r}z^{r-1})}{\mathbb E S_{n,k}}
=k+(m-1+z^k)\left(\frac{m-1+z}{m}\right)^{m-2}
-n\left(\frac{n-1+z}{n}\right)^{n-2}.\tag{4}
\]

## Assumptions and scope

The probability space consists of all \(n^{n-2}\) trees on the labeled vertex set \([n]\), each equally likely. Leaves have degree exactly one. A pendant \(k\)-fan is a choice of its center together with an unordered \(k\)-subset of its degree-one neighbors; fans with the same center may overlap. No maximum-degree restriction is imposed. The exact identity holds for all stated \(n,k,r\); asymptotic sign claims require \(k,r\) fixed independently of \(n\).

## Proof

**1. Count forced fans.** Fix distinct labels \(c\) and a \(k\)-element subset \(L\subseteq[n]\setminus\{c\}\). Let \(E_{c,L}\) be the event that every element of \(L\) is a leaf attached to \(c\). Deleting those forced leaves is a bijection between trees in \(E_{c,L}\) and labeled trees on the remaining \(m=n-k\) vertices. Cayley's formula gives \(m^{m-2}\) possibilities out of \(n^{n-2}\). There are \(n\binom{n-1}{k}=m\binom nk\) choices of \((c,L)\), proving (1) by linearity of expectation.

**2. Conditional degree profile.** On \(E_{c,L}\), the residual tree is exactly a uniform labeled tree on the \(m\) remaining labels. The \(k\) removed leaves contribute exactly \(k\) vertices of degree one. The degree of the center is its residual degree plus \(k\), whereas the other \(m-1\) residual degrees are unchanged. In a uniform labeled \(m\)-tree, the Prüfer representation gives

\[
\deg(v)\ \overset{d}=\ 1+\operatorname{Bin}(m-2,1/m),
\]

with probability mass function \(p_m(j)\) defined above. Hence

\[
\mathbb E[D_{n,r}\mid E_{c,L}]
=k\mathbf1_{\{r=1\}}+(m-1)p_m(r)+p_m(r-k).
\]

Unconditionally \(\mathbb E D_{n,r}=np_n(r)\). Since \(S_{n,k}=\sum_{c,L}\mathbf1_{E_{c,L}}\), sum the conditional mean difference over all \((c,L)\), proving (2). The generating polynomial (4) follows because \(\sum_{j\ge1}p_m(j)z^{j-1}=((m-1+z)/m)^{m-2}\).

**3. Asymptotic expansion.** For every fixed positive integer \(j\), directly expanding the binomial probability yields

\[
p_m(j)=\frac{e^{-1}}{(j-1)!}\left[1+\frac{3-j(j-1)}{2m}+O_j(m^{-2})\right].
\]

With fixed \(k\) and \(m=n-k\), the terms involving \(p_m(r)\) in (2) therefore satisfy

\[
(m-1)p_m(r)-n p_n(r)\longrightarrow-\frac{(k+1)e^{-1}}{(r-1)!}.
\]

Also \(p_m(r-k)\longrightarrow \mathbf1_{\{r\ge k+1\}}e^{-1}/(r-k-1)!\). Finally (1) gives \(\mathbb E S_{n,k}/n\longrightarrow e^{-k}/k!\). Multiplication proves (3).

**4. Strict signs.** For \(r=1\), the bracket in (3) equals \(k-(k+1)/e>0\), since \(e>2\) and \(k\ge2\). For \(2\le r\le k\), only the strictly negative middle term remains. For \(r\ge k+1\), after multiplication by \(e(r-1)!\), the sign is that of \((r-1)!/(r-k-1)!-(k+1)\). Its left side is strictly increasing in \(r\); at \(r=k+1\) it equals \(k!-(k+1)\), positive for \(k\ge3\), but negative for \(k=2\). In that exceptional case the sign is positive from \(r=4\) onward. All limiting signs are strict, proving the asserted eventual classifications.

## Verification

The standalone `verify.py` performs a distinct finite combinatorial enumeration: every Prüfer word for labeled trees of orders \(4\) through \(8\) is decoded to an adjacency list, from which both the actual leaf-fan and degree counts are computed. This covers \(280388\) trees and checks the exact mean and covariance identities for every admissible \(k,r\), yielding \(100\) exact-rational equalities. It is a finite consistency check, **not** a proof of the all-orders result. The proof above establishes the unrestricted identities.

## Relationship to prior work

Berzunza Ojeda, Holmgren and Janson develop central-limit and covariance methods for fringe trees in random tree models with prescribed degrees, including labeled trees; their fixed-fringe-tree asymptotics differ from the unrestricted-center finite mixed degree/fan formula and all-degree sign classification here [1]. Ekhad and Zeilberger derive joint statistics of the degree-profile counts in labeled trees; their degree–degree covariances do not directly contain the leaf-neighbor fan statistic [2]. Junk, Schmidt and Weber examine proper cherries (two leaves adjacent to a degree-three center), a different statistic from unrestricted-center fans, motivated by tree symmetries [3]. Cayley's enumeration and Prüfer degrees are standard inputs, not new claims. Prior generating-function identities could yield related coefficients implicitly; exhaustive historical priority is not asserted.

## Limitations

This result is specific to uniformly sampled labeled Cayley trees. The fixed-pair asymptotic does not control \(r\) or \(k\) growing with \(n\), and no global finite-order sign-transition cutoff is claimed. The theorem concerns covariance, not independence, large deviations, or joint limit distributions. Earlier general enumerations may implicitly contain identities equivalent to (2); no claim of independent external verification is made.

## References

[1] G. Berzunza Ojeda, C. Holmgren, S. Janson, *Fringe trees for random trees with given vertex degrees*, arXiv:2312.04243, first posted 2023-12-07. https://arxiv.org/abs/2312.04243

[2] S. B. Ekhad, D. Zeilberger, *Automated Counting and Statistical Analysis of Labeled Trees with Degree Restrictions*, arXiv:2201.07360, 2022. https://arxiv.org/abs/2201.07360

[3] T. Junk, S. Schmidt, M. Weber, *Almost all trees have quantum symmetry*, 2020. https://arxiv.org/abs/2007.04141
