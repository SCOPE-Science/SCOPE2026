# Sharp rim-edge deletion and unrestricted rigidity in priced wheel diffusion

## Finding

Fix an integer \(n\ge3\). Construct the wheel \(W_n\) from a cycle on rim vertices \(0,\ldots,n-1\) and one hub \(h\), joining \(h\) to each rim vertex. Assign independently chosen nonnegative conductances \(x_i\) to spokes \(\{h,i\}\) and \(y_i\) to rim edges \(\{i,i+1\pmod n\}\). For any positive prices \(P,Q\) and positive budget \(B\), maximize the second-smallest eigenvalue \(\lambda_2(L)\) of the corresponding weighted Laplacian subject to
\[
P\sum_{i=0}^{n-1}x_i+Q\sum_{i=0}^{n-1}y_i\le B.
\]
Set \(\alpha_n=2-2\cos(2\pi/n)\). Then the exact optimal value is
\[
\boxed{\lambda_*(n,P,Q,B)=
\begin{cases}
\dfrac{(n+1)\alpha_n B}{n(\alpha_n P+nQ)},&Q<\alpha_n P,\\[4pt]
\dfrac{B}{nP},&Q\ge\alpha_n P.
\end{cases}}
\]
For \(Q<\alpha_nP\), the **only** global optimizer, even without a symmetry restriction, has
\[
x_i=\frac{\alpha_n B}{n(\alpha_nP+nQ)},\qquad
 y_i=\frac{B}{\alpha_nP+nQ}\quad(0\le i<n).
\]
For \(Q>\alpha_nP\), the **only** global optimizer has
\[
x_i=\frac{B}{nP},\qquad y_i=0\quad(0\le i<n).
\]
At equality \(Q=\alpha_nP\), the optimal value remains \(B/(nP)\), but optimizers are not unique: every cyclically symmetric allocation satisfying
\[
0\le y\le\frac{B}{P(n+1)\alpha_n},\qquad
x=\frac{B}{nP}-\alpha_ny
\]
is optimal. No assertion is made here that these exhaust all nonsymmetric boundary optimizers.

For equal prices \(P=Q\), every optimal design deletes every rim edge when \(n\ge7\); the unique optimum uses all rim edges for \(3\le n\le5\). At \(n=6\), both support patterns (and a continuum between them) are optimal. Further, for fixed \(\kappa>0\) and the critical price sequence \(Q_n/P=\kappa/n^2\),
\[
\boxed{\lim_{n\to\infty}\frac{nP\lambda_*(n,P,Q_n,B)}B
=\max\!\left\{1,\frac{4\pi^2}{\kappa}\right\}.}
\]

## Assumptions and scope

All graph vertices have unit heat capacity or unit Markov stationary mass; \(L\) is the standard symmetric combinatorial Laplacian, with each edge \(\{u,v\}\) of conductance \(w\) contributing \(w(e_u-e_v)(e_u-e_v)^\mathsf T\). The second-smallest eigenvalue is counted with multiplicity and measures the slowest nonconstant continuous-time diffusion decay rate. Prices are per unit edge conductance and identical within each of the two edge classes, but design variables are individually free. Zero conductance is permitted, and the budget is a total, not a per-vertex, restriction. The wheel convention includes \(W_3\cong K_4\).

## Proof

**1. A symmetric optimizer exists.** The function \(L\mapsto\lambda_2(L)=\min_{v\perp\mathbf1,\,\|v\|=1}v^\mathsf TLv\) is concave in \(L\). Averaging any feasible design over the rotations and reflections of the rim preserves its price and cannot lower \(\lambda_2\). Because positive uniform spoke weights give a connected graph and positive value, every optimum exhausts its budget by positive homogeneity. Thus a symmetric optimum has constant spoke weight \(x\ge0\), rim weight \(y\ge0\), and \(n(Px+Qy)=B\).

**2. Exact two-branch spectrum.** On the two-dimensional subspace constant along the rim, the nonconstant eigenvalue of \(L\) is \((n+1)x\), with eigenvector \((-n,1,\ldots,1)\). The orthogonal rim modes have hub coordinate zero and Fourier eigenvalues
\[
x+y\bigl(2-2\cos(2\pi k/n)\bigr),\qquad k=1,\ldots,n-1.
\]
The smallest is \(x+\alpha_ny\). Therefore
\[
\lambda_2(L)=\min\{(n+1)x,\,x+\alpha_ny\}.
\]

**3. Price transition.** Using \(x=B/(nP)-(Q/P)y\), the two quantities in the minimum become a strictly decreasing affine function of \(y\) and the affine function \(B/(nP)+(\alpha_n-Q/P)y\). If \(Q>\alpha_nP\), the minimum is uniquely maximized at \(y=0\). If \(Q<\alpha_nP\), it is uniquely maximized at their intersection \(y=nx/\alpha_n\). Solving the budget equation gives the stated positive weights and optimal value. At equality, the second branch is constant, and the first remains at least that constant exactly for the displayed interval of \(y\). This proves optimal values and symmetric optimizers.

**4. Spectral rigidity without imposing symmetry.** The following elementary equality principle is useful. Let \(L\) be any globally optimal Laplacian, and let \(\bar L\) denote its average under the rim dihedral group. Let \(E\) be the \(\lambda_*\)-eigenspace of \(\bar L\) inside \(\mathbf1^\perp\). For a unit vector \(v\in E\), every group conjugate \(L_g\) satisfies \(v^\mathsf TL_gv\ge\lambda_*\), while their average equals \(v^\mathsf T\bar Lv=\lambda_*\). Every term is therefore equal. Positivity of \(L-\lambda_* I\) on \(\mathbf1^\perp\) implies \(Lv=\lambda_*v\). Hence every vector in \(E\) is also an eigenvector of \(L\).

If \(Q>\alpha_nP\), the symmetric optimum has all rim conductances zero. Since the average of nonnegative rim conductances is zero, every individual \(y_i=0\). Now \(E\) consists of all vectors with hub coordinate zero and rim coordinates summing to zero. Applying the eigenvector identity to \(e_i-e_j\) and inspecting its hub coordinate gives \(x_i=x_j\) for all \(i,j\); the budget forces the claimed uniform spoke weights.

If \(Q<\alpha_nP\), the symmetric optimum has a repeated spectral minimum contributed by both branches. The radial vector \((-n,1,\ldots,1)\in E\), whose rim equation is \((n+1)x_i=\lambda_*\), forces every \(x_i=x\). The complex Fourier vector \(v_i=\omega^i\), \(v_h=0\), with \(\omega=e^{2\pi\mathrm i/n}\), is also in the complexification of \(E\), and obeys \(Lv=\lambda_*v\). Subtracting the equal-spoke and equal-rim reference eigenvalue equation shows that the edge fluxes
\[
z_i=(y_i-y)(v_{i+1}-v_i)=(y_i-y)(\omega-1)\omega^i
\]
are constant in \(i\). Since \(y_i-y\) is real and \(\omega\notin\mathbb R\) for \(n\ge3\), a nonzero constant cannot have that form at two consecutive edges. Thus each \(z_i=0\), and \(y_i=y\) for every \(i\). This proves the two asserted unrestricted uniqueness statements.

**5. Natural thresholds and limit.** The values \(\alpha_5>1\), \(\alpha_6=1\), \(\alpha_7<1\), and strict decrease of \(\alpha_n\) in \(n\) give the equal-price classification. Finally \(n^2\alpha_n\to4\pi^2\). In the positive-rim regime substituting \(Q_n=\kappa P/n^2\) into the optimal formula gives \(nP\lambda_*/B\to4\pi^2/\kappa\); in the zero-rim regime it equals \(1\). At the crossover both limits agree. This yields the critical-window formula.

## Verification

Run `python3 verify.py` in a directory containing the accompanying verifier. It uses only the Python standard library, checks exact rational special cases, recomputes finite Laplacian eigenvalues using Jacobi rotations, checks budget and branch identities, tests feasible unrestricted asymmetric designs, and evaluates the boundary and asymptotic regimes. These finite numerical tests supplement the all-parameter mathematical proof; they do not establish its infinite quantifiers or prove novelty.

## Relationship to prior work

The semidefinite formulation of optimizing continuous-time Markov-process mixing under linear edge prices is established by Sun, Boyd, Xiao and Diaconis (2006). Boyd, Diaconis, Parrilo and Xiao (2007) derive the discrete-time fastest-mixing wheel chain under stochastic row constraints; that is a different objective and does not imply the present priced continuous-time algebraic-connectivity theorem. Wan and collaborators (2008) study structural properties of optimal algebraic-connectivity designs; their general results do not provide this wheel-specific price cutoff or the repeated-eigenspace rigidity proof. This result claims only the explicit priced wheel classification, unrestricted uniqueness away from the threshold, and critical scaling; no general optimization framework is claimed as new.

## Limitations

The design uses symmetric continuous-time diffusion, identical within-class edge prices, unit vertex capacities, and nonnegative unrestricted individual conductances; it is not a claim about discrete-time second-largest *absolute* eigenvalues, adaptive control, fixed edge counts, or robustness under a different norm. At the threshold, symmetric optimizers are exhibited but nonsymmetric boundary optimizers are not exhaustively classified. Specialized earlier wheel-design results not identified in the inspected literature could overlap the present formulation.

## References

1. J. Sun, S. Boyd, L. Xiao and P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review **48** (2006), 681–699. DOI: 10.1137/S0036144504443821. Freely accessible full text: https://stanford.edu/~boyd/papers/pdf/fmmp.pdf . Published online 2006-11-02.
2. S. Boyd, P. Diaconis, P. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1, public 2007-09-06, https://arxiv.org/abs/0709.0955 , particularly the wheel example in Section 5.3.3.
3. Y. Wan, S. Roy, X. Wang, A. Saberi, T. Yang, M. Xue and B. Malek, *On the Structure of Graph Edge Designs That Optimize the Algebraic Connectivity*, IEEE CDC (2008), 805–810. DOI: 10.1109/CDC.2008.4738734. Accessible author-posted full text: https://www.researchgate.net/publication/224367365_On_the_structure_of_graph_edge_designs_that_optimize_the_algebraic_connectivity .
4. M. Fiedler, *Laplacian of Graphs and Algebraic Connectivity*, Banach Center Publications **25** (1989). Full text not available in the present comparison; cited as relevant foundational context, not as verified noncoverage.
