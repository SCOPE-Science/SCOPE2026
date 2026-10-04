# Sharp logarithmic support envelope for Abelian pattern Sturmian words
## Finding
Let \(x\) be an Abelian pattern Sturmian word. By the incidence-forest characterization of Zeng, Xue and Zeng, after possibly interchanging the two letters one may write \(x=\mathbf 1_D\), where \(D=\{d_0<d_1<\cdots\}\subset\mathbb N_0\) is infinite and its bipartite sum-incidence graph \(\Gamma_D\) is a forest. Then, for every integer \(N\ge0\),
\[
\sum_{\substack{d\in D\\ d\le N}}(d+1)\le 2N+1.
\]
Consequently, for every \(n\ge0\),
\[
d_n\ge 2^n-1,
\]
and for every \(N\ge0\),
\[
|D\cap[0,N]|\le 1+\lfloor\log_2(N+1)\rfloor.
\]
The bounds are simultaneously sharp. For
\[
D_*=\{2^n-1:n\ge0\},
\]
one has \(d_{n+1}=2d_n+1>2d_n\), so Proposition 7.14 of Zeng--Xue--Zeng implies that \(\Gamma_{D_*}\) is a forest. Hence \(\mathbf 1_{D_*}\) is Abelian pattern Sturmian, with \(d_n=2^n-1\) and
\[
|D_*\cap[0,N]|=1+\lfloor\log_2(N+1)\rfloor.
\]
Thus the logarithmic prefix-occupancy envelope is exact.

## Assumptions and scope
An Abelian pattern Sturmian word is understood in the sense of Zeng, Xue and Zeng: its Abelian maximal pattern complexity at every positive pattern size is the least positive integer \(m\) satisfying \(\binom{m}{2}\ge k\). Their Theorem E states that such a word is, after relabeling, exactly a characteristic word \(\mathbf 1_D\) whose graph \(\Gamma_D\) is a forest; \(\Gamma_D\) has two disjoint copies of \(\mathbb N_0\) as its vertex classes and an edge \((r,s)\) exactly when \(r+s\in D\).

The theorem concerns this binary extremal class. It does not assert the same logarithmic envelope for arbitrary Sidon sets or for words over three or more letters.

## Proof
Fix \(N\ge0\). Consider the finite induced subgraph of \(\Gamma_D\) on the left vertices \(0,1,\ldots,N\) and the right vertices \(0,1,\ldots,N\). It has \(2N+2\) vertices. Because \(\Gamma_D\) is a forest, this induced graph is a forest and therefore has at most \(2N+1\) edges.

For each \(d\in D\) with \(d\le N\), there are exactly \(d+1\) edges in this induced graph whose endpoint labels sum to \(d\), namely
\[
(0,d),(1,d-1),\ldots,(d,0).
\]
The edge sets coming from distinct values of \(d\) are disjoint. The induced graph can also contain edges whose endpoint labels sum to a value in \(D\cap(N,2N]\), but discarding those edges only decreases its edge count. Hence
\[
\sum_{\substack{d\in D\\ d\le N}}(d+1)\le |E(\Gamma_D[0,\ldots,N;0,\ldots,N])|\le 2N+1.
\]
This proves the weighted prefix inequality.

Now put \(N=d_n\). The weighted inequality gives
\[
\sum_{j=0}^n(d_j+1)\le 2d_n+1,
\]
so
\[
d_n\ge\sum_{j=0}^{n-1}(d_j+1).
\]
Set \(a_j=d_j+1\). Then \(a_0\ge1\) and
\[
a_n\ge 1+\sum_{j=0}^{n-1}a_j.
\]
Induction yields \(a_n\ge2^n\), because \(a_j\ge2^j\) for \(j<n\) implies
\[
a_n\ge1+\sum_{j=0}^{n-1}2^j=2^n.
\]
Thus \(d_n\ge2^n-1\).

If \(k=|D\cap[0,N]|\ge1\), then \(d_{k-1}\le N\), whence
\[
2^{k-1}-1\le N.
\]
Therefore \(k\le1+\lfloor\log_2(N+1)\rfloor\).

For sharpness, take \(D_*=\{2^n-1:n\ge0\}\). Its increasing enumeration satisfies
\[
d_{n+1}=2d_n+1>2d_n.
\]
Proposition 7.14 of Zeng--Xue--Zeng then gives that \(\Gamma_{D_*}\) is a forest, and their Theorem E makes \(\mathbf1_{D_*}\) Abelian pattern Sturmian. For this support, the occurrence-position bound is an equality for every \(n\), the counting bound is an equality for every \(N\), and the weighted prefix inequality is an equality whenever \(N=d_n\).

## Verification
The proof uses only two nontrivial inputs from the cited 2026 source: Theorem E, which identifies Abelian pattern Sturmian words with characteristic words of incidence-forest supports, and Proposition 7.14, which certifies forestness from the strict inequalities \(d_{n+1}>2d_n\). Both statements were checked in the full arXiv text. The remaining steps are finite-graph edge counting and induction.

A boundary check at \(N=0\) gives \(d_0+1\le1\) only when \(0\in D\); otherwise the left side is zero. The derived assertion \(d_0\ge0\) is always valid. For the extremal support \(D_*\), \(d_0=0\), and all recurrence inequalities hold from \(n=0\) onward.

No finite experiment is used as evidence for the infinite statement.

## Relationship to prior work
Zeng, Xue and Zeng prove the exact incidence-forest characterization. Their Lemma 7.5 derives only the weaker Sidon consequences: gaps tend to infinity and, in an interval of length \(L\) containing \(h\) support points, \(\binom{h}{2}\le L-1\). They then note zero upper Banach density. Proposition 7.14 provides a sufficient growth condition \(d_{n+1}>2d_n\) and illustrates it with \(D=\{3^j:j\ge0\}\). The exact weighted prefix inequality, exponential lower envelope \(d_n\ge2^n-1\), logarithmic counting envelope, and the sharp extremizer \(D_*=\{2^n-1:n\ge0\}\) are not stated in the inspected source.

The 2013 work of Kamae, Widmer and Zamboni introduced the Abelian maximal-pattern framework and proved lower bounds for recurrent aperiodic words; its published abstract does not contain the incidence-forest structure used here.

## Limitations
The argument is specific to the forest characterization of the binary Abelian pattern Sturmian class. Sidon sets alone can be substantially denser, so the logarithmic envelope should not be transferred to every word satisfying only the three-pattern condition. The literature comparison included targeted searches and full-text inspection of the 2026 source, but an equivalent consequence could conceivably appear under different terminology in broader additive-combinatorics or graph-theoretic literature.

## References
1. Qingcheng Zeng, Yumei Xue, Cheng Zeng, “Abelian maximal pattern complexity and extremal words,” arXiv:2609.28059v1, 23 September 2026. In particular Theorem E, Lemma 7.5, Proposition 7.14 and Example 7.15.
2. Teturo Kamae, Steven Widmer, Luca Q. Zamboni, “Abelian maximal pattern complexity of words,” Ergodic Theory and Dynamical Systems 35 (2015), 142–151; first published online 13 August 2013, doi:10.1017/etds.2013.51.
