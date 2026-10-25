# Triangle-controlled covariance of isolated percolation components

## Finding

Let \(G\) be any finite simple \(d\)-regular graph on \(n\) vertices, with \(d\ge 2\), and let \(t(G)\) be its number of (unoriented) triangles. Independently retain every edge with probability \(p\in[0,1]\), putting \(q=1-p\). Let \(X_1\) count isolated vertices of the retained-edge graph and \(X_2\) count its two-vertex connected components (isolated retained edges). Then, for every such \(G\) and every \(p\),

\[
\operatorname{Cov}(X_1,X_2)=nd\,p\,q^{3d-3}(dp-1)+3t(G)\,p^3q^{3d-4}.
\]

Thus the entire mixed covariance depends on the host graph only through \(n\), \(d\), and its triangle count. Set \(\tau=3t(G)/(nd)\) and

\[
 p_*(G)=\frac{2}{d+1+\sqrt{(d-1)^2+4\tau}}.
\]

For \(0<p<1\), the covariance is negative if \(p<p_*(G)\), zero exactly at \(p=p_*(G)\), and positive if \(p>p_*(G)\). If \(G\) is triangle-free then \(p_*(G)=1/d\); if it contains a triangle, then \(p_*(G)<1/d\). At \(p=0\) and \(p=1\) the covariance is zero.

In particular, for the \(d\)-dimensional hypercube \(Q_d\) (\(d\ge2\)), which has \(2^d\) vertices and no triangles,

\[
\operatorname{Cov}(X_1,X_2)=2^d d p(1-p)^{3d-3}(dp-1).
\]

For fixed \(\lambda\ge0\) and \(p=\lambda/d\) when \(d>\lambda\),

\[
\lim_{d\to\infty}2^{-d}\operatorname{Cov}(X_1,X_2)
=\lambda(\lambda-1)e^{-3\lambda}.
\]

The finite-dimensional sign boundary \(p=1/d\) is an **exact covariance crossover**, not a claim that the finite-graph percolation critical probability equals \(1/d\).

## Assumptions and scope

The host \(G=(V,E)\) is deterministic, simple, finite, undirected, and \(d\)-regular; connectedness is not assumed. All edge-retention indicators are independent and have the same parameter \(p\). An isolated vertex has retained degree zero. A two-vertex component is one retained edge whose two endpoints have no other retained incident edges. In particular, \(X_2\) counts connected components, not arbitrary degree-one pairs or induced edges of the host. The result holds without limits for all integer \(d\ge2\), every admissible \(n\), and all \(p\in[0,1]\). There is no randomness in the host graph.

## Proof

For \(v\in V\), write \(A_v\) for the indicator that \(v\) is isolated in the retained graph. For each host edge \(e=xy\), write \(B_e\) for the indicator that \(e\) is the entire component of its endpoints. Thus \(X_1=\sum_v A_v\) and \(X_2=\sum_e B_e\). Since \(G\) is simple and \(d\)-regular,

\[
 \mathbb E A_v=q^d,\qquad \mathbb E B_e=pq^{2d-2},\qquad
 \mathbb E A_v\,\mathbb E B_e=pq^{3d-2}.
\]

Fix \(e=xy\), and let \(r(v,e)\) be the number of endpoints of \(e\) adjacent to \(v\), when \(v\notin\{x,y\}\). If \(v=x\) or \(v=y\), then \(A_vB_e=0\). Otherwise, the required open and closed edges are consistent. Exactly \(r(v,e)\) edges are constrained closed by both events, giving

\[
 \mathbb E(A_vB_e)=p q^{3d-2-r(v,e)}
 \quad (v\notin\{x,y\}).
\]

Let \(c_e=|N(x)\cap N(y)|\), the number of triangles through the host edge \(e\). Excluding \(x,y\), there are \(c_e\) vertices with \(r=2\), exactly \(2(d-1-c_e)\) vertices with \(r=1\), and all remaining vertices have \(r=0\). The last class has zero covariance. Therefore

\[
\begin{aligned}
\sum_{v\in V}\operatorname{Cov}(A_v,B_e)
={}&-2p q^{3d-2}
+2(d-1-c_e)p^2q^{3d-3}\\
&+c_e p q^{3d-4}(1-q^2)\\
={}&p q^{3d-4}\bigl[2q(dp-1)+c_e p^2\bigr].
\end{aligned}
\]

This equality also holds at \(p=0,1\), since the factored exponents are nonnegative for \(d\ge2\). Summing over all \(nd/2\) edges and using the exact triangle-incidence identity \(\sum_{e\in E}c_e=3t(G)\) proves the finite covariance formula.

For the sign claim take \(0<p<1\), so \(p q^{3d-4}>0\). Factoring \(nd\) from the bracket shows that the sign equals that of

\[
 F(p)=q(dp-1)+\tau p^2
 =-1+(d+1)p-(d-\tau)p^2.
\]

Each vertex is in at most \(\binom d2\) triangles, so \(0\le\tau\le(d-1)/2\); in particular \(d-\tau>0\). The discriminant of \(F\) is \((d-1)^2+4\tau\). Its smaller positive zero is the displayed \(p_*(G)\). The polynomial begins at \(F(0)=-1\) and has \(F(1)=\tau\ge0\). If \(\tau>0\), its larger zero exceeds one. If \(\tau=0\), its zeros are \(1/d\) and one. These observations establish all strict signs and boundary cases.

The hypercube specialization substitutes \(n=2^d\) and \(t(Q_d)=0\). For the stated scaling, \((1-\lambda/d)^{3d-3}\to e^{-3\lambda}\) and \(dp-1=\lambda-1\), yielding the limit; no interchange of infinite sums is involved.

## Verification

Run `python3 verify.py` from the directory containing this file and `verify.py`; it requires only the Python standard library. The checker enumerates every retained-edge configuration at three exact rational probabilities on eight regular host graphs (24 graph/probability strata, including triangle-free and triangle-rich cases) and compares rational covariances with the displayed formula. It also checks the finite crossover on triangle-free examples. These are independent finite diagnostics; the universal claims are established by the event-overlap proof above, not by enumeration.

## Relationship to prior work

Hulshof and Nachmias [1] study sizes, diameters, and mixing times of near-critical hypercube components; their foundational model has primary classification 60K35. McDiarmid, Scott, and Withers [2] explicitly calculate means of size-one and size-two components and prove joint Poisson approximation for small-component counts in the fixed-\(p\), high-dimensional hypercube (their equation (2) and Theorem 17). That joint approximation does not give an exact finite covariance or resolve the sign at the varying probability \(p=\lambda/d\). The present calculation instead isolates all exact mixed second-moment contributions, showing that *only host triangles* affect the correction to regular-graph universality. It does not assert priority over any unidentified earlier exact calculation.

The general small-component dependency-graph technique used in [2] is related to the event classification in the proof, but its stated theorems provide asymptotic distributional approximation rather than the precise formula, its triangle dependence, or its all-parameter crossover. General hypercube percolation phase-transition results [1,3] motivate the scaling \(p=\lambda/d\), but are not being reproved.

## Limitations

This is an exact second-moment identity, not a joint distribution, concentration theorem, or determination of the finite hypercube critical probability. Only independent uniform edge retention on a deterministic regular simple host is addressed; irregular hosts, dependent edge models, and larger-component covariances require different counts. The near-critical scale comparison is asymptotic and must not be interpreted as an equality between the finite percolation threshold and the covariance zero. Historical priority remains subject to examination of inaccessible work on isolated-vertex and isolated-edge generating polynomials [4] and older general small-component formulas.

## References

[1] T. Hulshof and A. Nachmias, *Slightly subcritical hypercube percolation*, arXiv:1612.01772 (first public version December 6, 2016); *Random Structures & Algorithms* 56 (2020), 557–593. https://arxiv.org/abs/1612.01772

[2] C. McDiarmid, A. Scott, and P. Withers, *The component structure of dense random subgraphs of the hypercube*, arXiv:1806.06433 (first public version June 17, 2018); *Random Structures & Algorithms* 59 (2021), 3–24. https://arxiv.org/abs/1806.06433

[3] C. Borgs, J. Chayes, R. van der Hofstad, G. Slade, and J. Spencer, *Random subgraphs of finite graphs: I. The scaling window under the triangle condition*, *Random Structures & Algorithms* 27 (2005), 137–184. https://doi.org/10.1002/rsa.20051

[4] M. Das, *Isolated Vertices in Random Subgraphs*, Master's thesis, Hochschule Mittweida (2021; repository release January 4, 2022), metadata and abstract only inspected. https://monami.hs-mittweida.de/frontdoor/index/index/docId/12887
