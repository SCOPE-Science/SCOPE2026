# Sharp theta-curvature envelope for Gaussian lifts of rectangular lattices

## Finding

For each positive parameter \(t\), put
\[
\Theta(t)=\sum_{k\in\mathbb Z}e^{-tk^2},\qquad
m(t)=\frac{\sum_{k\in\mathbb Z}k^2e^{-tk^2}}{\Theta(t)},\qquad
\mathcal A(t)=4t^2m(t).
\]
The curvature function \(\mathcal A:(0,\infty)\to(0,\infty)\) is strictly increasing until a unique \(t_\star\in(2,3)\), and strictly decreasing thereafter. Its sole maximizer is characterized by the exact scalar equation
\[
2m(t_\star)=t_\star\left(\frac{\sum k^4e^{-t_\star k^2}}{\Theta(t_\star)}-m(t_\star)^2\right).
\]
Numerically (not as a proof), \(t_\star\approx2.35301528944813\) and \(\mathcal A_\star=\mathcal A(t_\star)\approx3.55027661599222\).

For any integer \(d\ge1\) and side lengths \(a_1,\dots,a_d>0\), let the orthogonal lattice be \(\Lambda=a_1\mathbb Z\times\cdots\times a_d\mathbb Z\). Consider exactly the *coordinate-separable normalized Gaussian lifts*
\[
f_{\mathbf t}(x)=\prod_{j=1}^d\frac1{a_j}\frac{\exp[-t_j(x_j/a_j)^2]}{\sum_{k\in\mathbb Z}\exp[-t_j(x_j/a_j+k)^2]},\qquad t_j>0.
\]
These are positive smooth probability densities which are uniform modulo \(\Lambda\). Their *exact global strong log-concavity parameter*, the infimum over \(x\) of the smallest eigenvalue of \(\nabla^2[-\log f_{\mathbf t}](x)\), is
\[
\boxed{\alpha(\mathbf t)=\min_{1\le j\le d}\frac{\mathcal A(t_j)}{a_j^2}.}
\]
Consequently, if \(L=\max_j a_j\),
\[
\boxed{\sup_{\mathbf t>0}\alpha(\mathbf t)=\frac{\mathcal A_\star}{L^2},}
\]
and the supremum is attained. The complete optimizer set consists of \(t_j=t_\star\) for every \(j\) with \(a_j=L\), and arbitrary \(t_j>0\) with \(\mathcal A(t_j)\ge\mathcal A_\star(a_j/L)^2\) for every shorter side. Thus the same optimized curvature is dimension-independent for all cubic lattices, and the longest side determines the sharp rectangular-lattice value within this Gaussian product family.

## Assumptions and scope

Euclidean derivatives are used, and the lattice is orthogonal in the displayed coordinates. A density is \(\alpha\)-strongly log-concave when \(\nabla^2(-\log f)(x)\succeq\alpha I_d\) for every \(x\). The optimization ranges **only** over positive coordinate-separable Gaussian width parameters \(t_j\). It does not optimize over non-Gaussian lifts, non-diagonal quadratic forms, or nonorthogonal lattices. The constants refer to the actual rescaled coordinates \(x_j/a_j\), not to a different Gaussian normalization. The parameter \(\mathcal A_\star\) is defined by an absolutely convergent theta series and a unique implicit equation.

## Proof

**(1) Exact curvature of a normalized Gaussian lift.** Define \(H_t(z)=\sum_{k\in\mathbb Z}e^{-t(z+k)^2}\) and \(h_t(z)=e^{-tz^2}/H_t(z)\). As \(H_t(z)\) is positive and one-periodic, \(\sum_{k\in\mathbb Z}h_t(z+k)=1\); integrating on a unit cell proves \(\int_{\mathbb R}h_t=1\). For the discrete Gaussian on \(z+\mathbb Z\) with weights proportional to \(e^{-t(z+k)^2}\), differentiation gives
\[
\frac{d^2}{dz^2}[-\log h_t(z)]=4t^2\operatorname{Var}_{z,t}(z+K).
\]
The discrete-Gaussian shift-covariance inequality, reproduced in the cited source as its Lemma 3.2 with a proof by Cauchy--Schwarz and the Gaussian parallelogram identity, gives
\(\operatorname{Var}_{z,t}(z+K)\ge\operatorname{Var}_{0,t}(K)\).
At \(z=0\) equality holds, and symmetry gives \(\operatorname{Var}_{0,t}(K)=m(t)\). This proves that the **exact** global curvature of \(h_t\) is \(\mathcal A(t)\). The product Hessian is diagonal with entries \(\mathcal A(t_j)/a_j^2\) at the origin, and at all other points its entries are at least these. Thus the formula for \(\alpha(\mathbf t)\) is exact, not merely a sufficient bound.

**(2) Differentiation of the theta series.** With \(X=K^2\) under \(\Pr_t(K=k)=e^{-tk^2}/\Theta(t)\), write \(m=\mathbb E X\), \(v=\operatorname{Var}(X)\), and \(\kappa_3=\mathbb E[(X-m)^3]\). Termwise differentiation (locally uniform exponential convergence) yields
\[
m'=-v,\qquad v'=-\kappa_3,\qquad
\mathcal A'=4t(2m-tv),\qquad
(2m-tv)'=-3v+t\kappa_3.
\]

**(3) Positive derivative up to \(t=2\).** Jacobi's Poisson summation identity \(\Theta(t)=\sqrt{\pi/t}\,\Theta(\pi^2/t)\), with \(T=\pi^2/t\), gives
\[
t^2m(t)=t/2-\pi^2m(T),\qquad
\frac{d}{dt}[t^2m(t)]=\frac12-T^2v(T).
\]
If \(0<t\le2\), then \(T\ge\pi^2/2>9/2\). Since \(v(T)\le\mathbb E_TK^4\), and successive positive summands in \(\sum_{k\ge1}k^4e^{-Tk^2}\) have ratio at most \(16e^{-3T}\),
\[
v(T)\le\frac{2e^{-T}}{1-16e^{-3T}}<2.01e^{-T}.
\]
The function \(T^2e^{-T}\) decreases for \(T>2\), whence
\(T^2v(T)<2.01(9/2)^2e^{-9/2}<1/2\).
For the last strict inequality one can use \(e^{9/2}>85\), verified already by the first nine terms of its Taylor series. Hence \(\mathcal A'(t)>0\) on \((0,2]\).

**(4) The third-cumulant bound for \(t\ge2\).** Let \(p_x=\Pr_t(X=x)\), where \(x\) ranges over nonnegative perfect squares. The two-sample identities for variance and centered third moment give
\[
\kappa_3-v=\sum_{x>y}p_xp_y(x-y)^2(x+y-2m-1).
\]
The pair \((x,y)=(1,0)\) contributes \(-2mp_0p_1\). For \(x\ge4\) and \(0\le y<x\), the function \((x-y)^2(x+y-1)\) decreases with \(y\), because its derivative is \((x-y)(2-x-3y)<0\). Therefore all remaining pairs together contribute at most \(\sum_{x\ge4}p_xx^2(x-1)\), and
\[
\kappa_3-v\le-2mp_0p_1+\frac2{\Theta(t)}\sum_{k\ge2}k^4(k^2-1)e^{-tk^2}.
\]
Since \(m\ge p_1=2e^{-t}/\Theta(t)\) and \(p_0=1/\Theta(t)\), it suffices to show
\[
\Theta(t)^2\sum_{k\ge2}k^4(k^2-1)e^{-tk^2}<4e^{-2t}.
\]
For \(t\ge2\), the theta sum obeys \(\Theta(t)\le (1+e^{-t})/(1-e^{-t})<4/3\), since \(e^2>7\). The ratio of successive summands on the left for \(k\ge2\) is at most \((27/2)e^{-5t}<1/1000\), so the sum is less than \(49e^{-4t}\). Finally
\[
\Theta(t)^2\sum_{k\ge2}k^4(k^2-1)e^{-tk^2}<\frac{16}{9}\,49e^{-4t}<4e^{-2t},
\]
where the last inequality follows from \(e^{-2t}\le e^{-4}<1/50\). Hence \(\kappa_3<v\) for every \(t\ge2\).

**(5) One and only one maximum.** For \(2\le t\le3\), the formula in (2) and \(\kappa_3<v\) imply \((2m-tv)'<-3v+tv\le0\), with strict negativity including at \(t=3\) because \(\kappa_3<v\). This derivative quantity is positive at \(t=2\) by (3). For \(t\ge3\), the estimate
\[
m(t)\le2\sum_{k\ge1}k^2e^{-3k^2}\le\frac{2q(1+q)}{(1-q)^3}<\frac13,\quad q=e^{-3}<\frac1{20},
\]
combined with \(K^4\ge K^2\), implies \(v\ge m-m^2>2m/3\); hence \(2m-tv<0\) throughout \(t\ge3\). The continuous function \(2m-tv\) therefore crosses zero exactly once in \((2,3)\), from positive to negative. Thus \(\mathcal A\) rises then falls strictly, with the unique global maximum displayed above. As \(t\downarrow0\), Poisson summation yields \(\mathcal A(t)\sim2t\to0\), and as \(t\to\infty\), the leading terms give \(\mathcal A(t)\sim8t^2e^{-t}\to0\).

**(6) Rectangular-lattice optimizer classification.** The exact Hessian formula from (1) implies \(\alpha(\mathbf t)\le\mathcal A_\star/a_j^2\) for each \(j\), hence \(\alpha(\mathbf t)\le\mathcal A_\star/L^2\). Taking all \(t_j=t_\star\) attains it. Equality demands \(\mathcal A(t_j)\ge\mathcal A_\star(a_j/L)^2\) for every \(j\), and in longest coordinates the inequality forces equality at the unique scalar maximizer. Conversely these conditions suffice, proving the claimed complete optimizer set.

## Verification

The accompanying `verify_theta_curvature.py` recomputes theta moments at high precision, locates the unique root numerically, checks sampled derivative signs and the Jacobi moment identity numerically, and samples shifted-coset variances and product-lattice curvature values. It is a finite reproducibility aid, not an infinite proof. The analytic argument above proves existence, uniqueness and sharpness. Run it with Python 3 and `mpmath`; it prints the parameter, curvature, and successful check count.

## Relationship to prior work

Letwin, Reis and Rothvoss (arXiv:2610.29238v2, first public 2026-10-21) develop the normalized Gaussian lattice lift, derive its Hessian as a discrete-Gaussian covariance, and prove the shift-covariance minimum. Their existence theorem gives the universal curvature \(2\pi/e\), but it does not identify this scalar theta optimizer or the sharp rectangular-product Gaussian envelope. The exact curvature identity and shift comparison are explicitly credited, not claimed as novel.

Agostini and Améndola (arXiv:1801.02373) develop discrete Gaussian theta distributions and moment formulas. The present claim is an optimization of the normalized Gaussian quotient curvature, with a uniqueness proof and complete orthogonal-lattice equality conditions, not a new theory of theta moments. Regev and Stephens-Davidowitz (SIAM Journal on Discrete Mathematics 31 (2017), 749--757) provide related lattice Gaussian inequalities. The literature searches undertaken did not identify the exact scalar maximizer as a previously stated theorem; this is not a proof of historical priority.

## Limitations

No statement is made about a globally optimal strongly log-concave lift among **all** densities, or about Gaussian lifts with non-diagonal covariance. The numerical decimal is not an independently certified interval enclosure; the exact theorem uses the implicit theta equation. The shifted-covariance inequality is imported as a published, fully inspected lemma. Independent mathematical audit has not been performed.

## References

1. B. Letwin, V. Reis, and T. Rothvoss, *Strongly Log-Concave Measures and Lattices*, arXiv:2610.29238v2, Theorem 1.1 and Lemmas 3.1--3.3 (2026), https://arxiv.org/html/2610.29238v2.
2. D. Agostini and C. Améndola, *Discrete Gaussian Distributions via Theta Functions*, arXiv:1801.02373v2, especially Sections 2 and 4, https://arxiv.org/html/1801.02373v2.
3. O. Regev and N. Stephens-Davidowitz, *An inequality for Gaussians on lattices*, SIAM Journal on Discrete Mathematics 31 (2017), 749--757.
4. Jacobi's theta transformation, equivalently the Poisson summation formula for a Gaussian (classical identity).
