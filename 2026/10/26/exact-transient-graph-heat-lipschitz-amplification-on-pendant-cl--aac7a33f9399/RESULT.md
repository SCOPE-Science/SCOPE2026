# Exact transient graph-heat Lipschitz amplification on pendant cliques

## Finding
For every integer \(n\ge2\) and every \(t\ge0\), the graph-heat Lipschitz operator norm on the pendant clique is
\[
\|H_t\|_{\mathrm{Lip}\to\mathrm{Lip}}=
\frac{2(n-1)}n e^{-t}-\frac{n-2}n e^{-(n+1)t}.
\]
Contractivity for all times holds exactly for \(n\le3\). For \(n\ge4\), the unique positive-time maximum is reached at
\[
t_n=\frac1n\log\!\left(\frac{(n-2)(n+1)}{2(n-1)}\right),\qquad
M_n=\frac{2(n-1)}{n+1}\left(\frac{2(n-1)}{(n-2)(n+1)}\right)^{1/n}>1,
\]
and \(M_n\to2\) as \(n\to\infty\). The edge joining the pendant vertex and the clique hub is norming for every time.

## Assumptions and scope
Let \(G_n\) consist of a clique on \(n\) vertices \(h,o_1,\dots,o_{n-1}\), and one leaf \(p\) incident only with \(h\). Every edge is unweighted and has length one. Let \(L_n\) be the positive combinatorial Laplacian, \((L_nf)(v)=\sum_{w\sim v}(f(v)-f(w))\); heat acts as \(H_t=\exp(-tL_n)\). The seminorm is \(\mathrm{Lip}(f)=\max_{vw\in E(G_n)}|f(v)-f(w)|\), on real functions modulo constants. These conventions distinguish the claim from degree-normalized random walks.

## Proof
Write \(u=e^{-t}\), \(z=e^{-(n+1)t}\), and \(q=e^{-nt}\). The Laplacian has eigenvalues \(0,1,n,n+1\) on the constant, symmetric pendant–clique, ordinary-clique fluctuation, and hub/leaf modes, respectively, omitting empty eigenspaces. More directly, diagonalize the invariant space of triples constant across the \(n-1\) ordinary vertices, together with its ordinary-vertex mean-zero complement. For the signed heat-kernel difference \(v=H_t(p,\cdot)-H_t(h,\cdot)\), this gives
\[
v(p)=\frac{(n-1)u+z}n,\quad v(h)=-z,\quad
v(o_j)=-\frac{u-z}n\quad(1\le j\le n-1).
\]
Positive mass is located only at \(p\), whereas the hub is one edge away and each ordinary vertex is two edges away. Exact graph-metric transport (equivalently Kantorovich duality) therefore gives
\[
W_1(H_t(p,\cdot),H_t(h,\cdot))
=z+\frac{2(n-1)}n(u-z)=:F_n(t).
\]
For the hub–ordinary edge \((h,o_1)\), the signed heat-kernel difference has
\[
v(p)=\frac{u-z}n,\quad v(h)=z,\quad
v(o_1)=-\frac{u}{n(n-1)}-\frac zn-\frac{n-2}{n-1}q,
\]
and, for \(j\ne1\),
\[
v(o_j)=\frac{nq-u-(n-1)z}{n(n-1)}\le0.
\]
The last inequality is precisely \(ne^t\le e^{nt}+(n-1)\), which follows from the tangent-line inequality for the exponential. Thus all positive mass for this edge is at \(p,h\), all negative mass at ordinary vertices, and the transport cost is
\[
G_n(t)=\frac2n(u-z)+z=\frac2n u+\frac{n-2}n z.
\]
For an ordinary–ordinary clique edge, the signed kernel is \(q(\delta_{o_i}-\delta_{o_j})\), and its transport cost is exactly \(q\). As the graph-distance Lipschitz seminorm is the maximum over edges, its induced norm is the maximum of these three Wasserstein costs. The inequalities
\[
F_n(t)-G_n(t)=\frac{2(n-2)}n(u-z)\ge0,
\qquad F_n(t)\ge u\ge q
\]
show that the pendant edge always maximizes. This proves the norm formula.

Finally, \(F_n(0)=1\) and \(F_n'(0)=n-3\). If \(n=2\) then \(F_n(t)=e^{-t}\). If \(n=3\), \(F_n'(t)<0\) for every \(t>0\). If \(n\ge4\), differentiating gives one positive critical time \(t_n\) as stated; the derivative is positive before and negative after that time. Substitution yields \(M_n\), which exceeds one because \(F_n\) initially increases. Since \(t_n=(\log n+O(1))/n\to0\) and \((n+2)t_n\to\infty\), the displayed peak tends to \(2\).

## Verification
The accompanying `verify.py` independently constructs each graph Laplacian, exponentiates it numerically, and solves the complete finite Wasserstein linear program on all three edge types. It passed 147 graph/time instances for \(2\le n\le22\). These computations check formulas but are not the proof for all dimensions and times; the exact spectral and transport argument above supplies that proof.

## Relationship to prior work
Joulin's 2007 continuous-time Wasserstein-curvature treatment [1] defines the same Lipschitz-semigroup norm and its Kantorovich–Rubinstein interpretation but does not calculate this family. Ollivier [2] supplies the general Lipschitz/Wasserstein-contraction equivalence for Markov kernels but not this graph's finite-time sharp profile. Lin–Lu–Yau [3] considers a modified graph Ricci curvature for other graph classes, rather than the unnormalized heat operator's exact time-dependent norm. A previously available diameter-sharp graph-heat bound controls the supremum across graphs but does not determine this pendant-clique family's contractivity threshold, maximizing edge, or peak. The possible existence of an unindexed direct calculation remains a literature risk.

## Limitations
The statement is for simple unit-edge pendant cliques and the unnormalized combinatorial Laplacian only. It does not assert the same result for degree-normalized random walks, arbitrary numbers of leaves, or general lollipop graphs. It makes no assertion of independent audit or exhaustive historical priority.

## References
[1] A. Joulin, *Poisson-type deviation inequalities for curved continuous-time Markov chains*, arXiv:0709.0622 (first publicly posted 2007-09-05), Bernoulli 13 (2007), 782–798.
[2] Y. Ollivier, *Ricci curvature of Markov chains on metric spaces*, arXiv:math/0701886 (2007), J. Funct. Anal. 256 (2009), 810–864.
[3] Y. Lin, L. Lu, S.-T. Yau, *Ricci curvature of graphs*, Tohoku Math. J. 63 (2011), 605–627, doi:10.2748/tmj/1325886283.
