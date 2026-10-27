# Exact current fluctuations for asymmetric periodic permeable membranes

## Finding

For a one-dimensional diffusion separated into equal cells by identically biased permeable membranes, the full scaled cumulant-generating function (SCGF) of the net membrane-crossing number is given by an explicit scalar transcendental equation. It implies an exact large-deviation principle, an affinity fluctuation symmetry and an explicit asymptotic diffusion coefficient. For generic asymmetric permeabilities, that coefficient differs from the expression printed in equation (26) of Kay--Giuggioli [1]; an independent one-way first-passage calculation confirms the coefficient below.

Let \(D,L,a,b>0\) be respectively interior diffusivity, cell length, rightward membrane permeability, and leftward membrane permeability. If \(N_t\) denotes rightward minus leftward passages through membranes, then for every real \(\theta\),
\[
\Lambda(\theta)=\lim_{t\to\infty}t^{-1}\log\mathbb E[e^{\theta N_t}]
\]
exists and is the unique real \(\lambda\in(-Dq_0^2,\infty)\) solving
\[
(a+b)\cosh\!\left(L\sqrt{\lambda/D}\right)+\sqrt{D\lambda}\,\sinh\!\left(L\sqrt{\lambda/D}\right)=a e^\theta+b e^{-\theta}.
\tag{1}
\]
Here \(q_0\in(0,\pi/(2L))\) is the unique positive zero of \((a+b)\cos(qL)-Dq\sin(qL)\), and the left side of (1) is interpreted by entire analytic continuation in \(\lambda\). The root is the principal tilted-generator eigenvalue; it is real analytic in \(\theta\).

Writing \(S=a+b\), \(\Delta=a-b\), and \(H=2D+LS\), the effective drift and diffusivity of the physical position \(X_t\) satisfy
\[
\lim_{t\to\infty}\frac{\mathbb E[X_t]}t=\frac{2D\Delta}{H},\qquad
\lim_{t\to\infty}\frac{\operatorname{Var}(X_t)}{2t}
=\frac{DLS}{H}-\frac{DL^2(4D+LS)\Delta^2}{3H^3}.
\tag{2}
\]
The initial point may be anywhere inside one cell. The bounded difference between \(X_t\) and \(LN_t\) leaves the long-time cumulants unchanged. Equation (26) of [1] instead gives a value \(D_{[1]}\), for which the exact difference is
\[
D_{\rm exact}-D_{[1]}=\frac{DL^2(2D-LS)\Delta^2}{6H^3}.
\tag{3}
\]
Thus (2) coincides with that printed expression when \(a=b\) or \(LS=2D\), but not for generic asymmetric parameters.

For positive \(a,b\), the SCGF satisfies the exact affinity relation
\[
\Lambda(\theta)=\Lambda\!\left(-\log(a/b)-\theta\right).
\tag{4}
\]
Furthermore, \(N_t/t\) obeys a large-deviation principle with good convex rate function \(I(j)=\sup_{\theta\in\mathbb R}(\theta j-\Lambda(\theta))\), and \(I(j)-I(-j)=-j\log(a/b)\).

## Assumptions and scope

Cell \(n\in\mathbb Z\) is the open interval between adjacent barriers, written using local coordinate \(u\in(0,L)\). In its interior the particle evolves with generator \(D\partial_u^2\). At the interface from cell \(n\) to \(n+1\), the physical density has rightward net flux \(a p_n(L,t)-b p_{n+1}(0,t)\). Both sides of the interface have the same diffusive flux, so this is the usual semipermeable-interface boundary condition. There is no force in the interior, no bulk killing, and each crossing increases/decreases \(N_t\) by one. Crossing counts are integer valued; a change of starting cell adds a fixed integer without altering the SCGF. The main theorem assumes strictly positive \(D,L,a,b\). The one-way case \(b=0\) is used only as an independent boundary-limit check.

## Proof

**Tilt and characteristic equation.** The backward tilted generator on one compact cell acts as \(D f''\), with generator-domain boundary conditions
\[
D f'(0)=b[f(0)-e^{-\theta}f(L)],\qquad
D f'(L)=a[e^\theta f(0)-f(L)].
\tag{5}
\]
These follow from integration by parts against the forward flux condition, with each net right/left intercell transfer weighted by \(e^{\theta}\)/\(e^{-\theta}\). Insert \(f(u)=A\cosh(ku)+B\sinh(ku)\) with \(k^2=\lambda/D\). Eliminating \(A,B\) in (5) yields (1). The apparent factors of \(k\) in the determinant cancel by analytic continuation at \(\lambda=0\).

**Principal eigenvalue and uniqueness.** The diffusion with switching through both endpoints induces a strongly positive compact tilted semigroup on the split cell. Positivity improvement (or equivalently its one-dimensional positive Green resolvent) gives a simple real principal eigenvalue, which governs exponential moments of crossings. Put
\[
F(\lambda)=S\cosh(L\sqrt{\lambda/D})+\sqrt{D\lambda}\sinh(L\sqrt{\lambda/D}),\qquad R(\theta)=a e^\theta+b e^{-\theta}.
\]
For \(\lambda\ge0\), every coefficient beyond the constant in the Taylor series for \(F\) is positive. For \(\lambda=-Dq^2\) with \(0<q<q_0<\pi/(2L)\), \(F(-Dq^2)=S\cos(qL)-Dq\sin(qL)\) is strictly decreasing as \(q\) increases, hence \(F\) strictly increases with \(\lambda\). Consequently \(F\) maps \((-Dq_0^2,\infty)\) bijectively to \((0,\infty)\). Since \(R(\theta)>0\), (1) has exactly one root in that interval; the positive semigroup's principal root must lie there by continuity from the eigenvalue zero at \(\theta=0\) and cannot leave it or collide with another branch. The implicit-function theorem makes it analytic.

**Cumulants.** At zero tilt, \(\Lambda(0)=0\). Differentiating \(F(\Lambda(\theta))=R(\theta)\) gives
\[
F'(0)=L+\frac{SL^2}{2D}=\frac{LH}{2D},\quad
F''(0)=\frac{L^3}{3D}+\frac{SL^4}{12D^2},\quad
\Lambda'(0)=\frac{2D\Delta}{LH},\quad
\Lambda''(0)=\frac{S-F''(0)\Lambda'(0)^2}{F'(0)}.
\]
The spectral gap of the compact tilted problem makes differentiation of the long-time exponential growth legitimate and identifies these quantities with asymptotic first and second cumulants. Since \(X_t-LN_t\) lies in a fixed bounded interval, standard spectral perturbation of the joint position/count process gives the corresponding leading cumulants of \(X_t\). Substituting proves (2). Direct algebra using equation (26) of [1] gives (3).

**Current large deviations and symmetry.** The equation depends on \(\theta\) only through \(a e^\theta+b e^{-\theta}\), invariant under \(\theta\mapsto-\log(a/b)-\theta\). This proves (4). For \(|\theta|\to\infty\), the unique root tends to positive infinity, and the equation implies \(\Lambda(\theta)\sim D\theta^2/L^2\). In particular \(\Lambda'(\theta)\to\pm\infty\) as \(\theta\to\pm\infty\) (obtainable by implicit differentiation). Analyticity and steepness allow the differentiable Gärtner--Ellis theorem on the entire real line, proving the stated full large-deviation principle. Legendre duality and (4) yield its fluctuation relation.

**Independent one-way renewal calculation.** Let \(b\downarrow0\). Every crossing is then rightward. Starting at the left endpoint of one cell, the time \(T\) to cross the right membrane is a reflecting-at-zero/Robin-at-\(L\) first-passage time. Its Laplace transform is
\[
\mathbb E_0[e^{-sT}]=\frac{a}{a\cosh(L\sqrt{s/D})+\sqrt{Ds}\sinh(L\sqrt{s/D})}.
\]
For \(a=D=L=1\), Taylor expansion gives \(\mathbb E T=3/2\), \(\operatorname{Var}(T)=11/6\). Independent successive crossing times make \(N_t\) a renewal count; the renewal variance theorem gives \(D_{\rm exact}=L^2\operatorname{Var}(T)/(2(\mathbb ET)^3)=22/81\). Formula (26) of [1] gives \(43/162\) at the same limiting parameters. The nonzero difference \(1/162\) agrees with (3), independently of the tilted-generator calculation.

## Verification

The standalone `verify.py` symbolically differentiates the characteristic equation to second order; compares the resulting rational function with both (2) and the printed expression in [1]; checks the exact renewal Taylor coefficients, and compares principal eigenvalues of finite-volume biased random-walk approximations with the transcendental root. See `VERIFICATION.md` for the executed checks. The finite-grid calculations are supplementary consistency evidence, not a proof of the infinite-time theorem.

## Relationship to prior work

Kay and Giuggioli [1], especially section III.A and equations (23)--(26), establish the stochastic barrier model, the periodic-array propagator, the drift formula and a printed dispersion coefficient. Those objects and the drift are not claimed as new. This result provides the tilted spectral equation, full current large deviations and a separately certified comparison with its dispersion expression. The reflecting-diffusion current large-deviation techniques of Mallmin, du Buisson and Touchette [2] supply general background but do not give this exact asymmetric semipermeable-cell scalar equation. The transfer-matrix work of Moutal and Grebenkov [3] concerns barrier spectral problems, in particular symmetric transfer structures, not the same biased crossing-count law. Bressloff [4] discusses a probabilistic semipermeable barrier and renewal approach, not this infinite periodically biased array's current SCGF. Symmetry (4) is compatible with standard fluctuation relations and is not asserted to introduce fluctuation symmetry as a general concept.

## Limitations

This is a one-dimensional, periodic, stationary-parameter membrane model with Poissonian permeability and no external force. The rate function is implicit, not an elementary closed-form expression. Equality or disagreement with the dispersion coefficient in [1] is asserted for its **printed equation (26)** under the stated parameter interpretation, not for any later corrected version. The one-way renewal calculation serves as an independent boundary-limit certificate but is outside the main strict-positivity hypotheses. Similar transfer-eigenvalue methods can exist in earlier or incompletely indexed literature; no claim of exhaustive bibliographic uniqueness is made. No multidimensional, random-barrier, time-inhomogeneous or non-Poissonian extension is proven.

## References

[1] T. Kay and L. Giuggioli, *Local time statistics and permeable barrier crossing: from Poisson to Birth-Death Diffusion Equations*, arXiv:2406.07142 (first public June 11, 2024), section III.A and appendix D; https://arxiv.org/abs/2406.07142.

[2] E. Mallmin, J. du Buisson and H. Touchette, *Large deviations of currents in diffusions with reflective boundaries*, arXiv:2102.04846 (2021); https://arxiv.org/abs/2102.04846.

[3] N. Moutal and D. S. Grebenkov, *Diffusion across semi-permeable barriers: spectral properties, efficient computation, and applications*, arXiv:1807.06336 (2018); https://arxiv.org/abs/1807.06336.

[4] P. C. Bressloff, *A probabilistic model of diffusion through a semi-permeable barrier*, arXiv:2209.09176 (2022); https://arxiv.org/abs/2209.09176.
