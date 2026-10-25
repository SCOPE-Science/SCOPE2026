# A universal crossing law for random chords of rectangles

## Finding

Let \(a,b>0\), set \(K=[-a,a]\times[-b,b]\), and independently choose \(X,Y\) from the normalized arclength measure on \(\partial K\). Define the **central penetration gauge** of the random chord by
\[
T=\min_{0\le s\le1}\max\left\{\frac{|(1-s)X_1+sY_1|}{a},\frac{|(1-s)X_2+sY_2|}{b}\right\}.
\]
Equivalently, \(T\) is the smallest homothety factor \(t\in[0,1]\) for which the chord intersects \(tK\). Put
\[
p=\frac{a^2+b^2}{2(a+b)^2},\qquad
A(t)=\frac{t(3-t)}{1+t},\qquad
B(t)=t-\frac{(1-t)^2}{2}\log\frac{1+t}{1-t}.
\]
For every \(0<t<1\), the **entire distribution** is
\[
\boxed{\Pr(T\le t)=pA(t)+(1-2p)B(t).}
\]
There is an atom \(\Pr(T=1)=p\), and there are no other atoms. The inverse of this atom identifies the aspect ratio \(r=\max(a,b)/\min(a,b)\):
\[
\boxed{r=\frac{2p+\sqrt{4p-1}}{1-2p}}\qquad (1/4\le p<1/2).
\]
More unexpectedly, the continuous distribution functions for **all rectangle aspect ratios** share one and only one crossing at \(t_*\in(0,1)\), the unique solution of
\[
2B(t_*)=A(t_*),\qquad t_*=0.5604879233027861179\ldots.
\]
At that factor their common probability is
\[
\boxed{\Pr(T\le t_*)=B(t_*)=0.4381056198263137408\ldots.}
\]
If \(r_2>r_1\ge1\), then \(F_{r_2}(t)>F_{r_1}(t)\) for \(0<t<t_*\), while \(F_{r_2}(t)<F_{r_1}(t)\) for \(t_*<t<1\). In particular, there is no first-order stochastic ordering by aspect ratio.

## Assumptions and scope

The endpoints are independent, sampled *with replacement* from normalized **Euclidean perimeter arclength**. They are not selected by motion-invariant random lines, uniform chord directions, or area-uniform interior points. The rectangle is nondegenerate and centrally placed; scaling it or exchanging its axes does not change the law. The gauge is defined on the **whole closed segment** between the sampled endpoints. Endpoint coincidences and vertices are probability-zero events. At \(t=0\), \(F(0)=0\); at \(t=1\), \(F(1)=1\), including the stated jump. The parameter \(p\) lies in \([1/4,1/2)\); the limiting value \(1/2\) corresponds only to a degenerating rectangle, not a positive-area one.

## Proof

**Reduction and side-pair probabilities.** The diagonal affine map \((x,y)\mapsto(x/a,y/b)\) takes \(K\) to \(Q=[-1,1]^2\), takes \(tK\) to \(tQ\), and preserves uniform *conditional* arclength on each individual side. A point falls on either horizontal side with individual probability \(a/[2(a+b)]\), and either vertical side with individual probability \(b/[2(a+b)]\). Two independently sampled points lie on the same side with probability
\[
2\left(\frac{a}{2(a+b)}\right)^2+2\left(\frac{b}{2(a+b)}\right)^2=p.
\]
The event of lying on distinct opposite sides has the same probability \(p\), and the remaining adjacent-side event has probability \(1-2p\). Same-side segments remain on \(\partial Q\), and so have penetration gauge exactly \(1\). In the other two cases the gauge is less than \(1\) almost surely.

**Opposite-side kernel.** Take the normalized endpoints \((-1,u),(1,v)\), where \(u,v\) are independent uniform variables on \([-1,1]\). The segment at abscissa \(x\in[-1,1]\) has ordinate
\[
y(x)=\frac{u+v}{2}+x\frac{v-u}{2}.
\]
For \(0<t<1\), it misses the centered square \(tQ\) precisely if \(y(x)>t\) throughout \([-t,t]\), or if \(y(x)<-t\) throughout that interval. Set \(s=(u+v)/2\) and \(d=(u-v)/2\). The joint density of \((s,d)\) is \(1/2\) on the diamond \(|s|+|d|\le1\). The upper miss condition is \(s>t+t|d|\). Integrating over the diamond yields
\[
\Pr(\text{upper miss})=
\int_0^{(1-t)/(1+t)} [1-t-(1+t)d] \,\mathrm d d
=\frac{(1-t)^2}{2(1+t)}.
\]
The lower miss has the same probability, so the conditional hit probability is
\[
1-\frac{(1-t)^2}{1+t}=\frac{t(3-t)}{1+t}=A(t).
\]

**Adjacent-side kernel.** Take normalized endpoints \((u,1),(1,v)\). Their supporting line is
\[
(1-v)x+(1-u)y=1-uv.
\]
Because \(1-u\ge0\), \(1-v\ge0\), the line meets \(tQ\) exactly when \(1-uv\le t(2-u-v)\); the intersection on the line lies in the endpoint segment because \(tQ\subset Q\), and the line meets \(Q\) in precisely that segment (outside zero-measure boundary coincidences). Put \(U=1-u,V=1-v\), independent uniform on \([0,2]\), and \(c=1-t\). The inequality is \(UV/(U+V)\ge c\), requiring \(U\ge 2c/(2-c)\) and then \(V\ge cU/(U-c)\). Consequently the conditional hit probability is the normalized area
\[
\begin{aligned}
\frac14\int_{2c/(2-c)}^2\left(2-\frac{cU}{U-c}\right)\mathrm dU
&=1-c-\frac{c^2}{2}\log\frac{2-c}{c}\\
&=t-\frac{(1-t)^2}{2}\log\frac{1+t}{1-t}=B(t).
\end{aligned}
\]
Combining the three side-pair cases proves the distribution and the atom.

**The crossing, uniqueness, and inversion.** Define \(h(t)=2B(t)-A(t)\). Direct differentiation, with limits taken from inside \((0,1)\), gives
\[
h'''(t)=-\frac{8(5-t)}{(1-t)(1+t)^4}<0,
\]
\[
h(0)=0,\quad h(1^-)=1,\quad h'(0^+)=-3,\quad h'(1^-)=2,
\quad h''(0^+)=16,\quad h''(1^-)=-\infty.
\]
Thus \(h''\) is strictly decreasing, changes sign exactly once, and \(h'\) first increases and then decreases. Since \(h'(0^+)<0<h'(1^-)\), it vanishes exactly once; \(h\) first strictly decreases below zero, then strictly increases until it reaches \(1\). Hence it crosses zero exactly once in \((0,1)\). The value is characterized by \(2B(t_*)=A(t_*)\), or equivalently
\[
\frac{t_*(3t_*-1)}{1+t_*}=(1-t_*)^2\log\frac{1+t_*}{1-t_*}.
\]
The root and common probability quoted above are evaluations of these formulas. Since
\[
F_p(t)=pA(t)+(1-2p)B(t)=B(t)-p h(t),
\]
all aspect ratios cross at \(t_*\), and increasing \(p\) reverses CDF ordering there. Finally, writing \(r=a/b\ge1\) gives \(p=(r^2+1)/[2(r+1)^2]\), strictly increasing from \(1/4\) to \(1/2\). Solving that quadratic gives the stated positive-root inverse. These identities prove every assertion.

## Verification

The companion standard-library program `verify.py` tests the exact formulas against direct simulation of independent perimeter-uniform endpoints and an independent piecewise-linear minimum calculation for the penetration gauge. It also checks the universal crossing equation, the inverse aspect-ratio formula, and aspect-ratio independence at the crossing. Run `python verify.py`; its successful terminal line includes `RECTANGLE_PENETRATION_CHECKS_OK`. The finite numerical tests supplement the analytic argument; they do not certify the infinite family or priority.

## Relationship to prior work

Bäsel's regular-polygon chord paper [1] treats **motion-invariant random lines**, and the distribution of distances between **interior area-uniform points**, rather than the distribution of the minimum \(K\)-gauge along a chord whose endpoints are arclength-uniform on a rectangle boundary. Harutyunyan and Ohanyan [2] likewise use invariant random lines with both offset and direction randomized to study regular-polygon chord lengths. Their line models do not imply the present independent-perimeter-endpoint law. The published fourth-chord-moment comparison for parallelograms [3] does sample perimeter-uniform point pairs, but concerns the fourth moment of their **Euclidean endpoint distance**, not central penetration, the atom, or the common crossing. The published central-chord law for regular polygons [4] imposes a line through the center with uniform angular direction and studies chord length, a distinct geometric experiment. Neither work gives the claimed homothetic-intersection distribution, its aspect-ratio inversion, or its one-crossing theorem.

## Limitations

The law uses rectangles, a centered homothetic target, the normalized coordinate \(\ell_\infty\) gauge, and independent perimeter-uniform endpoint sampling. It does not describe Euclidean closest-point distance, arbitrary convex quadrilaterals, arbitrary sampling densities, or translation-invariant random lines. Its universal crossing holds among positive-area rectangles only and is unique **in the interior** \(0<t<1\); all distributions also share the trivial boundary value \(F(0)=0\). The literature comparison is not a claim that no unindexed, differently phrased, or inaccessible historical result exists. No independent scientific audit has been performed.

## References

[1] Uwe Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707, first publicly posted 2012-04-12. https://arxiv.org/abs/1204.2707.

[2] H. S. Harutyunyan and V. K. Ohanyan, *The chord length distribution function for regular polygons*, Advances in Applied Probability 41 (2009), 358–366. https://doi.org/10.1239/aap/1246886615.

[3] *Fourth-chord moment amplification and angular phase transition for parallelograms*, published mathematical research record. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-fourth-chord-moment-amplification-and-angular-phase-transition-f--45b0568cfb6e.

[4] *Parity-resolved central-chord laws for regular polygons*, published mathematical research record. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-parity-resolved-central-chord-laws-for-regular-polygons--de9bb055a653.
