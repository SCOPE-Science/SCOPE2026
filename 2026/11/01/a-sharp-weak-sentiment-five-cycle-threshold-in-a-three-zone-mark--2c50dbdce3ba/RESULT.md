# A sharp weak-sentiment five-cycle threshold in a three-zone market map

## Finding

Consider the stock-market piecewise-affine map of Gardini, Radi, Schmitt, Sushko and Westerhoff, with the neutral branch closed at both switching thresholds. On the zero-trace slice \(c=1+b\), an open weak-sentiment region \(0<d<h\) contains two attracting primitive five-cycles simultaneously with an attracting equilibrium. At the exact slice \(b=1/4\), \(c=5/4\), there are precisely two primitive five-cycles for \(205/252<d/h<1\), none for \(0<d/h\le205/252\), and there are no primitive cycles of periods two, three or four anywhere on that weak-sentiment slice. Thus \(205/252\) is the exact first period-five threshold for this slice, with the boundary excluded because its grazing point belongs to the neutral branch.

An explicit open family of coexisting attracting cycles is also available. Let \(b_*\in(0,1)\) be the unique root of \(b+2b^3=1\). For \(0<b<b_*\), put
\[
Q=1-b+b^2-b^3+b^4,\qquad Z=\max\{b(1+b^2),\,|1-b-b^3|\}.
\]
If
\[
\frac{Q}{1-b^3}<\frac dh<\min\left\{1,\frac QZ\right\},
\]
then \(F\) has two distinct, locally attracting least-period-five orbits with code sequences \(UUOLO\) and \(LLOUO\) (upper, lower and neutral branches are denoted \(U,L,O\) in the reference), as well as an attracting fixed point at the origin. This interval is nonempty for every \(0<b<b_*\).

## Assumptions and scope

All parameters are real, \(h,d>0\), \(0<b<1\), and \(c=1+b\). The map is defined on the **entire real plane** by
\[
F_{b,d,h}(x,y)=\bigl(-b y+d\,\sigma_h(x-y),\ x\bigr),\qquad
\sigma_h(u)=\begin{cases}1&u>h,\\0&-h\le u\le h,\\-1&u<-h.\end{cases}
\]
Thus \(L\) means \(x-y>h\) and forcing \(+d\); \(U\) means \(x-y<-h\) and forcing \(-d\). Both equalities are assigned to \(O\). The interpretation of an orbit as attracting is local: an open neighborhood of its points follows the same strict branches and converges to the orbit. No claim is made about cycles of period at least six, nonperiodic attractors, or global basin volumes.

## Proof

**1. Periodic affine responses.** Write \(z_i=x_i/d\) and \(s_i=\sigma_h(x_i-x_{i-1})\in\{-1,0,1\}\). Any \(n\)-cycle satisfies
\[
z_{i+1}=-b z_{i-1}+s_i,\qquad i\pmod n.
\]
Set \(L=n/\gcd(n,2)\). Iterating backwards by two indices exactly \(L\) times yields the *unique* affine response to any prescribed symbol word:
\[
\boxed{z_i=\frac{\displaystyle\sum_{k=0}^{L-1}(-b)^k s_{i-1-2k}}{1-(-b)^L}.}
\]
Because \(0<b<1\), the denominator cannot vanish. Put \(u_i=z_i-z_{i-1}\) and \(r=d/h>0\). Such a word corresponds to an actual trajectory exactly when \(s_i u_i>0\) at all active positions, and
\[
\frac1H<r\le\frac1Z,
\quad H=\min_{s_i\ne0}|u_i|,\quad
Z=\max_{s_i=0}|u_i|,
\]
where the upper bound is omitted if there is no neutral position. A word with an active symbol and \(H\le Z\) is impossible. The all-neutral word gives only \(z_i=0\). These inequalities follow from the strict active threshold \(|d u_i|>h\) and the inclusive neutral threshold \(|d u_i|\le h\); hence the criterion treats every boundary exactly.

**2. An open period-five family.** For \(s=(-1,-1,0,+1,0)\), direct substitution into the formula in part 1 gives \(z_i=q_i\), \(0\le i<5\), with
\[
(q_0,q_1,q_2,q_3,q_4)=\frac{1}{1+b^5}\bigl(-b^2(1+b+b^2),\,-(1+b+b^2),\,b^4+b^3-1,\,b(1+b+b^2),\,1+b-b^4\bigr).
\]
The normalized consecutive differences are
\[
(q_i-q_{i-1})_{i=0}^4=
\frac{1}{Q}\bigl(-(1+b^2),\,-(1-b^3),\,b(1+b^2),\,1+b^2-b^3,\,1-b-b^3\bigr).
\]
For \(0<b<b_*\), the active coordinates \(i=0,1,3\) have their prescribed signs and smallest absolute value \(H=(1-b^3)/Q\); at the other two indices the maximal absolute difference is \(Z/Q\). Thus the stated inequalities ensure this word, and odd symmetry gives its negative word \((+1,+1,0,-1,0)\), giving the second orbit. The two orbits are distinct: one has two strict upper-branch visits while the other has two strict lower-branch visits; cyclic rotation preserves those visit counts. Their least period is five because the symbol word is nonconstant and five is prime.

The interval is nonempty: \(Q<1-b^3\) follows from \(b+b^3<1\), and \(Z<1-b^3\) follows from \(b+2b^3<1\), which holds for \(b<b_*\). In particular \(Q/(1-b^3)<\min\{1,Q/Z\}\).

The branchwise Jacobian is constant,
\[
J=\begin{pmatrix}0&-b\\1&0\end{pmatrix},\quad J^2=-bI.
\]
The eigenvalues of the five-step derivative \(J^5\) are \(\pm i b^{5/2}\), of modulus strictly smaller than one. Because all three active and two neutral inequalities were made strict, the local five-step itinerary is persistent; this proves both cycles locally attracting. The origin lies in the neutral strip and obeys the contracting local linear map \(J\); hence it is simultaneously attracting.

**3. Exact primitive-period census on a rational slice.** Fix \(b=1/4\), \(c=5/4\), and retain \(0<r=d/h<1\). The affine-response formula of part 1 is an exact finite decision procedure for any \(n\), using rational arithmetic. For \(n=1,2,3,4,5\), enumerate all \(3^n\) ternary words, discard the all-neutral word (whose unique response is zero), calculate the response and the signed threshold range, and identify cyclically rotated words. This is **358 nonzero words** total. The complete certificate of *all nonempty intervals of positive \(r\)* is

| Length \(n\) | Canonical word | Exact admissible interval \(r=d/h\) |
|---|---|---|
| \(1,2,3,4\) | none | none |
| \(5\) | \((-1,-1,0,1,0)\) | \((205/252,205/188]\) |
| \(5\) | \((-1,0,1,1,0)\) | \((205/252,205/188]\) |
| \(5\) | \((-1,-1,0,1,1)\) | \((41/16,41/4]\) |
| \(5\) | \((-1,-1,1,1,0)\) | \((41/16,41/4]\) |

Each row is a distinct orbit up to time translation. The complete enumeration and exact-rational inequalities can be replayed from `check_period_five.py`, included with this result; there is no numerical tolerance, grid extrapolation or search-time cutoff. The first two rows are negatives of one another up to rotation, and the last two rows occur only at \(r>1\). Since \(0<r<1\), precisely the first two are admissible when \(205/252<r<1\), and none otherwise. In particular there are no primitive orbits of periods two through four, and the origin is the only fixed point. The five-cycle coordinates in the first row are explicitly
\[
(x_0,x_1,x_2,x_3,x_4)=\frac{d}{1025}(-84,-1344,-1004,336,1276),
\]
with points \((x_i,x_{i-1})\), indices interpreted modulo five. Their differences are
\[
(x_i-x_{i-1})_{i=0}^4=\frac d{205}(-272,-252,68,268,188).
\]
The first two differences are below \(-h\) exactly for \(r>205/252\); the fourth is above \(h\), and the remaining two lie inside \([-h,h]\) whenever \(r<1\). At \(r=205/252\), the second difference is exactly \(-h\), so the postulated active symbol is replaced by the neutral symbol: the open lower endpoint is essential. The other orbit is its negative.

This finite-census proof is complete for lengths at most five because every periodic orbit supplies a word, and the unique affine response associated with that word is tested. It asserts nothing about lengths six or greater.

## Verification

Run `python3 check_period_five.py` in a standard Python 3 installation. The script enumerates every nonzero word in lengths one to five over \(\{-1,0,1\}\), computes the exact admissible parameter intervals using `fractions.Fraction`, checks the four-row complete table and the sharp grazing boundary, and independently evaluates the two physical-map five-cycles for three rational weak-sentiment gains. It additionally checks the parametric five-cycle construction for six distinct rational values of \(b\). Only integer/rational comparisons are used. The universal parameter-family proof is algebraic; the exact finite certificate resolves only the stated length-five census on the rational slice.

## Relationship to prior work

The defining 2023 three-zone stock-market article introduces the affine branches and studies overlapping periodicity regions, primarily for the opposite regime \(d>h\). Its explicit cycle families, including the reported five-cycles \(L^2OU^2\) and \(U^2OL^2\), are different from the present two-neutral-visit words \(LLOUO\) and \(UUOLO\). The article explicitly identifies \(0<d<h\) as a direction for further investigation. The subsequent related 2024/2025 study of stock-market dynamics uses an equivalent class after a forcing-parameter rescaling, but its proofs and numerical cycle surveys do not establish this weak-forcing period-five onset or complete short-period census. The earlier two-zone model lacks the neutral strip and cannot directly supply this classification.

The new result is therefore a specific exact weak-forcing boundary and short-period classification, not a claim to invent the original model, period-adding structures, or the general method of periodic-word enumeration.

## Limitations

The open-family claim is sufficient, not a complete phase diagram across all \(b\). The **complete** five-period and shorter-period census is asserted only at \(b=1/4\), \(c=5/4\), \(0<d<h\), with the stated threshold conventions. No statement is made about longer cycles, invariant strange attractors, or basin proportions. Locally attracting does not imply global attraction. The originality comparison is based on inspected published literature and available indexed records; earlier unindexed analyses could overlap. An independent mathematical audit has not been performed.

## References

1. L. Gardini, D. Radi, N. Schmitt, I. Sushko and F. Westerhoff, “A 2D piecewise-linear discontinuous map arising in stock market modeling: Two overlapping period-adding bifurcation structures,” *Chaos, Solitons & Fractals* 176 (2023), 114143. DOI: `10.1016/j.chaos.2023.114143`. Available online 12 October 2023. Sections 2, 3, 4 and concluding remarks.
2. L. Gardini, D. Radi, N. Schmitt, I. Sushko and F. Westerhoff, “On boom-bust stock market dynamics, animal spirits, and the destabilizing nature of temporarily attracting virtual fixed points,” *Macroeconomic Dynamics* 29 (2025), e35, first published online 26 September 2024. DOI: `10.1017/S1365100524000439`. Sections 2–3 and Appendix A.
3. D. Radi et al., “Perception of fundamental values and financial market dynamics: Mathematical insights from a 2D piecewise linear map,” *SIAM Journal on Applied Dynamical Systems* 21 (2022), 2314–2337. DOI: `10.1137/21M1456339`. A prior two-branch context, not a source of the present three-zone theorem.
