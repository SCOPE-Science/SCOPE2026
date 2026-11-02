# Exact twofold Gabor bounds and two-ended conditioning laws for causal Erlang windows

## Finding

Fix \(a>0\) and the unnormalized causal second-order exponential window
\[
 g_a(t)=t e^{-at}\mathbf 1_{[0,\infty)}(t).
\]
On \(L^2(\mathbb R)\), consider the rectangular Gabor system
\[
 \mathcal G_a=\{e^{\pi i m t}g_a(t-n):m,n\in\mathbb Z\}.
\]
The translation period is exactly one and the modulation step is exactly one half. The coefficient-energy frame bounds below refer to these unnormalized atoms.

Put
\[
 r=e^{-a},\quad u=1+r^2,\quad v=1-r^2,\quad
 \Delta=\sqrt{u^2-4a^2r^2},
\]
\[
 x_a=\frac{u+2ar^2-\Delta}{2au},\qquad
 y_a=\frac{u+\Delta-2ar^2(3+r^2)/v}{2au}.
\]
For every \(a>0\), \(\Delta>0\), and \(x_a,y_a\in(0,1)\). The optimal lower and upper frame bounds are, **exactly**,
\[
 \boxed{A_a=\frac{2e^{-2ax_a}}{u^2}
    \left[x_a^2+r^2(1-x_a)^2\right]},
\]
\[
 \boxed{B_a=e^{-2ay_a}\left[
    \frac{(r+(1-r)y_a)^2}{(1-r)^4}
   +\frac{(y_a-r(1-y_a))^2}{(1+r)^4}\right]}.
\]
Both are strictly positive. In the unit Zak fundamental cell, the lower-bound fiber is uniquely minimized at spatial coordinate \(x_a\) and frequencies \(\omega=1/4,3/4\); the upper-bound fiber is uniquely maximized at spatial coordinate \(y_a\) and frequencies \(\omega=0,1/2\), where coordinates are understood modulo the Zak quasiperiodicity. In particular, the optimal condition number \(\kappa_a=B_a/A_a\) is explicit.

As the continuous shape parameter approaches its two singular ends, the sharp leading laws are
\[
 \boxed{\lim_{a\downarrow0}A_a=\frac14,\qquad
        \lim_{a\downarrow0}a^4 B_a=1,\qquad
        \lim_{a\downarrow0}a^4\kappa_a=4},
\]
\[
 \boxed{\lim_{a\to\infty}e^{2a}A_a=2,\qquad
        \lim_{a\to\infty}a^2 B_a=2e^{-2},\qquad
        \lim_{a\to\infty}a^2e^{-2a}\kappa_a=e^{-2}}.
\]
Hence the system is a frame at every fixed positive shape parameter but is arbitrarily ill-conditioned as the parameter approaches either endpoint. Continuity and divergence of \(\kappa_a\) at both ends imply that at least one finite positive shape parameter minimizes it; no uniqueness claim about such a minimizer is made.

## Assumptions and scope

The spatial variable is Lebesgue-measured, the Hilbert norm is the usual complex \(L^2\)-norm, translations are \((T_nf)(t)=f(t-n)\), and modulations are \((M_{m/2}f)(t)=e^{\pi i mt}f(t)\). These conventions matter: changing the normalization of the window rescales both bounds quadratically. The shape parameter ranges over every real \(a>0\), and all asserted limits are one-parameter limits for this precise lattice, not uniform statements over varying lattices or more general gamma shapes.

The window is the self-convolution, up to its scalar factor, of two equal-rate one-sided exponentials: \((e^{-a\cdot}\mathbf1_{[0,\infty)})*(e^{-a\cdot}\mathbf1_{[0,\infty)})(t)=g_a(t)\). This elementary repeated-pole totally positive window belongs to the natural class of recent Gabor frame-set results, for which mere existence of a positive frame bound does not determine optimal conditioning.

## Proof

**1. Zak diagonalization with the exact lattice normalization.** Define for \(0\le x<1\) and \(0\le\omega<1\)
\[
 (Zf)(x,\omega)=\sum_{j\in\mathbb Z}f(x+j)e^{-2\pi i j\omega}.
\]
The Zak transform is unitary from \(L^2(\mathbb R)\) to \(L^2([0,1)^2)\) by Fourier-series Parseval. In Zak coordinates, even modulation indices \(m=2k\) give an integer Fourier basis in \((x,\omega)\), with multiplier \(Zg_a(x,\omega)\); odd indices \(m=2k+1\) give the same basis multiplied by a unit-modulus phase, with multiplier \(Zg_a(x,\omega+1/2)\). Summing the two Parseval identities, for every \(f\in L^2(\mathbb R)\), gives the **exact** analysis-energy identity
\[
 \sum_{m,n\in\mathbb Z}|\langle f,M_{m/2}T_ng_a\rangle|^2
 =\int_0^1\!\int_0^1 \mathcal F_a(x,\omega)|Zf(x,\omega)|^2\,d\omega\,dx,
\]
\[
 \mathcal F_a(x,\omega)=|Zg_a(x,\omega)|^2+
 |Zg_a(x,\omega+1/2)|^2.
\]
No additional factor of two occurs in this convention. Thus its essential minimum and maximum are precisely the sharp frame bounds. Continuity on the compact fundamental cell (with the Zak seam identified) turns them into actual extrema.

**2. Closed form and frequency monotonicity.** For \(0\le x<1\), all contributing translates have index \(j\ge0\); the geometric-series identity \(\sum_{j\ge0}(x+j)z^j=[x+(1-x)z]/(1-z)^2\) yields
\[
 Zg_a(x,\omega)=e^{-ax}\frac{x+(1-x)z}{(1-z)^2},
 \qquad z=re^{-2\pi i\omega}.
\]
Write \(c=\cos(2\pi\omega)\) and \(C=x^2+r^2(1-x)^2\). Direct expansion gives
\[
 \mathcal F_a(x,\omega)=e^{-2ax}
 \frac{2C(u^2+4r^2c^2)+16ur^2x(1-x)c^2}
 {(u^2-4r^2c^2)^2}.
\]
For fixed \(x\in[0,1]\), the numerator is a strictly positive affine function of \(c^2\), with nonnegative slope, while the positive denominator strictly decreases with \(c^2\in[0,1]\) because \(u>2r\). Consequently \(\mathcal F_a\) is strictly increasing in \(c^2\). The frequency minimum occurs exactly when \(c=0\), and the maximum exactly when \(|c|=1\). This reduces global optimization to the spatial profiles
\[
 L_a(x)=\frac{2e^{-2ax}}{u^2}[x^2+r^2(1-x)^2]
\]
and
\[
 U_a(x)=e^{-2ax}\left[
 \frac{(r+(1-r)x)^2}{(1-r)^4}
 +\frac{(x-r(1-x))^2}{(1+r)^4}\right].
\]

**3. Unique minimum.** Since \(L_a(0)=L_a(1)=2r^2/u^2\) and \(L_a'(0)<0\), a global minimum is strictly interior. After removal of a positive factor, its critical-point equation is
\[
 au x^2-(u+2ar^2)x+(1+a)r^2=0.
\]
Its discriminant is \(\Delta^2=u^2-4a^2r^2=4r^2(\cosh^2a-a^2)>0\). Here \(\cosh a>a\) for \(a>0\). The derivative of a quadratic times \(e^{-2ax}\) has at most two zeros; if there are two, the first is a minimum and the second a maximum because the derivative is negative at \(x=0\). Therefore the smaller root is the unique global minimizer, namely \(x_a\in(0,1)\), giving the displayed expression for \(A_a\).

**4. Unique maximum.** Write \(U_a(x)=e^{-2ax}W_a(x)\), where \(W_a(x)=c_2x^2+c_1x+c_0\), and
\[
 c_2=\frac{2u}{v^2},\quad
 c_1=\frac{4r^2(3+r^2)}{v^3},\quad
 c_0=\frac{2r^2(1+6r^2+r^4)}{v^4}.
\]
An exact expansion gives
\[
 c_1^2-4c_2c_0=-\frac{16r^2}{v^4},
\]
so the discriminant of the critical-point polynomial \(2ac_2x^2+(2ac_1-2c_2)x+(2ac_0-c_1)\) is \(16\Delta^2/v^4>0\). The endpoint values coincide, \(U_a(0)=U_a(1)\). Furthermore,
\[
 \frac{W_a'(1)}{2W_a(1)}
 =\frac{(1-r^2)(1+3r^2)}{1+6r^2+r^4}
 <\frac{1-r^2}{1+r^2}=\tanh a<a.
\]
Thus \(U_a'(1)<0\), and an interior value just left of one is strictly larger than either endpoint. Since the stationary derivative is a quadratic with negative leading coefficient, there can be at most one local maximum; the larger of its two real roots is therefore the unique global maximizer. The quadratic formula simplifies to \(y_a\in(0,1)\), yielding exactly the expression for \(B_a\).

**5. Endpoint conditioning.** As \(a\downarrow0\), \(r\to1\), \(u\to2\), and \(L_a\) converges uniformly on \([0,1]\) to \([x^2+(1-x)^2]/2\). Its unique minimum is \(1/4\). The maximizer \(y_a\) stays in \((0,1)\), and from the displayed \(U_a\), uniformly on that interval,
\[
 a^4U_a(x)\longrightarrow1.
\]
Therefore \(a^4B_a\to1\). As \(a\to\infty\), \(r=e^{-a}\to0\), the explicit critical-point formulas give
\[
 x_a=(1+a+o(1))r^2,\qquad ay_a\to1.
\]
In the lower-bound expression, \(x_a^2=o(r^2)\), so \(A_a\sim2e^{-2a}\); in the upper one both squares contribute asymptotically \(e^{-2}a^{-2}\), so \(B_a\sim2e^{-2}a^{-2}\). Division proves the two condition-number limits. All steps concern actual global optima, not merely sufficient bounds.

## Verification

A standalone Python 3 checker (`erlang_gabor_check.py`) tests the exact geometrical Zak sum, the two extremizing fibers, and the predicted bound inequalities over a deterministic set of 72,421 assertions. It includes 11 positive shape parameters, dense finite spatial and frequency grids, direct comparisons with an independently computed 5,000-term Zak series at selected points, and both asymptotic regimes. These are finite **consistency** checks only; the preceding argument proves the global formulas for every real \(a>0\) and all signals in \(L^2(\mathbb R)\). To reproduce, run `python3 erlang_gabor_check.py` with a standard Python 3 installation; the test uses only the standard library.

## Relationship to prior work

The 2026 theorem by de Dios Pont, Gröchenig, Liehr, Shafkulovska, and Taylor establishes the frame-set criterion \(\alpha\beta<1\) for continuous integrable totally positive windows, including the present repeated-pole example. It is an existence theorem and does not furnish the specific shape-dependent optimal bounds or either limit for the fixed lattice \((1,1/2)\).

Kloos and Stöckler (2013/2014) analyze Zak transforms of totally positive windows and establish quantitative **lower** frame bounds for a symmetric two-sided exponential, an inequivalent order-two window; their general Zak characterization is a standard tool, not the optimization derived here. Ghosh and Selvan (2023/2025) address frame regions through sampling; their analyzed object is the frame set rather than the exact Erlang conditioning profile. Earlier frame-bound calculations of Janssen (1996) are relevant background. Its accessible abstract did not identify the present repeated-pole family, but its full text could not be inspected and explicit prior coverage cannot be excluded solely on that basis.

## Limitations

The formulas concern the unnormalized \(t e^{-at}\) family, the single fixed integer-translation/half-integer-modulation lattice, and every fixed \(a>0\). No results are claimed for nonrectangular lattices, arbitrary totally positive windows, general gamma shapes, or uniqueness of the shape parameter minimizing \(\kappa_a\). Earlier sources that could not be inspected completely create a residual originality risk.

## References

1. Jaume de Dios Pont, Karlheinz Gröchenig, Lukas Liehr, Irina Shafkulovska, and Mitchell A. Taylor, *Gabor Frames of Totally Positive Functions: A Complete Characterization*, arXiv:2608.04992v1, first posted August 5, 2026. https://arxiv.org/abs/2608.04992
2. Tobias Kloos and Joachim Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359; Journal of Approximation Theory 184 (2014), 209–237. https://arxiv.org/abs/1311.7359
3. Riya Ghosh and A. Antony Selvan, *On Gabor frames generated by B-splines, totally positive functions, and Hermite functions*, arXiv:2304.11322; Applied Numerical Mathematics 207 (2025), 1–23. https://arxiv.org/abs/2304.11322
4. A. J. E. M. Janssen, *Some Weyl–Heisenberg frame bound calculations*, Indagationes Mathematicae 7 (1996), 165–183. https://doi.org/10.1016/0019-3577(96)85088-9 (full text not inspected).
