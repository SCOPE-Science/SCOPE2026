# Sparse random formal contexts: a marked four-cycle correction law

## Finding
For each fixed real \(c>0\), let \(\mathcal K_n\) be the random formal context with \(n\) labelled objects, \(n\) labelled attributes, and independent incidences of probability \(p_n=c/n\), for integers \(n>c\). Write \(C_n\) for its number of formal concepts. In its bipartite incidence graph let \(D_n\) count vertices of degree at least two and let \(I_n\) count isolated-edge components (copies of \(K_{1,1}\) that are connected components). Then
\[
\frac{C_n}{n}\xrightarrow{\mathbb P}g(c)
=2\bigl(1-(1+c)e^{-c}\bigr)+ce^{-2c},
\]
and the **integer-valued, unscaled correction** obeys
\[
C_n-2-D_n-I_n\ \xrightarrow{d}\
\sum_{j=1}^{P_c}J_j,\qquad
P_c\sim\operatorname{Poisson}(c^4/4),\quad
J_j\overset{\mathrm{iid}}{\sim}1-\operatorname{Binomial}(4,e^{-c}),
\]
where the marks and \(P_c\) are independent. Equivalently, with \(q=e^{-c}\), the correction's limiting characteristic function is
\[
\exp\!\left[\frac{c^4}{4}\left(e^{it}(1-q+qe^{-it})^4-1\right)\right].
\]
The correction can be negative or positive; no central-limit assertion for \(C_n\), almost-sure assertion, or convergence of expectations is made.

## Assumptions and scope
A formal context \((U,V,\mathcal I)\) consists of objects \(U\), attributes \(V\), and incidences \(\mathcal I\subseteq U\times V\). For \(A\subseteq U\), define \(A'=\{v\in V:\forall u\in A,\ (u,v)\in\mathcal I\}\), with vacuous intersections for empty sets, and analogously define \(B'\subseteq U\) for \(B\subseteq V\). A concept is \((A,B)\) satisfying \(A'=B\) and \(B'=A\). A non-boundary concept is a maximal complete bipartite subgraph with both vertex classes nonempty. The incidence probability \(c/n\) is *sparse* and varies with \(n\); \(c\) does not vary with \(n\). All convergence is with respect to the distribution at size \(n\), so no coupling between different sizes is required.

For a four-cycle \(H\), regarded as one \(K_{2,2}\), let \(z(H)=|\{v\in V(H):\deg(v)=2\}|\). Such a vertex has no neighbors outside its four-cycle. Every four-cycle is counted once, independent of orientation.

## Proof
**1. A deterministic structural identity on a high-probability class.** Suppose a bipartite graph has (i) an isolated vertex in each part, (ii) no copy of \(K_{2,3}\) or \(K_{3,2}\), and (iii) vertex-disjoint distinct four-cycles. Every non-boundary formal concept is a maximal biclique with nonempty shores. If both shores have at least two vertices, then (ii) forces both shores to have exactly two vertices; it is a unique four-cycle biclique. Otherwise it is a star: a maximal biclique whose one shore is a singleton. A star centered at a vertex of degree at least two is maximal except when that vertex has degree exactly two and is on a four-cycle. Indeed, a failure of maximality means another vertex sees every neighbor of the center, producing a four-cycle, and condition (ii) precludes extra shared neighbors. A one-edge biclique is maximal precisely when its endpoints both have degree one. By (i), the two boundary concepts are distinct and cannot coincide with these. Hence, writing \(\mathcal Q\) for the set of four-cycles,
\[
C=2+D+I+\sum_{H\in\mathcal Q}(1-z(H)).\tag{1}
\]
In particular, the cycles act as *local identifications of star concepts*, not as freely addable new bicliques.

**2. The structural event is asymptotically certain.** There are \(\binom n2\binom n3\) candidate labelled \(K_{2,3}\)'s and the same number of \(K_{3,2}\)'s, each requiring six incidences. Thus their expected combined count is \(O_c(n^5(c/n)^6)=O_c(n^{-1})\). An ordered pair of distinct four-cycles sharing a vertex has a union with more edges than vertices; a finite case analysis by intersection type gives expected count \(O_c(n^{-1})\). Each side has \(n\) independent vertex-isolation indicators with success probability \((1-c/n)^n\to e^{-c}>0\), so the probability of no isolated vertex on either side is exponentially small. Markov's inequality proves that the hypotheses of (1) hold with probability \(1-O_c(n^{-1})\).

**3. The marked four-cycle limit.** Let \(X_{n,z}\) count four-cycles with precisely \(z\) degree-two vertices, for \(0\le z\le4\). There are \(\binom n2^2\) possible four-cycles. Given its four edges, each vertex has \(\operatorname{Binomial}(n-2,c/n)\) other incident edges, independently of the other three vertices, so the chance of exactly \(z\) degree-two vertices tends to \(\binom4z q^z(1-q)^{4-z}\) for \(q=e^{-c}\). For any fixed factorial moment order, choices of vertex-disjoint four-cycles contribute the product of these limiting probabilities times \((c^4/4)^k\). Any choice with intersecting cycles has a union with strictly more edges than vertices and contributes \(O_c(n^{-1})\); finitely many cross-edges between disjoint selected cycles alter marks by \(o(1)\). Consequently, by the multivariate factorial-moment method,
\[
(X_{n,0},\ldots,X_{n,4})\xrightarrow{d}(Z_0,\ldots,Z_4),
\quad Z_z\text{ independent Poisson}\!\left(\frac{c^4}{4}\binom4zq^z(1-q)^{4-z}\right).
\]
Equation (1), valid with probability tending to one, now gives \(C_n-2-D_n-I_n\xrightarrow d\sum_z(1-z)Z_z\), the stated marked compound-Poisson law.

**4. Linear typical scale.** Every vertex has degree \(\operatorname{Binomial}(n,c/n)\). Thus
\[
\frac{\mathbb E D_n}{n}=2\left(1-(1-c/n)^n-n(c/n)(1-c/n)^{n-1}\right)
\longrightarrow2(1-(1+c)e^{-c}).
\]
Indicators for vertices within one bipartite class are independent; across classes, any pair shares only one edge, giving covariance at most \(c/n\). Hence \(\operatorname{Var}(D_n)=O_c(n)\). Writing \(I_n\) as the sum over possible isolated edges gives
\[
\mathbb E I_n=n^2(c/n)(1-c/n)^{2n-2}=cn(1-c/n)^{2n-2}.
\]
Two isolated-edge indicators sharing an endpoint cannot both be one. For disjoint endpoints their joint probability is \((c/n)^2(1-c/n)^{4n-6}\); comparison with the product of marginal probabilities shows \(\operatorname{Var}(I_n)=O_c(n)\). Therefore \(D_n/n\) and \(I_n/n\) converge in \(L^2\) to their claimed constants. The correction from step 3 is tight, hence divided by \(n\) vanishes in probability. This proves the first limit.

## Verification
The standalone `VERIFY.py` checks, independently of the proof, the formal concept count computed directly via the two Galois derivation operators against the deterministic four-cycle identity for **every** bipartite graph with \(n\le4\) vertices on each side that satisfies its structural hypotheses (including 5,005 qualifying graphs for \(n=4\)). It also constructs five explicit contexts with exactly one four-cycle and all five possible values \(z=0,1,2,3,4\), verifying each predicted correction \(1-z\). Run `python3 VERIFY.py` using Python 3.9 or later. These are finite consistency checks; they do not establish the infinite-size probability limits.

## Relationship to prior work
Kovács (2018) developed the independent-incidence approach and a formula for expected formal concept counts, including sparse-data computational heuristics. Sakurai (2021) derived a general expectation identity and a superpolynomial expected-count lower bound in a different, fixed-density regime. Those general formulas and the concept–maximal-biclique correspondence are background, not new assertions here. Baudin, Magnien, and Tabourier (2024) analyze enumeration algorithms on sparse bipartite graphs, not their Bernoulli concept-count law. The claimed addition is the deterministic four-cycle *defect identity* on the typical sparse class, its full non-Gaussian marked-Poisson distribution, and the explicit linear typical-scale coefficient. The general expectation identities do not imply the defect distribution without further analysis.

## Limitations
The model has two equal, labelled parts and fixed \(c>0\) with independent edges of probability \(c/n\). No result is claimed for dense fixed probability, degree-conditioned random graphs, dependent incidences, unequal aspect ratios, or \(c\) varying with \(n\). The Poisson limit is an **unscaled residual after subtracting two observed degree-based statistics**, not the full fluctuation law for \(C_n\). The probability of a structural exception tends to zero, but no deterministic identity is asserted for arbitrary graphs containing overlapping four-cycles or larger complete bipartite subgraphs. Literature coverage is not exhaustive, so an earlier equivalent formulation remains possible.

## References
- L. Kovács, *Efficient approximation for counting of formal concepts generated from formal context*, Miskolc Mathematical Notes 19 (2018), 983–996, DOI: 10.18514/MMN.2018.2529. Full text: https://real.mtak.hu/92004/1/2529.pdf.
- T. Sakurai, *On formal concepts of random formal contexts*, arXiv:2101.11023v1, first public 2021-01-26. https://arxiv.org/abs/2101.11023.
- A. Baudin, C. Magnien, L. Tabourier, *BBK: a simpler, faster algorithm for enumerating maximal bicliques in large sparse bipartite graphs*, arXiv:2405.04428, 2024. https://arxiv.org/abs/2405.04428.
