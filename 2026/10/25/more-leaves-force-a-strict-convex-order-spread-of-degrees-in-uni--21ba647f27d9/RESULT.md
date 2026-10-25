# More leaves force a strict convex-order spread of degrees in uniform labeled trees

## Finding

Fix \(n\ge 4\), sample a uniformly random labeled tree on \(\{1,\ldots,n\}\), and denote its number of leaves by \(L\). For a fixed vertex \(v\), write \(D_v\) for its degree. For every \(2\le k\le n-2\),

\[
D_v\mid\{L=k\}\ \prec_{\mathrm{cx}}\ D_v\mid\{L=k+1\},
\]

with a strict inequality of expectations for **every strictly convex** function on the degree interval \([1,n-1]\). Thus conditioning on more leaves makes the degree of each fixed vertex strictly more dispersed, even though

\[
\mathbb E[D_v\mid L=k]=2-\frac2n
\qquad(2\le k\le n-1).
\]

In particular, \(\operatorname{Cov}(L,D_v)=0\), while \(\operatorname{Cov}(L,\varphi(D_v))>0\) for every strictly convex \(\varphi\) on \([1,n-1]\), and \(\mathbb E[\sum_v D_v^2\mid L=k]\) increases strictly with \(k\).

The underlying stronger ordering is likelihood-ratio domination of the **size-biased positive Prüfer multiplicity** when the number of occupied Prüfer labels decreases by one. This supplies a finite-sample relation covering every feasible leaf count, not just a variance comparison.

## Assumptions and scope

All trees on the labeled vertex set \(\{1,\ldots,n\}\) are equally likely. A leaf means a vertex of degree exactly one. Put \(N=n-2\), \(j=n-k\); hence \(1\le j\le N\). Write \(S(t,r)\) for the Stirling number of the second kind, with \(S(0,0)=1\), and \(S(t,r)=0\) outside \(0\le r\le t\). The Prüfer sequence is a uniformly random word of length \(N\) on \(n\) symbols, and \(j\) is its number of distinct symbols. Let \(X_j\) have the law of \(D_v-1\) conditional on \(L=n-j\). Let \(Y_j\) be the positive size-bias of \(X_j\): \(\mathbb P(Y_j=c)=c\mathbb P(X_j=c)/\mathbb E X_j\), for \(c\ge1\). Convex order means inequality of expectations for all convex real functions on the finite support, with equal means.

## Proof

**1. Exact conditioned degree and size-bias laws.** Symmetry in the \(n\) symbols and the fact that exactly \(j\) symbols occur give \(\mathbb P(X_j=0)=(n-j)/n\). For \(1\le c\le N\), choose the \(c\) occurrences of the tagged symbol, and partition the remaining positions among exactly \(j-1\) nonempty labeled fibers. Dividing by the total number of words with \(j\) occupied symbols gives

\[
\mathbb P(X_j=c)=\frac{\binom Nc\,S(N-c,j-1)}{nS(N,j)}.
\tag{1}
\]

The fixed total word length and exchangeability imply \(\mathbb E X_j=N/n\), whence \(\mathbb E D_v=1+N/n\), independent of \(j\). Size-biasing (1) gives

\[
q_j(c):=\mathbb P(Y_j=c)
 =\frac{\binom{N-1}{c-1} S(N-c,j-1)}{S(N,j)}.
\tag{2}
\]

For \(j\ge2\), the support of \(q_j\) consists of \(1,\ldots,N-j+1\), whereas \(q_{j-1}\) has the strictly larger support \(1,\ldots,N-j+2\).

**2. A strict Stirling-ratio lemma.** For each integer \(r\ge2\), the quantity \(S(t,r-1)/S(t,r)\) strictly decreases in integer \(t\ge r\). To see this, the Bell polynomial \(B_t(z)=\sum_{h=1}^t S(t,h)z^h\) has simple real nonpositive zeros. Induct from \(B_1(z)=z\) using \(B_{t+1}(z)=z(B_t(z)+B_t'(z))\): if the zeros of \(B_t\) are simple and nonpositive, the equation \(1+B_t'(z)/B_t(z)=0\) has exactly one simple root between each two successive zeros and one to the left of all of them, because its left-hand side has derivative \(-\sum_i(z-\rho_i)^{-2}<0\); the new zero at \(z=0\) remains simple. By real-rootedness, the coefficients of each \(B_t\) are log-concave, so

\[
\frac{S(t,r-2)}{S(t,r-1)}\le
\frac{S(t,r-1)}{S(t,r)}.
\]

The Stirling recurrence \(S(t+1,r)=rS(t,r)+S(t,r-1)\) therefore yields, for \(R_t=S(t,r-1)/S(t,r)\),

\[
R_{t+1}=R_t\frac{r-1+S(t,r-2)/S(t,r-1)}{r+R_t}<R_t.
\tag{3}
\]

All denominators in (3) are positive on the stated range. This proof requires no asymptotic approximation.

**3. Strict likelihood-ratio order.** For \(3\le j\le N\), whenever \(q_j(c)>0\), dividing (2) at consecutive values of \(j\) gives

\[
\frac{q_{j-1}(c)}{q_j(c)}=
\frac{S(N,j)}{S(N,j-1)}
\frac{S(N-c,j-2)}{S(N-c,j-1)}.
\tag{4}
\]

The last factor increases with \(c\) by (3) with \(r=j-1\) and \(t=N-c\). At \(c=N-j+2\), only \(q_{j-1}\) has mass. Thus \(q_{j-1}\) strictly dominates \(q_j\) in the monotone likelihood-ratio order and hence strictly in first-order stochastic order. When \(j=2\), \(Y_1=N\) deterministically while \(Y_2\le N-1\); the same strict ordering holds. These statements cover every \(2\le j\le N\).

**4. Convex ordering and consequences.** For any convex \(\varphi\) define \(g(c)=[\varphi(1+c)-\varphi(1)]/c\) for integers \(c\ge1\). Secant slopes of a convex function imply that \(g\) is nondecreasing; if \(\varphi\) is strictly convex on \([1,n-1]\), it is strictly increasing. Size-biasing therefore gives

\[
\mathbb E[\varphi(1+X_j)]
=\varphi(1)+\frac Nn\,\mathbb E[g(Y_j)].
\tag{5}
\]

The strict stochastic ordering of \(Y_{j-1}\) over \(Y_j\), together with (5), proves the stated strict convex ordering upon replacing \(j\) by \(n-k\). For convex but non-strict \(\varphi\), the inequality is non-strict. Both variables have the same mean. Since \(k\mapsto\mathbb E[\varphi(D_v)\mid L=k]\) increases strictly for strictly convex \(\varphi\) and \(L\) is nondegenerate for \(n\ge4\), the elementary covariance identity using two independent copies of \(L\) proves \(\operatorname{Cov}(L,\varphi(D_v))>0\), while \(\operatorname{Cov}(L,D_v)=0\). Summing the \(n\) vertex-wise inequalities with \(\varphi(d)=d^2\) proves the quadratic-degree statement.

For reproducibility, a general factorial-moment identity follows by merging \(r\) marked Prüfer positions:

\[
\mathbb E[(X_j)_r]=\frac{(N)_r}{n}\,
\frac{S(N-r+1,j)}{S(N,j)},
\qquad 1\le r\le N.
\tag{6}
\]

In particular, \(\operatorname{Var}(D_v\mid L=n-j)=N/n-N^2/n^2+[N(N-1)/n]S(N-1,j)/S(N,j)\), strictly increasing as the number of leaves increases. At the extreme \(k=2\), the degree equals one with probability \(2/n\) and two otherwise; at \(k=n-1\), it equals \(n-1\) with probability \(1/n\) and one otherwise.

## Verification

Run `python3 check.py` from the same directory as this file. The checker uses only the Python standard library and exact fractions. It independently enumerates all Prüfer words for \(4\le n\le8\); checks the conditioned mass formulas over \(4\le n\le46\); checks all size-biased likelihood-ratio minors and all nontrivial discrete convex-hinge inequalities in those ranges; and checks the Stirling ratio lemma through row index 64. Recorded counts are in `CHECK_OUTPUT.txt`. Finite enumeration corroborates, but does not replace, the all-size proof above.

## Relationship to prior work

Remmel and Williamson (2010) give exact fixed-leaf enumeration and ranking/unranking of labeled trees using degree-revealing codes. Their leaf-count formula supplies the natural conditioning class, but their finite algorithms do not provide the cross-leaf-count convex comparison of a tagged vertex's degree. Bakhtin and Heitsch (2007) study degree frequencies of large random trees under Gibbs laws by large-deviation methods, not this exact finite conditional stochastic order. Sagitov (2026) studies multinomial allocation moments and asymptotics, but does not condition a tagged load on the number of occupied boxes. A separate exact analysis of uniform Cayley trees gives the law of leaf count conditional on a tagged degree, together with comparisons of those conditional leaf distributions. Although Bayes' formula recovers the conditional degree masses from such a joint law, a strict convex-order comparison **across different fixed leaf counts** does not follow from those prior leaf-given-degree stochastic comparisons; it requires the Stirling-ratio ordering in (3)–(5). The present claim concerns the **implication** from one conditioned law to another in convex order, not merely the formulas for each distribution.

## Limitations

The theorem applies to **uniform labeled Cayley trees** and not to uniform unlabeled trees, recursive trees, general Gibbs trees, or nonuniform Prüfer letters. All comparisons are conditional on the exact feasible number of leaves. The size-biased variable here is a Prüfer multiplicity, not the actual degree sampled proportionally to degree. No independence or concentration theorem for all vertex degrees is asserted. The proof is complete for all finite \(n\ge4\), but a classical general result on occupancy-size stochastic ordering might encompass the same conclusion; historical priority requires separate assessment.

## References

1. Yuri Bakhtin and Christine Heitsch, *Large Deviations for Random Trees*, arXiv:0712.2253 (public 2007-12-13), https://arxiv.org/abs/0712.2253.
2. Jeffrey B. Remmel and S. Gill Williamson, *Ranking and unranking trees with a given number or a given set of leaves*, arXiv:1009.2060 (public 2010-09-10), https://arxiv.org/abs/1009.2060.
3. Serik Sagitov, *The Multinomial Allocation Model and the Random Box Load*, arXiv:2604.15152 (public 2026-04-16), https://arxiv.org/abs/2604.15152. Supporting comparison only; not the archival anchor.
