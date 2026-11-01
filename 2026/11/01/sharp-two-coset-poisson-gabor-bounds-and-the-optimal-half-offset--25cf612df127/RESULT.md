# Sharp two-coset Poisson Gabor bounds and the optimal half-offset

## Finding
Fix any \(w>0\) and \(0<\delta<1\). Let
\[
g_w(t)=\frac1{t^2+w^2},\qquad
\mathcal G_{w,\delta}=\left\{e^{2\pi i(m+\varepsilon)t}g_w(t-n):\;m,n\in\mathbb Z,\quad\varepsilon\in\{0,\delta\}\right\}.
\]
Write \(q=e^{-2\pi w}\) and \(d=\min\{\delta,1-\delta\}\). Then \(\mathcal G_{w,\delta}\) is a frame in \(L^2(\mathbb R)\) whose **exact optimal lower and upper frame bounds** are
\[
\boxed{A_w(\delta)=\frac{4\pi^2q}{w^2(1+q)^2}\left(\cosh(2\pi wd)-1\right)},
\]
\[
\boxed{B_w(\delta)=\frac{\pi^2}{w^2(1-q)^2}\left((1+q)^2+(q^\delta+q^{1-\delta})^2\right)}.
\]
Among all \(0<\delta<1\), the **unique** offset maximizing \(A_w\), minimizing \(B_w\), and minimizing the optimal condition number \(B_w/A_w\) is \(\delta=1/2\). In the colliding-coset limit \(d\downarrow0\),
\[
A_w(\delta)=\frac{8\pi^4q}{(1+q)^2}d^2+O_w(d^4),\qquad
\frac{B_w(\delta)}{A_w(\delta)}\sim\frac{(1+q)^4}{4\pi^2w^2q(1-q)^2}d^{-2}.
\]
These are sharp frame bounds for the **nonrectangular** union of two frequency cosets, not generic estimates for its lattice density.

## Assumptions and scope
The Hilbert space is complex \(L^2(\mathbb R)\) with its usual unweighted norm. The family contains both complete modulation rows indexed by \(\mathbb Z\), respectively \(\mathbb Z+\delta\), at **every integer translation**. Every atom is counted once; there is no averaging over the two rows. The Fourier transform is \(\widehat f(\omega)=\int_{\mathbb R}f(t)e^{-2\pi it\omega}\,dt\). For \(w>0\) the window belongs to \(L^1\cap L^2\), and its Zak transform converges absolutely. All assertions quantify over every \(w>0\), every \(0<\delta<1\), and all \(f\in L^2(\mathbb R)\). The parameter endpoints are excluded because the two frequency cosets then coincide; the limiting formulas quantify deterioration as they approach coincidence.

## Proof
**1. Exact frame multiplier.** Use the unitary Zak transform
\[
(Zf)(x,s)=\sum_{n\in\mathbb Z}f(x-n)e^{2\pi ins},\qquad (x,s)\in[0,1)^2.
\]
By the critical-density Zak diagonalization and Parseval in the integer Fourier indices, each row of \(\mathcal G_{w,\delta}\) contributes its squared Zak-window modulus. Thus the frame energy equals
\[
\sum_{h\in\mathcal G_{w,\delta}}|\langle f,h\rangle|^2
=\int_{[0,1)^2}|Zf(x,s)|^2 W_{w,\delta}(x,s)\,dx\,ds,
\quad
W_{w,\delta}=|Zg_w(x,s)|^2+|Zg_w(x,\{s-\delta\})|^2.
\]
Indeed \(Z(M_\delta g)(x,s)=e^{2\pi i\delta x}Zg(x,s-\delta)\), and the unimodular factor does not affect the multiplier. Consequently the optimal frame bounds are the essential minimum and maximum of \(W_{w,\delta}\).

**2. Poisson expansion and monotonicity in position.** The elementary Fourier identity \(\widehat g_w(\omega)=\pi e^{-2\pi w|\omega|}/w\), followed by Poisson summation, yields for \(0\le s<1\), \(X=e^{2\pi ix}\), \(q=e^{-2\pi w}\),
\[
Zg_w(x,s)=\frac\pi w e^{2\pi ixs}\left(\frac{q^s}{1-qX}+\frac{q^{1-s}}{X-q}\right).
\]
Set
\[
a_s=q^s(1-q^{2-2s}),\quad b_s=q^{1-s}(1-q^{2s}),\quad c=\cos(2\pi x).
\]
Both \(a_s,b_s\) are nonnegative, not simultaneously zero. Multiplying out the denominators shows
\[
|Zg_w(x,s)|^2=\left(\frac\pi w\right)^2
\frac{a_s^2+b_s^2+2a_sb_sc}{(1+q^2-2qc)^2}.
\]
Write \(N(c)=a_s^2+b_s^2+2a_sb_sc\ge0\) and \(D(c)=1+q^2-2qc>0\). Differentiation yields
\[
\frac{d}{dc}\frac{N(c)}{D(c)^2}=
\frac{2a_sb_sD(c)+4qN(c)}{D(c)^3}\ge0.
\]
Thus each summand, and hence \(W_{w,\delta}\), is increasing in \(c\). Its minimum over position occurs at \(x=1/2\) and maximum at \(x=0\), for every \(s\).

**3. Sharp lower bound.** At \(x=1/2\), the geometric series simplify to
\[
|Zg_w(1/2,s)|^2=\left(\frac\pi{w(1+q)}\right)^2(q^s-q^{1-s})^2.
\]
Let \(L=-\log q=2\pi w\) and \(h(s)=(q^s-q^{1-s})^2=4q\sinh^2(L(s-1/2))\). For \(\delta\le s<1\), the sum \(h(s)+h(s-\delta)\) equals
\[
4q\left(\cosh(L(2s-1-\delta))\cosh(L\delta)-1\right),
\]
with its unique minimum \(4q(\cosh(L\delta)-1)\) at \(s=(1+\delta)/2\). For \(0\le s<\delta\), the shifted fractional part is \(s+1-\delta\) and the analogous minimum is \(4q(\cosh(L(1-\delta))-1)\) at \(s=\delta/2\). Comparing these two minima and multiplying by the prefactor proves the stated optimal \(A_w(\delta)\). It is positive for every allowed \(\delta\).

**4. Sharp upper bound.** At \(x=0\),
\[
|Zg_w(0,s)|^2=\left(\frac\pi{w(1-q)}\right)^2(q^s+q^{1-s})^2.
\]
Let \(j(s)=(q^s+q^{1-s})^2=4q\cosh^2(L(s-1/2))\). This is strictly convex on \([0,1]\), and \(j(0)=j(1)=(1+q)^2\). On each of the two intervals \([0,\delta]\) and \([\delta,1]\), the function \(j(s)+j(\{s-\delta\})\) is strictly convex, so its maximum occurs at an endpoint. At the endpoints \(0,\delta,1\), periodic interpretation gives the same value \((1+q)^2+(q^\delta+q^{1-\delta})^2\). Multiplication by the prefactor gives the optimal \(B_w(\delta)\).

**5. Offset rigidity and degeneration.** The lower-bound formula is a strictly increasing function of \(d\in(0,1/2]\). The expression \(q^\delta+q^{1-\delta}\) is strictly convex and symmetric about \(1/2\), with its unique minimum there; hence \(B_w\) decreases as \(\delta\) moves toward \(1/2\), and both extrema are unique. Their positive ratio also has its unique minimum there. Taylor's formula \(\cosh(Ld)-1=L^2d^2/2+O_w(d^4)\), together with the continuous endpoint value \(B_w\to2\pi^2(1+q)^2/[w^2(1-q)^2]\), gives the two stated asymptotics.

**6. Optimality in the Hilbert-space sense.** All displayed Zak multipliers are continuous on the torus after the indicated fractional-part gluing, and their extrema are achieved on fibers. Since the Zak transform is unitary and onto, choose unit-norm Zak images supported on successively smaller neighborhoods of a minimizing or maximizing fiber. Their analysis energies tend to the corresponding extremal multiplier value. Therefore neither constant can be improved. This concentration argument does not assert existence of a nonzero \(L^2\) vector attaining equality.

## Verification
The companion pure-Python script `verify_bounds.py` recomputes the geometric Zak formula from direct summation of the original spatial translates; independently tests the frame multiplier formula, the exact extremizers in position and frequency, and the colliding-offset quadratic coefficient for multiple real parameter choices. Finite numerical tests are consistency checks; Steps 1–6 give the general analytic proof and strict inequalities.

## Relationship to prior work
Belov and Semenov (arXiv:2610.30037v1, first public October 21, 2026) give a geometric necessary-and-sufficient **frame property** criterion for the Poisson window on general semi-regular sets \(M\times\alpha\mathbb Z\). Setting \(\alpha=1\) and \(M=\mathbb Z\cup(\mathbb Z+\delta)\) yields qualitative coverage of the positive-frame claim but does not provide these exact optimal bound functions or determine the unique optimally conditioned coset offset. The numerical constants here refine, rather than reprove as novel, that qualitative result. Kloos and Stöckler (arXiv:1311.7359v1) employ critical Zak diagonalization and consider bounds for exponential B-splines; that broad technique includes the special rectangular-lattice offset \(\delta=1/2\), but not this complete nonlattice offset profile for the Poisson kernel. Belov, Kulikov, and Lyubarskii (arXiv:2212.08915) investigate a **Cauchy** window and its rectangular-lattice frame operator, not the two-frequency-coset Poisson system. Exact comparison is by claimed window, index geometry, sharp bounds, and parameter coverage, not merely by titles.

## Limitations
The formulas concern only the unnormalized Poisson window \(g_w(t)=1/(t^2+w^2)\), integer translations, and precisely two parallel frequency cosets. They do not classify arbitrary irregular Gabor sets, prove new qualitative frame criteria in the general setting, or resolve the open converse-orientation semi-regular problem. The bounds are exact for all \(w,\delta\) in the stated domain; pointwise fiber extrema need not correspond to nonzero \(L^2\) equality vectors. Prior work on periodic multilattice Gabor Zak representations could implicitly contain equivalent expressions, and an exhaustive historical priority check has not been made.

## References
1. Y. Belov and A. V. Semenov, *Irregular Gabor Frames for the Poisson Kernel*, arXiv:2610.30037v1, submitted 2026-10-21, https://arxiv.org/html/2610.30037v1.
2. T. Kloos and J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359v1, https://arxiv.org/html/1311.7359v1.
3. Y. Belov, A. Kulikov, and Y. Lyubarskii, *Gabor frame operator for the Cauchy kernel*, arXiv:2212.08915, https://arxiv.org/abs/2212.08915.
