# Complete period-four orbit census in the orientation-preserving Lozi family

## Finding
Consider the plane homeomorphism
\[
L_{a,b}(x,y)=(-a|x|-by+a-b-1,\,x),\qquad 0<b<1,\quad a>1+b.
\]
The map is orientation-preserving: on either smooth half-plane its Jacobian determinant is \(b>0\). Let \(N_4(a,b)\) be the number of distinct orbits of *least* period four, counting four iterates of one orbit only once. Write
\[
P(a,b)=a^3+a^2b-a^2+ab^2-a-b^3+b^2+b-1.
\]
Then the exact global census is
\[
N_4(a,b)=\begin{cases}1,&P(a,b)<0,\\2,&P(a,b)=0,\\3,&P(a,b)>0.\end{cases}
\]
The always-present orbit has cyclic sign word \(+++-\). The other two sign words are \(++--\) and \(+---\), and each occurs when \(P>0\). At \(P=0\) the latter two descriptions coalesce into one orbit with exactly one zero first-coordinate entry. No other least-period-four orbits exist. For \(P\ne0\) every such orbit is a hyperbolic saddle.

The transition is sharp. For each \(0<b<\sqrt2-1\), there is exactly one number \(a_4(b)>1+b\) with \(P(a_4(b),b)=0\); the number of orbits changes from one to two to three when \(a\) passes through this boundary. For \(\sqrt2-1\le b<1\), the count is three for every \(a>1+b\).

## Assumptions and scope
All coordinates and parameters are real. The parameter domain is *exactly* \(0<b<1\), \(a>1+b\); nothing is asserted on its excluded boundary or elsewhere. A period-four cycle is an orbit with least positive return time four under the displayed map, not merely a solution of its fourth iterate. A symbol \(+\) (respectively \(-\)) means strictly positive (respectively strictly negative) first coordinate. At a zero coordinate both adjacent branch formulas agree, so either sign may be assigned for itinerary enumeration.

Put \(t=a-b-1>0\). Since the second coordinate is always the preceding first coordinate, a period-four orbit with first coordinates \(x_0,x_1,x_2,x_3\) satisfies, for all \(i\) modulo four,
\[
x_{i+1}=-a|x_i|-b x_{i-1}+t.
\]

## Proof
**1. Exhaustion by cyclic binary words.** The six binary words of length four up to cyclic rotation are \(++++\), \(----\), \(+-+-\), \(+++-\), \(++--\) and \(+---\). On each assigned sign branch the displayed recurrence is a linear four-by-four system, whose solution is unique on our domain. The constant words lead to fixed points, while \(+-+-\) leads to a two-cycle. Thus only the three primitive words need be examined. This also covers any orbit touching the switching line, because one may assign either sign to each zero and the affine branches agree there.

**2. Exact solutions and signs.** Set
\[
\begin{aligned}
D&=a^4+(1-b^2)^2,\\
E&=(a^2-b^2+1)(a^2+b^2-1),\\
V&=a^3+a^2b-a^2-ab^2+a+b^3-b^2-b+1,\\
U&=a^3-a^2b+a^2+ab^2-a+b^3-b^2-b+1,\\
R&=a^3-a^2b+a^2-ab^2+a-b^3+b^2+b-1.
\end{aligned}
\]
Both denominators are strictly positive on the stated domain. Direct solution of the three linear systems, in itinerary order, gives
\[
\begin{aligned}
(+++ -):\quad &(x_0,x_1,x_2,x_3)
 =\frac{t}{D}\bigl(V,\,t(a-b+1)(a+b-1),\,U,\,-t[a^2+(b-1)^2]\bigr),\\
(++--):\quad &(x_0,x_1,x_2,x_3)
 =\frac{t}{E}(P,R,-U,-V),\\
(+---):\quad &(x_0,x_1,x_2,x_3)
 =\frac{t}{D}\bigl((a+b+1)[a^2+(b-1)^2],\,-R,\,-(a-b+1)(a+b-1)(a+b+1),\,-P\bigr).
\end{aligned}
\]
Here the spaced symbol \((+++ -)\) denotes the word \(+++-\). To verify every expression, substitute it into \(x_{i+1}+a\sigma_i x_i+b x_{i-1}=t\), with \(\sigma_i=1\) for \(+\) and \(-1\) for \(-\); all four identities hold exactly.

The three auxiliary numerators are strictly positive. In terms of \(t>0\) and \(0<b<1\),
\[
\begin{aligned}
V&=t^3+(4b+2)t^2+(4b^2+6b+2)t+2(b^3+b^2+b+1),\\
U&=t^3+(2b+4)t^2+(2b^2+6b+4)t+2(b^3+b^2+b+1),\\
R&=t^3+(2b+4)t^2+(6b+6)t+2(1+3b+b^2-b^3).
\end{aligned}
\]
Thus the \(+++-\) candidate has the required strict signs everywhere. The \(++--\) candidate has the required signs if and only if \(P\ge0\), with equality allowed at its first coordinate; the \(+---\) candidate has them if and only if \(P\ge0\), with equality at its last coordinate. When \(P>0\) these two orbits are distinct because their primitive sign words are not cyclic permutations. When \(P=0\), both candidate solutions describe one and the same orbit: shift \((+---)\) to place its zero at the beginning; it then has signs \((0,+,-,-)\), exactly as \((++--)\), and uniqueness of the branchwise linear solution identifies them. Strictness of all remaining entries gives least period four even at the collision. There are no further cycles by Step 1.

**3. Exact parameter boundary.** Expanding \(P\) in \(t=a-b-1\) yields
\[
P=t^3+(4b+2)t^2+(6b^2+6b)t+2(b+1)(b^2+2b-1).
\]
Its derivative with respect to \(t\) is strictly positive for every \(t>0\). At \(t=0\) its sign is the sign of \(b^2+2b-1\). Since \(P\) tends to positive infinity as \(t\) grows, this proves the unique interior threshold for \(b<\sqrt2-1\) and the three-cycle regime for \(b\ge\sqrt2-1\), including the equality case with \(t>0\).

**4. Hyperbolic type away from collision.** At a strictly signed point the Jacobian matrices are \(J_+=\begin{pmatrix}-a&-b\\1&0\end{pmatrix}\), \(J_-=\begin{pmatrix}a&-b\\1&0\end{pmatrix}\). Their fourfold products have determinant \(b^4\). The traces are \(-a^4+2b^2\) for \(+++-\) and \(+---\), and \(a^4+2b^2\) for \(++--\). Since \(a>1+b\) implies \(a^4>(1+b)^4>(1+b^2)^2\), one has \(-a^4+2b^2<-(1+b^4)\) and \(a^4+2b^2>1+b^4\). The characteristic roots therefore straddle the unit circle: every strictly signed four-cycle is a hyperbolic saddle. No differentiability or hyperbolicity is claimed at the switching-line collision.

## Verification
The standalone `lozi_period4_checker.py` checks each displayed orbit formula against all four recurrence equations as polynomial identities, checks the sign-controlling expansions and the multiplier traces exactly using SymPy, and tests representative rational parameter pairs. This is an algebraic checker, not a numerical search for every real parameter. The proof of completeness and parameter-wide inequalities is given above and does not depend on finite tests. Run `python lozi_period4_checker.py` with Python 3 and SymPy installed.

## Relationship to prior work
Lozi introduced the piecewise-affine map in 1978. In their 2022/2023 study of the *orientation-preserving* normalization used here, Boroński, Kucharski and Ou established periodic points for least periods one, two, three and all periods exceeding thirteen on a smaller region, without asserting this exact four-cycle census. Ou's paper on creation curves develops itinerary uniqueness and border-collision methods for this map; the present finite exact global enumeration of period four specializes those tools into a sharp result, rather than claiming symbolic dynamics or generic border-collision theory as new. Botella-Soler and collaborators' 2011 period-four continua occur at a different degeneracy in the conventional sign convention and are not a classification of these isolated four-cycles. Hansen's thesis displays period-four symbolic bifurcation diagrams in a different parameter region. Sushko, Avrutin and Gardini focus on center-bifurcation and stable rotation-region boundaries rather than a complete census in the hyperbolic region \(a>1+b\).

For comparison with the conventional map \(u_{n+1}=1-a|u_n|+\beta u_{n-1}\), scale \(x_n=t u_n\); its parameter is \(\beta=-b\), so the present regime corresponds to negative conventional \(\beta\), not positive \(\beta\). Qualitative or theorem-title matches without this sign and exact parameter transformation do not establish coverage.

## Limitations
The result is restricted to the specified two-parameter hyperbolic half-strip and to least period four. It makes no claims about orbit counts of higher periods, measure-theoretic dynamics, or attractor geometry. The source literature includes broad itinerary theorems, so the novelty claim is the *explicit complete count and exact border curve in this domain*, not the elementary principle of coding. Complete text of the relevant 2021 and 2023 center-bifurcation articles was not available; their abstracts and accessible previews describe a different focus/center regime, but historical priority cannot be ruled out absolutely. For the 1978 original, the publication month is verified as August 1978; an indexing service reports the first day of that month.

## References
1. R. Lozi, *Un attracteur étrange (?) du type attracteur de Hénon*, J. Phys. Colloques 39 (1978), C5-9–C5-10. DOI: 10.1051/jphyscol:1978505.
2. J. P. Boroński, P. Kucharski and D.-S. Ou, *Lozi maps with periodic points of all periods n > 13* (2022 preprint; public manuscript https://www.researchgate.net/publication/366740872_Lozi_maps_with_periodic_points_of_all_periods_n_13).
3. D.-S. Ou, *Critical points in higher dimensions, I: Reverse order of periodic orbit creations in the Lozi family*, arXiv:2203.02326 (2022), https://arxiv.org/pdf/2203.02326.
4. V. Botella-Soler, J. M. Castelo, J. A. Oteo and J. Ros, *Bifurcations in the Lozi map*, J. Phys. A 44 (2011), 305101, arXiv:1102.0034.
5. K. T. Hansen, *Pruned Horseshoes*, Chapter 4, Fig. 4.30, https://chaosbook.org/projects/KTHansen/thesis/chap_4.pdf.
6. I. Sushko, V. Avrutin and L. Gardini, *Center Bifurcation in the Lozi Map*, Int. J. Bifurc. Chaos 31 (2021), 2130046, DOI: 10.1142/S0218127421300469.
7. I. Sushko, V. Avrutin and L. Gardini, *Lozi map embedded into the 2D border collision normal form*, J. Difference Equ. Appl. 29 (2023), 965–981, DOI: 10.1080/10236198.2023.2205960.
