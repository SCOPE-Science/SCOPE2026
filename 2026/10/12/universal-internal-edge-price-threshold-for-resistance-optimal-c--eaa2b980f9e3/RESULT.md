# Universal internal-edge price threshold for resistance-optimal clique bouquets

## Finding

Let \(m\ge2\), let \(q_1,\ldots,q_m\ge2\) be integers, and put \(N=1+\sum_{i=1}^m q_i\). Form a connected graph from disjoint sets of \(q_i\) peripheral vertices by making each set a clique and joining every peripheral vertex to a single common hub. There are no edges between different peripheral sets. For each block \(i\), each hub--peripheral edge costs \(c_i>0\) per unit conductance and each internal clique edge costs \(d_i>0\) per unit conductance. Allocate nonnegative conductances with total cost one, minimizing the Kirchhoff index \(K=\sum_{u<v}R_{uv}\) of unordered-pair effective resistances, with disconnected allocations assigned infinite objective.

**Theorem.** There is exactly one global optimal allocation. It has a common spoke conductance \(a_i>0\) within each block and a common internal-edge conductance \(b_i\ge0\) within each block. Remarkably, the internal edges of block \(i\) are retained exactly when
\[
\boxed{\frac{d_i}{c_i}<\frac{2N}{N-1}}.
\]
For fixed total vertex count \(N\), the threshold is independent of how the peripheral vertices are partitioned into blocks, and it is independent of every block's other edge prices. Changing the total \(N\) changes the numerical threshold.

Here is a closed formula for all the optimal conductances and the optimal objective. For each block define
\[
 t_i=\frac{d_i}{c_i},\qquad
 \beta_i=\frac{(q_i-1)t_i}{2q_i},\qquad
 A_i=N-q_i,\qquad B_i=N(q_i-1).
\]
Define the local shape parameter and the local cost coefficient by
\[
(y_i,C_i)=
\begin{cases}
\left(\sqrt{\dfrac{B_i(1-\beta_i)}{A_i\beta_i}},\;
 q_ic_i\left[\sqrt{A_i(1-\beta_i)}+\sqrt{B_i\beta_i}\right]^2\right),
  & t_i<2N/(N-1),\\
\left(1,\;q_i^2c_i(N-1)\right),&t_i\ge2N/(N-1).
\end{cases}
\]
All square roots appearing in the first case have positive arguments. Put \(S=\sum_{j=1}^m\sqrt{C_j}\), \(p_i=\sqrt{C_i}/S\), and \(x_i=(y_i-1)/q_i\). The unique optimal allocation and objective are
\[
\boxed{
 a_i=\frac{p_i}{q_ic_i\left[1+\frac12(q_i-1)t_ix_i\right]},\qquad
 b_i=x_ia_i,\qquad
 K_{\min}=S^2.}
\]
The fraction \(p_i\) is the optimal *total cost* spent within block \(i\). At equality in the price threshold, \(y_i=1\), so internal edges are deleted.

A concrete heterogeneous instance has \((q_1,q_2)=(2,3)\), \(N=6\), unit spoke prices, and internal-edge prices \((12/11,4)\). Since the common deletion threshold is \(12/5\), the unique optimum satisfies \(b_1/a_1=1/2\) and \(b_2=0\), with
\[
K_{\min}=\left(\frac{14}{\sqrt{11}}+3\sqrt5\right)^2.
\]

## Assumptions and scope

All assertions hold for every integer \(m\ge2\), every integer \(q_i\ge2\), and all strictly positive real \(c_i,d_i\). The budget is exactly one; for a different positive budget \(B\), all optimal conductances scale by \(B\) and the optimum resistance scales by \(1/B\). The graph is simple and undirected, and conductance equals the reciprocal of resistance. The Kirchhoff index counts each unordered vertex pair once. No stochastic or normalized-Laplacian convention is used. The edge-price assumption requires that the two types of edges inside a given peripheral block share their respective prices, but different blocks may have completely different prices and sizes.

The theorem asserts uniqueness over **all individual edge allocations**, not just over symmetric allocations. At the optimum all spokes are strictly positive; internal edges can be exactly zero. Nothing is asserted about arbitrary non-clique blocks, unequal prices assigned to two edges of the same type within one block, or additional links between blocks.

## Proof

### 1. Existence, strict convexity, and within-block symmetry

For a connected weighted graph on \(N\) vertices, let \(L(g)\) be its conductance Laplacian and let \(J=\mathbf 1\mathbf 1^{\mathsf T}\). Its Kirchhoff index is
\[
K(g)=N\operatorname{tr}\left(L(g)+J/N\right)^{-1}-N.
\]
Every feasible edge vector is in a compact positive-price simplex. The objective tends to infinity if any cut loses all conductance, so a connected optimum exists. On the set where \(X(g)=L(g)+J/N\) is positive definite, consider any nonzero edge-allocation direction \(h\). Write \(H=\sum_e h_e(e_u-e_v)(e_u-e_v)^{\mathsf T}\). Then
\[
\frac{d^2}{ds^2}K(g+sh)=2N\operatorname{tr}(X^{-1}HX^{-1}HX^{-1})>0.
\]
Indeed, with \(Z=X^{-1/2}HX^{-1/2}\), the trace is \(\operatorname{tr}(Z^2X^{-1})\), positive unless \(H=0\). For a simple graph, the off-diagonal entry at each edge uniquely recovers \(-h_e\), so \(H=0\) forces \(h=0\). The Kirchhoff-index objective is therefore strictly convex across any two distinct connected feasible allocations, including allocations on a boundary face. Hence its optimum is unique.

The permutations of peripheral vertices separately within each clique preserve the graph, the prices, the budget, and the objective. Uniqueness forces the optimizer to have common values \(a_i\) on the \(q_i\) spokes of each block and \(b_i\) on the \(\binom{q_i}{2}\) internal edges of that block. If \(a_i=0\), the entire block is cut off from the hub, which is infeasible at any finite optimum. Thus \(a_i>0\).

### 2. Exact Kirchhoff-index decomposition through the hub

Fix one block with \(q\) peripheral vertices and common conductances \(a>0\) (spokes) and \(b\ge0\) (internal edges). In the corresponding \(q+1\) vertex weighted complete graph, the Laplacian has eigenvalue \(a+qb\) on the \((q-1)\)-dimensional leaf-contrast subspace and eigenvalue \((q+1)a\) on the hub-versus-leaf-uniform direction. Projection of the terminal current vector gives
\[
R(h,u)=\frac{1}{qa}+\frac{q-1}{q(a+qb)},
\qquad
R(u,v)=\frac{2}{a+qb}
\]
for a peripheral vertex \(u\), the common hub \(h\), and distinct peripheral vertices \(u,v\) of the same block.

The entire graph is a one-vertex union of these blocks. An electrical current between two vertices in the same block does not flow through any other block (which touches the rest only at the hub). A current between vertices in different blocks passes through the hub, so their effective resistance is the sum of their individual resistances to the hub. These statements follow as well by restricting the Dirichlet principle to each block.

Consequently, each block contributes its hub-resistance term to exactly \(q(N-q)\) unordered pairs, counting pairs crossing blocks via their appropriate summands, while it contributes its peripheral-to-peripheral resistance to \(\binom q2\) pairs. This yields the exact global decomposition
\[
\boxed{K(g)=\sum_{i=1}^m K_i(a_i,b_i),\qquad
K_i(a,b)=\frac{N-q_i}{a}+\frac{N(q_i-1)}{a+q_ib}.}
\]
This identity is also valid at \(b=0\).

### 3. Exact shape optimum within a block

For block \(i\), its budget expenditure is
\[
p_i=q_ic_ia_i+\frac{q_i(q_i-1)}2d_ib_i.
\]
Write \(x=b/a\ge0\), \(y=1+qx\ge1\), \(t=d/c>0\), \(\beta=(q-1)t/(2q)>0\), \(A=N-q>0\), and \(B=N(q-1)>0\). Eliminating \(a\) by the budget equation gives
\[
p_iK_i=q_ic_iF(y),\qquad
F(y)=(1-\beta+\beta y)\left(A+\frac{B}{y}\right),\quad y\ge1.
\]
An exact derivative calculation gives
\[
F'(y)=A\beta-\frac{B(1-\beta)}{y^2}.
\]
If \(0<\beta<B/(A+B)\), the unique minimizer on \(y\ge1\) is
\[
y_*=\sqrt{\frac{B(1-\beta)}{A\beta}}>1.
\]
For \(\beta\ge B/(A+B)\), \(F\) is strictly increasing on \(y>1\) (including the case \(\beta\ge1\)), so the unique minimizer is \(y_*=1\). Algebra shows
\[
\frac{B}{A+B}=\frac{N(q-1)}{q(N-1)},
\qquad
\beta<\frac{B}{A+B}
\iff \frac dc<\frac{2N}{N-1}.
\]
Here the factor \(q-1\) cancels. This proves the universal threshold. In the interior case, substitution gives the minimum
\[
F(y_*)=\left(\sqrt{A(1-\beta)}+\sqrt{B\beta}\right)^2.
\]
In the boundary case, it gives \(F(1)=A+B=q(N-1)\). Therefore the least possible contribution from this block, when its expenditure is fixed to \(p_i>0\), is exactly \(C_i/p_i\), with \(C_i\) and \(y_i\) as in the theorem. Both the minimizing shape and its positive spoke conductance are uniquely determined.

### 4. Global budget allocation and equality

For any connected feasible allocation, the blockwise lower bounds imply
\[
K=\sum_iK_i\ge\sum_i\frac{C_i}{p_i}
\ge\frac{\big(\sum_i\sqrt{C_i}\big)^2}{\sum_i p_i}
=\left(\sum_i\sqrt{C_i}\right)^2.
\]
The second inequality is Cauchy--Schwarz, and \(\sum_i p_i=1\). Equality occurs precisely when every block uses its unique locally optimal ratio \(x_i=(y_i-1)/q_i\), and the expenditures obey \(p_i=\sqrt{C_i}/S\). The formulas in the theorem then yield positive \(a_i\), nonnegative \(b_i\), and exact total cost one. They attain the lower bound. Strict convexity from step 1 excludes any non-symmetric competing optimum and establishes the stated global uniqueness.

For the example, \(N=6\) and the deletion threshold is \(12/5\). In block one, \(q=2\), \(t=12/11\), and \(\beta=3/11\), giving \(y=2\), \(x=1/2\), and \(C_1=196/11\). In block two, \(q=3\), \(t=4>12/5\), giving \(y=1\), \(b_2=0\), and \(C_2=45\). Therefore \(K_{\min}=(\sqrt{C_1}+\sqrt{C_2})^2=(14/\sqrt{11}+3\sqrt5)^2\).

## Verification

The accompanying `check_bouquet.py` is a Python 3 standard-library script. Run `python3 check_bouquet.py`. It separately computes exact rational grounded-Laplacian inverses on 217 finite weighted clique bouquets and compares their Kirchhoff indices to the one-vertex decomposition. It checks 700 arbitrary positive-cost instances against the closed-form conductance budget and the local first-order/boundary conditions, and compares their objective to 2,100 randomly selected feasible, not necessarily symmetric edge vectors using a separate floating-point matrix inversion routine. The numerical checks corroborate the algebra but **do not prove** the all-size, all-positive-price theorem. The proof above is analytic.

For a reproducible hand check of the price threshold, differentiate the displayed function \(F\) and evaluate \(F'(1)=A\beta-B(1-\beta)\); the sign becomes the sign of \(d/c-2N/(N-1)\). For a hand check of the global optimum, combine the displayed exact pair-resistance formulas with the equality case of Cauchy--Schwarz.

## Relationship to prior work

Ghosh, Boyd, and Saberi established convexity, uniqueness, optimality conditions, and numerical algorithms for minimizing total effective resistance on a fixed graph under a conductance budget; their analytical examples include trees, wheels, and barbells. These general tools establish the legitimacy of the optimization framework, not the present price-dependent all-block formula or its clique-size-independent rim-deletion threshold [1]. Kooij studied windmill graphs, their spectra, clustering and other structural measures, but did not optimize two classes of conductances with heterogeneous unit prices [2]. Sardar and Xu studied resistance distances and Kirchhoff indices of windmill graphs with unit-resistor substitutions; the accessible abstract describes a fixed-weight calculation rather than a priced conductance-allocation theorem [3]. We do not claim that the unweighted resistance formulas or general convexity principles are new.

The new claim is the exact unique global optimization across arbitrarily many differently sized and differently priced clique petals, in particular the same sharp local price ratio \(2N/(N-1)\) for every clique at fixed total \(N\), irrespective of its size within the partition and of prices elsewhere. While this formula can be derived from classical electrical-network tools, those tools alone do not state the classification without the blockwise optimization and equality analysis supplied here.

## Limitations

The theorem concerns a one-hub clique bouquet with exactly two uniform price classes within each petal; it makes no claim for additional cross-petal edges or individually heterogeneous edge prices inside a petal. The model optimizes an electrical Kirchhoff index, not the discrete-time Markov spectral gap or a network reliability probability. No independent mathematical audit has been performed. The full article of Sardar and Xu [3] was not available through the inspected lawful access paths; although its available abstract specifies unit resistors, an unlocated specialized antecedent remains an originality risk. Numerical stress tests are finite evidence only.

## References

[1] A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50(1), 37--66 (2008), DOI: 10.1137/050645452. Author-hosted full PDF: https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf. Published electronically 2008-02-01; a shorter conference version is recorded in July 2006 without a verified first-public calendar day.

[2] R. E. Kooij, *On generalized windmill graphs*, Linear Algebra and its Applications 565, 25--46 (2019), DOI: 10.1016/j.laa.2018.11.025. Full-text institutional copy: https://pure.tudelft.nl/ws/portalfiles/portal/102441316/1_s2.0_S0024379518305482_main.pdf.

[3] M. S. Sardar and S.-J. Xu, *Resistance Distance and Kirchhoff Index in Windmill Graphs*, Current Organic Synthesis 22(2), 159--168 (2025), published online 2024-07-04, DOI: 10.2174/0115701794299562240606054510. Publisher abstract: https://www.benthamscience.com/public/article/141453.
