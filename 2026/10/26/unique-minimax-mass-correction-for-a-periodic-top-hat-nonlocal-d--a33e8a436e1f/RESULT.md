# Unique minimax mass correction for a periodic top-hat nonlocal diffusion symbol

## Finding

For the one-dimensional top-hat nonlocal diffusion operator on every periodic interval, the ideal additive inverse-Poisson-plus-mass Fourier preconditioner has a **unique coefficient minimizing the worst spectral condition number uniformly over all periods and interaction horizons**. The kernel-mass coefficient \(\beta=1/2\) gives a uniform condition number **strictly above four**, whereas \(\beta=1/6\) gives a uniform condition number **at most two**. Thus the latter already improves this worst-case spectral condition number by a factor greater than two; the optimal coefficient has a rigorous explicit lower bound and lies below \(0.18\).

More precisely, with
\[
 a(t)=1-\frac{\sin t}{t},\qquad
 p_\beta(t)=2a(t)\left(\beta+\frac1{t^2}\right),\qquad
 H(t)=\frac{1}{6a(t)}-\frac1{t^2},\quad t>0,
\]
put
\[
 \beta_\star=\max_{t>0}H(t).
\]
The maximum exists and satisfies the proved bound
\[
 \frac16<H(5\pi/2)\le\beta_\star<\frac9{50}.
\]
Let \(\mathcal K(\beta)\) denote the supremum of the spectral condition numbers of the preconditioned operators over all periods and all positive horizons (equivalently the ratio of the supremum and infimum of \(p_\beta\) over positive real frequencies). Then
\[
 \beta_\star=\operatorname*{argmin}_{\beta>0}\mathcal K(\beta)
 \quad\text{uniquely},\qquad
 \mathcal K(\beta_\star)\le2<4<\mathcal K(1/2).
\]
Numerical one-dimensional optimization suggests \(\beta_\star\approx0.1747779924\) and \(\mathcal K(\beta_\star)\approx1.700200565\); these decimals are diagnostic and are not used to prove the universal claims.

## Assumptions and scope

Fix an arbitrary circumference \(L>0\), interaction horizon \(\delta>0\), and periodic mean-zero functions with Fourier frequencies \(\xi_k=2\pi k/L\), \(k\in\mathbb Z\setminus\{0\}\). Define
\[
 (\mathcal A_\delta f)(x)=\delta^{-3}\int_{-\delta}^{\delta}\bigl(f(x)-f(x+z)\bigr)\,dz,
 \qquad
 \mathcal B_{\beta,\delta}=(-\partial_x^2)^{-1}+\beta\delta^2 I,\quad\beta>0.
\]
Translations are periodic. The kernel is \(\rho(z)=1/2\) on \([-1,1]\), so its mass is one; the 2026 additive preconditioner's kernel-mass prescription specializes to \(\beta=1/(2\int\rho)=1/2\). The inverse Poisson operator is on the mean-zero space, and \(\mathcal B_{\beta,\delta}\mathcal A_\delta\) is a bounded positive diagonal Fourier multiplier. Every periodic spectral condition number uses the supremum and infimum over all nonzero Fourier modes (both finite and limiting spectral endpoints). The *uniform* condition number is the supremum over \(L,\delta>0\); the theorem does not say that \(\beta_\star\) optimizes each individual finite period.

## Proof

**Symbol reduction.** On \(e^{i\xi x}\), direct integration gives
\[
 \widehat{\mathcal A_\delta}(\xi)=2\delta^{-2}\left(1-\frac{\sin(\delta\xi)}{\delta\xi}\right),
\]
so the composite multiplier equals \(p_\beta(t)\) at \(t=\delta|\xi|\). It is strictly positive for \(t>0\), since \(\sin t<t\). It has endpoint limits
\[
 \lim_{t\downarrow0}p_\beta(t)=\frac13,\qquad
 \lim_{t\to\infty}p_\beta(t)=2\beta.
\]
It follows that \(\mathcal K(\beta)=\sup_{t>0}p_\beta(t)/\inf_{t>0}p_\beta(t)\). Indeed every periodic frequency grid is a subset of the positive frequencies, and taking \(2\pi\delta/L\downarrow0\) makes the grids dense on each compact positive-frequency interval; endpoint values are obtained by frequencies tending to zero or infinity. This is a uniform-over-periods statement, not a finite-matrix assertion.

**Existence and location of the threshold.** The identity \(p_\beta(t)\ge1/3\) is equivalent to \(\beta\ge H(t)\). For \(0<t\le\pi\), the sine upper Taylor bound and \(t^2<14\) imply
\[
 \frac{\sin t}{t}\le1-\frac{t^2}{6}+\frac{t^4}{120}
 \le\frac6{6+t^2};
\]
the last difference is \(t^4(14-t^2)/[120(6+t^2)]\). Thus \(p_{1/6}(t)\ge1/3\). For \(\pi\le t\le2\pi\), \(\sin t\le0\), so again \(p_{1/6}(t)\ge1/3\). Therefore \(H(t)\le1/6\) throughout \((0,2\pi]\). At \(t=5\pi/2\), where \(\sin t=1\), the inequality \(t^2>6(t-1)\) gives \(H(t)>1/6\). Moreover \(H(t)\to1/6\) as \(t\to\infty\), and \(H(t)\to1/20\) as \(t\downarrow0\). Consequently the global maximum is attained at some \(t_\star>2\pi\).

For \(t\ge2\pi>6\), \(\sin t\le1\) yields
\[
 H(t)\le\frac{t}{6(t-1)}-\frac1{t^2}<\frac9{50}.
\]
The strict last inequality reduces to positivity of \(2t^3-27t^2+150t-150\), which is already positive at \(t=6\) (value \(210\)) and has everywhere-positive derivative \(6(t^2-9t+25)\). Thus \(1/6<\beta_\star<9/50\), and \(p_{\beta_\star}(t)\ge1/3\) for all \(t>0\), with equality at \(t=t_\star\) and in the limit \(t\downarrow0\). Therefore \(\inf_{t>0}p_{\beta_\star}(t)=1/3\).

**Separation of maximum and minimum frequencies.** When \(t\ge2\pi>6\), positivity of \(\beta_\star\) and \(\sin t\ge-1\) imply
\[
 p_{\beta_\star}(t)
 \le2\left(1+\frac1t\right)\left(\beta_\star+\frac1{t^2}\right)
 <2\left(1+\frac16\right)\left(\frac9{50}+\frac1{36}\right)
 =\frac{1309}{2700}<\frac8{15}.
\]
But \(p_{\beta_\star}(\pi)=2(\beta_\star+1/\pi^2)>2(1/6+1/10)=8/15\), since \(\pi^2<10\). By continuity, the global maximum is attained at some \(u_\star\in(0,2\pi)\). In particular, \(u_\star<t_\star\).

**Global minimax and uniqueness.** For \(\beta>\beta_\star\), the value \(p_\beta(u_\star)>p_{\beta_\star}(u_\star)\), whereas \(\inf_t p_\beta(t)\le1/3\) by the zero-frequency limit. Hence \(\mathcal K(\beta)>\mathcal K(\beta_\star)\). If instead \(0<\beta<\beta_\star\), then \(p_\beta(t_\star)<1/3\), so
\[
 \mathcal K(\beta)\ge
 \frac{p_\beta(u_\star)}{p_\beta(t_\star)}.
\]
For any \(0<u<t\), the ratio
\[
 \frac{p_\beta(u)}{p_\beta(t)}
 =\frac{a(u)}{a(t)}\frac{\beta+u^{-2}}{\beta+t^{-2}}
\]
is strictly *decreasing* as \(\beta\) increases, since \(t^{-2}-u^{-2}<0\). Therefore \(\mathcal K(\beta)>p_{\beta_\star}(u_\star)/p_{\beta_\star}(t_\star)=\mathcal K(\beta_\star)\). The minimizer is unique.

**Certified greater-than-two improvement.** Write
\[
 p_{1/6}(t)=\frac13F(t),\qquad
 F(t)=\left(1-\frac{\sin t}{t}\right)\left(1+\frac6{t^2}\right).
\]
We prove \(9/10\le F(t)\le9/5\) for every \(t>0\). The lower bound is already at least one for \(t\le2\pi\). For \(t\ge2\pi>6\), it follows from
\[
 F(t)\ge\left(1-\frac1t\right)\left(1+\frac6{t^2}\right)\ge\frac9{10}:
\]
the second comparison is equivalent to \(t^3-10t^2+60t-60\ge0\); this cubic is positive at \(6\) (value \(156\)) and strictly increasing because its derivative \(3t^2-20t+60\) is positive for all real \(t\).

For \(0<t\le19/5\), the alternating Taylor lower bound \(\sin t/t\ge1-t^2/6+t^4/120-t^6/5040\) gives
\[
 F(t)\le 1+\frac{7t^2}{60}-\frac{t^4}{140}+\frac{t^6}{5040}<\frac95.
\]
Indeed the polynomial in \(v=t^2\) has derivative \([(v-12)^2+52]/1680>0\) and takes a value below \(9/5\) at \(v=361/25\). For \(t\ge19/5\), simply use
\[
 F(t)\le\left(1+\frac1t\right)\left(1+\frac6{t^2}\right)
 \le\frac{12264}{6859}<\frac95.
\]
Thus \(3/10\le p_{1/6}(t)\le3/5\), whence \(\mathcal K(1/6)\le2\).

Finally, at \(t=4\),
\[
 p_{1/2}(4)=\frac98\left(1-\frac{\sin4}{4}\right)>\frac43.
\]
The strict inequality follows from \(\sin4<-20/27\), itself certified by the sine Taylor upper polynomial through degree \(13\):
\[
 \sin4\le\sum_{j=0}^{6}\frac{(-1)^j4^{2j+1}}{(2j+1)!}
 =-\frac{131356}{173745}< -\frac{20}{27}.
\]
Since \(\inf_t p_{1/2}(t)\le\lim_{t\downarrow0}p_{1/2}(t)=1/3\), it follows that \(\mathcal K(1/2)>4\). Combining the estimates proves the claim.

## Verification

The standalone `check.py` supplied with this result checks exact rational arithmetic appearing in the proof, stress-tests the symbol on a logarithmic/dense finite frequency grid, computes illustrative scalar optima, and checks representative periodic Fourier grids. Run with `python check.py` (requires Python, NumPy, SciPy). The exact Taylor and polynomial inequalities and the monotonicity argument above—not finite grids—establish the universal conclusions. The finite checks cannot certify global maxima or literature originality.

## Relationship to prior work

Lu, Nie, H. Zhang, and P. Zhang (2026) motivate the inverse-Poisson-plus-mass additive preconditioner, fix the mass coefficient \(\beta=1/(2\mu_\rho)\), and prove uniform finite-element spectral equivalence for volume-constrained nonlocal diffusion. This result instead optimizes the *ideal periodic one-dimensional Fourier-symbol condition number* for the admissible top-hat kernel; it neither re-proves nor strengthens their finite-element uniform bound. Zhang, Sun, Sun, and Zhang (2026) study a different two-level Toeplitz \(\tau\)-preconditioning mechanism, with a different matrix class and spectral statement. Standard Fourier multiplier and Chebyshev/minimax ideas motivate the analysis; the contribution assessed here is the exact coefficient characterization, uniqueness mechanism through separated extremizers, and certified factor-of-two-plus quantitative reversal for this canonical kernel.

## Limitations

The exact coefficient is characterized as a one-variable global maximum rather than a closed-form elementary constant; reported decimals are numerical only. The theorem is for exact Fourier multipliers on one-dimensional mean-zero *periodic* domains, with the piecewise constant interval kernel and arbitrary periods/horizons. It does **not** assert that the same tuning optimizes a volume-constrained Dirichlet finite-element matrix, an approximate multigrid solver, or practical PCG iteration counts. An older related Toeplitz-preconditioner article was accessible in abstract but not full text; hidden equivalences in broader spectral preconditioning literature remain possible.

## References

1. J. Lu, Y. Nie, H. Zhang, and P. Zhang, *A mesh- and horizon-robust preconditioner for finite element discretizations of volume-constrained nonlocal diffusion problems*, arXiv:2609.24143v1 (first public 2026-09-21), especially Sections 1–2, 5–7. https://arxiv.org/abs/2609.24143
2. J. Zhang, T. Sun, H. Sun, and J. Zhang, *Spectral Analysis of \(\tau\)-Preconditioners for Two-Level Toeplitz Systems with Applications in Nonlocal Diffusion Models*, *Journal of Scientific Computing* 106, article 21 (2026), DOI:10.1007/s10915-025-03150-2. Abstract-level comparison only.
3. Q. Du, M. Gunzburger, R. B. Lehoucq, and K. Zhou, *Analysis and approximation of nonlocal diffusion problems with volume constraints*, *SIAM Review* 54(4), 667–696 (2012). Background only; no full-text novelty comparison claimed.
