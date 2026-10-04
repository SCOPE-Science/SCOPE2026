# Exact leading constant for the endpoint kernel norm of a trapezoidal disc mollifier

## Finding

For \(0<\delta<1/2\), define the canonical trapezoidal radial multiplier
\[
h_\delta(\xi)=
\begin{cases}
1,&|\xi|<1-\delta/2,\\
(1+\delta/2-|\xi|)/\delta,&1-\delta/2\le |\xi|\le1+\delta/2,\\
0,&|\xi|>1+\delta/2.
\end{cases}
\]
Use the Fourier convention
\[
\widehat f(\xi)=\int_{\mathbb R^2}f(x)e^{-ix\cdot\xi}\,dx,
\qquad
\mathcal F^{-1}g(x)=\frac1{(2\pi)^2}\int_{\mathbb R^2}g(\xi)e^{ix\cdot\xi}\,d\xi,
\]
and put \(K_\delta=\mathcal F^{-1}h_\delta\). Then
\[
\lim_{\delta\downarrow0}
\frac{\|K_\delta\|_{4/3}^{4/3}}{\log(1/\delta)}
=
\frac{2^{1/3}}{\pi^2}\,\mathrm B\!\left(\frac12,\frac76\right),
\]
where \(\mathrm B(a,b)=\Gamma(a)\Gamma(b)/\Gamma(a+b)\). Equivalently,
\[
\lim_{\delta\downarrow0}
\frac{\|K_\delta\|_{4/3}}{(\log(1/\delta))^{3/4}}
=
\frac{2^{1/4}}{\pi^{3/2}}\,\mathrm B\!\left(\frac12,\frac76\right)^{3/4}.
\]
The second constant is approximately \(0.3348516345\).

## Assumptions and scope

The statement is for the specific de la Vallée--Poussin-type trapezoidal profile displayed above, which is the concrete rough mollifier highlighted in the motivating paper. The dimension is exactly two and the exponent is exactly \(4/3\). The result concerns the convolution-kernel norm, not the full Fourier multiplier norm.

No assertion is made about the exact leading constant of \(\|h_\delta\|_{M_4}\) or \(\|h_\delta\|_{M_{4/3}}\). The motivating paper proves those operator norms have order \(\log(1/\delta)\), which is strictly larger than the kernel norm scale.

## Proof

Write \(r=|x|\), \(a=1-\delta/2\), and \(b=1+\delta/2\). Radial Fourier inversion gives
\[
K_\delta(r)=\frac1{2\pi}\int_0^\infty h_\delta(\rho)J_0(r\rho)\rho\,d\rho.
\]
Using
\[
\frac{d}{d\rho}\bigl(\rho J_1(r\rho)\bigr)=r\rho J_0(r\rho)
\]
and the fact that \(h_\delta'(\rho)=-1/\delta\) on \([a,b]\) and vanishes elsewhere, integration by parts yields the exact representation
\[
K_\delta(r)=\frac1{2\pi\delta r}\int_a^b \rho J_1(r\rho)\,d\rho.
\]
Let
\[
K_0(r)=\frac{J_1(r)}{2\pi r},
\]
the inverse Fourier transform of the unit-disc indicator.

Fix \(0<\varepsilon<1/4\). Standard large-argument bounds for \(J_1\) and its derivative imply, uniformly for \(1\le r\le\varepsilon/\delta\),
\[
|K_\delta(r)-K_0(r)|\le C\varepsilon r^{-3/2}.
\]
Indeed, averaging \(\rho J_1(r\rho)\) over the interval \([a,b]\) changes its value at \(\rho=1\) by at most \(C\delta r^{1/2}\); dividing by \(r\) gives the displayed estimate because \(\delta r\le\varepsilon\).

For the complementary range, the Bessel expansion
\[
J_1(t)=\sqrt{\frac2{\pi t}}\cos\!\left(t-\frac{3\pi}4\right)+O(t^{-3/2})
\]
and one integration by parts in the oscillatory average over \([a,b]\) give
\[
|K_\delta(r)|\le C\delta^{-1}r^{-5/2}
\qquad (r\ge\varepsilon/\delta),
\]
with \(C\) independent of \(\delta\) for fixed \(\varepsilon\). Hence
\[
2\pi\int_{\varepsilon/\delta}^\infty |K_\delta(r)|^{4/3}r\,dr
\le C\varepsilon^{-4/3},
\]
which is \(o(\log(1/\delta))\) as \(\delta\downarrow0\). The range \(0<r<1\) is uniformly bounded because \(h_\delta\) has uniformly bounded \(L^1(\mathbb R^2)\) norm.

For \(p=4/3\), the elementary inequality
\[
\bigl||u+v|^p-|u|^p\bigr|\le C_p\bigl(|u|^{p-1}|v|+|v|^p\bigr)
\]
shows that replacing \(K_\delta\) by \(K_0\) on \(1\le r\le\varepsilon/\delta\) changes the radial \(L^{4/3}\) integral by at most
\[
C\varepsilon\log(1/\delta)+O_\varepsilon(1).
\]

Now the standard Bessel asymptotic gives
\[
K_0(r)=c_0r^{-3/2}\cos\!\left(r-\frac{3\pi}4\right)+O(r^{-5/2}),
\qquad
c_0=\frac1{\sqrt2\,\pi^{3/2}}.
\]
The error contributes only \(O(1)\) to the \(4/3\)-power radial integral. Since \(|\cos t|^{4/3}\) is \(\pi\)-periodic,
\[
\lim_{R\to\infty}\frac1{\log R}
\int_1^R |\cos(r-3\pi/4)|^{4/3}\frac{dr}{r}
=
\frac1\pi\int_0^\pi|\cos t|^{4/3}\,dt
=
\frac1\pi\,\mathrm B\!\left(\frac12,\frac76\right).
\]
Therefore
\[
\lim_{R\to\infty}\frac{2\pi\int_1^R|K_0(r)|^{4/3}r\,dr}{\log R}
=
2\pi c_0^{4/3}\frac1\pi\,\mathrm B\!\left(\frac12,\frac76\right)
=
\frac{2^{1/3}}{\pi^2}\,\mathrm B\!\left(\frac12,\frac76\right).
\]
First let \(\delta\downarrow0\) with \(\varepsilon\) fixed, and then let \(\varepsilon\downarrow0\). This proves the first limit. Raising the coefficient to the power \(3/4\) gives the norm limit.

## Verification

The proof is analytic. The critical normalizations were checked directly from the motivating paper: it uses \(\widehat f(\xi)=\int f(y)e^{-iy\cdot\xi}\,dy\), lists the trapezoidal profile explicitly, and gives radial inverse Fourier normalization \((2\pi)^{-d/2}\) in its Hankel-transform notation. In dimension two these conventions give \(K_0(r)=J_1(r)/(2\pi r)\).

The coefficient calculation is then forced by the classical Bessel asymptotic and the exact periodic mean
\[
\frac1\pi\int_0^\pi|\cos t|^{4/3}\,dt
=
\frac1\pi\,\mathrm B\!\left(\frac12,\frac76\right).
\]
No finite numerical experiment is used to infer the limit. The decimal value quoted for the final constant is only a convenience and is not evidence for the theorem.

## Relationship to prior work

Carbery and Seeger prove a sharp endpoint multiplier estimate for mollifications of the planar disc multiplier. In the introduction and the accompanying remark they record
\[
\|K_\delta\|_{4/3}\asymp(\log(1/\delta))^{3/4}
\]
and contrast it with the larger operator norm
\[
\|h_\delta\|_{M_{4/3}}\asymp\log(1/\delta).
\]
Their statement is two-sided comparability: the exact leading coefficient of the kernel norm is not stated. Their full proof develops the sharper operator-norm result rather than evaluating this coefficient.

The Bessel asymptotic itself is classical and appears in the standard references used by the paper, including Stein--Weiss and Watson. What is new here is the combination of that asymptotic with the precise trapezoidal transition estimate to isolate the complete logarithmic coefficient of the endpoint kernel norm. Searches for the mollified-disc kernel, the \(L^{4/3}\) logarithmic asymptotic, the trapezoidal profile, and equivalent Bessel formulations found no prior statement of this coefficient.

## Limitations

This is not an exact asymptotic for the endpoint multiplier norm; the multiplier norm grows on the larger \(\log(1/\delta)\) scale. The theorem is not claimed for arbitrary mollifiers without additional control of their transition tails, and no higher-dimensional constant is asserted.

The originality comparison is strongest against the full motivating preprint, which treats exactly this multiplier and explicitly states only comparability of the kernel norm. Older disc-multiplier literature was searched by the same kernel and endpoint aliases, but an equivalent formula could still exist under substantially different notation.

## References

1. A. Carbery and A. Seeger, *Mollified disc multipliers*, arXiv:2609.32919v1, 2026.
2. E. M. Stein and G. Weiss, *Introduction to Fourier Analysis on Euclidean Spaces*, Princeton University Press, 1971.
3. G. N. Watson, *A Treatise on the Theory of Bessel Functions*, Cambridge University Press, 1995 reprint of the second edition.
