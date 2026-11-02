# A logarithmic–logarithmic lattice law for asymmetric exponential Gabor frames

## Finding

Fix two unequal positive decay rates \(0<r<R\). The normalized two-sided exponential window is
\[
g(t)=\sqrt{\frac{2rR}{r+R}}\begin{cases}e^{rt},&t<0,\\ e^{-Rt},&t\geq0.\end{cases}
\]
For an integer redundancy \(n\geq2\), let \(A_n(\eta)\) and \(B_n(\eta)\) denote the sharp lower and upper frame bounds of the rectangular Gabor family \(\mathcal G(g,(\eta/n)\mathbb Z\times(1/\eta)\mathbb Z)\). Put \(\kappa_n(\eta)=B_n(\eta)/A_n(\eta)\). Every global maximizer \(\eta_{A,n}\) of \(A_n\), every global minimizer \(\eta_{B,n}\) of \(B_n\), and every global minimizer \(\eta_{\kappa,n}\) of \(\kappa_n\) obey, as \(n\to\infty\),
\[
\begin{aligned}
r\eta_{A,n}&=2\log n-\log\log n+\log\!\frac{3r}{R-r}+o(1),\\
r\eta_{\kappa,n}&=2\log n-\log\log n+\log\!\frac{2r}{R-r}+o(1),\\
r\eta_{B,n}&=2\log n-\log\log n+\log\!\frac{3r}{2(R-r)}+o(1).
\end{aligned}
\]
In particular the three global optimizer locations are distinct and ordered \(\eta_{B,n}<\eta_{\kappa,n}<\eta_{A,n}\) for all sufficiently large \(n\). This asserts neither finite-\(n\) uniqueness nor any estimate uniform as the contrast \(R-r\) tends to zero.

There is also a sharp, nonquadratic global-scale penalty profile. Let \(L=\log n\), \(\eta_n(t)=(2L-\log L+t)/r\), and define
\[
D_A=1-A_n/n,\qquad D_B=B_n/n-1,\qquad D_\kappa=\kappa_n-1.
\]
For \(X\in\{A,B,\kappa\}\), write \(t_A=\log(3r/(R-r))\), \(t_B=\log(3r/[2(R-r)])\), \(t_\kappa=\log(2r/(R-r))\) and \(K_A=2R/(3r)\), \(K_B=4R/(3r)\), \(K_\kappa=2R/r\). Uniformly for \(t\) in any fixed compact set,
\[
\frac{n^2}{L}\big(D_X(\eta_n(t))-D_X(\eta_n(t_X))\big)
\longrightarrow K_X\big(t-t_X+e^{-(t-t_X)}-1\big).
\]
The limit is strictly positive away from \(t=t_X\) and hence quantitatively describes lattice-shape misspecification at the critical scale. Furthermore,
\[
\lim_{n\to\infty}\frac{n^2}{(\log n)^2}
\begin{pmatrix}1-A_n(\eta_{A,n})/n\\B_n(\eta_{B,n})/n-1\\\kappa_n(\eta_{\kappa,n})-1\end{pmatrix}
=\begin{pmatrix}2R/(3r)\\4R/(3r)\\2R/r\end{pmatrix}.
\]

## Assumptions and scope

All limits hold with fixed \(0<r<R\) and integer \(n\to\infty\). The Fourier convention for modulation is \(M_b f(t)=e^{2\pi i bt}f(t)\). The two rates are not interchangeable without time reversal; by that reversal any unequal pair reduces to \(r<R\). The Gabor frame property follows from the finite-type totally-positive frame-set theorem, since the window is the normalized convolution of a left and a right one-sided exponential and the lattice area equals \(1/n<1\) [1,2]. Frame bounds are sharp operator spectral extrema.

## Proof

**Exact scalar frame symbol.** Set \(a=\eta/n\), \(c^2=2rR/(r+R)\), and for \(0\leq x<a\) define
\[
\begin{aligned}
d_a(x)&=ac^2\left(\frac{e^{-2Rx}}{1-e^{-2Ra}}+\frac{e^{2r(x-a)}}{1-e^{-2ra}}\right),\\
U_a(x)&=\frac{e^{2r(x-a)}}{1-e^{-2ra}}+\frac{e^{(r-R)x}}{1-e^{-(R-r)a}},\\
V_a(x)&=\frac{e^{-2Rx}}{1-e^{-2Ra}}-\frac{e^{(r-R)x}}{1-e^{-(R-r)a}}.
\end{aligned}
\]
For \(0<q<1\) let \(P(q,v)=(q\cos v-q^2)/(1-2q\cos v+q^2)\). The Walnut representation of the frame operator, followed by discrete Fourier transform along the step \(\eta=na\), shows that \(S_n/n\) is unitarily equivalent (with finite multiplicity) to multiplication on \([0,a)\times[0,2\pi)\) by
\[
F_{n,\eta}(x,v)=d_a(x)+2ac^2\{U_a(x)P(e^{-r\eta},v)+V_a(x)P(e^{-R\eta},v)\}.
\]
Consequently \(A_n/n=\min F_{n,\eta}\), \(B_n/n=\max F_{n,\eta}\), with minimum and maximum over the compact quotient torus (the one-sided endpoint values agree). The identity follows directly by splitting the geometric series
\[
a\sum_{k\in\mathbb Z}g(x+ka)g(x+ka-m\eta)
=ac^2\big(U_a(x)e^{-rm\eta}+V_a(x)e^{-Rm\eta}\big),\quad m\geq1.
\]
Absolute exponential convergence validates the Fourier transformation and all rearrangements.

**Uniform small-cell expansion.** The autocorrelation at positive lag is exactly
\[
H(s)=\int_\mathbb Rg(t)g(t-s)\,dt
=\frac{Re^{-rs}-re^{-Rs}}{R-r}\quad(s>0).
\]
The Poisson formula applied to \(|g|^2\), whose Fourier transform is \(4rR/[(2R+2\pi i\xi)(2r-2\pi i\xi)]\), gives uniformly for \(u\in[0,1]\)
\[
d_a(au)=1+2rRa^2\left(u^2-u+\frac16\right)+O_{r,R}(a^3).
\]
For \(s\geq1\), the piecewise-smooth function \(g(t)g(t-s)\) has a distributional second derivative of total variation \(O_{r,R}(e^{-rs})\). Its nonzero Fourier modes therefore yield the uniform shifted trapezoid bound
\[
\sup_{x\in[0,a]}\left|a\sum_k g(x+ka)g(x+ka-s)-H(s)\right|
\leq C_{r,R}a^2e^{-rs},\quad 0<a\leq1.
\]
Thus, uniformly for \(\eta\geq1\), \(a\leq1\), the exact spectral symbol is
\[
F_{n,\eta}(au,v)=1+2rRa^2\left(u^2-u+\tfrac16\right)+2H(\eta)\cos v
+O_{r,R}\big(a^3+a^2e^{-r\eta}+e^{-2r\eta}\big).
\]
Since the Bernoulli polynomial attains its minimum \(-1/12\) and maximum \(1/6\), independently of the cosine extrema, it follows that
\[
\begin{aligned}
D_A&=\frac{rR\eta^2}{6n^2}+2H(\eta)+O(E),\\
D_B&=\frac{rR\eta^2}{3n^2}+2H(\eta)+O(E),\\
D_\kappa&=\frac{rR\eta^2}{2n^2}+4H(\eta)+O\big(E+(a^2+H(\eta))^2\big),
\end{aligned}
\]
where \(E=a^3+a^2e^{-r\eta}+e^{-2r\eta}\), uniformly in the stated region. These are two-sided sharp asymptotics of the true spectral extrema, rather than sampled bounds.

**Global localization of all optimizers.** All extrema exist: the frame bounds depend continuously on \(\eta>0\), while as \(\eta\to\infty\) the spatial periodization \(d_a\) develops arbitrarily large contrast; as \(\eta\to0\) the frequency periodization has a large peak at phase zero and collapses at phase \(\pi\). More explicitly, for small \(a\), \(F\) approaches \(\sum_{m\in\mathbb Z}H(|m|\eta)e^{imv}\). For \(\eta\downarrow0\) its value at \(v=0\) diverges like \(1/\eta\) and at \(v=\pi\) vanishes, by Poisson summation and the \(O(|\xi|^{-4})\) decay of \(|\widehat g(\xi)|^2\). This also applies when \(\eta\downarrow0\) with \(n\to\infty\), as the shifted trapezoid error is \(O(a^2)\). For bounded \(\eta\) separated from zero, the limiting positive autocorrelation Fourier coefficient \(H(\eta)\) makes the profile nonconstant. Therefore any sequence with any one of the three defects tending to zero must satisfy \(\eta\to\infty\). Likewise it must have \(a\to0\), because the strictly convex, nonconstant function \(d_a\) has nonzero contrast for each fixed \(a>0\) and unbounded contrast as \(a\to\infty\).

For the trial parameter \(\eta_\mathrm{trial}=(2\log n-\log\log n)/r\), all three defects are \(O((\log n)^2/n^2)\). Since \(F\) averaged over phase \(v\) equals \(d_a\), the small-cell spatial contrast supplies \(D_X\geq C_X a^2+O(a^3)\) with \((C_A,C_B,C_\kappa)=(rR/6,rR/3,rR/2)\). Hence every optimizer has \(a=O(\log n/n)\). The preceding full uniform expansion, and its positive \(H\)-term, then imply \(e^{-r\eta}=O((\log n)^2/n^2)\), so \(r\eta\geq 2\log n-2\log\log n-O(1)\). Comparing the leading \(C_Xa^2\) term with the trial deficit improves the other side to \(r\eta\leq2\log n+O(\log\log n)\). Thus every global optimizer lies in the logarithmic window \(r\eta=2\log n-\log\log n+t\) with \(|t|=O(\log\log n)\).

**Sharp log–log centering and profile.** Put \(L=\log n\) and \(M=R/(R-r)\). Uniformly throughout the just-derived window,
\[
H(\eta)=M\,Le^{-t}/n^2+o(L/n^2),
\]
where the remainder is uniform even for \(|t|=O(\log L)\); the terms of order \(e^{-R\eta}\) and \(e^{-2r\eta}\) are negligible. Subtracting the deficit at any fixed \(t_0\) yields
\[
\frac{n^2}{L}[D_X(\eta_n(t))-D_X(\eta_n(t_0))]
=\frac{4C_X}{r^2}(t-t_0)+E_XM(e^{-t}-e^{-t_0})+o(1),
\]
where \((E_A,E_B,E_\kappa)=(2,2,4)\). The error is uniform in the window. Each resulting strictly convex function is coercive in both directions and has its sole minimum at \(e^{-t_X}=4C_X/(E_XMr^2)\). It follows that every actual global optimizing \(t\) is bounded and converges to \(t_X\); evaluating the differences at this minimum yields the asserted penalty profile. Substituting \(\eta\sim2L/r\) in the leading spatial term yields the three limiting sharp defect constants. Strict separation of the limiting \(t_X\) establishes eventual optimizer ordering. This completes the proof.

## Verification

The accompanying `checker.py` independently evaluates the direct translated-window sums against the closed geometric formulas, checks autocorrelations by numerical quadrature, and tests the phase symbol against the predicted leading orders and finite-\(n\) optimizer ordering. These finite checks are diagnostic only. All infinite-dimensional claims and uniform limits follow from the analytic derivation above.

## Relationship to prior work

Faulhuber–Shafkulovska [3], originally publicly posted 2022-04-06, gives sharp rectangular optimization for the **symmetric** two-sided exponential \(e^{-\gamma|t|}\), along with other window families. Its symmetric exact bounds have a different high-density structure; they do not imply the fixed unequal-rate formulas here by unitary dilation or reflection, which preserve equality of rates. Gröchenig–Stöckler [1] and Gröchenig [2] establish the applicable Gabor frame-set property, not the optimizing unequal-tail spectral asymptotics. The present claim is the contrast-dependent \(-\log\log n\) centering, three separated constants, and universal quantitative penalty profile for **fixed** unequal rates. An earlier general optimization theorem, if found, may still dominate this result; priority is provisional.

## Limitations

No assertion is made for an equal-rate window, contrast tending to zero with redundancy, arbitrary irrational redundancy, nonrectangular lattices, or uniqueness of finite-\(n\) optimizing lattices. The time-reversal reduction accounts for the opposite ordering of decay rates. The convergence in the profile is locally uniform in the centered parameter, and only the stated asymptotic window contains global optimizers. The supporting numerical checker is not an infinite-dimensional certificate. No independent audit has been performed.

## References

[1] K. Gröchenig and J. Stöckler, *Gabor Frames and Totally Positive Functions*, arXiv:1104.4894 (first public 2011-04-26), https://arxiv.org/abs/1104.4894.

[2] K. Gröchenig, *Totally Positive Functions and Gabor Frames over Rational Lattices*, arXiv:2301.00857 (first public 2023-01-02), https://arxiv.org/html/2301.00857v1.

[3] M. Faulhuber and I. Shafkulovska, *Gabor Frame Bound Optimizations*, arXiv:2204.02917 (first public 2022-04-06), https://arxiv.org/html/2204.02917v2; *Applied and Computational Harmonic Analysis* 67 (2023), article 101574.
