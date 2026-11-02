# Sharp entropy collapse and a full-measure attracting basin in a modified tent map

## Finding

For \(1<t<2\), \(0<s<1\), \(ts<1\), and \(0<p<1\), consider the Type-1 two-slope tent composition \(T_{t,s,p}=g_{s,p}\circ f_t\) defined below. Put
\[
p_c=\frac{t-1}{1+ts-2s},\qquad R(p)=\frac{t(1-sp)}{1-p},\qquad p_* =\frac{2-t}{2-ts}.
\]
Then the **complete topological-entropy law** is
\[
h_{\mathrm{top}}(T_{t,s,p})=
\begin{cases}
\log\min\{R(p),2\},&0<p<p_c,\\
0,&p_c\le p<1.
\end{cases}
\]
The entropy collapses discontinuously at \(p=p_c\): its left limit is \(\log\min\{2,t/(2-t)\}>0\), while the value at the boundary is zero. When \(t>4/3\), the full-entropy plateau \(h_{\mathrm{top}}=\log2\) occupies the nonempty interval \(p_*\le p<p_c\); when \(t=4/3\), \(p_*=p_c\) and no positive-length plateau occurs; when \(t<4/3\), \(p_*>p_c\) and the entropy on \(p<p_c\) is \(\log R(p)\).

Furthermore, for \(0<p<p_c\), set
\[
a=\frac{p(1-s)}{t(1-sp)-(1-p)},\qquad I=[a,1-a].
\]
If \(R\le2\), \(I\) is forward invariant and its two-branch constant-slope subsystem has entropy \(\log R\); the attracting fixed point \(0\) has a basin of Lebesgue measure exactly \(2a\). If \(R>2\), the nonescaping set \(K=\bigcap_{n\ge0}T^{-n}(I)\cap I\) is a two-branch affine Cantor repeller, conjugate to the full one-sided two-symbol shift, with
\[
\dim_{\mathrm H}K=\frac{\log2}{\log R},\qquad
\operatorname{Leb}\{x\in I:T^j(x)\in I\ (0\le j\le n)\}
=(1-2a)\left(\frac2R\right)^n\quad(n\ge0).
\]
Thus \(0\) attracts Lebesgue-almost every initial point for \(R>2\), even though \(h_{\mathrm{top}}=\log2\). For uniform initial data in \(I\), the first exit time \(\tau=\min\{n\ge1:T^n(x)\notin I\}\) has \(\mathbb P(\tau>n)=(2/R)^n\) for \(n\ge0\), and expectation \(\mathbb E\tau=R/(R-2)\). At \(p\ge p_c\) the entropy is zero, and all points other than possible nonzero fixed boundary points tend to zero.

## Assumptions and scope

All parameters are real, with \(1<t<2\), \(0<s<1\), \(ts<1\), and \(p\in(0,1)\). The domain is the compact interval \([0,1]\). The underlying maps, with matching endpoint values on their breakpoints, are
\[
f_t(x)=t\min\{x,1-x\},\qquad
g_{s,p}(y)=
\begin{cases}
sy,&0\le y\le p,\\
\dfrac{1-sp}{1-p}y-\dfrac{p(1-s)}{1-p},&p\le y\le1.
\end{cases}
\]
Topological entropy is for \(T_{t,s,p}\) on all of \([0,1]\), not entropy conditioned on an invariant probability. Lebesgue basin means the set \(\{x:T^n(x)\to0\}\). The Cantor and first-exit statements require the *strict* inequality \(R>2\), equivalent here to \(t>4/3\) and \(p_*<p<p_c\). At \(R=2\), the core \(I\) remains invariant and is not Lebesgue-null. The exact geometric survivor formula is stated for nonnegative integers \(n\).

## Proof

**1. Parameter geometry.** Since \(ts<1\), direct rearrangement gives \(0<p_c<t/2<1\); the denominator \(1+ts-2s=1-s(2-t)\) is positive. For \(p<t/2\), define
\[
k=\frac{p(1-s)}{1-p},\qquad R=\frac{t(1-sp)}{1-p}.
\]
On \([p/t,1-p/t]\) the graph is the symmetric tent \(T(x)=R\min\{x,1-x\}-k\), and on the outer pieces its slopes are \(\pm ts\). Since \(R>t>1\) for \(s<1\) and \(p>0\), the rising central branch has exactly one fixed point \(a=k/(R-1)\). Moreover,
\[
a-\frac pt=\frac{p(1-ts)}{t(R-1)}>0,\qquad
T(1/2)-1/2=\frac{(t-1)-p(1+ts-2s)}{2(1-p)}.
\]
Thus \(a<1/2\) exactly when \(p<p_c\), and then \(I=[a,1-a]\) sits wholly inside the two central branches. For \(p\ge t/2\), the entire map has tent slopes \(\pm ts\), so its height is at most \(ts/2<1/2\). Between \(p_c\) and \(t/2\), the displayed height identity already gives \(T(1/2)\le1/2\). Consequently for **every** \(p\ge p_c\), the interval \([0,1/2]\) is forward invariant and \(T\) is increasing there, so \(h_{\mathrm{top}}(T)=0\). The latter reduction follows because every orbit enters that invariant monotone interval after one step, and a continuous monotone interval map has zero entropy. At \(p=p_c\), \(T(1/2)=1/2\), so the conclusion includes equality.

**2. Positive-entropy core.** Fix \(0<p<p_c\). The exact identities
\[
T(a)=T(1-a)=a,\quad T(1/2)=a+R(1/2-a),
\quad T(x)<x\ (0<x<a),\quad T(x)<a\ (1-a<x\le1)
\]
show that every point outside \(I\) tends to \(0\): points to the left decrease to the sole fixed point \(0\), while points to the right enter the left component in one step. Since \(T\) is increasing on \([0,a]\), no outside orbit returns to \(I\). The entropy outside \(I\) is therefore zero, and the entropy of the full map equals that of its maximal invariant subset inside \(I\), by the standard wandering-interval reduction (or directly by separated-set growth after the at-most-one excursion from \(I\)). The core is the exact symmetric two-slope map \(T(x)=R\min\{x,1-x\}-k\).

If \(1<R\le2\), the height satisfies \(T(1/2)\le1-a\), so \(I\) is forward invariant and its restriction has constant slopes \(\pm R\). The classical constant-slope entropy formula yields \(h_{\mathrm{top}}=\log R\). Since no orbit from \(I\) can tend to zero, and every point outside \(I\) does, the basin of zero has Lebesgue measure \(2a\), including the case \(R=2\).

If \(R>2\), the height exceeds \(1-a\). The two affine inverse branches from \(I\) into \(I\) are
\[
\ell(y)=\frac{y+k}{R},\qquad r(y)=1-\frac{y+k}{R}\quad(y\in I).
\]
They have disjoint images (strictly separated by the central escaping interval), so every binary sequence specifies one and only one point of \(K\); this is a topological conjugacy with the full one-sided two-symbol shift. Hence \(h_{\mathrm{top}}(T)\ge\log2\). Since \(T\) is unimodal on \([0,1]\), its iterates have at most \(2^n\) laps, giving the opposite entropy bound. The open-set condition for these two similarities yields \(\dim_{\mathrm H}K=\log2/\log R\). At depth \(n\), the survivor set in \(I\) is the disjoint union of \(2^n\) affine cylinder intervals, each with length \((1-2a)R^{-n}\). This proves the displayed survivor and geometric exit laws. As \(2/R<1\), \(K\) has zero Lebesgue measure and all remaining points tend to zero.

**3. Exact thresholds.** Since \(R(p)\) is strictly increasing in \(p\), the equation \(R=2\) has unique solution \(p_*=(2-t)/(2-ts)\). The exact comparison
\[
p_c-p_*=\frac{(1-s)(3t-4)}{(2-ts)(1+ts-2s)}
\]
shows when the full-entropy plateau is nonempty. Substituting \(p_c\) gives \(R(p_c)=t/(2-t)\), so the left entropy limit is \(\log\min\{2,t/(2-t)\}>0\), whereas the value at \(p_c\) is zero. This completes the proof of the discontinuity and phase diagram.

For example, at \(t=9/5\) and \(s=1/2\), the exact thresholds are \(p_*=2/11\), \(p_c=8/9\), the effective slope is \(R=9(2-p)/(10(1-p))\), and \(a=5p/(8+p)\). The entropy is \(\log[9(2-p)/(10(1-p))]\) for \(p<2/11\), \(\log2\) for \(2/11\le p<8/9\), and zero for \(p\ge8/9\).

## Verification

The supplied standalone `check_entropy.py` evaluates exact symbolic parameter identities, evaluates several rational examples in both regimes, constructs hundreds of exact-rational inverse-cylinder intervals in two supercritical examples, verifies that their endpoints map to the invariant core boundary after the indicated number of iterates, and checks their exact total lengths against the geometric law. It was executed successfully before this report. These finite checks do not establish universal entropy, Hausdorff dimension, or infinite-time statements; those follow from the proof above and the cited classical constant-slope, symbolic-shift, and similarity-dimension results. The checker can be run using Python 3 and SymPy.

## Relationship to prior work

Cánovas (2021), *Parrondo's Paradox for Tent Maps*, introduces exactly this family in Section 2, establishes its elementary monotonicity/zero-entropy cases (including the equality \(T(1/2)=1/2\)), and explores the nontrivial Type-1 parameter region through kneading-sequence numerics (Figures 1–2). Its Section 3 says that the relevant analytical parameter boundaries are not yet clear. The formula, jump at \(p_c\), full-entropy plateau, exact attracting-basin measure, similarity dimension, and geometric escape law above do not occur in the examined article. The established constant-slope entropy theorem is invoked rather than claimed as new. Alsedà, Misiurewicz and Pérez (2020) investigate piecewise expanding skew tent maps, generally without the contracting fixed-point basin and collapsing invariant core present here. Botella-Soler and collaborators studied entropy plateaus in a distinct discontinuous two-branch map, defined by their 2012 preprint Equation (5); its Section 4 theorems concern that different family, not this continuous four-segment composition. Search of a mathematical findings index with source-title, parameter, entropy, Cantor-repeller and escape-law formulations did not return an equivalent statement. This is evidence of non-overlap in inspected materials, not a proof of priority.

## Limitations

The classification is only for \(1<t<2\), \(0<s<1\), \(ts<1\), and \(0<p<1\); it does not classify Type-2 homeomorphisms \(s>1\), noncontracting origins, or all parameter faces. The scalar entropy result is topological and coexists with physical convergence to zero; it does not imply positive metric entropy for Lebesgue-typical initial conditions. The topological conjugacy on \(K\) holds when \(R>2\), not at the transition \(R=2\). Publication-priority searches are inherently incomplete; independent validation and external mathematical audit have not been performed.

## References

1. J. S. Cánovas, *Parrondo's Paradox for Tent Maps*, **Axioms** 10(2), article 85 (2021), DOI: `10.3390/axioms10020085`; https://doi.org/10.3390/axioms10020085 . First published 6 May 2021.
2. L. Alsedà, M. Misiurewicz, and R. A. Pérez, *Flexibility of Entropies for Piecewise Expanding Unimodal Maps* (2020), arXiv:`2004.01813`; https://arxiv.org/abs/2004.01813 . General comparison for skew tent maps, not a prior derivation of the presented phase law.
3. V. Botella-Soler, J. A. Oteo, J. Ros, and P. Glendinning, *Families of piecewise linear maps with constant Lyapunov exponent* (2012), arXiv:`1205.5360`, https://arxiv.org/abs/1205.5360 ; related 2013 article *Lyapunov exponent and topological entropy plateaus in piecewise linear maps*, DOI:`10.1088/1751-8113/46/12/125101` (a different discontinuous two-branch map family).
4. Classical interval-map results on lap numbers, entropy of piecewise constant-slope maps, and Hausdorff dimension of affine self-similar Cantor sets (used in their standard forms; no novelty claimed for these results).
