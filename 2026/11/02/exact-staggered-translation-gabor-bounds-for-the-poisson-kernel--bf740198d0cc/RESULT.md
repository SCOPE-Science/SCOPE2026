# Exact staggered-translation Gabor bounds for the Poisson kernel

## Finding
For every width \(w>0\) and phase offset \(0<\delta<1\), the two-coset Gabor system
\[
\mathcal G_{w,\delta}=\big\{ e^{2\pi i m t}g_w(t-n),\ e^{2\pi i m t}g_w(t-n-\delta):m,n\in\mathbb Z\big\},\quad g_w(t)=(t^2+w^2)^{-1},
\]
is a frame of \(L^2(\mathbb R)\). The **exact optimal lower bound** for all widths and offsets is
\[
A_w(\delta)=\frac{4\pi^2q(1-q)^2}{w^2}\,\frac{1-|\cos(\pi\delta)|}{(1+q^2+2q|\cos(\pi\delta)|)^2},\qquad q=e^{-2\pi w}.
\]
For each fixed width, \(\delta=1/2\) is the unique maximizer of \(A_w(\delta)\), the unique minimizer of the *optimal* upper frame bound, and therefore the unique minimizer of the optimal frame condition number. The optimal upper bound at the balanced offset is
\[
B_w(1/2)=\frac{\pi^2}{w^2}\big(\coth^2(\pi w)+\tanh^2(\pi w)\big).
\]
At the same point \(A_w(1/2)=4\pi^2q(1-q)^2/[w^2(1+q^2)^2]\). The sharp coalescence law, as \(d=\min\{\delta,1-\delta\}\downarrow0\), is
\[
A_w(\delta)=\frac{\pi^4}{2w^2}\tanh^2(\pi w)\operatorname{sech}^2(\pi w)\,d^2+O_w(d^4),
\]
while \(B_w(\delta)\to2\pi^2w^{-2}\coth^2(\pi w)\). The shift is in **time/translation**, not the frequency/modulation variable.

## Assumptions and scope
The Fourier transform is \(\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-2\pi it\xi}\,dt\), and modulation is \(M_mf(t)=e^{2\pi imt}f(t)\). Lebesgue measure on \(\mathbb R\) fixes the Hilbert norm. A Gabor frame has bounds \(A,B\) when \(A\|f\|_2^2\le\sum_{m,n\in\mathbb Z}(|\langle f,M_mT_ng_w\rangle|^2+|\langle f,M_mT_{n+\delta}g_w\rangle|^2)\le B\|f\|_2^2\) for every \(f\in L^2(\mathbb R)\). Optimal bounds mean respectively the largest possible \(A\) and smallest possible \(B\). Every positive width and every offset strictly between zero and one are included; zero and one themselves denote coinciding cosets and are not asserted to have positive lower frame bounds.

## Proof
**1. Zak fibers.** Define \(Zf(x,\omega)=\sum_{n\in\mathbb Z}f(x-n)e^{2\pi in\omega}\), with \(0\le x,\omega<1\). Its extension from Schwartz functions is unitary \(L^2(\mathbb R)\to L^2([0,1)^2)\). The critical-lattice Zak identities and Parseval show that the frame operator of the union acts by multiplication by
\[
F_{w,\delta}(x,\omega)=|Zg_w(x,\omega)|^2+|Zg_w(x-\delta,\omega)|^2.
\]
Consequently \(A_w(\delta)=\min F_{w,\delta}\) and \(B_w(\delta)=\max F_{w,\delta}\); continuity follows from the explicit formula below. Notice that swapping the two lattices' *frequency* sets would produce a different fiber problem.

**2. Exact Zak kernel.** Let \(q=e^{-2\pi w}\), \(\alpha=2\pi w\), and \(D(x)=1-2q\cos(2\pi x)+q^2>0\). Since \(\widehat g_w(\xi)=\pi e^{-2\pi w|\xi|}/w\), Poisson summation and two geometric series imply, for \(0\le\omega\le1\),
\[
|Zg_w(x,\omega)|^2=\frac{4\pi^2q^2}{w^2D(x)^2}\left[\sinh^2(\alpha(1-\omega))+\sinh^2(\alpha\omega)+2\sinh(\alpha(1-\omega))\sinh(\alpha\omega)\cos(2\pi x)\right].
\]
The formula extends continuously across all Zak boundary identifications, as an equality of squared magnitudes. Put \(h=\alpha/2\) and \(v=\alpha(\omega-1/2)\). The bracket in the preceding display equals
\[
4\left[\sinh^2h\,\cosh^2v\,\cos^2(\pi x)+\cosh^2h\,\sinh^2v\,\sin^2(\pi x)\right].
\]
Both factors \(\cosh^2v\) and \(\sinh^2v\) increase with \(|v|\). Thus, simultaneously for every \(x\), the minimum over \(\omega\) occurs at \(1/2\) and the maximum at \(0\) (equivalently \(1\)). Define their fiber values:
\[
H_w(x):=|Zg_w(x,1/2)|^2=C\frac{\cos^2(\pi x)}{D(x)^2},\quad C=\frac{4\pi^2q(1-q)^2}{w^2};
\qquad P_w(x):=|Zg_w(x,0)|^2=\frac{E}{D(x)^2},\quad E=\frac{\pi^2(1-q^2)^2}{w^2}.
\]
Therefore \(A_w(\delta)=\min_x\{H_w(x)+H_w(x-\delta)\}\) and \(B_w(\delta)=\max_x\{P_w(x)+P_w(x-\delta)\}\).

**3. Exact lower bound, with an attained Jensen inequality.** Put \(a=1+q^2\), \(b=2q\), \(\theta=2\pi x\), and \(\phi(t)=(1+t)/[2(a-bt)^2]\) for \(-1\le t\le1\). Then \(H_w(x)=C\phi(\cos\theta)\). Direct differentiation gives
\[
\phi'(t)=\frac{a+2b+bt}{2(a-bt)^3}>0,\qquad
\phi''(t)=\frac{b(2a+3b+bt)}{(a-bt)^4}>0,
\]
where \(a-b=(1-q)^2>0\). Writing \(t_1=\cos\theta\), \(t_2=\cos(\theta-2\pi\delta)\), the cosine addition identity gives
\[
\frac{t_1+t_2}{2}=\cos(\theta-\pi\delta)\cos(\pi\delta)\ge -|\cos(\pi\delta)|.
\]
Convexity and monotonicity give
\[
H_w(x)+H_w(x-\delta)\ge 2C\phi(-c)=C\frac{1-c}{(a+bc)^2},\qquad c=|\cos(\pi\delta)|.
\]
This estimate is **attained**: for \(\delta\le1/2\), take \(x=(1+\delta)/2\); for \(\delta\ge1/2\), take \(x=\delta/2\). In both cases \(t_1=t_2=-c\). The displayed exact formula for \(A_w(\delta)\) follows, and it is positive for \(0<\delta<1\). Since \(c\mapsto (1-c)/(a+bc)^2\) decreases strictly on \([0,1)\), and \(c\) has its unique zero at \(\delta=1/2\), the balanced shift uniquely maximizes the sharp lower bound.

**4. Upper bound and optimal conditioning.** For the balanced offset \(\delta=1/2\), \(\cos(2\pi(x-1/2))=-\cos(2\pi x)\), and hence
\[
P_w(x)+P_w(x-1/2)=E\left[(a-bt)^{-2}+(a+bt)^{-2}\right],\qquad t=\cos(2\pi x).
\]
This is an increasing function of \(|t|\), so its maximum occurs at \(|t|=1\). Consequently
\[
B_w(1/2)=E\left[(1-q)^{-4}+(1+q)^{-4}\right]=\frac{\pi^2}{w^2}\left[\coth^2(\pi w)+\tanh^2(\pi w)\right].
\]
For a different offset \(0<\delta<1\), evaluation at \(x=0\) yields \(B_w(\delta)\ge P_w(0)+P_w(\delta)\). Because \(D(\delta)<D(1/2)=(1+q)^2\) unless \(\delta=1/2\), this strictly exceeds \(P_w(0)+P_w(1/2)=B_w(1/2)\). The optimal upper bound is uniquely minimized at \(1/2\). Since the lower bound is simultaneously strictly maximized there, the ratio \(B_w(\delta)/A_w(\delta)\) is uniquely minimized there too.

**5. Sharp coalescence.** Symmetry under \(\delta\mapsto1-\delta\) permits \(d=\min\{\delta,1-\delta\}\). Expanding \(c=\cos(\pi d)=1-\pi^2d^2/2+O(d^4)\) in the exact formula gives
\[
A_w(\delta)=\frac{2\pi^4q(1-q)^2}{w^2(1+q)^4}\,d^2+O_w(d^4)
=\frac{\pi^4}{2w^2}\tanh^2(\pi w)\operatorname{sech}^2(\pi w)\,d^2+O_w(d^4).
\]
Finally \(B_w(\delta)=\max_x[P_w(x)+P_w(x-\delta)]\) is continuous in \(\delta\) by uniform continuity of the periodic positive function \(P_w\). Letting \(d\downarrow0\) gives \(2P_w(0)=2\pi^2w^{-2}\coth^2(\pi w)\), as claimed. This completes all frame, extremal, and asymptotic assertions.

## Verification
The standalone `CHECK.py` evaluates the closed Zak formula against a directly truncated Zak series at multiple widths and points, checks the exact minimizing fibers and the balanced maximum, and probes the quadratic asymptotic. Its tests are finite numerical consistency checks; the proof in the preceding section establishes the continuum and asymptotic statements. Run `python3 CHECK.py` with the Python standard library.

## Relationship to prior work
Belov and Semenov (2026) study Poisson-window Gabor frames with irregular **frequency** sets and a regular translation lattice; their formulation distinguishes the reverse configuration with irregular **translation** sets. The present exact theorem concerns the latter configuration, specifically a two-coset nonuniform time-translation pattern with fixed integer modulation. Kloos and Stöckler (2013) give qualitative frame criteria and Zak-zero information for totally positive/exponential-type windows. Belov, Kulikov, and Lyubarskii (2021) treat rectangular Gabor frames for rational windows. None of the inspected statements directly determines the complete exact two-coset translation-shift profile and its unique optimal staggering. The half-shift system alone is a regular oversampled lattice; the general-offset theorem and sharp degeneration are essential to the claim.

## Limitations
The optimal upper bound is given explicitly only at the balanced offset (and by a one-variable maximization at general offsets). No formula is claimed for arbitrary irregular translation sets or arbitrary modulation spacing. The theorem concerns the specific Poisson kernel and width/offset ranges above. Numerical tests alone cannot certify an infinite-dimensional frame, and an historical implicit equivalent may exist despite the inspected literature; independently checking priority and proof remains appropriate.

## References
- Yu. Belov and A. Semenov, *Irregular Gabor Frames for the Poisson Kernel*, arXiv:2610.30037 (first posted 2026-10-21).
- T. Kloos and J. Stöckler, *Zak Transforms and Gabor Frames of Totally Positive Functions and Exponential B-Splines*, arXiv:1311.7359.
- Yu. Belov, A. Kulikov and Yu. Lyubarskii, *Gabor Frames for Rational Functions*, arXiv:2103.08959.
