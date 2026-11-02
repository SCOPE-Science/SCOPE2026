# Six exact eight-step return phases for floor-discretized 45-degree rotation

## Finding
For the digital rotation \(R:\mathbb Z^2\to\mathbb Z^2\),
\[
R(x,y)=\left(\left\lfloor\frac{x-y}{\sqrt2}\right\rfloor,\left\lfloor\frac{x+y}{\sqrt2}\right\rfloor\right),
\]
let \(a\ge2\) be an integer, \(w=\lfloor a/\sqrt2\rfloor\), and \(t=\{a/\sqrt2\}\). Put
\[
 b_1=\frac{\sqrt2-1}{2},\quad b_2=1-\frac1{\sqrt2},\quad
 b_3=\sqrt2-1,\quad b_4=\frac12,\quad b_5=\sqrt2-\frac12.
\]
These five breakpoints are strictly ordered in \((0,1)\). The **complete eight-step displacement law on the positive horizontal axis** is

| Fractional-part range | \(R^8(a,0)-(a,0)\) |
| --- | --- |
| \(0<t<b_1\) | \((0,-1)\) |
| \(b_1<t<b_2\) | \((-1,0)\) |
| \(b_2<t\le b_3\) | \((0,0)\) |
| \(b_3<t<b_4\) | \((1,-1)\) |
| \(b_4<t<b_5\) | \((-1,-1)\) |
| \(b_5<t<1\) | \((-2,0)\) |

Among positive integers, only \(a=2\) can attain any listed breakpoint, and it attains \(b_3\). Hence a positive-axis point \((a,0)\), \(a\ge2\), has **least period eight if and only if**
\[
 1-\frac1{\sqrt2}<\left\{\frac{a}{\sqrt2}\right\}\le \sqrt2-1.
\]
The set of such integers has natural density
\[
\boxed{\quad\frac3{\sqrt2}-2\quad}\simeq0.12132034356.
\]
Each selected positive-axis seed belongs to a different eight-cycle. The excluded seed \((1,0)\) maps to \((0,0)\), and \((0,0)\) is fixed.

In particular, \(a=5\), \(w=3\) obeys the fractional-part and second-iterate assumptions of Theorem 5.2 in Hannusch--Pethő (2021/2022), but \(R^8(5,0)=(4,-1)\ne(5,0)\). Thus the sufficient range printed there is not valid in full; the sharper condition above gives the exact axial classification.

## Assumptions and scope
The map is coordinatewise **floor** of an ordinary counterclockwise \(\pi/4\) rotation; it is neither coordinatewise nearest-integer rounding nor the companion-matrix discretization. All statements concern integer initial coordinates \((a,0)\) with \(a\ge2\), except the explicitly handled cases \(a=0,1\). The density is with respect to \(a\in\{1,\ldots,N\}\) as \(N\to\infty\). No claim is made about points off this half-axis.

## Proof
Write \(a/\sqrt2=w+t\) with integer \(w\ge1\) and \(0<t<1\). The endpoints \(t=0\) and \(t=1/\sqrt2\) cannot occur for \(a\ge2\). Indeed \(a/\sqrt2=w+1/\sqrt2\) forces \(a=1\); the equality \(t=0\) forces \(a=0\). Directly,
\[
R(a,0)=(w,w),\qquad
R^2(a,0)=\begin{cases}(0,a-1),&t<1/\sqrt2,\\(0,a-2),&t>1/\sqrt2,\end{cases}
\qquad R^3(a,0)=(-w,w-1).
\]
The last equality follows in both branches by applying the floor to \(\pm(a-k)/\sqrt2\), \(k=1,2\). Consequently
\[
 R^4(a,0)=\bigl(-a+\lfloor\sqrt2\,t+1/\sqrt2\rfloor,-1\bigr).
\]
The first coordinate is \(-a\), \(-a+1\), or \(-a+2\) as \(t\) traverses the intervals separated by \(b_1\) and \(b_5\). In the next calculation it is necessary also to split at \(1/\sqrt2\), although the final displacement does not change there.

The following direct floor table lists **all four subsequent states**, with \(R^j\) evaluated at \((a,0)\). The seven rows partition the entire accessible range; \(b_3\) is handled in the third row by the explicit \(a=2\) calculation below.

| \(t\) range | \(R^5\) | \(R^6\) | \(R^7\) | \(R^8\) |
| --- | --- | --- | --- | --- |
| \((0,b_1)\) | \((-w,-w-1)\) | \((0,-a-1)\) | \((w,-w-1)\) | \((a,-1)\) |
| \((b_1,b_2)\) | \((-w+1,-w-1)\) | \((1,-a)\) | \((w,-w)\) | \((a-1,0)\) |
| \((b_2,b_3)\) | \((-w+1,-w-1)\) | \((1,-a)\) | \((w+1,-w)\) | \((a,0)\) |
| \((b_3,b_4)\) | \((-w,-w-1)\) | \((0,-a-1)\) | \((w+1,-w-2)\) | \((a+1,-1)\) |
| \((b_4,1/\sqrt2)\) | \((-w,-w-1)\) | \((0,-a)\) | \((w,-w-1)\) | \((a-1,-1)\) |
| \((1/\sqrt2,b_5)\) | \((-w,-w-1)\) | \((0,-a)\) | \((w,-w-1)\) | \((a-1,-1)\) |
| \((b_5,1)\) | \((-w+1,-w-1)\) | \((1,-a+1)\) | \((w,-w)\) | \((a-2,0)\) |

To verify each cell without approximation, for any integers \(m,n,c\) with even \(n\) use the identity
\[
\left\lfloor\frac{ma+nw+c}{\sqrt2}\right\rfloor
 =\frac n2 a+mw+\left\lfloor\left(m-\frac n{\sqrt2}\right)t+\frac c{\sqrt2}\right\rfloor.
\]
Every intermediate coordinate in the table is an integer linear combination of \(a,w,1\); the relevant coefficient \(n\) is even each time a floor is taken. The affine expression inside the final floor is bounded between two consecutive integers throughout each stated open interval, as verified by substituting its two algebraic endpoints. This establishes each line for every real \(t\) in its interval, not just numerical samples. The accompanying independent arithmetic program repeats all seven interval checks using exact rational arithmetic in \(\mathbb Q(\sqrt2)\).

No \(a\ge2\) attains \(b_1,b_2,b_4,b_5\): substituting \(a/\sqrt2=w+b_j\) in each case would equate a nonzero rational multiple of \(\sqrt2\) to a rational. Similarly, \(t=b_3\) forces \((a,w)=(2,1)\). Direct iteration gives
\[
 (2,0)\to(1,1)\to(0,1)\to(-1,0)\to(-1,-1)
 \to(0,-2)\to(1,-2)\to(2,-1)\to(2,0),
\]
so the endpoint is included. The displayed table now proves the six-phase law.

For every returning seed, \(R^2(a,0)\ne(a,0)\) because its first coordinate vanishes, and \(R^4(a,0)\ne(a,0)\) because its second coordinate is \(-1\). Hence an eight-step return has least period eight. On those cycles, phases \(1,\ldots,7\) never lie on the positive horizontal axis, as the table and the first four states show. Different seeds therefore give different cycles.

Finally, \(a/\sqrt2\) is uniformly distributed modulo \(1\) as \(a\) runs through the positive integers. The finite exceptional endpoint set has zero density, so the sharp period-eight interval has density \(b_3-b_2=3/\sqrt2-2\).

## Verification
Run `python3 verify.py` with Python 3 and no nonstandard packages. It constructs exact \(\mathbb Q(\sqrt2)\) arithmetic, checks that every affine floor expression has a constant integer part throughout each of the seven full open intervals, and verifies the claimed symbolic eight-step displacement. The checker additionally compares \(19,999\) positive integer seeds \(2\le a\le20,000\) using integer square-root flooring and checks the endpoint seed \(a=2\). The analytical case split and equidistribution prove the infinite statements independently of this finite enumeration.

## Relationship to prior work
Hannusch and Pethő (arXiv:2109.01828v1, September 4, 2021; journal DOI below) introduce this precise map. Their Theorem 5.2 proposes a sufficient fractional-part interval for eight-step returns, while Remark 5.3 notes that only a class of such points is supplied. For the same hypotheses, \(a=5\) is a direct counterexample; the exact return table and necessary-and-sufficient condition above repair and sharpen this specific local claim. Their much broader results concerning noninjectivity and nonsurjectivity are unaffected by the statement proved here. Akiyama and Pethő study the **different** companion-matrix map \((x,y)\mapsto(y,-\lfloor x+\lambda y\rfloor)\); its real-linear resemblance to rotations does not identify this coordinatewise-floor lattice map or imply the present return table.

## Limitations
This is a half-axis classification for a fixed angle and floor convention, not a global periodicity theorem and not an orbit count over the entire lattice. Period-eight density concerns positive integer axis seeds only. Prior-art checking covered directly relevant sources and published mathematical records, but not every possible unindexed note; independent audit remains unperformed.

## References
1. C. Hannusch and A. Pethő, *Rotation on the digital plane*, arXiv:2109.01828v1 (first public September 4, 2021), especially §5, Theorem 5.2, Lemma 5.1 and Remark 5.3. https://arxiv.org/abs/2109.01828
2. C. Hannusch and A. Pethő, *Rotation on the digital plane*, *Periodica Mathematica Hungarica* 86 (2023), 564–577, first published online July 16, 2022. https://doi.org/10.1007/s10998-022-00480-8
3. S. Akiyama and A. Pethő, *Discretized rotation has infinitely many periodic orbits*, arXiv:1206.3868 (2012), *Nonlinearity* 26 (2013), 871–880. https://arxiv.org/abs/1206.3868
