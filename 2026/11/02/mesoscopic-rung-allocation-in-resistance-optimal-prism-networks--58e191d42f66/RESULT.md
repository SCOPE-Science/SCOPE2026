# Mesoscopic rung allocation in resistance-optimal prism networks

## Finding
For every integer \(n\ge3\), let the circular ladder (prism) be \(C_n\square K_2\). Each of its \(2n\) ring edges costs \(P>0\) per unit conductance; each of its \(n\) rungs costs \(Q>0\) per unit conductance. With a positive total budget \(B\), allow **all \(3n\) edge conductances to vary independently**, including the possibility of zero conductances, and minimize the sum \(\mathcal K_n\) of effective resistances over unordered vertex pairs, with disconnected allocations assigned infinite cost.

The unique global optimizer has a common ring-edge conductance \(x_n>0\) and common rung conductance \(y_n>0\). Define \(\mu_k=4\sin^2(\pi k/n)\) for \(0\le k<n\), \(a_n=(n^2-1)/12\), and \(t_n=y_n/x_n\). Then \(t_n\) is the unique positive solution of
\[
Q a_n+\sum_{k=0}^{n-1}\frac{Q\mu_k-4P}{(\mu_k+2t_n)^2}=0,
\]
and the exact optimal weights are
\[
x_n=\frac{B}{n(2P+Qt_n)},\qquad y_n=t_nx_n.
\]
The minimum trace and Kirchhoff index are respectively
\[
T_n=\operatorname{tr}(L^+)=\frac{n(2P+Qt_n)}B\left(a_n+\sum_{k=0}^{n-1}\frac1{\mu_k+2t_n}\right),\qquad\mathcal K_n=2nT_n.
\]
For any **fixed** \(P,Q,B>0\), as \(n\to\infty\), write
\[
s_*=\left(\frac{18P^2}{Q^2}\right)^{1/3}.
\]
Then the rung-to-ring allocation exhibits a fractional-power boundary layer:
\[
\boxed{n^{2/3}\frac{y_n}{x_n}\longrightarrow s_*},\qquad
\boxed{n^{5/3}y_n\longrightarrow\frac{Bs_*}{2P}}.
\]
Moreover, the **two-term sharp optimum** is
\[
\boxed{T_n=\frac{P}{6B}n^3+\frac{Qs_*}{4B}n^{7/3}+o(n^{7/3})},
\]
so \(\mathcal K_n=(P/(3B))n^4+(Qs_*/(2B))n^{10/3}+o(n^{10/3})\). For equal edge prices \(P=Q\), the ratio of the optimal Kirchhoff index to the index of an equal-conductance allocation tends to exactly \(2/3\).

## Assumptions and scope
Vertices are \((i,\ell)\), with \(i\in\mathbb Z/n\mathbb Z\) and \(\ell\in\{0,1\}\); edges join \((i,\ell)\) to \((i+1,\ell)\) in each ring and \((i,0)\) to \((i,1)\) across each rung. The integer restriction \(n\ge3\) avoids double edges. The graph is undirected, edge conductances are real and nonnegative, and the scalar \(P\) or \(Q\) applies to each individual edge in its class. Budget expenditure equals \(B\). There are no pre-imposed equal-weight constraints: class equality is a conclusion. The limit holds with \(P,Q,B\) fixed, not varying with \(n\). We use \(L^+\) for the Moore--Penrose inverse of the connected weighted Laplacian, and the standard identity \(\mathcal K_n=(2n)\operatorname{tr}(L^+)\).

## Proof
**1. Unrestricted uniqueness and forced symmetry.** On the mean-zero vertex subspace, the Laplacian \(L\) is positive definite for every connected allocation. For any symmetric perturbation \(H\ne0\) of this restricted matrix, the second directional derivative of \(\operatorname{tr}(L^{-1})\) is
\[
2\operatorname{tr}(L^{-1}HL^{-1}HL^{-1})>0.
\]
Indeed, this is the trace of a positive-semidefinite, nonzero square conjugated by a positive-definite matrix. Distinct edge conductances determine distinct Laplacians, since each graph edge gives a distinct off-diagonal matrix entry. The objective is thus strictly convex on the convex connected domain of feasible conductances. It attains a minimum: the budget simplex is compact and the trace tends to infinity when a nonzero Laplacian eigenvalue tends to zero. This minimum is unique. Rotation, reflection, and ring interchange preserve objective and prices; by uniqueness, their edge orbits have constant conductances \(x_n\) and \(y_n\). Neither orbit can have zero weight: with all rungs absent the two rings disconnect; with all ring edges absent there are \(n\) separate two-vertex components. Thus \(x_n,y_n>0\).

**2. Exact reduction.** The class budget is \(2nPx_n+nQy_n=B\). The two ring-symmetric/antisymmetric vertex subspaces diagonalize \(L\). The symmetric block is \(x_n L(C_n)\), with eigenvalues \(x_n\mu_k\); its sole zero eigenvalue occurs at \(k=0\). The antisymmetric block is \(x_nL(C_n)+2y_nI\), with eigenvalues \(x_n\mu_k+2y_n\). Consequently,
\[
\operatorname{tr}(L^+)=\frac1{x_n}\sum_{k=1}^{n-1}\frac1{\mu_k}+\sum_{k=0}^{n-1}\frac1{x_n\mu_k+2y_n}.
\]
The cycle trigonometric identity \(\sum_{k=1}^{n-1}\mu_k^{-1}=(n^2-1)/12\) gives the stated objective. Put \(t=y/x\), eliminate \(x=B/[n(2P+Qt)]\), and minimize
\[
\Phi_n(t)=\frac nB(2P+Qt)\{a_n+F_n(t)\},\qquad F_n(t)=\sum_{k=0}^{n-1}\frac1{\mu_k+2t}.
\]
Both endpoints \(t\downarrow0\) and \(t\to\infty\) have infinite objective. Differentiation yields
\[
\frac Bn\Phi_n'(t)=Qa_n+\sum_{k=0}^{n-1}\frac{Q\mu_k-4P}{(\mu_k+2t)^2}.
\]
The derivative is negative near zero and positive at infinity, hence has a root. It has exactly one positive root: under the strictly monotone reparametrization \(t\mapsto y=Bt/[n(2P+Qt)]\), the objective is strictly convex along the affine two-class budget segment, so it has just one stationary point.

**3. Exact resolvent and fractional scaling.** For \(t>0\), define \(d(t)=\sqrt{t(t+2)}\) and \(\rho(t)=1+t-d(t)\in(0,1)\). Expanding the Poisson kernel and summing over the \(n\)-th roots of unity gives the exact identity
\[
F_n(t)=\frac{n}{2d(t)}\frac{1+\rho(t)^n}{1-\rho(t)^n}.
\]
Fix \(P,Q,B>0\), and abbreviate \(t_n\) as \(t\). Subtract the exact symmetric-mode baseline \(2Pna_n/B\) from the objective. The nonnegative excess is
\[
\Delta_n(t)=\frac nB\{Qta_n+(2P+Qt)F_n(t)\}.
\]
For each fixed \(s>0\), testing \(t=sn^{-2/3}\) in the displayed resolvent formula gives \(\Delta_n=O(n^{7/3})\). Minimality gives this upper bound for the optimizer. Since \(\Delta_n(t_n)\ge(n/B)Qt_na_n\), with \(a_n\sim n^2/12\), it follows that \(t_n\le Cn^{-2/3}\) for large \(n\). On the other hand, \(F_n(t)\ge n/(2\sqrt{t(t+2)})\), so for \(t_n\le1\), the excess has lower bound \(P n^2/(B\sqrt{3t_n})\). The same upper bound thus yields \(t_n\ge cn^{-2/3}\) for some \(c>0\). Therefore \(s_n=n^{2/3}t_n\) remains in a compact subset of \((0,\infty)\).

Uniformly for \(s\) in any such compact interval, \(n\sqrt{sn^{-2/3}}\to\infty\), and \(\rho(sn^{-2/3})^n\to0\) exponentially in \(n^{2/3}\). The closed formula therefore gives
\[
\frac{\Delta_n(sn^{-2/3})}{n^{7/3}}\longrightarrow
\frac1B\left(\frac{Qs}{12}+\frac{P}{\sqrt{2s}}\right)
\]
uniformly on compacts. The limiting function has exactly one minimizer, obtained from
\[
\frac Q{12}=\frac{P}{2\sqrt2}s^{-3/2},\qquad s=s_*=(18P^2/Q^2)^{1/3}.
\]
Compactness and uniqueness force \(s_n\to s_*\). At this value the limiting objective equals \(Qs_*/(4B)\), proving the two-term expansion. The conductance formulas immediately give \(n^{5/3}y_n\to Bs_*/(2P)\).

**4. Equal-price comparison.** For \(P=Q\), a uniform allocation has \(x=y=B/(3nP)\). Its trace is \((3nP/B)(a_n+F_n(1))=Pn^3/(4B)+O(n^2)\), since \(F_n(1)=O(n)\). The optimum has leading trace \(Pn^3/(6B)\); division proves the ratio \(2/3\).

## Verification
Run `python VERIFY.py` with Python, NumPy, SciPy, and SymPy. The verifier obtains \(57\) successful grouped checks, including \(15\) exact rational full-Laplacian trace identities, \(18\) unrestricted numerical minimizations, \(20\) exact-formula-to-Fourier-sum comparisons, the exact cube example, and \(3\) large-size scaling comparisons. In the eight-vertex cube case \(n=4\), \(P=Q=B=1\), symmetry gives \(t_4=1\), \(x_4=y_4=1/12\) and \(T_4=29\). The numerical scaling examples approach the proved coefficient \(18^{1/3}\) when \(P=Q\). The finite tests are supplementary; the limit for all \(n\) is proved analytically above.

## Relationship to prior work
Ghosh, Boyd, and Saberi's 2006 proceedings paper introduces and studies minimum-total-resistance conductance design; the longer 2008 treatment proves convexity, optimality conditions, and analyzes trees, wheels, and barbells. Neither inspected paper gives the circular-ladder two-class optimum or its fractional-power limit. Zhang and Yang (2006) give spectral Kirchhoff-index formulas for unweighted circulant graphs, and Cinkir's 2015 ladder and 2017 prism works concern resistance formulas for fixed unit edge weights. Those results motivate the prism geometry and permit spectral evaluations, but do not assert the free-weight price optimum or its asymptotic exponent. A published 2026 research record on the finite-ladder spanning-tree rung kernel addresses edge inclusion in a distinct, noncyclic ensemble; it does not optimize the trace pseudoinverse. Distinct price classes, free per-edge weights, and the asymptotic optimizer are essential additions here.

## Limitations
The asymptotics require fixed positive prices and budget. They do not describe price scales varying with \(n\), rectangular grid layers of growing width, random edge failures, or shortest-path performance. Earlier specialized work on optimally weighted prisms cannot be ruled out exhaustively, especially where only abstracts could be inspected; independent validation has not been undertaken. Its trace asymptotics are not finite-size error bounds with explicit constants, although the exact scalar minimization formula is available for each \(n\).

## References
1. A. Ghosh, S. Boyd, A. Saberi, *Minimizing Effective Resistance of a Graph*, Proceedings of MTNS 2006, Kyoto, July 24--28, 2006, session TuP12.2, pp. 1185--1196. Primary full text: https://stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf.
2. A. Ghosh, S. Boyd, A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50(1):37--66, 2008, DOI 10.1137/050645452. Full text: https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf.
3. H. Zhang, Y. Yang, *Resistance distance and Kirchhoff index in circulant graphs*, International Journal of Quantum Chemistry 107:330--339, first published September 5, 2006, DOI 10.1002/qua.21068.
4. Z. Cinkir, *Effective Resistances, Kirchhoff index and Admissible Invariants of Ladder Graphs*, arXiv:1503.06353, March 21, 2015.
5. Z. Cinkir, *Effective Resistances and Kirchhoff Index of Prism Graphs*, arXiv:1704.03429, April 11, 2017 (abstract consulted; full text not inspected).
6. *Exact finite-volume rung kernel and boundary-bulk split for weighted ladder spanning trees*, publicly available mathematical research record, October 4, 2026, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-finite-volume-rung-kernel-and-boundary-bulk-split-for-weig--647fc3f7ee8c.
