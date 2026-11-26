# Sharp bridge-activation threshold for dual numerical-radius functionals on double stars

## Finding

Let \(D_{p,q}\) have two adjacent hubs with \(p\) and \(q\) pendant leaves respectively, where \(p,q\ge1\) are integers. Orient edges away from any chosen root and let \(S_a e_u=\sum_{u\to v}a_{uv} e_v\), with freely variable complex edge weights. Put \(N(a)=w(S_a)\), where \(w(T)=\sup_{\|h\|_2=1}|\langle Th,h\rangle|\). For \(\beta\ge0\), define \(L_\beta(a)=\sum_{e\text{ pendant}}a_e+\beta a_{e_0}\), where \(e_0\) joins the hubs. Then
\[
\sup_{N(a)\le1}|L_\beta(a)|=
\begin{cases}
2(\sqrt p+\sqrt q), & 0\le\beta\le(pq)^{1/4},\\
2\sqrt{p+q+\beta^2+pq/\beta^2},&\beta>(pq)^{1/4}.
\end{cases}
\]
The supremum is attained. In every maximizer the **modulus** of the bridge coefficient vanishes through the critical value, including equality, and is strictly positive above it. With the phase convention \(L_\beta(a)>0\) real, all nonzero coefficients are positive real, so the active bridge coefficient is strictly positive in that convention. Arbitrary common complex phases are allowed when maximizing the absolute value.

## Assumptions and scope

The field is complex and the norm of a functional is the supremum of its absolute value on the full closed unit ball. There is no stipulated positivity or symmetry on the admissible weights. The norm and value are independent of the root. Pendant weights are summed once each and the bridge has independent multiplier \(\beta\).

## Proof

**Norm reduction.** The unique paths of a rooted tree allow a diagonal unitary change of phases taking the shift weights to their moduli. Also the depth grading makes \(e^{i\theta}S_a\) unitarily similar to \(S_a\). Taking the top eigenvalue of \(\operatorname{Re}(e^{i\theta}S_a)\) and optimizing in \(\theta\) thus gives
\[
N(a)=\tfrac12\rho(A_{|a|}),
\]
where \(A_{|a|}\) is the undirected weighted adjacency matrix. Its top eigenvalue equals its spectral radius by nonnegativity. In particular the norm is absolute and is invariant under the graph automorphisms that permute leaves within each hub's orbit. No invariance under arbitrary permutations of edges is needed.

Triangle inequality gives \(|L_\beta(a)|\le L_\beta(|a|)\), and \(|a|\) remains feasible. Averaging \(|a|\) over the independent pendant permutations preserves feasibility by convexity and preserves the nonnegative objective and the bridge modulus. Thus it suffices to optimize over nonnegative weights \(x,y\) on the two pendant orbits and \(c\) on the bridge; for any complex maximizer, the averaged vector is itself optimal and has \(c=|a_{e_0}|\).

**Feasible region.** The leaf-difference subspaces vanish under the symmetric weighted adjacency. On the two normalized leaf sums and two hubs it restricts to the weighted four-vertex path with consecutive weights \(u=\sqrt p\,x,c,v=\sqrt q\,y\). Its bipartite off-diagonal block is \(M=\left(\begin{smallmatrix}u&0\\c&v\end{smallmatrix}\right)\), so \(N(a)\le1\) is equivalent to \(\|M\|_{2\to2}\le2\). Testing \(4I-M^{\mathsf T}M\) for positive semidefiniteness gives
\[
0\le u,v\le2,\qquad 4c^2\le(4-u^2)(4-v^2).
\]
Indeed the determinant is \((4-u^2)(4-v^2)-4c^2\); these conditions imply \(u^2+c^2\le4\) as well. They include the cases \(u=2\) or \(v=2\), with \(c=0\).

**Optimization and activation.** Write \(u=2\cos\theta,v=2\cos\phi\), for angles in \([0,\pi/2]\). The largest allowed \(c\) is \(2\sin\theta\sin\phi\), and taking this value never decreases the objective. Maximizing the objective over \(\phi\) by Cauchy–Schwarz gives
\[
2\left(\sqrt p\cos\theta+\sqrt{q+\beta^2\sin^2\theta}\right)=2F(z),\qquad
F(z)=\sqrt{p(1-z)}+\sqrt{q+\beta^2 z},\quad z=\sin^2\theta.
\]
The optimizing \(\phi\) is unique, with \((\cos\phi,\sin\phi)=(\sqrt q,\beta\sqrt z)/\sqrt{q+\beta^2z}\). The function \(F\) is strictly concave and \(2F'(0)=\beta^2/\sqrt q-\sqrt p\). If \(\beta^2\le\sqrt{pq}\) the only maximizing \(z\) is zero, so \(u=v=2\) and feasibility forces \(c=0\), even at \(\beta=0\) where the objective ignores \(c\). If \(\beta^2>\sqrt{pq}\), the derivative tends to \(-\infty\) at 1 and the unique maximizer is
\[
z_* = \frac{\beta^4-pq}{\beta^2(\beta^2+p)}\in(0,1),\qquad
F(z_*)=\frac{\sqrt{(\beta^2+p)(\beta^2+q)}}{\beta}.
\]
The equality follows from \(\beta^4(1-z_*)=p(q+\beta^2z_*)\). Both optimizing sines are then positive and, as \(\beta>0\), any maximizer must take the largest allowed \(c\). These choices furnish feasible witnesses, prove both formulas, and give the asserted strict positivity of the optimized bridge modulus after averaging. Equality in the original triangle inequality requires all nonzero terms contributing to \(L_\beta\) to lie on the same complex ray. If \(\beta=0\) the bridge is already known to be zero, so in every case this condition applies to all nonzero coefficients. It proves the statement about phase normalization.

## Verification

At \(p=q=1,\beta=2\) the pendant weights \(1,1\) and bridge \(3/2\) yield \(N(a)=1\) by the determinant criterion and objective \(5\), as predicted. Multiplying all three weights by \(-1\) keeps the norm and absolute objective unchanged, illustrating why the unnormalized bridge need not be positive real. At \(p=q=1,\beta=1\), the threshold witness has pendant weights \(2,2\) and bridge zero. Independently, the support calculation in the two-by-two reduction can be checked by minimizing the nuclear norm of \(\left(\begin{smallmatrix}\sqrt p&t\\\beta&\sqrt q\end{smallmatrix}\right)\) over real \(t\), using operator/nuclear norm duality on a subspace. Its squared nuclear norm is \(p+q+\beta^2+t^2+2|\sqrt{pq}-\beta t|\), minimized at \(t=\beta\) on the plateau and \(t=\sqrt{pq}/\beta\) above it. In this check one can optimize over all real lower-triangular matrices since entrywise moduli preserve their operator norm by diagonal sign changes. The supplied `verify_double_star.py` is a finite numerical diagnostic for the unchanged real nonnegative optimization, not a check of the complex equality case or a proof of the all-parameter formula.

## Relationship to prior work and limitations

Budzynski, Dymek, Planeta and Ptak, *Weighted shifts on directed trees. Their multiplier algebras, reflexivity and decompositions* (arXiv:1702.00765), develop the directed-tree shift framework. Sharif, *On the numerical radius of weighted shifts on \(\ell^2\) as a norm on \(\ell^\infty\) and connections to Banach limits* (arXiv:2303.00876), studies the numerical-radius norm of unilateral path shifts. The graph-edge numerical-radius study *Strict convexity and the full smooth locus of graph-edge numerical-radius norms* (record `12716bf88722`) supplies the general primal adjacency norm and its Rayleigh representation. Its convexity and smoothness classification does not give the double-star dual support value; here the independent bridge multiplier is varied and its transition determined. The uniform three-edge path case \(p=q=\beta=1\) is not claimed anew. An equivalent closed formula under different support-function terminology cannot be ruled out by the comparisons made here. The result does not compute arbitrary edge-functional norms on other trees or classify all their maximizers.
