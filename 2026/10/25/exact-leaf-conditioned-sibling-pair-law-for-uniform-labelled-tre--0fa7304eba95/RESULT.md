# Exact leaf-conditioned sibling-pair law for uniform labelled trees

## Finding
Let \(T\) be uniformly distributed over the \(n^{n-2}\) simple trees on the fully labelled vertex set \([n]\), with integer \(n\ge3\). Let \(L\) be the number of degree-one vertices, and let \(C\) count unordered pairs of distinct degree-one vertices with the same neighbour. Unlike a binary-phylogenetic cherry count, \(C\) counts all \(\binom{a}{2}\) pairs at a vertex adjacent to \(a\) leaves.

For each integer \(2\le\ell\le n-2\), put \(m=n-\ell\) and define the formal series
\[
H(z,y)=\sum_{a\ge0}\frac{z^a}{a!}y^{\binom a2}.
\]
The **entire exact joint enumeration** is
\[
\boxed{\displaystyle
\sum_{T:\,L(T)=\ell}y^{C(T)}
=\binom n\ell\,\ell!\,(m-2)!
[u^{m-2}z^\ell]\bigl(e^uH(z,y)-1\bigr)^m.}
\tag{1}
\]
Equivalently, this is the finite alternating formula
\[
\boxed{\displaystyle
\sum_{T:\,L(T)=\ell}y^{C(T)}
=\binom n\ell\,\ell!\,[z^\ell]
\sum_{j=1}^{m}(-1)^{m-j}\binom mj j^{m-2}H(z,y)^j.}
\tag{2}
\]
For \(\ell=n-1\), the tree is a star; exactly \(n\) such labelled trees exist and all have \(C=\binom{n-1}{2}\). These formulas cover every possible leaf count for \(n\ge3\).

Let \(S(a,b)\) be a Stirling number of the second kind, defined to vanish when \(b>a\) or \(b<0\). For \(2\le\ell\le n-2\), conditioning on \(L=\ell\) gives
\[
\boxed{\displaystyle
\mathbb E[C\mid L=\ell]
=\binom\ell2\frac{S(n-3,m)}{S(n-2,m)},}
\tag{3}
\]
\[
\boxed{\displaystyle
\mathbb E[C(C-1)\mid L=\ell]
=\left((\ell)_3+\frac{(\ell)_4}{4}\right)
\frac{S(n-4,m)}{S(n-2,m)},}
\tag{4}
\]
where \((\ell)_r=\ell(\ell-1)\cdots(\ell-r+1)\), interpreted as zero for \(r>\ell\). Thus the full conditional variance follows as (4) plus (3) minus the square of (3).

The **exact support** of \(C\) conditional on \(L=\ell\) is the set
\[
\boxed{\displaystyle
\left\{\sum_{i=1}^{m}\binom{a_i}{2}:\ a_i\in\mathbb Z_{\ge0},\quad
\sum_i a_i=\ell,\quad \#\{i:a_i>0\}\ge2\right\}.}
\tag{5}
\]
In particular, its maximum is \(\binom{\ell-1}{2}\). The minimum is zero when \(\ell\le m\); when \(\ell>m\), write \(\ell=qm+r\) with \(0\le r<m\), and the minimum is
\[
(m-r)\binom q2+r\binom{q+1}{2}.
\]
The conditional support may have gaps between these sharp endpoints.

## Assumptions and scope
All trees are unrooted, simple, and uniformly sampled with **every vertex labelled**; nonleaf vertices may have arbitrary degree at least two. No binary-tree, leaf-only labelling, branching-process, or large-size assumption is made. The sample space is the \(n^{n-2}\) trees on \([n]\). For \(n=3\), only the star case occurs and \(L=2,C=1\). All equalities above are finite, exact identities; coefficient notation means extraction from formal power series. The polynomial \(H(z,y)\) may be truncated at \(z^\ell\) when computing (1) or (2).

## Proof
**1. Leaf-core decomposition.** Fix the set \(A\subset[n]\) of \(\ell\) leaf labels. When \(m=n-\ell\ge2\), delete the leaves and their incident edges. The remaining tree \(R\) on the complementary \(m\) labels is connected: paths between nonleaves cannot have a leaf as an interior vertex. Conversely, take any labelled tree \(R\) on the complementary vertices and attach every label in \(A\) to one vertex of \(R\). If a core vertex \(v\) has degree \(d_v\) in \(R\) and receives \(a_v\) leaves, it is nonleaf in the full tree exactly when \(d_v+a_v\ge2\). Since \(d_v\ge1\), this condition is \(a_v\ge1\) if \(d_v=1\), and imposes no extra restriction otherwise. Every original tree is obtained uniquely in this manner; its sibling-pair count is \(\sum_v\binom{a_v}{2}\).

**2. Degree-refined core count.** For a fixed sequence \(d_v\ge1\) with \(\sum_v(d_v-1)=m-2\), Prüfer's bijection counts core trees by
\[
\frac{(m-2)!}{\prod_v(d_v-1)!}.
\]
For a vertex with \(d_v=1\), the exponential leaf-allocation series is \(H(z,y)-1\), because it must receive a leaf; for \(d_v\ge2\), it is \(H(z,y)\). Mark \(d_v-1\) by \(u\). Summing possible degrees at one vertex yields
\[
(H-1)+H\sum_{r\ge1}\frac{u^r}{r!}=e^uH-1.
\]
Multiplying these factors for the \(m\) core labels, extracting \(u^{m-2}z^\ell\), assigning the \(\ell\) distinct leaves (factor \(\ell!\)), and choosing their label set (factor \(\binom n\ell\)) proves (1). Expanding the \(m\)-th power and using \([u^{m-2}]e^{ju}=j^{m-2}/(m-2)!\) proves (2). The \(j=0\) term may be omitted because \(\ell\ge2\).

**3. Exact conditional moments.** At \(y=1\), \(H(z,1)=e^z\). Thus (2) specializes to
\[
\binom n\ell\sum_{j=0}^m(-1)^{m-j}\binom mj j^{n-2}
=\binom n\ell\,m!\,S(n-2,m),
\]
which is strictly positive for \(2\le\ell\le n-2\). Differentiation in \(y\) is legitimate coefficientwise. The needed derivatives are
\[
H_y(z,1)=\frac{z^2}{2}e^z,\qquad
H_{yy}(z,1)=\left(z^3+\frac{z^4}{4}\right)e^z.
\]
Consequently,
\[
\left.\partial_yH(z,y)^j\right|_{y=1}=\frac{jz^2}{2}e^{jz},\quad
\left.\partial_y^2H(z,y)^j\right|_{y=1}
=\left(jz^3+\frac{j^2z^4}{4}\right)e^{jz}.
\]
Using the Stirling identity \(\sum_{j=0}^m(-1)^{m-j}\binom mj j^b=m!S(b,m)\), the first derivative of (2) equals \(\binom n\ell\,\binom\ell2\,m!S(n-3,m)\), and the second equals \(\binom n\ell\bigl((\ell)_3+(\ell)_4/4\bigr)m!S(n-4,m)\). Division by the count at \(y=1\) proves (3)–(4).

**4. Support and sharp extremes.** The leaf-core decomposition shows that every realized tree yields an allocation vector with at least two positive entries, since every core tree has at least two leaves, each of which requires an attached original leaf. Conversely, for any nonnegative vector of total \(\ell\) with at least two positive entries, choose a path on the \(m\) core vertices whose endpoints are two vertices with positive allocations; attach leaves as prescribed. Its full-tree nonleaves are exactly the core, realizing the vector and proving (5). Convexity of \(a\mapsto\binom a2\) shows the maximum is obtained with allocation \((\ell-1,1,0,\ldots,0)\); the minimum uses as many bins as possible with loads differing by at most one, giving the displayed expressions. The star case follows directly by selecting its centre.

As an unconditional consistency check, selecting two leaves and their common neighbour, then deleting the two leaves, gives
\[
\mathbb EC=\binom n2\frac{(n-2)^{n-3}}{n^{n-2}}\sim\frac{n}{2e^2}.
\]
This identity is a corollary, not required for the conditional enumeration proof.

## Verification
The supplied standalone \(verify.py\) uses exact integer arithmetic. It independently enumerates all Prüfer sequences for each \(3\le n\le8\), decodes the resulting tree edges, extracts its actual leaf set and sibling pairs, and compares the observed complete \((L,C)\)-tables with a separate integer allocation expansion of (2). It additionally checks the normalization to Cayley's count, both factorial-moment identities, and the exact support description. The executed checker reported 90 exact table, moment, and support assertions with no failures, over all \(280391\) labelled trees in those six sizes. Finite checking is corroboration; the preceding Prüfer/leaf-core argument proves the identities for all \(n\ge3\).

To reproduce from the extracted package: run `python3 verify.py` with the standard Python library.

## Relationship to prior work
Classical Prüfer codes give total counts and degree-sequence counts for labelled trees; they do not directly describe which leaves have common neighbours. Isaev, Southwell and Zhukovskii (arXiv:1912.09838, first version 2019-12-20) prove general asymptotic normality for local pattern counts on uniform fully labelled trees, but the inspected exact statements do not supply the finite bivariate leaf/sibling-pair polynomial (1) or its conditional factorial moments. Choi, Thompson and Wu (arXiv:2002.12643, 2020) derive cherry/pitchfork laws for binary phylogenetic trees with **only leaves labelled**, a distinct space in which all interior vertices have degree three. Choi, Kaur and Wu (arXiv:2101.07488, 2021) treat asymptotic joint laws in those binary YHK/PDA models. Neither model allows the present arbitrary-degree fully labelled cores. The claimed contribution here is the exact all-size joint law for that different natural probability space and the resulting full conditional support/moments, not Cayley's formula, Prüfer's bijection, or existing binary phylogenetic results.

## Limitations
No priority claim is made against all unindexed literature: the exact formula may be recoverable from an older, more general labelled-tree generating function that was not identified in the inspected searches. The result concerns fully labelled Cayley trees, not sampling distributions under the PDA or YHK phylogenetic models. General conditional stochastic-order comparisons between different leaf counts are not claimed. No independent validation has been performed.

## References
- M. Isaev, A. Southwell, M. Zhukovskii, *Distribution of tree parameters by martingale approach*, arXiv:1912.09838 (first public version 2019-12-20), https://arxiv.org/html/1912.09838v2 .
- K. P. Choi, A. Thompson, T. Wu, *On cherry and pitchfork distributions of random rooted and unrooted phylogenetic trees*, arXiv:2002.12643 (2020), https://arxiv.org/abs/2002.12643 .
- K. P. Choi, G. Kaur, T. Wu, *On asymptotic joint distributions of cherries and pitchforks for random phylogenetic trees*, arXiv:2101.07488 (2021), https://arxiv.org/abs/2101.07488 .
- Classical Prüfer correspondence and Cayley's labelled-tree enumeration (standard combinatorial identities, used as prior tools).
