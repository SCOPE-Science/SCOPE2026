# An all-Courant Fourier stability certificate and nearby calibration failure for uniform AdHImEx

## Finding

For the one-dimensional, uniform-periodic, unlimited AdHImEx transport discretization specified below, the proposed implicitness calibration with coefficient \(\gamma=7/10\) is \(\ell^2\)-nonexpansive for **every** Courant number \(C\geq0\) and for every discrete Fourier mode. In fact its scalar amplification factor has modulus at most one for **every continuous** Fourier phase \(\xi\in[0,2\pi]\), without sampling the phase or Courant ranges.

This guarantee has a narrow, mathematically meaningful calibration margin: keeping the same scheme and cutoff but replacing \(\gamma=7/10\) by \(\gamma=69/100\) produces amplification above one at phase \(\xi=\pi/2\) for all sufficiently large Courant numbers. Hence a four-cell periodic mesh already contains the unstable mode. The claim is **not** that \(7/10\) is the sharp optimal coefficient.

## Assumptions and scope

Consider \(u_t+a u_x=0\) with constant velocity \(a>0\), a uniform periodic mesh of spacing \(\Delta x\), and a step \(h\geq0\). Put \(C=ah/\Delta x\). At the right face of cell \(j\), use the paper's uncorrected fifth-order face interpolation
\[
\widehat u_{j+1/2}=-\frac1{20}u_{j+2}+\frac9{20}u_{j+1}+\frac{47}{60}u_j-\frac{13}{60}u_{j-1}+\frac1{30}u_{j-2}.
\]
Use the difference of consecutive fluxes and the five-stage Runge--Kutta tableau (6) of te Winkel--Weller--Kühnlein--Kent (2026), without nonlinear flux correction, with spatially uniform blending parameter
\[
\theta_\gamma(C)=1-\frac{1}{1+\gamma\max\{0,C-7/5\}},\qquad \gamma>0.
\]
Negative velocity gives the complex-conjugate Fourier symbol after reversing orientation and thus the same stability statement with \(C=|a|h/\Delta x\). The zero-velocity case is the identity map. All statements concern exact arithmetic and periodic, constant-coefficient linear transport; they do not assert stability for spatially varying blending.

## Proof

**1. The exact scalar amplification factor.** For a scalar test equation \(y'=\lambda y\), direct substitution into all five rows of the stated tableau, with \(z=h\lambda\), gives
\[
R(z,\theta)=\frac{1+\theta z/2}{1-\theta z/2}\,P_3((1-\theta)z),\qquad
P_3(w)=1+w+\frac{w^2}{2}+\frac{w^3}{6}.
\]
This identity is algebraic; it does not require treating the split operators as commuting matrices. We use it only on a scalar Fourier mode, where the same circulant spatial operator occurs in every stage.

**2. The fifth-order symbol.** For a Fourier vector \(u_j=e^{\mathrm i j\xi}\), the dimensionless semidiscrete operator is \(-Q(\xi)\), with
\[
Q(\xi)=-\frac{e^{2\mathrm i\xi}}{20}+\frac{e^{\mathrm i\xi}}2+\frac13-e^{-\mathrm i\xi}+\frac{e^{-2\mathrm i\xi}}4-\frac{e^{-3\mathrm i\xi}}{30}.
\]
Writing \(T=\sin^2(\xi/2)\), direct trigonometric simplification gives
\[
\Re Q=\frac{16}{15}T^3,\qquad
\Im Q=\frac{\sin\xi}{15}(8T^2+10T+15).
\]
Thus \(\Re Q\geq0\). With \(z=-CQ\), the Crank--Nicolson factor in \(R\) has modulus at most one, for every \(C\geq0\) and \(\theta\in[0,1]\).

**3. A uniform exact certificate for the explicit factor.** Set \(c=C(1-\theta)\). For \(\gamma=7/10\), one has
\[
0\leq c\leq\frac{10}{7}.
\]
Indeed, \(c=C\leq7/5\) for \(C\leq7/5\), while for \(C>7/5\),
\[
c=\frac{C}{1+(7/10)(C-7/5)}=\frac{C}{(7/10)C+1/50}<\frac{10}{7}.
\]
We prove the following *finite rational-polynomial identity and positivity certificate*:
\[
1-|P_3(-cQ(\xi))|^2=cT^2 H(c,T),
\qquad H(c,T)\geq0\quad (0\leq c\leq10/7,\;0\leq T\leq1).
\]
Here \(H\) is defined explicitly by the left side and by the following rational data:
\[
\alpha=16T^3/15,\qquad
\beta^2=4T(1-T)(8T^2+10T+15)^2/225,
\]
\[
U=-c\alpha,\quad V=c^2\beta^2,\quad
R_0=1+U+\frac{U^2-V}{2}+\frac{U^3-3UV}{6},\quad
J_0=1+U+\frac{U^2}{2}-\frac{V}{6},
\]
\[
H(c,T)=\frac{1-R_0^2-VJ_0^2}{cT^2}
\quad\text{(the quotient is an exact polynomial).}
\]
The quotient has degree \(5\) in \(c\) and \(13\) in \(T\). Set \(\eta=7c/10\in[0,1]\). On each of the rectangles \(0\leq T\leq1/2\) and \(1/2\leq T\leq1\), expand \(H\) in the tensor-product Bernstein basis of bidegree \((13,5)\) after affinely mapping \(T\) and \(\eta\) to the unit square. Every one of the \(84\) exact rational coefficients is nonnegative on either rectangle. On the first rectangle exactly three coefficients vanish and the least positive coefficient is \(16/195\); on the second none vanish and the minimum is \(2706544/551353635\). The complete coefficient calculation, including the polynomial division and two Bernstein expansions, is reproduced in \(\texttt{verify.py}\) using only exact rational arithmetic. Since every Bernstein basis function is nonnegative and the coefficients are nonnegative, \(H\geq0\) on both rectangles. This is an exhaustive algebraic certificate for the entire continuum; it is not a finite sample of Fourier modes. Therefore \(|P_3(-cQ)|\leq1\). Multiplication by the contractive Crank--Nicolson factor proves \(|R(-CQ,\theta_{7/10}(C))|\leq1\) for every \(C\geq0\) and every \(\xi\). Parseval's identity gives the asserted \(\ell^2\)-nonexpansion for every periodic mesh size.

**4. A nearby exact failure.** Replace \(\gamma=7/10\) by \(\gamma=69/100\). For every fixed nonconstant Fourier mode, as \(C\to\infty\), one has \(c=C(1-\theta_\gamma(C))\to1/\gamma=100/69\), while the Crank--Nicolson factor tends to \(-1\), of modulus one. At \(\xi=\pi/2\) the symbol is exactly \(Q=(2+22\mathrm i)/15\). Direct rational arithmetic yields
\[
\left|P_3\left(-\frac{100}{69}\frac{2+22\mathrm i}{15}\right)\right|^2-1
=\frac{14399294983760}{708051067974441}>0.
\]
Continuity of the rational amplification factor then implies \(|R|>1\) at this mode for every sufficiently large finite \(C\). A periodic mesh whose size is a multiple of four realizes the mode. This proves the failure assertion.

## Verification

Run \(\texttt{python3 verify.py}\) in a standard Python 3 environment. The standalone program constructs the real and squared-imaginary parts of the Fourier symbol as exact rational bivariate polynomials; verifies divisibility by \(cT^2\); converts \(H\) into tensor-product Bernstein coordinates over \([0,10/7]\times[0,1]\); splits once at \(T=1/2\) by exact de Casteljau arithmetic; checks all \(168\) coefficient inequalities; computes the exact positive instability excess; and compares the stage recurrence with the factored scalar amplification formula on \(1000\) seeded floating-point checks. Exact checks certify the polynomial inequalities; random checks are only supplementary consistency tests.

## Relationship to prior work

Te Winkel, Weller, Kühnlein and Kent introduce the AdHImEx tableau, fifth-order spatial interpolation and the numerical calibration rule (their equations (6), (16), (18)). Their von Neumann study evaluates \(401\) phases over Courant numbers up to \(100\), and explicitly describes the stability envelope as numerically obtained. The present finding proves the reported uniform-coefficient stability condition without any Courant or Fourier sampling and supplies an exact instability witness after a small change of calibration. The scalar Crank--Nicolson and SSPRK3 factors are classical; neither the factorization alone nor the classical SSPRK3 polynomial is claimed as an original contribution.

Earlier work on operator splitting, including Ullrich and Jablonowski (2012), supplies related structural background. A numerical RK3/fifth-order-upwind CFL value near \(1.43498\) appears in the NEMO Ocean Engine manual; that numerical value is consistent with the present rational certificate but does not itself provide the stated continuum certificate for AdHImEx or the exact \(69/100\) failure. These comparisons do not constitute exhaustive historical-priority certification.

## Limitations

The result is a constant-coefficient, uniform-grid, unlimited, periodic, linear \(\ell^2\) von Neumann statement. It does not address discontinuous or spatially varying blending, nonuniform grids, nonlinear transport, absolute monotonicity, positivity, the flux-corrected variant, boundary conditions, finite precision, or convergence order. The calibration \(7/10\) is only a rigorously sufficient value, not proved optimal; \(69/100\) is a rigorously insufficient value in the large-Courant limit. No independent mathematical audit has been performed.

## References

1. A. J. te Winkel, H. Weller, C. Kühnlein and J. Kent, *AdHImEx: Adaptively High-Order Implicit-Explicit Transport for Large Time Steps*, arXiv:2610.08166v1, publicly submitted 6 October 2026; especially equations (6), (16), (18), and section 2.4. https://arxiv.org/html/2610.08166
2. P. A. Ullrich and C. Jablonowski, *Operator-Split Runge--Kutta--Rosenbrock Methods for Nonhydrostatic Atmospheric Models*, Monthly Weather Review 140 (2012), 1257--1284, doi:10.1175/MWR-D-10-05073.1.
3. *NEMO Ocean Engine Manual 5.0*, numerical RK3/UP5 CFL table (quoted value \(1.43498\)); the tabulation is context, not used as proof.
