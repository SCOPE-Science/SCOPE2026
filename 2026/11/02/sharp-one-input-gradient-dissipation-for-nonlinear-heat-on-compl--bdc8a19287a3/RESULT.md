# Sharp one-input gradient dissipation for nonlinear heat on complete multipartite graphs

## Finding

For every finite complete multipartite graph \(G=K_{n_1,\ldots,n_r}\), with \(r\ge 2\), positive integer part sizes and unit vertex masses and edge conductances, the edge-Lipschitz seminorm is nonincreasing along **every individual** discrete \(p\)-heat trajectory, for any prescribed \(1<p<\infty\), exactly when
\[
2s\le N+2,
\]
where \(N=\sum_i n_i\) and \(s\ge t\) are the two largest part sizes. In particular the contraction condition is independent of the nonlinear power.

More strongly, let \(\Gamma_p(G)\) be the largest right instantaneous derivative of the seminorm among all initial states with seminorm one. It is sharp, not merely an upper estimate, and equals
\[
\Gamma_p(G)=
\begin{cases}
2s-N-2,&1<p\le2\ \text{or}\ 2s\ge N,\\[3pt]
-2-\left[(N-2s)^{-1/(p-2)}+(N-s-t)^{-1/(p-2)}\right]^{-(p-2)},
& p>2\ \text{and}\ 2s<N.
\end{cases}
\]
The two denominators in the second case are strictly positive. Thus even when contraction holds for all powers, its **optimal instantaneous dissipation** depends nontrivially on the exponent and, for \(p>2\), on the second-largest part.

For example, on \(K_{2,2,2}\), the sharp coefficients at powers \(2,3,4\) are respectively \(-4,-3,-5/2\). On \(K_{5,1,1,1}\) the sharp coefficient is zero for every power, while on \(K_{6,1,1}\) it is \(+2\) and an individual solution initially increases its edge-Lipschitz seminorm.

## Assumptions and scope

The graph is the finite simple connected complete multipartite graph with at least two nonempty parts and vertex set \(V\). Every edge has weight one and every vertex has mass one. For each real \(p>1\), put \(\phi_p(z)=|z|^{p-2}z\) for \(z\ne0\) and \(\phi_p(0)=0\), and let \(S_\tau u\) solve
\[
\frac{d}{d\tau}u_x(\tau)=\sum_{y\sim x}\phi_p(u_y(\tau)-u_x(\tau)),
\qquad u(0)=u\in\mathbb R^V.
\]
Define \(L_G(u)=\max_{xy\in E}|u_x-u_y|\) and the upper right derivative \(D^+f(0)=\limsup_{h\downarrow0}(f(h)-f(0))/h\). The exact invariant is
\[
\Gamma_p(G)=\sup_{L_G(u)=1}D^+\!\left[L_G(S_\tau u)\right]_{\tau=0}.
\]
The supremum is attained by explicit finite configurations. This is **one-input** contraction \(L_G(S_\tau u)\le L_G(u)\), not contraction of the difference between two distinct solutions.

## Proof

**Global well-posedness.** The vector field is the negative Euclidean gradient of \(\sum_{xy\in E}|u_x-u_y|^p/p\), which is convex and continuously differentiable for \(p>1\). If \(u,v\) are solutions, monotonicity of \(\phi_p\) gives
\[
\frac12\frac{d}{d\tau}\sum_x(u_x-v_x)^2
=-\sum_{xy\in E}(u_x-u_y-v_x+v_y)
\bigl(\phi_p(u_x-u_y)-\phi_p(v_x-v_y)\bigr)\le0.
\]
This gives uniqueness even when \(1<p<2\). The maximum coordinate cannot increase and the minimum cannot decrease, giving boundedness and global existence; every solution is continuously differentiable.

**Exact one-edge variational problem.** Fix any edge joining parts of orders \(a,b\), let \(k=N-a-b\) and \(d=|a-b|\), and orient its endpoints \(x,y\) so \(u_x-u_y=L_G(u)=1\). Subtract a constant to make \(u_x=1,u_y=0\). For remaining values \(\alpha\) in the first part, \(\beta\) in the second part and \(z\) in any other part, the edge constraint gives
\[
\alpha\in[-1,1],\quad\beta\in[0,2],\quad z\in[0,1].
\]
Writing \(F_x\) for the time derivative of \(u_x\), cancellation of the direct edge and of the shared neighbors yields exactly
\[
F_x-F_y=-2+\sum_{\beta}\phi_p(\beta-1)
-\sum_{\alpha}\phi_p(\alpha)
-\sum_z\bigl(z^{p-1}+(1-z)^{p-1}\bigr).
\tag{1}
\]
If a \(\beta\) exceeds \(1\), let \(h\in(0,1]\) be the largest excess. All \(\alpha\) and common-neighbor values must be at least \(h\) by the complete-multipartite adjacency constraints; the two nonshared sums have combined upper bound \((b-a)h^{p-1}\). If an \(\alpha\) is negative, the reflected argument gives \((a-b)h^{p-1}\), where \(h\) is the maximal depth below zero. These two kinds of excursion cannot both occur because the corresponding vertices are adjacent. If neither occurs, the two nonshared sums are nonpositive.

Put
\[
H_p(h)=\min_{h\le z\le1}\bigl(z^{p-1}+(1-z)^{p-1}\bigr).
\]
The preceding argument bounds (1) by
\[
-2+\max_{0\le h\le1}\{d h^{p-1}-kH_p(h)\}.
\tag{2}
\]
This bound is attained: when \(b\ge a\), assign \(1\) to the chosen endpoint in the \(a\)-part, \(h\) to its other vertices, \(0\) to the chosen endpoint in the \(b\)-part, \(1+h\) to its remaining vertices, and a minimizer of \(H_p(h)\) to every vertex in each other part. Every edge difference then has magnitude at most one and the chosen edge attains (2). If \(a>b\), exchange the part labels before making the construction. In particular (2) is the **exact maximum** of the derivative along an initially tight edge for these part sizes.

**Scalar maximization.** When \(1<p\le2\), concavity of \(z^{p-1}+(1-z)^{p-1}\) gives \(H_p(h)=1\); the maximum in (2) is \(d-k\) at \(h=1\). When \(p>2\), writing \(q=p-1>1\), convexity gives
\[
H_p(h)=\begin{cases}2^{1-q},&0\le h\le1/2,\\h^q+(1-h)^q,&1/2\le h\le1.\end{cases}
\]
If \(d\ge k\), then \(H_p(h)\ge h^q\), and the maximum equals \(d-k\) at \(h=1\). If \(d<k\), the expression increases for \(0\le h\le1/2\), while for \(h\ge1/2\) it is
\[
-(k-d)h^q-k(1-h)^q.
\]
Its unique maximum is at
\[
h_*={k^{1/(p-2)}\over k^{1/(p-2)}+(k-d)^{1/(p-2)}}\in[1/2,1),
\]
and has value
\[
-\bigl[(k-d)^{-1/(p-2)}+k^{-1/(p-2)}\bigr]^{-(p-2)}.
\tag{3}
\]
Consequently every ordered pair of distinct parts has the exact sharp tight-edge rate \(\gamma_p(a,b)\) given by (2)--(3), minus the universal contribution \(2\).

**Optimization over all part pairs.** Suppose \(a\ge b\). Then
\[
d-k=2a-N,\quad k-d=N-2a,\quad k=N-a-b.
\]
For \(p\le2\), the largest rate is attained by choosing \(a=s\), hence \(\Gamma_p(G)=2s-N-2\). For \(p>2\) and \(2s\ge N\), that pair falls in the \(d\ge k\) case, and every other pair is bounded above by its value. For \(p>2\) and \(2s<N\), all pairs satisfy \(d<k\). The expression in (3), including its minus sign, increases when either \(a\) or \(b\) increases, so the maximizing pair uses the largest two parts \(s,t\). This proves the displayed formula for \(\Gamma_p(G)\) in every parameter regime. It also proves that the upper rate is genuinely attained.

**From instantaneous rates to complete classification.** Positive homogeneity of the vector field yields, at any state with \(L_G(u)>0\),
\[
D^+L_G(S_\tau u)\big|_{\tau=0}\le
\Gamma_p(G)L_G(u)^{p-1}.
\]
This follows by taking the maximum directional derivative over the finitely many active oriented edges; each satisfies the tight-edge bound. Apply the same inequality at every time along a solution. If \(\Gamma_p(G)\le0\), a scalar Dini-derivative comparison shows \(L_G(S_\tau u)\le L_G(u)\). If \(\Gamma_p(G)>0\), the sharp witness constructed above has a strictly positive right derivative, so contraction fails immediately. The formula for \(\Gamma_p\) has nonpositive sign exactly when \(2s\le N+2\), proving the power-independent if-and-only-if statement.

Moreover, whenever \(\Gamma_p(G)<0\), scalar integration gives
\[
L_G(S_\tau u)\le\begin{cases}
\bigl[L_G(u)^{2-p}+(2-p)\Gamma_p(G)\tau\bigr]_+^{1/(2-p)},&1<p<2,\\
L_G(u)e^{\Gamma_2(G)\tau},&p=2,\\
\bigl[L_G(u)^{2-p}-(p-2)\Gamma_p(G)\tau\bigr]^{-1/(p-2)},&p>2.
\end{cases}
\]
These are rigorous decay **bounds** with a sharp initial coefficient, not claims of equality at later times. When \(\Gamma_p(G)>0\) and \(p\ne2\), rescaling the initial witness by amplitude \(\lambda>0\) multiplies its normalized initial growth rate by \(\lambda^{p-2}\). Letting \(\lambda\to\infty\) for \(p>2\), or \(\lambda\downarrow0\) for \(1<p<2\), makes that rate unbounded.

## Verification

Run `python3 verify_multipartite_pheat.py` with Python 3 and NumPy/SciPy available. The independent finite checker builds graph edges from part labels and computes the original vertex differential equation directly. It tests 2,855 exact-rational sample inequalities for the active-edge upper bound, 60 exact witness equalities, 350 global sharp-coefficient cases over powers \(3/2,2,3,4,5\), and short-time integrations of contracting, critical and expanding examples. All checks passed. These tests validate implementations and special cases, **not** the universal analytic argument.

## Relationship to prior work

Mugnolo's 2012 discrete \(p\)-heat theory establishes well-posedness, order preservation and general nonlinear semigroup properties. Hua--Mugnolo (2014) study time regularity and long-time behavior. Lin--Liu--Yang (2015) prove a different positive-function gradient estimate, and Münch--Wojciechowski (2017) discuss curvature and linear graph-heat Lipschitz bounds. The exact edge-Lipschitz **one-input** sharp rate here is different from order contraction in vertex norms, positive-function gradient estimates, linear curvature estimates and **two-input** graph-Lipschitz stability.

The special linear exponent \(p=2\) and its part-size threshold are not asserted to be new in isolation; neither are the pure-clique or star specializations. The nontrivial content is the all-nonlinear-powers classification together with the exact, exponent-dependent sharp initial dissipation formula. A matching result under different terminology in unindexed literature is a remaining priority risk.

## Limitations

All graph edges and vertex masses are one; varying them can change the rates and phase boundary. The graph must be complete multipartite with at least two nonempty parts and must be finite. Signals are real-valued. Unbounded instantaneous normalized growth does not establish unbounded amplification at any fixed positive time. The sharp coefficient is local in time; the integrated decay inequalities need not be attained after time zero. Independent validation has not been performed.

## References

1. Delio Mugnolo, *Parabolic theory of the discrete p-Laplace operator*, arXiv:1207.1996, first public 2012-07-09. https://arxiv.org/abs/1207.1996
2. Bobo Hua and Delio Mugnolo, *Time regularity and long-time behavior of parabolic p-Laplace equations on infinite graphs*, arXiv:1410.1584, first public 2014-10-06. https://arxiv.org/abs/1410.1584
3. Yong Lin, Shuang Liu, and Yunyan Yang, *A gradient estimate for positive functions on graphs*, arXiv:1509.07981, first public 2015-09-26. https://arxiv.org/abs/1509.07981
4. Florentin Münch and Radosław Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, arXiv:1712.00875, first public 2017-12-04. https://arxiv.org/abs/1712.00875
