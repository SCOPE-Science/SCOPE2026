# A microscopic two-crossing covariance window for induced four-vertex graphlets

## Finding

In the independent-edge Erdős–Rényi graph \(G(n,p)\), let \(A_n\) count induced copies of the four-vertex claw \(K_{1,3}\), and let \(B_n\) count induced copies of the four-vertex path \(P_4\). Each occurrence is counted once per four-element vertex set. For every integer \(n\ge4\) and every \(0<p<1\), their covariance is exactly

\[
\begin{aligned}
\operatorname{Cov}(A_n,B_n)
=6p^4(1-p)^5\bigg[&2p(2p-1)^2\binom n2\binom{n-2}2^2\\
&-(2p-1)(8p^2-4p+1)\binom n3(n-3)^2\\
&+4(6p^3-6p^2+3p-1)\binom n4\bigg].
\end{aligned}
\]

In particular, the covariance at the balanced density is strictly negative:

\[
\operatorname{Cov}(A_n,B_n)\big|_{p=1/2}=-\frac3{256}\binom n4\quad(n\ge4).
\]

The nontrivial sign crossover takes place in a *microscopic* density window. For every fixed real \(\lambda\), put \(p_n=1/2+\lambda/n\) (which lies in \((0,1)\) for all sufficiently large \(n\)). Then

\[
\lim_{n\to\infty}n^{-4}\operatorname{Cov}(A_n,B_n)
=\frac{12\lambda^2-8\lambda-1}{2048}.
\]

For all sufficiently large \(n\), two distinct zeros of the covariance lie near \(1/2\), at

\[
p_n^{\pm}=\frac12+\frac{2\pm\sqrt7}{6n}+O(n^{-2}).
\]

In every fixed bounded \(n(p-1/2)\)-window containing these two roots in its interior, they are the only zeros for all sufficiently large \(n\). The covariance is negative between the two roots and positive in the immediately neighboring regions within this window.

The corresponding individual variances at the balanced density obey

\[
\operatorname{Var}(A_n)=\frac{n^5}{1536}+O(n^4),\qquad
\operatorname{Var}(B_n)=\frac{n^5}{512}+O(n^4).
\]

Consequently, on the same microscopic density scale,

\[
\lim_{n\to\infty} n\operatorname{Corr}(A_n,B_n)
=\frac{\sqrt3}{4}(12\lambda^2-8\lambda-1).
\]

Thus even though the two normalized graphlet counts asymptotically decorrelate at these densities, their next-order covariance reveals a two-crossing, asymmetric sign transition.

## Assumptions and scope

Here \(G(n,p)\) is the finite simple undirected graph on labeled vertices \(\{1,\ldots,n\}\) in which all \(\binom n2\) edges are independent Bernoulli\((p)\) random variables. A claw has degree multiset \(\{3,1,1,1\}\), while a path \(P_4\) has degree multiset \(\{2,2,1,1\}\). For each four-element set, its contribution is one if its *induced* graph is of the specified type, and zero otherwise. The exact identity is for every \(n\ge4\) and every \(p\in(0,1)\). All limits have \(n\to\infty\) with the stated fixed \(\lambda\); the two root expansions concern locally defined roots, not a complete classification of all zeros throughout \(p\in(0,1)\).

## Proof

Write \(X_e\) for the indicator that unordered edge \(e\) is present, \(Y_e=X_e-p\), and \(q=p(1-p)\). Distinct squarefree monomials \(Y_T=\prod_{e\in T}Y_e\) are orthogonal in \(L^2\), and \(\mathbb E[Y_T^2]=q^{|T|}\). For a fixed four-element vertex set \(U\), let \(f_A(U)\) and \(f_B(U)\) denote its induced-claw and induced-path indicators. Their finite multilinear expansions are

\[
f_H(U)=\sum_{T\subseteq\binom U2}a_{H,T}(p)Y_T,
\qquad
 a_{H,T}(p)=\sum_{J\in\mathcal H}
(-1)^{|T\setminus J|}p^{3-|T\cap J|}(1-p)^{3-|T\setminus J|},
\]

where \(\mathcal H\) is the collection of the four labeled claws or the twelve labeled four-vertex paths, regarded as three-edge subsets of the six possible edges. This coefficient formula comes from expanding the exact indicator \(\prod_{e\in J}X_e\prod_{e\notin J}(1-X_e)\). In particular it is a finite identity, not an approximation.

For a nonempty edge set \(T\) supported on \(v\) vertices, its coefficient in the *total* count \(H_n\) is \(\binom{n-v}{4-v}a_{H,T}(p)\), because there are that many four-vertex sets extending its vertex support. Every such \(T\) has \(2\le v\le4\). Orthogonality therefore gives

\[
\operatorname{Cov}(A_n,B_n)
=\sum_{v=2}^4\binom nv\binom{n-v}{4-v}^{\!2}\,c_v(p),
\]

where \(c_v(p)\) is the sum over the labeled nonempty edge sets on \(v\) vertices that touch all \(v\) vertices of \(a_{A,T}(p)a_{B,T}(p)q^{|T|}\). Direct enumeration of these finitely many edge sets yields the three exact polynomials

\[
\begin{aligned}
c_2(p)&=12p^5(1-p)^5(2p-1)^2,\\
c_3(p)&=-6p^4(1-p)^5(2p-1)(8p^2-4p+1),\\
c_4(p)&=24p^4(1-p)^5(6p^3-6p^2+3p-1).
\end{aligned}
\]

Substituting proves the exact covariance formula, including the value at \(p=1/2\). These coefficients are also verified by the standalone exact-arithmetic program described below. The code enumerates all \(64\) four-vertex edge patterns for each graphlet, then checks the three polynomial identities at thirteen distinct rational probabilities; the polynomial degree bound of twelve makes these finite interpolation checks a complete symbolic certificate for the displayed identities.

For the microscopic limit, put \(\delta=\lambda/n\) and \(p=1/2+\delta\). The contributions from supports on two, three and four vertices have respectively the expansions

\[
\begin{aligned}
\binom n2\binom{n-2}2^2 c_2(p)&=\frac{3\lambda^2}{512}n^4+O_{\lambda}(n^3),\\
\binom n3(n-3)^2c_3(p)&=-\frac{\lambda}{256}n^4+O_{\lambda}(n^3),\\
\binom n4c_4(p)&=-\frac1{2048}n^4+O_{\lambda}(n^3).
\end{aligned}
\]

This proves the quadratic profile; its two simple zeros are \(\lambda_{\pm}=(2\pm\sqrt7)/6\). After scaling by \(n^{-4}\), the exact finite covariance is analytic in \(\lambda\) and \(1/n\) near any fixed real \(\lambda\) and converges with its first derivative uniformly on compact sets. The implicit function theorem near the two simple limiting roots gives \(\lambda_n^{\pm}=\lambda_{\pm}+O(n^{-1})\); uniform separation from zero away from these neighborhoods excludes additional local roots. The limiting polynomial is negative between its zeros and positive outside.

Finally, at \(p=1/2\), the only contribution of order \(n^5\) to the claw variance is the three-edge triangle monomial on three vertices: its local coefficient is \(-1/2\), so its leading term is \(\binom n3(n-3)^2(1/2)^2(1/4)^3=n^5/1536+O(n^4)\). The only contribution of order \(n^5\) to the path variance is the three wedge (two adjacent edges) monomials on three vertices, each with local coefficient \(-1/4\); the leading term is \(3\binom n3(n-3)^2(1/4)^2(1/4)^2=n^5/512+O(n^4)\). The edge coefficients of both graphlets vanish at \(p=1/2\), and their two distinct three-vertex projections are orthogonal. The same variance limits remain valid for \(p=1/2+\lambda/n\), since all perturbations contribute at lower order. Dividing the covariance limit by these two variance scales yields the claimed correlation profile.

## Verification

The accompanying `verify.py` uses only Python's standard library, constructs all four labeled claws and twelve labeled paths, and checks the complete mixed-projection polynomial identity using exact rational arithmetic. It also independently enumerates **all** labeled simple graphs on four, five and six vertices at three nondegenerate rational edge densities and compares directly computed covariances against the formula. A total of 74 exact certificate assertions pass. The finite enumerations check the finite formula; the asymptotic and root claims follow from the displayed exact expansions and the ordinary implicit function theorem, not from extrapolating finite numerical output.

Run from the artifact directory with `python verify.py`.

## Relationship to prior work

Induced four- and five-vertex graphlet statistics are natural network descriptors (Yaveroğlu and coauthors, arXiv:1405.7348, first posted May 28, 2014). Janson's 1990 work developed functional limit methods for random-graph subgraph statistics, including induced counts and exceptional nonnormal regimes. Sah and Sawhney (arXiv:2006.11369, Sections 1 and 4.2) give a general graph-factor expansion for induced subgraph counts and local limit theorems away from exceptional fixed densities. Bhattacharya, Chatterjee and Janson (arXiv:2104.07259) analyze higher-order fluctuations and degeneracy for graphon-based counts. These approaches establish the general counting and projection framework; the result here specifies the **mixed** claw–path covariance, its exact finite cancellations, and its two-root order-\(n^{-1}\) window. Their inspected statements do not provide this pair-specific microscopic covariance profile; priority through uninspected older treatments remains possible. No claim of a new general theory of induced subgraph counts or an asymptotic joint distribution is made.

## Limitations

This is an exact second-moment and local asymptotic statement in the independent-edge \(G(n,p)\) model, not in the fixed-edge \(G(n,m)\) model. It does not assert that the two motif counts are independent, that a joint central limit theorem holds, or that the covariance has only two roots over the entire interval \((0,1)\). The present literature comparison does not establish exhaustive historical priority, particularly because the full text of Janson's 1990 article could not be inspected. All claimed exact identities can be independently recomputed from the embedded finite expansions.

## References

- O. N. Yaveroğlu et al., *ergm.graphlets: A Package for ERG Modeling Based on Graphlet Statistics*, first public arXiv version May 28, 2014, https://arxiv.org/abs/1405.7348.
- S. Janson, *A functional limit theorem for random graphs with applications to subgraph count statistics*, *Random Structures & Algorithms* 1 (1990), 15–37, https://doi.org/10.1002/rsa.3240010103.
- A. Sah and M. Sawhney, *Local limit theorems for subgraph counts*, arXiv:2006.11369 (first posted June 19, 2020), https://arxiv.org/abs/2006.11369; *J. Lond. Math. Soc.* 105 (2022), 950–1011, https://doi.org/10.1112/jlms.12523.
- B. B. Bhattacharya, A. Chatterjee and S. Janson, *Fluctuations of Subgraph Counts in Graphon Based Random Graphs*, arXiv:2104.07259 (first posted April 15, 2021), https://arxiv.org/abs/2104.07259.
