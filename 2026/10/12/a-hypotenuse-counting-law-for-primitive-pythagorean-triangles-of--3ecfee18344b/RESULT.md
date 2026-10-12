# A hypotenuse-counting law for primitive Pythagorean triangles of square inradius

## Finding

For real \(X\ge1\), let \(S(X)\) be the number of *unordered* primitive Pythagorean triangles with positive integral legs, hypotenuse \(c\le X\), and inradius a perfect square. Then

\[
S(X)=\kappa X^{1/2}+O\!\left(X^{1/4}\log(2X)\right),
\qquad
\kappa=\frac{2}{\pi^2}\int_0^{\pi/2}\!\frac{d\theta}{\sqrt{1+\cos^4\theta}}
=0.2783651328106908117\ldots.
\]

The constant is positive and the error estimate holds with an absolute implied constant. The growth is of order \(\sqrt X\); the result is not merely an existence or fixed-inradius statement.

## Assumptions and scope

A primitive Pythagorean triangle has integer sides \(a,b,c>0\), \(a^2+b^2=c^2\), and \(\gcd(a,b,c)=1\). The legs are not ordered, so interchange is not a second triangle. Its inradius is \(r=(a+b-c)/2\), a positive integer. “Square inradius” means \(r=k^2\) with integer \(k\ge1\), not that the area of the incircle is square. The cutoff is on the actual hypotenuse, not on the inradius, perimeter, or generating parameters. All asymptotics are as \(X\to\infty\) through real \(X\ge1\).

## Proof

**1. A bijection.** Every primitive Pythagorean triangle occurs uniquely, up to interchanging its legs, from integers \(m>n\ge1\) with \(\gcd(m,n)=1\) and \(m-n\) odd, as
\[
(a,b,c)=(m^2-n^2,\ 2mn,\ m^2+n^2).
\]
The inradius formula gives \(r=n(m-n)\). Since \(\gcd(n,m-n)=1\), this product is a square if and only if *both* factors are squares. Thus \(n=u^2\), \(m-n=v^2\) for uniquely determined integers \(u,v\ge1\). The parity condition is exactly that \(v\) is odd; the coprimality condition is exactly \(\gcd(u,v)=1\). Conversely, every such pair gives a unique primitive triangle with
\[
r=(uv)^2,\qquad c=(u^2+v^2)^2+u^4.
\]
Consequently \(S(X)\) is *exactly* the number of integer pairs \(u,v\ge1\), \(\gcd(u,v)=1\), \(v\) odd, satisfying the displayed quartic inequality. No approximation occurs in this reduction.

**2. Uniform parity-restricted lattice count.** Let
\[
\Omega=\{(x,y)\in\mathbb R_{>0}^2:(x^2+y^2)^2+x^4\le1\},\quad
A=\operatorname{area}(\Omega),\quad T=X^{1/4}.
\]
For every real \(t\ge1\), let \(L(t)\) count positive lattice points in \(t\Omega\) whose second coordinate is odd. For \(0\le x\le2^{-1/4}\), the upper boundary is
\[
f(x)=\sqrt{\sqrt{1-x^4}-x^2};
\]
this is bounded, continuous, and decreasing from \(1\) to \(0\). For fixed positive first coordinate \(u\), the number of positive odd second coordinates \(v\le tf(u/t)\) is \(tf(u/t)/2+O(1)\). Summing over \(1\le u\le2^{-1/4}t\), and using the elementary monotone Riemann-sum error bound, gives
\[
L(t)=\frac{t^2}{2}\int_0^{2^{-1/4}}f(x)\,dx+O(t+1)
=\frac{A}{2}t^2+O(t+1).
\]
For \(0<t<1\), the bound \(L(t)=O(1)\) is sufficient. The constants are absolute, and boundary points are counted correctly by the \(O(1)\) term per slice.

**3. Coprimality and the exact density.** Möbius inversion imposes \(\gcd(u,v)=1\). Because \(v\) is odd, every common divisor is odd; substituting \(u=d u'\), \(v=d v'\) for such an odd \(d\) preserves the oddness of \(v'\) and scales the quartic inequality by \(d^4\). Since \(u,v\ge1\), no common divisor exceeding \(T\) can contribute. Therefore
\[
S(X)=\sum_{\substack{1\le d\le T\\ d\text{ odd}}}\mu(d)L(T/d)
=\frac{AT^2}{2}\sum_{\substack{d\le T\\d\text{ odd}}}\frac{\mu(d)}{d^2}
+O\!\left(\sum_{d\le T}(T/d+1)\right).
\]
The last error is \(O(T\log(2T))\). Extending the absolutely convergent main sum to infinity costs \(O(T)\), and
\[
\sum_{d\text{ odd}}\frac{\mu(d)}{d^2}
=\prod_{p\ne2}\left(1-\frac1{p^2}\right)
=\frac{1/\zeta(2)}{1-1/4}=\frac8{\pi^2}.
\]
Hence \(S(X)=(4A/\pi^2)T^2+O(T\log(2T))\).

**4. Evaluation of the constant.** Polar coordinates \(x=\rho\cos\theta\), \(y=\rho\sin\theta\) for \(0<\theta<\pi/2\) give \(\rho^4(1+\cos^4\theta)\le1\), whence
\[
A=\frac12\int_0^{\pi/2}\frac{d\theta}{\sqrt{1+\cos^4\theta}}.
\]
Substituting \(T=X^{1/4}\) yields the asserted \(\kappa=4A/\pi^2\) and error \(O(X^{1/4}\log(2X))\). This proves the theorem for all real cutoffs and both parity branches of the Euclidean parametrization.

## Verification

Run `python3 verify_square_inradius.py` in a Python 3 environment with its standard library. It constructs primitive Euclidean triples and independently constructs the quartic coprime-pair parametrization. Exact set equality is asserted for hypotenuse bounds 100, 1000, 10000, 100000, 1000000 and 2000000; the largest test finds 396 qualifying triangles. It prints a numerical quadrature approximation \(\kappa\approx0.278365132811\). The computations are finite regression tests only. The infinite asymptotic and error term follow from the preceding argument.

## Relationship to prior work

Robbins, *Fibonacci Quarterly* **44** (2006), pp. 368–369, gives the classical representation \(r=n(m-n)\) and the exact number of primitive triangles with a **fixed inradius**. That fact is acknowledged; it does not count the triangles with **square inradius and hypotenuse at most a varying bound**. OEIS A087459 tabulates the related excess \(a+b-c=2r\) in order of increasing hypotenuse, and OEIS A020887 lists ordered excess values. These finite databases and the fixed-radius enumeration do not give the claimed area constant or the asymptotic error term. Omland's similarly titled 2016/2017 fixed-radius note and O'Loughlin's 2010 inradius note were identified but not fully inspectable; their full texts remain a specific literature-comparison uncertainty.

## Limitations

The theorem concerns primitive triangles, counted once up to swapping the legs, and the exact square-inradius condition. It does not count nonprimitive triples or prescribe a square hypotenuse/perimeter/area. The error estimate is elementary, not an asserted optimal discrepancy estimate. No claim of publication priority or independent audit is made; possible earlier unindexed treatments of the same hypotenuse-truncated statistic remain a residual originality risk.

## References

1. N. Robbins, “On the Number of Primitive Pythagorean Triangles with a Given Inradius,” *The Fibonacci Quarterly* **44** (2006), 368–369. DOI: `10.1080/00150517.2006.12428307`. Full text: `https://www.fq.math.ca/Papers1/44-4/quartRobbins04_2006.pdf`.
2. OEIS A087459, “Values (X + Y - Z) sorted on Z, then on Y ...” (dated initial entry 2003-10-23). `https://oeis.org/A087459`.
3. OEIS A020887, “Ordered set of a + b - c as ... primitive Pythagorean triples.” `https://oeis.org/A020887`.
4. T. Omland, “How many Pythagorean triples with a given inradius?”, *Journal of Number Theory* **170** (2017), 1–2. DOI: `10.1016/j.jnt.2016.06.009`.
5. M. O'Loughlin, “Half angles and the inradius of a Pythagorean triangle,” *The Mathematical Gazette* **94** (2010), 144–146. DOI: `10.1017/S0025557200007300`.
