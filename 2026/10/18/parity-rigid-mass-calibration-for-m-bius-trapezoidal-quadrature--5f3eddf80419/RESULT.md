# Parity-rigid mass calibration for Möbius trapezoidal quadrature of Cauchy mixtures

## Finding
For every positive finite mixture of centered Cauchy probability densities, the unshifted scaled Möbius trapezoidal rule has an exact mass formula, with a sharp parity distinction. If the rule has an **odd** number of nodes, precisely one positive Möbius scale integrates the constant function exactly. If the rule has an **even** number of nodes, the quadrature overestimates mass for every scale unless all Cauchy components have the same scale; its mass is strictly convex as a function of the logarithmic Möbius scale and has a unique optimum.

More precisely, fix an integer \(k\ge1\), positive numbers \(a_1,\ldots,a_k\), and weights \(w_i>0\) with \(\sum_i w_i=1\). Define
\[
\rho(x)=\sum_{i=1}^k w_i\frac{a_i}{\pi(x^2+a_i^2)},\qquad
q_i(c)=\frac{a_i-c}{a_i+c},\qquad c>0.
\]
For any integer \(n\ge1\), let \(Q_n(c)\) be the transformed \(n\)-node trapezoidal approximation to \(\int_{\mathbb R}\rho(x)\,dx=1\), using the continuous endpoint value described below. Then
\[
\boxed{Q_n(c)=\sum_{i=1}^k w_i\frac{1+q_i(c)^n}{1-q_i(c)^n}.}
\]
If \(n\) is odd, \(Q_n\) is strictly decreasing from \(+\infty\) to \(0\), and its unique mass-exact scale \(c_n\) lies in \([\min_i a_i,\max_i a_i]\), strictly inside when the scales are not all equal. If \(n\) is even, \(Q_n(c)\ge1\) for every \(c>0\), with equality exactly when \(a_i=c\) for all \(i\), and \(s\mapsto Q_n(e^s)\) is strictly convex and coercive, hence has a unique minimizer.

For the natural equal-weight, two-scale mixture \(k=2\) with \(0<a<b\), the even-node minimizer is exactly \(c_*=\sqrt{ab}\), and its unavoidable positive mass bias is
\[
\boxed{\min_{c>0}(Q_n(c)-1)=\frac{2r^n}{1-r^n},\qquad r=\frac{\sqrt b-\sqrt a}{\sqrt b+\sqrt a},\quad n\ge2\ \text{even}.}
\]
For odd \(n\), the unique exact scale satisfies \(\sqrt{ab}<c_n<b\) and
\[
\boxed{\log\frac{c_n}{\sqrt{ab}}\sim\frac{2r^{n+1}}{n(1-r^2)}\qquad(n\to\infty\text{ through odd integers}).}
\]

## Assumptions and scope
Define the Möbius map \(\phi_c(\theta)=-c\cot(\theta/2)\) for \(0<\theta<2\pi\). The unshifted \(n\)-node rule uses \(\theta_j=2\pi j/n\), \(j=1,\dots,n\). It approximates the integral of \(\rho\) by \((2\pi/n)\sum_j h_c(\theta_j)\), where \(h_c(\theta)=\rho(\phi_c(\theta))\phi'_c(\theta)\). At \(\theta=2\pi\), the product is defined by its **continuous extension**, not by evaluating the infinite factors separately. The result applies to centered Cauchy mixtures only, and makes no claim for shifted nodes or nonconstant integrands.

The Cauchy tails are algebraic, not Schwartz. In particular the limiting mapped density at \(\theta=0\) is nonzero, unlike the zero endpoint stipulated for Schwartz weights in the motivating integration theory. The present exact rule is defined directly through the continuous transformed density, independently of that theory's hypotheses.

## Proof
**1. The exact formula.** For a single Cauchy scale \(a>0\), direct differentiation and substitution give
\[
 h_{a,c}(\theta)=\frac{ac}{2\pi\{a^2\sin^2(\theta/2)+c^2\cos^2(\theta/2)\}}
 =\frac1{2\pi}\frac{1-q^2}{1-2q\cos\theta+q^2},
 \qquad q=\frac{a-c}{a+c}.
\]
In particular \(h_{a,c}(0)=a/(2\pi c)\) by continuous extension. Since \(|q|<1\), the Poisson-kernel Fourier series is absolutely convergent:
\[
2\pi h_{a,c}(\theta)=1+2\sum_{\ell=1}^{\infty}q^\ell\cos(\ell\theta).
\]
The average over \(n\) equispaced nodes kills every cosine mode except multiples of \(n\). Its value is thus \(1+2\sum_{j\ge1}q^{jn}=(1+q^n)/(1-q^n)\). Positivity and finiteness allow summing the component rules using \(w_i\).

**2. Odd nodes.** For odd \(n\), the function \(F_n(q)=(1+q^n)/(1-q^n)\) has derivative \(2nq^{n-1}/(1-q^n)^2\ge0\), positive except at \(q=0\) for \(n>1\). Each \(q_i(c)\) is strictly decreasing in \(c\), so their positive weighted sum is strictly decreasing; any isolated vanishing derivatives do not affect strict monotonicity. The endpoint limits are \(+\infty\) at \(c\downarrow0\) and \(0\) at \(c\uparrow\infty\). At \(c=\min a_i\), all \(q_i\ge0\) and \(Q_n\ge1\). At \(c=\max a_i\), all \(q_i\le0\) and \(Q_n\le1\). Strict inequalities hold when at least two scales differ. The intermediate value theorem gives the asserted unique mass-exact scale. For \(n=1\), it is the weighted arithmetic mean \(\sum_i w_i a_i\).

**3. Even nodes and strict logarithmic convexity.** Set \(n=2m\ge2\), \(s=\log c\), and \(u=\tanh((s-\log a)/2)=(c-a)/(c+a)\). Since \(n\) is even, the single-component mass equals \(F_n(u)=(1+u^n)/(1-u^n)\). Differentiating with respect to \(s\), using \(du/ds=(1-u^2)/2\), gives
\[
\frac{d^2}{ds^2}F_n(u)=\frac{n\,u^{n-2}(1-u^2)}{2(1-u^n)^3}\,N_n(u),
\]
where
\[
N_n(u)=(n-1)-(n+1)u^2+(n+1)u^n-(n-1)u^{n+2}.
\]
With \(R=u^2\in[0,1)\), its decisive factorization is
\[
N_n(u)=(1-R)\left((2m-1)(1+R^m)-2\sum_{j=1}^{m-1}R^j\right).
\]
Convexity of \(t\mapsto R^t\) on \([0,m]\) gives \(R^j\le(1-j/m)+(j/m)R^m\). Therefore the bracket is at least \(m(1+R^m)>0\). The second derivative is positive except possibly at the single point \(u=0\) for \(m>1\), so each summand is strictly convex as a function of \(s\); so is their positive weighted sum. Each \(F_n(u)\ge1\), with equality if and only if \(u=0\). As \(s\to\pm\infty\), all summands tend to infinity. Hence a unique minimizer exists. Its position lies between the smallest and largest component scales, since each summand decreases to its own minimizer and increases thereafter.

**4. Equal-weight two-scale extremum.** For \(a<b\), put \(g=\sqrt{ab}\) and \(r=(\sqrt b-\sqrt a)/(\sqrt b+\sqrt a)\). The two transformed ratios at \(c=g\) are \(-r,r\). On the logarithmic scale the sum is symmetric under \(s\mapsto2\log g-s\). For even \(n\), symmetry and strict convexity force the unique optimizer \(g\). Substitution yields \(Q_n(g)-1=2r^n/(1-r^n)\).

For odd \(n\), evaluation at \(g\) instead gives \(Q_n(g)=(1+r^{2n})/(1-r^{2n})>1\), so \(c_n>g\). Let \(s_n=\log(c_n/g)>0\). The two absolute ratios near \(g\) are \(u(s)=\tanh((L-s)/2)\) and \(v(s)=\tanh((L+s)/2)\), where \(L=\log(b/a)/2\) and \(u(0)=v(0)=r\). The exact root equation is
\[
v(s_n)^n-u(s_n)^n=2u(s_n)^n v(s_n)^n.
\]
Comparing the dominant magnitudes for any fixed positive or negative \(s\) shows \(s_n\to0\). The root equation then implies \(ns_n\to0\), since the left-hand relative imbalance otherwise stays bounded away from zero while the right-hand relative factor vanishes geometrically. Taylor expansion, now uniform under \(ns_n\to0\), gives
\[
v(s_n)^n-u(s_n)^n = n r^{n-1}(1-r^2)s_n(1+o(1)),
\quad 2u(s_n)^nv(s_n)^n=2r^{2n}(1+o(1)).
\]
Equating proves \(s_n\sim2r^{n+1}/[n(1-r^2)]\), as claimed.

## Verification
The standalone file `verify.py` recomputes the circle-node rule directly at 180 combinations of scales and node counts using high precision; verifies 20 symbolic differentiation and factorization identities; checks 43 parity inequalities/root cases; tests 28 two-scale extrema; and compares six odd-node asymptotic ratios. **All 277 checks passed.** These finite tests corroborate algebraic and numerical statements but are not a substitute for the proofs above. Run `python verify.py` with Python 3, SymPy, and mpmath installed; the script contains the actual test parameters and tolerances.

## Relationship to prior work
Suzuki, Hyvönen, and Karvonen introduced the Möbius-transformed trapezoidal rule and proved weighted-Sobolev convergence rates for monotonic Schwartz weights. Their quadrature formula and endpoint handling for rapidly decaying weights are prior work. The present statement instead concerns the exact mass-calibration geometry of algebraically decaying Cauchy mixtures, whose endpoint value is **not zero**. It does not extend their error theorem by assertion.

Trefethen and Weideman give the classical Fourier-aliasing representation of periodic trapezoidal quadrature, which supplies the well-known proof mechanism for the mass formula. Neither that general aliasing identity nor the Poisson-kernel Fourier expansion is claimed as new. The assessed mathematical statement is the complete odd/even calibration and uniqueness classification, strict log-scale convexity for all even node counts, and the exact two-scale extremum and odd-node displacement law. No publication-priority or independent verification claim is made.

## Limitations
This is an exact-arithmetic result for **unshifted** nodes and for the integral of the constant function against a centered finite Cauchy mixture. It does not bound integration error for general observables, establish an optimal scale for such observables, or imply that a mass-calibrated rule is always more accurate than post-hoc renormalization. The formulas use continuous endpoint extension; literal evaluation of the unbounded coordinate map at an endpoint is undefined. These points are essential to the scope. The general periodic aliasing calculation is classical; specialist literature might contain equivalent optimizations not identified in the inspected sources.

## References
1. Y. Suzuki, N. Hyvönen, T. Karvonen, *Möbius-Transformed Trapezoidal Rule*, arXiv:2407.13650, publicly submitted 18 July 2024; see especially the map, quadrature (3.1), its endpoint implementation remark, and the weighted-Sobolev hypotheses. https://arxiv.org/abs/2407.13650
2. L. N. Trefethen, J. A. C. Weideman, *The Exponentially Convergent Trapezoidal Rule*, SIAM Review 56 (2014), 385–458, DOI:10.1137/130932132, especially §§2–3 on Fourier aliasing. https://doi.org/10.1137/130932132
