# A sharp tree-size covariance transition between isolated vertices and motif counts

## Finding

Let \(n\ge4\), \(N=\binom n2\), and \(P=\binom{n-1}2\). Let \(H\) be any nonempty simple graph with **no isolated vertices**, \(v=|V(H)|\in[2,n-1]\), and \(e=|E(H)|\). Write \(I\) for the number of isolated vertices of a random graph and \(X_H\) for the number of distinct **not-necessarily-induced** copies of \(H\) (injective edge-preserving embeddings divided by \(|\operatorname{Aut}(H)|\)).

For \(G(n,m)\), whenever \(e\le m\le P\), put
\[
R_{n,v,e}=\frac{n-v}{n}\frac{(N)_e}{(P)_e},\qquad (a)_b=\prod_{j=0}^{b-1}(a-j).
\]
Then
\[
\operatorname{Cov}_{n,m}(I,X_H)
=\mathbb E_{n,m}[I]\,\mathbb E_{n,m}[X_H](R_{n,v,e}-1),
\]
where the two expectations are strictly positive. Thus the **sign is independent of the fixed edge count** \(m\) and of the isomorphism type of \(H\) once \((v,e)\) are fixed. For \(m<e\) or \(m>P\), the covariance vanishes identically. In contrast, for \(0<p<1\),
\[
\operatorname{Cov}_{n,p}(I,X_H)
=-\frac vn\mathbb E_{n,p}[I]\,\mathbb E_{n,p}[X_H]<0.
\]

A particularly sharp universal transition holds for **all trees**, regardless of shape. Set \(e=v-1\) and \(R_{n,v}=R_{n,v,v-1}\). Then \(R_{n,2}=1\) and, for \(2\le v\le n-2\),
\[
\frac{R_{n,v+1}}{R_{n,v}}-1
=\frac{(n-2)(n+1-2v)}{2(n-v)(P-v+1)}.
\]
For every \(n\ge7\), the tree-size sequence is initially strictly above one and eventually strictly below one, with **exactly one positive-to-negative sign transition** (a zero at one intermediate integer is possible). In particular, the covariance with the count of any three-vertex tree is positive, while its covariance with the count of any \((n-1)\)-vertex tree is negative. For instance, at \(n=7\), \(R_{7,3}=8/7\) and \(R_{7,6}=969/1001\).

For any sequence of trees with vertex counts \(v_n/n\to\alpha\in(0,1)\),
\[
\log R_{n,v_n}\longrightarrow\log(1-\alpha)+2\alpha.
\]
The unique positive zero \(\alpha_*\) of \(\log(1-\alpha)+2\alpha=0\) is
\[\alpha_*=0.79681213002002\ldots.\]
Thus fixed-edge covariance is eventually positive when \(0<\alpha<\alpha_*\) and negative when \(\alpha_*<\alpha<1\), while the independent-edge covariance remains negative in both regimes. More generally, when \(v_n/n\to\alpha\in(0,1)\) and \(e_n/n\to\beta\in(0,\infty)\), the log-factor tends to \(\log(1-\alpha)+2\beta\); only strict nonzero limits determine the eventual sign.

## Assumptions and scope

All random graphs are labeled, simple, undirected graphs with vertex set \([n]\). The edge count \(m\) is a deterministic integer between zero and \(N\). The requirement of no isolated vertices in \(H\) is essential: otherwise a host isolated vertex could belong to a copy of \(H\), invalidating the factorization. Counts are of non-induced copies and may be zero in a particular sample. No asymptotic restriction on the shape or maximum degree of a tree is imposed. The asymptotic sign statements exclude the critical equality \(\alpha=\alpha_*\) and, in the general motif case, the critical line \(2\beta=-\log(1-\alpha)\).

## Proof

Fix a vertex \(u\). In \(G(n,m)\), the isolation probability is
\[
q=\Pr(u\text{ isolated})=\frac{\binom Pm}{\binom Nm}
\]
when \(m\le P\), and zero otherwise. Conditional on \(u\) being isolated, the \(m\) surviving edges are uniformly selected from the \(P\) possible edges on the remaining \(n-1\) vertices. Because \(H\) has no isolated vertices, all of its copies necessarily avoid \(u\). Consequently,
\[
\mathbb E[X_H\mid u\text{ isolated}]
=\frac{(n-1)_v}{|\operatorname{Aut}(H)|}\frac{(m)_e}{(P)_e},
\]
whereas direct embedding enumeration gives
\[
\mathbb E[X_H]=\frac{(n)_v}{|\operatorname{Aut}(H)|}\frac{(m)_e}{(N)_e},
\qquad \mathbb E[I]=nq.
\]
Summing \(\mathbb E[\mathbf1_{\{u\text{ isolated}\}}X_H]\) over all \(u\) and subtracting \(\mathbb E[I]\mathbb E[X_H]\) proves the stated exact fixed-edge covariance. The boundary cases are deterministic zeros of \(X_H\) or \(I\).

For \(G(n,p)\), isolation of \(u\) leaves the other edges independently distributed, so
\[
\mathbb E[X_H\mid u\text{ isolated}]
=\frac{(n-1)_v}{|\operatorname{Aut}(H)|}p^e
=\frac{n-v}{n}\mathbb E[X_H].
\]
The analogous sum yields the negative independent-edge formula.

For trees substitute \(e=v-1\) into the ratio. Cancelling successive falling-factorial terms gives the displayed exact adjacent ratio. It increases with \(v\) while \(2v<n+1\), is equal between two adjacent values only if \(2v=n+1\), and decreases thereafter. Its first terms are \(R_{n,2}=1\) and \(R_{n,3}=(n+1)/n>1\). To prove the last term is less than one for \(n\ge7\), note
\[
\log R_{n,n-1}
=-\log n+\sum_{j=0}^{n-3}\log\!\left(1+\frac{n-1}{P-j}\right)
\le-\log n+\frac{2(n-2)(n-1)}{n^2-5n+8}.
\]
The right side is strictly negative at \(n=12\) and thereafter, since \(\log n\) increases while the rational correction decreases for \(n\ge12\). Direct exact evaluation gives \(R_{n,n-1}<1\) for \(n=7,8,9,10,11\). This proves the single finite sign transition.

When \(e_n=O(n)\), \(N-P=n-1\), and \(P=\Theta(n^2)\), uniformly for \(0\le j<e_n\),
\[
\log\frac{N-j}{P-j}
=\log\left(1+\frac{n-1}{P-j}\right)
=\frac2n+O(n^{-2}).
\]
Summing and adding \(\log((n-v_n)/n)\) proves the general asymptotic log-factor. In the tree case \(\beta=\alpha\). The function \(f(\alpha)=\log(1-\alpha)+2\alpha\) has \(f(0)=0\), initial derivative \(1\), strictly negative second derivative, and tends to \(-\infty\) as \(\alpha\uparrow1\), hence has exactly one root in \((0,1)\) and the stated sign regimes.

## Verification

Execute `python3 verify.py` using the Python standard library. It enumerates all \(33{,}856\) labeled simple graphs on \(4\), \(5\), and \(6\) vertices and independently computes isolated-vertex counts and six motif types (subject to \(v<n\)) using explicit edge-mask embeddings. It checks fixed-edge covariance and both marginal means against the theorem using exact rational arithmetic for all edge counts. It additionally checks the tree adjacent-ratio identity through \(n=100\) with rational arithmetic and brackets the asymptotic root. A successful execution prints `VERIFY_OK` with the number of assertions and graphs. Enumeration supports, but does not establish, the all-order theorem; the proof above is analytic.

## Relationship to prior work

Stark and Wormald, *The probability of nonexistence of a subgraph in a moderately sparse random graph* (2016), explicitly supply the standard exact expectation of a given motif count in \(G(n,m)\) (Section 1), which is used here and **not claimed as new**. Their main results concern nonexistence probabilities, small clusters, and sparse-regime expansions for motif counts, not the isolation–motif covariance or its tree-size sign transition. Chatterjee and Varadhan, *The large deviation principle for the Erdős–Rényi random graph* (2010), treat dense-graph large deviations and triangle-count phases in \(G(n,p)\), rather than finite fixed-edge mixed covariance. The contribution here is the exact mixed moment, the edge-count independence of its sign, and the shape-universal tree-size transition at the specified constant. These comparisons are based on accessible full texts, not solely titles or abstracts.

## Limitations

A source identity for motif means is elementary and known; a novelty claim is made only for the **joint covariance/sign phase diagram**, not for the independent marginal expectation. This theorem does not concern induced motif counts, isolated vertices in the motif, or the covariance at a critical asymptotic ratio where the leading log-factor vanishes. It does not assert statistical independence; zero covariance for one-edge patterns occurs because their count equals the deterministic number of edges in \(G(n,m)\). Earlier equivalent analyses in broader mixed subgraph-moment literature may exist and have not been exhaustively excluded. No independently performed audit is asserted.

## References

1. S. Chatterjee and S. R. S. Varadhan, *The large deviation principle for the Erdős–Rényi random graph*, arXiv:1008.1946, first posted 2010-08-11, https://arxiv.org/html/1008.1946v3 .
2. D. Stark and N. Wormald, *The probability of nonexistence of a subgraph in a moderately sparse random graph*, arXiv:1608.05193, first posted 2016-08-18, https://arxiv.org/html/1608.05193v1 .
