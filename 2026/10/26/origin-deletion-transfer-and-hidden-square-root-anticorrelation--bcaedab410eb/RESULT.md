# Origin-deletion transfer and hidden square-root anticorrelation in random mappings

## Finding
Consider a uniformly selected map \(f:[n]\to[n]\), with \(n\ge2\). Let \(K_n\) count vertices on directed cycles (loops count as cycles), and let \(Z_n=|[n]\setminus f([n])|\) count indegree-zero vertices.

For \(j=0,1,\ldots,n-1\), let \((a)_j=a(a-1)\cdots(a-j+1)\), with \((a)_0=1\). For every real or complex function \(h\) on positive integers,
\[
\mathbb E[(Z_n)_j h(K_n)]=(n)_j\left(1-\frac{j}{n}\right)^n\mathbb E h(K_{n-j}).

\]
The right-hand expectation uses an independent uniform mapping of \(n-j\) vertices; the identity is of laws, not of independent random variables within one graph. In particular the complete bivariate probability generating function is
\[
\mathbb E[s^{K_n}t^{Z_n}]=\sum_{j=0}^{n-1}\binom nj\left(1-\frac jn\right)^n(t-1)^j\mathbb E[s^{K_{n-j}}].

\]
For every strictly increasing \(h\),
\[
\operatorname{Cov}(h(K_n),Z_n)=n\left(1-\frac1n\right)^n\left(\mathbb E h(K_{n-1})-\mathbb E h(K_n)\right)<0.

\]
The ordinary covariance is asymptotic to a strictly negative constant times \(\sqrt n\):
\[
\lim_{n\to\infty}\frac{\operatorname{Cov}(K_n,Z_n)}{\sqrt n}=-\frac{\sqrt{\pi/2}}{2e}.

\]
Furthermore,
\[
\lim_{n\to\infty}\sqrt n\operatorname{Corr}(K_n,Z_n)=-\frac{\sqrt{\pi/2}}{2\sqrt{(2-\pi/2)(e-2)}}.

\]

## Assumptions and scope
All functions \(f:[n]\to[n]\) are equiprobable; their values at distinct arguments are independent and uniform on \([n]\). The graph has one outgoing arc per vertex. An origin is a vertex of *indegree zero*, not a directed root or a member of the cyclic core. For \(j=n\), the event that all \(n\) vertices are origins is impossible, and \(K_0\) is deliberately undefined; identity (1) is asserted only for \(0\le j\le n-1\). Strictness in (3) requires \(n\ge2\) and strictly increasing \(h\) on the positive integers; at \(n=1\) the covariance is zero. No assertion is made about likelihood-ratio ordering for \(Z_n\) conditioned on \(K_n\).

## Proof
**Deletion lemma.** Fix an ordered \(j\)-tuple \(J\) of distinct labels. The probability that no image of \(f\) lies in \(J\) equals \(((n-j)/n)^n\). Under this event, the restriction of \(f\) to the complement \(B=[n]\setminus J\) is exactly a uniform random map \(B\to B\). All vertices in \(J\) have indegree zero, so none can lie on a cycle; hence the cyclic-vertex count of \(f\) equals that of its restriction to \(B\). Expand \((Z_n)_j\) as the sum over the \((n)_j\) ordered \(j\)-tuples of the indicator that all are origins and take expectations. This proves (1). Expanding \(t^{Z_n}=(1+(t-1))^{Z_n}=\sum_j (Z_n)_j(t-1)^j/j!\) proves (2); the \(j=n\) term has expectation zero.

**Cyclic-core distribution and sign.** Rooted-forest enumeration for a fixed set of \(k\) cyclic labels gives \(k n^{n-k-1}\) directed forests oriented toward those roots. Choose those labels and a permutation of them. Consequently, for every \(1\le k\le n\),
\[
\Pr(K_n=k)=\frac{k(n)_k}{n^{k+1}},\qquad
\Pr(K_n\ge k)=\frac{(n)_k}{n^k},\qquad
\mathbb E K_n=\sum_{k=1}^n\frac{(n)_k}{n^k}.

\]
The second formula telescopes the first: writing \(a_n(k)=(n)_k/n^k\) and \(a_n(n+1)=0\), the mass equals \(a_n(k)-a_n(k+1)\). For every fixed \(k\ge2\), \(a_m(k)=\prod_{i=0}^{k-1}(1-i/m)\) is strictly increasing in integer \(m\ge k\). Therefore \(K_m\) increases strictly in first-order stochastic order as \(m\) grows. For any strictly increasing \(h\), its expectation strictly increases between \(m=n-1\) and \(m=n\), proving (3) from the \(j=1\) case of (1).

**Sharp asymptotic.** Let \(a_m(k)=(m)_k/m^k\) for \(k\le m\), zero otherwise, and write \(\Delta_n=\mathbb E K_n-\mathbb E K_{n-1}=\sum_{k\ge1}(a_n(k)-a_{n-1}(k))\). For \(k\le n-1\), direct cancellation gives
\[
1-\frac{a_{n-1}(k)}{a_n(k)}=1-\prod_{i=1}^{k-1}\left(1-\frac{i}{(n-1)(n-i)}\right).

\]
If \(k/\sqrt n\to x\ge0\), then \(a_n(k)\to\exp(-x^2/2)\) and the expression on the right of (7), multiplied by \(n\), tends to \(x^2/2\). For \(k\le n/2\), the product difference is at most \(Ck^2/n^2\), while \(a_n(k)\le\exp(-k(k-1)/(2n))\). The sum over \(k>n/2\) is exponentially negligible, including the \(k=n\) boundary term. Dominated Riemann summation therefore yields
\[
\sqrt n\,\Delta_n\longrightarrow\frac12\int_0^\infty x^2 e^{-x^2/2}\,dx=\frac12\sqrt{\frac\pi2}.

\]
Setting \(h(k)=k\) in (3), using \((1-1/n)^n\to e^{-1}\), and applying (8) proves (4).

Finally (6) and the same Gaussian tail bound give \(K_n/\sqrt n\) converging with its first two moments to a Rayleigh random variable of density \(xe^{-x^2/2}\), \(x>0\). Thus \(\operatorname{Var}(K_n)/n\to2-\pi/2\). Since \(Z_n\) is the number of empty boxes in \(n\) independent uniform allocations among \(n\) boxes, putting \(u_n=(1-1/n)^n\) and \(v_n=(1-2/n)^n\) gives
\[
\operatorname{Var}(Z_n)=nu_n(1-u_n)+n(n-1)(v_n-u_n^2),\quad
\operatorname{Var}(Z_n)/n\to e^{-1}-2e^{-2}.

\]
Divide (4) by the square root of the two variance asymptotics to obtain (5).

## Verification
Run `python verification.py` with the standard Python library. The script enumerates all \(50{,}068\) mappings over sizes \(2\) through \(6\), checks the exact mixed factorial-transfer identity against direct counts of cyclic points and origins, independently checks conditional occupancy moments by inclusion-exclusion, and evaluates the normalized covariance for several sizes up to \(10{,}000\). Its exact arithmetic gives \(6{,}653\) assertions across the finite cases. These computations check implementation and boundary handling, not the infinite theorem, for which the preceding proof is required.

## Relationship to prior work
Hansen and Jaworski [1] study random mappings with a fixed number of cyclic points and derive distributions of typical component sizes. Arney and Bender [2] analyze origins and cyclic points among broader random-mapping parameters, including separate marginal and degree-count results. Those inspected treatments do not exhibit the origin-deletion mixed-factorial transfer (1), the strict covariance class (3), or the \(\sqrt n\)-scaled constant (4). Flajolet and Odlyzko [3] analyze many random-mapping parameters by generating functions, but full text was not accessible for direct comparison; an equivalent earlier result there remains possible. Extended occupancy models [4] concern a related occupancy marginal, but do not by themselves supply the link to cyclic-point counts in (1).

## Limitations
The claims concern only uniform mappings with all self-maps equally likely; they do not extend automatically to mappings with prescribed indegrees, nonuniform target probabilities, or random functional graphs with forbidden loops. The scale \(\sqrt n\) is a covariance scale, not a claim of a nondegenerate normalized joint distribution. The novelty assessment is based on inspected material and may be changed by previously inaccessible or unindexed literature. This is a mathematical proof and a finite computational cross-check; independent audit has not been performed.

## References
[1] J. C. Hansen and J. Jaworski, *Random Mappings with a Given Number of Cyclical Points*, Ars Combinatoria 94 (2010), 341–359; public article record dated 2010-01-31. https://combinatorialpress.com/ars-articles/volume-094-ars-articles/random-mappings-with-a-given-number-of-cyclical-points/
[2] J. Arney and E. A. Bender, *Random Mappings with Constraints on Coalescence and Number of Origins*, Pacific Journal of Mathematics 103 (1982), 269–294. https://msp.org/pjm/1982/103-2/pjm-v103-n2-p03-s.pdf
[3] P. Flajolet and A. M. Odlyzko, *Random Mapping Statistics*, EUROCRYPT 1989, Lecture Notes in Computer Science 434 (1990), 329–354, DOI:10.1007/3-540-46885-4_34 (full text not inspected).
[4] B. O’Neill, *Three Distributions in the Extended Occupancy Problem*, public preprint, https://arxiv.org/abs/2209.02220 (used only for comparison of occupancy models).
