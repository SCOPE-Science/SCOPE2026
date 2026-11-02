# A linear-price crossover in D-optimal conductance allocation on square tori

## Finding

Let \(G_n=C_n\square C_n\), \(n\ge3\), with one independently adjustable nonnegative conductance on every edge. Horizontal conductance costs one unit per unit weight and vertical conductance costs \(Q>0\); the total budget is \(B>0\). Maximize the weighted spanning-tree enumerator
\[
\tau(w)=\sum_{T\text{ spanning tree of }G_n}\prod_{e\in T}w_e.
\]
The optimizer exists and is **unique among all individually adjustable edge weights**, including allocations with zero edges. Every horizontal edge has the same positive weight \(a_n\), and every vertical edge has the same positive weight \(b_n\).

Put \(\lambda_j=4\sin^2(\pi j/n)\) for \(0\le j<n\) and
\[
A_n(t)=\sum_{(j,k)\ne(0,0)}\frac{\lambda_j}{\lambda_j+t\lambda_k},\qquad
D_n(t)=\sum_{(j,k)\ne(0,0)}\frac{\lambda_k}{\lambda_j+t\lambda_k}.
\]
For every \(Q>0\) there is exactly one \(t_n(Q)>0\) satisfying
\[
\frac{D_n(t_n(Q))}{A_n(t_n(Q))}=Q.
\]
The full, unrestricted optimum is exactly
\[
a_n=\frac{B}{n^2(1+Qt_n(Q))},\qquad b_n=t_n(Q)a_n.
\]
It obeys \(t_n(Q)t_n(1/Q)=1\), and for each fixed \(n\),
\[
\lim_{Q\to\infty}nQt_n(Q)=1.
\]

The singular large-torus/large-price regime has an explicit two-term expansion. Define
\[
\ell(y)=4\sin^2(\pi y),\qquad
\Phi(z)=\frac{\sqrt z}{2}\coth\!\left(\frac{\sqrt z}{2}\right),\quad \Phi(0)=1,
\]
\[
H(u)=\int_0^1\Phi(u\ell(y))\,dy,\qquad u>0.
\]
For every fixed \(\kappa>0\), there is exactly one \(u_\kappa>0\) such that \(H(u_\kappa)/u_\kappa=\kappa\). Define
\[
v_\kappa=\frac{u_\kappa\bigl(H(u_\kappa)^2-1\bigr)}{H(u_\kappa)-u_\kappa H'(u_\kappa)}>0.
\]
If \(Q=\kappa n\), then
\[
\boxed{t_n(\kappa n)=\frac{u_\kappa}{n^2}+\frac{v_\kappa}{n^3}+O_\kappa(n^{-4}).}
\]
The crossover curve has sharp extremes
\[
\lim_{\kappa\to\infty}\kappa u_\kappa=1,\qquad
\lim_{\kappa\downarrow0}\kappa^2u_\kappa=\frac4{\pi^2}.
\]
In contrast, for a fixed \(Q>0\), the limit \(t_\infty(Q)=\lim_{n\to\infty}t_n(Q)\) is strictly positive, and \(t_\infty(Q)\sim4/(\pi^2Q^2)\) as \(Q\to\infty\). Consequently, taking high price before increasing the side length produces a different conductance power law from taking the infinite-volume limit first.

## Assumptions and scope

The vertices are \((j,k)\in(\mathbb Z/n\mathbb Z)^2\). Horizontal edges join \((j,k)\) to \((j+1,k)\); vertical edges join \((j,k)\) to \((j,k+1)\). For \(n\ge3\) these are \(2n^2\) distinct undirected edges. Each horizontal weight has price one, each vertical weight price \(Q\), and weights satisfy \(\sum_{e\mathrm{\ horizontal}}w_e+Q\sum_{e\mathrm{\ vertical}}w_e\le B\). The objective uses edge weights, not weighted edge lengths, and is the sum of products of conductances over spanning trees. Throughout, \(n\) is an integer tending to infinity, \(\kappa\) is a fixed positive real in the double-scaling statement, and constants in \(O_\kappa\) can depend on \(\kappa\) but not \(n\).

## Proof

**1. Unrestricted uniqueness and symmetry.** A budget-feasible maximizer exists by compactness and has positive tree enumerator because positive constant weights are feasible. On the connected-support domain, \(\tau(w)=\det L_0(w)\), where \(L_0\) is any grounded weighted Laplacian. The matrix \(L_0(w)\) is positive definite. The function \(\log\det\) is strictly concave on positive definite matrices, and the map from individual edge weights to \(L_0\) is injective on a simple graph: its off-diagonal entries determine the weights, including edges incident to the removed vertex via the original row-sum constraints. Equivalently, if two grounded Laplacians agree, the associated full Laplacians agree on the orthogonal complement of the constants and thus agree identically; each off-diagonal edge weight is then determined. Therefore \(\log\tau\) is strictly concave on the feasible connected-support set. The objective increases strictly with any additional edge weight, so the budget is saturated. Translating and reflecting either cycle preserves both the graph and the prices. Averaging a maximizing vector over these automorphisms cannot decrease \(\log\tau\), and strict concavity forces invariance under every translation. Thus all horizontal weights are \(a\) and all vertical weights are \(b\). If either is zero, the graph splits into \(n\) disjoint cycles; hence \(a,b>0\).

**2. Exact finite equation.** Fourier diagonalization of the weighted torus Laplacian gives eigenvalues \(a\lambda_j+b\lambda_k\). The weighted matrix-tree theorem yields
\[
\tau(a,b)=\frac1{n^2}\prod_{(j,k)\ne(0,0)}(a\lambda_j+b\lambda_k).
\]
Write \(t=b/a\), \(M=n^2-1\), and \(a=B/[n^2(1+Qt)]\). Differentiating \(\log\tau\) in \(t\) gives \(D_n(t)-MQ/(1+Qt)\). Since \(A_n(t)+tD_n(t)=M\), stationarity is precisely \(D_n(t)=QA_n(t)\).

To prove there is only one positive root, note \(D_n'(t)=-\sum'\lambda_k^2/(\lambda_j+t\lambda_k)^2\) and \(A_n=M-tD_n\). Hence
\[
\left(\frac{D_n}{A_n}\right)'=
\frac{M D_n'(t)+D_n(t)^2}{A_n(t)^2}<0.
\]
Strictness follows from Cauchy--Schwarz applied to the \(M\) terms \(\lambda_k/(\lambda_j+t\lambda_k)\): some terms vanish and others do not. As \(t\downarrow0\), the \(j=0,k\ne0\) terms give \(D_n(t)=(n-1)/t+O(1)\), while \(A_n(t)=n(n-1)+O(t)\). Therefore \(D_n/A_n\sim1/(nt)\). Exchanging \(j,k\) shows \((D_n/A_n)(1/t)=(A_n/D_n)(t)\), proving the reciprocal identity and that the ratio tends to zero at infinity. Both root uniqueness and the fixed-size high-price law follow.

**3. Exact cyclic resolvent.** Put \(F_n(t)=tD_n(t)=\sum' t\lambda_k/(\lambda_j+t\lambda_k)\). For \(\alpha>0\) write \(\alpha=4\sinh^2(\gamma/2)\). The Poisson-kernel identity and the sum over \(n\)-th roots of unity give
\[
\sum_{j=0}^{n-1}\frac{\alpha}{\alpha+\lambda_j}
=n\tanh(\gamma/2)\coth(n\gamma/2).
\]
Applying this with \(\alpha=t\lambda_k\), excluding the unique zero mode, gives the exact finite identity
\[
F_n(t)=\sum_{k=1}^{n-1}n\sqrt{\frac{t\lambda_k}{4+t\lambda_k}}
\coth\!\left(n\operatorname{arsinh}\frac{\sqrt{t\lambda_k}}2\right).
\]
For \(t=u/n^2\), with \(u\) in any compact positive interval and \(z=u\lambda_k\), each summand is \(\Phi(z)+O(n^{-2})\), uniformly including the removable singularity \(z=0\). The periodic trapezoidal rule applied to the smooth periodic function \(y\mapsto\Phi(u\ell(y))\) gives \(\sum_{k=0}^{n-1}\Phi(u\lambda_k)=nH(u)+O(n^{-1})\). Thus, uniformly on compact positive \(u\)-intervals, including one \(u\)-derivative,
\[
F_n(u/n^2)=nH(u)-1+O(n^{-1}).
\]
The exact optimum equation can be rewritten as
\[
Q=\frac{F_n(t)}{t(M-F_n(t))}.
\]
Substitution gives
\[
\frac{Q_n(u/n^2)}n=\frac{H(u)}u+\frac{H(u)^2-1}{nu}+O(n^{-2}),
\]
where \(Q_n(t)=D_n(t)/A_n(t)\). Moreover, from the classical partial-fraction expansion of \(\coth\),
\[
\frac{H(u)}u=\sum_{r\in\mathbb Z}\int_0^1
\frac{\ell(y)}{(2\pi r)^2+u\ell(y)}\,dy.
\]
The integrand for \(r=0\) is interpreted as \(1/u\) except at a measure-zero point. This representation is continuous and strictly decreasing in \(u>0\), with limits \(+\infty\) and \(0\). So the positive solution \(u_\kappa\) exists uniquely. Strict monotonicity of \(Q_n\) sandwiches the finite positive solution \(u_n=n^2t_n(\kappa n)\) around \(u_\kappa\), proving \(u_n\to u_\kappa\). Since \((H/u)'=(uH'-H)/u^2<0\), Taylor expansion of the preceding uniform equation yields
\[
u_n=u_\kappa+\frac{u_\kappa(H(u_\kappa)^2-1)}{n(H(u_\kappa)-u_\kappa H'(u_\kappa))}+O_\kappa(n^{-2}).
\]
This is the two-term expansion for \(t_n\). Positivity of the correction follows because \(\Phi(z)>1\) for \(z>0\), and \(\Phi(z)-z\Phi'(z)>0\) for \(z\ge0\).

**4. The two limiting price powers.** The Taylor expansion \(\Phi(z)=1+z/12+O(z^2)\) gives \(H(u)\to1\) as \(u\downarrow0\), and hence \(\kappa u_\kappa\to1\) for \(\kappa\to\infty\). Dominated convergence in the integral defining \(H\) gives
\[
\lim_{u\to\infty}\frac{H(u)}{\sqrt u}
=\frac12\int_0^1\sqrt{\ell(y)}\,dy=\frac2\pi,
\]
so \(\kappa^2u_\kappa\to4/\pi^2\) as \(\kappa\downarrow0\).

For fixed \(t>0\), the double Riemann sum satisfies
\[
\frac{F_n(t)}{n^2-1}\longrightarrow
s(t)=\int_0^1\sqrt{\frac{t\ell(y)}{4+t\ell(y)}}\,dy.
\]
The inner integral in the first Fourier coordinate is the same Poisson-kernel integral used above. Consequently, \(Q_n(t)\to s(t)/[t(1-s(t))]\). This continuous strictly decreasing function ranges from infinity to zero; the same sandwich argument proves the existence and uniqueness of \(t_\infty(Q)\). Finally \(s(t)\sim2\sqrt t/\pi\) for \(t\downarrow0\), which gives \(t_\infty(Q)\sim4/(\pi^2Q^2)\) as \(Q\to\infty\).

## Verification

The independently executable `VERIFY.py` requires only the Python 3 standard library. It performs exact Bareiss reduced-Laplacian cofactor evaluations for small toroidal graphs and compares them to the Fourier determinant; checks the finite stationarity equation, monotonicity, reciprocity, high-price behavior, the root-of-unity resolvent, and finite-size convergence to both crossover coefficients. An actual run completed **124 checks successfully**. These finite calculations do not replace the general concavity, Fourier, and asymptotic proofs above.

## Relationship to prior work

Tzeng and Wu's 2000 Theorem 2 gives the directionally weighted hypercubic spanning-tree product used in Step 2; that product is **not** claimed as new. Izmailian and Kenna (2015) study the same type of finite weighted-lattice partition function and its finite-size free-energy corrections under several boundary conditions. Khosoussi et al. (2016) give general weighted spanning-tree network-design and determinant-optimization context, principally for edge selection. The distinct claim here concerns unrestricted per-edge **continuous conductance allocation under unequal prices**, especially the singular \(Q=\kappa n\) optimum and its nontrivial integral-\(\coth\) limit with an explicit first correction. Earlier results on resistance-optimal square tori concern the different objective \(\operatorname{tr}(L^+)\), and D-optimal prism networks have a fixed-width second factor rather than a second growing cycle. Neither objective/geometric case supplies this theorem merely by parameter substitution.

## Limitations

The result is for simple square tori with \(n\ge3\), two direction-wide linear prices, and nonnegative independently adjustable undirected conductances. It does not cover arbitrary price patterns, higher dimensions, or rectangular aspect ratios. The displayed finite-size remainder is for each fixed \(\kappa>0\), not asserted uniformly as \(\kappa\) tends to zero or infinity. Mathematical novelty is assessed against the inspected literature, not certified by an exhaustive world-literature search. No independent external mathematical validation has been performed.

## References

- W.-J. Tzeng and F. Y. Wu, *Spanning Trees on Hypercubic Lattices and Non-orientable Surfaces*, arXiv:cond-mat/0001408, first posted 2000-01-27. https://arxiv.org/abs/cond-mat/0001408
- N. Sh. Izmailian and R. Kenna, *Exact finite-size corrections for the spanning-tree model under different boundary conditions*, arXiv:1409.7282, first posted 2014-09-25; Physical Review E 91, 022129 (2015). https://arxiv.org/abs/1409.7282
- K. Khosoussi, G. S. Sukhatme, S. Huang and G. Dissanayake, *Maximizing the Weighted Number of Spanning Trees: Near-t-Optimal Graphs*, arXiv:1604.01116, first posted 2016-04-05. https://arxiv.org/abs/1604.01116
