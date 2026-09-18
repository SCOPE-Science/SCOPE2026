# Concave square-root cusp criterion for strict SDE comparison

## Result

Consider the synchronous one-dimensional driftless stochastic differential equation
\[
dX_t^x=\sigma(X_t^x)\,dB_t,\qquad X_0^x=x\in\mathbb R.
\]
Strict comparison means that for every \(x<y\),
\[
\mathbb P\!\left(X_t^x<X_t^y\ \text{for all }t\ge0\right)=1.
\]

Let \(\phi:[0,\infty)\to[0,\infty)\) be nondecreasing and concave, with
\[
\phi(0)=0,\qquad \phi(r)\le K\sqrt r\quad(r\ge0)
\]
for some finite \(K\). Define either
\[
\sigma_+(x)=1+\phi(x^+)
\]
or
\[
\sigma_{\mathrm{sym}}(x)=1+\phi(|x|).
\]

Then both coefficients have global pathwise-unique strong solutions and satisfy strict comparison:
\[
\boxed{
x<y\quad\Longrightarrow\quad
\mathbb P(X_t^x<X_t^y\text{ for every }t\ge0)=1.
}
\]

This gives a one-variable shape criterion implying the two-variable Lyapunov condition in Theorem 2.6 of Larsen (2026). It is stronger than merely assuming \(1/2\)-Hölder regularity: Larsen constructs \(C^\beta\) coefficients, including \(\beta\ge1/2\), for which strict comparison fails.

## Proof

Concavity and \(\phi(0)=0\) imply that \(r\mapsto \phi(r)/r\) is nonincreasing on \((0,\infty)\).

First, the square-root envelope and concavity imply a global \(1/2\)-Hölder bound. For \(0\le u<v\), put \(h=v-u\). If \(u\le h\), then \(v\le2h\), hence
\[
0\le\phi(v)-\phi(u)\le\phi(v)\le K\sqrt{2h}.
\]
If \(u>h\), concavity gives
\[
\frac{\phi(v)-\phi(u)}{h}
\le \frac{\phi(u)}{u}
\le \frac K{\sqrt u}
<\frac K{\sqrt h},
\]
so again \(\phi(v)-\phi(u)\le K\sqrt h\). Thus
\[
|\phi(v)-\phi(u)|\le \sqrt2K\,|v-u|^{1/2}.
\]
Because \(x\mapsto x^+\) and \(x\mapsto |x|\) are 1-Lipschitz, both \(\sigma_+\) and \(\sigma_{\mathrm{sym}}\) satisfy the Yamada-Watanabe pathwise-uniqueness modulus. Continuity and positivity give weak existence, hence strong existence; on \(\mathbb R\), the driftless solutions are global. Concavity also makes \(\phi\) locally Lipschitz away from zero, so Larsen's local-Lipschitz hypothesis off the cusp holds.

For \(D>0\), set
\[
\Sigma(M,D)=\frac{\sigma(M+D/2)+\sigma(M-D/2)}2,
\]
\[
\Delta(M,D)=\sigma(M+D/2)-\sigma(M-D/2),
\]
and
\[
\Gamma(M,D)=\Sigma(M,D)-\frac MD\,\Delta(M,D).
\]
Write \(z=M/D\). We verify Larsen's condition
\[
\Delta(M,D)^2\le D\,Q(z)\,\Gamma(M,D)^2
\]
with
\[
\boxed{
Q(z)=\frac{4K^2}{1+|z|}.
}
\]
Its one-sided integrals satisfy
\[
\int_0^bQ(u)\,du=\int_{-b}^0Q(u)\,du
=4K^2\log(1+b).
\]

If \(|z|\le1\), the two nonnegative arguments fed into \(\phi\) differ by at most \(D\), so the \(1/2\)-Hölder estimate gives
\[
\Delta(M,D)^2\le2K^2D\le DQ(z).
\]
If \(z\ge1\), put
\[
a=z+\frac12,\qquad b=z-\frac12.
\]
For both the one-sided and symmetric coefficients, the relevant increment is
\[
\phi(Da)-\phi(Db).
\]
Concavity gives
\[
\phi(Da)-\phi(Db)
\le D\,\frac{\phi(Db)}{Db}
=\frac{\phi(Db)}b
\le K\sqrt{\frac D b}
\le K\sqrt{\frac{2D}{z}},
\]
hence
\[
\Delta(M,D)^2\le\frac{2K^2D}{z}\le DQ(z).
\]
For \(z\le-1\), the one-sided increment vanishes, while the symmetric case reduces to the positive-\(z\) bound by evenness.

It remains to show \(\Gamma\ge1\). For the one-sided coefficient, if \(z\le-1/2\) then both cusp terms vanish. If \(-1/2\le z\le1/2\), only the upper point contributes and
\[
\Gamma-1=\left(\frac12-z\right)\phi\!\left(D\left(z+\frac12\right)\right)\ge0.
\]
For \(z\ge1/2\), with \(a=z+1/2\), \(b=z-1/2\),
\[
\Gamma-1=a\phi(Db)-b\phi(Da)\ge0,
\]
because \(\phi(r)/r\) is nonincreasing. For the symmetric coefficient, \(\Gamma\) is even. On \(0\le z\le1/2\), putting \(a=z+1/2\), \(b=1/2-z\),
\[
\Gamma-1=b\phi(Da)+a\phi(Db)\ge0,
\]
and for \(z\ge1/2\) the preceding concavity argument applies. Therefore \(\Gamma\ge1\) everywhere, and
\[
\Delta^2\le DQ\le DQ\,\Gamma^2.
\]
Theorem 2.6 of Larsen then yields strict comparison.

## A logarithmically damped square-root family

The criterion gives a continuum of explicit cusp coefficients beyond the pure square-root example. For \(\gamma\ge0\), write
\[
L(r)=\log(e/r),\qquad r_\gamma=e^{-(2\gamma+1)},
\]
and define
\[
\phi_\gamma(0)=0,
\]
\[
\phi_\gamma(r)=\frac{\sqrt r}{L(r)^\gamma},
\qquad 0<r\le r_\gamma,
\]
with constant continuation
\[
\phi_\gamma(r)=
\frac{\sqrt{r_\gamma}}{[2(\gamma+1)]^\gamma},
\qquad r\ge r_\gamma.
\]
Then \(\phi_\gamma\) is nondecreasing, concave, and satisfies
\[
0\le\phi_\gamma(r)\le\sqrt r.
\]
Indeed, for \(0<r<r_\gamma\),
\[
\phi_\gamma'(r)
=
r^{-1/2}L(r)^{-\gamma}
\left(\frac12+\frac{\gamma}{L(r)}\right)>0
\]
and
\[
\phi_\gamma''(r)
=
r^{-3/2}L(r)^{-\gamma}
\left[
-\frac14+\frac{\gamma(\gamma+1)}{L(r)^2}
\right].
\]
Since \(L(r)\ge2(\gamma+1)\) on this interval, the bracket is negative. At \(r_\gamma\), the slope drops from a nonnegative left derivative to zero, preserving concavity.

Consequently, for every \(\gamma\ge0\), both
\[
\boxed{
\sigma_{\gamma,+}(x)=1+\phi_\gamma(x^+)
}
\qquad\text{and}\qquad
\boxed{
\sigma_{\gamma,\mathrm{sym}}(x)=1+\phi_\gamma(|x|)
}
\]
satisfy strict comparison.

These examples have an exact Sobolev transition. Near zero,
\[
|\phi_\gamma'(r)|^p
\asymp
r^{-p/2}[\log(e/r)]^{-\gamma p}.
\]
Hence
\[
\phi_\gamma\in W^{1,p}_{\mathrm{loc}}
\quad\text{for every }p<2,
\]
while
\[
\boxed{
\phi_\gamma\in W^{1,2}_{\mathrm{loc}}
\iff \gamma>\frac12.
}
\]
At \(\gamma=1/2\), the \(L^2\)-derivative divergence is logarithmic.

The classical Yamada-Ogura strict-comparison modulus condition also fails for every \(\gamma\ge0\). Any local modulus \(\rho\) for \(\sigma_{\gamma,+}\) or \(\sigma_{\gamma,\mathrm{sym}}\) must satisfy
\[
\rho(h)\ge\phi_\gamma(h)
\]
for small \(h>0\), and therefore
\[
\int_{0+}\frac{h\,dh}{\rho(h)^2}
\le
\int_0^{r_\gamma}[\log(e/h)]^{2\gamma}\,dh
<\infty.
\]
Thus, for
\[
0<\gamma\le\frac12,
\]
strict comparison holds even though the Yamada-Ogura modulus condition fails and the standard \(W^{1,2}_{\mathrm{loc}}\) sufficient route is unavailable. No claim is made that these coefficients evade every possible factorization covered by Yamada's broader 1986 criterion.

For the canonical power cusps \(\phi(r)=r^\beta\) near zero, the square-root envelope holds exactly on the side \(\beta\ge1/2\). This is consistent with Larsen's sharp result that the coefficients \(1+(x^+)^\beta\) and \(1+|x|^\beta\) have strict comparison if and only if \(\beta\ge1/2\).

## Context and originality boundary

Larsen (2026) introduced the two-variable criterion used above and verified it for the pure root cusps \(1+\sqrt{x^+}\) and \(1+\sqrt{|x|}\). The same paper proves failure for the corresponding power cusps with exponent below \(1/2\), and gives counterexamples showing that Sobolev or Hölder regularity alone does not characterize strict comparison.

Yamada and Ogura (1981) gave the classical modulus sufficient condition
\[
\int_{0+}\frac{u\,du}{\rho(u)^2}=\infty.
\]
Yamada (1986) gave a broader factorization criterion and, after localization, covers positive \(W^{1,2}_{\mathrm{loc}}\) coefficients. Fang and Zhang (2005) and Lan and Wu (2014) provide more general nonconfluence results; Larsen explains that, after specialization to the present driftless one-dimensional setting, their modulus assumptions do not enlarge the older class relevant here.

To the best of our knowledge, the surveyed literature does not state the reduction of Larsen's two-variable condition to the concave square-root envelope above, nor the logarithmically damped family with its exact \(W^{1,2}\) transition. The latter is particularly informative for \(0<\gamma\le1/2\): it gives an explicit continuum of strict-comparison coefficients beyond the standard \(W^{1,2}\) route while still failing the classical Yamada-Ogura modulus test.

The main residual originality risk is Yamada's 1986 factorization theorem and related older one-dimensional nonconfluence literature: the full theorem was not inspected here, and an equivalent shape criterion may be encoded there under different factorization language. The present originality claim is therefore limited to the explicit reduction and family above, to the best of our knowledge.

## Limitations

The criterion is sufficient, not necessary. Concavity and the square-root envelope are structural assumptions; Larsen's general two-variable theorem applies beyond this class. The logarithmically damped examples are one-dimensional, driftless, uniformly positive diffusions with one cusp. No converse is proved for logarithmic perturbations, and no claim is made about multidimensional SDEs, nonzero drift, discontinuous diffusion coefficients, or a complete characterization of strict comparison.

## References

- Kasper Larsen, *Strict SDE Comparison for Cusp Coefficients and Counterexamples*, arXiv:2609.19389, 2026. https://arxiv.org/abs/2609.19389
- Toshio Yamada and Yukio Ogura, *On the strong comparison theorems for solutions of stochastic differential equations*, Z. Wahrscheinlichkeitstheorie verw. Gebiete 56 (1981), 3-19. https://doi.org/10.1007/BF00531971
- Toshio Yamada, *On the non-confluent property of solutions of one-dimensional stochastic differential equations*, Stochastics 17 (1986), 111-124. https://doi.org/10.1080/17442508608833385
- Shizan Fang and Tusheng Zhang, *A study of a class of stochastic differential equations with non-Lipschitzian coefficients*, Probab. Theory Relat. Fields 132 (2005), 356-390. https://doi.org/10.1007/s00440-004-0398-z
- Guangqiang Lan and Jiang-Lun Wu, *New sufficient conditions of existence, moment estimations and non confluence for SDEs with non-Lipschitzian coefficients*, Stochastic Processes and their Applications 124 (2014), 4030-4049. https://doi.org/10.1016/j.spa.2014.07.010
