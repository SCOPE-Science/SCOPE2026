# Sharp quadratic least-squares stability on complete metric graphs

## Finding
For each integer \(n\ge3\), replace every edge of the complete graph \(K_n\) by a unit interval with Lebesgue arclength measure. Let \(P_n\) be the real \(L^2\)-orthogonal projection onto functions continuous at graph vertices and of degree at most two on each edge, without derivative-matching conditions. For a vertex \(v\), put \(N_n=\sup_{\|f\|_{L^\infty}\le1}|(P_nf)(v)|\). Then this vertex-evaluation norm, independent of \(v\), is exactly
\[
N_n=\frac{1}{3n-2}\left[2n+\frac{4(9n^2-8n+4)^{3/2}}{25n^2}+\frac{(n-2)(5+2\sqrt5)}5\right].
\]
It is strictly increasing for every real parameter \(n\ge3\), when the displayed formula is viewed as a real function, and has the sharp integer threshold \(N_n>5/2\) if and only if \(n\ge6\). For every integer \(n\ge6\), the **full**, attained operator norm is exactly
\[
\|P_n\|_{L^\infty\to L^\infty}=N_n.
\]
Every vertex is norming; no interior edge point is norming. Furthermore,
\[
\sup_{n\ge6}\|P_n\|=\frac{61}{25}+\frac{2\sqrt5}{15},\qquad
\lim_{n\to\infty}n\left(\frac{61}{25}+\frac{2\sqrt5}{15}-\|P_n\|\right)=\frac{24}{25}+\frac{8\sqrt5}{45}.
\]
The first supremum is not attained for any finite \(n\). Among all inputs satisfying \(0\le f\le1\), the exact largest possible downward excursion of \(P_nf\), at a vertex for every \(n\ge3\) and globally for \(n\ge6\), is \((N_n-1)/2\).

## Assumptions and scope
The graph is finite, simple, complete, connected, and has precisely \(n\ge3\) vertices. Its edges are separate unit intervals; each edge is integrated once with ordinary arclength and has density one. The approximation space consists of globally continuous, edgewise quadratic real functions: function values, but not derivatives, match at vertices. Input functions belong to real \(L^\infty\) on the disjoint edge interiors, identified up to arclength-null sets; output functions have their canonical continuous representatives. The asserted full operator norm applies to \(n\ge6\). For \(n=3,4,5\), only exact **vertex** evaluation norms and their positivity defects are asserted, not the unrestricted full operator norm.

## Proof
**1. Orthogonal edge decomposition.** On the oriented unit interval write
\[
h(t)=t(1-t),\qquad \phi(t)=1-t-\frac52h(t),\qquad \psi(t)=t-\frac52h(t).
\]
Direct integration gives \(\int_0^1 h^2=1/30\), \(\int_0^1\phi h=\int_0^1\psi h=0\), \(\int_0^1\phi^2=\int_0^1\psi^2=1/8\), and \(\int_0^1\phi\psi=-1/24\). Every continuous edgewise quadratic has a unique representation on each edge \(e=ij\) as \(U_i\phi+U_j\psi+c_eh\), oriented from \(i\) to \(j\). Its nodal and edge-bubble subspaces are mutually orthogonal. The nodal Gram matrix has diagonal \((n-1)/8\) and off-diagonal \(-1/24\), hence
\[
H=\frac{(3n-2)I-J}{24},\qquad
H^{-1}_{vv}=(2n-1)\beta_n,\quad H^{-1}_{vw}=\beta_n\quad(v\ne w),\qquad
\beta_n=\frac{12}{(3n-2)(n-1)}.
\]
Here \(J\) is the all-ones matrix. The inverse follows by splitting into the constant-vector and mean-zero eigenspaces, whose positive eigenvalues are \((n-1)/12\) and \((3n-2)/24\).

**2. Reproducing kernel at a vertex.** For \(f\in L^\infty\), the functional \(f\mapsto(P_nf)(v)\) has an edgewise polynomial integral kernel. On an edge incident to \(v\), with its coordinate chosen so that \(v\) is at \(t=0\), it is \(\beta_n q_n(t)\), where
\[
q_n(t)=(2n-1)\phi(t)+\psi(t)=5nt^2+(2-7n)t+(2n-1).
\]
On every other edge it is \(\beta_n p(t)\), where \(p(t)=\phi(t)+\psi(t)=1-5t(1-t)\). These expressions follow directly by applying the displayed inverse Gram matrix to the nodal evaluation vector. There are \(n-1\) incident edges and \((n-1)(n-2)/2\) nonincident edges. Consequently,
\[
N_n=\frac{12}{3n-2}\left[\int_0^1|q_n(t)|\,dt+\frac{n-2}{2}\int_0^1|p(t)|\,dt\right].
\]

**3. Exact absolute integrals.** The discriminant of \(q_n\) is \(\Delta_n=9n^2-8n+4\), and its roots are \(r_\pm=(7n-2\pm\sqrt{\Delta_n})/(10n)\). For \(n\ge3\), both roots lie strictly between zero and one; \(q_n\) is negative exactly between them. If a positive-leading quadratic \(a(t-r_-)(t-r_+)\) has two such roots, its negative-area integral is \(a(r_+-r_-)^3/6\). With \(\int q_n=n/6\), this gives
\[
\int_0^1|q_n(t)|\,dt=\frac n6+\frac{\Delta_n^{3/2}}{75n^2}.
\]
Similarly the two roots of \(p\) are \((5\pm\sqrt5)/10\); because \(\int_0^1p=1/6\),
\[
\int_0^1|p(t)|\,dt=\frac{5+2\sqrt5}{30}.
\]
Substitution proves the stated exact formula for \(N_n\). The bounded sign function of the displayed vertex kernel attains this evaluation norm.

**4. Strict monotonicity, threshold, and asymptotics.** Regard the formula as a differentiable function of real \(n\ge3\). Direct differentiation, with \(\Delta_n=9n^2-8n+4\), gives
\[
\frac{dN_n}{dn}=\frac{8\bigl[5\sqrt5\,n^3+(9n^2-22n+8)\sqrt{\Delta_n}\bigr]}{25n^3(3n-2)^2}>0,
\]
since \(9n^2-22n+8=(n-2)(9n-4)\ge0\) for \(n\ge3\). The exact neighboring values are \(N_5=1+6\sqrt5/65+2268\sqrt{21}/8125<5/2\) and \(N_6=1+\sqrt5/10+7\sqrt{70}/45>5/2\); these inequalities follow, for example, from rational square-root brackets \(2.236<\sqrt5<2.237\), \(4.582<\sqrt{21}<4.583\), and \(8.366<\sqrt{70}<8.367\). Monotonicity yields the claimed threshold. Expanding \(\Delta_n^{3/2}/n^2\) at infinity, or applying the binomial expansion with a controlled remainder, yields
\[
N_n=\frac{61}{25}+\frac{2\sqrt5}{15}-\frac1n\left(\frac{24}{25}+\frac{8\sqrt5}{45}\right)+O(n^{-2}).
\]

**5. Global norm and absence of interior norming points.** Let \(\|f\|_\infty\le1\), let \(U_i=(P_nf)(i)\), and let \(c_e\) be its edge-bubble coefficient. Step 1 and orthogonality give \(c_e=30\int_0^1f_e(t)h(t)\,dt\); hence \(|c_e|\le5\). The vertex calculation gives \(|U_i|\le N_n\). Put \(S(t)=|\phi(t)|+|\psi(t)|\). A direct three-interval sign check, with division points \(2/5\) and \(3/5\), establishes
\[
S(t)+2h(t)\le1 \qquad(0\le t\le1),
\]
with strict inequality for \(0<t<1\): on the first interval the deficit is \(2t^2\), on the middle it is \(2-7t(1-t)\), and on the last it is \(2(1-t)^2\). If \(n\ge6\), then \(N_n>5/2\), so on each edge
\[
|(P_nf)_e(t)|\le N_nS(t)+5h(t)\le N_n\bigl(S(t)+2h(t)\bigr)\le N_n.
\]
The inequality is strict for interior points. A vertex sign-kernel input supplies equality. This proves the exact full norm and the stated norming-location assertion for every \(n\ge6\).

**6. Positivity defect.** Constants belong to the spline space, so \(P_n1=1\). For any evaluation with sharp norm \(N\), the substitution \(g=2f-1\) shows that the infimum over \(0\le f\le1\) equals \((1-N)/2\), attained by \(f=(1-\operatorname{sgn}K)/2\), where \(K\) is the reproducing kernel at that evaluation. Apply the vertex formula for every \(n\ge3\), and the full norm formula for \(n\ge6\).

## Verification
Run `python verify.py` with SymPy and mpmath installed; `requirements.txt` lists the dependencies. The program independently builds the **original**, non-orthogonal nodal-plus-edge-bubble Gram matrices for complete graphs of orders three through eight, inverts those exact rational matrices, checks 83 kernel polynomials edge by edge, and compares independently integrated absolute kernels at 45-digit precision. It also checks all elementary Gram identities, the symbolic derivative, the asymptotic limits, the two integer threshold values, and the three polynomial inequalities used for edge-interior control. The unrestricted claims are established in the preceding proof; finite matrix checks are not presented as an infinite proof.

## Relationship to prior work
Classical work on spline \(L^2\) projection investigates uniform norm bounds on an interval; Kayumov's publicly deposited 2004 thesis discusses linear and higher-order spline bounds but does not treat the junction coupling of a complete metric graph. Arioli and Benzi develop mass/stiffness matrices and linear finite elements on quantum graphs; their linear-element constructions do not imply this quadratic-graph endpoint formula. Diening, Storn and Tscherpel study weighted \(L^p\) and Sobolev stability for Lagrange finite elements under mesh regularity hypotheses, rather than exact one-element-per-edge graph constants. These sources motivate the sensitivity question and supply relevant comparison machinery, not the displayed sharp formula. Earlier independently published equivalent calculations under alternative terminology cannot be categorically excluded.

## Limitations
The full \(L^\infty\) norm is established here for \(n\ge6\), not for complete graphs of orders three, four, or five; their vertex evaluation norms are nevertheless exact. This does not cover weighted edges, non-unit lengths, nonconstant densities, other graph families, derivative continuity at vertices, or polynomial degrees other than two. Norm attainment refers to bounded measurable inputs; the kernel-sign extremizers generally need not be continuous.

## References
1. A. Kayumov, *Least-squares approximation by second-order L-splines*, public arXiv version dated 2004-08-30, https://arxiv.org/abs/math/0408418.
2. M. Arioli and M. Benzi, *A finite element method for quantum graphs*, IMA Journal of Numerical Analysis 38 (2018), 1119–1163; openly accessible author manuscript https://cerfacs.fr/wp-content/uploads/2017/03/revised4-1-ARIOLI.pdf; DOI 10.1093/imanum/drx029.
3. L. Diening, J. Storn and T. Tscherpel, *On the Sobolev and \(L^p\)-stability of the \(L^2\)-projection*, preprint first posted 2020-08-04, https://arxiv.org/abs/2008.01801.
