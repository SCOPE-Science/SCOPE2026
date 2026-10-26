# A sharp unequal-jump sub-gamma phase surface and quadratic crossover

## Finding

For every \(0\le b<1\), the variance-one infinitely divisible family \(X_{b,p}\), \(0<p<1\), defined below has an **exact phase boundary**
\[
p_*(b)=\frac{5b+3+\sqrt{9b^2+30b+9}}{8(1+b)}.
\]
Let \(c_+(b,p)\) be its least right sub-gamma scale when the quadratic proxy is fixed at the **true variance one**, and let \(m(b,p)=[p-(1-p)b]/3\). The complete classification is
\[
\begin{aligned}
p_*(b)\le p<1&:\quad c_+(b,p)=m(b,p) \quad\text{(local control)},\\
0<p<p_*(b)&:\quad c_+(b,p)>\max\{0,m(b,p)\}\quad\text{(positive interior control)}.
\end{aligned}
\]
In the second regime the infimum is attained by at least one strictly positive finite variational argument; on the boundary \(p=p_*(b)\) the optimum is **only** the zero-argument limit. The crossover is quadratic: let \(p_*=p_*(b)\), \(m_* =m(b,p_*)\), and
\[
 u(b)=-\left[\frac{1-b^2}{12}-\frac{2(1+b)m_*}{3}\right]>0,\qquad
 B(b)=\frac{p_*-(1-p_*)b^3}{60}-m_*^3<0.
\]
For fixed \(0\le b<1\), as \(p\uparrow p_*\) from below the global maximizer is unique and satisfies
\[
 t_{\rm opt}(b,p)=\frac{u(b)}{-2B(b)}(p_*-p)+O((p_*-p)^2),
\quad
 c_+(b,p)=m(b,p)+\frac{u(b)^2}{-4B(b)}(p_*-p)^2+O((p_*-p)^3).
\]
In the Gaussian-smoothing endpoint \(b=0\), the phase threshold is exactly \(p_*(0)=3/4\), and the coefficients reduce to
\[
 t_{\rm opt}(0,p)=\frac{40}{3}\left(\frac34-p\right)+O\!\left(\left(\frac34-p\right)^2\right),\quad
 c_+(0,p)=\frac p3+\frac59\left(\frac34-p\right)^2+O\!\left(\left(\frac34-p\right)^3\right).
\]
For every fixed \(0\le b<1\), the rare-positive-jump boundary has the uniform exponent
\[\lim_{p\downarrow0}c_+(b,p)\log(1/p)=1.\]
The limiting value at \(b=1\) is \((2+\sqrt3)/4\), the already-published equal-amplitude Skellam phase threshold; that endpoint is **not claimed as new**.

## Assumptions and scope

Fix \(0\le b<1\) and \(0<p<1\). When \(b>0\), let \(N_+\) and \(N_-\) be independent Poisson variables with means \(p\) and \((1-p)/b^2\), respectively, and set
\[
X_{b,p}=N_+-p-b\left(N_--\frac{1-p}{b^2}\right).
\]
For \(b=0\), let \(G\) be an independent standard Gaussian and set
\[
 X_{0,p}=N_+-p+\sqrt{1-p}\,G.
\]
In both cases \(\mathbb EX_{b,p}=0\), \(\operatorname{Var}(X_{b,p})=1\), and all exponential moments exist. Define \(c_+(b,p)\) as the infimum of \(c\ge0\) for which
\[
\log\mathbb E\exp(tX_{b,p})\le\frac{t^2}{2(1-ct)}\quad
\text{for every }0\le t<1/c,
\]
with \(1/0=+\infty\). The quantity optimized is the exact-variance right scale, not the best variance proxy or the negative-tail scale.

## Proof

**1. Exact moment-generating transform.** Set \(K_{b,p}(t)=\log\mathbb E\exp(tX_{b,p})\) and \(M_{b,p}(t)=2K_{b,p}(t)/t^2\) for \(t>0\), extended by \(M_{b,p}(0)=1\). By Poisson and Gaussian exponential generating functions,
\[
K_{b,p}(t)=p(e^t-1-t)+\begin{cases}
\dfrac{1-p}{b^2}(e^{-bt}-1+bt),&b>0,\\
\dfrac{1-p}{2}t^2,&b=0.
\end{cases}
\]
An entire-function expansion gives
\[
 M_{b,p}(t)=\sum_{n=0}^{\infty}a_n(b,p)t^n,\qquad
 a_0=1,\qquad a_n=\frac{2\{p+(1-p)(-b)^n\}}{(n+2)!}\quad(n\ge1).
\]
The same expression applies at \(b=0\) with \(0^n=0\) for \(n\ge1\). In particular,
\[
 m=a_1=\frac{p-(1-p)b}{3},\qquad a_2=\frac{p+(1-p)b^2}{12},\qquad a_3=\frac{p-(1-p)b^3}{60}.
\]
The elementary equivalence between the defining sub-gamma inequality and a bound on \(M\) gives the variational identity
\[
 c_+(b,p)=\max\left\{0,\sup_{t>0}F_{b,p}(t)\right\},\qquad
 F_{b,p}(t)=\frac{1-M_{b,p}(t)^{-1}}{t}.
\]
Indeed for \(t<1/c\), \(M(t)\le (1-ct)^{-1}\) is equivalent to \(F(t)\le c\); for \(t\ge1/c\), automatically \(F(t)<1/t\le c\). This identity is also the previously known signed-canonical-remainder formula.

**2. Location of the phase boundary.** Expansion at the origin yields
\[
 F_{b,p}(t)=m+(a_2-m^2)t+(a_3-2ma_2+m^3)t^2+O(t^3).
\]
The two roots in \(p\) of \(a_2=m^2\) are
\[
\frac{5b+3\pm\sqrt{9b^2+30b+9}}{8(1+b)}.
\]
The greater root is \(p_*(b)\). One checks that \(0<p_*(b)<1\) for \(b<1\) and \(p_*(b)>b/(1+b)\); thus for \(p\ge p_*(b)\), \(m>0\) and \(a_2\le m^2\). The latter means
\[
\frac{p+(1-p)b^2}{p-(1-p)b}\le4m.
\]
All \(a_n\) are then nonnegative, since \(p>(1-p)b\) and \(0\le b\le1\). For each integer \(n\ge1\),
\[
\frac{a_{n+1}}{a_n}
=\frac{p+(1-p)(-b)^{n+1}}{(n+3)\{p+(1-p)(-b)^n\}}
\le\frac{p+(1-p)b^2}{(n+3)\{p-(1-p)b\}}
\le\frac{4m}{n+3}\le m.
\]
Consequently \(a_n\le m^n\) by induction, with strict inequality for every \(n\ge3\). For \(0<t<1/m\), summation proves
\[
 M_{b,p}(t)\le\frac1{1-mt}
\quad\Longrightarrow\quad F_{b,p}(t)\le m.
\]
For \(t\ge1/m\), the elementary bound \(F(t)<1/t\le m\) gives the same conclusion. The limit \(F(0+)=m\) shows \(c_+=m\), with no positive maximizer at \(p=p_*\).

For \(p<p_*\) with \(m>0\), the quadratic polynomial \(a_2-m^2\) is strictly positive: this follows from its concavity in \(p\) and the fact that \(p\) lies above the lower root and below the upper root whenever \(m>0\). Thus \(F(t)>m\) for all sufficiently small \(t>0\). If instead \(m\le0\), the positive unit jump with intensity \(p>0\) implies \(M(t)\to\infty\); hence \(F(t)>0\) for all sufficiently large \(t\). In either case \(c_+>\max\{0,m\}\). The function \(F\) is continuous, has the finite limit \(m\) at zero, and tends to zero at infinity, so its positive strict supremum is attained at a finite positive argument.

**3. Quadratic bifurcation.** Write \(A(p)=a_2-m^2\), \(B(p)=a_3-2ma_2+m^3\). At the upper zero \(p_*\) of the strictly concave quadratic \(A\), its derivative is negative, so \(u=-A'(p_*)>0\). At \(p_*\), \(a_2=m_*^2\), and the strict ratio bound for \(n=2\) in step 2 gives \(a_3<m_*^3\); hence \(B(p_*)<0\). The analytic extension of \(F\) satisfies \(\partial_tF(p_*,0)=0\) and \(\partial_{tt}F(p_*,0)=2B(p_*)<0\). The implicit-function theorem therefore supplies a unique nearby critical point for \(p<p_*\) with
\[
 t_{\rm opt}=\frac{u}{-2B(p_*)}(p_*-p)+O((p_*-p)^2).
\]
It is the unique *global* maximizer for all \(p<p_*\) sufficiently close to \(p_*\): at \(p_*\), the preceding strict inequality makes \(F(p_*,t)<m_*\) for every \(t>0\); the bound \(F(p,t)<1/t\) makes the large-\(t\) region uniformly negligible, while continuity makes every compact region away from zero have a strict gap. Thus all maximizers tend to zero, where \(\partial_{tt}F<0\) forces uniqueness. Substituting the stationary-point expansion in \(F\) gives the stated quadratic excess over \(m(b,p)\). Inserting \(b=0\) gives \(u=1/12\), \(B=-1/320\), hence \(40/3\) and \(5/9\).

**4. Rare-positive-jump limit.** Write \(L=\log(1/p)\) and \(g(t)=2(e^t-1-t)/t^2\). The opposite-jump (or Gaussian) term satisfies \(0\le (e^{-bt}-1+bt)/b^2\le t^2/2\), with the natural limiting interpretation at \(b=0\). Therefore
\[
 M(t)\le 1+p\{g(t)-1\},\qquad g(t)\ge1.
\]
For \(0<t\le1\), \(F(t)\le p(g(t)-1)/t=O(p)\). For \(1\le t\le(1-\varepsilon)L\), the same argument gives \(F(t)\le2pe^t/t^3\le2p^\varepsilon\). For \(t\ge(1-\varepsilon)L\), \(F(t)<1/t\le1/[(1-\varepsilon)L]\). Hence \(\limsup c_+L\le1\) by letting \(\varepsilon\downarrow0\). Conversely take \(t=L+3\log L\). Its positive-jump contribution makes \(M(t)\ge 2p(e^t-1-t)/t^2\sim2L\), so \(F(t)\sim1/t\sim1/L\) and \(\liminf c_+L\ge1\). This proves the limit.

## Verification

The companion `verify.py` independently evaluates the Poisson/Gaussian cumulant generating functions at high precision; checks exact rational coefficient domination in local regimes through degree 60; verifies local and interior regimes across twenty-one parameter examples; and compares critical optimizer locations and excess-scale coefficients against the analytical asymptotics at ten near-critical settings. It reports 1,680 exact coefficient checks, 21 phase examples, and 10 near-critical comparisons. These are finite checks, not an infinite proof. The proof's global claims rest on the coefficient ratio inequality, compactness, and the analytic implicit-function argument above.

## Relationship to prior work

Chen and Wang (2026, arXiv:2609.02590v1), Sections 2–3 and 6–7, already establish the signed variational formula, **the equal-amplitude case \(b=1\)** with boundary \((2+\sqrt3)/4\), and its rare-positive-jump asymptotics. These are used as background rather than asserted original. The present new contribution is the **unequal-amplitude continuum \(0<b<1\), the Gaussian-smoothing endpoint \(b=0\), an explicit boundary surface, and a sharp quadratic onset law**. The two earlier general theorems imply a variational optimization problem but do not state the resulting unequal-jump classification or critical expansion. Chen (2026, arXiv:2610.00032v1) treats spectrally positive laws, which encompass the Gaussian-smoothed endpoint through their general transform but do not explicitly determine its \(3/4\) transition or quadratic expansion. Leskelä and Välimaa (2025/2026, arXiv:2508.12103) optimize a **sub-Poisson variance proxy**, not the variance-fixed sub-gamma pole.

## Limitations

This result is for one positive unit jump and one nonpositive jump size \(-b\) with \(0\le b<1\), fixed total variance one, and the **right** tail. No globally unique interior maximizing argument is asserted away from a neighborhood of the transition. The \(b=1\) endpoint is previously known. The formula does not characterize arbitrary jump laws, optimize both variance proxy and scale jointly, or determine exact rare-jump second-order asymptotics. The general variational formula is established prior art. Although full texts of the principal relevant sources were compared, the possibility of an implicit equivalent special-case theorem in broader concentration literature remains open; independent validation has not been performed.

## References

1. Y. Chen and X. Wang, *Directional Optimal Sub-Gamma Scales for Infinitely Divisible Laws*, arXiv:2609.02590v1 (first public September 2, 2026), especially Sections 3, 6, and 7; https://arxiv.org/html/2609.02590v1.
2. Y. Chen, *Optimal Sub-Gamma Scales for Spectrally Positive Infinitely Divisible Laws*, arXiv:2610.00032v1 (first public September 2, 2026); https://arxiv.org/html/2610.00032v1.
3. L. Leskelä and I. Välimaa, *Sub-Poisson distributions: Concentration inequalities, optimal variance proxies, and closure properties*, arXiv:2508.12103 (first public August 16, 2025); https://arxiv.org/abs/2508.12103.
