# Unimodality of general position polynomials for generalized windmill graphs
## Finding
For integers \(n\ge 2\) and \(m\ge 1\), let
\[
W_{n,m}=K_1\vee nK_m,
\]
so that \(W_{n,m}\) consists of \(n\) cliques of order \(m+1\) sharing exactly one common hub. If \(\psi(G;x)=\sum_k \operatorname{gp}_k(G)x^k\) is the general position polynomial, then
\[
\psi(W_{n,m};x)=(1+x)^{nm}+x+n x\big((1+x)^m-1\big).
\]
Moreover, for every \(n\ge2\) and \(m\ge1\), the coefficient sequence of \(\psi(W_{n,m};x)\) is unimodal.

Equivalently, writing \(N=nm\) and \(a_k=[x^k]\psi(W_{n,m};x)\),
\[
a_0=1,\qquad a_1=N+1,\qquad
 a_k=\binom Nk+n\binom m{k-1}\quad(k\ge2),
\]
where a binomial coefficient is zero outside its natural range. The theorem includes stars \(W_{n,1}\) and friendship graphs \(W_{n,2}\).
## Assumptions and scope
Graphs are finite, simple, and undirected. A vertex set is in general position when no vertex of the set lies on a shortest path between two other vertices of the set. The parameters satisfy \(n\ge2\) and \(m\ge1\). The result concerns the balanced generalized windmill \(K_1\vee nK_m\); no assertion is made here for unequal petal sizes.
## Proof
Let \(c\) be the common hub and let the \(n\) disjoint outer cliques be the petals after deleting \(c\).

First characterize the general position sets. If \(c\notin S\), then every subset \(S\) of the \(nm\) outer vertices is in general position. Indeed, two chosen vertices in one petal are adjacent, while two chosen vertices in different petals have the unique length-two geodesic through \(c\), which is not selected. If \(c\in S\), then \(S\) is in general position exactly when all selected outer vertices lie in one petal: vertices from two different petals have \(c\) on their geodesic, whereas \(c\) together with any subset of a single petal induces a clique. Therefore
\[
\psi(W_{n,m};x)=(1+x)^{nm}+x+n x\big((1+x)^m-1\big),
\]
and the displayed coefficient formula follows.

It remains to prove unimodality. Put \(N=nm\).

For \(m=1\),
\[
a_0=1,\qquad a_1=n+1,\qquad a_2=\binom{n+1}{2},\qquad
 a_k=\binom nk\quad(k\ge3).
\]
Thus \(a_1\le a_2\), and
\[
a_3-a_2=\frac{n(n^2-6n-1)}6.
\]
For \(2\le n\le6\), one has \(a_2\ge a_3\) and the ordinary binomial tail \(\binom nk\) is nonincreasing for \(k\ge3\). For \(n\ge7\), one has \(a_2\le a_3\), and the binomial sequence from index \(3\) onward rises to its usual middle mode and then falls. Hence the full sequence is unimodal.

Now suppose \(m\ge2\). Since \(a_2-a_1=\binom N2-1\ge0\), it suffices to control later differences. For \(2\le k\le m\),
\[
a_{k+1}-a_k=
\left(\binom N{k+1}-\binom Nk\right)
+n\left(\binom mk-\binom m{k-1}\right).
\]
When \(2k\le m+1\), both summands are nonnegative. Assume instead that \(2k>m+1\).

First take \(n\ge3\). The elementary product comparison
\[
\binom{nm}{k}\ge n^k\binom mk
\]
reduces the desired inequality \(a_{k+1}\ge a_k\) to
\[
n^{k-1}(N-2k-1)(m-k+1)
\ge (k+1)(2k-m-1).
\]
Because \(k\le m\) and \(n\ge3\),
\[
N-2k-1\ge m-1\ge k-1,
\qquad
2k-m-1\le k-1.
\]
Consequently the left side is at least \(3^{k-1}(k-1)\), while the right side is at most \((k+1)(k-1)\). Since \(3^{k-1}\ge k+1\) for \(k\ge2\), all these differences are nonnegative. Thus
\[
a_0\le a_1\le\cdots\le a_{m+1}.
\]

For degrees above \(m+1\), the correction term vanishes, so \(a_k=\binom Nk\) for \(k\ge m+2\). The only possible difficulty is the transition from \(m+1\) to \(m+2\). If \(N\le2m+3\), then \(m+2\) is at or to the right of the middle of the binomial row, so whatever the sign of that single transition, the remaining tail is nonincreasing and unimodality follows. If \(N\ge2m+4\), then
\[
\binom N{m+2}-\binom N{m+1}
=\binom N{m+1}\frac{N-2m-3}{m+2}.
\]
Here \(N-2m-3\ge1\), and \(m+1\) lies on the increasing side of the binomial row. Hence \(\binom N{m+1}\ge\binom N3\). Also \(N=nm\ge8\) and \(m\ge2\), so
\[
\frac{\binom N3}{m+2}\ge n.
\]
Therefore \(a_{m+2}-a_{m+1}\ge0\). From degree \(m+2\) onward, the coefficients are an ordinary binomial tail and hence increase to the middle and then decrease. This proves unimodality for \(n\ge3\).

It remains to treat \(n=2\) and \(m\ge2\). For \(2\le k\le m-1\), a negative correction can occur only when \(2k>m+1\). Using
\[
\binom{2m}{k}\ge2^k\binom mk,
\]
it is enough to prove
\[
2^{k-1}(2m-2k-1)(m-k+1)
\ge(k+1)(2k-m-1).
\]
Write \(h=m-k\). In the negative-correction range, \(h\ge1\), \(h\le k-2\), and \(k\ge3\). The left side is at least \(2^k\), while the right side is at most \((k+1)(k-2)\); the elementary inequality \(2^k\ge(k+1)(k-2)\) for \(k\ge3\) gives the result. Hence the coefficients rise through degree \(m\). Finally,
\[
a_m=\binom{2m}{m}+2m
>\binom{2m}{m+1}+2=a_{m+1},
\]
and thereafter the binomial tail is decreasing, with the extra \(+2\) at degree \(m+1\) only strengthening the first descent. Thus the sequence is unimodal also for \(n=2\).

All parameter ranges are covered.
## Verification
The accompanying `verify.py` reconstructs the displayed coefficient formula from exact subset enumeration for the four smallest parameter pairs \((n,m)\in\{2,3\}\times\{1,2\}\). It also checks coefficient unimodality and the inequalities used in the proof for every \(2\le n\le30\) and \(1\le m\le30\). These finite checks are reproducibility support; the theorem itself is proved symbolically above.
## Relationship to prior work
Iršič, Klavžar, Rus, and Tuite introduced the general position polynomial and proved a general formula for joins. Their join formula specializes directly to the polynomial displayed above for \(K_1\vee nK_m\). The contribution here is the all-parameter unimodality theorem for this generalized windmill family. Subsequent work on explicit general position polynomials studies other structured families, including complete multipartite graphs and corona constructions.
## Limitations
The proof uses the equal-petal structure essentially. It does not establish unimodality for \(K_1\vee(K_{m_1}\cup\cdots\cup K_{m_n})\) with unequal \(m_i\), nor does it claim log-concavity, real-rootedness, or a classification of all block graphs with unimodal general position polynomials.
## References
[1] V. Iršič, S. Klavžar, G. Rus, and J. Tuite, “General position polynomials,” arXiv:2401.05696; published in *Results in Mathematics* (2024), DOI:10.1007/s00025-024-02133-3.

[2] B. A. Rather, “Explicit Formulas and Unimodality Phenomena for General Position Polynomials,” arXiv:2603.06930 (2026).
