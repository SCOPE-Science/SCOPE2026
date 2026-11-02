# Sharp correlation-sign transition despite second-order invariant variance for BDF2–Maruyama

## Finding

For the scalar Ornstein–Uhlenbeck (OU) process, standard BDF2–Maruyama has a sharply identifiable statistical tradeoff: its invariant one-time variance is closer to the exact value than backward Euler–Maruyama for **every** positive step size, yet its stationary autocovariances begin to oscillate in sign exactly after the scaled step \(z=\lambda h\) exceeds \(1/2\).

Write \(C_k=\mathbb E[X_nX_{n-k}]\) in the unique stationary numerical law. Then
\[
C_0=\frac{\sigma^2h(5z+4)}{2z(z+1)(z+4)},\qquad
\frac{C_1}{C_0}=\frac{12+11z-3z^2}{(2z+3)(5z+4)}.
\]
The complete qualitative classification is
\[
\begin{aligned}
& C_k>0\quad\text{for every integer }k\ge0&&\Longleftrightarrow 0<z\le\tfrac12,\\
& \#\{k\ge0:C_k>0\}=\#\{k\ge0:C_k<0\}=\infty&&\text{if }z>\tfrac12.
\end{aligned}
\]
In particular, the lag-one sign changes only later, at \(z_*=(11+\sqrt{265})/6\): it is positive below \(z_*\), zero at \(z_*\), and negative above \(z_*\).

## Assumptions and scope

Let \(\lambda>0\), \(\sigma\in\mathbb R\setminus\{0\}\), \(h>0\), and let \((\xi_n)_{n\in\mathbb Z}\) be independent standard normal variables. Set \(z=\lambda h\) and \(c=z+3/2\). The scalar BDF2–Maruyama recursion, with **the same successive increments appearing in neighboring steps**, is
\[
cX_n=2X_{n-1}-\tfrac12X_{n-2}+\sigma\sqrt{h}\left(\tfrac32\xi_n-\tfrac12\xi_{n-1}\right).
\]
The term involving \(\xi_{n-1}\) must not be replaced by a fresh independent normal: doing so changes the scheme and the asserted stationary law. The exact OU invariant variance is \(V_\mathrm{OU}=\sigma^2/(2\lambda)\), with strictly positive covariance \(V_\mathrm{OU}e^{-\lambda kh}\) at lag \(k\ge0\). The comparison backward Euler–Maruyama (BEM) uses the same \(h,\lambda,\sigma\) and independent Brownian increments. Initial data for the numerical process may be arbitrary square-integrable values independent of future innovations; the stationary results describe its unique limiting law.

## Proof

**1. Existence of the stationary law.** The deterministic homogeneous recurrence has characteristic equation \(cr^2-2r+1/2=0\), hence roots
\[
r_\pm=\frac{2\pm\sqrt{1-2z}}{3+2z}.
\]
For \(0<z\le1/2\) the roots are real in \((0,1)\). For \(z>1/2\) they are complex conjugates of modulus \((3+2z)^{-1/2}<1\). Thus the homogeneous recurrence is Schur stable for every \(z>0\), including the double root at \(z=1/2\). The forced linear process has a unique stationary centered Gaussian solution and convergence from every square-integrable initialization.

**2. Exact covariances.** Put \(Y_n=X_n/(\sigma\sqrt{h})\) and \(U_n=(Y_n,Y_{n-1},\xi_n)^\top\). Then \(U_n=TU_{n-1}+b\xi_n\), where
\[
T=\begin{pmatrix}2/c&-1/(2c)&-1/(2c)\\1&0&0\\0&0&0\end{pmatrix},\qquad
b=\begin{pmatrix}3/(2c)\\0\\1\end{pmatrix}.
\]
Schur stability gives the unique solution \(S=TS T^\top+bb^\top\) for the stationary covariance matrix. Solving its six independent scalar equations yields
\[
S_{11}=\frac{5z+4}{2z(z+1)(z+4)},\quad
\frac{S_{12}}{S_{11}}=\frac{12+11z-3z^2}{(2z+3)(5z+4)},\quad
S_{13}=\frac{3}{2z+3}.
\]
These are exactly the stated \(C_0/(\sigma^2h)\), \(C_1/C_0\), and the newest-noise cross-covariance. For \(k\ge2\), the noise forcing at time \(n\) is independent of \(X_{n-k}\), so the Yule–Walker relation is
\[
cC_k=2C_{k-1}-\tfrac12C_{k-2},\qquad k\ge2.
\]

**3. Invariant-variance bias and strict comparison.** Direct simplification gives
\[
\frac{C_0}{V_\mathrm{OU}}=\frac{5z+4}{(z+1)(z+4)}=1-\frac{z^2}{(z+1)(z+4)}.
\]
Thus the relative stationary-variance deficit is strictly positive and of order \(z^2/4\) as \(z\downarrow0\). BEM's invariant variance is \(\sigma^2/[\lambda(z+2)]\) and its ratio to \(V_\mathrm{OU}\) is \(2/(z+2)\). The BDF2 ratio minus the BEM ratio is exactly
\[
\frac{z(3z+4)}{(z+1)(z+2)(z+4)}>0.
\]
Since both ratios lie below one, BDF2 is strictly closer to the exact invariant variance for every \(z>0\).

**4. Sharp all-lag correlation-sign transition.** Define \(q=C_1/C_0\). For \(0<z<1/2\), the roots \(0<r_-<r_+<1\) are real. A direct calculation shows
\[
cq^2-2q+\tfrac12=\frac{z^2(z+4)(9z+8)}{2(2z+3)(5z+4)^2}>0,
\]
while
\[
q-\frac{2}{3+2z}=\frac{(z+1)(4-3z)}{(2z+3)(5z+4)}>0.
\]
Because \(2/(3+2z)\) is the midpoint of the roots, these two inequalities imply \(q>r_+\). Writing \(C_k=Ar_+^k+Br_-^k\) and solving for \(A,B\) from \(C_0,C_1\), one gets \(A>C_0>0\) and \(B<0\). Hence \(C_k\ge(A+B)r_+^k=C_0r_+^k>0\) for every \(k\ge0\). At \(z=1/2\), \(r_+=r_-=1/2\) and \(q>1/2\); thus \(C_k=C_0(1+k(2q-1))2^{-k}>0\) for all \(k\ge0\).

For \(z>1/2\), write \(r_\pm=R e^{\pm i\theta}\), with \(R=(3+2z)^{-1/2}\) and \(0<\theta<\pi/2\). The real sequence has the representation
\[
C_k=C_0R^k[\cos(k\theta)+\beta\sin(k\theta)],\quad
\beta=\frac{(3+2z)q-2}{\sqrt{2z-1}}.
\]
The bracket is a nonzero sinusoid with zero angular mean. If \(\theta/(2\pi)\) is irrational, the angular orbit is dense; if rational, its equally spaced finite orbit has mean zero and includes the strictly positive term at \(k=0\). In either case it has both positive and negative terms infinitely often. This proves the sharp \(z=1/2\) transition. Finally, the numerator \(12+11z-3z^2\) has exactly one positive root, \(z_*=(11+\sqrt{265})/6\), yielding the lag-one trichotomy.

**5. An exact witness.** At \(z=1\), \(C_0=9\sigma^2h/20\), \(C_1=\sigma^2h/5\), and the recurrence gives \(C_2=7\sigma^2h/100\), \(C_3=2\sigma^2h/125\), but \(C_4=-3\sigma^2h/2500<0\). The exact OU covariance at this lag is \(\sigma^2 h e^{-4}/2>0\).

## Verification

Run `python verify_bdf2.py` with Python 3.10+ and SymPy 1.10+. It constructs the three-dimensional stationary Lyapunov equation from the stated recursion, solves all six covariance entries symbolically, checks the claimed rational factorizations, and checks the full lag recursion at 120 exact-rational parameter choices. The observed output was: `VERIFY_OK Lyapunov symbolic identities, variance inequalities, 120 exact parameters, 3335 rational covariance checks`. The infinite-lag sign claims rely on the proof, not on finite calculations.

## Relationship to prior work

BDF2–Maruyama itself and the colored Brownian forcing are established in Andersson and Kruse (2015/2017) and Kruse and Weiske (2021); neither is claimed as new. Those works primarily analyze well-posedness and finite-time strong/mean-square convergence. Related Buckwar–Winkler (2006) treats stability and consistency of stochastic multistep methods. Classical deterministic BDF2 decay has the root transition at \(z=1/2\), and earlier work analyzes delayed sign loss of deterministic iterates. The contribution here is the **stationary stochastic covariance**: its exact all-step invariant-marginal bias, lag-one value, and complete positivity-versus-sign-oscillation classification with a concrete statistical witness. The standard recurrence's oscillatory roots alone do not supply these stationary stochastic covariance initial values or invariant-bias comparison.

## Limitations

The classification concerns the scalar additive-noise OU equation, the classical equal-step BDF2–Maruyama forcing, its stationary two-time covariances, and exact arithmetic. It does not assert the same transition for nonlinear drifts, multidimensional nonnormal discretizations, finite-time strong errors, other stochastic multistep noise conventions, or arbitrary observables. The root transition of deterministic BDF2 is classical; priority of the exact stochastic-covariance combination remains subject to independent historical verification.

## References

1. A. Andersson and R. Kruse, *Mean-square convergence of the BDF2-Maruyama and backward Euler schemes for SDE satisfying a global monotonicity condition*, arXiv:1509.00609 (first public 2015), especially equation (3) and Section 5. https://arxiv.org/html/1509.00609v2
2. R. Kruse and R. Weiske, *The BDF2-Maruyama Scheme for Stochastic Evolution Equations with Monotone Drift*, arXiv:2105.08767 (first public 2021-05-18), especially Section 1 and Section 5. https://arxiv.org/html/2105.08767v1
3. E. Buckwar and R. Winkler, *Multistep methods for SDEs and their application to problems with small noise*, SIAM J. Numer. Anal. 44 (2006), 779–803. https://doi.org/10.1137/040602857
4. W. Liu, X. Mao, and Y. Wu, *The backward Euler-Maruyama method for invariant measures of stochastic differential equations with super-linear coefficients*, Appl. Numer. Math. 184 (2023), 137–150. https://doi.org/10.1016/j.apnum.2022.09.017
