# Shifted square-root conductance law for heterogeneously priced bicliques

## Finding
Let \(p,q\ge2\) be integers and let \(K_{p,q}\) have labelled left vertices \(u_1,\ldots,u_p\) and right vertices \(v_1,\ldots,v_q\). Every edge \(u_iv_j\) has unit-conductance price \(\rho_i>0\). Independently choose nonnegative conductances \(w_{ij}\) with budget \(\sum_{i,j}\rho_iw_{ij}=B>0\), to minimize the sum \(\mathcal K=\sum_{x<y}R_{xy}\) of all unordered-pair effective resistances, with disconnected allocations assigned infinite objective.

Write \(N=p+q\), and let \(\alpha\in(0,\min_i\rho_i)\) be the **unique** solution of
\[
\alpha\left(\sum_{i=1}^p\frac{1}{\sqrt{\rho_i-\alpha}}\right)^2=\frac{Nq(q-1)}{N-1}.
\]
Define \(T=\sum_i\rho_i/\sqrt{\rho_i-\alpha}\). The unique global minimizer, **without any assumed edge symmetry**, is
\[
w_{ij}^{*}=\frac{B}{qT\sqrt{\rho_i-\alpha}}\qquad(1\le i\le p,\;1\le j\le q),
\]
and the optimal resistance sum is
\[
\boxed{\mathcal K_{*}=\frac{N-1}{B}T^2.}
\]
Every edge is strictly positive. A cheaper left vertex always receives strictly more conductance on each incident edge, and tied prices yield equal conductance.

As a normalization check, when every price equals \(\rho\), the formulas reduce to \(w_{ij}^*=B/(pq\rho)\) and \(\mathcal K_*=\rho[(N-1)p^2+Nq(q-1)]/B\).

**Large-right-class concentration.** Fix \(p\), \(B\), and prices with one strict minimum \(\rho_1<\rho_i\) for \(i\ge2\), then let \(q\to\infty\). The exact optimal designs satisfy
\[
q^2(\rho_1-\alpha)\longrightarrow\rho_1,\qquad
\frac{q\rho_1w_{1j}^{*}}{B}\longrightarrow1,
\]
\[
\frac{q^2w_{ij}^{*}}{B}\longrightarrow
\frac{1}{\sqrt{\rho_1(\rho_i-\rho_1)}}\quad (i\ge2),
\qquad
\frac{\mathcal K_*}{q^3}\longrightarrow\frac{\rho_1}{B}.
\]
Thus, although every edge remains positive for every finite \(q\), asymptotically all the budget concentrates on edges incident with the uniquely cheapest left vertex.

## Assumptions and scope
Conductance, not resistance, is the independently adjustable physical edge variable. An edge with left endpoint \(u_i\) costs \(\rho_i\) per unit conductance, identically for all its right endpoints. The objective counts **unordered** vertex pairs and uses the unnormalized weighted graph Laplacian, so \(\mathcal K=N\operatorname{tr}(L^\dagger)\). Both parts contain at least two vertices; \(q=1\) instead gives the known tree square-root rule with \(\alpha=0\). A disconnected design has infinite objective, not the formal pseudoinverse trace of a disconnected Laplacian.

## Proof
**1. Unrestricted uniqueness and forced symmetry.** On the connected domain, \(\mathcal K=N\operatorname{tr}((L|_{\mathbf 1^\perp})^{-1})\) is strictly convex as a function of independent edge conductances. Indeed, for any nonzero symmetric perturbation \(H\) on \(\mathbf 1^\perp\), the positive-definite Hessian quadratic form is \(2N\operatorname{tr}(X^{-1}HX^{-1}HX^{-1})>0\), with \(X=L|_{\mathbf 1^\perp}\); equivalently it is twice the squared Frobenius norm of \(X^{-1/2}HX^{-1}\). The affine edge-to-Laplacian map is injective because each off-diagonal entry records one edge weight. The feasible budget simplex is compact; a minimizing sequence cannot approach disconnection because some effective resistance then diverges. Strict convexity therefore gives one global minimizer. Each permutation of the \(q\) right vertices preserves both cost and objective. Uniqueness forces \(w_{ij}=a_i\), independently of \(j\), for every \(i\). Necessarily \(a_i>0\), since otherwise \(u_i\) would be isolated. The budget becomes \(q\sum_i\rho_i a_i=B\).

**2. Exact pair resistances.** Put \(s=\sum_i a_i\). By applying unit-current laws and symmetry to this weighted complete bipartite network,
\[
R_{u_i,u_k}=\frac1q\left(\frac1{a_i}+\frac1{a_k}\right),\qquad
R_{v_j,v_\ell}=\frac2s,\qquad
R_{u_i,v_j}=\frac1{qa_i}+\frac{q-1}{qs}.
\]
For the third identity, ground \(v_j\), inject unit current at \(u_i\), and denote by \(x\) the potential of \(u_i\) and by \(y\) the common potential at the other \(q-1\) right vertices. Each other left vertex has potential \((q-1)y/q\); Kirchhoff's law gives \(y=qa_ix/(s+(q-1)a_i)\) and \(1=qa_ixs/(s+(q-1)a_i)\), hence the stated expression for \(x\). Summing all pair types gives the *exact* reduced objective
\[
\mathcal K(a)=\frac{N-1}{q}\sum_{i=1}^p\frac1{a_i}+\frac{N(q-1)}{\sum_i a_i}.
\]
This can also be checked directly from the Laplacian pseudoinverse.

**3. Solving the constrained problem.** Let \(A=(N-1)/q>0\), \(C=N(q-1)>0\), \(s=\sum_i a_i\). The objective \(A\sum_i1/a_i+C/s\) has Hessian \(\operatorname{diag}(2A/a_i^3)+2C\mathbf1\mathbf1^{\mathsf T}/s^3\), which is positive definite. The unique interior optimizer satisfies, for some \(\eta>0\),
\[
\frac A{a_i^2}+\frac C{s^2}=\eta\rho_i.
\]
Set \(\alpha=C/(\eta s^2)\) and \(t=\sqrt{A/\eta}\). Then \(a_i=t/\sqrt{\rho_i-\alpha}\). Since \(s=t\sum_i(\rho_i-\alpha)^{-1/2}\), consistency is precisely \(\alpha[\sum_i(\rho_i-\alpha)^{-1/2}]^2=C/A=Nq(q-1)/(N-1)\). Its left side is strictly increasing from zero to infinity on \((0,\min_i\rho_i)\), proving existence and uniqueness. The budget gives \(t=B/(qT)\). Finally, \(C/[A\sum_i(\rho_i-\alpha)^{-1/2}]=\alpha\sum_i(\rho_i-\alpha)^{-1/2}\); substituting into the objective yields \(\mathcal K_*=A T/t=(N-1)T^2/B\). Every premise and equality is valid for arbitrary positive real prices and budget.

**4. Concentration asymptotic.** For fixed \(p\) and a uniquely smallest \(\rho_1\), the equation's right side \(K_q=Nq(q-1)/(N-1)\) satisfies \(K_q/q^2\to1\). Writing \(\varepsilon=\rho_1-\alpha\), the equation is \((\rho_1-\varepsilon)(\varepsilon^{-1/2}+O(1))^2=K_q\), whence \(q^2\varepsilon\to\rho_1\). Then \(T/q\to\sqrt{\rho_1}\). Direct substitution into the conductance and optimum formulas gives all four stated limits.

## Verification
Run `python check_biclique.py` with NumPy, SciPy, and SymPy. The embedded checker verifies an exact-rational \(K_{3,4}\) resistance identity \(\mathcal K=29559/1096\), 96 independent spectral objective computations, 96 budget/KKT checks, 2,400 independently asymmetric feasible allocations, four unrestricted numerical optimizer comparisons, and three large-\(q\) asymptotic examples. Numerical trials corroborate but do not establish the quantified theorem; the four proof steps above establish it without finite enumeration.

For example, \(p=3\), \(q=4\), \((\rho_1,\rho_2,\rho_3)=(1,4,9)\), and \(B=1\) yield \(\alpha\approx0.892022879357\), row conductances \((0.08979316,0.01673671,0.01036222)\), and \(\mathcal K_*\approx430.73787328\). Every edge to the same right vertex is allowed to vary independently in the global claim.

## Relationship to prior work
Ghosh, Boyd and Saberi established general convex minimization of total effective resistance and its strict convexity and treated trees, wheels and two-clique barbells analytically [1,2]. Their general method permits numerical optimization of this problem but does not state the heterogeneous vertex-price biclique scalar law or its cheapest-channel large-size concentration. The related vertex-weighted multipartite resistance-distance paper by Chen and Yan [3] concerns closed resistance expressions for multiplicatively vertex-weighted **edge resistances**; its abstract does not claim this budget optimization or asymptotics, but the full paper was not inspected. The present explicit optimization theorem is distinct from an arbitrary-weight resistance formula. Specialized unlocated prior work could nonetheless cover part or all of the result.

## Limitations
Only prices constant along each left vertex's incident edges are classified; arbitrary edge-by-edge price matrices are not. The concentration theorem fixes \(p\), \(B\), and prices and requires a unique cheapest left vertex. For all equal prices, the formula specializes to equal conductance per edge. No new general convexity theorem, independent validation, or publication priority is claimed. Historical novelty is based on the sources and searches identified above and is not a proof of exhaustive priority.

## References
[1] A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, MTNS 2006, Kyoto, July 24–28, 2006, pp. 1185–1196. https://web.stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf

[2] A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review **50** (2008), 37–66, DOI:10.1137/050645452. https://www.web.stanford.edu/~boyd/papers/eff_res.html

[3] W. Chen and W. Yan, *Resistance distances in vertex-weighted complete multipartite graphs*, Applied Mathematics and Computation **409** (2021), 126382, DOI:10.1016/j.amc.2021.126382. Abstract examined; full text not available in this review.
