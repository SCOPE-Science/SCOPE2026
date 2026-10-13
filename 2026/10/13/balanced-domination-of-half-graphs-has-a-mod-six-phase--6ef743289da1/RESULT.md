# Balanced domination of half graphs has a mod-six phase
## Finding
For every integer
\[
n\ge1,
\]
let \(H_n\) be the half graph with bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
and adjacency
\[
a_i b_j\in E(H_n)\quad\Longleftrightarrow\quad i\le j.
\]

Every balanced dominating function
\[
f:V(H_n)\to\{-1,0,1\}
\]
is determined by a parameter \(t\in\{-1,0,1\}\). For a nonzero function its paired values \((f(a_i),f(b_i))\) repeat with period six as
\[
(t,-t),\ (0,-t),\ (-t,0),\ (-t,t),\ (0,t),\ (t,0).
\]
Such a nonzero function exists exactly when
\[
n\equiv1\pmod3.
\]
Consequently
\[
\gamma_b(H_n)=
\begin{cases}
2,&n\equiv4\pmod6,\\
0,&\text{otherwise}.
\end{cases}
\]
Equivalently, \(H_n\) is \(d\)-balanced exactly when \(n\not\equiv4\pmod6\).

More precisely, if \(n\not\equiv1\pmod3\), the zero function is the only balanced dominating function. If \(n\equiv1\pmod6\), there are exactly three balanced dominating functions and all three have weight zero. If \(n\equiv4\pmod6\), there are exactly three and their weights are \(-2,0,2\).

## Assumptions and scope
A balanced dominating function on a finite simple graph \(G\) is a map
\[
f:V(G)\to\{-1,0,1\}
\]
such that
\[
\sum_{u\in N_G[v]}f(u)=0
\]
for every vertex \(v\). Its weight is
\[
\omega(f)=\sum_{v\in V(G)}f(v),
\]
and the balanced domination number \(\gamma_b(G)\) is the maximum weight of a balanced dominating function. A graph is called \(d\)-balanced when \(\gamma_b(G)=0\).

The definition above is the one introduced in the cited 2021 primary source. The theorem covers every finite half graph, including the boundary \(H_1\cong K_2\).

## Proof
Write
\[
x_i=f(a_i),\qquad y_i=f(b_i).
\]
The closed-neighborhood equations are
\[
x_i+\sum_{j=i}^{n}y_j=0\qquad(1\le i\le n)
\tag{A_i}
\]
and
\[
y_j+\sum_{i=1}^{j}x_i=0\qquad(1\le j\le n).
\tag{B_j}
\]

Subtracting consecutive equations gives, for \(1\le i<n\),
\[
x_{i+1}=x_i+y_i
\]
and
\[
y_{i+1}=y_i-x_{i+1}=-x_i.
\]
The first boundary equation is
\[
x_1+y_1=0.
\]
Put \(t=x_1\), so \(y_1=-t\). Iterating the recurrence yields
\[
(x_i,y_i)=
\begin{cases}
(t,-t),&i\equiv1\pmod6,\\
(0,-t),&i\equiv2\pmod6,\\
(-t,0),&i\equiv3\pmod6,\\
(-t,t),&i\equiv4\pmod6,\\
(0,t),&i\equiv5\pmod6,\\
(t,0),&i\equiv0\pmod6.
\end{cases}
\]
Because every label must lie in \(\{-1,0,1\}\), the only possible values of the free parameter are \(t\in\{-1,0,1\}\).

The remaining endpoint equation is
\[
x_n+y_n=0.
\]
For \(t\ne0\), inspection of the six-periodic pattern shows that this holds exactly when
\[
n\equiv1\pmod3.
\]
Conversely, the recurrence makes all consecutive differences of the left sides of the \((A_i)\) equations zero and likewise for the \((B_j)\) equations. Hence the two endpoint equations force every closed-neighborhood equation. The displayed family is therefore complete.

It remains to calculate the weights. The six successive contributions \(x_i+y_i\) are
\[
0,-t,-t,0,t,t,
\]
whose sum over a full period is zero. Thus for \(n\equiv1\pmod6\), every feasible value of \(t\) gives weight zero. For \(n\equiv4\pmod6\), the nonzero functions have weight
\[
-2t,
\]
so the maximum is \(2\), attained at \(t=-1\). In all other congruence classes only \(t=0\) is feasible, completing the proof.

## Verification
The included verifier constructs \(H_n\) directly from the adjacency rule and checks the defining closed-neighborhood sum for every labeling in \(\{-1,0,1\}^{2n}\) for \(1\le n\le6\). It checks \(597{,}870\) labelings in total and recovers exactly the claimed balanced-function sets and weights.

A separate symbolic recurrence check evaluates all three starting values \(t\in\{-1,0,1\}\) for every \(1\le n\le120\), confirming both the endpoint feasibility condition and the weight formula. These computations corroborate the proof; they are not used to infer the infinite theorem.

## Relationship to prior work
The 2021 introducing paper defines balanced domination, proves general bounds, and identifies several \(d\)-balanced classes, including regular graphs, complete multipartite graphs, generalized ladders, and some joins. Its inspected full text does not contain the terms “half graph,” “chain graph,” or “Ferrers,” and none of its stated classes contains the half-graph family as a direct specialization.

A later 2025--2026 treatment reformulates balanced dominating functions as vectors in the kernel of the closed-neighborhood matrix \(A(G)+I(G)\) and develops exact results for convex-polytope graphs, trees, caterpillars, and grids. Its inspected full text likewise contains no occurrence of “half graph,” “chain graph,” “Ferrers,” or “bipartite.” The kernel formulation is compatible with the recurrence proof above, but it does not supply the half-graph congruence classification or the ternary weight analysis.

Spectral work on chain graphs gives general characteristic-polynomial machinery for adjacency matrices. Such results can detect whether \(-1\) is an adjacency eigenvalue after specialization, but an eigenvalue statement alone does not classify which kernel vectors have coordinates in \(\{-1,0,1\}\), nor their weights. The present theorem resolves exactly those balanced-domination constraints on the canonical twin-free chain graph.

## Limitations
The theorem concerns the standard half graph and does not classify balanced dominating functions of arbitrary chain graphs with repeated neighborhood classes.

The result is exact for the ternary balanced-domination definition. It does not assert an analogous congruence law for signed, Roman-balanced, or other domination variants.

Targeted literature and semantic searches cannot exclude a differently phrased or non-indexed earlier half-graph calculation. The general chain-graph characteristic-polynomial literature is a residual comparison risk, although no inspected source states the ternary balanced-function or weight classification proved here.

## References
1. B. Xu, W. Sun, S. Li, C. Li, “On the balanced domination of graphs,” *Czechoslovak Mathematical Journal* 71 (2021), 933–946, DOI 10.21136/CMJ.2021.0055-20; published online 11 October 2021.
2. B. Nikolic, M. Djukanovic, “Balanced Domination in Convex Polytopes, Trees, and Grid Graphs,” arXiv:2511.06539, first submitted 9 November 2025; version 3 dated 20 August 2026.
3. M. Anđelić, Z. Du, C. M. da Fonseca, S. K. Simić, “Tridiagonal matrices and spectral properties of some graph classes,” *Czechoslovak Mathematical Journal* 70 (2020), 1125–1138, DOI 10.21136/CMJ.2020.0182-19.
