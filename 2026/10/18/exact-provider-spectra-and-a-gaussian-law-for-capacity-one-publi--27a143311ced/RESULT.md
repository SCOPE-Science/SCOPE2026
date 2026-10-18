# Exact provider spectra and a Gaussian law for capacity-one public-goods equilibria on paths and rings

## Finding
Consider the exact capacitated-domination representation of specialized public-goods Nash equilibria, with capacity one at every vertex. On the labeled path \(P_n\) (\(n\ge 2\)) and labeled cycle \(C_n\) (\(n\ge 3\)), write \(B_{n,k}\) and \(A_{n,k}\), respectively, for the number of full DP-Nash subgraphs having exactly \(k\) contributors (the \(D\)-vertices). A full subgraph includes the provider/consumer partition **and** the chosen sharing edges, so this is not merely a count of distinct contributor sets.

For every integer \(k\), the exact counts are
\[
 B_{n,k}=\binom{n-k}{2k-n}2^{2n-3k},\qquad
 A_{n,k}=\frac{n}{n-k}\binom{n-k}{2k-n}2^{2n-3k}
\]
when \(\lceil n/2\rceil\le k\le\lfloor2n/3\rfloor\), and they are zero otherwise. The nonzero range is sharp. Thus closing a path into a ring multiplies the number of full equilibria with exactly \(k\) contributors by the **exact** factor \(n/(n-k)\).

With formal generating variable \(z\) for contributors, define \(B_n(z)=\sum_k B_{n,k}z^k\) and \(A_n(z)=\sum_k A_{n,k}z^k\). Their complete generating functions are
\[
 \sum_{n\ge0} B_n(z)t^n=\frac{1}{1-2zt^2-z^2t^3},\qquad
 A_n(z)=-n[t^n]\log(1-2zt^2-z^2t^3).
\]
The first identity uses formal auxiliary conventions \(B_0(z)=1\) and \(B_1(z)=0\); the second is asserted for \(n\ge3\).

If a full DP-Nash subgraph of \(C_n\) is selected uniformly, and \(K_n\) denotes its number of contributors, then
\[
 \frac{K_n-\mu n}{\sqrt{\sigma^2n}}\ \Longrightarrow\ \mathcal N(0,1),
 \qquad \mu=1-\frac1{\sqrt5},\qquad
 \sigma^2=1-\frac{11}{5\sqrt5}>0.
\]
In particular, the contributor fraction converges in probability to \(\mu\), strictly between one half and two thirds. The variance coefficient is about \(0.016130089900\).

## Assumptions and scope
Let \(G=(V,E)\) be an undirected finite simple graph, with every vertex having capacity \(\kappa(v)=1\). A **full DP-Nash subgraph** consists of a labeled bipartition \(V=D\sqcup P\) and a spanning subgraph \(H\subseteq G\), whose edges cross \(D\) and \(P\), such that each \(v\in D\) has degree exactly one in \(H\) and each \(v\in P\) has degree at least one in \(H\). These are the specialized Nash configurations in the graph-theoretic formulation of Gerke, Gutin, Hwang and Neary. Since all path and cycle vertices have positive degree, their capacity is exactly one. Different subgraphs or differently labeled bipartitions are counted separately, even when their sets of contributors happen to coincide. Graph vertices and edges are labeled (no quotient by rotation/reflection). The stochastic assertion is purely a uniform counting measure over these configurations, not a behavioral claim about equilibrium selection.

## Proof
**1. Structural bijection.** Every \(D\)-vertex has exactly one incident edge in \(H\). Consequently each connected component of \(H\) is a star centered at one \(P\)-vertex, with at least one \(D\)-leaf; no \(P\)-vertex is isolated. As \(P_n\) and \(C_n\) have maximum degree two, the possible components have either two vertices (one \(D\), one \(P\), with two possible provider orientations along a prescribed edge) or three vertices (a consecutive \(D\)-\(P\)-\(D\) path, with one possible provider assignment). Conversely, any spanning decomposition into disjoint consecutive two- and three-vertex components, with those orientations, is a full DP-Nash subgraph. For \(C_3\) each length-three component consists of a two-edge path inside the triangle, determined by its central \(P\)-vertex. Hence the bijection also applies at the minimum cycle size.

Write \(l\) for the number of two-vertex components and \(j\) for the three-vertex components. Then \(n=2l+3j\), and \(k=l+2j\). Solving gives \(l=2n-3k\), \(j=2k-n\) and \(l+j=n-k\). Their nonnegativity is equivalent to the claimed sharp range. Conversely every pair \((l,j)\) of nonnegative integers with \(2l+3j=n\) is realizable on a path or cycle.

**2. Exact path and cycle counts.** For a path, choose the ordered positions of the \(j\) triple-components among the \(m=l+j=n-k\) components in \(\binom{m}{j}\) ways. Each two-vertex component admits two provider orientations, so the count is \(\binom{m}{j}2^l\). On a cycle, count pairs consisting of a configuration together with a distinguished starting component boundary. Every cyclic ordered string of \(m\) component types with weighted orientations has \(m\) choices of distinguished boundary, while the labeled cycle offers \(n\) possible positions for that starting boundary. Thus the cycle count is \(n\binom{m}{j}2^l/m\). This double counting is valid for periodic component strings too because the vertices remain labeled and every configuration has exactly \(m\) component boundaries. It yields both exact coefficient formulas and the ratio.

**3. Generating functions.** The two possible oriented pair blocks each contribute \(zt^2\), and each triple contributes \(z^2t^3\), so the weight of one generic component is \(W(t,z)=2zt^2+z^2t^3\). A path is a sequence of such components, giving \(1/(1-W)\). The rooted cyclic decomposition computed above is \(-n[t^n]\log(1-W)\); indeed the coefficient of \(-\log(1-W)\) is \(\sum_{m\ge1}W^m/m\). This derivation is formal and does not assume analyticity.

**4. Gaussian limit.** Let \(\lambda_1(z),\lambda_2(z),\lambda_3(z)\) be the three roots (with multiplicity) of \(\lambda^3-2z\lambda-z^2=0\). Factorization of \(1-2zt^2-z^2t^3\) gives
\[
 A_n(z)=\lambda_1(z)^n+\lambda_2(z)^n+\lambda_3(z)^n.
\]
At \(z=1\) these roots are \(\varphi=(1+\sqrt5)/2\), \(-1\), and \((1-\sqrt5)/2\), so \(\varphi\) is positive, simple, and strictly dominant in absolute value. For \(z=e^u\) with \(u\) complex in a fixed small neighborhood of zero, the dominant root \(\lambda(e^u)\) continues analytically, remains isolated, and the other roots have uniformly smaller modulus. It follows uniformly in that neighborhood that
\[
 \log\mathbb E[e^{uK_n}]
 =n\bigl(\log\lambda(e^u)-\log\varphi\bigr)+O(\rho^n)
\]
for some \(\rho\in(0,1)\), choosing the analytic logarithm near zero. Implicitly differentiating the root equation at \(u=0\) gives
\[
 \left.\frac{d}{du}\log\lambda(e^u)\right|_{u=0}=1-\frac1{\sqrt5},\qquad
 \left.\frac{d^2}{du^2}\log\lambda(e^u)\right|_{u=0}=1-\frac{11}{5\sqrt5}.
\]
The second derivative is strictly positive. Substituting \(u=it/\sqrt{\sigma^2n}\), subtracting the deterministic centering term, and expanding the analytic logarithm to second order gives the characteristic function limit \(e^{-t^2/2}\) for each fixed real \(t\). Lévy's continuity theorem proves the displayed central limit theorem. Analytic differentiation also gives \(\mathbb EK_n=\mu n+O(n\rho^n)\) and \(\operatorname{Var}(K_n)=\sigma^2n+O(n^2\rho^n)\); the weaker convergences alone already follow from the CLT plus those analytic moment bounds.

## Verification
The accompanying standalone `verify_capacity_cycle.py` script runs using only Python's standard library. Invoke `python verify_capacity_cycle.py`. It independently enumerates bipartitions and all selected edge subsets for each path and cycle of sizes \(3\) through \(9\), checks the exact provider-count coefficients, checks the path polynomial recurrence and the known total cycle recurrence through size \(32\), and compares exact finite-size moments with the derived limiting constants. Its expected opening line is `VERIFIED: 77 independent exact/asymptotic checks`; representative coefficients are \(A_{8,4}=32\), \(A_{8,5}=16\), \(B_{8,4}=16\), and \(B_{8,5}=6\). Finite tests are not used as proofs of the exact formulas or the limit theorem.

## Relationship to prior work
Gerke, Gutin, Hwang and Neary introduced the constrained-sharing public-goods equilibrium model; Gutin, Neary and Yeo established general exact-capacitated-domination properties and explicitly observed that capacity-one DP-Nash subgraphs are disjoint spanning stars. The star description and Nash correspondence are **previously known**, not original contributions here. The latter work also discusses counting such configurations as a problem. The present statement gives, for the degree-two path and cycle families, the complete **contributor-refined** counting spectrum, exact ring-to-path comparison, and corresponding asymptotic equilibrium-composition law. The univariate ring total \(A_n(1)=L_n+(-1)^n\) agrees with **already catalogued OEIS A099925**; neither this numerical sequence nor its recurrence is claimed as new. The contribution is not a new abstract dimer/trimer counting mechanism but the precise equilibrium identification, refinement, and asymptotic consequence for the specified game.

## Limitations
The provider spectrum counts full graph-theoretic DP-Nash subgraphs, not necessarily distinct sets of contributors, payoff levels, non-specialized equilibria, or strategic adjustment paths. For general graphs of degree at least three, connected capacity-one components may be larger stars and the formulas do not apply. The CLT concerns uniform selection among full cycle equilibria and makes no claim that a population actually selects equilibria uniformly. The simple star-component reduction is previously established; unlocated equivalent weighted-tiling or game-specific enumerations remain a publication-priority risk. Independent scientific verification has not been performed.

## References
1. S. Gerke, G. Gutin, S.-H. Hwang and P. R. Neary, *Public goods in networks with constraints on sharing*, arXiv:1905.01693, initial public version May 5, 2019. https://arxiv.org/abs/1905.01693
2. G. Gutin, P. R. Neary and A. Yeo, *Exact capacitated domination: on the computational complexity of uniqueness*, arXiv:2003.07106, initial public version March 16, 2020. https://arxiv.org/abs/2003.07106
3. On-Line Encyclopedia of Integer Sequences, A099925, *a(n) = Lucas(n) + (-1)^n*, https://oeis.org/A099925 . This records the already-known scalar sequence, not the contributor-refined game-theoretic statement.
