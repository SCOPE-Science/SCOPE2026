# Sharp Lipschitz deviation from affine least-squares detrending

## Finding

The orthogonal least-squares affine approximation \(Pg\) of every real- or complex-valued Lipschitz function on the unit interval satisfies the sharp inequality
\[
\|g-Pg\|_{L^\infty[0,1]}\leq \frac{8}{27}\operatorname{Lip}(g).
\]
The only maximizing evaluation points are \(x=0\) and \(x=1\). For nonconstant \(g\), equality holds precisely when its almost-everywhere derivative, normalized to have essential supremum one, is a unimodular multiple of one of the sign functions
\[
f_0(t)=\begin{cases}-1,&0<t<1/3,\\+1,&1/3<t<1,\end{cases}
\qquad
f_1(t)=\begin{cases}-1,&0<t<2/3,\\+1,&2/3<t<1.\end{cases}
\]
Thus the extremizing \(g\) are additive constants plus nonzero scalar multiples of the primitives of \(f_0\) or \(f_1\).

## Assumptions and scope

The interval is \([0,1]\) with Lebesgue measure of total mass one. The orthogonal projector \(P:L^2(0,1)\to\operatorname{span}\{1,t\}\) uses the usual, unweighted \(L^2\) inner product. The Lipschitz seminorm \(\operatorname{Lip}(g)\) is the least global Lipschitz constant of \(g\); for every Lipschitz function it equals the essential supremum of its almost-everywhere derivative. The theorem applies to complex and real functions. For a general interval of length \(\ell>0\), affine rescaling multiplies the sharp constant by \(\ell\). No claim is made for nonuniform sampling, higher polynomial degrees, or other Sobolev exponents.

## Proof

**Projection kernel.** Centering the coordinate in the orthogonal basis \(\{1,x-1/2\}\), one has, for every integrable \(g\),
\[
(Pg)(x)=\int_0^1g(s)\,ds+12\left(x-\frac12\right)\int_0^1\left(s-\frac12\right)g(s)\,ds.
\]
Define \((Vf)(x)=\int_0^x f(t)\,dt\) and \(T=(I-P)V\). Fubini's theorem yields
\[
(Tf)(x)=\int_0^1K(x,t)f(t)\,dt,\qquad
K(x,t)=\mathbf1_{\{t\le x\}}+t-1-6\left(x-\frac12\right)t(1-t).
\]
The kernel satisfies \(K(1-x,1-t)=-K(x,t)\) away from the measure-zero jump, and \(\int_0^1K(x,t)\,dt=0\). Hence the operator norm is \(\max_{x\in[0,1]}S(x)\), where \(S(x)=\int_0^1|K(x,t)|\,dt\), with \(S(1-x)=S(x)\).

**Exact absolute kernel mass.** It suffices to take \(0\le x\le1/2\). Put \(a=6x-3\). For \(t<x\), the kernel is \(t(1-a+at)\ge0\). For \(t>x\), it is \(-(1-t)(1+at)\). On \(0\le x\le1/3\), the only negative region is \(x<t<-1/a\), where \(x<-1/a\le1\); elementary integration and the identity \(\int_0^1K(x,t)\,dt=0\) give
\[
S(x)=2\int_x^{-1/a}(1-t)(1+at)\,dt
=\frac{4(3x^2-6x+2)(6x^2-3x+1)^2}{27(1-2x)^2}.
\]
For \(1/3\le x\le1/2\), the kernel is positive on \((0,x)\) and negative on \((x,1)\), so
\[
S(x)=2\int_0^x t(1-a+at)\,dt=4x^2(1-x)^2.
\]
At the junction the two expressions both equal \(16/81\).

**Global endpoint rigidity.** Differentiating the first rational expression gives
\[
S'(x)=\frac{8(6x^2-6x+1)(6x^2-3x+1)(12x^2-18x+5)}{27(2x-1)^3}.
\]
For \(0\le x\le1/3\), the second and third quadratic factors are strictly positive, whereas the denominator is negative. The first factor has its only zero in this range at \((3-\sqrt3)/6\); consequently \(S\) strictly decreases and then strictly increases, and its maximum over this range lies at an endpoint. Direct evaluation gives \(S(0)=8/27\) and \(S(1/3)=16/81\). On \([1/3,1/2]\), the expression \(4x^2(1-x)^2\) increases strictly and ends at \(S(1/2)=1/4<8/27\). Reflection now proves that the global maximizers are precisely \(x=0,1\).

**Sharpness and all extremizers.** At the two maximizing evaluations, the kernel becomes \(K(0,t)=(1-t)(3t-1)\) and \(K(1,t)=t(3t-2)\). Therefore \(f_0=\operatorname{sgn}K(0,\cdot)\) and \(f_1=\operatorname{sgn}K(1,\cdot)\) attain \(\|Tf\|_\infty=(8/27)\|f\|_\infty\). Conversely, if equality holds, continuity of \(Tf\) yields a maximizing evaluation, necessarily an endpoint. Equality in the integral triangle inequality forces \(f\) to coincide almost everywhere with a fixed unimodular multiple of the sign of the corresponding real kernel, apart from an overall magnitude. Finally every Lipschitz \(g\) has \(g(x)=g(0)+(Vg')(x)\) and \((I-P)g=(I-P)Vg'\); this proves the inequality and the complete equality characterization. Constants give the trivial zero-seminorm case.

## Verification

The standalone file `checker.py` uses only Python's exact rational arithmetic. It checks the rational absolute-kernel formulas at 1,501 grid values, tests their exact integral expressions, symbolically verifies the derivative polynomial identity coefficient by coefficient, and checks reflection on a rational grid. Its successful replay reports 12,910 exact-rational assertions. The computations corroborate the algebra but do not establish the inequalities over the continuum: positivity of the displayed factors and the analytical monotonicity argument provide that proof. The pointwise sign functions furnish explicit exact extremizers, rather than a discretized approximation.

## Relationship to prior work

Sharp constants for local \(L^2\) projectors and Volterra integration operators motivate asking for the sharp error of the composition \((I-P)V\). Hangelbroek, Narcowich, Sun and Ward [1] study \(L^\infty\) stability of kernel-space \(L^2\) projectors on manifolds; their setting and operator are different. Ransford and Walsh [2] study Hilbert-space norms of polynomials in the Volterra operator, not this rank-two affine correction in the \(L^\infty\) geometry. Joharinad and collaborators [3] study periodic reverse Bernstein inequalities and orthogonality to trigonometric modes, rather than least-squares affine detrending on an interval. The precise constant, full equality cases, and endpoint rigidity here are not entailed by the results inspected. No general claim of exhaustive historical priority is made.

## Limitations

Only degree-one least-squares detrending with uniform continuous measure on a single interval is covered. The numerical checker is finite and does not certify the global extremum independently of the displayed symbolic proof. Earlier specialist Ostrowski, Peano-kernel, or polynomial approximation literature could contain an equivalent sharp inequality; such historical overlap was not exhaustively eliminated. No independent audit has been performed.

## References

[1] T. Hangelbroek, F. Narcowich, X. Sun and J. Ward, *Kernel Approximation on Manifolds II: The L-infinity norm of L2 Projector*, arXiv:1005.2424, first posted 2010-05-13.

[2] T. Ransford and N. Walsh, *Norms of polynomials of the Volterra operator*, arXiv:2206.09947.

[3] P. Joharinad, J. Jost, L.-H. Lim and D. Matveev, *Reverse Bernstein Inequality on the Circle*, arXiv:2302.10122.
