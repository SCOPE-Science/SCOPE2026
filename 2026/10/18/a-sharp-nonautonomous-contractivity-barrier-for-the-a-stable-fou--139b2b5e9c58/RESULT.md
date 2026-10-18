# A sharp nonautonomous contractivity barrier for the A-stable four-stage nIRK4 method

## Finding
Consider the four-stage nIRK4 Runge–Kutta method of Mizerová and Tvrdá [1], applied in one step of length one to the smooth, uniformly nonexpanding scalar flow
\[
y'(t)=-a(1-t)y(t),\qquad t\in[0,1],\qquad y(0)=y_0\in\mathbb R,\qquad a\geq0.
\]
Its exact flow multiplier is \(e^{-a/2}\). The numerical step is uniquely defined for every \(a\geq0\) and is multiplication by
\[
R_{\mathrm{var}}(a)=\frac{1080-316a+36a^2-2a^3}{1080+224a+13a^2}.
\]
Let \(a_*\) be the unique positive root of
\[
2a^3-49a^2+92a-2160=0,\qquad 24<a_*<25,
\]
so \(a_*=24.4268678121564\ldots\). Then the numerical step is nonexpansive for every initial state exactly when \(0\leq a\leq a_*\); it is strictly contractive for every nonzero initial state when \(0<a<a_*\). At the boundary it flips the sign of a nonzero input with unchanged magnitude; for \(a>a_*\) it strictly amplifies every nonzero input despite exact-flow contraction. The amplification is unbounded as \(a\to\infty\): \(R_{\mathrm{var}}(a)/a\to-2/13\).

This is not detectable from the autonomous scalar stability function. The nIRK4 method and three-stage Gauss–Legendre collocation share the same diagonal \([3/3]\) Padé stability function
\[
R(z)=\frac{120+60z+12z^2+z^3}{120-60z+12z^2-z^3}.
\]
Nevertheless, for every \(a\geq0\), three-stage Gauss–Legendre remains uniquely solvable and nonexpansive on the identical variable-coefficient initial-value problem (strictly contractive for \(a>0\)).

For the entirely rational test \(a=25\), nIRK4 gives \(y_1=-346y_0/329\), whereas the exact flow gives \(y(1)=e^{-25/2}y_0\) and three-stage Gauss–Legendre gives a strictly smaller final magnitude than \(|y_0|\).

## Assumptions and scope
All statements concern exact arithmetic, the real scalar ODE specified above, a single unit-length Runge–Kutta step from \(t=0\) to \(t=1\), and arbitrary real input \(y_0\). Parameter \(a\) ranges over all nonnegative real numbers. At \(a=0\) the flow and both schemes are the identity. Nonexpansive means \(|y_1|\leq|y_0|\) for all inputs; strict contractivity means the inequality is strict for all nonzero inputs. This is a pointwise parameter-family classification, not a general theorem for all nonautonomous equations or all step lengths.

For reproducibility, the printed nIRK4 tableau [1, Appendix A5] has stages \(c=(0,1/3,2/3,1)^\mathsf T\), weights \(b=(1/8,3/8,3/8,1/8)^\mathsf T\), and coefficient matrix
\[
A=\begin{pmatrix}
0&0&0&0\\
47/360&89/360&-19/360&1/120\\
7/60&77/180&23/180&-1/180\\
1/8&3/8&3/8&1/8
\end{pmatrix}.
\]
The final stage equals the numerical output because the last row of \(A\) equals \(b^\mathsf T\).

## Proof
Let \(\mathbf1\) denote the four-component vector of ones, define \(D_a=\operatorname{diag}(a,2a/3,a/3,0)\), and write the nIRK4 stage values as \(Y\). Its stage equations for the specified scalar flow are
\[
(I+AD_a)Y=y_0\mathbf1,
\qquad y_1=y_0-b^\mathsf TD_aY=Y_4.
\]
Direct exact determinant expansion gives
\[
\det(I+AD_a)=\frac{13a^2+224a+1080}{1080}>0\qquad(a\geq0).
\]
Consequently the stages exist uniquely for every admissible parameter. Solving for the last component gives the stated rational multiplier \(R_{\mathrm{var}}(a)\). The two comparisons with unit modulus factor exactly as
\[
R_{\mathrm{var}}(a)-1=-\frac{a(2a^2-23a+540)}{13a^2+224a+1080},
\]
\[
R_{\mathrm{var}}(a)+1=-\frac{2a^3-49a^2+92a-2160}{13a^2+224a+1080}.
\]
The first difference is strictly negative when \(a>0\), since the quadratic has positive leading coefficient and negative discriminant \(-3791\). Put \(F(a)=2a^3-49a^2+92a-2160\). Its derivative factors as \(F'(a)=2(a-1)(3a-46)\). The local maximum at \(a=1\) is \(F(1)=-2115\); the only subsequent local minimum is still negative. Thus \(F\) has exactly one positive root, lying between \(24\) and \(25\), as \(F(24)=-528\) and \(F(25)=765\). It follows that \(R_{\mathrm{var}}(a)>-1\) for \(0\leq a<a_*\), equals \(-1\) at \(a=a_*\), and is below \(-1\) for \(a>a_*\). Together with \(R_{\mathrm{var}}(a)<1\) for positive \(a\), this proves the sharp nonexpansivity criterion. Polynomial division gives the stated divergent large-parameter limit, and substitution of \(a=25\) yields \(-346/329\). Integrating the continuous equation gives the exact multiplier \(e^{-a/2}\).

The two RK methods' identical autonomous stability function follows by evaluating \(1+z b^\mathsf T(I-zA)^{-1}\mathbf1\), with the corresponding Gaussian tableau obtained by integrating its cardinal Lagrange polynomials. Their equality as \([3/3]\) Padé functions also follows from the stability function printed in [1, Appendix A5].

To compare the genuinely nonautonomous steps, write the three-stage Gauss tableau as \((A_G,b_G,c_G)\), with all weights \(b_{G,i}>0\). For Gaussian collocation the symplectic (algebraic-stability) identities [2] hold:
\[
b_{G,i}(A_G)_{ij}+b_{G,j}(A_G)_{ji}=b_{G,i}b_{G,j}
\qquad\text{for every }i,j.
\]
For arbitrary sampled damping values \(\lambda_i\geq0\), stage values \(Y_i\) and derivatives \(K_i=-\lambda_iY_i\) therefore obey the exact quadratic-energy identity
\[
y_1^2-y_0^2=2\sum_i b_{G,i}Y_iK_i
-\sum_{i,j}\bigl(b_{G,i}(A_G)_{ij}+b_{G,j}(A_G)_{ji}-b_{G,i}b_{G,j}\bigr)K_iK_j
=-2\sum_i b_{G,i}\lambda_iY_i^2\leq0.
\]
Uniqueness of the Gaussian stage solution also follows: applying this identity to a homogeneous stage system with \(y_0=0\) forces \(\lambda_iY_i=0\) for each \(i\), since \(b_{G,i}>0\), so every \(K_i=0\) and every \(Y_i=0\). Hence its stage matrix is invertible. Here \(\lambda_i=a(1-c_{G,i})>0\) for \(a>0\), since all Gauss nodes lie strictly inside \((0,1)\). Equality of final and initial squared magnitudes would force every \(Y_i=0\) and thus \(y_0=0\). This proves strict contractivity when \(a>0\) and nonexpansivity at \(a=0\), completing the comparison.

## Verification
The self-contained Python/SymPy program `verify.py` constructs both RK tableaux from exact rational or algebraic entries, checks the stage determinant and rational amplification identities, isolates the positive cubic root, proves the autonomous stability functions coincide symbolically, checks all nine Gaussian algebraic-stability identities, and tests the stage equations at exact rational parameter values. Executing `python verify.py` completes all stated symbolic assertions. These finite checks support the reproducibility of the analytic identities; the all-parameter and uniqueness statements are established by the preceding proof, not by sampling.

## Relationship to prior work
Mizerová and Tvrdá [1] introduce the repeated-integral nIRK4 tableau, establish its classical A-stability, state its autonomous scalar stability function and report favorable finite-step accuracy experiments for stiff systems. These prior claims are not new here. Gaussian collocation's algebraic-stability identity and ensuing contractivity are also classical [2,3]. The separate assertion here is the exact, sharp nonautonomous amplitude classification for the *published nIRK4 tableau*, and the striking contrast with Gauss collocation despite identical autonomous Padé functions. Autonomous A-stability does not imply contractivity for arbitrary time-varying dissipative coefficients; our exact threshold and unbounded amplification exhibit this distinction for a concrete, smooth, nonnegative damping profile.

## Limitations
The result does not assert that nIRK4 is unstable on all dissipative nonautonomous problems, nor that any finite trajectory necessarily diverges. It addresses a single full interval with strong spatial-temporal damping variation; practical time refinement may alleviate it. It does not classify arbitrary nonlinear contractivity or vector systems and does not claim a novel general algebraic-stability theory. While the primary method description and closely related stability literature were inspected, equivalent treatment of this precise tableau and damping family in other literature remains possible. No independent scientific audit has been performed.

## References
[1] H. Mizerová and K. Tvrdá, *A new way of deriving implicit Runge-Kutta methods based on repeated integrals*, arXiv:2404.16665v1 (first public 25 April 2024). https://arxiv.org/html/2404.16665v1 ; specifically Section 3, Section 4 and Appendix A5.

[2] E. Hairer and G. Wanner, *Solving Ordinary Differential Equations II: Stiff and Differential-Algebraic Problems*, 2nd revised edition, Springer. Classical algebraic stability and Gauss collocation (background).

[3] U. M. Ascher and G. Bader, *Stability of collocation at Gaussian points*, 1985 (classical background on Gauss collocation stability).
