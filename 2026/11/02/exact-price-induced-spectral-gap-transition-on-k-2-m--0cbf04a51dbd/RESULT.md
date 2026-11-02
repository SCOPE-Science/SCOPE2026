# Exact price-induced spectral-gap transition on \(K_{2,m}\)

## Finding

Fix an integer \(m\ge3\), positive conductance prices \(p,q\), and a positive budget \(B\). Consider the complete bipartite graph \(K_{2,m}\), with two distinguished hubs and \(m\) other vertices. Every edge incident to the first hub costs \(p\) per unit conductance; every edge incident to the second hub costs \(q\). Conductances of all \(2m\) edges are freely and independently nonnegative. Maximize the second-smallest eigenvalue \(\lambda_2(L)\) of the **unnormalized** weighted Laplacian subject to total price at most \(B\).

Relabel hubs, if needed, so that \(p\le q\). Put
\[
\delta=\sqrt{\frac{m-2}{m+2}},\qquad
T=\sqrt{\frac qp}+\sqrt{\frac pq},\qquad
H=m^2-2.
\]
Define
\[
C_*=
\begin{cases}
\displaystyle \frac m2\bigl[p(1+\delta)+q(1-\delta)\bigr],&T\le H,\\[3mm]
\displaystyle \frac{(m+1)(p+q)+2\sqrt{pq}}{m+2},&T>H.
\end{cases}
\]
Then the exact unrestricted optimum is
\[
\boxed{\max\lambda_2(L)=\frac{B}{C_*}.}
\]
An optimum is obtained by assigning the same conductance to all edges of each hub, namely \(w_{1i}=(B/C_*)u\) and \(w_{2i}=(B/C_*)v\), where
\[
(u,v)=
\begin{cases}
\left(\frac{1+\delta}{2},\frac{1-\delta}{2}\right),&T\le H,\\[2mm]
\left(\frac{m+1+\sqrt{q/p}}{m(m+2)},
\frac{m+1+\sqrt{p/q}}{m(m+2)}\right),&T>H.
\end{cases}
\]
All the exhibited optimal edge conductances are strictly positive. For \(p<q\), the orbit-constant optimum is unique. In that unequal-price case the optimal Fiedler eigenvalue has multiplicity \(m\) when \(T\le H\) and multiplicity one when \(T>H\). At \(p=q\), orbit-constant optimizers need not be unique: all \(u+v=1\) with \(uv\ge1/(m+2)\), after scaling by \(B/(mp)\), are optimal. No classification of *asymmetric* optimizers is asserted.

## Assumptions and scope

The graph is precisely \(K_{2,m}\), with no hub-to-hub or leaf-to-leaf edges. Each edge is independently allocated nonnegative conductance; no upper bound besides the total strictly positive linear cost is imposed. Both price classes are positive and constant across their own hub's edges. \(m\) is an integer at least three. The budget is an inequality, and homogeneity implies equality at the optimum. No normalization by vertex degrees or stochastic transition matrix is used. For the eigenvalue multiplicity assertion we assume unequal prices; the equal-price exception is expressly covered above.

## Proof

**Symmetrization.** For a Laplacian \(L\), \(\lambda_2(L)\) is the minimum of \(x^{\mathsf T}Lx\) over unit vectors orthogonal to the all-ones vector, hence is concave in the edge conductances. Permuting the \(m\) peripheral vertices preserves both prices and the budget. Averaging any feasible conductance vector over these permutations cannot reduce \(\lambda_2\). Therefore an unrestricted optimizer exists with conductance \(u\) on each edge at the first hub and \(v\) on each edge at the second hub. This is an existence/value reduction, not an assertion of unrestricted uniqueness.

**Exact spectrum.** Set \(s=u+v\). Leaf-difference vectors give eigenvalue \(s\) of multiplicity \(m-1\). The remaining three-dimensional hub/constant-leaf subspace has eigenvalues zero and the two roots \(\lambda_-\le\lambda_+\) of
\[
F(z)=z^2-(m+1)sz+m(m+2)uv.
\]
Consequently \(\lambda_2(L)=\min\{s,\lambda_-\}\). For strictly positive weights, all nonzero eigenvalues are positive. By common scaling, maximizing the gap with budget \(B\) is equivalent to minimizing cost \(m(pu+qv)\) subject to \(\lambda_2\ge1\), and subsequently scaling the resulting weights by \(B/C_*\). Requiring \(\lambda_2\ge1\) is equivalent to
\[
s\ge1,\qquad uv\ge\frac{(m+1)s-1}{m(m+2)}.
\]
Indeed, \(\lambda_+\ge(m+1)s/2>1\) for \(m\ge3\), so \(F(1)\ge0\) is equivalent to \(\lambda_-\ge1\).

**One-dimensional convex allocation.** Since \(p\le q\), at each fixed \(s\ge1\) the least costly admissible split uses the smallest admissible \(v\):
\[
v(s)=\frac{s-\sqrt{D(s)}}2,\qquad
D(s)=s^2-\frac{4((m+1)s-1)}{m(m+2)}.
\]
The discriminant is positive for \(s\ge1\). Writing
\[
a=\frac{2(m+1)}{m(m+2)},\qquad b=\frac2{m(m+2)},
\]
we have \(D(s)=(s-a)^2-b^2\). In particular,
\[
v'(s)=\frac12\left(1-\frac{s-a}{\sqrt{D(s)}}\right)<0,
\qquad
v''(s)=\frac{b^2}{2D(s)^{3/2}}>0.
\]
Thus the minimum-cost function \(m[ps+(q-p)v(s)]\) is convex on \([1,\infty)\), strictly convex when \(p<q\), and tends to infinity. For \(p=q\) it is \(mps\), minimized by \(s=1\). For \(p<q\), its unconstrained stationary point is
\[
s_*=\frac{2(m+1)+(p+q)/\sqrt{pq}}{m(m+2)}.
\]
It lies above one precisely when \(T>m^2-2\). Otherwise the minimum is attained at \(s=1\), where \(D(1)=(m-2)/(m+2)=\delta^2\), giving the first displayed allocation and cost. If \(T>m^2-2\), the stationary condition yields
\[
u=\frac{m+1+\sqrt{q/p}}{m(m+2)},\qquad
v=\frac{m+1+\sqrt{p/q}}{m(m+2)}.
\]
Substitution gives the second cost formula. Both allocations meet the feasibility inequalities with equality where claimed. Rescaling proves the unrestricted maximum.

**Multiplicity and equality cases.** If \(p<q\) and \(T\le H\), the minimizing orbit-constant solution has \(s=1\), \(uv=1/(m+2)\), and \(F(z)=(z-1)(z-m)\); eigenvalue one has multiplicity \(m\), counting the \(m-1\) leaf-difference modes. If \(T>H\), then \(s=s_*>1\) and \(\lambda_-=1<\min\{s,\lambda_+\}\), so the eigenspace is one-dimensional. The strict convexity above gives orbit-constant uniqueness for \(p<q\). If \(p=q\), all feasible allocations with \(s=1\) and \(uv\ge1/(m+2)\) attain the same cost; this establishes the stated symmetric nonuniqueness.

## Verification

The accompanying `verify_two_hub_gap.py` uses Python's standard library only. It reconstructs complete weighted Laplacian characteristic polynomials by exact-rational Faddeev–LeVerrier calculations, independently compares them with the claimed factorization, tests the high-price optimality identities for exact rational prices and weights, tests the low-price discriminant and endpoint identities, and performs independent dense ratio sweeps for a range of dimensions and price contrasts. Execute it using `python3 verify_two_hub_gap.py`. The replay reported 72,390 assertions or checks; these finite calculations are supplementary and are not a proof of the all-parameter theorem. The spectral decomposition and strict convexity argument above establish the infinite claim.

As a fully rational instance, take \(m=3\), \(p=1\), \(q=64\). The high-price branch gives unit-gap edge conductances \(u=4/5\), \(v=11/40\) and minimum unit-gap cost \(C_*=276/5\). The entire Laplacian spectrum is \(\{0,1,43/40,43/40,33/10\}\); scaling by \(5B/276\) gives the exact budget-\(B\) optimum.

## Relationship to prior work

Ghosh and Boyd (2006) establish convexity/symmetry reductions for algebraic-connectivity optimization and derive unpriced, fully symmetric graph-family bounds; these general techniques and the basic eigenvalue variational characterization are prior work, not claimed as new. Their symmetric block-arrow examples do not impose distinct conductance prices at the two hubs and do not give this exact two-regime \(K_{2,m}\) cost or the threshold \(T=m^2-2\). Shafi, Arcak, and El Ghaoui (2010) formulate convex edge- and node-weight Laplacian spectral optimization, including optional cost constraints, but do not derive this graph-specific two-class optimum or price threshold. Shakeri and coauthors (2015) analyze optimal interlayer coupling between connected network layers using a one-to-one interconnection and a uniform sum budget, a different graph family and resource model. The later broad multi-layer treatment likewise does not supply this price-dependent \(K_{2,m}\) formula in its inspected model and results. Other graph topologies, such as a priced star or a four-cycle, cannot imply the result for all \(m\ge3\), because the leaf-difference eigenspace and the hub quotient here have a different competing-mode structure.

The specific assessed contribution is the explicit priced \(K_{2,m}\) optimum, the sharp large price-ratio threshold, the positive optimal allocation, and its Fiedler multiplicity transition. The searches and comparisons described in the companion review are evidence of best-known noncoverage, not proof that no equivalent historical formulation exists.

## Limitations

Only the graph family \(K_{2,m}\), \(m\ge3\), and two hubwise uniform positive price classes are classified. The theorem concerns the maximum unnormalized Laplacian gap, not full discrete-time second-largest-eigenvalue-modulus mixing or resistance minimization. It identifies an unrestricted *optimal value* and one optimal orbit-constant allocation; it does not classify every possible asymmetric optimizer. The broader literature could contain an equivalent special case under a different formulation. Independent external mathematical validation has not been performed.

## References

1. A. Ghosh and S. Boyd, *Upper bounds on algebraic connectivity via convex optimization*, Linear Algebra and its Applications **418** (2006), 693–707. DOI: https://doi.org/10.1016/j.laa.2006.03.006. The accessible source reports availability online on 2006-05-05.
2. S. Yusef Shafi, M. Arcak, and L. El Ghaoui, *Designing Node and Edge Weights of a Graph to Meet Laplacian Eigenvalue Constraints*, Allerton Conference (2010). https://people.eecs.berkeley.edu/~elghaoui/Pubs/SAE_Allerton_2010.pdf. Sections III–V provide convex design frameworks and examples, not the two-price biclique formula.
3. H. Shakeri, N. Albin, F. Darabi Sahneh, P. Poggi-Corradini, and C. Scoglio, *Maximizing Algebraic Connectivity in Interconnected Networks*, arXiv:1510.06785, first version 2015-10-22. https://arxiv.org/abs/1510.06785.
4. *The art of interconnections: Achieving maximum algebraic connectivity in multilayer networks*, Network Science (2024), https://www.cambridge.org/core/journals/network-science/article/art-of-interconnections-achieving-maximum-algebraic-connectivity-in-multilayer-networks/67B428A634B2BF0741AFD0B350F8AB4E.
