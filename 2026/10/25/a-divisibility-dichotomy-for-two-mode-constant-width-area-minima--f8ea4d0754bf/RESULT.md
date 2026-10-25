# A divisibility dichotomy for two-mode constant-width area minima

## Finding
Fix odd integers \(3\le n<m\), and a width \(w>0\). Among all planar convex bodies with prescribed-axis support function
\[
h(\theta)=\frac w2+a\cos(n\theta)+b\cos(m\theta),
\]
adding the higher cosine mode \(m\) strictly reduces the minimum attainable area **if and only if \(n\mid m\)**. More precisely:

1. **Nondivisible frequencies.** If \(n\nmid m\), the exact sharp minimum is
\[
\boxed{\min\operatorname{Area}=\frac{\pi w^2}{4}-\frac{\pi w^2}{8(n^2-1)}.}
\]
In the fixed coordinates, equality holds **only** for \(b=0\) and \(a=\pm w/[2(n^2-1)]\). Define \(d=n/\gcd(n,m)\ge3\), \(r^2=(n^2-1)/(m^2-1)\), and
\[
\kappa_d^2=\begin{cases}\frac12,&d=3,\\ \cos^2(\pi/d),&d\ge5.\end{cases}
\]
Then \(\kappa_d^2>r^2\). Every body in the family obeys the quantitative area gap
\[
\boxed{\operatorname{Area}(h)-\operatorname{Area}_{\min}
\ \ge\ \frac{\pi w^2}{8(n^2-1)}(\kappa_d^2-r^2)
\left(\frac{2(m^2-1)b}{w}\right)^2.}
\]
The displayed gap coefficient is explicit and positive, but is not asserted to be optimal.

2. **Divisible frequencies.** If \(m=kn\) for an odd integer \(k\ge3\), put \(t=1/(k^2+1)\) and take
\[
\boxed{a=\frac{w(1+t)}{2(n^2-1)},\qquad
b=-\frac{wt}{2(m^2-1)}.}
\]
This is a genuine convex body of width \(w\), and its area is **strictly smaller** than the nondivisible/pure-\(n\) benchmark, by the exact amount
\[
\frac{\pi w^2}{8(n^2-1)}\bigl(2t+(1+r^2)t^2\bigr)>0.
\]
No sharp formula for the full divisible-frequency minimum is asserted here. The theorem is the complete arithmetic criterion for whether the second harmonic helps, plus a sharp minimum and explicit stability bound throughout the complementary class.

## Assumptions and scope
The support function is \(h(\theta)=\max_{x\in K}\langle x,(\cos\theta,\sin\theta)\rangle\), measured relative to fixed Cartesian axes. Bodies are compact convex subsets of \(\mathbb R^2\) with nonempty interior. Weak convexity is included: the continuous curvature-radius density \(h+h''\) may vanish at isolated directions. Since both frequencies are odd, \(h(\theta)+h(\theta+\pi)=w\), so width is identically \(w\). No sine coefficients, translation terms, or other Fourier modes are admitted; this is a genuine fixed-axis two-mode problem, not the unrestricted Blaschke–Lebesgue problem.

Introduce the dimensionless coefficients and weight
\[
X=\frac{2(n^2-1)a}{w},\qquad Y=\frac{2(m^2-1)b}{w},\qquad r^2=\frac{n^2-1}{m^2-1}.
\]
The exact convexity and area identities are
\[
\|X\cos(n\theta)+Y\cos(m\theta)\|_{L^\infty(\mathbb R)}\le1,
\qquad
\operatorname{Area}(h)=\frac{\pi w^2}{4}
-\frac{\pi w^2}{8(n^2-1)}(X^2+r^2Y^2).
\]

## Proof
**1. Curvature and area reduction.** For twice continuously differentiable periodic support functions, \(h+h''\ge0\) is necessary and sufficient for convexity: the normal-angle parametrization \(x(\theta)=h u+h'u_\perp\) has tangent derivative \((h+h'')u_\perp\). Here
\[
h+h''=\frac w2\{1-X\cos(n\theta)-Y\cos(m\theta)\}.
\]
Shifting \(\theta\) by \(\pi\) changes the sign of both cosines, making the nonnegativity condition equivalent to the stated uniform-norm inequality. The standard support-area formula \(\operatorname{Area}=\tfrac12\int_0^{2\pi}(h^2-h'^2)d\theta\), followed by cosine orthogonality, gives the stated area identity. Thus minimizing area amounts to maximizing \(J=X^2+r^2Y^2\) subject to the exact norm constraint.

**2. Sharp nondivisible norm inequality.** Assume \(n\nmid m\). Put \(g=\gcd(n,m)\), \(d=n/g\) and \(q=m/g\). Then \(d,q\) are odd coprime integers, \(3\le d<q\), and so \(q\ge d+2\). Changing both coefficient signs does not change the norm, so assume \(X\ge0\). At \(\theta_j=2\pi j/n\), the first cosine equals one, while the second assumes the \(d\) distinct values \(\cos(2\pi j/d)\) (each repeated \(g\) times), because \(\gcd(q,d)=1\).

If \(d=3\), the mean of the three sampled squared values is exactly \(X^2+Y^2/2\): the cosines have zero mean and squared mean \(1/2\). Hence
\[
\|X\cos(n\theta)+Y\cos(m\theta)\|_\infty^2\ge X^2+Y^2/2.
\]
If \(d\ge5\), the largest sampled cosine is \(1\) and the smallest is \(-\cos(\pi/d)\). For \(Y\ge0\), a sampled value equals \(X+Y\); for \(Y<0\), one equals \(X+\cos(\pi/d)|Y|\). Hence the norm is at least \(X+\cos(\pi/d)|Y|\), and consequently its square is at least \(X^2+\cos^2(\pi/d)Y^2\). These arguments establish the uniform bound
\[
\boxed{\|X\cos(n\theta)+Y\cos(m\theta)\|_\infty^2\ge X^2+\kappa_d^2Y^2.}
\]

**3. Strict weight comparison and all equality cases.** Since \(q\ge d+2\),
\[
r^2<\frac{n^2}{m^2}=\frac{d^2}{q^2}\le\frac{d^2}{(d+2)^2}.
\]
For \(d=3\), the latter bound is \(9/25<1/2\). For odd \(d\ge5\), the elementary inequalities \(\pi^2<10\) and \(\cos x>1-x^2/2\) for \(0<x\le\pi/5\) give
\[
\cos(\pi/d)>1-5/d^2>\frac{d}{d+2},
\]
where the final strict comparison is exactly \(2d^2-5d-10>0\), valid for \(d\ge5\). Thus \(\kappa_d^2>r^2\) always. If the norm is at most one, then
\[
J=X^2+r^2Y^2\le1-(\kappa_d^2-r^2)Y^2\le1.
\]
Equality forces \(Y=0\), and then \(|X|=1\). Both signed one-mode choices are admissible; the area minimum, uniqueness, and displayed area-gap inequality follow at once.

**4. Constructive strict gain for every divisible pair.** If \(m=kn\), then \(k\) is odd and \(k\ge3\). Let \(t=(k^2+1)^{-1}\), \(X=1+t\), \(Y=-t\), and \(x=\cos(n\theta)\). The cosine multiple-angle identity gives \(\cos(m\theta)=T_k(x)\), where \(T_k\) is the Chebyshev polynomial. Its derivative satisfies \(\|T_k'\|_{L^\infty([-1,1])}\le k^2\): for \(x=\cos s\), \(T_k'(x)=k\sin(ks)/\sin s\), and \(|\sin(ks)|\le k|\sin s|\) follows by induction from the sine addition formula; endpoints follow by continuity. Since \(T_k(\pm1)=\pm1\) for odd \(k\), comparison with \(\operatorname{sgn}(x)\) yields
\[
|x-T_k(x)|\le(k^2+1)(1-|x|),\qquad -1\le x\le1.
\]
Therefore
\[
|(1+t)x-tT_k(x)|\le |x|+t(k^2+1)(1-|x|)=1.
\]
The proposed curvature profile is nonnegative everywhere, so it gives a bona fide convex body. Finally
\[
J=(1+t)^2+r^2t^2=1+2t+(1+r^2)t^2>1,
\]
proving a strict area improvement for every divisible pair with the exact indicated margin. Together with Steps 2–3 this gives the claimed if-and-only-if criterion for all permitted indices and widths.

## Verification
Run `python3 verify.py` in the same directory as this document; Python's standard library suffices. The checker verifies rational comparison inequalities for many odd divisors, 3,581 nondivisible frequency pairs, independent high-resolution trigonometric-norm and stability tests, admissible strictly improving resonant constructions, and numerical quadrature of the support-area identity. These finite checks corroborate, but do not replace, the universal analytic argument above. All constants and boundary equality cases are specified symbolically in the proof.

## Relationship to prior work
Bayen and Henrion study optimization of convex bodies subject to width constraints using semidefinite programming; their accessible bibliographic record and abstract do not resolve the all-frequency arithmetic classification here. Their full primary manuscript could not be examined, so overlap there remains a concrete bibliographic risk. Resnikoff develops Fourier/support-function constructions for curves of constant width and derives one-mode examples. Antunes and Bogosel examine numerical support-function shape optimization, including constant-width problems. These methods provide the natural setting but do not state the sharp nondivisible minimum and its arithmetic complement in the inspected portions.

A closely relevant published mathematical note, *Sharp two-harmonic area minimum for dihedrally invariant constant-width bodies*, solves the **divisible \(m=3n\)** case and gives its full exact optimizer. Its stronger result for that particular divisible class is expressly not repeated or contradicted: the contribution here is the dichotomy across **all** odd higher frequencies, the unique pure-mode optimizer for every nondivisible pair, and explicit nondivisible stability. Another published note, *Odd-multiple rigidity for one-frequency Carathéodory–Fejér augmentation*, gives a superficially similar divisibility rule for a different optimization: maximizing the coefficient of \(\cos\theta\) in a nonnegative three-frequency polynomial. It does not control the weighted quadratic area objective of the present two-frequency curvature problem. Overlap was assessed by mathematical statements and implications, not title similarity.

## Limitations
The sharp **value** of the divisible-frequency two-mode area minimum is not determined here; only a strictly improving feasible construction is claimed for all such pairs. The explicit nondivisible stability coefficient need not be best possible. No claim is made for sine phases, arbitrary mixtures of frequencies, unrestricted constant-width shapes, or higher-dimensional bodies. One plausible earlier primary manuscript was available only through its bibliographic description, so definitive historical priority needs independent examination. No independent mathematical audit has been performed.

## References
1. T. Bayen and D. Henrion, *Semidefinite programming for optimizing convex bodies under width constraints*, DOI:10.1080/10556788.2010.547580, first verified online date 2011-08-15. https://doi.org/10.1080/10556788.2010.547580
2. H. L. Resnikoff, *On Curves and Surfaces of Constant Width*, arXiv:1504.06733v1 (2015-04-25). https://arxiv.org/abs/1504.06733
3. P. R. S. Antunes and B. Bogosel, *Parametric Shape Optimization using the Support Function*, arXiv:1809.00254 (2018). https://arxiv.org/abs/1809.00254
4. *Sharp two-harmonic area minimum for dihedrally invariant constant-width bodies*, published published-finding corpus mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-two-harmonic-area-minimum-for-dihedrally-invariant-constan--0094d4f2c8a9
5. *Odd-multiple rigidity for one-frequency Carathéodory–Fejér augmentation*, published published-finding corpus mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-odd-multiple-rigidity-for-one-frequency-carath-odory-fej-r-augme--537434123da6
