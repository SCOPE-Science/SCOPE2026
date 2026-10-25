# Exact sharp redundancy-two Gabor bounds for asymmetric two-sided exponentials

## Finding

For arbitrary real \(a,b>0\), set
\[
 g_{a,b}(t)=\begin{cases}e^{-at},&t\geq0,\\e^{bt},&t<0.\end{cases}
\]
The Gabor system \(\{e^{\pi i m t}g_{a,b}(t-n):m,n\in\mathbb Z\}\) is a frame of \(L^2(\mathbb R)\). The following are its **optimal**, not merely admissible, frame bounds. Put
\[
 r=e^{-a},\quad s=e^{-b},\quad D=(1+r^2)^{-1},\quad E=(1+s^2)^{-1},\quad H=\frac{r+s}{(1+r^2)(1+s^2)},
\]
\[
 t_* =\frac{(b-a)H+\sqrt{(b-a)^2H^2+4abDE}}{2bE},\qquad
 x_* =\frac{\log(t_*/s)}{a+b}.
\]
Then \(0<x_*<1\). With \(U_*=e^{-ax_*}\) and \(V_*=e^{-b(1-x_*)}\), the sharp lower and upper bounds are
\[
 \boxed{A(a,b)=2\big(DU_*^2+EV_*^2-2HU_*V_*\big)>0,}
\]
\[
 \boxed{B(a,b)=(1-rs)^2\left[\frac1{(1-r)^2(1-s)^2}+\frac1{(1+r)^2(1+s)^2}\right].}
\]
The Zak-transform energy multiplier attains its unique minimum at \((x,\omega)=(x_*,1/4)\) and its unique maximum at \((x,\omega)=(0,0)\), modulo \(x\mapsto x+1\) and \(\omega\mapsto\omega+1/2\). The results hold for **all** positive decay rates, including unequal ones. The known equal-rate case is included as a specialization but is not asserted to be new.

## Assumptions and scope

Use Lebesgue measure on \(\mathbb R\), the inner-product convention \(\langle f,h\rangle=\int f\overline h\), and the unnormalized continuous window \(g_{a,b}(0)=1\). Here translations have step \(1\) and modulations have frequency step \(1/2\): the lattice cell has area \(1/2\), with redundancy two. A frame bound means a constant satisfying, for every \(f\in L^2(\mathbb R)\),
\[
 A\|f\|_2^2\leq\sum_{m,n\in\mathbb Z}|\langle f,e^{\pi i mt}g_{a,b}(t-n)\rangle|^2\leq B\|f\|_2^2.
\]
There are no symmetry assumptions on \(a\) and \(b\), and all extrema refer to the specified lattice and normalization, not to optimization over lattices.

## Proof

**Step 1: exact Zak multiplier.** Define \(Zf(x,\omega)=\sum_{j\in\mathbb Z}f(x+j)e^{-2\pi i j\omega}\) for \((x,\omega)\in[0,1]^2\). Its unitary extension maps \(L^2(\mathbb R)\) to \(L^2([0,1]^2)\). Separate the even and odd modulation indices. Their Zak transforms are Fourier characters on the unit square times, respectively, \(Zg(x,\omega)\) and \(e^{\pi i x}Zg(x,\omega-1/2)\). The remaining integer translates contribute the other Fourier characters. Parseval on the unit square gives the exact frame-operator multiplier
\[
 M(x,\omega)=|Zg(x,\omega)|^2+|Zg(x,\omega+1/2)|^2.
\]
Both essential spectral bounds are thus the extrema of this continuous function on the Zak torus. Geometric series, valid since \(r,s\in(0,1)\), give for \(0\leq x\leq1\), with \(z=e^{2\pi i\omega}\),
\[
 Zg(x,\omega)=\frac{e^{-ax}}{1-rz^{-1}}+\frac{e^{-b(1-x)}z}{1-sz}
 =\frac{z(P_x+Q_xz)}{(z-r)(1-sz)},
\]
where \(U=e^{-ax}\), \(V=e^{-b(1-x)}\), \(P_x=U-rV\geq0\), and \(Q_x=V-sU\geq0\). (At an endpoint one of \(P_x,Q_x\) is zero, and they never vanish simultaneously.)

**Step 2: frequency extrema.** Write \(u=\cos(2\pi\omega)\in[-1,1]\) and
\[
 F_x(u)=\frac{P_x^2+Q_x^2+2P_xQ_xu}{(1+r^2-2ru)(1+s^2-2su)}.
\]
Then \(M(x,\omega)=F_x(u)+F_x(-u)\). Each reciprocal affine denominator is strictly positive, increasing, and strictly convex in \(u\) on \([-1,1]\). Their product has strictly positive first and second derivatives. Since the numerator is nonnegative on the interval and has nonnegative slope, \(F_x''(u)>0\), including the endpoint cases where one of \(P_x,Q_x\) vanishes. Consequently \(F_x(u)+F_x(-u)\) is strictly increasing with \(|u|\). For each \(x\), its unique minimum occurs at \(u=0\), meaning \(\omega=1/4\pmod{1/2}\), and its unique maximum at \(|u|=1\), meaning \(\omega=0\pmod{1/2}\).

**Step 3: maximum in the space coordinate.** Substituting \(\omega=0\) and \(\omega=1/2\) into the geometric sums gives
\[
 M(x,0)=\left(\frac{U}{1-r}+\frac{V}{1-s}\right)^2+\left(\frac{U}{1+r}-\frac{V}{1+s}\right)^2.
\]
Expansion has strictly positive coefficients of \(U^2=e^{-2ax}\), \(V^2=s^2e^{2bx}\), and \(UV=s e^{(b-a)x}\), because
\[
 \frac1{(1-r)(1-s)}-\frac1{(1+r)(1+s)}>0.
\]
The sum is strictly convex in \(x\), even if \(a=b\). The Zak torus identifies its endpoint values \(M(0,0)=M(1,0)\), so its maximum occurs only at the identified endpoint. At \(x=0\), \(U=1\), \(V=s\), and simplification gives the displayed \(B(a,b)\).

**Step 4: minimum and positive lower bound.** At \(\omega=1/4\), the cross terms in the squared-modulus expression cancel, yielding
\[
 M(x,1/4)=2\big(DU^2+EV^2-2HUV\big).
\]
The matrix \(\begin{pmatrix}D&-H\\-H&E\end{pmatrix}\) is positive definite: the exact determinant is
\[
 DE-H^2=\frac{(1-rs)^2}{(1+r^2)^2(1+s^2)^2}>0.
\]
Thus the minimum is strictly positive. Differentiate and divide by the positive quantity \(4U^2\):
\[
 \frac{\partial_x M(x,1/4)}{4U^2}= -aD+bE\tau^2-(b-a)H\tau,\qquad \tau=V/U=s e^{(a+b)x}.
\]
This quadratic has exactly one positive root, \(\tau=t_*\), since its leading coefficient is positive and its constant coefficient is negative. The derivative is negative below that root and positive above it. Also \(M(0,1/4)=M(1,1/4)\) by Zak quasiperiodicity; hence the strictly decreasing-then-increasing function must have its unique minimum strictly inside \((0,1)\). Therefore \(x_*\in(0,1)\) and the asserted formula and uniqueness for \(A\) follow. Combined with Steps 1–3 this proves that \(A\) and \(B\) are optimal frame bounds for every \(a,b>0\).

## Verification

The companion standard-library Python script `check_asymmetric_exponential_gabor.py` evaluates the analytic constants against directly summed Zak geometric series on 64 distinct positive parameter pairs, samples 21 space fibers and 41 frequency fibers for each pair, checks both end-fiber identities, and separately verifies 49 exact-rational matrix determinant and endpoint identities. Its completed output was `CHECK_OK: 64 two-parameter grids; 49 exact rational determinant/end-fiber checks`. These finite tests check normalization and algebra only; the preceding analytic proof establishes the all-parameter assertion. For example, \(a=1,b=3\) gives \(x_*\approx0.653154419670\), \(A\approx0.456191869778\), and \(B\approx3.138526828831\), showing that the lower fiber is generally not centered at \(x=1/2\).

## Relationship to prior work

The full theorem of de Dios Pont, Gröchenig, Liehr, Shafkulovska, and Taylor (arXiv:2608.04992, first public 2026-08-05) characterizes the Gabor frame set of all continuous integrable totally positive functions by strict lattice-density inequality; it proves existence but does not assert sharp spectral constants for this asymmetric two-rate window. Faulhuber and Shafkulovska (arXiv:2204.02917, especially Section 8) determine sharp bounds and optimize rectangular lattices for **symmetric** two-sided exponential windows; the equal-rate specialization here belongs to that established theory. Kloos and Stöckler (arXiv:1311.7359) study Zak transforms, frame existence, and estimates for even exponential windows, without the two-rate closed-form spectrum stated here. Janssen's 1996 study of Weyl–Heisenberg frame bounds is historically relevant; its complete text was not available for this comparison, so priority beyond the inspected works remains uncertain. The novelty claim concerns the complete unequal-rate, two-parameter exact frame bounds and extremal fibers, not qualitative frame existence or the symmetric diagonal.

## Limitations

The result covers only rectangular translation step \(1\), modulation step \(1/2\), and the specified two-sided exponential family. It does not classify noninteger redundancies, other integer redundancies, or general totally positive windows. The two-sided exponential is normalized by its value at zero, not by its \(L^2\) norm. Historical priority is not independently certified; in particular, the complete text of Janssen's 1996 paper was inaccessible. The numerical checker does not replace the infinite-dimensional Zak-transform argument.

## References

1. J. de Dios Pont, K. Gröchenig, L. Liehr, I. Shafkulovska, M. A. Taylor, *Gabor Frames of Totally Positive Functions: A Complete Characterization*, arXiv:2608.04992 (initial release 2026-08-05), https://arxiv.org/abs/2608.04992.
2. M. Faulhuber, I. Shafkulovska, *Gabor frame bound optimizations*, arXiv:2204.02917 (2022), especially Section 8, https://arxiv.org/html/2204.02917v2.
3. T. Kloos, J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359 (2013), https://arxiv.org/abs/1311.7359.
4. A. J. E. M. Janssen, *Some Weyl-Heisenberg frame bound calculations*, Indagationes Mathematicae 7 (1996), 165–183, DOI:10.1016/0019-3577(96)85088-9 (full text not inspected).
