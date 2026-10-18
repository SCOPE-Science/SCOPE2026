# Exact cycle–indegree covariance phases in uniform random mappings

## Finding

**Theorem.** Let \(n\ge2\) and \(f:[n]\to[n]\) be uniformly random among the \(n^n\) functions. Write \(C_{n,k}\) for its number of directed cycles of exact length \(k\), including fixed points as cycles of length one, and \(H_{n,r}\) for the number of vertices with indegree exactly \(r\). Then the entire mixed covariance array is explicit. For \(p=1/n\), \(q=1-p\) and
\[
b_m(r)=\begin{cases}\binom{m}{r}p^r q^{m-r},&0\le r\le m,\\0,&\text{otherwise},\end{cases}
\qquad e_{n,k}=\frac{(n)_{\underline{k}}}{k n^k},
\]
we have
\[
\boxed{\operatorname{Cov}(C_{n,k},H_{n,r})=
 e_{n,k}\bigl[kb_{n-k}(r-1)+(n-k)b_{n-k}(r)-nb_n(r)\bigr].}
\tag{1}
\]
Here \(1\le k\le n\), \(0\le r\le n\), and \(e_{n,k}=\mathbb E C_{n,k}\).

Every degree class is uncorrelated with the fixed-point count: the right side of (1) vanishes for \(k=1\). For all \(2\le k\le n\), its sign is strictly **negative** for \(r=0\) and \(3\le r\le n\), strictly **positive** for \(r=1\), and follows the complete single-switch rule below for \(r=2\).

Define the exact scalar
\[
S_{n,k}=(n-k)\bigl[(n-k)(n-k-1)+2k(n-1)\bigr]
             -n^2(n-1)\left(1-\frac1n\right)^k.
\tag{2}
\]
The sign for \(r=2\) is exactly the sign of \(S_{n,k}\). When \(n\ge4\), let
\[
\kappa_n=\min\{k\in\{2,\ldots,n\}:S_{n,k}\le0\}.
\]
Then \(S_{n,k}>0\) for \(2\le k<\kappa_n\); at \(k=\kappa_n\) its sign is zero or negative; and \(S_{n,k}<0\) for \(k>\kappa_n\). There is at most one value of \(k\) at which \(S_{n,k}=0\). For \(n=2\), the \(r=2,k=2\) covariance is negative. For \(n=3\), its signs at \(k=2,3\) are zero and negative, respectively. The transition occurs on a linear length scale:
\[
\boxed{\frac{\kappa_n}{n}\longrightarrow\tau=0.58472438648\ldots,\qquad
 e^\tau(1-\tau)(1+\tau^2)=1,\quad0<\tau<1.}
\tag{3}
\]

There is a more general structural result. For any \(\phi:\{0,\ldots,n\}\to\mathbb R\), let
\(W_\phi=\sum_{v=1}^n\phi(\deg^-(v))\), and set
\(\Delta^2\phi(d)=\phi(d+2)-2\phi(d+1)+\phi(d)\). Then
\[
\boxed{\operatorname{Cov}(C_{n,k},W_\phi)
=-\frac{e_{n,k}}{n}\sum_{j=1}^{k-1}j\,
 \mathbb E\bigl[\Delta^2\phi(B_{n-j-1})\bigr],\quad
 B_m\sim\operatorname{Bin}(m,1/n).}
\tag{4}
\]
Thus every discretely convex score \(\phi\) has nonpositive covariance with the cycle count. In particular,
\[
\operatorname{Cov}\left(C_{n,k},\sum_v\binom{\deg^-(v)}2\right)
=-\frac{k(k-1)}{2n}\,e_{n,k}.
\tag{5}
\]

## Assumptions and scope

The map images \(f(1),\ldots,f(n)\) are mutually independent, each uniform on \([n]\). All cycles are simple directed cycles in the functional graph, including loops; a vertex has exactly one outgoing edge, and its indegree includes loops. Formulae (1)–(5) are finite-sample, exact identities for every allowed integer \(n,k,r\). The score \(\phi\) in (4) is arbitrary and needs no monotonicity; discrete convexity means \(\Delta^2\phi(d)\ge0\) for all \(0\le d\le n-2\). Empty sums equal zero. Formula (3) concerns \(n\to\infty\) with the crossover length \(\kappa_n\); it is not a claim of ordinary asymptotic correlation for an event with a long cycle.

## Proof

**1. Cycle-Palm law.** A prescribed ordered \(k\)-cycle on a set of \(k\) distinct vertices fixes exactly \(k\) mapping images, so its probability is \(n^{-k}\). There are \((n)_{\underline{k}}/k\) such directed cycles; hence \(\mathbb EC_{n,k}=e_{n,k}\). Conditioning on one specified cycle leaves exactly \(n-k\) independent uniform images. A vertex on that cycle receives exactly one forced incoming edge and a \(\operatorname{Bin}(n-k,p)\) number of other incoming edges; a vertex off the cycle receives only \(\operatorname{Bin}(n-k,p)\) incoming edges. Averaging over the \(k\) on-cycle and \(n-k\) off-cycle vertices, then summing over prescribed cycles, gives
\[
\mathbb E[C_{n,k}H_{n,r}]
=e_{n,k}\,[k b_{n-k}(r-1)+(n-k)b_{n-k}(r)].
\]
Since \(\mathbb EH_{n,r}=n b_n(r)\), (1) follows. More generally the cycle-weighted indegree of a uniformly marked vertex has the distribution
\[
T_{n,k}\stackrel d=\operatorname{Bin}(n-k,p)+\operatorname{Bern}(kp),
\tag{6}
\]
with independent summands. This is an expectation weighted by \(C_{n,k}\), **not** conditioning on the event that any \(k\)-cycle exists.

**2. Discrete-curvature identity.** Define \(T_{n,j}\) by (6) for \(1\le j\le k\). At \(j=1\), \(T_{n,1}\sim\operatorname{Bin}(n,p)\). To pass from \(j\) to \(j+1\), write the common part as \(B_{n-j-1}\); the two residual Bernoulli probability-generating functions differ by
\[
[1+(j+1)p(z-1)]-[1+p(z-1)][1+jp(z-1)]
=-jp^2(z-1)^2.
\]
Coefficient extraction against an arbitrary score \(\phi\) yields
\[
\mathbb E\phi(T_{n,j+1})-\mathbb E\phi(T_{n,j})
=-jp^2\mathbb E\Delta^2\phi(B_{n-j-1}).
\]
By the cycle-Palm law,
\(\operatorname{Cov}(C_{n,k},W_\phi)
=ne_{n,k}(\mathbb E\phi(T_{n,k})-\mathbb E\phi(T_{n,1}))\).
Summing and using \(np^2=1/n\) proves (4) and the convex-score claim. For \(\phi(d)=\binom d2\), its second difference is identically one, so (5) follows. Formula (4) also proves every \(k=1\) covariance is zero without implying independence.

**3. Signs away from indegree two.** Take \(\phi(d)=\mathbf 1\{d=r\}\) in (4). Its expected second difference is
\(A_m(r)=b_m(r)-2b_m(r-1)+b_m(r-2)\), with \(m=n-j-1\). For \(r=0\) this is \(b_m(0)>0\), yielding strict negativity for \(k\ge2\). For \(r=1\) it is \(b_m(1)-2b_m(0)<0\), because \(b_m(1)/b_m(0)=m/(n-1)\le(n-2)/(n-1)<2\). Thus its covariance is strictly positive. For \(r\ge3\), \(A_m(r)\ge0\): if \(m\ge r-2\), then
\[
\frac{b_m(r-1)}{b_m(r-2)}
=\frac{m-r+2}{(r-1)(n-1)}<\frac12,
\]
and consequently \(A_m(r)>0\); if \(m<r-2\), all three terms vanish. Since the first summand in (4) has \(m=n-2\ge r-2\), the covariance is strictly negative for all \(3\le r\le n\), \(k\ge2\).

**4. One-switch rule at indegree two.** Equation (1) with \(r=2\) gives, for all \(2\le k\le n\),
\[
\operatorname{Cov}(C_{n,k},H_{n,2})
=\frac{e_{n,k}q^{n-k-2}}{2n^2}\,S_{n,k},
\tag{7}
\]
where the prefactor is strictly positive (the power may be negative, but \(q>0\)). For \(r=2\), the curvature in step 3 equals
\[
A_m(2)=q^{m-2}P_m,\qquad
P_m=q^2-2mpq+\frac{m(m-1)}2p^2.
\]
The polynomial \(P_m\) is strictly decreasing in \(m\in\{0,\ldots,n-2\}\), since
\(P_{m+1}-P_m=mp^2-2pq<0\) throughout the relevant range. In the sum (4), as \(j\) increases, \(m=n-j-1\) decreases, so the successive values of \(A_m(2)\) can change sign only from negative to positive, at most once. Hence the covariance bracket as a function of \(k\), starting at zero for \(k=1\), first increases (while \(A_m(2)<0\)) and then decreases (while \(A_m(2)>0\)); its successive differences have at most one sign change. At \(n\ge4\),
\(A_{n-2}(2)=-q^{n-4}(n-3)/(2n)<0\), so the bracket is positive at \(k=2\); at \(k=n\) the cycle-Palm indegree is deterministically one, so the bracket for \(r=2\) equals \(-b_n(2)<0\). This gives exactly one positive-to-negative transition, with at most one zero; (7) converts it to the stated signs of \(S_{n,k}\). The \(n=2,3\) cases follow directly from (1).

**5. The asymptotic crossover.** Let \(k/n\to t\in(0,1]\). Dividing (2) by \(n^3\) gives the uniform-on-compact limit
\[
\frac{S_{n,k}}{n^3}\longrightarrow
F(t)=(1-t)(1+t^2)-e^{-t}.
\]
The sign of \(F(t)\) is that of \(h(t)-1\), where \(h(t)=e^t(1-t)(1+t^2)\). A derivative calculation gives
\(h'(t)=e^t t(1-2t-t^2)\); thus \(h\) rises above one on \((0,\sqrt2-1]\) and decreases strictly thereafter to zero at \(t=1\), crossing one exactly once at \(\tau\in(\sqrt2-1,1)\). Sign convergence at fixed \(t\) on either side of \(\tau\), together with the finite one-switch rule, traps \(\kappa_n/n\) between any two fixed numbers bounding \(\tau\). This proves (3). A numerical root computation gives the quoted decimal; it is not used as the proof.

## Verification

The accompanying standalone file `verify.py` uses only the Python standard library. It independently enumerates all \(n^n\) maps for \(2\le n\le6\) and computes the complete cycle–indegree covariance array and degree-pair collision covariance exactly with rational numbers. It then checks the binomial–Bernoulli identity, curvature telescoping, sign classes and equality cases for additional finite sizes, verifies the complete one-switch property through \(n=99\), and compares the asymptotic root with numerical transition indices. The executed checker reported 94,602 passing assertions. These finite checks corroborate the proofs; they do not constitute exhaustive verification for unbounded \(n\).

To reproduce: `python3 verify.py`. No network, external data or packages are needed.

## Relationship to prior work

The broad study of uniform random functional digraphs, marginal cycle-length counts and marginal indegree (\(r\)-node) counts is classical; Flajolet and Odlyzko [1, especially Theorem 4] give separate marginal asymptotics. Hansen and Jaworski [2, 3] introduce and analyze exchangeable-indegree mapping models and their cyclic vertices, component counts and local predecessor/successor statistics. Leckey and Wormald [4] study six-length and tail-length asymptotics conditional on the indegree sequence. These works supply models and methods, not an explicit complete all-length, all-indegree finite covariance-sign classification or the universal discrete-convex score relation (4) as identified in the inspected sections. In particular, the known negative covariance between indegree-zero counts and nontrivial cycle counts is not claimed as new; the new focus is the full indegree spectrum and degree-two phase transition.

## Limitations

This theorem concerns independent uniform images, not arbitrary mappings with fixed indegree sequences or nonuniform image laws. The nonzero crossover \(\tau\) describes covariance **signs**, not a law of large numbers for the number of cycles of macroscopic length: such cycles are rare. Covariance zero for fixed points does not imply independence of the full statistics. Equations (1) and (4) admit elementary derivations from cycle conditioning, so a previously published more general mixed generating-function statement could subsume them. No claim of an independent audit or exhaustive historical-priority determination is made. An early paper [2] and marginal generating-function methods [1] are plausible sources of unrecorded implicit formulae; the nontrivial one-switch classification requires the additional sign argument above.

## References

[1] P. Flajolet and A. Odlyzko, *Random Mapping Statistics*, in EUROCRYPT 1989, Lecture Notes in Computer Science 434 (1990), pp. 329–354. Available full text: https://scispace.com/pdf/random-mapping-statistics-yjuqfvoh87.pdf .

[2] J. C. Hansen and J. Jaworski, *A new random mapping model* (arXiv:math/0603529, originally posted March 22, 2006); later published as *Random Mappings with Exchangeable In-degrees*, Random Structures & Algorithms 33 (2008), 105–126, doi:10.1002/rsa.20187. Original preprint: https://arxiv.org/pdf/math/0603529 .

[3] J. C. Hansen and J. Jaworski, *Local properties of random mappings with exchangeable in-degrees*, Advances in Applied Probability 40 (2008), 183–205, doi:10.1239/aap/1208358892. Full text: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/6993B104668C73703B9E57AF3DCC643E/S0001867800002433a.pdf/local-properties-of-random-mappings-with-exchangeable-in-degrees.pdf .

[4] K. Leckey and N. Wormald, *A limit theorem for the six-length of random functional graphs with a fixed degree sequence*, first public arXiv version March 7, 2018, arXiv:1803.02667, https://arxiv.org/abs/1803.02667 .
