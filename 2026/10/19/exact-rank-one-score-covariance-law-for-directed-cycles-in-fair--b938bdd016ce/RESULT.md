# Exact rank-one score-covariance law for directed cycles in fair tournaments

## Finding

Let \(T_n\) be the uniformly random labeled tournament on \(n\ge3\) vertices, obtained by independently orienting each unordered edge with equal probability. Write \(C_\ell\) for its number of directed simple cycles of length \(\ell\), counted up to cyclic rotation but not reversal, for \(3\le\ell\le n\). Write \(D_v\) for the outdegree of vertex \(v\), and for every function \(f:\{0,\ldots,n-1\}\to\mathbb R\) set \(H_f=\sum_v f(D_v)\). Put \(m=n-1\) and let \(D\sim\operatorname{Bin}(m,1/2)\).

**Theorem (complete cycle-to-score covariance law).** For all integers \(n\ge3\), \(3\le\ell\le n\), and every such \(f\),

\[
\operatorname{Cov}(C_\ell,H_f)
=\frac{n(m-2)_{\underline{\ell-3}}}{2^{\ell-2}}
\operatorname{Cov}\bigl(D(m-D),f(D)\bigr).
\tag{1}
\]

Here \((a)_{\underline r}=a(a-1)\cdots(a-r+1)\), and \((a)_{\underline0}=1\). In particular,

\[
\operatorname{Cov}(C_\ell,H_f)
=\frac{(n-3)_{\underline{\ell-3}}}{2^{\ell-3}}
\operatorname{Cov}(C_3,H_f).
\tag{2}
\]

Thus the matrix of covariances between all \(C_3,\ldots,C_n\) and the entire outdegree histogram has **rank exactly one**. Every residual
\[
C_\ell-\frac{(n-3)_{\underline{\ell-3}}}{2^{\ell-3}}C_3
\]
is uncorrelated with every additive outdegree statistic \(H_f\); this asserts neither independence nor a conditional-distribution identity.

For \(0\le d\le m\), define \(H_d=\#\{v:D_v=d\}\), \(p_b(j)=2^{-b}\binom bj\) on \(0\le j\le b\) and zero otherwise. Then
\[
\operatorname{Cov}(C_\ell,H_d)
=\frac{n(m-2)_{\underline{\ell-3}}}{2^\ell}p_m(d)
\bigl[m-(2d-m)^2\bigr].
\tag{3}
\]
This covariance is positive precisely when \((2d-m)^2<m\), negative when \((2d-m)^2>m\), and zero when equality holds. Equality occurs precisely for \(m\) a positive perfect square and \(d=(m\pm\sqrt m)/2\).

For \(1\le k\le m\) define \(H_{\ge k}=\#\{v:D_v\ge k\}\). The threshold covariance is
\[
\operatorname{Cov}(C_\ell,H_{\ge k})
=\frac{n\,m(m-1)(m-2)_{\underline{\ell-3}}}{2^{\ell+2}}
\bigl[p_{m-2}(k-1)-p_{m-2}(k-2)\bigr].
\tag{4}
\]
Its sign is positive if \(2k<n\), zero if \(2k=n\), and negative if \(2k>n\), for **every** admissible cycle length. Hence a single threshold at half the vertex count governs every directed-cycle statistic simultaneously.

## Assumptions and scope

The tournament is the independent **fair** orientation of the complete graph on \(n\) labeled vertices. Outdegrees count outgoing arcs; a simple directed cycle visits distinct vertices and is identified under cyclic changes of starting point. Reverse traversal is not identified, but in a tournament it is never simultaneously a directed cycle on the same vertices. No biased-orientation, fixed-score, or directed-Erdős–Rényi law is covered. Binomial masses outside support are zero. All expectations and covariances are with respect to the finite tournament measure, and all identities are exact for the stated integer parameter ranges.

## Proof

**1. Exact conditioning on one vertex.** Fix \(v\) and put \(D_v=d\). The arcs among the other \(m=n-1\) vertices remain independent fair orientations. Directed \(\ell\)-cycles avoiding \(v\) have conditional expected count
\[
\binom m\ell\frac{(\ell-1)!}{2^\ell},
\]
with the convention that the binomial coefficient vanishes if \(\ell>m\). To count cycles through \(v\), represent each uniquely by the ordered cycle \(v\to x\to w_1\to\cdots\to w_{\ell-3}\to y\to v\). There are \(d\) choices for the outneighbor \(x\), \(m-d\) choices for the in-neighbor \(y\), and \((m-2)_{\underline{\ell-3}}\) ways to choose and order the remaining distinct vertices. Its \(\ell-2\) internal arcs, none incident to \(v\), have independent fair orientations. Therefore
\[
\mathbb E[C_\ell\mid D_v=d]
=\binom m\ell\frac{(\ell-1)!}{2^\ell}
+\frac{(m-2)_{\underline{\ell-3}}}{2^{\ell-2}}d(m-d).
\tag{5}
\]
The same proof applies at the extreme cycle length \(\ell=n\).

**2. Master covariance.** By linearity and exchangeability,
\[\operatorname{Cov}(C_\ell,H_f)
=n\operatorname{Cov}(C_\ell,f(D_v)).\]
The law of total covariance and (5) reduce this to (1), since \(D_v\sim\operatorname{Bin}(m,1/2)\) and \(\mathbb E[D(m-D)]=m(m-1)/4\). Comparing the coefficients of (1) for \(\ell\) and for \(\ell=3\) proves (2). The coefficient for \(\ell=3\) is \(n/2\). Rank is exactly one because the entry for \(\ell=3,d=0\) in (3) is nonzero for all \(m\ge2\); rank is at most one by (2).

**3. Exact degree classes.** Taking \(f(t)=\mathbf1_{\{t=d\}}\) in (1), and using \(4d(m-d)-m(m-1)=m-(2d-m)^2\), gives (3). The stated classification follows from the strictly positive prefactors. Integer solutions of \((2d-m)^2=m\) exist exactly when \(m\) is a square, with the two stated indices (whose parity is automatically integral).

**4. Cumulative thresholds.** The binomial identity
\[
d(m-d)p_m(d)=\frac{m(m-1)}4p_{m-2}(d-1)
\]
and the convolution \(\operatorname{Bin}(m,1/2)\overset{d}=\operatorname{Bin}(m-2,1/2)+\operatorname{Bin}(2,1/2)\) give
\[
\operatorname{Cov}(D(m-D),\mathbf1_{\{D\ge k\}})
=\frac{m(m-1)}{16}
\bigl[p_{m-2}(k-1)-p_{m-2}(k-2)\bigr].
\]
Substitution into (1) proves (4). Because the binomial mass \(p_{m-2}\) is symmetric and unimodal, the displayed difference is positive for \(2k<m+1=n\), zero for equality, and negative for \(2k>n\), including boundary values where one mass vanishes. This proves the sign classification without limiting arguments.

## Verification

The companion `verification/check_cycles.py` uses only Python's standard library and exact rational arithmetic. It exhaustively enumerates the \(2^{\binom n2}\) labeled tournaments for every \(3\le n\le6\), counts directed simple cycles directly, and compares all exact degree-histogram and threshold covariances with (3)–(4). All **90** exact finite covariance comparisons pass. It separately evaluates **89,996** finite parameter/sign comparisons for \(3\le n\le300\). These finite checks support, but do not constitute, the proof of the all-\(n\) theorem.

To reproduce: `python verification/check_cycles.py` from the directory containing that file. Runtime and storage scale exponentially with \(n\) in the exhaustive enumeration; the script intentionally stops exhaustive enumeration at six vertices.

## Relationship to prior work

Classical work relates the number of cyclic triples to the tournament score sequence. Linial and Morgenstern (2014 preprint, subsequently 2016 journal paper) address extremal four-cycle counts at prescribed three-cycle density, using different questions and methods. Komarov and Mackey (2014 preprint, subsequently 2017 journal paper) give a deterministic five-cycle formula in terms of **edge scores**, which are richer than the outdegree histogram. Neither cited theorem asserts (1)–(4) for uniformly random tournaments; the current result concerns finite-size joint **covariances** and covers every cycle length.

Kuo, Liu, Ribas, and Zhou (2019, Theorem 1.4) bound the number of tournaments with a prescribed number of restricted cycles by a shifted sieve; those counting bounds do not specify joint covariances with vertex score classes. The all-length proportionality is compatible with deterministic score-sequence constraints on cyclic triples, but it does not follow merely from the fact that cyclic-triple counts are degree-determined: the expectation of longer-cycle counts conditional on a single vertex degree must still be evaluated. Existing motif-count and orthogonal-projection methods may yield an implicit derivation; no priority claim beyond the assessed explicit theorem is made.

## Limitations

The conclusions are covariances only, not mutual independence, conditional monotonicity of full cycle counts, or comparison of their full distributions. Degree counts are dependent, and their total is the deterministic vertex count; "rank one" concerns the cross-covariance matrix, not the covariance matrix of the histogram itself. The literature comparison has not established independent novelty certification. A 2006 cycle-census work in a Bernoulli directed-graph null could not be examined in full, leaving a residual risk of equivalent general moment methods.

## References

1. N. Linial and A. Morgenstern, *On the number of 4-cycles in a tournament*, arXiv:1405.1576v1 (first posted 2014-05-07), https://arxiv.org/abs/1405.1576.
2. N. Komarov and J. Mackey, *On the number of 5-cycles in a tournament*, arXiv:1410.6828v1 (first posted 2014-10-24), https://arxiv.org/abs/1410.6828; published in *Journal of Graph Theory* 86 (2017), 341–356.
3. W. Kuo, Y.-R. Liu, S. Ribas, and K. Zhou, *The Shifted Turán Sieve Method on Tournaments*, *Canadian Mathematical Bulletin* 62 (2019), 841–855, https://doi.org/10.4153/S000843951900016X.
4. C. T. Butts, *Cycle Census Statistics for Exponential Random Graph Models* (2006), https://escholarship.org/uc/item/4719h8d2 (available summary only in the present literature assessment).
