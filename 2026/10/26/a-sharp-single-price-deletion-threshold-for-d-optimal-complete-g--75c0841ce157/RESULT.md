# A sharp single-price deletion threshold for D-optimal complete-graph conductances

## Finding

**Theorem.** Fix an integer \(n\ge4\), a budget \(B>0\), and a relative price \(r>0\). On the complete graph \(K_n\), all edge conductances \(w_e\ge0\) are independently adjustable. The edge \(\{1,2\}\) costs \(r\) per unit conductance; every other edge costs one. Under
\[
rw_{12}+\sum_{e\ne\{1,2\}}w_e\le B,
\]
maximize the weighted spanning-tree enumerator \(\tau(w)\), equivalently any grounded Laplacian determinant.

The maximizer is **unique** and has three edge classes: \(a=w_{12}\); \(b=w_{1j}=w_{2j}\) for \(3\le j\le n\); and \(c=w_{ij}\) for \(3\le i<j\le n\). Set
\[
r_c=\frac{n-1}{n-2},\qquad H=n-1-\frac{n-2}{2}r.
\]
For \(0<r<r_c\), every edge is active and the unique optimum is
\[
\boxed{a=\frac{B}{n-1}\left(\frac1r-\frac{n-2}{2H}\right),\quad
b=\frac{B}{(n-1)H},\quad
c=\frac{2B(H-1)}{(n-1)(n-2)H}.}
\]
For \(r\ge r_c\), exactly the distinguished edge is deleted:
\[
\boxed{a=0,\quad b=\frac{2B}{(n-1)^2},\quad
c=\frac{2B(n-3)}{(n-1)^2(n-2)}.}
\]
Every edge other than \(\{1,2\}\) has strictly positive optimal conductance. The exact maximum is
\[
\boxed{\tau_*=\left(\frac{2B}{n-1}\right)^{n-1}
\begin{cases}
\dfrac{1}{2rH},&0<r<r_c,\\[3pt]
\dfrac{n-2}{(n-1)^2},&r\ge r_c.
\end{cases}}
\]
In particular, the threshold tends to one from above as \(n\to\infty\): a distinguished edge needs only a relative price \(1+1/(n-2)\) to become entirely unused in an optimal information design.

## Assumptions and scope

The graph is finite, undirected, simple, and complete. A conductance may be zero; a feasible design is accepted as informative only if its positively weighted support is connected, because otherwise \(\tau=0\). There are no upper bounds on individual conductances, no integrality constraint on the number of observations, and no lower bounds forcing every edge to be retained. All other edges have identical prices, and there is exactly one exceptional edge. The objective is the weighted **sum of spanning-tree products**, not the weight of a minimum spanning tree.

Define the Laplacian \(L(w)\) by \(L_{ij}=-w_{ij}\) for \(i\ne j\), and \(L_{ii}=\sum_{j\ne i}w_{ij}\). Let \(L^{(n)}(w)\) be the principal minor obtained by deleting row and column \(n\). The weighted matrix-tree theorem yields \(\tau(w)=\det L^{(n)}(w)\). Since every edge price is strictly positive, the feasible set is compact. A positive, connected feasible weight vector exists, so the optimum has \(\tau>0\).

## Proof

**Strict concavity and reduction by symmetry.** On positive-definite grounded Laplacians, \(\log\det\) is strictly concave in the matrix. On simple graphs, the map from individual edge weights to \(L^{(n)}\) is injective: off-diagonal entries determine weights between nongrounded vertices, and then the diagonal entries determine weights to the grounded vertex. Consequently, \(\log\tau\) is strictly concave on the set of connected weighted designs. There is a unique maximizer. Permutations exchanging vertices \(1,2\) and arbitrary permutations of vertices \(3,\ldots,n\) preserve the objective and prices. Uniqueness forces the asserted three conductance classes, without imposing symmetry as a restriction on competitors.

**The exact determinant.** For weights \((a,b,c)\), the Laplacian eigenvalue on the antisymmetric vector supported on vertices \(1,2\) is \(s=2a+(n-2)b\). The vector constant on \(\{1,2\}\) and separately constant on the remaining vertices has eigenvalue \(nb\). The subspace supported on the last \(n-2\) vertices, with zero sum, has eigenvalue \(t=2b+(n-2)c\), repeated \(n-3\) times. Along with the simple zero eigenvalue, these account for all \(n\) dimensions. By the matrix-tree theorem,
\[
\tau(a,b,c)=b\,[2a+(n-2)b]\,[2b+(n-2)c]^{n-3}=b s t^{n-3}.
\]
The budget becomes
\[
ra+2(n-2)b+\frac{(n-2)(n-3)}2c\le B.
\]

**Optimality conditions.** Because \(\tau\) is homogeneous of degree \(n-1\), the budget is active at every optimum; the Lagrange multiplier for maximizing \(\log\tau\) is \(\lambda=(n-1)/B\), by Euler's identity. For positive variables the stationarity equations are
\[
\frac2s=\lambda r,\qquad
\frac1b+\frac{n-2}s+\frac{2(n-3)}t=2(n-2)\lambda,\qquad
\frac{(n-2)(n-3)}t=\frac{(n-2)(n-3)}2\lambda.
\]
When \(a>0\), these give \(s=2/(\lambda r)\), \(t=2/\lambda\), and \(b=1/(\lambda H)\). Solving \(s=2a+(n-2)b\) and \(t=2b+(n-2)c\) yields precisely the first displayed triple. It is feasible and has \(a,b,c>0\) exactly when \(0<r<r_c\): in that interval \(H>(n-1)/2>1\), and \(a>0\) is equivalent to \(r<r_c\).

When \(a=0\), the stationarity equations for \(b,c>0\) imply \(t=2/\lambda\) and \(b=2/[\lambda(n-1)]\), giving the second displayed triple. The one-sided condition for \(a=0\) to be optimal is
\[
\left.\frac{\partial\log\tau}{\partial a}\right|_{a=0}
=\frac{2}{(n-2)b}=\lambda\frac{n-1}{n-2}\le\lambda r,
\]
which holds exactly for \(r\ge r_c\). Thus all stationarity and complementary-slackness inequalities hold throughout the claimed regimes. Since the objective is concave after taking logarithms, these conditions establish global optimality; strict concavity proves uniqueness, including exactly at the threshold.

**Value and boundary.** Substituting the first triple into \(b s t^{n-3}\) yields \((2B/(n-1))^{n-1}/(2rH)\); substituting the second yields \((2B/(n-1))^{n-1}(n-2)/(n-1)^2\). At \(r=r_c\), \(H=(n-1)/2\), so the two expressions meet continuously. These are exact identities for all specified real parameters, with no limiting or numerical step in the proof.

## Verification

The standalone runnable `verify.py` constructs actual grounded Laplacians and checks the proposed budgets, weighted matrix-tree determinant identities, and every individual-edge KKT equality or inequality with exact rational arithmetic. Its 42 rational cases cover graph orders \(4\) through \(9\), prices below, at, and above the threshold, and boundary cases with a deleted edge. It also compares unrestricted asymmetric feasible allocations and performs numerical full-dimensional constrained optimizations, using NumPy and SciPy. Run `python verify.py` with Python, SymPy, NumPy, and SciPy installed. The successful output is recorded in `verification_output.txt`.

These finite calculations are independent corroboration only; the global theorem is established by the spectral and concavity argument above.

## Relationship to prior work

Osting, Brune, and Osher (first public arXiv version dated 2012-07-26, arXiv:1207.6430) identify the D-optimal Laplacian information criterion with a product of nonzero eigenvalues and, via the matrix-tree theorem, with spanning-tree counts. Their paper develops a general ranking/scheduling setting and analyzes E-optimality; it does not state this complete-graph single-price conductance solution or its sharp deletion threshold.

Harman and Benková (2014, arXiv:1408.2698) develop general approximate D-optimal design with cost constraints, including an equivalence theorem and algorithms. Their general framework applies in principle after interpreting edges as regression vectors, but the inspected treatment contains no complete-graph exceptional-price classification or the present explicit formulas.

Ghosh and Boyd (2006) demonstrate symmetry reduction for certain Laplacian spectral optimizations, chiefly algebraic connectivity. Such a symmetry principle is used here as an ingredient; it alone does not supply the three-class determinant factorization, the price-dependent active set, or uniqueness for this objective. The ordinary weighted matrix-tree theorem is assumed as standard.

## Limitations

The statement treats one anomalously priced edge and a continuous conductance budget. It does not solve arbitrary heterogeneous prices, multiple anomalous edges, exact integer-valued experiment counts, or simultaneous count-and-cost constraints. The formulas do not apply to the objective of finding a single minimum spanning tree. The supporting search cannot exclude a pre-existing specialized statement in historical optimal-design literature; therefore mathematical originality remains subject to independent literature review.

## References

1. B. Osting, C. Brune, S. J. Osher, *Optimal Data Collection For Informative Rankings Expose Well-Connected Graphs*, arXiv:1207.6430 (first publicly posted 2012-07-26), especially Proposition 4.2, Equation (15c), and Remark 1. https://arxiv.org/abs/1207.6430
2. R. Harman and E. Benková, *Approximate D-optimal Experimental Design with Simultaneous Size and Cost Constraints*, arXiv:1408.2698 (first posted 2014-08-12), especially Sections 1–2 and 5.1. https://arxiv.org/abs/1408.2698
3. A. Ghosh and S. Boyd, *Upper Bounds on Algebraic Connectivity via Convex Optimization*, Linear Algebra Appl. 418 (2006), 693–707. https://stanford.edu/~boyd/papers/eigbounds_laplacian.html
