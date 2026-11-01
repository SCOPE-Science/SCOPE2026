# Sharp two-branch Hilbert profile for asymmetric linear skew constants

## Finding
Let \(H\) be a real Hilbert space with \(\dim H\geq2\), fix \(0<a<1\), and put \(\delta=|2a-1|\). Define the weighted skew geometric constant
\[
\mathcal C_{a,p}(H)=\sup_{\substack{u,v\in H,\ \|u\|=\|v\|=1\\ r,s\geq0,\ \|(r,s)\|_{\ell_p^2}=1}}\bigl(a\|ru+sv\|+(1-a)\|su-rv\|\bigr),\qquad 1\leq p\leq\infty.
\]
Then its full asymmetric-weight, exponent-dependent profile is
\[
\boxed{\mathcal C_{a,p}(H)=
\begin{cases}
1,&p=1,\\
(1+\delta^{p/(p-1)})^{(p-1)/p},&1<p\leq2,\\
2^{1/2-1/p}\sqrt{1+\delta^2},&2\leq p\leq\infty.
\end{cases}}
\]
The two branches agree at \(p=2\), where both equal \(\sqrt{1+\delta^2}\). Every supremum is attained; all maximizing coefficient ratios and pairwise angles are classified below. Moreover the exponent \(p=2\) is a strict corner: with \(h(t)=-t\log t-(1-t)\log(1-t)\) and \(0\log0=0\),
\[
\frac{d}{dp^-}\log\mathcal C_{a,p}(H)\bigg|_{p=2}=\frac14h\!\left(\frac{\delta^2}{1+\delta^2}\right)
<\frac{\log2}{4}=
\frac{d}{dp^+}\log\mathcal C_{a,p}(H)\bigg|_{p=2}.
\]
The strict inequality holds for every \(0<a<1\), including the balanced weight \(a=1/2\).

## Assumptions and scope
The scalar field is real, \(\dim H\geq2\), \(a\in(0,1)\), and \(p\in[1,\infty]\). For finite \(p\), \(\|(r,s)\|_{\ell_p^2}=(r^p+s^p)^{1/p}\); for \(p=\infty\) it is \(\max(r,s)\). The definition uses nonnegative \(r,s\) and unit vectors \(u,v\). The normalization of the positive linear weight \(\lambda_a(x,y)=ax+(1-a)y\) is \(\lambda_a(1,1)=1\). This is the skew pair \((ru+sv,su-rv)\), not the distinct symmetric pair \((ru+sv,ru-sv)\).

All maximizers are as follows, allowing simultaneous exchange of \((r,u)\) with \((s,v)\) and arbitrary Hilbert-space isometries. Set \(\varepsilon=\operatorname{sgn}(2a-1)\) when \(\delta>0\).

* If \(p=1\), exactly one of \(r,s\) equals \(1\) and the other equals \(0\); the two unit vectors may be arbitrary.
* If \(1<p<2\) and \(\delta>0\), the ratio of the smaller positive coefficient to the larger is \(\delta^{1/(p-1)}\), and \(\langle u,v\rangle=\varepsilon\). If \(1<p<2\) and \(\delta=0\), precisely one coefficient is nonzero; the unit vectors are arbitrary.
* If \(p=2\) and \(\delta>0\), the coefficients are both positive, and for \(t=\min(r,s)/\max(r,s)\) they obey \(\delta\leq t\leq1\); their inner product is
\[
\langle u,v\rangle=\varepsilon\frac{\delta(1+t^2)}{(1+\delta^2)t}.
\]
If \(p=2\) and \(\delta=0\), either exactly one coefficient is nonzero and \(u,v\) are arbitrary, or both are positive and \(u\perp v\).
* If \(2<p\leq\infty\), the coefficients are equal, with \(r=s=2^{-1/p}\) (interpreting \(2^{-1/\infty}=1\)), and
\[
\langle u,v\rangle=\frac{2(2a-1)}{1+\delta^2}.
\]
The last inner product is strictly between \(-1\) and \(1\), so all these optimizers have oblique or orthogonal distinct directions, whereas the unequal-weight low-exponent regime forces collinearity.

## Proof
Write \(b=1-a\), \(R=r^2+s^2\), and \(c=\langle u,v\rangle\). The Hilbert identity gives
\[
\|ru+sv\|=\sqrt{R+2rsc},\qquad \|su-rv\|=\sqrt{R-2rsc}.
\]
The supremum only depends on \(a,b,p\). Reflecting \(c\) swaps \(a,b\), so without loss for the computation take \(a\geq b\) and \(\delta=a-b\in[0,1)\). We may take \(r\geq s\) because simultaneously exchanging the coefficient/vector pairs leaves both norms unchanged. Set \(t=s/r\in[0,1]\) and \(d=a^2+b^2=(1+\delta^2)/2\). The case \(r>0\) is automatic under the normalization and ordering.

**Angular optimization.** For fixed \(r,s>0\), the function of \(x=2rsc\)
\[
f(x)=a\sqrt{R+x}+b\sqrt{R-x},\qquad -2rs\leq x\leq2rs,
\]
is strictly concave; its unrestricted maximum occurs at \(x_*=\delta R/d\), where the maximum is \(\sqrt{2dR}=\sqrt{1+\delta^2}\sqrt R\). The condition \(x_*\leq2rs\) is
\[
\delta(1+t^2)\leq(1+\delta^2)t
\quad\Longleftrightarrow\quad t\geq\delta,
\]
using \(t\in[0,1]\) and \(\delta\in[0,1)\). (For \(\delta=0\), the condition holds for all positive \(t\).) Otherwise the concavity maximum is at \(x=2rs\), namely \(f=r+\delta s\). Consequently, after the \(\ell_p\) normalization, the exact maximum over all pairwise angles for fixed ratio \(t\) equals
\[
F_p(t)=
\begin{cases}
\dfrac{1+\delta t}{(1+t^p)^{1/p}},&0\leq t\leq\delta,\\[2mm]
\sqrt{1+\delta^2}\,\dfrac{\sqrt{1+t^2}}{(1+t^p)^{1/p}},&\delta\leq t\leq1,
\end{cases}
\]
with the standard interpretation of the denominator for \(p=\infty\). Both expressions agree at \(t=\delta\). For \(p=1\), the first branch strictly decreases, and the second strictly decreases on \((0,1)\); the maximum is \(F_1(0)=1\).

**The low-exponent branch.** For \(1<p<2\), differentiating the first branch shows its derivative has the sign of \(\delta-t^{p-1}\); it has a unique maximum at \(t_0=\delta^{1/(p-1)}\leq\delta\). The second branch has logarithmic derivative
\[
\frac{t}{1+t^2}-\frac{t^{p-1}}{1+t^p}
=\frac{t-t^{p-1}}{(1+t^2)(1+t^p)}<0\quad(0<t<1).
\]
Thus its maximum occurs at the first branch's endpoint, and cannot exceed the first-branch maximum at \(t_0\). Substitution gives \(F_p(t_0)=(1+\delta^{p/(p-1)})^{(p-1)/p}\). The strict inequalities give the claimed complete equality cases, including the \(\delta=0\) endpoint.

**The Hilbert and high-exponent branches.** If \(p=2\), \(\sqrt{1+t^2}/(1+t^p)^{1/p}=1\); the second branch is constant on \([\delta,1]\). The first branch increases up to \(t=\delta\). Strict angular concavity gives the stated angle, and the cases \(\delta=0\) and \(rs=0\) follow directly. If \(p>2\), the angular Cauchy inequality yields, for all admissible pairs,
\[
a\|ru+sv\|+b\|su-rv\|
\leq\sqrt{2(a^2+b^2)}\sqrt{r^2+s^2}
\leq2^{1/2-1/p}\sqrt{1+\delta^2}.
\]
Equality in the second inequality forces \(r=s=2^{-1/p}\), including \(p=\infty\); equality in the first forces \(x=x_*\). At equal coefficients this corresponds to \(c=\delta/d=2\delta/(1+\delta^2)\), which lies in \([0,1)\), and hence is realized by unit vectors in any real Hilbert space of dimension at least two. For \(a<1/2\), reverse the sign of \(c\). This proves the values and all equality conditions.

**The corner at the exponent two.** For \(1<p<2\), set \(q=p/(p-1)\). Differentiating \(q^{-1}\log(1+\delta^q)\) at \(q=2\), using \(dq/dp=-1\) there, gives the left derivative \(h(\delta^2/(1+\delta^2))/4\). When \(\delta=0\), this is the direct derivative of the constant one. For \(p>2\), differentiating \((1/2-1/p)\log2+(1/2)\log(1+\delta^2)\) gives the right derivative \(\log2/4\). Since \(\delta<1\), the argument of \(h\) lies in \([0,1/2)\) and therefore \(h<\log2\). This proves the strict corner.

## Verification
The proof is exact and uses no limiting numerical enumeration. The supplementary standard-library script `checker.py` evaluates the closed formula and explicit extremizers, compares against deterministic random admissible triples, and tests numerical one-sided derivatives near the corner. It prints `PASS: 18867 deterministic checks`; those checks are not a substitute for the analytic optimization and do not establish priority.

## Relationship to prior work
Du, Zhang, Fang, and Liu introduced the parameterized *skew* vector pair and derived general bounds and Hilbert-space formulas under a differential balance hypothesis. Their Example 4 exhibits the asymmetric linear weight and notes that a nonorthogonal maximizing angle may occur, but does not give its two-parameter exact value, all maximizing configurations, or the change at exponent two. The balanced-weight endpoint follows their standard Hilbert-space calculation.

Ni, Liu, and Zhou studied other skew geometric constants with coefficients *inside* the vector sums rather than unequal external weights. Their Hilbert-space Propositions 1 and 6 are related but do not imply the exact all-exponent profile above. The symmetric-parameter family of Amini-Harandi and Rahimi also uses a different vector pair. The new claim is the full asymmetric linear-weight profile with equality classification and strict exponent corner, not the already-known general Cauchy bound by itself.

## Limitations
Only real Hilbert spaces of dimension at least two and strictly positive external weights are treated. No claim is made for nonlinear weights, arbitrary Banach spaces, higher-arity constants, or complex scalars. The proof is self-review, not independently audited; searches do not prove absolute publication priority. The 2019 symmetric-framework primary text could not be inspected in full, leaving a limited possibility of an equivalent result expressed differently.

## References
1. Qing Du, Wenwen Zhang, Zhiyao Fang, Qi Liu, *Skew-Parameterized Geometric Constants in Banach Spaces*, arXiv:2608.00933 (public 2026-08-02), https://arxiv.org/abs/2608.00933, especially Definition 2, Theorem 14, Example 4.
2. Qichuan Ni, Qi Liu, Yin Zhou, *Some Aspects of New Skew Geometric Constants in Banach Spaces*, Mathematical Inequalities & Applications 28 (2025), 327–342, DOI:10.7153/mia-2025-28-22, https://files.ele-math.com/articles/mia-28-22.pdf, especially Propositions 1 and 6.
3. A. Amini-Harandi, M. Rahimi, *On Some Geometric Constants in Banach Spaces*, Mediterranean Journal of Mathematics 16 (2019), article 120, DOI:10.1007/s00009-019-1377-z (bibliographic record and summary only inspected).
