# Unique optimal algebraic-connectivity design on non-tree bridge-barbells

## Finding
Let \(p,q\ge2\) be integers, \(N=p+q\), \(D=9pq-4N\), and \(B>0\). Take two hubs linked by one bridge, with respectively \(p-1\) and \(q-1\) peripheral vertices; each peripheral vertex is joined to its hub. Any additional edges *within* either peripheral class are allowed, but no other edges between the classes are. Let all allowed conductances be independently adjustable and nonnegative, subject to total conductance at most \(B\). For the weighted combinatorial Laplacian \(L\), maximize its algebraic connectivity \(\lambda_2(L)\).

**Theorem.** Whenever \(\max\{p,q\}\le2\min\{p,q\}\), the maximum is
\[
\lambda_2^*=\frac{BN}{D}.
\]
It has a **unique** optimizer: every peripheral-to-hub edge on the \(p\)-side has weight \(3qB/D\), every peripheral-to-hub edge on the \(q\)-side has weight \(3pB/D\), the unique bridge has weight \((3pq-N)B/D\), and **every optional within-class edge has zero weight**. This remains true when the two groups are internally complete graphs, so the designable graph has cycles. If \(\max\{p,q\}>2\min\{p,q\}\), the sharp bound \(BN/D\) is **not attained** and the optimal connectivity is strictly smaller; no formula for that latter optimum is claimed.

In particular, on a graph made from \(K_2\) and \(K_3\) joined by one bridge, the unique optimum for \(B=1\) has weights \(9/34\) on the small-side spoke, \(6/34\) on each large-side spoke, \(13/34\) on the bridge, and \(0\) on the remaining triangle edge. Its full Laplacian spectrum is \(\{0,5/34,3/17,9/17,39/34\}\), so its algebraic connectivity is **simple**. This explicitly contradicts the unqualified converse direction of Theorem 7 in Wan and collaborators (2008), which says that a simple-connectivity optimum can have a unique design only for a tree-shaped designable edge set.

## Assumptions and scope
The network has \(N\) labelled vertices. Let \(u\) be a hub with peripheral class \(U\) of size \(p-1\), and \(v\) a hub with peripheral class \(V\) of size \(q-1\). Designable edges are exactly \(uv\), every \(ux\) for \(x\in U\), every \(vy\) for \(y\in V\), and an arbitrary specified collection of edges internal to \(U\) or internal to \(V\). No parallel edges or edges from one peripheral class to the opposite hub are allowed. The budget is \(\sum_e w_e\le B\), with \(w_e\ge0\). The Laplacian uses the unnormalized convention \(x^\top Lx=\sum_{ij\in E}w_{ij}(x_i-x_j)^2\). This is an exact result about the *algebraic connectivity* objective, not total effective resistance or a stochastic-chain SLEM.

## Proof
**1. Universal eigenvector bound.** Put \(t_x=3/2\) for \(x\in U\), \(t_u=1/2\), \(t_v=-1/2\), and \(t_y=-3/2\) for \(y\in V\). Let \(z=t-(3(p-q)/(2N))\mathbf 1\), so \(z\perp\mathbf1\). Direct expansion gives
\[
 z_U=3q/N,\quad z_u=(2q-p)/N,\quad z_v=(q-2p)/N,\quad z_V=-3p/N,
 \qquad \|z\|^2=D/N.
\]
Each spoke and the bridge have squared \(z\)-difference \(1\), whereas each optional within-class edge has squared difference \(0\). Hence every feasible weighting satisfies
\[
 \lambda_2(L)\le\frac{z^\top Lz}{z^\top z}
 =\frac{N}{D}\sum_{\text{spokes and bridge}}w_e\le\frac{BN}{D}.
\]
The two inequalities are simultaneously equal only if the entire budget is spent on spoke/bridge edges and \(z\) itself is an eigenvector for eigenvalue \(BN/D\).

**2. Rigidity.** Write \(\lambda=BN/D\). The eigenvector equation at every left peripheral vertex \(x\in U\) forces \(w_{ux}(z_U-z_u)=\lambda z_U\), hence \(w_{ux}=3qB/D\). Similarly every right spoke is fixed at \(3pB/D\). The hub equation then forces the bridge weight to be \((3pq-N)B/D\). Every internal peripheral weight is forced to vanish by the equality case of the Rayleigh bound. Thus *any* optimum attaining the upper bound is exactly the claimed one; its budget identity follows from \(3q(p-1)+3p(q-1)+(3pq-N)=D\).

**3. Spectral sufficiency in the balanced interval.** At these weights, the vector \(z\) satisfies \(Lz=\lambda z\) at all vertices. The leaf-transverse invariant subspaces have respective eigenvalues \(a=3qB/D\) with multiplicity \(p-2\), and \(c=3pB/D\) with multiplicity \(q-2\). For \(p/2<q<2p\), both are greater than \(\lambda\). In the remaining four-dimensional constant-on-classes subspace, analyze \(L-\lambda I\): eliminating the two strictly positive leaf diagonal blocks gives the symmetric hub Schur complement
\[
 S=\begin{pmatrix}
 b-\lambda-(p-1)a\lambda/(a-\lambda)&-b\\
 -b&b-\lambda-(q-1)c\lambda/(c-\lambda)
 \end{pmatrix},\qquad b=(3pq-N)B/D.
\]
The hub entries of \(z\), \(((2q-p)/N,(q-2p)/N)\), have opposite nonzero signs, and constitute a null vector of \(S\). Since \(S\) has negative off-diagonal entry \(-b<0\), its diagonal entries are negative (use its null equation and the opposite signs), so its remaining eigenvalue is strictly negative. Inertia therefore gives exactly one negative eigenvalue of \(L-\lambda I\) in the four-dimensional quotient, together with one zero and two positive eigenvalues. The only Laplacian eigenvalue below \(\lambda\) is the constant mode at zero; hence \(\lambda_2=\lambda\), and it is simple.

At \(q=2p\), the right leaf-transverse block has eigenvalue exactly \(\lambda\). Eliminate only the strictly positive left leaf diagonal block in the four-dimensional quotient. Its remaining symmetric matrix (coordinates: left hub, right hub, normalized sum of right leaves) has form
\[
 \begin{pmatrix}0&-b&0\\-b&b+(q-2)\lambda&-\sqrt{q-1}\lambda\\0&-\sqrt{q-1}\lambda&0\end{pmatrix}.
\]
Its inertia is one positive, one negative and one zero; together with the eliminated positive direction and the transverse nonnegative blocks, \(L-\lambda I\) again has exactly one negative direction, corresponding to the constant Laplacian eigenvector. Therefore \(\lambda_2=\lambda\) at the endpoint too. The case \(p=2q\) follows by swapping the sides.

**4. Strictness beyond the interval.** Suppose \(q>2p\). The only possible weighting saturating the universal bound is the rigid candidate in step 2. Its right leaf-transverse eigenvalue is \(c=3pB/D<BN/D=\lambda\) and has positive multiplicity because \(q\ge5\). The candidate cannot attain the upper bound. The feasible conductance simplex is compact and algebraic connectivity is continuous, so its true maximum is strictly less than the bound. Interchange the sides for \(p>2q\).

**5. Explicit non-tree contradiction.** For \((p,q,B)=(2,3,1)\), the designable graph has one triangle and five vertices. The above unique optimum has the five eigenvalues displayed in the finding section, so the optimizing algebraic connectivity is simple. The graph nevertheless is not a tree. This refutes the stated tree-only uniqueness criterion without challenging its valid tree-direction or other structural results.

## Verification
The standalone standard-library script `verify.py` checks the budget, exact mean-zero norm, and the identity \(Lz=\lambda z\) using rational arithmetic, then checks full spectra numerically for every \(2\le p,q\le10\) (81 pairs), including strict inequality outside the threshold (24 pairs). It independently verifies the exact five-vertex optimum and its five rational eigenvalues numerically. Run `python verify.py` with Python 3; the 81 finite cases corroborate, but do **not** replace, the inertia argument or establish the theorem at infinitely many sizes.

## Relationship to prior work
Sun, Boyd, Xiao and Diaconis (2006) derive the variational/Semidefinite framework linking graph edge design to spectral connectivity; they do not supply the present non-tree uniqueness counterexample. Wan and coauthors (2008), Theorem 7, assert that when an optimal edge design has non-repeated algebraic connectivity, uniqueness occurs if and only if the designable graph is a tree. Their proof attempts to vary conductances on unused edges. Here the unique optimal Fiedler vector has squared difference zero across each unused cycle-closing edge, compared with squared difference one across all used edges. The sharp Rayleigh bound rules out such a perturbation at the same optimal value. The small double-star *tree* is a special case already studied in spectral optimization and is not claimed to be original; the contribution is the cyclic designable-graph counterexample, its global rigidity, and the sharp two-to-one family boundary. The related bridge-barbell zero-forcing result concerns a different invariant.

## Limitations
The theorem determines the exact optimum only within the two-to-one size ratio, and establishes a strict upper bound outside without classifying the optimum there. The uniqueness is for the specific allowed-edge architecture and unconstrained nonnegative conductances under one total budget, not for arbitrary additional cross edges, positive lower bounds on all conductances, or normalized-Laplacian objectives. The proof is analytical, but publication priority cannot be guaranteed; other specialized results may imply this classification. No independent validation has been performed.

## References
1. J. Sun, S. Boyd, L. Xiao and P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), DOI: 10.1137/S0036144504443821; electronic publication recorded 2006-11-02. https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf
2. Y. Wan et al., *On the Structure of Graph Edge Designs that Optimize the Algebraic Connectivity*, 47th IEEE CDC (2008), Theorem 7, DOI: 10.1109/CDC.2008.4738734. https://www.researchgate.net/publication/224367365_On_the_structure_of_graph_edge_designs_that_optimize_the_algebraic_connectivity
3. M. Fiedler, *Absolute algebraic connectivity of trees*, Linear and Multilinear Algebra 26 (1990), DOI: 10.1080/03081089008817967.
