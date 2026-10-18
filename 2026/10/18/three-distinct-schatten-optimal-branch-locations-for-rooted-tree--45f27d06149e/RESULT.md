# Three distinct Schatten-optimal branch locations for rooted-tree integration

## Finding

For every integer \(m\ge 2\) and \(L>0\), form a compact rooted metric broom \(\Gamma_{m,a}\) from a common stem of length \(a\) and \(m\) terminal branches of length \(b=L-a\), with \(0\le a\le L\). Equip it with arclength measure, and define the path-integration operator on \(L^2(\Gamma_{m,a})\) by
\[
(T_{m,a}f)(x)=\int_{[o,x]}f(y)\,dy.
\]
The end cases are interpreted by collapsing zero-length edges. Its three natural Schatten norm functionals have **three distinct, uniquely maximizing stem fractions** \(t=a/L\):
\[
\operatorname*{argmax}_{0\le t\le1}\|T_{m,tL}\|_{\mathcal S_2}=\{0\},\qquad
\operatorname*{argmax}_{0\le t\le1}\|T_{m,tL}\|_{\mathcal S_4}=\left\{\frac{9m-\sqrt{3m(3m+4)}}{2(6m-1)}\right\},\qquad
\operatorname*{argmax}_{0\le t\le1}\|T_{m,tL}\|_{\mathcal S_\infty}=\left\{\frac12\right\}.
\]
The middle fraction is strictly between \(0\) and \(1/2\) for every allowed \(m\). Explicit norm identities are given below. Thus quadratic energy, fourth-order singular concentration, and worst-case amplification prescribe different locations for the branching vertex even when every root-to-leaf distance is held fixed.

## Assumptions and scope

A metric broom is the finite one-dimensional length space formed by identifying the far endpoint of one stem interval \([0,a]\) with the initial endpoints of \(m\) copies of \([0,b]\). The root \(o\) is the stem's initial endpoint. For \(a=0\), the rooted star has \(m\) branches of length \(L\); for \(a=L\), the collapsed branches yield a single interval of length \(L\). All \(L^2\) norms use non-normalized arclength measure; \(\mathcal S_p\) denotes the Schatten class on this Hilbert space, and \(\mathcal S_\infty\) the operator norm. The operator is compact and Hilbert–Schmidt since its integral kernel is the indicator that its input point precedes its output point along the rooted path. No result is asserted for unequal branch lengths or non-tree graphs.

## Proof

**Second and fourth singular moments.** The kernel of \(K=T_{m,a}T_{m,a}^*\) is the length of the common initial segment of the two rooted paths:
\[
K(x,y)=|[o,x]\cap[o,y]|.
\]
On two stem points with coordinates \(s,t\), this is \(\min(s,t)\). On a stem point of coordinate \(s\) and any branch point, it is \(s\). On two distinct terminal branches, it is \(a\), while on one terminal branch with local coordinates \(s,t\) it is \(a+\min(s,t)\). Integrating the diagonal and the square of this symmetric Hilbert–Schmidt kernel yields, without approximation,
\[
\begin{aligned}
\|T_{m,a}\|_{\mathcal S_2}^2
&=\operatorname{tr}K=\frac{a^2}{2}+mab+\frac{mb^2}{2}
=\frac{L^2}{2}\left[m-(m-1)t^2\right],\\
\|T_{m,a}\|_{\mathcal S_4}^4
&=\operatorname{tr}K^2=\frac{a^4}{6}+\frac{2m}{3}a^3b+m^2a^2b^2
 +\frac{2m}{3}ab^3+\frac{mb^4}{6}.
\end{aligned}
\]
The \(\mathcal S_2\) identity decreases strictly for positive \(t\). Writing \(M_4(t)=\|T_{m,tL}\|_{\mathcal S_4}^4/L^4\), differentiation and factorization give
\[
M_4'(t)=\frac{2(m-1)t}{3}\bigl((6m-1)t^2-9mt+3m\bigr).
\]
The quadratic equals \(3m\) at \(t=0\), equals \(-1/4\) at \(t=1/2\), and equals \(-1\) at \(t=1\). Since it opens upward, precisely one root lies in \((0,1/2)\) and the other exceeds \(1\). Its first root is
\[
t_4=\frac{9m-\sqrt{3m(3m+4)}}{2(6m-1)}.
\]
Hence \(M_4\) increases strictly on \((0,t_4)\) and decreases strictly on \((t_4,1)\), proving the unique fourth-order maximizer.

**Operator norm.** The mapping \(T_{m,a}\) is the inverse of differentiation \(u\mapsto u'\) on the rooted Sobolev space of continuous edgewise \(H^1\) functions with \(u(o)=0\). Accordingly,
\[
\|T_{m,a}\|^{-2}=\min_{\substack{u(o)=0\\u\ne0}}\frac{\int_{\Gamma_{m,a}}|u'|^2}{\int_{\Gamma_{m,a}}|u|^2}
=\lambda_1(\Gamma_{m,a}),
\]
where the associated self-adjoint Laplacian has a Dirichlet root, Neumann leaves, and Kirchhoff continuity/flux conditions at the junction. For \(0<a<L\), permutation symmetry splits the spectrum into a radial sector (same function on each terminal branch) and transverse sectors (Dirichlet at the junction, Neumann at the leaf). The transverse first wave number is \(\pi/(2b)\ge\pi/(2L)\). The radial eigenfunction of wave number \(k\) has stem component proportional to \(\sin(ks)\) and branch component proportional to \(\cos(k(b-s))\), yielding the characteristic equation
\[
\begin{aligned}
F(k,a)&=\cos(ka)\cos(kb)-m\sin(ka)\sin(kb)\\
&=\tfrac12\bigl[(m+1)\cos(kL)-(m-1)\cos(k(2a-L))\bigr]=0.
\end{aligned}
\]
For \(0<k\le\pi/(2L)\), put \(d=|2a-L|\le L\). Then
\[
\frac{\partial F}{\partial k}
=-\frac{m+1}{2}L\sin(kL)+\frac{m-1}{2}d\sin(kd)
\le -L\sin(kL)<0.
\]
Since \(F(0,a)=1\) and \(F(\pi/(2L),a)\le0\), there is exactly one radial root \(k_1(a)\) in this interval; it is strictly below the transverse spectrum and equals the first Laplacian wave number. The endpoint cases follow directly from the interval/identical-ray spectra.

For each fixed \(k\) in this interval, \(\cos(k(2a-L))\le1\), with equality only at \(a=L/2\). Thus \(F(k,a)\ge F(k,L/2)\), strictly off the midpoint for \(k>0\). Evaluating at the midpoint root shows \(k_1(a)>k_1(L/2)\) whenever \(a\ne L/2\). At the midpoint the characteristic equation simplifies to \(\cos(kL)=(m-1)/(m+1)\), so
\[
k_1(L/2)=\frac{2}{L}\arctan\frac1{\sqrt m},\qquad
\max_{0\le a\le L}\|T_{m,a}\|_{\mathcal S_\infty}
=\frac{L}{2\arctan(m^{-1/2})}.
\]
The three maximizers are pairwise distinct, as claimed.

## Verification

A standalone checker `checks/tree_hardy_checker.py` reproduces the symbolic \(\mathcal S_2\) and \(\mathcal S_4\) identities and the derivative factorization, verifies spectral-root and extremality formulas on several branching counts, and independently compares exact moment expressions against both rational quadrature and Nyström discretization of \(TT^*\). Running `python checks/tree_hardy_checker.py` with NumPy and SymPy installed gave `PASS 172 checks`. This numerical testing is corroborative; the preceding calculus, kernel integration, spectral decomposition and root comparison establish the infinite-dimensional statements.

## Relationship to prior work

Evans–Harris–Lang, *The approximation numbers of Hardy-type operators on trees* (first arXiv posting 2000-03-30), develops approximation-number theory for tree Hardy operators. Naimark–Solomyak, *Eigenvalue estimates for the weighted Laplacian on metric trees* (2000), provides metric-tree spectral estimates and decomposition methods. Rozhenko, *On characteristic functions of equilateral regular star-trees* (2012), gives characteristic-function formulas for star-tree Laplacians with different boundary conditions. These sources motivate the geometric and spectral setting, but the inspected sections do not state the present three-way sharp branch-location separation at fixed root-to-leaf length. The present comparison concerns the **same path-integration operator** under all three Schatten norms and includes exact global optimizers; generic approximation-number bounds and star-graph spectral characterizations do not by themselves assert this three-way optimization result.

## Limitations

The claim is for integer \(m\ge2\), equal leaf lengths and fixed common root-to-leaf length. It does not classify maximizing shapes of arbitrary metric trees, unequal-length brooms or values of every intermediate Schatten exponent. Mathematical correctness has been analytically checked and supported by reproducibility tests, but independent verification has not been performed. Historical priority remains subject to broader bibliographic examination, particularly treatments of the rooted Dirichlet–Neumann metric-tree Laplacian under alternate terminology.

## References

1. W. D. Evans, D. J. Harris and J. Lang, *The approximation numbers of Hardy-type operators on trees*, arXiv:math/0003215v1 (posted 2000-03-30), https://arxiv.org/abs/math/0003215.
2. K. Naimark and M. Solomyak, *Eigenvalue estimates for the weighted Laplacian on metric trees*, Proc. London Math. Soc. 80 (2000), 690–724, https://doi.org/10.1112/S0024611500012272.
3. N. A. Rozhenko, *On characteristic functions of equilateral regular star-trees*, Matematychni Studii 37 (2012), 65–75, https://doi.org/10.30970/ms.37.1.65-75.
