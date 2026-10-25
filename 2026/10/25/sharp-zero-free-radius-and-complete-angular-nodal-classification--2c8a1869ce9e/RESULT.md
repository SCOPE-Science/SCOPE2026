# Sharp zero-free radius and complete angular nodal classification for linearly weighted harmonic Bergman kernels of real balls

## Finding
Fix an integer \(d\ge3\). For the space of complex-valued harmonic functions in the real unit ball \(B^d\) with the normalized radial probability measure
\[
 d\mu_d(x)=\frac{d+2}{2\operatorname{vol}(B^d)}(1-|x|^2)\,dx,
\]
its reproducing kernel has a sharp zero-free product radius \(u_d\in(0,1)\), characterized by
\[
48v_d^3+12(d+2)v_d^2=d(d+2),\qquad u_d=\frac{v_d}{1+v_d},\qquad v_d>0.
\]
For every nonzero \(x,y\in B^d\) put \(u=|x||y|\) and \(t=(x\cdot y)/(|x||y|)\). If \(0\le u<u_d\), the kernel is strictly positive for every angular parameter \(-1\le t\le1\). On \(u=u_d\) its sole angular zero occurs at \(t=-1\). For each \(u_d<u<1\), there exists exactly one \(t_d(u)\in(-1,1)\) at which the kernel is zero; the kernel is negative below that angular threshold and positive above it. The function \(t_d\) is real analytic and tends to \(1\) as \(u\uparrow1\); all zeros with non-antipodal angles are angularly transverse. The threshold \(u_d\) increases strictly with dimension and obeys \(1-u_d\sim\sqrt{12/d}\) as \(d\to\infty\). In particular \(u_4=1/3\). The largest radius of a centered ball on which the kernel is positive for all pairs is \(\sqrt{u_d}\), as a sharp supremum.

## Assumptions and scope
The ambient space is real Euclidean dimension \(d\ge3\); harmonicity refers to the real Laplacian, not holomorphic functions on a complex ball. The weight is exactly \(1-|x|^2\), with the displayed normalizing constant. Harmonic functions are considered with the complex Hilbert inner product induced by \(L^2(d\mu_d)\). The kernel is real on two real position arguments; when either point is the origin, it equals \(1\). The argument \(t\) is defined only when both points are nonzero. A zero at \(u=u_d,t=-1\) is attainable by taking opposite points with radii \(\sqrt{u_d}\) in the open unit ball.

## Proof
Write \(a=d/2\), \(D=1-2ut+u^2>0\), and \(R=u\partial_u\). For the spherical harmonic degree \(n\), the radial moment of \(d\mu_d\) is
\[
 m_{n,d}=\frac{a(a+1)}{(a+n)(a+n+1)}.
\]
Indeed the squared radius has the \(\operatorname{Beta}(a,2)\) distribution. The spherical addition theorem expresses the harmonic reproducing kernel as a sum of normalized Gegenbauer zonal harmonics; their Poisson generating function is
\[
 P_d(u,t)=\frac{1-u^2}{D^a}.
\]
Multiplication of the degree-\(n\) term by \(1/m_{n,d}\) is thus the exact radial differential operation
\[
 K_d(u,t)=\frac{[R^2+(d+1)R+d(d+2)/4]P_d(u,t)}{d(d+2)/4}.
\]
Termwise differentiation is justified by uniform convergence on compact sets \(u<1\). Direct differentiation and collecting terms give
\[
 K_d(u,t)=\frac{N_d(u,t)}{d(d+2)D^{d/2+2}},
\]
where the polynomial numerator is
\[
\begin{aligned}
N_d(u,t)={}&d^2(1-u^2)^3\\
&+d\bigl(10u^6+6u^4-18u^2+2+24tu^3(1-u^2)\bigr)\\
&-24u^2(1+u^2)^2+96tu^3(1+u^2)-96t^2u^4.
\end{aligned}
\]
The denominator is strictly positive. Differentiation of this polynomial gives
\[
\partial_t N_d(u,t)=24u^3\bigl[(d+4)+(4-d)u^2-8ut\bigr]
\ge24u^3(1-u)\bigl[(d+4)+(d-4)u\bigr]>0
\]
for \(0<u<1\), \(-1\le t\le1\), \(d\ge3\); the final factor is positive even when \(d=3\). Therefore the numerator is strictly increasing in angle parameter \(t\).

On the antipodal axis let \(v=u/(1-u)\). Exact factorization yields
\[
 N_d(u,-1)=(1-u^2)^3\bigl[d(d+2)-12(d+2)v^2-48v^3\bigr].
\]
The bracket decreases strictly from a positive value to minus infinity as \(v>0\) grows, giving the unique \(v_d\) and all asserted antipodal signs. At the aligned angle \(t=1\), every term in the positive Gegenbauer addition-series expression for \(K_d(u,1)\) is nonnegative, with constant term \(1\); hence \(K_d(u,1)>0\). Strict monotonicity in \(t\), together with these endpoint signs, proves the complete three-regime angular classification. For \(u>u_d\), the implicit-function theorem applies since \(\partial_tN_d>0\), so \(t_d(u)\) is real analytic and angularly transverse. As \(u\uparrow1\), the polynomial approaches \(N_d(1,t)=-96(t-1)^2\); the unique root must therefore satisfy \(t_d(u)\to1\), since for every fixed \(t<1\) the limiting numerator is negative.

Dividing the equation for \(v_d\) by \(d(d+2)\) yields
\[
1=\frac{12v_d^2}{d}+\frac{48v_d^3}{d(d+2)}.
\]
For fixed positive \(v\), the right-hand side strictly decreases with \(d\), hence \(v_d\) and \(u_d\) strictly increase. The same equation implies \(v_d\sim\sqrt{d/12}\), so \(1-u_d=1/(1+v_d)\sim\sqrt{12/d}\). At \(d=4\), the unique positive cubic root is \(v_4=1/2\), yielding \(u_4=1/3\). Finally, a pair of opposite points at radius \(\sqrt{u_d}\) realizes the boundary zero, while any larger radius allows opposite points with product \(u>u_d\) and therefore a negative kernel value. This proves the sharp common-ball radius.

## Verification
The standalone file `check_kernel.py` verifies the differential-to-polynomial identity, the antipodal cubic factorization, the second angular derivative and the boundary polynomial with SymPy exact algebra. It also compares the resulting kernel against an independent 150-term Gegenbauer spherical-harmonic expansion for four dimensions at three angles and radii each, plus high-precision checks of seven cubic thresholds. The checked spectral truncations do not constitute proof for infinitely many degrees; the Poisson generating function and differential computation above provide that proof. Run `python check_kernel.py` with the versions specified in `requirements.txt`. The accompanying `checker_output.txt` is one concrete run.

## Relationship to prior work
Engliš, *High-power asymptotics of some weighted harmonic Bergman kernels*, arXiv:1601.03716v1 (January 14, 2016), develops general weighted harmonic Bergman kernel representations on balls; its accessible Section 3 supplies the relevant spherical-harmonic and moment framework. The contribution here is the exact sign/nodal geometry, a unique angular zero for each supercritical product radius, and the sharp dimension-dependent cubic threshold for the specific linear weight, not the general kernel representation itself. Otáhalová (2008) studies weighted harmonic Bergman kernels and Toeplitz operators; the accessible bibliographic/abstract information does not resolve whether it contains an equivalent special-case sign analysis. Miao (1998) treats the unweighted harmonic Bergman kernel, a different reproducing kernel. Holomorphic weighted Bergman kernels on complex balls cannot be substituted for real harmonic reproducing kernels: their spaces, coefficients and zero sets differ.

## Limitations
This is a statement for the precise linear radial weight in real dimension \(d\ge3\), not a complete classification of general weights or of holomorphic kernels. The natural boundary \(u=1\) lies outside the open ball and is used only to establish a limiting angular trend. The literature comparison is subject to older weighted-kernel sources whose full texts were inaccessible, so historical publication priority is not independently certified. The computation checks finite examples, while all-dimensional conclusions rely on the analytic argument. An independent mathematical audit has not been performed.

## References
- M. Engliš, *High-power asymptotics of some weighted harmonic Bergman kernels*, arXiv:1601.03716v1, publicly posted 2016-01-14, https://arxiv.org/abs/1601.03716.
- R. Otáhalová, *Weighted harmonic Bergman kernels and Toeplitz operators*, Proceedings of the American Mathematical Society (2008), https://doi.org/10.1090/S0002-9939-08-09384-2.
- J. Miao, *Reproducing kernels for harmonic Bergman spaces*, https://doi.org/10.1007/BF01489456 (1998), unweighted comparison.
