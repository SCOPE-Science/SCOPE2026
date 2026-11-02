# Score-profile projection rigidity and square-root covariance phases for directed cycles

## Finding
Let \(\mathcal T_n\) be the uniformly random labeled tournament on \(n\ge3\) vertices: every unordered pair is independently oriented in either direction with probability \(1/2\). For each \(3\le r\le n\), let \(C_{r,n}\) count directed simple cycles of length \(r\), where cyclic rotations represent the same cycle. For \(0\le k\le n-1\), let \(N_{k,n}\) count vertices with outdegree exactly \(k\).

Set \(B_{n,k}=2^{-(n-1)}\binom{n-1}{k}\). Then the following exact identity holds simultaneously for all permitted \(n,r,k\):
\[
\operatorname{Cov}(C_{r,n},N_{k,n})
=\frac{(n)_{\underline r}}{2^r}\,B_{n,k}\,
\frac{(n-1)-\bigl(2k-(n-1)\bigr)^2}{(n-1)(n-2)}.
\]
Here \((n)_{\underline r}=n(n-1)\cdots(n-r+1)\).

The sign is strictly positive when \(\lvert 2k-(n-1)\rvert<\sqrt{n-1}\), strictly negative when this inequality is reversed, and zero on its boundary. A zero class occurs **if and only if** \(n-1=s^2\) for an integer \(s\ge2\); in that case the only zeros are at \(k=(s^2-s)/2\) and \(k=(s^2+s)/2\). These phase boundaries are independent of the directed-cycle length \(r\).

There is a stronger exact linear-projection statement. Put \(T_n=C_{3,n}\) and \(a_{r,n}=(n-3)_{\underline{r-3}}/2^{r-3}\). Define
\[
R_{r,n}= C_{r,n}-\mathbb E C_{r,n}-a_{r,n}(T_n-\mathbb E T_n).
\]
Then \(\operatorname{Cov}(R_{r,n},N_{k,n})=0\) for **every** \(0\le k\le n-1\). Because \(T_n-\mathbb E T_n\) lies in the linear span of the centered score-class counts, the orthogonal \(L^2\) projection of \(C_{r,n}-\mathbb EC_{r,n}\) onto that entire span is exactly \(a_{r,n}(T_n-\mathbb ET_n)\).

## Assumptions and scope
Every edge of the complete labeled graph receives an independently fair orientation. The theorem covers all integers \(n\ge3\), \(3\le r\le n\), and \(0\le k\le n-1\), including extreme score classes and the length-\(n\) Hamiltonian-cycle count. A directed cycle is counted once modulo cyclic rotation, not by its starting vertex. No condition is placed on the realized score sequence.

The projection is onto the **linear** span of the score-class counts, not the space of all square-integrable functions of the score histogram. No conditional-mean identity or independence from the entire score histogram is claimed.

## Proof
First, by counting ordered distinct vertex lists modulo cyclic rotation and conditioning on their \(r\) prescribed arcs,
\[
\mathbb EC_{r,n}=\frac{(n)_{\underline r}}{r2^r}.
\]
Fix one potential directed \(r\)-cycle and condition on all its arcs occurring. For any vertex on that cycle, precisely one outgoing and one incoming incident edge are fixed. Its remaining \(n-3\) incident edges are independent fair orientations. Therefore its conditional score has law \(1+\operatorname{Bin}(n-3,1/2)\). A vertex outside the fixed cycle retains the unconditional score law \(\operatorname{Bin}(n-1,1/2)\), because the required arcs do not touch it.

Writing \(Q_{n,k}=2^{-(n-3)}\binom{n-3}{k-1}\), with out-of-range binomial coefficients equal to zero, linearity of expectation over potential cycles gives
\[
\operatorname{Cov}(C_{r,n},N_{k,n})
=r\mathbb EC_{r,n}(Q_{n,k}-B_{n,k}).
\]
For all \(0\le k\le n-1\), including the endpoints,
\[
Q_{n,k}=B_{n,k}\frac{4k(n-1-k)}{(n-1)(n-2)}.
\]
The elementary identity
\(4k(n-1-k)-(n-1)(n-2)=(n-1)-(2k-(n-1))^2\)
proves the covariance formula. Since \(B_{n,k}>0\), its sign is exactly the sign of that integer expression. Equality forces \((n-1)\) to be a square, and the two integer solutions follow by parity. Conversely, a square \(n-1=s^2\) has \(s\) and \(s^2\) of the same parity, so both stated scores are valid integers between zero and \(n-1\).

For the projection claim, the formula for any length divided by the formula for \(r=3\) gives
\[
\operatorname{Cov}(C_{r,n},N_{k,n})
=a_{r,n}\operatorname{Cov}(T_n,N_{k,n})
\quad\text{for every }k.
\]
In every tournament, a transitive triple has a unique vertex defeating its other two vertices, while a cyclic triple has none. Thus the **deterministic** identity
\[
T_n=\binom n3-\sum_{v=1}^n\binom{\operatorname{outdeg}(v)}2
=\binom n3-\sum_{k=0}^{n-1}\binom k2N_{k,n}
\]
holds. Therefore the centered variable \(T_n-\mathbb ET_n\) belongs to the score-class linear span. Subtracting its prescribed multiple from the centered cycle count yields a residual orthogonal to each generating score class, hence to their entire finite-dimensional span. The finite-dimensional orthogonal-projection characterization proves the assertion.

## Verification
A standalone Python 3 standard-library program, `verify.py`, independently enumerates every labeled tournament for \(3\le n\le6\) (including all \(2^{15}=32768\) six-vertex tournaments). It explicitly counts directed simple cycles and score classes, derives covariances using exact rational arithmetic, checks their equality with the formula, checks the projection covariance identities, and verifies the deterministic triangle/score identity for each enumerated tournament. It additionally checks the integer sign and perfect-square zero classification for \(3\le n\le120\). The executable completed 41,341 exact assertions. Run `python verify.py` from the directory containing these two files.

The enumeration and finite sign checks are corroboration, **not** the proof for arbitrary \(n\). The exact proof above establishes the infinite quantifiers.

## Relationship to prior work
The score sequence is a classical invariant of tournaments. Gao, McKay, and Wang studied asymptotic probabilities of prescribed digraphs in tournaments conditional on a given entire score sequence. Linial and Morgenstern studied deterministic extremal relations between cyclic triple and four-cycle densities. Kolesnik and Sanchez studied the geometry and realizability of score sequences, including random tournaments. Janson studied asymptotic normality of Hamilton-cycle counts in random tournaments. These furnish natural comparison points for the different, exact **unconditional mixed score-class covariance** here.

Earlier cycle/triangle fluctuation results give the scalar coefficient \(a_{r,n}\) and a Walsh decomposition. Combined with the observation that score-class Fourier coefficients live on stars whereas cycle Walsh coefficients use only subgraphs of cycle degree at most two, that decomposition can also yield the projection statement. The principal additional result here is the explicit score-class covariance, its complete square-root sign profile and its exact arithmetic zero classes, not a claim of priority for the Walsh projection method.

## Limitations
The theorem concerns fair, independent edge orientations. It does not assert the same formula in prescribed-score, correlated-edge, or biased-edge ensembles. Orthogonality is pairwise linear, not distributional independence. For example, for \(n=4\), a transitive score histogram has \(C_{4,4}=0\), whereas extrapolation of the linear projection expression for that same histogram would be \(-1/8\); the projection is **not** a conditional expectation given the full histogram.

Historical priority of an equivalent formulation remains subject to independent review, particularly for general tournament-subgraph projection methods and older conditional-score enumeration literature. No new limit law is claimed.

## References
1. Z. Gao, B. D. McKay, X. Wang, *Asymptotic enumeration of tournaments with a given score sequence containing a specified digraph*, Random Structures & Algorithms 16 (2000), 47–57, DOI: 10.1002/(SICI)1098-2418(200001)16:1<47::AID-RSA4>3.0.CO;2-L (publisher reports first publication 2000-01-03).
2. N. Linial and A. Morgenstern, *On the number of 4-cycles in a tournament*, arXiv:1405.1576 (first posted 2014-05-07).
3. B. Kolesnik and M. Sanchez, *The geometry of random tournaments*, arXiv:2009.09322 (first posted 2020-09-19).
4. S. Janson, *Hamilton cycles in a random tournament*, Random Structures & Algorithms 6 (1995), 213–220, DOI: 10.1002/rsa.3240060209.
