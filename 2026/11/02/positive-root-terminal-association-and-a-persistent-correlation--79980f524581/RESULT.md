# Positive root–terminal association and a persistent correlation in the Moran forest

## Finding
Let \(n\ge3\), and sample the stationary Moran rooted forest on \(n\) vertices. Let \(C_n\) be its number of rooted components and \(T_n\) its number of **terminal vertices**, defined as vertices with zero children (zero outgoing degree in the orientation away from roots; an isolated root is terminal). Then, for every pair of nondecreasing real functions \(f,g\),
\[
\operatorname{Cov}\bigl(f(C_n),g(T_n)\bigr)\ge0.
\tag{1}
\]
The inequality is strict if both functions are strictly increasing. Put \(q=(n-2)/(n-1)\). The exact covariance is
\[
\operatorname{Cov}(C_n,T_n)
=(n-2)-\frac{5n-8}{2}q^{n-1}>0.
\tag{2}
\]
Despite fluctuations of both counts having order \(\sqrt n\), their correlation has a nonzero limit:
\[
\lim_{n\to\infty}\operatorname{Corr}(C_n,T_n)
=\left(e-\frac52\right)\sqrt{\frac6{e-2}}
=0.6308785600\ldots.
\tag{3}
\]
A more local statement holds in the uniform-attachment representation described below. Writing \(A_j\) for the indicator that vertex \(j\) starts a component and \(B_i\) for the indicator that vertex \(i\) is terminal, the entire cross-covariance kernel is
\[
\operatorname{Cov}(A_j,B_i)=
\begin{cases}
\dfrac{n-j}{(n-1)^2}q^{n-i-1},&1\le i<j\le n,\\[5pt]
0,&1\le j\le i\le n.
\end{cases}
\tag{4}
\]
Here \(A_1=1\) and \(A_n=0\). The positive lower-triangular kernel is a quantitative version of the association (1).

## Assumptions and scope
The stationary Moran forest is obtained from the finite directed-graph Markov chain which chooses an ordered pair of distinct vertices uniformly, deletes all edges incident to the second vertex, then inserts the edge directed from the first vertex to the second. Its unique stationary law is supported on nonempty rooted forests; the uniform-attachment representation used here is Proposition 2.1 of Bienvenu, Duchamps and Foutel-Rodier [1]. No large-sample or independence assumption on the counts is made in (1), (2), or (4). Terminal means *zero children*, not graph-theoretic degree one: an isolated vertex is included, and a nonroot with one parent and no children is included.

For computations, before the final uniform relabeling, take mutually independent \(U_j\), each uniform on \(\{1,\ldots,n\}\setminus\{j\}\). Insert an oriented edge \(U_j\to j\) exactly when \(U_j<j\). The relabeling preserves \(C_n,T_n\); all indexed indicators in (4) refer to this pre-relabeling representation. Then
\[
A_j=\mathbf1\{U_j>j\},\qquad
B_i=\prod_{j=i+1}^{n}\mathbf1\{U_j\ne i\},
\quad C_n=\sum_{j=1}^n A_j,\quad T_n=\sum_{i=1}^n B_i.
\tag{5}
\]

## Proof
**1. Local identities.** Set \(q=(n-2)/(n-1)\). Independence across the attachment variables gives
\[
\mathbb P(B_i=1)=q^{n-i},\qquad
\mathbb P(A_j=1)=\frac{n-j}{n-1},\quad (1\le j\le n).
\tag{6}
\]
For \(j\le i\), the variables \(A_j,B_i\) use disjoint attachment choices and are independent. For \(i<j\), the event \(A_j=1\) forces \(U_j>j>i\), so it automatically excludes an attachment to \(i\), and
\[
\mathbb P(A_j=B_i=1)=\frac{n-j}{n-1}q^{n-i-1}.
\tag{7}
\]
Subtracting the product of the marginal probabilities proves (4). Summing over \(i<j\), and putting \(m=n-i\), gives
\[
\operatorname{Cov}(C_n,T_n)=
\frac1{(n-1)^2}\sum_{m=2}^{n-1}\binom m2q^{m-1}.
\tag{8}
\]
The summands are nonnegative, and the \(m=2\) summand is positive for every \(n\ge3\). The geometric-series identity
\[
\sum_{m=2}^{n-1}\binom m2q^{m-1}
=\frac q2\frac{d^2}{dq^2}\left(\frac{1-q^n}{1-q}\right)
\tag{9}
\]
(with \(q\) treated as a formal variable during differentiation) and subsequent substitution \(q=(n-2)/(n-1)\) yield (2). Equation (8) also gives the asymptotic
\[
\frac{\operatorname{Cov}(C_n,T_n)}n\longrightarrow
\int_0^1\frac{t^2}2e^{-t}\,dt
=1-\frac5{2e}.
\tag{10}
\]

**2. Monotone coupling and association.** Independently for each \(j\ge2\), sample \(A_j\sim\operatorname{Bernoulli}((n-j)/(n-1))\) and an independent \(V_j\) uniform on \(\{1,\ldots,j-1\}\). If \(A_j=0\), attach \(j\) to \(V_j\); if \(A_j=1\), start a new root. This produces the same forest law as (5), since the original conditional choice of a lower parent is uniform. Take \(A_1=1\). For any fixed target vector \(V=(V_2,\ldots,V_n)\), turning one coordinate \(A_j\) from zero to one deletes exactly one edge to an older vertex; therefore it cannot decrease the number of terminal vertices. Both \(f(C_n)\) and \(g(T_n)\) are coordinatewise nondecreasing functions of the independent Bernoulli vector \((A_2,\ldots,A_{n-1})\). Harris's elementary product-measure covariance inequality gives nonnegative covariance conditional on \(V\). It follows by induction on the number of Bernoulli coordinates: conditioning on the last coordinate leaves nonnegative covariance by induction, while the conditional means of the two increasing functions are likewise increasing in the last Bernoulli coordinate. Since \(C_n\) is independent of \(V\), the covariance-of-conditional-means term vanishes when averaging over \(V\), establishing (1).

For strictness, one may take \(V_j=j-1\) for all \(j\ge3\) and \(A_j=0\) for all \(j\ge3\). This has positive probability. Changing \(A_2\) from zero to one then increases both \(C_n\) and \(T_n\) by exactly one: vertex 1 changes from nonterminal to terminal. The same Bernoulli-conditioning proof gives strictly positive covariance for any strictly increasing \(f,g\). This also proves an explicit monotone coupling of the terminal count when the full root-indicator vector is increased coordinatewise; no claim about monotonicity under conditioning **only** on the scalar component count is required.

**3. Variances and correlation.** From the independent root indicators, as already known for this forest [1, Proposition 3.1],
\[
\mathbb EC_n=\frac n2,\qquad
\operatorname{Var}(C_n)=\frac{n(n-2)}{6(n-1)}.
\tag{11}
\]
Also \(\mathbb ET_n=(n-1)(1-q^n)\). Put \(r=(n-3)/(n-1)\). For \(i<j\), the independence of the choices \(U_\ell\), with one excluded target when \(i<\ell\le j\) and two excluded targets when \(\ell>j\), yields
\[
\mathbb P(B_i=B_j=1)=q^{j-i}r^{n-j}.
\tag{12}
\]
Consequently,
\[
\operatorname{Var}(T_n)=
\sum_{i=1}^{n}q^{n-i}(1-q^{n-i})
+2\sum_{1\le i<j\le n}
\left(q^{j-i}r^{n-j}-q^{2n-i-j}\right).
\tag{13}
\]
For \(n\ge3\), the ratio \(r/q^2=1-(n-2)^{-2}\), and the difference inside the double sum is
\(q^{2n-i-j}[(1-(n-2)^{-2})^{n-j}-1]\).
Set \(t=(n-i)/n\), \(s=(n-j)/n\). The diagonal Riemann sum in (13), divided by \(n\), tends to
\[
\int_0^1e^{-t}(1-e^{-t})\,dt=
\frac12-e^{-1}+\frac12e^{-2}.
\]
For \(i<j\), \(0\le s<t\le1\), and uniformly over these indices the off-diagonal covariance multiplied by \(n\) tends to \(-s e^{-(t+s)}\). Thus the off-diagonal sum divided by \(n\) tends to
\[
-2\int_0^1\int_s^1 s e^{-(s+t)}\,dt\,ds
=-\frac12+2e^{-1}-\frac52e^{-2}.
\]
Adding gives
\[
\lim_{n\to\infty}\frac{\operatorname{Var}(T_n)}n
=e^{-1}-2e^{-2}=\frac{e-2}{e^2}>0.
\tag{14}
\]
The uniform approximation follows directly by Taylor expansion of \(\log(1-(n-2)^{-2})\) and \(\log q\), with \(0\le n-j\le n\); no independent limit theorem is invoked. Combining (10), (11), and (14) proves (3).

## Verification
The standalone standard-library script `verify.py` independently enumerates every possible attachment choice for \(3\le n\le7\), reconstructing each rooted forest from its edges. Across 50,068 configurations, it checks 425 exact-rational identities or inequalities: the cross-covariance kernel, terminal-pair probabilities, the closed covariance and moment formulas, and all nontrivial upper-quadrant threshold covariance inequalities. Its output on the packaged script is reported in `VERIFICATION.md`. Exhaustion at these small sizes is not a proof of the general identities, whose proofs are above.

## Relationship to prior work
Bienvenu, Duchamps and Foutel-Rodier [1] introduce and prove the uniform-attachment construction, the exact component-count marginal distribution, and the degree distribution. Those are used as **known inputs**, not rediscovered contributions. The new quantitative statements concern the *joint* behavior of component roots and zero-child terminals: the exact triangular kernel (4), positive association (1), exact finite covariance (2), and its nonvanishing asymptotic correlation (3). The source's degree-one and degree-zero vertices should not be conflated with our zero-child terminal vertices. Earlier work on uniform recursive forests [2] uses a different forest distribution; it is not an immediate model identification. Classical positive-association inequalities on Bernoulli product spaces supply the proof mechanism, not the forest-specific conclusions.

## Limitations
The claims concern the stated stationary Moran forest, not uniform random recursive forests, Cayley trees, or nonuniform parent-choice mechanisms. The correlation limit does not imply a bivariate central limit theorem. The variance and covariance calculations are algebraic consequences of the sampling construction in [1], and a prior implicit derivation from that construction cannot be ruled out. The older source [2] was accessible at abstract level but not in full text, leaving a bounded historical-priority risk.

## References
[1] F. Bienvenu, J.-J. Duchamps, F. Foutel-Rodier, *The Moran forest*, arXiv:1906.08806 (first public version June 20, 2019); Random Structures & Algorithms **59** (2021), 155–188. Author-hosted manuscript: https://www.normalesup.org/~bienvenu/articles/BienvenuRSA2021.pdf . In particular Sections 2.2, 3.1, and 4.1.

[2] K. T. Balińska, L. V. Quintas, J. Szymański, *Random recursive forests*, Random Structures & Algorithms **5** (1994), 3–12, doi:10.1002/rsa.3240050103. Different uniform recursive-forest model; the abstract was accessible, not the complete article.
