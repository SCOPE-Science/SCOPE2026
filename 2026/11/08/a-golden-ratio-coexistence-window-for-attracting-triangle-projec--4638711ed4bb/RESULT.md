# A golden-ratio coexistence window for attracting triangle-projection cycles

## Finding
Let \(h>0\), let \(A=(0,h)\), \(B=(-1,0)\), and \(C=(1,0)\), and write \(L_0=AB\), \(L_1=BC\), \(L_2=CA\) for the **complete supporting lines**. On their union consider Everett's farthest-orthogonal-projection map \(T_h\): at a nonvertex point on one line, project orthogonally onto each of the other two lines and choose the projection at the greater Euclidean distance; at equal distances the point is fixed. Count cycles up to cyclic rotation. Let \(N_j(h)\) denote the number of **primitive least-period \(j\)** cycles avoiding the three vertices.

Put
\[
\varphi=\frac{1+\sqrt5}{2},\qquad H=\sqrt{3+2\sqrt3}.
\]
Then the complete period-three and period-four census is
\[
\boxed{\quad N_3(h)=2\,\mathbf 1_{\{1<h<H\}},\qquad
N_4(h)=\mathbf 1_{\{0<h<\sqrt\varphi\}}.\quad}
\]
All counted cycles lie strictly in the three triangle edges and are locally attracting. In particular, exactly **three distinct locally attracting cycles of two different prime periods** coexist when
\[
\boxed{\qquad 1<h<\sqrt\varphi\qquad}
\]
(two of period three and one of period four). At the endpoints \(h=1\) and \(h=\sqrt\varphi\), the corresponding disappearing itinerary fails at a fixed-point tie; the inequalities are strict. The apex-angle form of the coexistence interval is
\[
2\arctan(1/\sqrt\varphi)<\alpha<\pi/2.
\]
No claim about primitive periods five and higher, or about global basin coverage, is made.

The unique four-cycle, when it exists, has ordered points
\[
\left(\frac{h^2}{h^2+2},0\right),\quad
\left(-\frac{h^2}{h^2+2},\frac{2h}{h^2+2}\right),\quad
\left(-\frac{h^2}{h^2+2},0\right),\quad
\left(\frac{h^2}{h^2+2},\frac{2h}{h^2+2}\right).
\]
The two three-cycles are mirror images. One, oriented from the base to the right side and then to the left side, is
\[
\left(\frac{1-h^2}{h^2+3},0\right),\quad
\left(\frac{h^2+1}{h^2+3},\frac{2h}{h^2+3}\right),\quad
\left(\frac{1-h^2}{h^2+3},\frac{4h}{h^2+3}\right).
\]
Its mirror in the vertical axis gives the other. In their respective local line coordinates the three-step and four-step multipliers are
\[
\boxed{m_3=\frac{1-h^2}{(1+h^2)^2},\qquad m_4=\frac{1}{(1+h^2)^2}.}
\]
They have modulus strictly below one whenever the corresponding cycle exists.

## Assumptions and scope
The three lines are pairwise distinct, nonparallel, and nonconcurrent, and \(h>0\) makes a nondegenerate isosceles triangle. The map uses the *whole other supporting lines*, not a clipped perpendicular foot on an edge. A point where the two possible distances agree stays fixed, as in Everett's original definition. A nonvertex periodic cycle is unambiguous because each point belongs to one line; the definition at a vertex is immaterial to this statement. The classification is exhaustive **only for primitive least periods three and four**. Multipliers refer to the affine return on the appropriate continuity interval of a line; neither multipliers nor finite symbolic tests assert a global basin decomposition.

## Proof
For a point \(z\) and line \(L_i\), let \(P_i z\) be its ordinary Euclidean orthogonal projection, and put \(d_i(z)=\|z-P_i z\|^2\). On each line, any nonfixed step changes the line label. Also, any finite composition of projections that uses at least two nonparallel lines is a strict affine contraction on the initial line, so each prescribed admissible cyclic itinerary has at most one periodic candidate. We determine the candidates by solving its scalar affine fixed-point equation and then **separately** check the farthest-choice inequalities.

**Period three.** A cyclic word of length three on three line symbols without equal adjacent symbols must use all three, in one of two orientations. For the word \(1\to2\to0\to1\), solving
\[
P_1P_0P_2(t,0)=(t,0)
\]
gives \(t=(1-h^2)/(h^2+3)\) and the displayed three points. The signed differences \(d_{\mathrm{next}}-d_{\mathrm{unused}}\), evaluated in order along this candidate, are
\[
\begin{aligned}
D_0&=\frac{4h^2(h^2-1)}{(h^2+1)(h^2+3)},\\
D_1&=\frac{4h^4}{(h^2+3)^2},\\
D_2&=\frac{-4h^2(h^4-6h^2-3)}{(h^2+1)(h^2+3)^2}.
\end{aligned}
\]
All three are strictly positive exactly when \(h>1\) and \(h^4-6h^2-3<0\), equivalently \(1<h<H\). Strict positivity is necessary: an equality would make the point fixed, not take the proposed step. Reflection in the vertical axis preserves the map and yields the second candidate with the same condition. The two cycles are distinct because their base points have opposite nonzero coordinates. No other three-cycle itinerary is possible. The third-iterate derivative on the base is \((1-h^2)/(1+h^2)^2\).

**Period four with repeated base.** Four is the shortest even period whose itinerary can traverse all three supporting lines; a two-line alternating itinerary cannot make a nonconstant periodic cycle. A cyclic word of length four without adjacent equal symbols either alternates between two lines, or contains exactly three symbols with one repeated at opposite positions. Alternation between two lines cannot yield a nonconstant periodic orbit: the two-line projection return is a strict contraction whose only periodic fixed point is the intersection of those lines, and that point does not follow the alternating farthest-choice itinerary.

Take the word \(1\to0\to1\to2\to1\). Solving its projection-return fixed-point equation gives the displayed four points. At the two base points the signed target-versus-unused squared-distance difference is
\[
D_{\mathrm{base}}=\frac{4h^4}{(1+h^2)(h^2+2)}>0;
\]
at the two side points it is
\[
D_{\mathrm{side}}=
\frac{-4h^2(h^4-h^2-1)}{(1+h^2)(h^2+2)^2}.
\]
Consequently the itinerary is valid exactly when \(h^4-h^2-1<0\), i.e. \(h^2<\varphi\). It is genuinely least-period four (its four points occupy distinct side-and-base positions), and its four-step multiplier is \((1+h^2)^{-2}\).

**Period four with a repeated inclined side is impossible.** By symmetry it suffices to consider \(0\to1\to0\to2\to0\). Its unique unconstrained projection-return candidate, if written on the base at the step \(0\to1\), has coordinate
\[
t=-\frac{(h^2-1)^2}{h^4+2h^2+5}\le0.
\]
For \(t<0\), a point \((t,0)\) is strictly farther from the right inclined line \(L_2\) than from the left inclined line \(L_0\): their squared distances are respectively \(h^2(1-t)^2/(1+h^2)\) and \(h^2(1+t)^2/(1+h^2)\). Thus the proposed move from the base to \(L_0\) is impossible. If \(h=1\), then \(t=0\) is a distance tie and is fixed, so it too cannot follow the itinerary. Reflecting eliminates the analogous word with \(L_2\) repeated. This completes the exhaustive period-four count.

Because every valid branch inequality is strict, it persists on a neighborhood of each candidate. There, the corresponding return is the stated affine contraction; each valid cycle is locally attracting. All displayed candidate points lie in relative interiors of the triangle edges throughout their validity intervals. Combining the necessary and sufficient tests proves the census and the exact coexistence window.

## Verification
The independent exact-rational orbit enumerator in `verify.py` constructs fixed points of **every** cyclic line itinerary of lengths three and four, checks all farthest-choice inequalities directly from rational squared Euclidean distances, and deduplicates time shifts. For 111 distinct rational triangle heights, it confirmed the two census formulas and the multipliers in 488 exact assertions. The sampled regimes included no period-three/four cycles, only one four-cycle, only two three-cycles, and all three coexisting; the last regime occurred for nine heights. Run `python3 verify.py` with Python 3 and no external libraries. These are supporting finite checks; the proof above establishes the formulas for every real \(h>0\).

## Relationship to prior work
Everett introduced the full-three-line farthest-projection map, analyzed its asymptotic periodicity, and discussed geometric bifurcations for isosceles triangles. That article does not state the exact primitive four-cycle classification or the golden-ratio coexistence window. A separately published exact classification of primitive three-cycles on the same three-line system determines the two orientations and their existence thresholds; the period-three portion above is credited as covered prior knowledge, not an independent novelty claim. The contribution here is the **complete primitive four-cycle obstruction, its sharp parameter boundary, and the resulting coexistence of different attracting least periods**. The elementary fact that prescribed alternating orthogonal projections contract does not establish farthest-choice admissibility, which requires the strict squared-distance tests.

## Limitations
The result does not classify fixed points, primitive periods two or five and above, global basins, or invariant measures. Coexistence means existence of three distinct **locally** attracting cycles, not convergence of every orbit to one of them. It relies on complete supporting lines and the tie-as-fixed convention. Although the only two previous works found addressing precisely the same triangle map do not present the primitive four-cycle cutoff, priority in unindexed and otherwise inaccessible literature cannot be guaranteed.

## References
1. S. Everett, *A Piecewise Contractive Map on Triangles*, *Journal of Dynamical Systems and Geometric Theories* 18(2), 183–192, DOI `10.1080/1726037X.2020.1847765`. Publisher's first verified online publication: January 7, 2021. Author preprint: arXiv `2408.16019v1` (August 26, 2024), especially Definition 2.1, Sections 3–4.
2. *Exact two-orientation classification of primitive three-cycles for the farthest-projection triangle map*, published research record (October 11, 2026), `https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-two-orientation-classification-of-primitive-three-cycles-f--2944d54e59d8`, especially the strict-inequality criterion and stated period-three-only scope.
