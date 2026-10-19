# Sharp fixed-center first-moment profile for bounded conjugate functions

## Finding

Let \(F\) be holomorphic on the unit disk \(\mathbb D\), with \(\operatorname{Re}F(z)>0\) and \(|\operatorname{Im}F(z)|<B\) for every \(z\in\mathbb D\), where \(B>0\). Write \(F(0)=M+iV\), so \(M>0\), \(|V|<B\). The radial boundary trace \(v^*(e^{it})=\lim_{r\uparrow1}\operatorname{Im}F(re^{it})\) exists almost everywhere. With \(dm(t)=dt/(2\pi)\), the **exact sharp bound for every centre** is

\[
\int_{\mathbb T}|v^*|\,dm\ \le B\,\mathcal G(M/B,V/B),
\qquad
\mathcal G(X,Y)=1-\frac8{\pi^2}\sum_{j=0}^{\infty}
\frac{e^{-(2j+1)\pi X/2}\cos((2j+1)\pi Y/2)}{(2j+1)^2}.
\]

The bound is attained for **each** \(X>0\) and \(|Y|<1\). In fact, equality holds if and only if the analytic disk self-map

\[
\Phi(z)=\frac{\sinh(\pi F(z)/(2B))-1}{\sinh(\pi F(z)/(2B))+1}
\]

is **inner**, meaning \(|\Phi^*(e^{it})|=1\) almost everywhere. This characterizes all equality cases, including nonunivalent extremizers.

The complete derivative profile is

\[
\partial_X\mathcal G(X,Y)=\frac1\pi
\log\frac{\cosh(\pi X/2)+\cos(\pi Y/2)}
{\cosh(\pi X/2)-\cos(\pi Y/2)}.
\]

Consequently \(X\mapsto\mathcal G(X,Y)\) is strictly increasing and strictly concave for \(|Y|<1\); its boundary value is \(\mathcal G(0,Y)=|Y|\). At every fixed \(0<|Y|<1\), its initial right slope is the finite quantity \((2/\pi)\log\cot(\pi|Y|/4)\). At the centered slice \(Y=0\) the slope diverges, with the exact logarithmic law

\[
\mathcal G(X,0)=\frac{2X}{\pi}\left(1+\log\frac4{\pi X}\right)+O(X^3)
\qquad(X\downarrow0).
\]

More precisely, at the corner \((X,Y)\to(0,0)\), uniformly for \(X>0\) and \(|Y|\) small,

\[
\mathcal G(X,Y)=|Y|+\frac2\pi\left[
X\left(1+\log\frac4{\pi\sqrt{X^2+Y^2}}\right)
-|Y|\arctan\frac{X}{|Y|}\right]
+O\bigl(X(X^2+Y^2)\bigr),
\]

where the product involving \(|Y|\) is interpreted as zero at \(Y=0\). Thus the two-parameter crossover interpolates rigorously between the regular nonzero-mean boundary and the singular centered endpoint.

## Assumptions and scope

All quantifiers are as stated: \(B\in(0,\infty)\), \(M\in(0,\infty)\), \(V\in(-B,B)\), and **any** holomorphic \(F\) with the indicated range. No Hardy-space assumption on the unbounded real part is needed. Its imaginary part is bounded harmonic, so the radial trace and its integral exist. The integrals are normalized by total circle mass one. Endpoint centres \(M=0\) or \(|V|=B\) are excluded from the open-strip theorem and only appear as continuous profile limits.

For \(Y=0\), an alternative closed form of the sharp profile is

\[
\mathcal G(X,0)=1-\frac4{\pi^2}\left[
\operatorname{Li}_2(e^{-\pi X/2})-\operatorname{Li}_2(-e^{-\pi X/2})\right],
\quad
\partial_X\mathcal G(X,0)=\frac2\pi\log\coth\frac{\pi X}{4}.
\]

In particular \(1-\mathcal G(X,0)\sim(8/\pi^2)e^{-\pi X/2}\) as \(X\to\infty\).

## Proof

**1. Harmonic majorization.** By scaling assume \(B=1\), and set
\(\Omega=\{x+iy:x>0,\ |y|<1\}\). Let \(U(x,y)\) be the unique bounded harmonic function on \(\Omega\) extending the continuous boundary datum \(h(x+iy)=|y|\). Since \(|y|\) is subharmonic and bounded, the comparison principle on truncated half-strips, with the limit at infinity, gives \(U(x,y)\ge |y|\). The inequality is *strict in the interior*: for Brownian motion first exiting \(\Omega\), the imaginary exit coordinate \(Y_\tau\) has mean \(y\) by bounded optional stopping, and has positive probability of both signs from every interior point, so \(E|Y_\tau|>|E Y_\tau|\). Harmonic measure represents \(U=E|Y_\tau|\).

The function \(U\circ F\) is bounded harmonic on \(\mathbb D\), hence its circle means equal \(U(F(0))\). For each radius, \(|\operatorname{Im}F|\le U(F)\); bounded radial convergence and Fatou's theorem therefore give

\[
\int_{\mathbb T}|v^*|\,dm\le U(F(0)).
\]

This proof does not require radial limits of the positive real part.

**2. Explicit Dirichlet solution.** Put \(W=1-U\). It has zero boundary data on \(y=\pm1\) and triangular datum \(1-|y|\) on \(x=0\). The even Dirichlet eigenfunctions are \(\cos(\lambda_j y)\), \(\lambda_j=(j+1/2)\pi\), with unit squared norm on \((-1,1)\). Direct integration yields

\[
2\int_0^1(1-y)\cos(\lambda_j y)\,dy=\frac2{\lambda_j^2}.
\]

Thus uniqueness of the bounded Dirichlet solution, or separation of variables, gives

\[
W(X,Y)=\sum_{j=0}^\infty \frac{2}{\lambda_j^2}
 e^{-\lambda_j X}\cos(\lambda_j Y).
\]

This is the claimed \(\mathcal G(X,Y)=1-W(X,Y)\). Its convergence is absolute for \(X>0\), allowing differentiation. Summing the differentiated odd-power series gives

\[
\partial_X\mathcal G(X,Y)=\frac4\pi
\operatorname{Re}\operatorname{artanh}
\left(e^{-\pi X/2+i\pi Y/2}\right),
\]

which simplifies to the displayed logarithmic formula. Because \(\cos(\pi Y/2)>0\), direct differentiation proves strict increase and strict concavity in \(X\). The triangular Fourier series gives \(\mathcal G(0,Y)=|Y|\). The derivative at \(X=0\) is finite for \(Y\ne0\), equal to \((2/\pi)\log\cot(\pi|Y|/4)\).

**3. Attainment and equality classification.** The map

\[
H(w)=\sinh(\pi w/2)
\]

is a conformal bijection \(\Omega\to\{\operatorname{Re}\zeta>0\}\), with inverse \((2/\pi)\operatorname{arsinh}\zeta\) using the branch mapping into \(\Omega\). For any given centre \(w_0=X+iY\), put \(h_0=H(w_0)\), \(a=\operatorname{Re}h_0>0\), \(b=\operatorname{Im}h_0\). Then

\[
F_{w_0}(z)=\frac2\pi\operatorname{arsinh}
\left(a\frac{1+z}{1-z}+ib\right)
\]

is holomorphic \(\mathbb D\to\Omega\), takes value \(w_0\) at the origin, and maps almost every point of the circle to a finite point of \(\partial\Omega\). On this boundary \(U=|y|\), so the inequality is an equality. This also establishes sharpness for each fixed two-parameter centre, not just asymptotically as the centre approaches the boundary.

More generally, \(\Phi=(H\circ F-1)/(H\circ F+1)\) is a disk self-map. If it is inner, its a.e. boundary values lie on the unit circle and avoid the single point \(1\) almost everywhere, so \(F^*\in\partial\Omega\) a.e. and equality follows. Conversely, if \(\Phi\) is not inner, the set \(\{|\Phi^*|<1\}\) has positive measure, and on that set \(F^*\) is interior to \(\Omega\); the strict pointwise gap \(U(F^*)-|\operatorname{Im}F^*|>0\) forces strict inequality after integration. This is the asserted if-and-only-if characterization. Undoing the scaling \(F\mapsto F/B\) gives the general case.

**4. The critical corner.** Writing \(a=\pi/2\), the derivative takes the form

\[
\partial_X\mathcal G(X,Y)=\frac1\pi\log
\frac{\cosh(aX)+\cos(aY)}{\cosh(aX)-\cos(aY)}.
\]

Taylor expansion of the numerator and denominator shows, uniformly as \((X,Y)\to(0,0)\), \(X>0\),

\[
\partial_X\mathcal G(X,Y)=\frac2\pi
\log\frac4{\pi\sqrt{X^2+Y^2}}+O(X^2+Y^2).
\]

Integrate from \(0\) to \(X\), using \(\mathcal G(0,Y)=|Y|\) and the elementary primitive

\[
\int_0^X\log\sqrt{t^2+Y^2}\,dt=
\frac X2\log(X^2+Y^2)-X+|Y|\arctan\frac X{|Y|},
\]

with its continuous \(Y=0\) convention. The uniform remainder is \(O(X(X^2+Y^2))\), proving the joint expansion and its centered special case.

## Verification

The separate `check.py` tests the Fourier/eigenfunction and dilogarithm formulas against a direct integral of the *explicit conformal extremizer* for multiple real and nonreal centres, checks the derivative against high-precision differentiation, and tests the joint corner expansion. It is a numerical cross-check only; the infinite-dimensional claims are proved above by harmonic majorization, uniqueness, boundary attainment and exact Fourier expansion.

## Relationship to prior work

Brazitikos (2026), *Sharp Estimates for Conjugate Functions with Applications to Trigonometric Polynomials*, arXiv:2605.18087v1, Theorem 1 and its proof (pages 3–7), considers \(p>1\) and derives the half-strip Dirichlet majorant to obtain a **linear** sharp \(L^p\) constant. The published bound has \(A_p\to\infty\) as \(p\downarrow1\), and does not state this fixed-centre \(p=1\) profile, nonzero-imaginary-centre bound, inner-map classification, or uniform logarithmic-corner law. The separation-of-variables framework is explicitly credited to that paper; no claim is made to invent the majorant method itself.

Older sharp conjugate-function research includes Baernstein (1978) and Essén–Shea–Stanton (2002), which study wider sharp inequality principles; their possible reduction to this explicit endpoint classification remains a historical-priority risk. This result states a precise new fixed-centre endpoint theorem, not a claim of an independently new general conformal technique.

## Limitations

The sharpness and complete equality classification concern the whole specified holomorphic class, **not** degree-bounded trigonometric polynomials. The endpoint centre \(M=0\) is not covered by the open-domain theorem. The result does not claim uniqueness of extremizers (many inner compositions are allowed) or independent audit. Although primary and indexed literature were compared, exhaustive historical priority—particularly in broad older conjugate-function inequalities—has not been established.

## References

1. S. Brazitikos, *Sharp Estimates for Conjugate Functions with Applications to Trigonometric Polynomials*, arXiv:2605.18087v1 (first public May 18, 2026), https://arxiv.org/pdf/2605.18087.
2. A. Baernstein II, *Some sharp inequalities for conjugate functions*, Indiana Univ. Math. J. **27** (1978), 833–852, DOI 10.1512/iumj.1978.27.27055.
3. M. Essén, D. F. Shea, C. S. Stanton, *Sharp \(L\log^\alpha L\) inequalities for conjugate functions*, Ann. Inst. Fourier **52** (2002), 623–659, DOI 10.5802/aif.1896.
