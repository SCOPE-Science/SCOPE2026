# A sharp edge-conditioning reversal of leaf–triangle covariance

## Finding

Let \(n\ge4\) be an integer, \(M=\binom n2\), and let \(G(n,m)\) be uniform among simple labeled graphs on \(n\) vertices having exactly \(m\in\{0,\ldots,M\}\) edges. Write \(L\) for the number of vertices of degree exactly one and \(T\) for the number of (not necessarily induced) triangles. Define the falling factorial \((a)_{\underline{k}}=\prod_{j=0}^{k-1}(a-j)\), with \((a)_{\underline0}=1\).

Set
\[
E_T=\binom n3\frac{(m)_{\underline3}}{(M)_{\underline3}},\qquad
E_L=n(n-1)\frac{m(M-m)_{\underline{n-2}}}{(M)_{\underline{n-1}}}.
\]
Here \(E_T=0\) for \(m<3\), and \(E_L=0\) for \(m=0\) or \(m>M-n+2\). Then, for \(3\le m\le M-n+2\),
\[
\boxed{\operatorname{Cov}_{G(n,m)}(L,T)
=E_LE_T\left[\frac{n+1}{n}\frac{n^2-n-4}{n^2-3n-2}\frac{m-3}{m}-1\right].}
\]
The covariance is zero outside this range. Its sign is completely classified:

* For every \(n\ge5\), it is strictly negative when \(3\le m\le n\), strictly positive when \(n+1\le m\le M-n+2\), and zero at all other edge counts.
* For \(n=4\), it is negative at \(m=3\), positive at \(m=4\), and zero otherwise.
* For \(n\le3\), covariance is zero for all allowable \(m\).

In contrast, for independent-edge \(G(n,p)\) with \(n\ge3\) and \(0<p<1\),
\[
\boxed{\operatorname{Cov}_{G(n,p)}(L,T)
=-\frac3n\,\mathbb E_{G(n,p)}L\,\mathbb E_{G(n,p)}T<0,}
\]
where \(\mathbb EL=n(n-1)p(1-p)^{n-2}\) and \(\mathbb ET=\binom n3p^3\). Thus fixing the edge count reverses the dependence sign for the entire nondegenerate positive regime, whose first edge count is exactly \(m=n+1\) for \(n\ge5\).

Moreover, whenever \(m=m(n)\) and \(m/n\to c\in(0,\infty)\),
\[
\boxed{\operatorname{Cov}_{G(n,m)}(L,T)\longrightarrow 8c^3(c-1)e^{-2c}.}
\]

## Assumptions and scope

All graphs are finite, undirected, labeled, loopless, and without multiple edges. A leaf means a vertex of degree exactly one, including each endpoint of an isolated-edge component; a triangle is any three vertices with all three connecting edges present. The covariance statements concern counts of these objects, not connectivity-conditioned random graphs or uniform graphs with prescribed degrees. For \(n\le3\), the fixed-edge covariance vanishes for elementary support reasons; the displayed rational factor applies only for \(n\ge4\).

## Proof

Fix a vertex \(v\) and a three-vertex set \(\tau\). Write \(d=n-1\). In \(G(n,m)\), uniform sampling without replacement gives
\[
\Pr(\deg(v)=1)=d\frac{\binom{M-d}{m-1}}{\binom Mm}
=d\frac{m(M-m)_{\underline{d-1}}}{(M)_{\underline d}},
\qquad
\Pr(\tau\text{ is a triangle})=\frac{(m)_{\underline3}}{(M)_{\underline3}}.
\]
These identities give the expressions for \(E_L\) and \(E_T\). If \(v\in\tau\), the triangle event makes \(\deg(v)\ge2\), so the joint leaf-and-triangle probability is zero. If \(v\notin\tau\), all \(d\) star edges at \(v\) are disjoint from the three edges of \(\tau\). Conditional on the triangle event, the other \(m-3\) selected edges are uniform among the other \(M-3\) possibilities. Therefore
\[
\Pr(\deg(v)=1\mid\tau\text{ triangle})
=d\frac{(m-3)(M-m)_{\underline{d-1}}}{(M-3)_{\underline d}}.
\]
This is interpreted as zero when \(m=3\). There are \(n-3\) vertices outside \(\tau\). By symmetry and linearity,
\[
\frac{\mathbb E(L\mid\tau\text{ triangle})}{\mathbb EL}
=\frac{n-3}{n}\frac{m-3}{m}\frac{(M)_{\underline d}}{(M-3)_{\underline d}}
=\frac{m-3}{m}\,Q_n,
\]
where cancellation of three falling-factorial terms yields
\[
Q_n=\frac{(n+1)(n^2-n-4)}{n(n^2-3n-2)},\qquad
Q_n-1=\frac{3n^2-3n-4}{n(n^2-3n-2)}>0
\quad(n\ge4).
\]
Summing \(\operatorname{Cov}(L,\mathbf1_{\tau\text{ triangle}})\) over the \(\binom n3\) possible triangles proves the displayed exact covariance formula when both means are nonzero. When \(m<3\), triangles are impossible; when \(m>M-n+2\), no vertex can have degree one, because the complement would need at least \(n-2\) incident missing edges. Hence the covariance is zero at the excluded edge counts.

For nonzero means, the sign is that of \(Q_n(m-3)/m-1\), and this strictly increases with \(m>0\). Its zero as a real number is
\[
m_*(n)=\frac{3Q_n}{Q_n-1}
=\frac{3(n+1)(n^2-n-4)}{3n^2-3n-4}.
\]
For \(n\ge5\),
\[
m_*(n)-n=\frac{3n^2-11n-12}{3n^2-3n-4}>0,
\qquad
n+1-m_*(n)=\frac{8(n+1)}{3n^2-3n-4}>0.
\]
The first numerator is positive at \(n=5\) and strictly increasing for larger integers. This proves the sharp integer sign transition. For \(n=4\), the real zero is \(15/4\); direct substitution gives the stated exceptional classification. For \(n\le3\), the triangle count is either zero or deterministic at every fixed \(m\).

For \(G(n,p)\), let \(A_\tau\) be the event that a specified triangle is present. Its three vertices cannot be leaves conditional on \(A_\tau\), whereas the degree distribution of each vertex outside the triangle is unaffected by \(A_\tau\), by independence of edge indicators. Thus \(\mathbb E(L\mid A_\tau)=(n-3)\mathbb EL/n\). Summing over \(\tau\) proves the independent-edge identity.

Finally, suppose \(m/n\to c>0\). Elementary falling-factorial estimates give
\[
E_T\to \frac43c^3,\qquad E_L\sim2cne^{-2c},\qquad
Q_n\frac{m-3}{m}-1=\frac{3(c-1)}{cn}+o(n^{-1}).
\]
Multiplying proves the sparse-limit expression, including \(c=1\), where the limiting covariance is zero.

## Verification

The standalone `verify.py` independently enumerates every labeled graph for \(n\in\{4,5,6\}\) and checks every fixed-edge stratum against exact rational expressions for \(\mathbb EL\), \(\mathbb ET\), and \(\operatorname{Cov}(L,T)\). The exhaustive stratum counts are respectively \(7\), \(11\), and \(16\), drawn from \(64\), \(1024\), and \(32768\) labeled graphs. The same enumeration checks the independent-edge formula exactly at \(p=1/2\). The checker also tests \(6948\) exact-arithmetic sign cases covering selected critical and boundary edge counts for \(4\le n\le500\), and numerical convergence at four positive sparse densities. All tests passed. Finite checks corroborate the identities; the preceding proof establishes them for all stated parameters.

Reproduce with `python3 verify.py` using the Python standard library. The captured result is in `verification_output.txt`.

## Relationship to prior work

Janson's paper on conditioning and vertex-degree statistics in random graphs (arXiv:math/0605642, first public version 24 May 2006) gives asymptotic degree-count results for \(G(n,m)\), not a finite joint covariance with triangle counts or its integer sign boundary. Goldstein (arXiv:1005.4390) gives degree-count normal approximations in the independent-edge model, not this two-count dependence. Janson's 1990 functional theorem treats fixed-subgraph count asymptotics; a degree-one vertex is not a fixed finite subgraph occurrence, because it specifies absence of all other incident edges. Its full text could not be examined, and its possible broader methodological overlap remains a priority limitation. Related fixed-edge work on isolated-edge component counts differs: degree-one vertices also occur as pendant vertices in larger components, and its corresponding sign boundary does not determine the one here.

## Limitations

The result concerns covariance rather than stochastic association, higher mixed moments, joint limit laws, or conditional distributions of the entire pair. Strict signs require both observables to be nondegenerate, as spelled out above. The sparse-limit formula is a covariance limit, not a convergence-in-distribution theorem. Historical novelty cannot be independently certified from the inspected literature, especially given limited access to some older general results.

## References

1. S. Janson, *Monotonicity, asymptotic normality and vertex degrees in random graphs*, arXiv:math/0605642 (first public 24 May 2006); *Bernoulli* 13 (2007), 952–965. https://arxiv.org/abs/math/0605642
2. L. Goldstein, *A Berry–Esseen bound with applications to vertex degree counts in the Erdős–Rényi random graph*, arXiv:1005.4390 (first public 24 May 2010); *Annals of Applied Probability* 23 (2013), 617–636. https://arxiv.org/abs/1005.4390
3. S. Janson, *A functional limit theorem for random graphs with applications to subgraph count statistics*, *Random Structures & Algorithms* 1 (1990), 15–37. https://doi.org/10.1002/rsa.3240010103
4. J. H. Kim and V. H. Vu, *Divide and conquer martingales and the number of triangles in a random graph*, *Random Structures & Algorithms* 24 (2004), 166–174. https://doi.org/10.1002/rsa.10113
