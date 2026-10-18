# Exact Euclidean distortion of alternating weighted four-cycle transportation spaces

## Finding
For every real \(t>0\), let \(M_t\) be four points with the shortest-path metric of the cyclic graph whose successive positive edge lengths are \(1,t,1,t\). Let \(F_t=\mathcal F(M_t)\) be its three-dimensional **real** Lipschitz-free space. Set \(s=\max\{t,t^{-1}\}\). Then
\[
\boxed{d_{\mathrm{BM}}(F_t,\ell_2^3)^2=\frac{(2s+1)(3s-1)}{(s+1)(2s-1)}.}
\]
Among all alternating ratios, the smallest possible distance is exactly \(5/3\), attained **only** for \(t=2\) and \(t=1/2\). The equal-edge cycle has distance \(\sqrt3\); the distance tends to \(\sqrt3\) as \(t\) tends to either zero or infinity. An explicit optimal positive definite quadratic form is given below.

## Assumptions and scope
For real finite-dimensional Banach spaces of the same dimension, \(d_{\mathrm{BM}}(X,Y)=\inf_T \|T\|\,\|T^{-1}\|\), where \(T\) ranges over all invertible linear maps. Lipschitz-free means the predual of real Lipschitz functions on the finite pointed metric, equivalently the transportation-cost space. Each indicated cycle edge is a shortest path between its endpoints: the alternative three-edge route is strictly longer. All scalars and linear maps here are real. Neither the complex case nor arbitrary four independent edge lengths are claimed.

## Proof
**1. A three-dimensional absolute norm.** Orient the cycle consecutively and write \(e_i=f(v_i)-f(v_{i+1})\) for the four signed edge differences of any real function on the vertices. They satisfy \(e_1+e_2+e_3+e_4=0\). Conversely every such quadruple integrates to a function, unique modulo constants. The graph shortest-path definition gives the exact Lipschitz norm
\[
\|f\|_{\mathrm{Lip}}=\max\{|e_1|,|e_2|/t,|e_3|,|e_4|/t\}.
\]
Define \(e_1=u+w\), \(e_3=w-u\), \(e_2=v-w\), and \(e_4=-v-w\). This is an invertible parametrization of the zero-sum hyperplane. Using \(\max(|x+y|,|x-y|)=|x|+|y|\), the dual space \(F_t^*\) is linearly isometric to \((\mathbb R^3,N_t)\), where
\[
N_t(u,v,w)=\max\left\{|u|+|w|,\frac{|v|+|w|}{t}\right\}.
\]
Finite-dimensional duality preserves multiplicative Banach–Mazur distance, and Euclidean space is self-dual. Also \(tN_t(u,v,w)=N_{1/t}(v,u,w)\), so the distance is unchanged when \(t\) is replaced by \(1/t\). It therefore suffices to prove the claimed formula for \(t=s\ge1\).

**2. Optimal ellipsoids may be chosen diagonal.** For any positive-definite quadratic form \(Q\), the squared Euclidean distortion associated with its norm is the least ratio \(\beta/\alpha\) such that
\[
\alpha N_t(x)^2\le Q(x)\le\beta N_t(x)^2\quad\text{for all }x\in\mathbb R^3.
\]
The norm is invariant under all eight independent coordinate sign changes. Averaging \(Q\) over this group preserves positivity and the two inequalities, and annihilates all off-diagonal coefficients. Thus the infimum over **all** Hilbertian norms equals that over \(Q(u,v,w)=a u^2+b v^2+c w^2\), with \(a,b,c>0\).

**3. Exact inner and outer ratios.** Define
\[
M(Q)=\max_{N_t(x)\le1}Q(x),\qquad
R(Q)=\max_{Q(x)\le1}N_t(x)^2.
\]
The squared distortion for \(Q\) is \(M(Q)R(Q)\). The unit ball \(N_t\le1\) has \(0\le|w|\le1\) and coordinate bounds \(|u|\le1-|w|\), \(|v|\le t-|w|\). Maximizing a positive quadratic first over the signs and coordinate magnitudes, then over \(z=|w|\), gives the convex function \(a(1-z)^2+b(t-z)^2+cz^2\). Its maximum on \([0,1]\) is at an endpoint; hence
\[
M(Q)=\max\{a+bt^2,\ b(t-1)^2+c\}.
\]
For \(R\), the maximum of \((|u|+|w|)^2\) on the ellipsoid \(Q\le1\) is \(1/a+1/c\) by Cauchy–Schwarz, and likewise the second term of \(N_t^2\). Therefore
\[
R(Q)=\max\left\{\frac1a+\frac1c,\frac{1/b+1/c}{t^2}\right\}.
\]
No diagonal approximation has been made in either identity.

**4. Solve the global minimax.** By scaling \(Q\), impose \(R(Q)=1\). Write \(h=1/c\); necessarily \(0<h<1\). The two constraints on \(R\) give \(a\ge(1-h)^{-1}\) and \(b\ge(t^2-h)^{-1}\). As \(M\) is increasing in \(a\) and \(b\), equality in both constraints is optimal at fixed \(h\). Conversely both equalities give \(R=1\). Thus the unrestricted optimal squared distortion is exactly
\[
\min_{0<h<1}\max\{A_t(h),B_t(h)\},
\quad A_t(h)=\frac1{1-h}+\frac{t^2}{t^2-h},
\quad B_t(h)=\frac{(t-1)^2}{t^2-h}+\frac1h.
\]
The first expression is strictly increasing in \(h\); the second is strictly decreasing because
\[
B'_t(h)=\frac{(t-1)^2}{(t^2-h)^2}-\frac1{h^2}<0
\]
for \(t\ge1\), \(0<h<1\) (equivalently \(h(t-1)<t^2-h\)). Their unique crossing solves
\[
A_t(h)-B_t(h)=0\quad\Longleftrightarrow\quad h=\frac{t}{2t+1}
\]
within the indicated interval; the remaining algebraic root \(h=t\) is inadmissible, apart from the endpoint outside the open interval. Substitution yields
\[
A_t\left(\frac{t}{2t+1}\right)=B_t\left(\frac{t}{2t+1}\right)
=\frac{(2t+1)(3t-1)}{(t+1)(2t-1)}.
\]
For the displayed coordinates an optimal quadratic form normalized by \(R=1\) is
\[
Q_t(u,v,w)=\frac{2t+1}{t+1}u^2
+\frac{2t+1}{t(2t-1)(t+1)}v^2
+\frac{2t+1}{t}w^2.
\]
Each lower/upper extremum is attained: the two terms defining \(M\) are witnessed respectively at \((u,v,w)=(1,t,0)\) and \((0,t-1,1)\), while the two terms defining \(R\) have their Cauchy–Schwarz equality witnesses. This establishes the global optimum over all real invertible linear maps.

**5. A strict optimal ratio.** Differentiating the rational expression in step 4 gives
\[
\frac{d}{dt}\frac{(2t+1)(3t-1)}{(t+1)(2t-1)}
=\frac{4t(t-2)}{(t+1)^2(2t-1)^2}.
\]
It decreases strictly for \(1\le t<2\) and increases strictly for \(t>2\); its unique minimizer on this half-line is \(t=2\), with squared distance \(25/9\). Reciprocity proves the two and only two minimizers over all positive ratios. The endpoint values and limits follow by substitution. \(\square\)

## Verification
The accompanying `check.py` uses only Python's standard library and exact rational arithmetic. Execute `python check.py` in the folder containing the file; the expected line is `ALTERNATING_CYCLE_RATIONAL_CHECK_OK 8`. It checks eight rational ratios, the quadratic-form coefficients, Cauchy–Schwarz constraints, all vertex endpoint energies, reciprocity, and comparisons with 39 finite grid points. These are arithmetic cross-checks, not an exhaustive real-parameter proof. The continuum and unrestricted-ellipsoid claims follow from the analytic argument above.

## Relationship to prior work
Hájek, Lancien and Pernecká (2015) give the Lipschitz-free space definition and foundational finite-dimensional dual viewpoint. Dilworth, Kutzarova and Ostrovskii (2018) analyze Lipschitz-free spaces of finite metric graphs and broader Banach–Mazur comparisons with \(\ell_1\) spaces. Alexander, Fradelizi, García-Lirola and Zvavitch (2019/2020), in a directly inspected paper, characterize the equal-edge four-cycle as the exceptional three-dimensional cube free-space ball and show that unequal weights lose the zonotope property; their focus is isometries, decompositions and volume products, not an exact Hilbert-distance formula. Ostrovska and Ostrovskii (2021) prove the weighted edge-quotient description of transportation-cost spaces, but do not calculate this alternating profile.

The publicly available exact real Hilbert-distance results for a **single** exceptional weighted cycle edge, including the four-cycle case, have a different weight multiset \((1,1,1,r)\), not the two-opposite-edge deformation \((1,t,1,t)\). Their formulas neither state a general arbitrary-weight four-cycle result nor imply the present alternating profile without new optimization. The uniform-edge cycle parity formula covers only \(t=1\); it supplies that boundary value, not the nonmonotone family or its two optimal ratios. Other geometric constants, such as operator numerical radii of weighted shifts, involve different spaces and invariants.

## Limitations
Only real spaces and four-cycle edge patterns with two alternating lengths are treated. No uniqueness among all nonsymmetric optimal Euclidean quadratic forms is asserted, nor any assertion for arbitrary four-edge weights or higher cycles. The finite program validates rational instances only. The literature assessment cannot rule out an equivalent calculation hidden in unindexed older work or a more general ellipsoid theorem whose implications have not been explicitly tabulated. No independent mathematical or bibliographic validation has been performed.

## References
1. P. Hájek, G. Lancien, E. Pernecká, *Approximation and Schur properties for Lipschitz free spaces over compact metric spaces*, arXiv:1507.02701v1, first public 2015-07-09; Section 1, primary MSC 46B20.
2. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814v1, 2018; Sections 1–3.
3. M. Alexander, M. Fradelizi, L. C. García-Lirola, A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642v2, 2020, Sections 2–4 (original preprint 2019).
4. S. Ostrovska, M. I. Ostrovskii, *Isometric structure of transportation cost spaces on finite metric spaces*, arXiv:2112.02689v1, 2021; Proposition 1.5.
5. *Exact Euclidean distortion of a one-defect four-cycle transportation space*, publicly indexed 2026 research result, identifier `1b1292e047f1`; applies to the distinct pattern \((1,1,1,r)\).
6. *Opposite parity laws for exact Hilbert distortion of one-edge weighted cycles*, publicly indexed 2026 research result, identifier `38cb69cb8edd`; applies to one exceptional edge.
7. *Scalar-field parity in Euclidean distortion of cycle transportation spaces*, publicly indexed 2026 research result, identifier `13d7bdc76366`; covers uniform-edge cycles.
