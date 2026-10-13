# Sharp price-distance threshold for a reweighted cycle with one optional chord

## Finding

Let \(n\ge4\) and \(2\le d\le\lfloor n/2\rfloor\) be integers, and let \(t>0\). On the cycle with vertices \(0,1,\ldots,n-1\), let \(w_i\ge0\) be the conductance of edge \(\{i,i+1\pmod n\}\); a potential extra chord \(\{0,d\}\) has conductance \(z\ge0\). Allocate a total cost of one:
\[
\sum_{i=0}^{n-1}w_i+t z=1.
\]
Minimize the Kirchhoff index (total unordered-pair effective resistance), assigning value \(+\infty\) to disconnected networks. Define
\[
\Theta_{n,d}=\frac{d(n-d)\,[d(n-d)+2]}{n^2-1}.
\]
There is exactly one optimal conductance vector, and its chord conductance satisfies
\[
z^*=0\quad\Longleftrightarrow\quad t\ge\Theta_{n,d}.
\]
When \(t\ge\Theta_{n,d}\), the unique optimizer is \(z^*=0\), \(w_i^*=1/n\) for every \(i\); when \(0<t<\Theta_{n,d}\), its chord conductance is strictly positive. The boundary \(t=\Theta_{n,d}\) belongs to the chord-free phase, including the equality case. No closed formula for the positive optimal chord conductance is claimed.

The threshold increases strictly with the chord distance \(d\) throughout the indicated range. For a fixed integer \(d\ge2\) and \(n\to\infty\), it tends to \(d^2\); if \(d/n\to\alpha\in(0,1/2]\), then
\[
\lim_{n\to\infty}\frac{\Theta_{n,d}}{n^2}=\alpha^2(1-\alpha)^2.
\]
These are different economic scales for local and macroscopic shortcuts.

## Assumptions and scope

The graph is undirected, finite and simple, with the indicated fixed ring and one candidate non-ring chord. Every edge is assigned a nonnegative *conductance*, not a resistance. All ring conductances have unit linear price, the chord has constant price \(t\), and the entire unit budget is allocated. For connected graphs the Laplacian is
\[
L=\sum_{i=0}^{n-1}w_i(e_i-e_{i+1})(e_i-e_{i+1})^{\mathsf T}
+z(e_0-e_d)(e_0-e_d)^{\mathsf T},
\]
where indices on ring vertices are taken modulo \(n\). With \(L^+\) its Moore--Penrose inverse, the Kirchhoff index is \(K(L)=n\operatorname{tr}L^+\). The convention \(K=+\infty\) for disconnected networks prevents interpreting a disconnected pseudoinverse as a finite resistance network. The theorem optimizes all ring weights jointly with the optional chord; it does not assume that the ring remains uniform after a chord is installed.

## Proof

**1. Strict convexity and a unique optimum.** Restrict \(L\) to the space orthogonal to the all-ones vector. For a connected network this restriction is positive definite and
\[
K(L)=n\operatorname{tr}\left[(L|_{\mathbf1^\perp})^{-1}\right].
\]
For any nonzero symmetric perturbation \(H\), the second directional derivative of \(\operatorname{tr}(X^{-1})\) at positive definite \(X\) is
\[
2\operatorname{tr}(X^{-1}HX^{-1}HX^{-1})
=2\|X^{-1/2}HX^{-1}\|_F^2>0.
\]
Because all ring edges and the chord are distinct edges of a simple graph, their weights uniquely determine the Laplacian by its off-diagonal entries. Hence \(K\) is strictly convex on the connected part of the feasible simplex. If a sequence of connected weights tends to a disconnected Laplacian, its second eigenvalue tends to zero and \(K\ge n/\lambda_2(L)\to+\infty\). The compact feasible simplex therefore has a connected, unique minimizer.

**2. Chord-free reference optimum.** On the face \(z=0\), strict convexity and rotational symmetry of the ring imply the unique optimum \(w_i=1/n\) for all \(i\). Let \(L_0\) denote the cycle Laplacian with all conductances equal to one. The reference Laplacian is \(L_0/n\), so its pseudoinverse is \(n L_0^+\).

**3. Exact squared-potential kernel.** For an edge incidence vector \(b\), matrix differentiation gives
\[
\frac{\partial K}{\partial w_b}=-n\,b^{\mathsf T}(L^+)^2b.
\]
Define \(D_n(d)=(e_d-e_0)^{\mathsf T}(L_0^+)^2(e_d-e_0)\). The real vector
\[
u_i=
\begin{cases}
\frac{(n-d)i}{n},&0\le i\le d,\\
\frac{d(n-i)}n,&d<i<n
\end{cases}
\]
satisfies \(L_0u=e_d-e_0\) by directly checking the discrete second differences, including both endpoints. Since \(L_0^+(e_d-e_0)=u-\overline u\mathbf1\), with \(\overline u=d(n-d)/(2n)\), finite square sums give
\[
D_n(d)=\sum_{i=0}^{n-1}(u_i-\overline u)^2
=\frac{d(n-d)\,[d(n-d)+2]}{12n}.
\]
The same formula at adjacent distance one yields
\[
D_n(1)=\frac{n^2-1}{12n}.
\]
In particular, at the uniform reference ring, an individual ring-edge derivative is \(-n^3D_n(1)\), and the new chord derivative is \(-n^3D_n(d)\). The extra factor \(n^2\) comes from the reference pseudoinverse scaling; the outer \(n\) is the Kirchhoff-index normalization.

**4. Global threshold from a supporting hyperplane.** For any feasible allocation \((w,z)\), the budget imposes
\[
\sum_{i=0}^{n-1}(w_i-1/n)=-tz.
\]
The objective's first-order supporting-plane expression at the uniform chord-free point is therefore
\[
\nabla K\cdot\big((w,z)-(1/n,\ldots,1/n,0)\big)
=n^3z\big[tD_n(1)-D_n(d)\big].
\]
When \(t\ge D_n(d)/D_n(1)\), this is nonnegative at every feasible allocation, and convexity proves the uniform chord-free point globally optimal. Strict convexity makes the optimum unique, including equality. When \(t<D_n(d)/D_n(1)\), take a small \(\varepsilon>0\), set \(z=\varepsilon\) and every ring weight to \((1-t\varepsilon)/n\). This remains feasible and connected, and its derivative of \(K\) at \(\varepsilon=0\) is strictly negative. Thus the chord-free optimum cannot be globally optimal, and the unique optimizer has \(z>0\). Substitution of the two exact kernel values gives the stated \(\Theta_{n,d}\).

**5. Geometry of the threshold.** On integers \(1\le d\le n/2\), the quantity \(d(n-d)\) increases strictly with \(d\); the map \(s\mapsto s(s+2)\) is increasing for positive \(s\). This proves strict distance monotonicity. Dividing the explicit formula by appropriate powers of \(n\) proves the two limits without any assumption about optimizer continuity.

## Verification

The accompanying standard-library Python program `verify.py` verifies the exact cycle-Poisson equation, centered-potential square-sum identity, and rational threshold over \(460\) integer size/distance cases. It also computes the *actual Kirchhoff-index objective* using exact rational matrix inversion on both sides of the critical price in \(32\) test cases. Running `python verify.py` returns `VERIFY_OK 460 exact cycle-Poisson/threshold identities; 32 exact objective-side comparisons`. The executable checks do not replace the strict-convexity and supporting-hyperplane proof for all sizes and real prices.

For example, \(n=8\) and \(d=3\) give \(\Theta_{8,3}=85/21\). The optimizer buys a chord at price \(t=4\) and excludes it at price \(t=5\); at price \(85/21\), it excludes the chord by strict convexity.

## Relationship to prior work

Ghosh, Boyd and Saberi (2008) established convexity, uniqueness, gradient optimality conditions and analytic weight allocations for general fixed edge sets, including uniform optima on edge-transitive graphs. The present result uses that framework, but supplies a closed, exact chord-price and distance classification for the cycle under a *shared* budget and full reoptimization of the original edges. Deng, Chang and Yang (2026) gave exact Kirchhoff-index improvement formulas for adding a chord to a *fixed-weight* cycle and described antipodal optimality under a separate chord budget; these results do not optimize the cycle weights jointly with the chord under a common weighted price budget. Bhoite and collaborators (2026) optimized candidate-edge weights on a fixed weighted base graph under heterogeneous costs; their base-edge weights are held fixed. None of these inspected statements gives the all-size, distance-resolved omission threshold stated here. General covariance/gradient formulas are acknowledged rather than claimed as original.

## Limitations

The theorem characterizes whether the unique optimum uses the chord; it does not express the positive optimum conductances in closed form or handle multiple simultaneous optional chords. The cost model is linear and deterministic. Although the examined primary literature does not explicitly state this exact threshold, equivalent formulas or a corollary in older electrical-network optimization literature cannot be definitively excluded. A generic convex optimality theorem alone is not being represented as new.

## References

1. A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37--66; DOI: 10.1137/050645452. Full text: https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf . Published electronically February 1, 2008; a shorter conference version appeared in July 2006 (exact first-public day not established here).
2. J. Deng, L. Chang and Q. Yang, *Single-Chord Augmentation of Weighted Cycles for Algebraic Connectivity and Network Coherence*, arXiv:2605.24479 (first posted May 23, 2026). https://arxiv.org/pdf/2605.24479 .
3. O. Bhoite, V. S. Dhuli, S. Werner and K. Kansanen, *Budget-Constrained Graph Augmentation for Robust Network Design via Kirchhoff Index Minimization*, arXiv:2609.29790 (first posted September 24, 2026). https://arxiv.org/pdf/2609.29790 .
