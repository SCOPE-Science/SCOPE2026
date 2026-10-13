# EBSH has a sharp heavy-tail phase at alpha equals one
## Finding
Let \(X\) follow the extended bounded sine hyperbolic (EBSH) distribution of Aldawsari et al., with
\[
\alpha>0,\qquad \theta>0,
\]
and cumulative distribution function
\[
F(x)=
\frac{
\sinh\!\left[
\frac{\pi}{2}
\left(1-e^{-x^\alpha}\right)^\theta
\right]
}{
\sinh(\pi/2)
},
\qquad x>0.
\]
Put
\[
C_\theta=
\frac{\pi\theta}{2}\coth\!\left(\frac{\pi}{2}\right).
\]
Then, as \(x\to\infty\),
\[
\boxed{
1-F(x)\sim C_\theta e^{-x^\alpha},
}
\]
\[
\boxed{
f(x)\sim
C_\theta\alpha x^{\alpha-1}e^{-x^\alpha},
}
\]
and
\[
\boxed{
h(x)\sim\alpha x^{\alpha-1}.
}
\]

These equivalents yield the sharp terminal phase diagram
\[
\begin{array}{c|c|c|c}
\alpha & \text{positive MGF} & h(x) & \text{tail class}\\
\hline
0<\alpha<1
&
\mathbb E[e^{tX}]=\infty\ \text{for every }t>0
&
h(x)\to0
&
\text{heavy and long-tailed}
\\
\alpha=1
&
\mathbb E[e^{tX}]<\infty\iff t<1
&
h(x)\to1
&
\text{exponential order}
\\
\alpha>1
&
\mathbb E[e^{tX}]<\infty\ \text{for every }t>0
&
h(x)\to\infty
&
\text{super-exponential}.
\end{array}
\]

Thus the source's statement that the EBSH distribution belongs to the class of light-tailed distributions is not valid throughout its stated parameter space under the standard definition based on positive exponential moments. The regime \(0<\alpha<1\) is genuinely heavy-tailed.

The parameter \(\theta\) affects the multiplicative tail constant \(C_\theta\), but it does not change the exponent \(\alpha\) governing terminal decay, nor the leading terminal hazard.

Every positive power moment remains finite:
\[
\boxed{
\mathbb E[X^r]<\infty
\quad\text{for every }r>0\text{ and every }\alpha,\theta>0.
}
\]
The upper quantile has the corresponding asymptotic scale
\[
\boxed{
Q(1-q)\sim
\left[\log\!\left(\frac1q\right)\right]^{1/\alpha}
}
\qquad(q\downarrow0).
\]

## Assumptions and scope
The distribution is exactly the EBSH model defined by the source, with
\[
\alpha,\theta>0,\qquad x>0.
\]
“Heavy-tailed” is used in the standard positive-exponential-moment sense: a nonnegative law is heavy-tailed when its moment-generating function is infinite for every positive argument. This criterion is equivalent to failure of any exponential upper-tail bound.

“Long-tailed” means that for every fixed \(y>0\),
\[
\frac{\Pr(X>x+y)}{\Pr(X>x)}\to1.
\]

The result classifies the terminal right tail, positive exponential moments, upper quantiles, and terminal hazard. It does not claim that finite-range hazard plots, skewness, likelihood fit, or predictive performance are determined solely by \(\alpha\).

## Proof
Write
\[
a=\frac{\pi}{2},
\qquad
u=e^{-x^\alpha}.
\]
The exact survival is
\[
1-F(x)
=
\frac{
\sinh(a)-\sinh\!\left(a(1-u)^\theta\right)
}{
\sinh(a)
}.
\]
As \(u\downarrow0\),
\[
(1-u)^\theta
=
1-\theta u+O(u^2).
\]
Taylor expansion of \(\sinh\) at \(a\) gives
\[
\sinh(a)-
\sinh\!\left(a(1-u)^\theta\right)
=
a\theta\cosh(a)u+O(u^2).
\]
Hence
\[
1-F(x)
\sim
a\theta\coth(a)e^{-x^\alpha}
=
C_\theta e^{-x^\alpha}.
\]

The published density is
\[
f(x)
=
a\alpha\theta\,
\operatorname{csch}(a)\,
x^{\alpha-1}e^{-x^\alpha}
\left(1-e^{-x^\alpha}\right)^{\theta-1}
\cosh\!\left[
a\left(1-e^{-x^\alpha}\right)^\theta
\right].
\]
The last two factors tend to \(1\) and \(\cosh(a)\), respectively, so
\[
f(x)
\sim
C_\theta\alpha x^{\alpha-1}e^{-x^\alpha}.
\]
Dividing by the survival equivalent yields
\[
h(x)=\frac{f(x)}{1-F(x)}
\sim
\alpha x^{\alpha-1}.
\]

For \(0<\alpha<1\) and any \(t>0\),
\[
tx-x^\alpha\to+\infty.
\]
Since
\[
f(x)\asymp
x^{\alpha-1}e^{-x^\alpha}
\]
on a sufficiently large tail interval,
\[
e^{tx}f(x)
\]
does not have an integrable tail, and therefore
\[
\mathbb E[e^{tX}]=\infty.
\]
Moreover, for fixed \(y>0\),
\[
\log\frac{1-F(x+y)}{1-F(x)}
=
-(x+y)^\alpha+x^\alpha+o(1)
\to0,
\]
so this regime is long-tailed.

When \(\alpha=1\),
\[
f(x)\sim C_\theta e^{-x}.
\]
Thus
\[
\mathbb E[e^{tX}]<\infty
\quad\text{for }t<1,
\]
while at \(t=1\) the integrand \(e^x f(x)\) tends to the positive constant \(C_\theta\), and for \(t>1\) it grows exponentially. Hence the positive MGF domain is exactly \(t<1\).

When \(\alpha>1\), for each fixed \(t>0\),
\[
tx-x^\alpha\to-\infty
\]
with superlinear negative growth, proving finiteness of every positive exponential moment.

Likewise, for every \(r>0\),
\[
x^r f(x)
\asymp
x^{r+\alpha-1}e^{-x^\alpha},
\]
which is integrable for every \(\alpha>0\). Hence all positive power moments are finite throughout the parameter space.

Finally, if \(q=1-F(Q(1-q))\), then
\[
q\sim C_\theta e^{-Q(1-q)^\alpha}.
\]
Taking logarithms gives
\[
Q(1-q)^\alpha
=
\log\!\left(\frac1q\right)
+\log C_\theta+o(1),
\]
and therefore
\[
Q(1-q)\sim
[\log(1/q)]^{1/\alpha}.
\]

## Verification
The accompanying checker evaluates the exact published EBSH CDF and density at high precision. For representative values on all three sides of the phase boundary, it verifies convergence of
\[
\frac{1-F(x)}
{C_\theta e^{-x^\alpha}},
\qquad
\frac{f(x)}
{C_\theta\alpha x^{\alpha-1}e^{-x^\alpha}},
\qquad
\frac{h(x)}
{\alpha x^{\alpha-1}}
\]
to \(1\).

It also checks the fixed-shift survival ratio numerically in the regime \(0<\alpha<1\), where the ratio approaches \(1\), and verifies the opposite terminal tendencies of the hazard for \(\alpha<1\) and \(\alpha>1\).

The computations are consistency checks only. The infinite-domain classifications follow from the analytic equivalents above.

## Relationship to prior work
Aldawsari et al. derive the EBSH density and CDF and state in their linear-representation section that the terminal factor
\[
e^{-x^\alpha}
\]
makes the EBSH distribution light-tailed. They further state that both \(\alpha\) and \(\theta\) control the rate of decay. The exact asymptotics above refine both assertions: \(\alpha\) creates a genuine heavy/exponential/super-exponential phase transition, while \(\theta\) changes only the leading multiplicative tail constant.

Saeed et al. introduce the bounded sine hyperbolic parent distribution on \((0,1)\). Its bounded support means that it has no unbounded right-tail phase to classify; the EBSH phase transition appears after the logarithmic-power transformation used by Aldawsari et al.

Modern heavy-tail references define a nonnegative law as heavy-tailed when its positive moment-generating function is infinite for every positive argument, equivalently when its tail is not exponentially bounded. Under that standard definition, the EBSH regime \(0<\alpha<1\) is heavy-tailed.

Focused searches using the exact EBSH name and DOI, stretched-exponential and Weibull-tail aliases, MGF-domain language, long-tail terminology, and the \(\alpha=1\) phase boundary did not locate a published EBSH theorem covering the survival constant, hazard equivalent, or complete MGF phase diagram.

## Limitations
The finding is a terminal asymptotic classification. It does not determine whether the hazard is globally monotone for a given parameter pair, nor does it replace the source's finite-range hazard-shape analysis.

The term “light-tailed” is not completely uniform across applied disciplines. The mathematical content here is therefore stated through the exact survival equivalents and MGF domains, which are definition-independent; the heavy/light labels are attached using the standard positive-MGF convention stated above.

No second-order tail expansion is claimed. The factor \(\theta\) can affect finite-threshold behavior even though it does not change the leading terminal exponent or hazard scale.

## References
1. A. M. A. Aldawsari, Z. F. Althobaiti, A. S. Mohammed, and A. A. R. Alharbi, “A new extended distribution with monotonic and nonmonotonic failure rates: statistical properties and comparative predictive modeling in medical datasets,” AIMS Mathematics 11 (2026), 14870–14914. DOI: 10.3934/math.2026613.
2. A. Saeed, A. Saboor, F. Jamal, N. Alsadat, O. S. Balogun, A. Faal, and M. Elgarhy, “Bounded sine hyperbolic distribution with applications to real datasets,” Kuwait Journal of Science 52 (2025), 100467. DOI: 10.1016/j.kjs.2025.100467.
3. B. Merz, S. Basso, G. Fischer, D. Lun, G. Blöschl, R. Merz, A. Guse, A. Viglione, S. Vorogushyn, and U. Wietzke, “Understanding heavy tails of flood peak distributions,” Water Resources Research 58 (2022), e2021WR030506. DOI: 10.1029/2021WR030506.
