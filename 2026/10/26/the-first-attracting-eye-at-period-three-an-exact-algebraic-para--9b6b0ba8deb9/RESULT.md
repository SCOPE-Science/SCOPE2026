# The first attracting eye at period three: an exact algebraic parameter band

## Finding
Consider the piecewise-linear perturbation of the doubling map described below. A regular attracting periodic orbit belonging to an *eye* (an attracting component whose slope itinerary contains at least two right-branch visits) has primitive period at least three, and this lower bound is attained. Indeed, the primitive itinerary \(+--\) occurs on a nonempty explicitly characterized open two-parameter region. On the natural lift with successive integer carries \((0,1,2)\), this entire region is exactly
\[
 b_0<b<b_*,\qquad L(b)<a<U(b),
\]
where \(b_0\in(0,1)\) is the unique solution of \(8(1+b_0)(1-b_0)^2=1\),
\[
 b_* = \frac{\sqrt{21}-1}{4},\quad
 L(b)=\frac{(1+b)(4b^2-10b+9)}{2(7+2b-4b^2)},\quad
 U(b)=\frac{4+3b-2b^2-4b^3}{2(7-2b-4b^2)}.
\]
The interval width has the exact factorization
\[
 U(b)-L(b)=\frac{(5-2b-4b^2)\bigl(1-8(1+b)(1-b)^2\bigr)}{2(7+2b-4b^2)(7-2b-4b^2)}.
\]
These two heights are sharp for this *specified lift*: below \(b_0\) its periodic orbit cannot strictly attract, while at or above \(b_*\) it cannot have the stated strict branch itinerary. The result does not claim that every period-three eye belongs to this lift.

An exact interior example is \(a=10/19\), \(b=3/4\), with the primitive attracting cycle
\[
\frac9{76}\longmapsto\frac{43}{76}\longmapsto\frac{71}{76}\longmapsto\frac9{76},
\qquad (f_{a,b}^3)'=\frac78.
\]
Because two of the three points lie in the contracting right branch, the nonempty hyperbolic component containing this example is an eye by the previously established itinerary criterion.

## Assumptions and scope
For \(0\le a,b\le1\), identify the circle with \([0,1)\) and define
\[
 f_{a,b}(x)=\begin{cases}
 (2(1+b)x+a-b/2)\bmod1,&0\le x<1/2,\\
 (2(1-b)x+a+3b/2)\bmod1,&1/2\le x<1.
 \end{cases}
\]
The map is continuous on the circle. A regular cycle avoids the branch boundaries \(0\) and \(1/2\). Denote an interior left-branch visit by \(+\) and an interior right-branch visit by \(-\). The branch *carry code* \((0,1,2)\) means that the three displayed affine expressions, starting at the unique \(+\) point, have respectively the integers \(0,1,2\) subtracted to obtain their fractional parts. “Attracting” here means a strict absolute period multiplier below one, which yields local exponential attraction at a regular orbit. “Eye” follows the source's definition and its established theorem that non-single-minus attracting cycles lie in an eye rather than a tongue.

## Proof
Put \(u=2(1+b)\), \(t=2(1-b)\) and \(p=ut^2=8(1+b)(1-b)^2\). A regular orbit of itinerary \(+--\) and carry code \((0,1,2)\), written as \(x_0,x_1,x_2\), must satisfy
\[
 x_1=ux_0+a-b/2,\quad
 x_2=tx_1+a+3b/2-1,\quad
 x_0=tx_2+a+3b/2-2.
\]
For \(p\ne1\), these equations have exactly one solution:
\[
 x_0=\frac{t^2(a-b/2)+t(a+3b/2-1)+(a+3b/2-2)}{1-p},
\]
with the other coordinates given by the first two equations. Its period multiplier is \(p\). Differentiating \(p\) gives \(p'(b)=-8(1-b)(1+3b)<0\) for \(0<b<1\), while \(p(0)=8\) and \(p(1)=0\). Thus strict attraction forces \(b>b_0\), where \(b_0\) is the unique root described above.

For \(b>b_0\), each solved coordinate is a strictly increasing affine function of \(a\). Solving \(x_1=1/2\) yields \(a=L(b)\), and solving \(x_2=1\) yields \(a=U(b)\). Consequently the necessary inequalities \(x_1>1/2\) and \(x_2<1\) are equivalent to \(L(b)<a<U(b)\). The displayed factorization of \(U-L\) shows that this interval is nonempty precisely for \(b_0<b<b_*\), where \(4b_*^2+2b_*-5=0\).

It remains to check the other four strict branch inequalities rather than infer them from the two just used. At \(a=L\) and \(a=U\), direct substitution gives
\[
 x_0(L)=\frac{-4b^2+6b-1}{2(7+2b-4b^2)}>0,\qquad
 x_2(L)-\frac12=\frac{2b+1}{7+2b-4b^2}>0,
\]
\[
 x_0(U)=\frac{2(1-b)}{7-2b-4b^2}<\frac12,\qquad
 x_1(U)=1-\frac1{7-2b-4b^2}<1.
\]
All denominators are positive and the inequalities hold throughout \(b_0<b<b_*\), which lies inside \((7/10,9/10)\). Monotonicity in \(a\) therefore gives \(0<x_0<1/2<x_1<1\) and \(1/2<x_2<1\) for every \(L<a<U\). In particular each carry remains the prescribed integer, so the point is genuinely periodic under the circle map and is strictly attracting. The itinerary \(+--\) has primitive length three, hence the cycle cannot have a shorter period. The explicit rational example follows by direct substitution into the original map.

Finally, no attracting eye can have primitive period one, because an eye requires at least two minus visits. An attracting period-two eye would have itinerary \(--\). If \(t\ge1\), its period multiplier \(t^2\ge1\), so it cannot strictly attract. If \(0\le t<1\), write the two right-branch points as \(x,y\in(1/2,1)\) and their integer carries as \(k,\ell\). Subtracting their two orbit equations gives \((1+t)(y-x)=\ell-k\in\mathbb Z\). But \(|(1+t)(y-x)|<1\), because \(|y-x|<1/2\). Hence \(x=y\), contradicting primitive period two. This proves the sharp global minimum of three.

## Verification
`verify_period_three_eye.py` is a standalone Python 3 program using only the standard-library `fractions.Fraction` type. It evaluates the cycle and multiplier at exact rational parameters, verifies the representative \((9,43,71)/76\) cycle exactly, checks the factored interval width, tests interior cycles and their integer carries at six rational heights, and probes branch-collision equalities at three heights. Its completed execution reported 231 successful exact rational assertions. These finite checks are supplementary; the universal parameter-window theorem and the period floor are proved by the algebra above.

## Relationship to prior work
Bhattacharyya and Banerjee, *On the Piecewise Linear Perturbations of the Doubling Map* (arXiv:2510.11441v1, publicly posted 13 October 2025), define eyes and prove that a **nonempty** attracting component with more than one minus visit is an eye (Theorem 2.5). Their Section 4.1 constructs a period-three **tongue** with one minus visit, not a \(+--\) eye; Section 7 illustrates period-five eyes numerically. The present calculation supplies the missing short-period existence witness, sharp minimal-period conclusion, and a full rational-inequality description for a concrete period-three lift. The source's conditional eye theorem is used only to identify the type of the newly constructed component, not to infer its existence.

## Limitations
The parameter inequalities classify only the regular period-three orbit with the **specified** lift carries \((0,1,2)\); they are not a global census of all period-three components or carry codes. At boundary parameters a periodic point may hit a branch boundary, and the strict regular attractor assertion does not extend there. Generic priority under other piecewise-affine-circle-map terminology cannot be absolutely excluded by bibliographic search. No assertion is made about period-four or longer eye realization questions, arbitrary smooth circle maps, or independent review.

## References
- A. Bhattacharyya and K. Banerjee, *On the Piecewise Linear Perturbations of the Doubling Map*, arXiv:2510.11441v1 (2025-10-13), https://arxiv.org/html/2510.11441v1 , especially Sections 2, 4.1, 5, 7 and 8.
