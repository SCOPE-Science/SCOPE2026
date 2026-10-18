# Exact Lipschitz distance to strong minimum-attainment on an interval

## Finding

Let \(f\in\operatorname{Lip}_0([0,1];\mathbb R)\) be strictly increasing, with \(0<a:=\operatorname*{ess\,inf}_{t\in(0,1)} f'(t)\) and \(b:=\operatorname*{ess\,sup}_{t\in(0,1)}f'(t)<\infty\). Define the **smallest local upper slope**
\[
 h(f)=\inf_{0<u<v<1}\operatorname*{ess\,sup}_{t\in(u,v)}f'(t),\qquad a\le h(f)\le b.
\]
For any Lipschitz map \(g\), write
\[
 m(g)=\inf_{0\le u<v\le1}\frac{|g(v)-g(u)|}{v-u}.
\]
Let \(\mathcal S\) consist of the real-valued Lipschitz maps \(g\), normalized by \(g(0)=0\), for which some distinct \(u,v\) attain \(m(g)\). Let \(\mathcal S_{\mathrm{inj}}\) consist of the *injective* members of \(\mathcal S\). In the Lipschitz norm \(\|g\|_{\mathrm{Lip}}=\sup_{u<v}|g(v)-g(u)|/(v-u)\), the **exact distances** are
\[
 \boxed{\operatorname{dist}_{\mathrm{Lip}}(f,\mathcal S_{\mathrm{inj}})=\frac{h(f)-a}{2}},
 \qquad
 \boxed{\operatorname{dist}_{\mathrm{Lip}}(f,\mathcal S)=\min\!\left\{a,\frac{h(f)-a}{2}\right\}}.
\]
These are infima; minimizers need not exist.

For an explicit attainment transition, let \(F\subset[0,1]\) be any closed nowhere-dense set of positive Lebesgue measure, put \(U=[0,1]\setminus F\), and fix \(0<a<b\). Define
\[
 f_{a,b}(t)=at+(b-a)\int_0^t\mathbf{1}_U(s)\,ds.
\]
Then
\[
 \operatorname{dist}_{\mathrm{Lip}}(f_{a,b},\mathcal S)
 =\min\!\left\{a,\frac{b-a}{2}\right\}.
\]
Moreover **a nearest strongly minimum-attaining map exists if and only if \(b\le3a\)**. For \(b\le3a\), the affine map \(g(t)=(a+b)t/2\) is a minimizer. For \(b>3a\), the distance equals \(a\) but is not attained.

## Assumptions and scope

All maps are real-valued and defined on the *whole* Euclidean interval \([0,1]\), with basepoint \(0\). Differentiation is the almost-everywhere derivative of absolutely continuous Lipschitz functions. Essential bounds use Lebesgue measure. Only \(a>0\) and finite Lipschitz norm are assumed; \(f'\) need not be continuous, and \(f\) need not attain its lower secant slope. The set \(F\) in the example may be a Smith–Volterra (fat Cantor) set. Distances are measured in the Lipschitz seminorm, which is a norm after basepoint normalization.

## Proof

**Lemma (slopes and attained minima).** For every absolutely continuous increasing \(g\) with derivative bounded below by a strictly positive number, 
\[
 m(g)=\operatorname*{ess\,inf}g'.
\]
Indeed, the integral-average formula proves the lower bound, and the Lebesgue differentiation theorem gives arbitrarily short secant quotients converging to \(g'(t)\) at almost every differentiability point. Further, if \(m(g)\) is attained on \([u,v]\), then \(g'=m(g)\) almost everywhere on that interval, since the nonnegative function \(g'-m(g)\) integrates there to zero. The same conclusion holds for a strictly decreasing \(g\) after replacing it by \(-g\).

**Lower bound for the injective class.** Let \(g\in\mathcal S_{\mathrm{inj}}\) and \(\delta=\|f-g\|_{\mathrm{Lip}}\). If \(g\) is decreasing, then \(\delta\ge b\), because \(f'\ge a>0\) and \(g'\le0\) almost everywhere; this already dominates \((h(f)-a)/2\). Otherwise \(g\) is strictly increasing. Since it attains its minimum at two *distinct* points, injectivity forces \(m(g)>0\). The secant lower bound then implies \(g'\ge m(g)\) almost everywhere; the lemma applies. From \(\|g'-f'\|_{L^\infty}\le\delta\) we get \(m(g)\le a+\delta\). On an interval \(I\) attaining \(m(g)\), its derivative equals \(m(g)\) almost everywhere. Hence
\[
 h(f)\le \operatorname*{ess\,sup}_{I} f'\le m(g)+\delta\le a+2\delta.
\]
Thus \(\delta\ge(h(f)-a)/2\). (If \(I\) touches an endpoint, replace it by an interior subinterval.)

**Matching injective construction.** For any \(\delta>(h(f)-a)/2\), choose a nonempty open interval \(I\subset(0,1)\) with \(\operatorname*{ess\,sup}_{I}f'<a+2\delta\). Set \(c=a+\delta\) and prescribe
\[
 g'(t)=\begin{cases}c,&t\in I,\\ \max\{f'(t),c\},&t\notin I,\end{cases}\qquad g(0)=0.
\]
Then \(g'\ge c>0\), \(\|f'-g'\|_{L^\infty}\le\delta\), and \(m(g)=c\) is attained on every subinterval of \(I\). Therefore \(g\in\mathcal S_{\mathrm{inj}}\), proving the first distance formula.

**Lower bound for the unrestricted class.** If \(\delta<\min\{a,(h(f)-a)/2\}\) and \(\|g-f\|_{\mathrm{Lip}}\le\delta\), then \(g'\ge a-\delta>0\) almost everywhere. Thus \(g\) is injective; by the preceding lower bound it cannot lie in \(\mathcal S\).

**Matching noninjective construction.** Only the case \(a<(h(f)-a)/2\) remains. Then \(b\ge h(f)>3a\). For every sufficiently small \(\varepsilon>0\), choose \(c\in(a,a+\varepsilon)\) with \(c<b\) and set \(g(t)=f(t)-ct\). The sets where \(g'<0\) and where \(g'>0\) each have positive measure: this follows respectively from the definition of \(a\) and from \(c<b\). A continuous injective real map on an interval must be strictly monotone; the signs of \(g'\) exclude both monotonicities. Hence \(g\) takes the same value at two distinct points, \(m(g)=0\) is attained, and \(\|g-f\|_{\mathrm{Lip}}=c<a+\varepsilon\). This proves the unrestricted formula.

**Sharp two-phase attainment transition.** For the specified \(F\), positivity of its measure gives \(\operatorname*{ess\,inf}f'_{a,b}=a\). Every nonempty open interval meets the dense open \(U\) in a nonempty open subinterval, so its essential supremum equals \(b\): thus \(h(f_{a,b})=b\). The distance formula follows. For \(b\le3a\), the stated affine \(g\) has derivative \((a+b)/2\), differs in essential-supremum slope by exactly \((b-a)/2\), and belongs to \(\mathcal S\).

If \(b>3a\) and \(\|g-f_{a,b}\|_{\mathrm{Lip}}\le a\), then \(g'\ge0\) almost everywhere and on the dense open set \(U\) one has \(g'\ge b-a>2a\). Thus \(g\) is strictly increasing (every nonempty interval contains a nonempty subinterval of \(U\)) and is injective. Meanwhile \(m(g)\le2a\) by Lebesgue differentiation on the positive-measure set \(F\), where \(g'\le2a\) almost everywhere. If this minimum were attained on some interval, \(g'\) would equal \(m(g)\le2a\) almost everywhere there, contradicting the portion of \(U\) where \(g'>2a\). Hence no nearest member of \(\mathcal S\) exists in this regime.

## Verification

The proof uses only the fundamental theorem of calculus for absolutely continuous functions, essential bounds, the Lebesgue differentiation theorem, and the elementary fact that a continuous injective map of an interval is monotone. The lower bound is independent of the upper-bound constructions; the first uses an attained-derivative plateau, and the second uses loss of injectivity. For the two-speed example, the transition is determined by the exact comparison \((b-a)/2\le a\iff b\le3a\). No finite enumeration, extrapolation, or external numerical certificate enters the proof.

## Relationship to prior work

Geunsu Choi's 2026 preprint *A bi-Lipschitz characterization of strong minimum-attainment for Lipschitz maps* establishes a qualitative density/non-density criterion for scalar Lipschitz functions on complete metric spaces. That result motivates examining exact *distances of individual functions* to the strong-minimum-attainment set. The classification in that preprint's available abstract does not specify the derivative-envelope formula or the attained/unattained two-speed transition. Its complete proof and appendices could not be inspected here, so no whole-paper absence claim is made; priority relative to any unpublished quantitative lemma remains unresolved.

## Limitations

The formulas are for scalar real Lipschitz maps on a single Euclidean interval, with a strictly positive lower slope, not for arbitrary metric domains or vector-valued maps. The smallest local upper slope is an essential supremum over **every** nonempty interval; replacing it by a pointwise maximum or by the global upper slope changes the general theorem. The theorem gives distances as infima: except for the specified two-speed family it does not classify best-approximation existence. The source preprint's complete text was inaccessible, leaving a specific comparison risk.

## References

1. Geunsu Choi, *A bi-Lipschitz characterization of strong minimum-attainment for Lipschitz maps*, arXiv:2609.11080, first posted 2026-09-10, https://arxiv.org/abs/2609.11080.
2. Lebesgue differentiation theorem and the fundamental theorem of calculus for absolutely continuous functions (classical results; used with their standard statements).
