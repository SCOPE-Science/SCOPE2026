# A sharp matching-price transition in resistance-optimized complete networks

## Finding
Let \(N=2m\ge4\), and distinguish a perfect matching \(M\) in the complete graph on \(N\) vertices. A unit of conductance on an edge of \(M\) costs \(t>0\), whereas it costs one on every other edge. Under the exact budget
\[
 t\sum_{e\in M}w_e+\sum_{e\notin M}w_e=1,\qquad w_e\ge0,
\]
minimize the Kirchhoff index \(K(w)=\sum_{u<v}R_{uv}(w)\), interpreted as \(+\infty\) if the positive-conductance subgraph is disconnected.

Put \(d=N-2\) and
\[
 t_N^{\mathrm{crit}}=\frac{N^2}{N^2-2N+2}=\frac{2N^2}{N^2+d^2}.
\]
There is exactly **one** globally optimal conductance vector. All matching edges have a common optimal conductance \(a^*\); all other edges have a common conductance \(b^*\). If \(t\ge t_N^{\mathrm{crit}}\), then
\[
 a^*=0,\qquad b^*=\frac{1}{m d},\qquad K^*=K_{\rm delete}:=\frac N4(N^2+d^2).
\]
If \(0<t<t_N^{\mathrm{crit}}\), define
\[
 x^*=\frac{N\sqrt{(2-t)/t}-d}{2}>0,
 \qquad b^*=\frac{1}{m(d+t x^*)},\qquad a^*=x^*b^*.
\]
Then
\[
 K^*=\frac N8\left(N\sqrt t+d\sqrt{2-t}\right)^2,
\]
and the exact benefit from retaining the matching class is
\[
 K_{\rm delete}-K^*=\frac N8\left(N\sqrt{2-t}-d\sqrt t\right)^2>0.
\]
At equality \(t=t_N^{\mathrm{crit}}\) the two expressions for the optimum agree and \(a^*=0\).

The critical price tends to one and has a nontrivial finite-size window. For each fixed real \(s\), choose \(t_N=1+s/N>0\) for all sufficiently large even \(N\). Then
\[
 \lim_{N\to\infty}\frac{a^*(t_N)}{b^*(t_N)}=\left(1-\frac s2\right)_+,
 \qquad
 \lim_{N\to\infty}\frac{K_{\rm delete}-K^*(t_N)}N=\frac{(2-s)_+^2}{8},
\]
where \(z_+=\max\{z,0\}\). In particular, \(N(t_N^{\mathrm{crit}}-1)\to2\). For a fixed \(t>0\), the macroscopic optimum is
\[
 \lim_{\substack{N\to\infty\\N\text{ even}}}\frac{K^*(t)}{N^3}=
 \begin{cases}
 \frac18(\sqrt t+\sqrt{2-t})^2,&0<t<1,\\
 \frac12,&t\ge1.
 \end{cases}
\]
Thus this design problem has a sharp pruning boundary for the matching orbit and a second-order singularity in its normalized large-network value at unit price.

## Assumptions and scope
The graph is the undirected simple complete graph \(K_N\), with an arbitrary fixed perfect matching and positive real edge prices as specified above. Conductances may be zero. All vertex pairs are included in the resistance objective, not merely adjacent pairs. Every edge not in the distinguished matching has the same unit price. The exact unit budget fixes the scale. The assertions hold for every even integer \(N\ge4\) and every real \(t>0\); no assumption that the underlying network begins unweighted is imposed. The pair-symmetric subgraph with all matching conductances zero remains connected, including at \(N=4\).

## Proof
**Existence and global uniqueness.** Let \(L(w)\) be the weighted combinatorial Laplacian and \(J=\mathbf1\mathbf1^{\mathsf T}\). On connected allocations,
\[
 K(w)=N\operatorname{tr}(L(w)+J/N)^{-1}-N.
\]
Indeed, \(L(w)+J/N\) has eigenvalue one along the constants and the positive Laplacian eigenvalues on their orthogonal complement. For each nonzero symmetric perturbation \(H\), the second directional derivative of the inverse-trace objective is
\[
 2N\operatorname{tr}\!\left(A^{-1}HA^{-1}HA^{-1}\right)>0,
 \quad A=L(w)+J/N>0.
\]
To see strict positivity, write the trace as \(\operatorname{tr}[A^{-1/2}(A^{-1/2}HA^{-1/2})^2A^{-1/2}]\). Different edge-weight vectors give different Laplacians because their off-diagonal entries are the negatives of the individual edge conductances. Consequently \(K\) is strictly convex in the edge weights on the domain of connected allocations. The feasible nonnegative budget simplex is compact, contains connected allocations, and the objective diverges as a positive Laplacian eigenvalue tends to zero. Its minimizing allocation therefore exists, is connected, and is unique. The automorphism group preserving the matching acts transitively on matching edges and, separately, on all other edges. Since the objective and budget are invariant under this group, global uniqueness forces the optimizer to have matching conductance \(a\ge0\) and other-edge conductance \(b>0\), each constant within its orbit.

**Spectrum and scalar reduction.** There are \(m=N/2\) matching edges and \(md=N(N-2)/2\) nonmatching edges. Thus the budget is
\[
 m(ta+db)=1.
\]
The \(m\)-dimensional space of vectors antisymmetric inside each matched pair is a Laplacian eigenspace of eigenvalue \(2a+db\). The \((m-1)\)-dimensional space of vectors constant on each pair and summing to zero overall has eigenvalue \(Nb\). The last eigenvector is constant, with eigenvalue zero. As \(b>0\), the corresponding Kirchhoff index is exactly
\[
 K(a,b)=N\left[\frac m{2a+db}+\frac{m-1}{Nb}\right].
\]
Write \(x=a/b\ge0\). The budget gives \(b=[m(tx+d)]^{-1}\); with \(y=2x+d\ge d\), the index becomes
\[
 K(y)=C+A_0y+\frac{B_0}{y},
\]
where
\[
 C=\frac{Nm^2t}{2}+m(m-1)d\left(1-\frac t2\right),\quad
 A_0=\frac{mt(m-1)}2>0,\quad
 B_0=\frac{Nm^2d(2-t)}2.
\]
If \(0<t<2\), then \(B_0>0\) and the unconstrained unique minimizer is
\[
 y_0=\sqrt{B_0/A_0}=N\sqrt{\frac{2-t}{t}}.
\]
It lies in \([d,\infty)\) precisely when
\[
 t\le \frac{2N^2}{N^2+d^2}=t_N^{\mathrm{crit}}.
\]
Since \(t_N^{\mathrm{crit}}<2\), these two alternatives cover the full positive-price domain. If \(t\ge2\), then \(B_0\le0\) and \(K'(y)=A_0-B_0/y^2>0\), again forcing \(y=d\). For \(t_N^{\mathrm{crit}}\le t<2\), the unconstrained minimum is below \(d\), so the unique feasible minimum is also \(y=d\). For lower prices, \(y=y_0>d\). Substitution into \(b=[m(tx+d)]^{-1}\) and \(x=(y-d)/2\) gives exactly the stated conductances and proves their uniqueness among all feasible edge-weight vectors.

**Optimal values and deletion benefit.** At the deleted-matching allocation, the nonzero Laplacian eigenvalues are \(db\) (multiplicity \(m\)) and \(Nb\) (multiplicity \(m-1\)), with \(b=1/(md)\). Hence
\[
 K_{\rm delete}=\frac N4(N^2+d^2).
\]
For the interior solution \(y=y_0\), substituting into \(C+A_0y+B_0/y\) and using \(d=N-2\) yields
\[
 K^*=\frac N8\bigl(N\sqrt t+d\sqrt{2-t}\bigr)^2.
\]
Subtracting the latter from the former uses the identity
\[
 2(N^2+d^2)-(N\sqrt t+d\sqrt{2-t})^2
 =(N\sqrt{2-t}-d\sqrt t)^2.
\]
The right-hand side is positive exactly on the lower-price regime and zero at its boundary; above the boundary the deleted-matching allocation is already optimal.

**Asymptotics and critical window.** The exact threshold is \(t_N^{\mathrm{crit}}=(1-2/N+2/N^2)^{-1}\), so \(N(t_N^{\mathrm{crit}}-1)\to2\). Fix real \(s\), put \(t_N=1+s/N\), and note that
\[
 \sqrt{(2-t_N)/t_N}=1-s/N+O(N^{-2}).
\]
Therefore \(x^*=\bigl(N\sqrt{(2-t_N)/t_N}-d\bigr)_+/2\to(2-s)_+/2\). The deletion-benefit formula and
\[
 N\sqrt{2-t_N}-d\sqrt{t_N}=2-s+O(N^{-1})
\]
prove the second window limit, including the boundary value \(s=2\). For fixed \(t<1\), the lower-price formula is eventually applicable; dividing it by \(N^3\) gives \((\sqrt t+\sqrt{2-t})^2/8\). For fixed \(t>1\), eventually \(t\ge t_N^{\mathrm{crit}}\) and the deleted-matching formula gives the limit \(1/2\). At \(t=1\) the interior formula gives the same limit. The normalized limiting value has left second derivative \(-1/4\) and right second derivative zero at \(t=1\), making the second-order singularity explicit.

## Verification
The standalone standard-library checker `verify_matching.py` uses exact rational arithmetic. For rational parameters of the form \(t=2/(1+r^2)\), with positive rational \(r\), the candidate ratio \(x^*\), budget weights, and optimal value are rational. The checker constructs the entire weighted Laplacian, inverts \(L+J/N\) over rational numbers, and compares the resulting Kirchhoff index with the independent spectral formula and closed optimum. It also tests rational alternative feasible allocations and exact threshold equalities. Run `python3 verify_matching.py` alongside this document.

The finite checker is supportive evidence only; its sample sizes do not establish the quantified uniqueness, optimality, or asymptotic assertions, which are proved above.

## Relationship to prior work
Ghosh, Boyd, and Saberi [1] established convex optimization of total effective resistance and analytic results for trees, wheels, barbells, and the equal-price complete graph. The present theorem uses the same electrical objective and general convexity mechanism; it does **not** claim that framework as new. Its additional content is the complete two-price, perfect-matching class solution, exact removal threshold, and sharp finite-size window, rather than an optimization algorithm for a generic graph.

Bapat, Karimi, and Liu [2] computed ordinary Kirchhoff indices for fixed unit-conductance complete multipartite graphs, including the cocktail-party graph obtained here by deleting the perfect matching. That covers the fixed-topology/unweighted endpoint, not optimizing both edge orbits under a variable relative price. Gervacio [3] established fixed-unit-resistance formulas for complete multipartite graphs, again not the jointly optimized priced-matching problem. Those endpoint and spectral formulas are antecedents, not claimed discoveries.

## Limitations
The result requires a **perfect** matching in a complete graph of even order, a single relative price for all matched edges, a common price for all other edges, and a linear conductance budget. It does not treat odd-order near-perfect matchings, arbitrary individual edge prices, nonlinear costs, multiple disjoint distinguished classes, or other resistance objectives. It does not imply that a search over all possible priced-graph designs has been solved. While the stated claim is supported by a complete proof, equivalently formulated historical classifications cannot be absolutely ruled out by literature search alone. No independent mathematical audit is represented here.

## References
[1] A. Ghosh, S. Boyd, and A. Saberi, “Minimizing Effective Resistance of a Graph,” *SIAM Review* **50** (2008), 37–66, doi:10.1137/050645452. Author-hosted primary full text: https://stanford.edu/~boyd/papers/pdf/eff_res.pdf ; electronically published 2008-02-01 (earlier conference version announced for July 2006 without a verified day).

[2] R. B. Bapat, M. Karimi, and J.-B. Liu, “Kirchhoff index and degree Kirchhoff index of complete multipartite graphs,” arXiv:1611.09457, https://arxiv.org/abs/1611.09457 ; especially Section 3 and the cocktail-party specialization.

[3] S. V. Gervacio, “Resistance distance in complete n-partite graphs,” *The Mindanawan Journal of Mathematics* **3** (2012), 1–19, https://journals.msuiit.edu.ph/tmjm/article/view/26 ; see also *Discrete Applied Mathematics* **203** (2016), 53–61, doi:10.1016/j.dam.2015.09.017.
