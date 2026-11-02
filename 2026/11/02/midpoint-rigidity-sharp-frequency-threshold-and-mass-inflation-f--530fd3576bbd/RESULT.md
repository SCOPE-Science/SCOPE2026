# Midpoint rigidity, sharp frequency threshold, and mass inflation for three-node trigonometric SBP

## Finding
Let \(0<\omega<\pi\), and let the three interpolation nodes be \(-1,a,1\) with \(-1<a<1\). Consider the three-dimensional real function space \(\mathcal F_\omega=\operatorname{span}\{1,\cos(\omega x),\sin(\omega x)\}\). A nodal first-derivative matrix \(D\) and a **positive diagonal** matrix \(P\) satisfying both exact differentiation on \(\mathcal F_\omega\) and the summation-by-parts identity
\[
 P D+D^{\mathsf T}P=\operatorname{diag}(-1,0,1)
\]
exist **if and only if** the interior node is the midpoint, \(a=0\), and \(0<\omega<2\pi/3\). When they exist, both matrices are unique. Writing \(s=\sin\omega\) and \(c=\cos\omega\), they are
\[
 D=\omega\begin{pmatrix}
 -(1+2c)/(2s)&s/(1-c)&-1/(2s)\\
 -1/(2s)&0&1/(2s)\\
 1/(2s)&-s/(1-c)&(1+2c)/(2s)
 \end{pmatrix},\qquad
 P=\operatorname{diag}(q,2(1+c)q,q),\quad
 q=\frac{s}{\omega(1+2c)}.
\]
Unlike an ordinary quadrature rule, the unique positive SBP norm **overintegrates the constant function**:
\[
 M(\omega):=\mathbf1^{\mathsf T}P\mathbf1
 =\frac{2(2+\cos\omega)\sin\omega}{\omega(1+2\cos\omega)}>2.
\]
The mass defect obeys \(M(\omega)=2+(2/45)\omega^4+O(\omega^6)\) as \(\omega\downarrow0\). Both the endpoint weight and the total mass diverge at the feasibility boundary:
\[
 \lim_{\omega\uparrow2\pi/3}(2\pi/3-\omega)q=\frac{3}{4\pi},\qquad
 \lim_{\omega\uparrow2\pi/3}(2\pi/3-\omega)M(\omega)=\frac{9}{4\pi}.
\]

## Assumptions and scope
All matrices and node values are real. Exact differentiation means \(D(f(-1),f(a),f(1))^{\mathsf T}=(f'(-1),f'(a),f'(1))^{\mathsf T}\) for every \(f\in\mathcal F_\omega\). Positive diagonal means all three diagonal entries of \(P\) are strictly positive. No requirement to integrate ordinary coordinate polynomials is imposed. The frequency satisfies \(0<\omega<\pi\); the endpoint \(\omega=\pi\) would make the three nodal trigonometric traces linearly dependent on the symmetric grid. The boundary matrix \(\operatorname{diag}(-1,0,1)\) corresponds to the two endpoint evaluations in the standard one-dimensional first-derivative SBP identity. This statement is a complete classification within precisely this three-node, positive-diagonal setting, not a claim about additional nodes or other function spaces.

## Proof
**Step 1 (unisolvence and uniqueness of the derivative).** On an interval of length \(2\), with \(0<\omega<\pi\), any nonzero function \(A+B\cos(\omega x)+C\sin(\omega x)\) has at most two distinct zeros: otherwise, over a trigonometric period longer than the interval, the sinusoidal graph would cross the horizontal level at least three times, which is impossible. Thus the three evaluation vectors of the stated basis are linearly independent. Consequently exact differentiation fixes the unique derivative matrix \(D=V'V^{-1}\), where the rows of \(V\) are basis values at the three nodes and those of \(V'\) are their derivatives.

**Step 2 (interior-node rigidity).** The unique cardinal function associated with the interior node is
\[
 \ell_a(x)=\frac{\cos\omega-\cos(\omega x)}{\cos\omega-\cos(\omega a)}.
\]
Its endpoint values vanish and its value at \(a\) equals one. Therefore the middle diagonal entry of the unique derivative matrix is
\[
 D_{11}=\ell_a'(a)=\frac{\omega\sin(\omega a)}{\cos\omega-\cos(\omega a)}.
\]
Here indices are \(0,1,2\). Because \(P\) is diagonal and positive, the center diagonal entry of the SBP equation is \(2P_{11}D_{11}=0\). Since \(|\omega a|<\pi\), its only solution is \(a=0\). Thus no off-center interior point admits the requested diagonal norm.

**Step 3 (the only possible norm and its sharp positivity threshold).** Set \(a=0\). Inverting the sampling matrix for the three basis functions gives the displayed \(D\); its central diagonal vanishes, the endpoint diagonals are opposite, and its off-diagonal entries satisfy the weighted cancellations described below. Write \(P=\operatorname{diag}(p_0,p_1,p_2)\). The endpoint diagonal SBP identities \(2p_0D_{00}=-1\) and \(2p_2D_{22}=1\) force \(p_0=p_2=q=s/[\omega(1+2c)]\). The \((0,1)\) off-diagonal identity forces \(p_1=2(1+c)q\). Substitution into all nine matrix entries verifies the SBP identity exactly; uniqueness follows. On \(0<\omega<\pi\), \(s>0\) and \(1+c>0\), so positivity is equivalent to \(1+2\cos\omega>0\), or \(\omega<2\pi/3\). At equality the endpoint derivative diagonal is zero but the SBP boundary diagonal is nonzero, so no norm exists. Above equality the forced endpoint weights are negative.

**Step 4 (strict mass inflation).** Sum the diagonal weights to obtain the formula for \(M\). Because \(1+2\cos\omega>0\) in the feasible range, \(M>2\) is equivalent to positivity of
\[
 H(\omega):=(2+\cos\omega)\sin\omega-\omega(1+2\cos\omega).
\]
Direct differentiation yields \(H'(\omega)=2\sin\omega\,(\omega-\sin\omega)>0\) for \(0<\omega<2\pi/3\); also \(H(0)=0\). This proves the strict inequality. Standard Taylor expansion around zero gives \(q\to1/3\), \(p_1\to4/3\), and the stated \((2/45)\omega^4\) leading mass defect. For \(\omega_c=2\pi/3\), \(1+2\cos\omega=\sqrt3(\omega_c-\omega)+O((\omega_c-\omega)^2)\) and \(\sin\omega_c=\sqrt3/2\); substitution gives both stated blow-up constants.

## Verification
The standalone script `verify_fsbp.py` reproduces exact symbolic differentiation and all nine entries of the SBP identity using SymPy; it verifies the displayed mass formula, derivative of \(H\), small-frequency coefficients and critical limits, then tests centered positivity and off-center diagonal obstruction over seeded parameter samples. It passes **668** algebraic, boundary, and seeded finite checks. Finite checks illustrate only the general statements established analytically in the proof. Run with `python verify_fsbp.py` using SymPy.

## Relationship to prior work
General-function-space summation-by-parts (FSBP) theory characterizes existence using positive quadrature for products of basis functions and derivatives; this abstract equivalence is not claimed as new. Glaubitz, Nordström and Öffner (2022) also construct trigonometric FSBP examples using a different node count and a full-period frequency. Haase, Winters and Glaubitz (2026) study conservation/entropy stability for nonpolynomial FSBP spaces and illustrate richer trigonometric-polynomial spaces. The present statement resolves the specific minimal-node *geometry/frequency* feasibility problem explicitly and shows that preserving a trigonometric differentiation space on the three-node grid forces nonphysical norm mass on the constant function. No claim is made that a fixed-grid numerical method from either paper was shown unstable.

## Limitations
The frequency interval \(0<\omega<\pi\), exact arithmetic, three nodes including endpoints, and a positive **diagonal** norm are essential to the classification. A non-diagonal norm, four or more nodes, periodic SBP, or inclusion of the coordinate function may change feasibility and quadrature mass. Strict inflation of the SBP-weighted constant does not itself contradict SBP energy stability or mean weighted conservation. The classification is an analytical consequence of a small exact linear system; prior use of the same three-node formula in uninspected historical literature cannot be excluded. No independently conducted mathematical audit has occurred.

## References
1. J. Glaubitz, J. Nordström, and P. Öffner, *Summation-by-parts operators for general function spaces*, arXiv:2203.05479 (first posted 2022-03-10), especially the general existence construction and trigonometric examples.
2. T. Haase, A. R. Winters, and J. Glaubitz, *Summation-by-parts operators for general function spaces: Flux differencing, entropy stability, and accuracy*, arXiv:2610.30272v1 (first posted 2026-10-21), especially the general FSBP identities and trigonometric function-space examples.
3. J. Bercik, A. Patrascu, and D. W. Zingg, *Construction and Optimization of Sum-by-Parts Operators for General Function Spaces Using an Improved Generalized Gaussian Quadrature Algorithm*, arXiv:2607.08934 (2026), for higher-node FSBP construction and quadrature design.
