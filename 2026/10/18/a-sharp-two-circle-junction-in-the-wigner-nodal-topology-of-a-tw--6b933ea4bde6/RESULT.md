# A sharp two-circle junction in the Wigner nodal topology of a two-Hermite superposition

## Finding

Consider the normalized even oscillator wave packet
\[
 f_t=\frac{h_0+t h_2}{\sqrt{1+t^2}},\qquad t>0,
\]
where \(h_0(x)=\pi^{-1/4}e^{-x^2/2}\) and \(h_2(x)=(2x^2-1)h_0(x)/\sqrt2\). Use the convention
\[
 W_t(q,p)=\frac1{2\pi}\int_{\mathbb R}f_t(q+y/2)\overline{f_t(q-y/2)}e^{-ipy}\,dy.
\]
Let \(\mathcal D_t=\{(q,p)\in\mathbb R^2:W_t(q,p)<0\}\), and let \(\mathcal Z_t=\{W_t=0\}\). There is exactly one positive topological transition parameter, \(t_*=2\sqrt2\):

1. For \(0<t<t_*\), \(\mathcal D_t\) has exactly two connected components, each diffeomorphic to an open disk and contained respectively in \(p>0\) and \(p<0\). Its boundary \(\mathcal Z_t\) comprises two disjoint smooth Jordan curves.
2. At \(t=t_*\), \(\mathcal Z_{t_*}\) consists **exactly** of the two unit circles centered at \((0,1/2)\) and \((0,-1/2)\), meeting transversely at \((\pm\sqrt3/2,0)\). The negative set comprises exactly two open crescents, the portions strictly inside one unit circle and strictly outside the other. Each intersection is a nondegenerate nodal saddle, with Hessian eigenvalues \(96\) and \(-32\) for the polynomial Wigner factor.
3. For \(t>t_*\), \(\mathcal D_t\) is a single bounded annulus. Its two boundary components are disjoint smooth radial graphs over the full angular circle. There are no further singular nodal points for any \(t>0\).

The signed negative Wigner volume \(\mathcal N(t)=\int_{\mathbb R^2}(-W_t)_+\,dq\,dp\) is positive for every \(t>0\), but exhibits a nonperturbative near-vacuum law:
\[
 \boxed{\lim_{t\downarrow0}t\log\mathcal N(t)=-\frac1{\sqrt2}.}
\]
In particular, the negative part is exponentially small in reciprocal amplitude even though it is present for arbitrarily small nonzero \(t\).

## Assumptions and scope

All wave functions are real and \(L^2\)-normalized, the oscillator units have Planck constant \(\hbar=1\), and \(t\) is a positive real amplitude ratio (not the excited-state probability). The Wigner transform is the explicitly defined bilinear integral above, so no convention-dependent rescaling is implicit. The nodes are real zeros in the full \((q,p)\) plane. The limiting vacuum \(t=0\) is Gaussian and has no zeros; the limiting pure second excited state \(t\to\infty\) is not assigned a finite transition parameter. The negative volume convention is the integral of the negative part, without an additional factor of two.

## Proof

**1. Exact Fourier--Gaussian calculation.** Direct integration of the product \(f_t(q+y/2)f_t(q-y/2)\), using Gaussian Fourier moments up to order four, gives
\[
 W_t(q,p)=\frac{e^{-(q^2+p^2)}}{\pi(1+t^2)}P_t(q,p),
\]
where
\[
 P_t(q,p)=1+t^2\bigl[1-4(q^2+p^2)+2(q^2+p^2)^2\bigr]+2\sqrt2\,t(q^2-p^2).
\tag{1}
\]
The envelope is everywhere strictly positive. Thus the nodal and sign questions are equivalent to those for \(P_t\). This polynomial identity also follows from the standard Hermite--Laguerre cross-Wigner formula, but the explicit Gaussian calculation fixes normalization independently.

**2. Radial discriminant and exact regions.** Put \(\rho=2(q^2+p^2)\), and at \(\rho>0\) write \(q+ip=\sqrt{\rho/2}\,e^{i\theta}\). Formula (1) becomes
\[
 P_t=\frac{t^2}{2}\rho^2+(\sqrt2\,t\cos2\theta-2t^2)\rho+(1+t^2).
\tag{2}
\]
The radial discriminant is
\[
 \Delta_t(\theta)=2t^2\bigl[(\cos2\theta-\sqrt2 t)^2-(1+t^2)\bigr].
\]
Two distinct positive radial roots occur **if and only if**
\[
 \cos2\theta<c(t):=\sqrt2 t-\sqrt{1+t^2}.
\tag{3}
\]
Indeed, the other branch of the absolute-value inequality would require \(\cos2\theta>\sqrt2t+\sqrt{1+t^2}>1\), impossible, and under (3) the coefficient of \(\rho\) is strictly negative. On these rays the negative region lies exactly between
\[
 \rho_\pm(\theta)=\frac{2t^2-\sqrt2\,t\cos2\theta\ \pm\sqrt{2t^2\bigl[(\cos2\theta-\sqrt2t)^2-(1+t^2)\bigr]}}{t^2}.
\tag{4}
\]
The function \(c(t)\) is strictly increasing, with \(c(t)>-1\) for every \(t>0\), and \(c(t)=1\) precisely at \(t=2\sqrt2\). For \(0<t<2\sqrt2\), condition (3) defines two disjoint angular arcs, one around \(\theta=\pi/2\) and one around \(\theta=3\pi/2\). The radial intervals (4) fill precisely two bounded topological disks; their inner and outer radial roots merge at each arc endpoint, giving one closed boundary component per disk. For \(t>2\sqrt2\), (3) holds at every angle and the two positive continuous radial graphs (4) enclose one annulus. In both cases, the boundaries are smooth; the derivative check below rules out singularities at the merged endpoints.

**3. Unique singularity and exact circular factorization.** From (2), a nonzero nodal point is singular only if the radial and angular derivatives both vanish. The angular derivative is \(-2\sqrt2\,t\rho\sin2\theta\), hence \(\cos2\theta=\pm1\). Along \(\cos2\theta=-1\), the discriminant is strictly positive for every \(t>0\). Along \(\cos2\theta=1\), the discriminant equals \(2t^2(t^2-2\sqrt2t)\), which vanishes only for \(t=2\sqrt2\). There are no nodal points at the origin because \(P_t(0,0)=1+t^2>0\). Therefore there are no singular zeros off this critical parameter.

At \(t=2\sqrt2\), direct polynomial factorization yields
\[
 P_{2\sqrt2}(q,p)=16\bigl(q^2+(p-\tfrac12)^2-1\bigr)\bigl(q^2+(p+\tfrac12)^2-1\bigr).
\tag{5}
\]
The two unit circles intersect where \(p=0\) and \(q^2=3/4\). Their tangent lines are distinct there. Equivalently, their polynomial Hessians satisfy
\[
 \nabla^2P_{2\sqrt2}(\pm\sqrt3/2,0)=\operatorname{diag}(96,-32).
\]
Both eigenvalues are nonzero and opposite. The product in (5) is negative precisely at points strictly inside one disk and strictly outside the other closed disk. Thus the open negative set is \(D_+\setminus\overline{D_-}\) united with \(D_-\setminus\overline{D_+}\), where \(D_\pm=\{q^2+(p\mp1/2)^2<1\}\). There are no additional zeros or components.

**4. Sharp exponential law for negative volume.** Since \(P_t\) increases with \(\cos2\theta\) at any fixed positive \(\rho\), the smallest radius at which it can be negative is approached on the vertical axis \(\cos2\theta=-1\), at the smaller root \(\rho_{\min}(t)=\rho_-(\pi/2)\) of (4). The explicit formula gives
\[
 \rho_{\min}(t)=\frac{2t^2+\sqrt2t-\sqrt{2t^2(2\sqrt2t+t^2)}}{t^2},\qquad
 \lim_{t\downarrow0}t\rho_{\min}(t)=\sqrt2.
\]
Thus \(R_{\min}(t)^2=\rho_{\min}(t)/2\) satisfies \(tR_{\min}(t)^2\to1/\sqrt2\). For \(0<t\le1\), equation (1) and polar Gaussian integration give a universal constant \(C\) such that
\[
 0<\mathcal N(t)\le C(1+R_{\min}(t)^4)e^{-R_{\min}(t)^2}.
\tag{6}
\]
For the complementary lower bound, choose \(q=0\) and \(p=p_0(t)=2^{-1/4}t^{-1/2}\). Exact substitution shows
\[
 P_t(0,p_0(t))=t^2-2\sqrt2t<0
\]
for sufficiently small \(t\). The polynomial gradient in the disk of radius \(t^2\) centered at \((0,p_0(t))\) is uniformly \(O(\sqrt t)\), so \(P_t\le-c t\) throughout that disk for some absolute \(c>0\). The Gaussian exponential on this disk is bounded below by \(\exp(-1/(\sqrt2t)-o(1/t))\). Integrating over its area \(\pi t^4\), and dividing by the bounded normalization \(\pi(1+t^2)\), gives
\[
 \mathcal N(t)\ge c' t^5\exp\bigl(-1/(\sqrt2t)-o(1/t)\bigr).
\tag{7}
\]
Multiplying the logarithms of (6)--(7) by \(t\) and taking \(t\downarrow0\) proves the limit.

## Verification

`artifacts/verify.py` symbolically reconstructs (1) from Gaussian Fourier moments (not by assuming (1)), verifies (5) and the two saddle Hessians exactly, evaluates both sides of the discriminant threshold for seven parameter values, and checks four Wigner values by independent high-precision numerical integration of the original defining integral. It also checks the exact negative polynomial test used in (7). All these checks succeeded. The angular/topological and exponential-limit statements follow from the complete analytic argument above, not from sampled phase-space plots.

## Relationship to prior work

Bonami--Demange--Jaming (2001 preprint, 2003 journal version) established a foundational Gaussian--Hermite and windowed-Fourier framework, not this complete two-mode Wigner nodal phase diagram. Kenfack--Życzkowski (2004) defined and analyzed the negative Wigner volume but did not establish this sharp reciprocal-amplitude rate or topology for the specific two-even-level family. Dahl--Mack--Wolf--Schleich (2006) studied negative regions for hyperradial entangled states, a different family. Abreu--Chabaud--Costa Dias--Prata (2025) proved inverse Wigner nodal rigidity for pure Hermite modes and a general bounded-nodal-set characterization; neither determines the two circles of (5), their unique parameter, or the two-disk-to-annulus transition. The exact low-degree Hermite--Laguerre formula is classical and is **not** presented as original. The new claim is the full global topological classification, exceptional transverse circle junction, and near-vacuum negative-volume exponent for this normalized family.

## Limitations

This is a one-parameter family with a real relative phase; a classification for arbitrary superpositions of three or more oscillator levels is not claimed. The logarithmic law determines the exponential rate, not a full pre-exponential asymptotic series. Literature comparisons are finite and cannot establish priority against every older quantum-optical depiction or alternate normalization. No independent review has been performed.

## References

1. A. Bonami, B. Demange and P. Jaming, "Hermite functions and uncertainty principles for the Fourier and the windowed Fourier transforms," arXiv:math/0102111v1 (first public 2001-02-14), *Rev. Mat. Iberoamericana* **19** (2003), 23--55, DOI:10.4171/RMI/337.
2. A. Kenfack and K. Życzkowski, "Negativity of the Wigner function as an indicator of nonclassicality," arXiv:quant-ph/0406015v1 (2004-06-02).
3. J. P. Dahl, H. Mack, A. Wolf and W. P. Schleich, "Entanglement versus negative domains of Wigner functions," *Phys. Rev. A* **74**, 042323 (2006), DOI:10.1103/PhysRevA.74.042323.
4. L. D. Abreu, U. Chabaud, N. Costa Dias and J. N. Prata, "Inverse problems for the zeros of the Wigner function," arXiv:2504.20324v1 (2025-04-29), especially introduction and sections 2--3.
5. K. Gröchenig, P. Jaming and E. Malinnikova, "Zeros of the Wigner distribution and the short-time Fourier transform," arXiv:1811.03937v1 (2018).
