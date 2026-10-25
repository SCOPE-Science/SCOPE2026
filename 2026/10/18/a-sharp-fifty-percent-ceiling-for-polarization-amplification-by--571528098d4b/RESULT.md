# A sharp fifty-percent ceiling for polarization amplification by one social tie

## Finding

**Theorem (sharp one-edge amplification).** Let \(n\ge3\), let \(G\) be any undirected network on \(n\) vertices with nonnegative finite symmetric edge weights, and let \(u\ne v\) be vertices not previously adjacent. In the equal-unit-anchoring Friedkin–Johnsen model, set \(z=(I+L)^{-1}s\), where \(L\) is the weighted graph Laplacian and \(s\in[-1,1]^n\) is a nonconstant innate-opinion vector. Define the total stationary polarization by \(P_G(s)=\sum_{i=1}^n(z_i-\bar s)^2\), with \(\bar s=n^{-1}\sum_i s_i\). Add a unit-strength edge between \(u\) and \(v\), obtaining \(G^+\). Then

\[
 P_{G^+}(s)<\frac32 P_G(s).
\]

The constant \(3/2\) cannot be reduced uniformly over weighted networks and innate opinions, even if the network has only twelve vertices: two disjoint six-vertex complete communities, with every internal weight tending to infinity, have attainable amplification ratios tending to \(3/2\). In particular, adding one social tie can never increase this equilibrium variance by \(50\%\) or more, although it can increase it.

For a fixed network and prospective edge, the **exact** largest ratio over all nonconstant innate opinions equals

\[
\lambda_+(r,\tau)=\frac{1+r+\tau+\sqrt{(1+r+\tau)^2-(1+r)^2}}{(1+r)^2},\quad
r=b^{\mathsf T}(I+L)^{-1}b,\quad \tau=b^{\mathsf T}(I+L)^{-2}b,
\]

where \(b=e_u-e_v\). The corresponding least squared singular value is the same expression with a minus sign before the radical. Both are on the mean-zero opinion subspace. Thus the bound is an explicit sharp, all-network robustness law, not merely a particular adverse example.

## Assumptions and scope

Vertices may be disconnected; zero weights are equivalent to absent edges. All existing weights are finite and nonnegative, and the added edge has weight exactly one. Self-loops do not affect the Laplacian. The opinion update has identical stubbornness coefficient one at each vertex; heterogeneous anchoring, directed influence and an edge weight other than one are not claimed. The total squared deviation and variance divided by \(n\) give the same ratios. The optimum over innate opinions is achieved for every fixed finite graph by an admissible mean-zero innate-opinion vector, after scaling into \([-1,1]^n\).

## Proof

**1. Mean and edge update.** Put \(A=(I+L)^{-1}\) and \(b=e_u-e_v\). Symmetry and positive semidefiniteness of \(L\) give \(0\prec A\preceq I\), \(A\mathbf1=\mathbf1\), and \(b^{\mathsf T}\mathbf1=0\). Consequently \(\bar z=\bar s\) and the mean-zero vector \(y=z-\bar s\mathbf1\) has \(\|y\|_2^2=P_G(s)\). The added edge has Laplacian \(bb^{\mathsf T}\). The Sherman–Morrison identity, with \(v=Ab\) and \(r=b^{\mathsf T}v>0\), implies

\[
 y^+=\left(I-\frac{v b^{\mathsf T}}{1+r}\right)y=:Ty.
\]

The map \(s\mapsto y\) is bijective on the mean-zero subspace; maximizing over nonzero mean-zero \(y\) and rescaling \(s=(I+L)y\) to the permitted opinion interval does not alter the squared-norm ratio.

**2. Exact two-dimensional singular spectrum.** Set \(\tau=\|v\|_2^2=b^{\mathsf T}A^2b\). On the mean-zero subspace, \(T\) acts identically on the orthogonal complement of \(\operatorname{span}\{b,v\}\); this exceptional subspace has dimension at most two. The trace of \(T^{\mathsf T}T\) within that two-dimensional block is

\[
 \lambda_++\lambda_- =\frac{2(1+r+\tau)}{(1+r)^2},
\]

and the determinant is \(\lambda_+\lambda_-=(1+r)^{-2}\), by the matrix determinant lemma. If \(b\) and \(v\) are dependent, one of these two formal block eigenvalues is \(1\); the same quadratic still describes all nontrivial singular behavior. Solving gives the stated \(\lambda_\pm\). Because \(n\ge3\), a nonzero mean-zero \(y\perp b\) satisfies \(Ty=y\), so \(\lambda_+\ge1\). In addition \(Tv=v/(1+r)\), whence \(0<\lambda_-\le(1+r)^{-2}<1\).

**3. The universal sharp bound.** Since \(0\prec A\preceq I\), one has \(0<\tau\le r\). The characteristic polynomial \(q(\lambda)=(\lambda-\lambda_+)(\lambda-\lambda_-)\) obeys the **exact nonnegative identity**

\[
 q(3/2)=\frac{(1-3r)^2/4+3(r-\tau)}{(1+r)^2}\ge0.
\]

As \(\lambda_-<1<3/2\), the sign of \(q(3/2)\) forces \(\lambda_+\le3/2\). Equality would require simultaneously \(r=\tau=1/3\). But \(r=\tau\) means \(b\) is supported only on the eigenvalue-one subspace of \(A\), which equals \(\ker L\); hence \(Ab=b\) and \(r=b^{\mathsf T}b=2\), a contradiction. Thus strict inequality holds for every finite weighted graph.

**4. Constructive sharpness with twelve vertices.** Let \(G_w\) consist of two disconnected copies of \(K_6\) with each internal edge of weight \(w>0\); join one selected vertex from each community by a new edge of weight one. Write \(a=(1+6w)^{-1}\). On the constant subspace within each clique, \(A\) has eigenvalue one; on its five-dimensional zero-sum subspace, eigenvalue \(a\). Decomposing the endpoint difference vector across these eigenspaces gives

\[
 r_w=\frac{1+5a}{3},\qquad \tau_w=\frac{1+5a^2}{3}.
\]

As \(w\to\infty\), both converge to \(1/3\), and substituting them in the exact formula yields \(\lambda_+(r_w,\tau_w)\to3/2\). For each finite \(w\), take a nonzero mean-zero right singular vector \(y_w\) associated with \(\lambda_+\), and set \(s_w=\epsilon_w(I+L_w)y_w\), choosing \(\epsilon_w>0\) small enough that every coordinate lies in \([-1,1]\). The original equilibrium is \(\epsilon_w y_w\), and the ratio after adding the cross-community edge is exactly \(\lambda_+(r_w,\tau_w)\). Hence the universal coefficient is sharp without assuming an infinite graph, and the construction uses only twelve vertices.

**5. Explicit connected-graph increase.** For the unweighted path with vertices \(1-2-3-4\), choose \(y=(0,-1,-1,2)\). Then \((I+L)y=(1,-2,-4,5)\). Rescaling these innate opinions by \(1/5\) gives an admissible example. Adding edge \(\{1,3\}\) changes polarization from \(6/25\) to \(4941/(800\cdot25)\), an increase by the exact factor \(1647/1600>1\).

## Verification

The self-contained numerical/symbolic supplement `verify.py` requires Python 3 and SymPy and runs via `python verify.py`. It independently constructs rational graph Laplacians, inverts the original and changed equilibrium matrices, verifies the connected-path increase, checks the characteristic-polynomial certificate symbolically, and tests the two-clique resolvent moments by direct \(12\times12\) rational inversion at five weights. In the current execution it passed **881** symbolic, exact rational, and finite-graph checks. The proof of the universal statement and asymptotic sharpness is analytic; finite computations alone would not establish either.

## Relationship to prior work

Musco, Musco and Tsourakakis [1] use exactly the mean-centered squared equilibrium opinion deviation, generally alongside a disagreement statistic. Bhalla, Lechowicz and Musco [2] derive rank-one edge-update identities and study local edge dynamics, with theoretical focus on polarization plus disagreement rather than the sharp worst-case *polarization-only* relative increase. Rácz and Rigobon [3, Lemma 3.3] already derive the exact change in polarization caused by an edge, and explicitly show that inserting an edge can increase it. Their Theorem 3.7 provides conditional, derivative-based bounds, not the stated all-network, exact \(3/2\) operator-norm ceiling and fixed-size extremal sequence. The present claim is **only** that sharp universal multiplicative bound with its sharpness and singular-spectrum formula, not the already-known rank-one identity or nonmonotonicity.

## Limitations

The bound is for adding **one edge of weight exactly one** in the **undirected, equal-unit-anchoring** equilibrium model; it is not a claim about arbitrary edge weights, multiple simultaneous changes, directed influence, nonlinear dynamics, or polarization metrics based on bimodality rather than variance. The sharpness family uses weighted, disconnected initial communities and opinions chosen for the worst case; it does not show that the same constant is sharp on simple unweighted connected networks or for random innate opinions. Exact matching of equivalent results in all literature cannot be certified by finite searches; publication priority merits independent examination. The review is self-review only, not independently audited.

## References

[1] C. Musco, C. Musco and C. Tsourakakis, *Minimizing Polarization and Disagreement in Social Networks*, first public preprint December 28, 2017, arXiv:1712.09948, https://arxiv.org/abs/1712.09948.

[2] N. Bhalla, A. Lechowicz and C. Musco, *Local Edge Dynamics and Opinion Polarization*, first public preprint November 28, 2021, arXiv:2111.14020, https://arxiv.org/abs/2111.14020.

[3] M. Z. Rácz and D. E. Rigobon, *Towards Consensus: Reducing Polarization by Perturbing Social Networks*, first public preprint June 17, 2022, arXiv:2206.08996, https://arxiv.org/abs/2206.08996.
