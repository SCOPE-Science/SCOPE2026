# Dirichlet oscillations and universal residual slack in complete-bipartite Lipschitz polytopes

## Finding

Let \(p,q\ge2\), \(n=p+q\), and let \(A,B\) be disjoint coordinate sets of sizes \(p,q\). In the intrinsic Euclidean hyperplane \(H=\{x\in\mathbb R^n:\sum_i x_i=0\}\), consider the polar of the symmetric edge polytope of the complete bipartite graph:
\[
Q_{p,q}=\{x\in H:|x_a-x_b|\le1\ \text{for every }a\in A,b\in B\}.
\]
For a point \(x\), write \(R_A(x)=\max_{a\in A}x_a-\min_{a\in A}x_a\), \(R_B(x)=\max_{b\in B}x_b-\min_{b\in B}x_b\), and \(S(x)=2-R_A(x)-R_B(x)\). If \(X\) is uniformly distributed by intrinsic Euclidean volume on \(Q_{p,q}\), then
\[
\boxed{(R_A(X)/2,R_B(X)/2,S(X)/2)\sim\operatorname{Dirichlet}(p-1,q-1,2).}
\]
Consequently the unused cross-part oscillation budget has a distribution **independent of the bipartition at fixed total order**:
\[
S(X)/2\sim\operatorname{Beta}(2,n-2),\qquad
\mathbb P(S(X)\ge s)=(1-s/2)^{n-2}\bigl(1+(n-2)s/2\bigr),\quad 0\le s\le2.
\]
The exact intrinsic Euclidean volume is
\[
\boxed{\operatorname{vol}_{n-1}(Q_{p,q})=
\frac{2^{n-1}\sqrt n}{\binom np}.}
\]
This volume identity also holds for \(p,q\ge1\). Thus among complete bipartite graphs of fixed order the balanced bipartition minimizes polar volume, whereas the star bipartition maximizes it, with the usual symmetry under exchange of parts.

If \(p=p_n,q=q_n\to\infty\), \(p_n/n\to\alpha\in(0,1)\), and \(Z\sim N(0,\alpha(1-\alpha))\), \(G\sim\operatorname{Gamma}(2,1)\) are independent, then
\[
\boxed{\left(\sqrt n\left(\frac{R_A(X)}2-\frac{p-1}{n}\right),
\sqrt n\left(\frac{R_B(X)}2-\frac{q-1}{n}\right),nS(X)\right)
\ \Longrightarrow\ (Z,-Z,2G).}
\]
In particular the two macroscopic within-part oscillations exhibit perfectly anticorrelated Gaussian fluctuations, while their small remaining slack has a universal, asymptotically independent gamma law.

## Assumptions and scope

All polytopes use the **standard signed edge-root realization** with edge vectors \(\pm(e_a-e_b)\), unit edge thresholds, and Euclidean volume induced on \(H\); neither a different metric normalization nor a coordinate-lattice-normalized volume is intended. The random point is Lebesgue-uniform in dimension \(n-1\), not uniform over lattice points or vertices. For \(p,q\ge2\), both ranges are almost surely positive; boundary degeneracies have zero measure. The volume statement extends to singleton parts, but the three-parameter Dirichlet statement is asserted only for \(p,q\ge2\). The limit is taken along integer sequences with positive limiting part proportions and uses exact finite-dimensional centering.

## Proof

**1. Polar identification and slack nonnegativity.** The symmetric edge polytope of \(K_{p,q}\) is the convex hull of all \(\pm(e_a-e_b)\) with \(a\in A,b\in B\). Its polar inside \(H\) is precisely \(Q_{p,q}\). Write \(m_A,M_A,m_B,M_B\) for the extreme coordinates in the two parts. The defining inequalities amount to
\[
M_A-m_B\le1,\qquad M_B-m_A\le1.
\]
Adding them gives \(R_A+R_B\le2\), so \(S\ge0\). Thus all three normalized variables in the theorem are nonnegative and sum to one.

**2. Euclidean normalization.** Fix any \(a_0\in A\), impose the anchored gauge \(x_{a_0}=0\), and use the other \(n-1\) raw coordinate variables \(y\). Translating each anchored vector by its mean realizes an isomorphism to \(H\). Its Gram matrix is \(I_{n-1}-\frac1n\mathbf1\mathbf1^\mathsf T\), whose determinant is \(1/n\). Accordingly intrinsic volume equals anchored-coordinate volume divided by \(\sqrt n\), while uniform probabilities are unchanged by the constant Jacobian.

**3. An exact anchored range integral.** For a fixed anchored \(A\)-configuration \(a\) of span \(r=M_A-m_A\), the feasible \(B\)-coordinates independently fill
\[
[M_A-1,m_A+1]^q,
\]
a cube of side \(2-r\), present precisely when \(0\le r\le2\). The \((p-1)\)-dimensional anchored-coordinate measure of configurations with span at most \(r\) is \(p r^{p-1}\): partition by the position of the anchored coordinate among the ordered extremes, or condition on which extreme attains the maximal distance from zero. Its derivative is \(p(p-1)r^{p-2}\,dr\) for \(p\ge2\). Therefore the total anchored-coordinate volume is
\[
I_{p,q}=p(p-1)\int_0^2r^{p-2}(2-r)^q\,dr
=2^{n-1}\frac{p!q!}{(n-1)!}.
\]
The \(p=1\) case follows directly from the independent \(q\) intervals \([-1,1]\), giving \(I_{1,q}=2^q\), which agrees with the same factorial formula. Dividing \(I_{p,q}\) by \(\sqrt n\) gives the stated Euclidean volume; its alternative binomial form is an algebraic rearrangement.

**4. Conditional range law and Dirichlet factorization.** By the weighted integral, \(U=R_A/2\) has \(\operatorname{Beta}(p-1,q+1)\) distribution. Conditional on the anchored \(A\) coordinates, the \(q\) coordinates in \(B\) are independent uniform points of the same interval of length \(2-R_A\). The range of \(q\ge2\) iid unit uniforms has density \(q(q-1)v^{q-2}(1-v)\) on \(0<v<1\), so
\[
V=\frac{R_B}{2-R_A}\sim\operatorname{Beta}(q-1,2),
\]
independently of \(U\). The beta stick-breaking identity now yields
\[
(U,(1-U)V,(1-U)(1-V))
\sim\operatorname{Dirichlet}(p-1,q-1,2),
\]
which is exactly the first assertion. Equivalently, the joint density of unnormalized ranges is
\[
f_{R_A,R_B}(r,s)=\frac{(n-1)!}{2^{n-1}(p-2)!(q-2)!}
 r^{p-2}s^{q-2}(2-r-s),\quad r,s>0,\ r+s<2.
\]
Integrating the beta density for the third coordinate proves the explicit slack tail.

**5. High-dimensional behavior.** Represent the Dirichlet vector by independent gamma variables \(G_A\sim\Gamma(p-1,1)\), \(G_B\sim\Gamma(q-1,1)\), \(G_S\sim\Gamma(2,1)\), divided by their sum \(T_n\). These shapes add to \(n\). As \(p/n\to\alpha\in(0,1)\), the classical two-dimensional central limit theorem for the first two independent gamma sums, followed by the delta method, shows that the first two normalized coordinates fluctuate jointly as \((Z,-Z)\) with variance \(\alpha(1-\alpha)\). Meanwhile \(T_n/n\to1\) in probability and \(G_S\) is independent of both large gamma sums, giving \(nS=2nG_S/T_n\Rightarrow2G_S\) jointly and independently of the Gaussian component. Centering by \((p-1)/n\) and \((q-1)/n\) avoids any unstated rate assumption on convergence of \(p/n\).

**6. Sharp fixed-order extremizers.** At fixed \(n\), the volume formula is proportional to \(1/\binom np\). The binomial coefficients increase strictly from an endpoint to the central index (and are symmetric), proving the stated extremal bipartitions, with both central choices when \(n\) is odd.

## Verification

The accompanying standalone `checker.py` uses three independent finite diagnostics. First it computes Euclidean hull volumes from the original defining halfspaces, and checks the anchored Gram determinant, for eight small bipartitions. Second it enumerates integer lattice points in dilates of the anchored inequality system and recovers eight leading Ehrhart coefficients by exact integer finite differences; all equal the analytically calculated coordinate volumes. Third it draws rejection samples uniformly from an ambient anchored box subject to the original edge constraints and compares both empirical means and marginal empirical distribution functions to the predicted beta laws for four bipartitions. All checks passed. These are finite corroborations; the analytical arguments above prove the general theorem and the limit law.

## Relationship to prior work

D'Alì, Delucchi and Michałek establish symmetric-edge-polytope connections to Lipschitz and Kantorovich–Rubinstein polytopes, and analyze polar-dual integer-point counts for planar bipartite graphs. Higashitani, Jochemko and Michałek derive a detailed \(h^*\)-polynomial and facet theory for the **primal** complete-bipartite symmetric edge polytope. Gordon and Petrov investigate face structures of general finite-metric Lipschitz polytopes. The new statement here concerns **continuous uniform volume within the polar**, especially the joint Dirichlet law for two class oscillations and the bipartition-independent slack, rather than primal Ehrhart data or polar face counts. The exact volume formula is included because it normalizes this probability law; its presence alone is not offered as a claim that no equivalent volume expression existed previously.

## Limitations

No statement about arbitrary graphs, nonunit edge weights, changing metrics, or growing numbers of graph parts is asserted. The observed Dirichlet law relies on completeness of the bipartite graph, which makes the conditional feasible region an independent-coordinate cube. The joint limit requires both part sizes proportional to \(n\). The formula is mathematically derived here, but claims of novelty are limited by the checked literature: a differently named order-statistic or Lipschitz-body equivalent could exist. Independent external mathematical audit has not occurred.

## References

1. A. D'Alì, E. Delucchi and M. Michałek, *Many Faces of Symmetric Edge Polytopes*, arXiv:1910.05193 (first public version 2019-10-11), especially Sections 2.3 and 4.5. https://arxiv.org/abs/1910.05193
2. A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic Aspects of Symmetric Edge Polytopes*, arXiv:1807.07678 (2018), particularly the complete-bipartite \(h^*\)-formula and facet theory. https://arxiv.org/abs/1807.07678
3. G. Gordon and F. Petrov, *Combinatorics of the Lipschitz Polytope*, arXiv:1608.06848 (2016). https://arxiv.org/abs/1608.06848
4. *On gamma-vector of symmetric edge polytopes*, arXiv:2201.09835 (2022), a related study of primal combinatorial invariants. https://arxiv.org/abs/2201.09835
