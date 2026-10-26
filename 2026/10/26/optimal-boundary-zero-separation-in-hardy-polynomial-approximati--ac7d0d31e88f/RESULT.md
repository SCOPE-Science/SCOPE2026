# Optimal boundary-zero separation in Hardy polynomial approximation: the sinc crossover

## Finding

Let \(H^2(\mathbb D)\) have coefficient norm \(\|\sum_{k\ge0}a_kz^k\|^2=\sum_{k\ge0}|a_k|^2\). For \(n\ge0\) and \(0\le\theta\le\pi\), let
\[
f_\theta(z)=(1-z)(1-e^{-i\theta}z),\qquad
E_n(\theta)=\min_{\deg p\le n}\|1-f_\theta p\|_{H^2}^{2}.
\]
Set \(N=n+3\). There is a uniquely determined \(c_*\in(2\pi,3\pi)\) at which
\[
F(c)=\frac{2c(c-\sin c)}{c^2-2+2\cos c}\quad(c>0),\qquad F(0)=4
\]
attains its global minimum on \([0,\infty)\). Its defining equation is
\[
-c^3\cos c+3c^2\sin c+6c(\cos c-1)
   +2\sin c-\sin(2c)=0.
\]
Numerically, \(c_*=7.540314189594786\ldots\) and \(F(c_*)=1.791269160760916\ldots\). The **sharp globally optimized squared-error law** is
\[
\lim_{n\to\infty}(n+3)\min_{0\le\theta\le\pi}E_n(\theta)
  =F(c_*).
\]
Every sequence of exact minimizing angles \(\theta_n\) satisfies
\[
(n+3)\theta_n\longrightarrow c_*.
\]
For each fixed \(c\ge0\), \((n+3)E_n(c/(n+3))\to F(c)\). In contrast, if \((n+3)\theta_n\to\infty\), then \((n+3)E_n(\theta_n)\to2\). Thus the optimal separation is critical, neither coincident nor macroscopic.

The limiting profile has infinitely many strict *interference windows*: for each integer \(m\ge1\), let \(t_m\) be the unique root of \(\tan t=t\) in \((m\pi,m\pi+\pi/2)\). Then
\[
F(c)<2\ \Longleftrightarrow\
c\in\bigcup_{m\ge1}(2m\pi,2t_m).
\]
The first window contains the unique global optimum.

## Assumptions and scope

The optimization is over unrestricted complex polynomial coefficients of degree at most \(n\), in the classical Hardy coefficient norm, and over the shorter angular separation of two roots on the unit circle. At \(\theta=0\), the factor has a double root; this endpoint is included. For \(\theta>0\), the two roots are distinct. All asymptotic statements concern squared norm and \(N=n+3\), not its square root. Numerical values are approximations, not definitions of the constants.

## Proof

**1. Exact finite problem.** Put \(r=1-f_\theta p\); then \(\deg r\le n+2=N-1\). For \(\theta>0\), divisibility by \(f_\theta\) is equivalent to \(r(1)=r(e^{i\theta})=1\). The polynomial evaluation kernel is \(K_N(z,w)=\sum_{k=0}^{N-1}z^k\overline w^{\,k}\). Write \(S_N(\theta)=\sum_{k=0}^{N-1}e^{ik\theta}\). The Gram matrix at the two roots has diagonal entries \(N\), off-diagonal entries \(S_N\) and \(\overline S_N\). Minimal-norm interpolation gives
\[
 E_n(\theta)=\frac{2(N-\operatorname{Re}S_N(\theta))}{N^2-|S_N(\theta)|^2}
 \qquad(0<\theta\le\pi).
\]
The determinant is strictly positive because the two evaluation functionals are linearly independent on polynomials of degree at most \(N-1\), with \(N\ge3\). For \(\theta=0\), the constraints become \(r(1)=1\) and \(r'(1)=0\). Inverting the moment Gram matrix of \(1\) and \(k\) for \(0\le k<N\) gives
\[
 E_n(0)=\frac{2(2N-1)}{N(N+1)}.
\]
This equals the continuous limit of the two-point formula as \(\theta\downarrow0\).

**2. Compact critical scaling and escape.** Put \(U_N\) uniformly distributed on \(\{0,1/N,\ldots,(N-1)/N\}\), and \(s_N(c)=\mathbb E(e^{icU_N})\). For \(0<c\le N\pi\),
\[
NE_n(c/N)=\frac{2[1-\operatorname{Re}s_N(c)]}{1-|s_N(c)|^2}.
\]
Represent the numerator as \(2\mathbb E[1-\cos(cU_N)]\) and the denominator as \(\mathbb E[1-\cos(c(U_N-U_N'))]\) for an independent copy \(U_N'\). After division by \(c^2\), both extend continuously to \(c=0\), with denominator tending to \(\operatorname{Var}(U_N)>0\); the resulting ratio equals \(\mathbb E(U_N^2)/\operatorname{Var}(U_N)=2(2N-1)/(N+1)\) there. Riemann sums and uniform continuity now give locally uniform convergence on \([0,\infty)\) to the same ratio with \(U\sim\operatorname{Uniform}[0,1]\). Evaluating its characteristic function \(s(c)=(e^{ic}-1)/(ic)\) gives the stated \(F(c)\), including \(F(0)=4\).

If \(c_N=N\theta_N\to\infty\) with \(0<\theta_N\le\pi\), the geometric-sum estimate
\[
 |S_N(\theta_N)|/N\le\frac{1}{N\sin(\theta_N/2)}\le\frac{\pi}{c_N}
\]
forces \(NE_n(\theta_N)\to2\).

**3. Interference windows.** For \(c>0\), the denominator \(D(c)=c^2-2(1-\cos c)>0\). Hence
\[
 F(c)-2=\frac{-2[c\sin c-2(1-\cos c)]}{D(c)}.
\]
Using \(t=c/2\), its bracket equals \(4\sin t\cos t(t-\tan t)\) wherever \(\cos t\ne0\), with continuous extension across the removable points. For \(0<c<2\pi\) it is negative. In each interval \(2m\pi<c<2(m+1)\pi\), \(m\ge1\), it is positive precisely up to the unique root \(t_m\) of \(\tan t=t\) in \((m\pi,m\pi+\pi/2)\). Uniqueness follows since \(\tan t-t\) increases strictly there from a negative value to \(+\infty\). This proves the exact window classification.

**4. Uniqueness of the first-window minimum.** Differentiating \(F/2=c(c-\sin c)/D(c)\), the sign of its derivative is the sign of
\[
 W(c)=-c^3\cos c+3c^2\sin c+6c(\cos c-1)+2\sin c-\sin(2c).
\]
A cancellation yields \(W'(c)=c^3\sin c-4(1-\cos c)^2\). On \((2\pi,3\pi)\), the positive ratio
\[
R(c)=\frac{4(1-\cos c)^2}{c^3\sin c}
\]
strictly increases from zero to infinity, because, with \(t=c/2\in(\pi,3\pi/2)\),
\[
 \frac{d}{dc}\log R(c)
  =\frac32\cot t+\frac12\tan t-\frac3c
  \ge\sqrt3-\frac3{2\pi}>0.
\]
Thus \(W'\) changes once from positive to negative. Since \(W(2\pi)=-(2\pi)^3<0\) and \(W(3\pi)=(3\pi)^3-12(3\pi)>0\), \(W\) itself has exactly one zero in \((2\pi,3\pi)\), at which \(F\) changes from decreasing to increasing. As \(F<2\) in the first window, this minimum lies inside \((2\pi,2t_1)\).

**5. Global exclusion and rigidity.** Outside the first window and below \(4\pi\), \(F\ge2\). For \(c\ge4\pi\), if \(F(c)<2\), its sign formula and \(c\sin c-2(1-\cos c)\le c\) yield
\[
 F(c)\ge2-\frac{2c}{c^2-4}
 \ge2-\frac{8\pi}{16\pi^2-4}
 > F(5\pi/2).
\]
The final inequality is exact: the difference equals
\[
\frac{2(15\pi^3-32\pi^2-2\pi+8)}{(2\pi-1)(2\pi+1)(25\pi^2-8)}>0;
\]
the numerator polynomial is positive and increasing for arguments at least \(3\), while \(\pi>3\). Thus the unique first-window minimum is the unique global minimum.

Continuity on \([0,\pi]\) gives a minimizing \(\theta_n\) at each finite degree. Testing \(\theta=c_*/N\) bounds the scaled optimal value by \(F(c_*)+o(1)<2\). The escape estimate forces all minimizers to have bounded \(N\theta_n\). Every subsequential limit then minimizes \(F\) by locally uniform convergence. Global uniqueness forces \(N\theta_n\to c_*\), and the optimal values converge to \(F(c_*)\), as claimed.

## Verification

The included `checker.py` (Python standard library) checks the finite Gram expression against independently assembled least-squares normal equations for degrees \(0\) through \(7\), checks the coalescing endpoint, compares multiple critical scalings with the limiting profile, checks the unique stationary root numerically, and tests representative points of six interference windows. A replay yielded 10,167 passed finite assertions and approximations \(c_*=7.540314189594786\) and \(F(c_*)=1.791269160760916\). These finite computations corroborate but do not establish the quantified infinite-degree and global statements, which follow from the proof above.

## Relationship to prior work

Bénéteau, Manolaki and Seco give the general finite-dimensional kernel-Gram formula for optimal polynomial residuals with fixed simple zeros, and separately handle repeated zeros. Acuaviva and Seco analyze their zero distribution and explicitly examine a two-root Gram matrix at fixed angular separation. Those foundational exact formulas and qualitative convergence results are not claimed here. The present claim concerns a different optimization: the globally best **degree-dependent zero separation**, its unique \(1/n\)-scale, its sharp limiting constant, and the infinitely many interference windows. The cited results supply the interpolation starting point but do not report the sharp spacing optimum or its rigidity. This is a comparison with inspected sources, not a proof that no equivalent result exists elsewhere.

## Limitations

Only the classical unweighted Hardy space, the reciprocal of a quadratic with two boundary zeros, and squared-error minimization are addressed. The theorem does not assert uniqueness of the optimal angle for every finite degree, higher-degree multi-zero optimal designs, or quantitative finite-degree convergence rates. No independent validation or exhaustive historical-priority certificate is claimed.

## References

1. C. Bénéteau, M. Manolaki and D. Seco, *Boundary behavior of optimal polynomial approximants*, arXiv:1901.00694 (first posted January 3, 2019), Theorem 1.1 and Section 7; https://arxiv.org/abs/1901.00694 .
2. A. Acuaviva and D. Seco, *Equidistribution of zeros of some polynomials related to cyclic functions*, arXiv:2110.06788v1 (October 13, 2021); *Analysis and Mathematical Physics* 12 (2022), 53, Lemma 2.1, Example 3.2; https://arxiv.org/abs/2110.06788 .
3. T. Qian, *n-Best Kernel Approximation in Reproducing Kernel Hilbert Spaces*, arXiv:2201.07228 (January 18, 2022), for broader existence context; https://arxiv.org/abs/2201.07228 .
