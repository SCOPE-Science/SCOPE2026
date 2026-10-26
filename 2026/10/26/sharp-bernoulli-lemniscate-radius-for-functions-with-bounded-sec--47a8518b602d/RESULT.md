# Sharp Bernoulli-lemniscate radius for functions with bounded second derivative

## Finding

For every real \(M>0\), put \(\mathcal Q_1(M)=\{f\in\mathcal O(\mathbb D):f(0)=0,\ f'(0)=1,\ |f''(z)|\le M\text{ for all }z\in\mathbb D\}\). The sharp radius of starlikeness associated with the right Bernoulli lemniscate \(\Omega_{\mathrm{Le}}=\{w:|w^2-1|<1,\ \Re w>0\}\) is
\[
R_{\mathrm{Le}}(\mathcal Q_1(M))=\min\left\{1,\frac{\sqrt{2/3}}{M}\right\}.
\]
In other words, for every \(f\in\mathcal Q_1(M)\), the logarithmic derivative \(zf'(z)/f(z)\) is subordinate on \(|z|<R\) to the principal branch \(\sqrt{1+z}\), and this radius is best possible. For \(M>\sqrt{2/3}\), a quadratic function witnesses sharpness arbitrarily close outside the stated radius.

A stronger exact variability assertion underlies the bound: for each fixed \(z\ne0\), \(r=|z|\), \(m=Mr<1\), the complete region of values of \(zf'(z)/f(z)\) across \(\mathcal Q_1(M)\) is
\[
\left\{\frac{1+m w}{1+\frac m2w}:\ |w|\le1\right\}.
\]
All boundary points are realized by the quadratic family \(f_\theta(\zeta)=\zeta+(M/2)e^{i\theta}\zeta^2\).

## Assumptions and scope

Here \(\mathbb D=\{z\in\mathbb C:|z|<1\}\); \(M\) is any positive real number and no univalence hypothesis is added. The radius is the supremum of \(r\le1\) such that all dilations \(f(r\zeta)/r\) belong to the specified Ma--Minda starlike class. The normalizations of \(f\), \(\Omega_{\mathrm{Le}}\), and the principal square root matter. The equality formulation for a radius means that every smaller radius is valid, not that the open-image condition must hold at a tangent boundary point.

## Proof

**1. A weighted Schwarz--Pick moment inequality.** Let \(h\) be any Schur function on \(\mathbb D\): \(|h(t)|\le1\) for real \(0\le t<1\). Set
\[
A=\int_0^1t h(t)\,dt,\quad B=\int_0^1(1-t)h(t)\,dt,\quad C=B-A.
\]
Then \(2|A|+|C|\le1\). Indeed, integration by parts gives \(C=-\int_0^1t(1-t)h'(t)\,dt\). For any unit complex \(\xi\), Schwarz--Pick and \(1-|h|^2\le2(1-\Re(\overline\xi h))\) imply
\[
|C|\le\int_0^1\frac{t(1-|h(t)|^2)}{1+t}\,dt
\le 2\int_0^1t(1-\Re(\overline\xi h(t)))\,dt.
\]
Choosing \(\xi=A/|A|\) if \(A\ne0\), or arbitrary \(\xi\) otherwise, yields \(|C|\le1-2|A|\). Constant unimodular \(h\) gives \(|A|=1/2\), \(C=0\), so the inequality is sharp.

**2. Exact region of logarithmic derivatives.** Fix \(0<|z|=r<1\), and set \(m=Mr<1\). Let \(h(t)=f''(tz)/M\), initially on a slightly larger complex disk around \([0,1]\); Schwarz--Pick on the disk \(|t|<1/r\) gives \(|h'(t)|\le (1-|h(t)|^2)/(1-t^2)\) for \(0\le t<1\), since restriction to the unit disk suffices. Taylor's integral identities are
\[
f(z)/z=1+Mz B,\qquad f'(z)=1+Mz(A+B),
\]
whence, with \(p=zf'(z)/f(z)\),
\[
\frac{p-1}{2-p}=\frac{Mz A}{1+Mz C}.
\]
Here \(|Mz C|\le m|C|<1\) and \(|Mz B|\le m/2<1\), so denominators are nonzero. By the moment inequality,
\[
\left|\frac{p-1}{2-p}\right|\le\frac{m|A|}{1-m|C|}\le\frac{m|A|}{1-|C|}\le\frac m2.
\]
(The case \(A=0\) follows immediately.) This is precisely \(p=P_m(w)\) for some \(|w|\le1\), where \(P_m(w)=(1+mw)/(1+(m/2)w)\). Conversely, any \(|w|\le1\) is realized by taking \(f(\zeta)=\zeta+(M/2)e^{i\theta}\rho\zeta^2\), with \(\rho=|w|\) and phase chosen so that \(e^{i\theta}z/r=w/|w|\), interpreting \(w=0\) separately. Thus the variability region is exact. At \(z=0\) the logarithmic derivative extends as \(p(0)=1\).

**3. Exact disk--lemniscate containment.** Set \(a=m/2\), and write \(w\) on the unit circle with \(c=\Re w\in[-1,1]\). Direct expansion gives
\[
|P_m(w)^2-1|^2=\frac{a^2(4+12ac+9a^2)}{(1+2ac+a^2)^2}.
\]
The difference between its denominator and numerator equals
\[
(1-2a^2+2ac)^2+2a^2(1-6a^2).
\]
It is strictly positive whenever \(0<m<\sqrt{2/3}\). Maximum modulus then gives \(|P_m(w)^2-1|<1\) for \(|w|\le1\). Moreover \(|P_m(w)-1|\le m/(2-m)<1\), placing the entire disk inside the right lobe \(\Omega_{\mathrm{Le}}\). Thus all \(f\in\mathcal Q_1(M)\) satisfy the desired subordination for \(|z|<\min\{1,\sqrt{2/3}/M\}\); the analytic inverse square mapping of \(\Omega_{\mathrm{Le}}\) supplies the required Schwarz function.

**4. Sharpness.** At \(a_*=1/\sqrt6\), the squared difference vanishes for \(c_*=-\sqrt{2/3}\), which lies in \((-1,1)\). For every \(a>a_*\) sufficiently near \(a_*\), choose \(c=(2a^2-1)/(2a)\in(-1,1)\); then the difference is \(2a^2(1-6a^2)<0\). Choose \(w\in\partial\mathbb D\) with this real part, and select the quadratic extremizer above so that its logarithmic derivative at \(z=r\) equals \(P_{Mr}(w)\). If \(M>\sqrt{2/3}\), radii \(r>\sqrt{2/3}/M\), arbitrarily close to that number, therefore fail lemniscate starlikeness. If \(M\le\sqrt{2/3}\), the entire unit disk works and the radius cannot exceed one by definition.

## Verification

The auxiliary script `check.py` verifies the Möbius and sum-of-squares identities exactly using symbolic algebra, checks the tangent point, and displays sample boundary moduli. Its finite sample values are diagnostic, not substitutes for the analytic Schwarz--Pick argument or the global strict inequality. All proof inequalities are valid for arbitrary complex Schur functions and all positive real \(M\) in the stated range.

## Relationship to prior work

Poomalai and Ravichandran, arXiv:2610.07845v1 (first posted 2026-10-06), Theorem 3.2 and Remark 3.3, give for \(\mathcal Q_1(M)\) the sufficient lower bound \(\min\{1,(2-\sqrt2)/M\}\) and explicitly identify the available radius as only a lower estimate. Their argument uses the centered bound for the logarithmic derivative; the present moment inequality yields the exact, displaced Möbius variability disk and a sharp radius larger when \(M>\sqrt{2/3}\). The 2006 paper by Korzybska, Kowalczyk, and Wójcik derives a centered disk estimate for these bounded-second-derivative classes, but not the displaced variability disk or its sharp Bernoulli-lemniscate radius. Earlier lemniscate subordination criteria operate under different differential or quotient hypotheses.

## Limitations

The exact result concerns \(n=1\) (no prescribed higher vanishing derivative), the right Bernoulli lemniscate, and real \(M>0\). No result is claimed for general \(\mathcal Q_n(M)\) with \(n>1\), other Ma--Minda targets, or uniqueness of extremizers. The threshold depends on the chosen normalization. The originality comparison covers the accessible cited primary works and targeted searches, not an exhaustive proof that no mathematically equivalent statement exists elsewhere. No independent audit has been performed.

## References

1. P. Poomalai and V. Ravichandran, *Radius of Ma--Minda Starlikeness and Convexity for Functions with Bounded Second Derivative*, arXiv:2610.07845v1 (2026-10-06), Theorem 3.2 and Remark 3.3; https://arxiv.org/abs/2610.07845.
2. U. Korzybska, K. Kowalczyk, P. Wójcik, *On a convex class of univalent functions*, Ann. Univ. Mariae Curie-Skłodowska Sect. A 60 (2006), 31--38; https://bc.umcs.pl/Content/22057/PDF/czas4050_60_2006_4.pdf.
3. S. Kumar and collaborators, *Sufficient conditions for starlike functions associated with lemniscate of Bernoulli* (2013); comparison of distinct differential subordinations.
