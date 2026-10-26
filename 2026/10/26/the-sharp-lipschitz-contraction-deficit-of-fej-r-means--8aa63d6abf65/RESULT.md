# The sharp Lipschitz contraction deficit of Fejér means

## Finding
Let \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\) carry normalized Haar measure \(d\mu(t)=dt/(2\pi)\). For every integer \(n\ge 2\), put
\[
F_n(t)=\frac1n\left(\frac{\sin(nt/2)}{\sin(t/2)}\right)^2
=\sum_{|k|<n}\left(1-\frac{|k|}{n}\right)e^{ikt},
\qquad T_nf=F_n*f.
\]
For real-valued periodic Lipschitz functions, with \(\operatorname{Lip}(f)=\|f'\|_{L^\infty(\mathbb T)}\), the sharp contraction factor
\[
L_n=\sup_{\operatorname{Lip}(f)>0}\frac{\operatorname{Lip}(T_nf)}{\operatorname{Lip}(f)}
\]
is precisely
\[
\boxed{L_n=\min_{c\in\mathbb R}\int_{\mathbb T}|F_n(t)-c|\,d\mu(t).}
\]
The minimizers are the medians of \(F_n\); each yields an explicit extremizer with derivative \(\operatorname{sgn}(F_n-c)\), up to a circle translation and global sign. For every odd \(n\ge3\), the median is exactly \(c=1/n\), so the extremizing derivative is the sign of \(\sin((n+1)t/2)\sin((n-1)t/2)\). The exact initial cases are \(L_2=2/\pi\) and \(L_3=8/(3\pi)\). Every finite \(n\ge2\) has \(0<L_n<1\), and the sharp large-degree contraction deficit is
\[
\boxed{\lim_{n\to\infty}n(1-L_n)=\frac4{\pi^2}.}
\]
In particular, \(L_n=1-4/(\pi^2n)+o(n^{-1})\). The asymptotic coefficient belongs to this specific periodic Lipschitz seminorm, not to uniform approximation errors, total-variation mixing, or \(L^2\)-derivative smoothing.

## Assumptions and scope
The circle metric is the geodesic arc metric. All functions are real, periodic and Lipschitz; all derivatives are their almost-everywhere weak derivatives. Convolution uses the normalized Haar measure, so \(\int F_n\,d\mu=1\). A median of a real kernel means a number with at most half the circle lying strictly above and at most half lying strictly below. The symbol \(L_n\) denotes the induced seminorm, not an \(L^\infty\)-operator norm on functions. For \(n=1\), \(F_1=1\) and the factor equals zero; odd-median assertions are stated for \(n\ge3\).

## Proof
**1. Exact operator duality and attainment.** Every periodic real Lipschitz function \(f\) has an almost-everywhere derivative \(g\in L^\infty(\mathbb T)\) with \(\int g\,d\mu=0\); conversely every such \(g\) has a periodic Lipschitz primitive. Moreover, \((T_nf)'=F_n*g\). Consequently
\[
L_n=\sup_{\substack{|g|\le1\ \mathrm{a.e.}\\ \int g\,d\mu=0}}
\left|\int F_n(t)g(t)\,d\mu(t)\right|.
\]
For any constant \(c\), the last integral is bounded by \(\int|F_n-c|\,d\mu\). Conversely an \(L^1\)-best constant is a median: minimizing \(c\mapsto\int|F_n-c|\,d\mu\) gives a \(c\) for which \(\int\operatorname{sgn}(F_n-c)\,d\mu=0\), because a nonconstant trigonometric polynomial has level sets of measure zero. This sign function is an admissible derivative and attains equality. Translation of the primitive places the output derivative maximum at any specified point. Thus the displayed formula is exact, attained, and not merely a bound.

**2. Exact odd-degree medians.** Away from isolated zeros of the denominator,
\[
\operatorname{sgn}(F_n(t)-1/n)
=\operatorname{sgn}\!\left(\sin((n+1)t/2)\sin((n-1)t/2)\right).
\]
When \(n=2m+1\), this product becomes \(\sin((m+1)t)\sin(mt)\), which changes sign under \(t\mapsto t+\pi\), since consecutive integers have opposite parity. Its positive and negative sets therefore have equal Haar measure. Hence \(1/n\) is the (unique) median, and the stated sign derivative realizes \(L_n\). For \(n=2\), \(F_2(t)=1+\cos t\), whose median is \(1\); its mean absolute deviation is \(2/\pi\). For \(n=3\), \(F_3(t)-1/3=(4/3)\cos t(1+\cos t)\), whose absolute mean is \(8/(3\pi)\). The kernel is positive almost everywhere and not constant when \(n\ge2\), giving \(0<L_n<1\) directly from the median representation.

**3. Two-scale distributional limit.** Let \(t\) be Haar-uniform, and define \(H_n(t)=nF_n(t)=\sin^2(nt/2)/\sin^2(t/2)\). The pair \((t/2\bmod\pi,nt/2\bmod\pi)\) converges in distribution to two independent uniforms on \([0,\pi)\). Indeed, for any fixed integer Fourier modes \((k,\ell)\ne(0,0)\), the corresponding torus average \(\int e^{i(k+n\ell)t}\,d\mu(t)\) vanishes for all sufficiently large \(n\); density of trigonometric polynomials proves joint weak convergence. It follows, by the continuous-mapping theorem away from the null set where the denominator vanishes, that
\[
H_n\ \Longrightarrow\ H=\frac{\sin^2 U}{\sin^2 V},
\]
where \(U,V\) are independent uniforms on \([0,\pi/2]\). The law of \(H\) is atomless, has strictly increasing distribution function on \((0,\infty)\), and has unique median \(1\), by the exchange symmetry of its independent identically distributed numerator and denominator. If \(c_n\) is the median of \(H_n\), then \(c_n\to1\). The median of \(F_n\) is \(c_n/n\).

**4. Capped-limit evaluation.** Since \(\int F_n\,d\mu=1\), the absolute-deviation identity yields
\[
 n(1-L_n)=2\int\min(H_n,c_n)\,d\mu-c_n.
\]
The integrands are uniformly bounded for large \(n\) because \(c_n\to1\), and their only limiting discontinuities occur on Haar-null sets. Thus joint equidistribution and \(c_n\to1\) imply
\[
\lim_{n\to\infty}n(1-L_n)=2\mathbb E\min(H,1)-1.
\]
For independent uniforms \(U,V\) on \([0,\pi/2]\), the region \(U\ge V\) contributes \(1/2\). On \(U<V\), direct integration gives
\[
\begin{aligned}
\mathbb E\min(H,1)
&=\frac12+\frac4{\pi^2}\int_0^{\pi/2}\frac{\int_0^v\sin^2u\,du}{\sin^2v}\,dv\\
&=\frac12+\frac2{\pi^2}\int_0^{\pi/2}\left(v\csc^2v-\cot v\right)\,dv\\
&=\frac12+\frac2{\pi^2},
\end{aligned}
\]
because the last integral is \([-v\cot v]_{0}^{\pi/2}=1\). Substitution proves the sharp coefficient \(4/\pi^2\).

## Verification
The standalone program `verify_fejer.py` implements two independent finite formulas for the kernel (its sine quotient and its cosine Fourier sum), computes the median absolute deviation by symmetric midpoint quadrature, checks the exact values \(L_2=2/\pi\), \(L_3=8/(3\pi)\), tests the odd-median sign symmetry on sampled circles and compares \(n(1-L_n)\) for increasing \(n\) with \(4/\pi^2\). Numerical quadrature is corroborative; steps 1–4 above are the proof for all degrees and the infinite limit.

## Relationship to prior work
Fejér kernels are classical nonnegative approximation kernels. Gaubert and Qu (arXiv:1302.5226, Theorem 1.1) provide a general Dobrushin formula for contraction in Hopf's *oscillation* seminorm, which does not evaluate the periodic *Lipschitz* seminorm on zero-mean derivatives. Mishra and Sonavane (2015, DOI 10.7153/jca-06-11, Theorems 3.1–3.3) study approximation *errors* for distinct summability transforms of conjugate Fourier series on Lipschitz classes, not sharp Fejér Lipschitz contraction. Kravitz and Steinerberger (arXiv:2007.13700, Theorems 1–2) optimize discrete \(\ell^2\)-derivative smoothing over averaging kernels, rather than computing the real periodic Lipschitz contraction of a fixed kernel. The present precise median reduction, odd-degree extremizer and \(4/\pi^2\) coefficient are not implied by those stated results.

## Limitations
This is a theorem for real periodic functions and the ordinary first-order Fejér kernel, not for arbitrary Cesàro orders or higher-dimensional tori. The asymptotic has an \(o(n^{-1})\) remainder and does not claim a second-order coefficient or monotonicity of \(L_n\) with \(n\). The exact finite-degree expression is a median-based integral, not a single elementary closed formula for all even \(n\). Novelty has not been established by exhaustive examination of every older Fourier-analysis textbook or unindexed table; an independent literature audit remains appropriate.

## References
1. S. Gaubert and Z. Qu, *Dobrushin ergodicity coefficient for Markov operators on cones, and beyond*, first arXiv version 2013-02-21, arXiv:1302.5226, https://arxiv.org/abs/1302.5226.
2. V. N. Mishra and V. Sonavane, *Approximation of functions of Lipschitz class by \((N,p_n)(E,1)\) summability means of conjugate series of Fourier series*, Journal of Classical Analysis 6 (2015), 137–151, DOI:10.7153/jca-06-11, https://files.ele-math.com/articles/jca-06-11.pdf.
3. N. Kravitz and S. Steinerberger, *The smoothest average: Dirichlet, Fejér and Chebyshev*, arXiv:2007.13700, 2020-07-27, https://arxiv.org/abs/2007.13700.
