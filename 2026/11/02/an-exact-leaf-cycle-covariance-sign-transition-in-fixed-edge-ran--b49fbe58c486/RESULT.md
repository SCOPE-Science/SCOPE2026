# An exact leaf–cycle covariance sign transition in fixed-edge random graphs

## Finding

Let \(G(n,m)\) be uniformly distributed among simple graphs on \(n\) labeled vertices with exactly \(m\) edges, with \(0\le m\le\binom n2\). Write \(L\) for the number of vertices of degree exactly one and \(T\) for the number of unordered triangles. **For every \(n\ge5\)**,
\[
\operatorname{Cov}(L,T)
\begin{cases}
<0,&3\le m\le n,\\
>0,&n+1\le m\le\binom{n-1}{2}+1,\\
=0,&0\le m<3\text{ or }\binom{n-1}{2}+1<m\le\binom n2.
\end{cases}
\]
No intermediate edge count gives zero covariance. This is an exact finite-size reversal at the first integer edge count above the vertex count. In the sparse scaling \(m=\lfloor cn\rfloor\), for fixed \(c>0\),
\[
\operatorname{Cov}_{G(n,m)}(L,T)\longrightarrow
8c^3(c-1)e^{-2c}.
\]
In particular the sign reversal remains nondegenerate in the sparse limit for \(c\ne1\).

More generally, fix any simple graph \(H\) with \(h\ge3\) vertices, \(e\) edges, **minimum degree at least two**, and automorphism-group order \(a_H\). Count distinct not-necessarily-induced, unlabeled copies by injective edge-preserving embeddings divided by \(a_H\), calling this number \(X_H\). For all \(n\ge h+1\) and \(e\le m\le A+1\), where \(N=\binom n2\) and \(A=\binom{n-1}{2}\),
\[
\boxed{
\operatorname{Cov}(L,X_H)
=\mathbb EL\,\mathbb EX_H
\left[\frac{n-h}{n}\frac{m-e}{m}\frac{(N)_{\underline e}}{(A)_{\underline e}}-1\right].
}
\]
Here \((z)_{\underline e}=z(z-1)\cdots(z-e+1)\). The expectations are strictly positive in this range. Thus the covariance sign, conditional on the motif's \((h,e)\), is **independent of its isomorphism type**, and the normalized covariance increases strictly with \(m\), so it has at most one change from negative to positive. For \(m<e\) or \(m>A+1\), the covariance is zero. The formula includes disconnected motifs whose components all have minimum degree at least two.

## Assumptions and scope

All graphs are finite, labeled, undirected, simple, and loopless. The distribution \(G(n,m)\) is uniform on its exact-size sample space, not the independent-edge distribution \(G(n,p)\). Motifs are counted non-induced: extra edges between their vertices are permitted. For the general theorem, \(3\le h\le n-1\), \(H\) is fixed, \(\delta(H)\ge2\), \(e=|E(H)|\le\binom h2\le A\), and \(0\le m\le N\). In the displayed general formula, \(e\le m\le A+1\); all other edge counts have the separately stated zero covariance. Expectations and covariances are taken under the same fixed-size graph law. The falling factorial is defined even when its value is zero at a nonnegative integer argument smaller than its order.

The triangle sign classification starts at \(n=5\) because the exceptional case \(n=4\) has negative covariance at \(m=3\), positive covariance at \(m=4\), and zero at all other edge counts. A single motif may have no strict sign change over the available integer support; the general statement only asserts monotonicity of the normalized bracket and at most one crossing.

## Proof

**Exact leaf conditioning.** Fix a vertex \(v\) and let \(B_v\) be the event that \(v\) has degree one. Choosing its unique incident edge and then the remaining \(m-1\) edges outside its star gives
\[
\Pr(B_v)=\frac{(n-1)\binom A{m-1}}{\binom Nm}.
\]
When \(e\le m\le A+1\), this probability is strictly positive. Given \(B_v\), the graph induced by the other \(n-1\) vertices has exactly \(m-1\) edges uniformly selected from their \(A\) possible edges; the unique neighbor of \(v\) is uniform and immaterial to this induced graph. Because every vertex in \(H\) has degree at least two, no copy of \(H\) can contain \(v\) on the event \(B_v\). Consequently
\[
\mathbb E[X_H\mid B_v]
=\frac{(n-1)_{\underline h}}{a_H}
  \frac{(m-1)_{\underline e}}{(A)_{\underline e}}.
\]
Each injective embedding specifies \(e\) required edges. Since all \(m\)-edge subsets are equiprobable, the unconditional expectation is
\[
\mathbb EX_H=
\frac{(n)_{\underline h}}{a_H}
\frac{(m)_{\underline e}}{(N)_{\underline e}}.
\]
Use \(L=\sum_{v=1}^n\mathbf1_{B_v}\) and vertex symmetry to obtain
\[
\operatorname{Cov}(L,X_H)=n\Pr(B_v)
\left(\mathbb E[X_H\mid B_v]-\mathbb EX_H\right).
\]
Dividing the two motif expectations uses exactly
\[
\frac{(n-1)_{\underline h}}{(n)_{\underline h}}=\frac{n-h}{n},
\qquad
\frac{(m-1)_{\underline e}}{(m)_{\underline e}}=\frac{m-e}{m}.
\]
These yield the boxed identity, with \(\mathbb EL=n\Pr(B_v)\). For \(m<e\), \(X_H=0\) surely; for \(m>A+1\), \(L=0\) surely, because after specifying one incident edge the other \(m-1\) edges cannot all avoid \(v\). These establish the zero ranges. The normalized bracket equals \(K_{n,h,e}(1-e/m)-1\), where
\[
K_{n,h,e}=\frac{n-h}{n}\frac{(N)_{\underline e}}{(A)_{\underline e}}>0.
\]
Its exact difference at consecutive edge counts is \(K_{n,h,e}e/[m(m+1)]>0\). Therefore any sign reversal must be unique and from negative to positive. No feature of \(H\) beyond \(h,e\) enters this factor.

**Sharp triangle threshold.** Put \(H=K_3\), \(h=e=3\). Direct cancellation yields
\[
K_{n,3,3}=\frac{(n+1)(n^2-n-4)}{n(n^2-3n-2)}.
\]
The continuous zero of the normalized covariance bracket is
\[
m_*(n)=\frac{3(n+1)(n^2-n-4)}{3n^2-3n-4}.
\]
For every \(n\ge5\), the denominator is positive and
\[
m_*(n)-n=\frac{3n^2-11n-12}{3n^2-3n-4}>0,
\qquad
m_*(n)-(n+1)=-\frac{8(n+1)}{3n^2-3n-4}<0.
\]
The first numerator is positive already at \(n=5\) and increases thereafter. Hence \(n<m_*(n)<n+1\). Because the normalized bracket is strictly increasing in the integer \(m\), it is negative through \(m=n\) and positive from \(m=n+1\), within the nondegenerate support. At \(n=4\), substitution gives the stated exception. At \(n\ge5\), the positive support is nonempty because \(A+1\ge n+1\).

**Sparse covariance.** With \(m=\lfloor cn\rfloor\), \(N=\binom n2\), fixed \(c>0\), direct fixed-size inclusion probabilities yield
\[
\mathbb EL\sim 2cn e^{-2c},
\qquad \mathbb ET\longrightarrow\frac{(2c)^3}{6}=\frac43c^3.
\]
For example \(\Pr(B_v)=(n-1)\binom A{m-1}/\binom Nm\sim2ce^{-2c}\), from a finite product of the exact hypergeometric probabilities. Expansion of the rational bracket gives
\[
K_{n,3,3}(1-3/m)-1
=\frac{3-3/c}{n}+O(n^{-2})
\]
for fixed \(c\) (the floor only changes the order-\(n^{-2}\) term). Multiplication proves the displayed limit. For a fixed general motif, expansion gives \(K_{n,h,e}=1+(2e-h)/n+O(n^{-2})\); this implies that any positive continuous crossing location, when present for large \(n\), satisfies \(m_*/n\to e/(2e-h)\). Since \(\delta(H)\ge2\), \(2e-h>0\).

## Verification

`python3 check.py` (Python 3 standard library only) reproduces the formula by enumerating all labeled simple graphs on four, five, and six vertices, grouping by the exact edge count, measuring degree-one vertices and triangle/four-cycle counts, and matching their exact rational mixed covariances. Additional exact rational checks cover the all-size triangle sign split and the motif formula for triangle, four-cycle, five-cycle, and four-clique parameter families up to forty vertices. The packaged verifier reports `PASS: 68 exhaustive graph-ensemble checks; 39329 exact rational formula/sign checks; total 39397`.

The enumerations test finite instances only. The proof for all integer sizes and all eligible motifs is the conditioning and factorization argument above, together with the explicit rational root inequalities. No independence or machine certification is claimed.

## Relationship to prior work

Janson, *Monotonicity, asymptotic normality and vertex degrees in random graphs*, arXiv:math/0605642 (first publicly submitted May 24, 2006), proves asymptotic distributional results for degree-class counts in both the independent-edge and fixed-edge models. Its Section 4, especially Theorem 4.1, concerns degree-count covariance profiles, not a finite mixed covariance of degree-one counts and cyclic subgraph counts. Alm, Janson, and Linusson, *Correlations for paths in random orientations of \(G(n,p)\) and \(G(n,m)\)*, arXiv:0906.0720 (first submitted June 3, 2009), compare edge ensembles for oriented reachability correlations; their objects and statistics differ.

Classical factorial-moment formulas can recover the unconditional motif expectation, and degree-count identities can recover the leaf expectation. The result here is specifically the **mixed fixed-edge identity and its sharp all-size triangle sign threshold**, not those established first-moment formulas. In \(G(n,p)\), the analogous covariance is always negative for motifs of minimum degree at least two:
\[
\operatorname{Cov}_{G(n,p)}(L,X_H)
=-\frac hn\mathbb EL\,\mathbb EX_H<0\quad(0<p<1).
\]
This independent-edge fact is included solely as an ensemble comparison; it is not claimed as a new theorem.

## Limitations

No induced-motif claim is made: the proof specifically counts non-induced copies and needs the minimum-degree-two assumption to rule out motif copies meeting the leaf. No stochastic dominance or monotonicity of \(\mathbb E[T\mid L]\) is asserted. The normalized bracket varies strictly with \(m\), but the raw covariance need not vary monotonically. The sparse limit is fixed-\(c\) and does not imply a uniform limit over moving \(c\). Historical-priority risk remains in general graph moment literature, including Janson's 1990 paper, whose complete text was unavailable for comparison; no priority or independence guarantee is asserted.

## References

1. Svante Janson, *Monotonicity, asymptotic normality and vertex degrees in random graphs*, arXiv:math/0605642v1 (May 24, 2006), https://arxiv.org/abs/math/0605642 . Full manuscript, especially Section 4, consulted.
2. Sven Erick Alm, Svante Janson, and Svante Linusson, *Correlations for paths in random orientations of \(G(n,p)\) and \(G(n,m)\)*, arXiv:0906.0720v1 (June 3, 2009), https://arxiv.org/abs/0906.0720 . Full open-access HTML manuscript consulted.
3. Svante Janson, *A functional limit theorem for random graphs with applications to subgraph count statistics*, Random Structures & Algorithms **1** (1990), https://doi.org/10.1002/rsa.3240010103 . Only bibliographic record and abstract inspected.
