# A sharp fixed-edge anticorrelation law for isolated and degree-one vertices

## Finding

**Theorem.** Let \(n\ge4\) and \(0\le m\le N=\binom n2\) be integers. Choose a labeled simple graph uniformly from the \(\binom Nm\) graphs with exactly \(m\) edges. Let \(X_0\) count degree-zero vertices and \(X_1\) count degree-one vertices. Then

\[
\operatorname{Cov}_{G(n,m)}(X_0,X_1)
\begin{cases}<0,&2\le m\le\binom{n-1}2,\\=0,&m=0,1\text{ or }\binom{n-1}2<m\le\binom n2.
\end{cases}
\]

Writing \(A=\binom{n-1}2\), \(B=\binom{n-2}2\), the exact joint-moment identity valid at every edge count is

\[
\operatorname{Cov}(X_0,X_1)=\frac{n(n-1)(n-2)\binom B{m-1}}{\binom Nm}
-\frac{n^2(n-1)\binom A m\binom A{m-1}}{\binom Nm^2}.
\]

With the convention \(\binom ab=0\) for integers \(b<0\) or \(b>a\), this formula includes both degenerate boundaries. For every sequence of edge counts satisfying \(2m/n\to c\in(0,\infty)\),

\[
\lim_{n\to\infty}\frac1n\operatorname{Cov}_{G(n,m)}(X_0,X_1)=-c^2e^{-2c}.
\]

In contrast, in the *independent-edge* model \(G(n,p)\), the already-known covariance is

\[
\operatorname{Cov}_{G(n,p)}(X_0,X_1)
=n(n-1)p(1-p)^{2n-4}(np-2).
\]

Consequently, for every \(n\ge5\), taking \(m=n\) and \(p=m/\binom n2=2/(n-1)\) gives **negative** covariance under the fixed-edge model and **positive** covariance under the independent-edge model at the same expected edge count. In the sparse limit \(p\sim c/n\), the independent-edge normalized covariance tends to \(c(c-2)e^{-2c}\), which has the opposite sign to the fixed-edge limit whenever \(c>2\). The independent-edge identity and its direct consequence are comparisons to existing work, not claimed as novel.

## Assumptions and scope

The graph is undirected, simple, labeled, and sampled uniformly among all \(m\)-edge graphs. Every edge count from empty to complete is included. An isolated vertex has degree zero; a leaf has degree one, even if it forms one endpoint of an isolated edge. The strict sign classification is asserted for \(n\ge4\). For \(n=3\), the same elementary formulas give covariance zero at all edge counts.

## Proof

Set \(N=\binom n2\), \(A=\binom{n-1}2\), and \(B=\binom{n-2}2\). For a specified vertex to be isolated, the \(m\) edges must be chosen among its \(A\) possible nonincident edges. For a specified vertex to have degree one, its unique neighbor can be chosen in \(n-1\) ways, followed by \(m-1\) edges among \(A\) nonincident edges. If a specified vertex \(u\) is isolated and another specified vertex \(v\ne u\) has degree one, the neighbor of \(v\) is chosen from the remaining \(n-2\) vertices, and the other \(m-1\) edges are selected among the \(B\) pairs avoiding \(u,v\). Summing these indicator probabilities gives

\[
\begin{aligned}
\mathbb EX_0 &=n\binom A m/\binom Nm,\\
\mathbb EX_1 &=n(n-1)\binom A{m-1}/\binom Nm,\\
\mathbb E(X_0X_1)&=n(n-1)(n-2)\binom B{m-1}/\binom Nm.
\end{aligned}
\]

This proves the displayed covariance formula, including zero conventions.

Let \(f_n(m)=\mathbb E_{G(n,m)}X_1\). For \(m\le A\), conditioning on one specified vertex being isolated leaves the uniform law \(G(n-1,m)\), and the number of degree-one vertices in the full graph equals that of the remaining graph. Since there are \(n\) symmetric choices of isolated vertex,

\[
\operatorname{Cov}_{G(n,m)}(X_0,X_1)
=\mathbb EX_0\,[f_{n-1}(m)-f_n(m)].
\]

For \(1\le m\le B+1\), all displayed expectations used in the ratio below are positive, and direct cancellation yields

\[
R_n(m):=\frac{f_{n-1}(m)}{f_n(m)}
=\frac{n-2}{n}\frac{\binom B{m-1}\binom Nm}{\binom A m\binom A{m-1}}.
\]

Now \(R_n(1)=1\); for every \(1\le m\le B\),

\[
\frac{R_n(m+1)}{R_n(m)}
=\frac{(B-m+1)(N-m)}{(A-m)(A-m+1)}<1.
\]

Indeed, the positive-denominator difference is exactly

\[
(A-m)(A-m+1)-(B-m+1)(N-m)
=(n-3)(n-1)-(A-m)
\ge\frac{(n-1)(n-4)}2+1>0.
\]

Thus \(f_{n-1}(m)<f_n(m)\) for \(2\le m\le B+1\). For \(B+2\le m\le A\), the smaller graph has too many edges to contain a degree-one vertex, so \(f_{n-1}(m)=0<f_n(m)\). Also \(\mathbb EX_0>0\) whenever \(m\le A\). At \(m=0,1\), the number of degree-one vertices is deterministic; for \(m>A\), the number of isolated vertices is zero deterministically. This proves every sign and boundary case.

For the sparse asymptotic, suppose \(m/n\to c/2\in(0,\infty)\). Standard finite-product estimates applied to the first displayed formulas give \(\mathbb EX_0/n\to e^{-c}\) and \(f_n(m)/n\to ce^{-c}\). More precisely, for \(1\le j\le m=O(n)\), the exact consecutive-ratio expression above is

\[
\frac{R_n(j+1)}{R_n(j)}=1-\frac2{n^2}+O_c(n^{-3}),
\]

uniformly for large \(n\). Multiplication over \(j=1,\ldots,m-1\), with \(R_n(1)=1\), gives

\[
R_n(m)=1-\frac{2m}{n^2}+O_c(n^{-2})=1-\frac cn+o(n^{-1}).
\]

Using the conditioning covariance identity, divide by \(n\) and take the limit: \(\operatorname{Cov}(X_0,X_1)/n=(\mathbb EX_0/n)f_n(m)(R_n(m)-1)\to-c^2e^{-2c}\). Finally, the independent-edge covariance follows by considering ordered distinct vertices, counting the configurations in which one is isolated and the other has degree one; it also follows from the degree-count covariance formula of Goldstein and Rinott [1, Eq. (25)]. When \(m=n\), \(n\ge5\) implies \(2\le m\le A\), and \(np=2n/(n-1)>2\), proving the stated opposite signs.

## Verification

The standalone standard-library Python program `artifacts/verify.py` can be run as `python3 artifacts/verify.py` from the unpacked package root. It independently enumerates all labeled graphs through six vertices and checks the three joint moments and strict boundary signs for every edge count; it also checks the independent-edge covariance under direct exhaustive averaging at three rational edge probabilities. Separately, it checks the finite formulas, signs, exact ratio factorization, and independent-edge identity for all \(4\le n\le84\) and admissible \(m\). Successful execution prints `CHECKS_OK` and reports 283216 assertion units. These finite checks are supporting evidence; the unrestricted signs and asymptotics follow from the preceding proof.

## Relationship to prior work

Goldstein and Rinott [1, §4.2, Theorem 4.2 and Eq. (25)] already gave the exact cross-covariances of degree-class counts in independent-edge random graphs, and normal approximations. Goldstein [2, §§1–2] develops univariate degree-count normal approximation, again for independent Bernoulli edges. Neither cited discussion supplies this all-parameter fixed-edge sign theorem or the particular isolate-conditioning ratio argument. The moment formulas are direct finite hypergeometric counting; no novelty is claimed for such elementary ingredients or for the independent-edge covariance. The proposed new contribution is the sharp all-edge-count sign classification, its conditional-monotonicity proof, and the resulting explicit ensemble reversal and sparse fixed-edge limit.

## Limitations

The sign theorem concerns only the cross-covariance of degree-zero and degree-one counts; it does not establish negative association of the entire graph degree profile or of the individual vertex-degree events. Finite checking does not certify the infinite claim. An older fixed-edge joint degree-count result or a general negative-dependence theorem may subsume this result, and historical novelty has not been independently certified. No independent scientific audit has been performed.

## References

[1] L. Goldstein and Y. Rinott, *Multivariate normal approximations by Stein's method and size bias couplings*, Journal of Applied Probability 33 (1996), 1–17; arXiv:math/0510586, first submitted 2005-10-27, https://arxiv.org/html/math/0510586v1 (especially §4.2, Eq. (25)).

[2] L. Goldstein, *A Berry–Esseen bound with applications to vertex degree counts in the Erdős–Rényi random graph*, Annals of Applied Probability 23 (2013), 617–636; arXiv:1005.4390, first submitted 2010-05-24, https://arxiv.org/html/1005.4390v4 (especially §§1–2).

[3] B. Bollobás, *Degree sequences of random graphs*, Discrete Mathematics 33 (1981). Available publisher abstract consulted; full text not reviewed and historical coverage cannot be ruled out.
