# The exact two-cycle threshold and supercritical flip of a rational sine map

## Finding

For the continuous interval maps
\[
f_r(x)=\frac{\sin(\pi x)}{1+rx},\qquad x\in[0,1],\quad r>0,
\]
let
\[
c=\frac{1}{\pi}\arccos\left(-\frac1\pi\right),\quad
s=\sin(\pi c)=\sqrt{1-\pi^{-2}},\quad
r_*=\frac{s-c}{c^2}=0.94810546376144358339\ldots.
\]
Then each map has exactly two fixed points, \(0\) and \(x_r\in(0,1)\). The zero fixed point is repelling. The positive fixed point is hyperbolically attracting exactly when \(r>r_*\), hyperbolically repelling exactly when \(0<r<r_*\), and has multiplier \(-1\) at \(r=r_*\).

The complete primitive-period-two census on \([0,1]\), counting unordered two-point orbits, is
\[
N_2(r)=\begin{cases}1,&0<r<r_*,\\0,&r\ge r_*.\end{cases}
\]
The unique two-cycle is born supercritically at the fixed-point flip. Set
\[
C=\frac{s\pi^2/2+1/(3s)+r_*(c/(3s)-1)}{c^2}
=11.77383080256061656\ldots>0,
\qquad k=\frac{\pi^2c^4}{2s}>0.
\]
Writing its points as \(x_-(r)<x_+(r)\), as \(\delta=r_*-r\downarrow0\),
\[
x_\pm(r)=c\pm\sqrt{\delta/C}+O(\delta),\qquad
f'_r(x_-(r))f'_r(x_+(r))=1-4k\delta+O(\delta^{3/2}).
\]
In particular, this two-cycle is locally exponentially attracting for all \(r<r_*\) sufficiently close to \(r_*\).

## Assumptions and scope

The parameter is any real \(r>0\); the real state space is the closed unit interval. A primitive two-cycle is an unordered pair of distinct points in \([0,1]\) exchanged by \(f_r\). Since \(f_r(0)=f_r(1)=0\), neither endpoint can belong to a primitive two-cycle. The original positive parameters \(\mu,e\) of Zhu et al. give \(r=e/\mu\) by algebraic normalization of \(\mu\sin(\pi x)/(ex+\mu)\). The source's primary mathematics classification includes 37E05. Local attraction means attraction from a neighborhood, not global basin classification.

## Proof

**1. Fixed points and the critical multiplier.** For \(x\in(0,1)\), the function \(\sin(\pi x)/[x(1+rx)]\) is strictly decreasing from \(\pi\) to \(0\), because \(\sin(\pi x)/x\) and \(1/(1+rx)\) are strictly decreasing. Thus there is exactly one positive fixed point \(x_r\). The fixed point \(0\) has derivative \(\pi>1\). At \(x_r\), use \(1+rx_r=\sin(\pi x_r)/x_r\) to write
\[
D(x_r):=f'_r(x_r)=\pi x_r\cot(\pi x_r)-1+\frac{x_r}{\sin(\pi x_r)},
\quad
D(x_r)+1=\frac{x_r[1+\pi\cos(\pi x_r)]}{\sin(\pi x_r)}.
\]
The latter changes sign at exactly \(c\). Setting \(u=\pi x\), direct differentiation gives
\[
\frac{dD}{du}=\frac{\sin u\cos u-u+(\sin u-u\cos u)/\pi}{\sin^2u}<0
\quad(0<u<\pi).
\]
Indeed \(B=\sin u-u\cos u>0\), while \(A=u-\sin u\cos u\) satisfies \(A-B=(1+\cos u)(u-\sin u)>0\), so \(-A+B/\pi<0\). Also \(D(0+)=1/\pi<1\), and \(D(c)=-1\). The fixed-point parameter is \(r(x)=[\sin(\pi x)-x]/x^2\), strictly decreasing on the positive fixed-point branch. It equals \(r_*\) at \(c\). Hence \(-1<D(x_r)<1\) for \(r>r_*\) and \(D(x_r)<-1\) for \(0<r<r_*\). The inequalities \(3/5<c<2/3\), \(s>c\), and \(s<c+c^2\) show \(0<r_*<1\). They follow from the monotonicity of cosine and \(\sin(2\pi/3)>2/3\), \(\sin(3\pi/5)<24/25\).

**2. Necessary geometry of a two-cycle.** Suppose \(0<x<y<1\) and \(f_r(x)=y,\ f_r(y)=x\). Subtracting the two equations cancels \(rxy\) and gives \(H(x)=H(y)\), where \(H(t)=t+\sin(\pi t)\). Because \(H''(t)=-\pi^2\sin(\pi t)<0\) in \((0,1)\), its unique maximizer is \(c\). Thus \(x<c<y\). Set \(m=(x+y)/2\), \(d=(y-x)/2\). The difference equation becomes
\[
\cos(\pi m)=-\frac{d}{\sin(\pi d)},
\]
so necessarily \(m=m(d)=\pi^{-1}\arccos[-d/\sin(\pi d)]\). For \(0<d\le1/2\), \(m(d)\) is strictly increasing from \(c\) to \(2/3\), and there is a unique \(d_0\in(0,1/2)\) satisfying \(m(d_0)+d_0=1\). All potential two-cycles have \(0<d<d_0\), since \(m-d>0\) automatically there.

**3. Exact reduction to one strictly decreasing equation.** Adding the two equations yields
\[
F(d,r):=\sin(\pi m(d))\cos(\pi d)-m(d)-r\bigl(m(d)^2-d^2\bigr)=0.
\]
Conversely, every root \(d\in(0,d_0)\) reconstructs a genuine two-cycle \((m(d)-d,m(d)+d)\), because the sum and difference equations are equivalent to the original two equations. The continuous extension at \(d=0\) is \(F(0,r)=s-c-rc^2=c^2(r_*-r)\). At \(d=d_0\), \(m+d_0=1\), \(H(m-d_0)=H(1)=1\), whence \(\sin(\pi[m-d_0])=2d_0\); therefore
\[
F(d_0,r)=-(1+r)(1-2d_0)<0.
\]
Writing \(b(d)=d/\sin(\pi d)\), note \(0<b(d)\le1/2\), \(m'(d)>0\), \(\cos(\pi d)>0\), and \(\sin(\pi m(d))=\sqrt{1-b(d)^2}\ge\sqrt3/2\). Direct differentiation gives
\[
\partial_dF=-\bigl(1+\pi b(d)\cos(\pi d)+2rm(d)\bigr)m'(d)
-\pi\sin(\pi m(d))\sin(\pi d)+2rd.
\]
For \(0\le r\le r_*<1\), the inequality \(\sin(\pi d)\ge2d\) on \(0<d<1/2\) implies
\[
\partial_dF<-(\pi\sqrt3-2)d<0.
\]
Hence for \(0<r<r_*\) there is exactly one root by the intermediate-value theorem. At \(r=r_*\), there is no positive root. For \(r>r_*\), \(F(d,r)=F(d,r_*)-(r-r_*)[m(d)^2-d^2]<0\); again there is no root. This exhausts all unordered primitive two-cycles.

**4. Nondegenerate birth and attraction.** As \(d\to0\), analytic even expansion gives
\[
m(d)=c+\frac{d^2}{6s}+O(d^4),\qquad
F(d,r_*-\delta)=c^2\delta-c^2Cd^2+O(\delta d^2+d^4).
\]
The coefficient \(C\) is strictly positive: the first term \(s\pi^2/2\) in its numerator is greater than \(2\), while the only potentially negative term is bounded below by \(-r_*>-1\). The implicit-function theorem applied to \(d^2\) therefore yields \(d=\sqrt{\delta/C}+O(\delta^{3/2})\) and the claimed two-point positions. At the fixed-point branch, \(r'(c)=-2s/c^3\) and \(D'(c)=-\pi^2c\), so its multiplier is \(-1-k\delta+O(\delta^2)\) with \(k=\pi^2c^4/(2s)>0\). Write the map near its positive fixed point as \(f_r(x_r+z)-x_r=p(r)z+a(r)z^2+b(r)z^3+O(z^4)\). At the critical parameter, explicit differentiation yields
\[
a_0=\frac{f''_{r_*}(c)}2=c\left(-\frac{\pi^2}{2}+\frac{r_*}{s}\right),\qquad
b_0=\frac{f'''_{r_*}(c)}6=\frac{\pi^2c/s+3r_*\pi^2c^2/s-6r_*^2c^2/s^2}{6}.
\]
Using \(1+r_*c=s/c\), direct algebra gives the critical cubic coefficient identity \(a_0^2+b_0=kC>0\). The second-iterate Taylor expansion is therefore
\[
f_r^2(x_r+z)-x_r=(1+2k\delta)z-2kCz^3
+O(\delta^2|z|+\delta z^2+|z|^4).
\]
At either nonzero branch, \(z=\pm\sqrt{\delta/C}+O(\delta)\), so differentiation gives return multiplier \(1-4k\delta+O(\delta^{3/2})\). Since \(k>0\), the return multiplier lies strictly between \(-1\) and \(1\) for sufficiently small \(\delta>0\), proving local exponential attraction. No global stability conclusion follows.

## Verification

Run `python verify.py` using Python 3 and the `mpmath` package. It independently recomputes the special constants, solves the exact scalar equation at multiple parameters using high precision, checks both return identities, tests the no-root sign in sample regimes, and checks the square-root and Floquet asymptotics. In the delivered environment the program passed 540 high-precision assertions. Its sampling is a diagnostic only: completeness, monotonicity, and asymptotic limits are proved in the preceding analysis.

For example, at \(r=1/2\), the primitive two-cycle is approximately \((0.41932237337322076019,\ 0.80026668600763447101)\) with return multiplier \(-0.63002060097726843929\). For \(r\ge r_*\), the proof rules out every primitive two-cycle, without relying on numerical root searches.

## Relationship to prior work

Zhu, Deng, Zhang and Zhu (2023), DOI `10.3390/math11010231`, introduce precisely the family \(\mu\sin(\pi x)/(ex+\mu)\). Their accessible mathematical analysis includes bounds, the positive fixed point, a sufficient approximate instability condition at fixed-point coordinate greater than \(0.604\), and numerical dynamical diagnostics. The present result instead gives a sharp full-range primitive two-cycle census and its nondegenerate critical birth; these are not implications of the paper's printed fixed-point inequality. The fixed-point multiplier threshold by itself is an elementary strengthening of their derivative calculation and is not claimed as the independent mathematical advance. The familiar sine map \(x\mapsto a\sin(\pi x)\) lacks the parameter-dependent denominator, and results about it do not directly supply this parameter census. A similarly named later sine-fraction map uses a different denominator and is not the same family.

Actual searches for primitive two-cycles, rational-sine/fractional maps, alternative parameterizations, and published mathematical result records found no covering claim. This is evidence of nonoverlap in inspected material, not proof of publication priority. The publisher's indexed mathematical sections were inspected, but unrestricted direct full-document retrieval was unavailable. This leaves a publication-priority risk for material not visible in indexed text.

## Limitations

The result classifies only primitive period two and fixed points on \([0,1]\), not higher periods, the global attracting basins, invariant measures, entropy, chaos, or cryptographic security. The period-two orbit is not claimed to attract for every \(0<r<r_*\); it is repelling for some smaller parameters. The asymptotic assertions hold only as \(r\uparrow r_*\) from below. Finite numerical diagnostics do not certify infinite claims. No independent mathematical audit has been performed. Further literature may contain a stronger covering theorem not found in accessible searches.

## References

1. Shenli Zhu, Xiaoheng Deng, Wendong Zhang, Congxu Zhu, “Image Encryption Scheme Based on Newly Designed Chaotic Map and Parallel DNA Coding,” *Mathematics* **11** (2023), article 231, published January 2, 2023; DOI: `10.3390/math11010231`; https://doi.org/10.3390/math11010231.
2. Background comparison: the ordinary sine family \(x\mapsto a\sin(\pi x)\), discussed in standard one-dimensional bifurcation literature; no result for the rational-sine census is taken from this family.
