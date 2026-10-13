# A motif-universal sign transition for leaf covariance in fixed-edge random graphs

## Finding

For a uniformly sampled simple graph \(G\sim G(n,m)\), let \(L\) count vertices of degree exactly one and \(X_H\) count non-induced copies of a fixed graph \(H\) with minimum degree at least two. Write \(h=|V(H)|\), \(e=|E(H)|\), \(N=\binom n2\), and \(B=\binom{n-1}{2}\). For every integer \(n\ge h+1\) and \(0\le m\le N\), the covariance is zero if \(m<e\) or \(m>B+1\). Otherwise,

\[
\operatorname{Cov}(L,X_H)=\mathbb E[L]\mathbb E[X_H]\left(R_{n,h,e}\left(1-\frac em\right)-1\right),\qquad
R_{n,h,e}=\frac{n-h}{n}\frac{(N)_e}{(B)_e},
\]

where \((z)_e=z(z-1)\cdots(z-e+1)\) is the falling factorial. Throughout \(e\le m\le B+1\), the two expectations are positive. If \(R_{n,h,e}\le1\), the covariance is strictly negative. If \(R_{n,h,e}>1\), define

\[
m_*(n,h,e)=\frac{eR_{n,h,e}}{R_{n,h,e}-1}.
\]

The covariance is negative, zero, or positive exactly as the integer \(m\) is less than, equal to, or greater than \(m_*\), subject to the feasible interval. **This finite sign classification depends on the motif only through \(h\) and \(e\), not its internal shape.** An upper positive interval may be empty if its threshold exceeds the feasible range.

For each fixed \(H\) and each sequence with \(m/n\to c\in(0,\infty)\),

\[
\frac{\operatorname{Cov}(L,X_H)}{\mathbb E[X_H]}
\longrightarrow 2c e^{-2c}\left(2e-h-\frac ec\right).
\]

Consequently the asymptotic sign changes at \(c_H=e/(2e-h)\); for every fixed \(H\) the finite threshold satisfies \(m_*/n\to c_H\). For triangles \(H=K_3\), every \(n\ge5\) has a particularly sharp integer transition: covariance is negative for \(3\le m\le n\), positive for \(n+1\le m\le B+1\), and zero in the degenerate ranges. For \(n=4\), the continuous cutoff is \(15/4\). In the triangular sparse limit,

\[
\operatorname{Cov}(L,X_{K_3})\longrightarrow 8c^3(c-1)e^{-2c}.
\]

By contrast, in the edge-independent model \(G(n,p)\) for \(0<p<1\), the exact covariance is always negative:

\[
\operatorname{Cov}(L,X_H)=-\frac hn\,\mathbb E[L]\mathbb E[X_H].
\]

Thus fixing the edge count changes the sign of a natural dependence, including for the triangle statistic.

## Assumptions and scope

All graphs are finite, simple, undirected, and labeled at the ambient-graph level. The fixed motif \(H\) may be disconnected, but has \(h\ge3\) vertices and minimum degree at least two. The number \(X_H\) is the count of distinct edge sets of copies of \(H\), not induced copies. No assumption of motif balance, regularity, or connectedness is required. Let \(a_H=|\operatorname{Aut}(H)|\). The hypotheses \(n\ge h+1\) and minimum degree at least two imply \(e\le\binom h2\le B\), making all denominators well defined. The finite classification covers all integers \(0\le m\le N\). The asymptotics hold with \(H\) fixed; they do not claim uniformity for motifs growing with \(n\).

## Proof

A specified vertex \(v\) has degree one with probability

\[
\Pr(\deg(v)=1)=(n-1)\frac{\binom B{m-1}}{\binom Nm},
\]

where a binomial coefficient outside its natural integer range is interpreted as zero. Therefore, when \(1\le m\le B+1\),

\[
\mathbb E[L]=n(n-1)\frac{\binom B{m-1}}{\binom Nm}.
\]

A fixed embedding of \(H\) is present with probability \((m)_e/(N)_e\); the distinct edge-set embeddings number \((n)_h/a_H\), because \(H\) has no isolated vertices. Hence

\[
\mathbb E[X_H]=\frac{(n)_h}{a_H}\frac{(m)_e}{(N)_e}.
\]

Condition on \(\deg(v)=1\). Exactly one edge incident to \(v\) is present, and the remaining \(m-1\) edges are uniformly chosen among the \(B\) edges not incident to \(v\). Every copy of \(H\) must avoid \(v\), since every vertex of \(H\) has degree at least two. Consequently

\[
\mathbb E[X_H\mid\deg(v)=1]=\frac{(n-1)_h}{a_H}\frac{(m-1)_e}{(B)_e}.
\]

Exchangeability gives \(\mathbb E[LX_H]=\mathbb E[L]\mathbb E[X_H\mid\deg(v)=1]\). Subtracting products of means and using \((m-1)_e/(m)_e=(m-e)/m\) yields the exact formula. If \(m<e\), every \(X_H=0\); if \(m>B+1\), no vertex can have degree one, so \(L=0\). For feasible positive means the bracket is strictly increasing in \(m\), giving the complete sign rule.

For fixed \(h,e\), expansion of the finite products gives

\[
R_{n,h,e}=1+\frac{2e-h}{n}+O(n^{-2}).
\]

Since \(e\ge h\), the coefficient \(2e-h\) is strictly positive. Thus \(m_*/n\to e/(2e-h)\), and substituting \(m/n\to c\) into the covariance formula, together with \(\mathbb E[L]/n\to2ce^{-2c}\), proves the normalized limit.

For triangles an elementary simplification gives

\[
R_{n,3,3}=\frac{(n+1)(n^2-n-4)}{n(n^2-3n-2)},\qquad
m_*(n,3,3)=\frac{3(n+1)(n^2-n-4)}{3n^2-3n-4}.
\]

The differences from consecutive integers are

\[
m_*-n=\frac{3n^2-11n-12}{3n^2-3n-4}>0,\quad
m_*-(n+1)=\frac{-8(n+1)}{3n^2-3n-4}<0
\]

for every \(n\ge5\). This proves the exact integer cutoff. For fixed-edge triangles, \(\mathbb E[X_{K_3}]\to4c^3/3\) when \(m/n\to c\), yielding the absolute covariance limit.

In \(G(n,p)\), conditioning on \(\deg(v)=1\) leaves all edges not incident to \(v\) independent Bernoulli \(p\). Every \(H\)-copy again avoids \(v\), giving \(\mathbb E[X_H\mid\deg(v)=1]=(n-h)\mathbb E[X_H]/n\), and hence the strictly negative binomial-model identity.

## Verification

Run `python3 check.py` using only the Python 3 standard library. The checker independently constructs all non-induced motif embeddings and exhaustively enumerates every labeled host graph on four, five, or six vertices. It tests seven structurally distinct motifs (triangles, two cycles, diamond, four-clique, house, bowtie), comparing \(163\) exact-rational covariance cells against the analytic formula. It also tests \(867049\) exact-rational finite sign cells over a broad parameter grid and checks the triangle cutoff for every \(5\le n\le1000\). Finite enumeration is corroborative; all universal assertions above follow analytically.

## Relationship to prior work

Goldstein's work on the Erdős–Rényi vertex-degree count treats degree-frequency statistics and a normal approximation in the independent-edge setting [1]. Stark and Wormald's fixed-edge analysis studies counts of a fixed motif and states the known expectation formula for \(X_H\) [2, Introduction, equation preceding its Poisson discussion]. These marginal counting components are prior knowledge. The new statement considered here is their exact mixed covariance with the number of degree-one vertices **under a fixed edge count**, including its motif-shape invariance and sharp sign transition. The edge-independent covariance above is a distinct model and does not imply the fixed-edge sign reversal. No assertion is made that this result could not be derived implicitly from other classical factorial-moment identities.

## Limitations

The statistic counts non-induced copies only, and the derivation depends crucially on minimum motif degree at least two. The sign cutoff can lie outside the feasible edge range for some small host graphs and motifs. The asymptotics hold for fixed motifs only, and no claim is made for other degree counts, induced motifs, or nonuniform graph models. Historical coverage in older random-graph moment literature has not been exhaustively ruled out.

## References

[1] L. Goldstein, *A Berry–Esseen bound with applications to vertex degree counts in the Erdős–Rényi random graph*, arXiv:1005.4390, first submitted 24 May 2010. https://arxiv.org/abs/1005.4390

[2] D. Stark and N. Wormald, *The probability of nonexistence of a subgraph in a moderately sparse random graph*, arXiv:1608.05193, first submitted 18 August 2016. https://arxiv.org/abs/1608.05193
