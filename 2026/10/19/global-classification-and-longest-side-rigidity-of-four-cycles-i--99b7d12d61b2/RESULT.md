# Global classification and longest-side rigidity of four-cycles in the farthest-projection triangle map

## Finding
Let \(T\) be the farthest-orthogonal-projection map on the union of the three **complete supporting lines** of a nondegenerate Euclidean triangle, with equal projection distances interpreted as a fixed point. Then **at most one primitive period-four orbit exists** (counted up to cyclic permutation); if present, it is locally attracting, and its four-step linear contraction factor is explicitly determined by the triangle shape. Such an orbit can occur only when its repeated supporting line is the triangle's uniquely longest side.

Here is a necessary and sufficient criterion for **every** triangle shape. After an orientation-preserving Euclidean similarity, label the unique candidate longest side \(AB\) with \(A=(0,0)\), \(B=(1,0)\), and the third vertex \(C=(u,v)\), \(v>0\). Write
\[
 s=u^2+v^2,\qquad t=(1-u)^2+v^2,\qquad E=u^2+(1-u)^2+v^2.
\]
There is exactly one primitive period-four orbit if and only if **all four strict tests** hold:
\[
\begin{aligned}
 st&>(1-u)^4, &u^2t&>(E-u)^2,\\
 st&>u^4, &(1-u)^2s&>(E-1+u)^2.
\end{aligned}
\tag{1}
\]
(The tests themselves force \(0<u<1\) and \(s,t<1\), so the hypothesized base is automatically strictly longest.) When the tests hold, the ordered orbit is
\[
\begin{aligned}
 P_0&=(s/E,0),&P_1&=(u^2/E,uv/E),\\
 P_2&=(u^2/E,0),&P_3&=(s/E,(1-u)v/E),
\end{aligned}
\tag{2}
\]
with \(T(P_i)=P_{i+1}\) for indices modulo four. Its contraction factor on the initial line is
\[
 \eta=\frac{u^2(1-u)^2}{st}\in(0,1).
\tag{3}
\]
All ties are **excluded**, not counted as period-four cycles. If the original triangle is presented with another longest side, relabel that side as \(AB\) and apply (1); if no side satisfies (1), there is no four-cycle anywhere on the three lines.

For the natural isosceles family \(C=(1/2,v)\), the global classification reduces to the **golden-ratio height threshold**
\[
 N_4(v)=\begin{cases}
 1,&0<v<\sqrt{(1+\sqrt5)/8},\\
 0,&v\ge\sqrt{(1+\sqrt5)/8}.
 \end{cases}
\tag{4}
\]
The critical height is \(\sqrt{\varphi}/2\), where \(\varphi=(1+\sqrt5)/2\). At equality the prospective four-cycle encounters a farthest-choice tie and is not a period-four orbit. **The threshold and four-cycle uniqueness were already established for acute isosceles triangles with \(v>1/2\)**; equation (4) is a consistency check and extension of the domain to all \(v>0\), not the central novelty claim.

## Assumptions and scope
The ambient space is \(X=\ell_{AB}\cup\ell_{AC}\cup\ell_{BC}\), each \(\ell\) being a full infinite line. From \(x\in\ell_i\), orthogonally project onto the other two lines and move to the more distant projection, comparing the Euclidean distances from \(x\) to those two projections. If the distances are equal, set \(T(x)=x\). At a triangle vertex the chosen nonfixed move is unambiguous: projection onto the other incident line has zero movement while projection onto the third line has positive movement. Period means the **least positive period**, and cycles differing by cyclic permutation of their listed points are counted once. No assumption of an acute triangle, genericity, or avoidance of branch boundaries is imposed. The fixed-point tie rule is essential to the boundary exclusions.

## Proof
**1. Exhaustive period-four line itineraries.** Label an orbit point by the supporting line targeted by its immediately preceding nonfixed step. Consecutive labels must differ. This rule also works at vertices: the incident line with zero projection distance cannot be the chosen nonfixed target. A cyclic four-word on three labels with adjacent distinct labels, including the wraparound, either alternates between two lines or uses all three lines and repeats exactly one of them at opposite positions. In the two-line case, the two orthogonal projections compose to a strict affine contraction on one line. Its unique fixed point is the intersection of the two lines, which cannot participate in a nonfixed periodic orbit. Thus every primitive four-cycle has a three-line itinerary of the form \(\ell_0\to\ell_1\to\ell_0\to\ell_2\to\ell_0\), up to cyclic rotation. Interchanging the names \(\ell_1,\ell_2\) merely changes the starting occurrence of the repeated line, not the orbit.

**2. The unique prescribed-itinerary candidate.** Normalize the repeated line to \(\ell_0=AB\), with \(\ell_1=AC\) and \(\ell_2=BC\). Each orthogonal projection is an affine map between lines with strict Lipschitz modulus less than one; the fourth return to \(AB\) is therefore a strict affine contraction with one fixed point. A direct composition of \(AB\to AC\to AB\to BC\to AB\) yields the starting coordinate \(s/E\), and its successive projections are exactly the four points in (2). This uniquely determines the potential four-cycle for that repeated line. The reverse labeling \(AB\to BC\to AB\to AC\to AB\) starts instead at \(P_2\) and gives precisely the same set of four points, so it supplies no additional cycle.

**3. Farthest-choice inequalities, including ties.** At the points \(P_0,P_1,P_2,P_3\), respectively, the preferred target lines are \(AC,AB,BC,AB\), and the competitors are \(BC,BC,AC,AC\). Elementary orthogonal-projection formulas show that the four squared-distance margins (chosen target minus competitor), each multiplied by the common positive factor \(E^2/v^2\), are
\[
 \frac{st-(1-u)^4}{t},\quad
 \frac{u^2t-(E-u)^2}{t},\quad
 \frac{st-u^4}{s},\quad
 \frac{(1-u)^2s-(E-1+u)^2}{s}.
\tag{5}
\]
Here \(s,t,E,v\) are strictly positive. Consequently the itinerary is realized by \(T\) **exactly** when all four inequalities (1) are strict. If any is equal to zero, the map fixes the corresponding point by its tie rule, and if negative, the prescribed step is not selected. Thus none of the equality cases is spuriously admitted.

**4. The repeated line must be uniquely longest.** The second strict test in (1) forces \(u>0\): if \(u\le0\), then \(E-u=t+u^2-u>|u|\sqrt t\), contradicting that test. The fourth similarly forces \(u<1\), because if \(u\ge1\), then \(E-1+u=s+(1-u)^2-(1-u)>|1-u|\sqrt s\). Hence \(0<u<1\). Suppose \(t\ge1\). Then \(E-u=t+u^2-u\) and the function \(f(t)=t+u^2-u-u\sqrt t\), for \(t\ge1\), satisfies \(f(1)=(1-u)^2>0\) and \(f'(t)=1-u/(2\sqrt t)>0\). Thus \(E-u>u\sqrt t\), contradicting the second strict test. Therefore \(t<1\). The symmetric argument, exchanging \(u\) with \(1-u\), gives \(s<1\) from the fourth test. The side lengths squared are \(1,s,t\), so \(AB\) is strictly the longest. A nondegenerate triangle cannot have two different strictly longest sides: at most one of its supporting lines can be the repeated line of a primitive four-cycle. Combined with uniqueness in Step 2, this proves the global maximum of one.

**5. Primitivity and local attraction.** From \(0<u<1\) and \(v>0\), the four points (2) are distinct (\(P_0\ne P_2\) since \(s-u^2=v^2>0\), and the points off \(AB\) have positive heights). The strict comparisons remain valid in a neighborhood of the cycle, so its fourth iterate agrees there with the prescribed affine projection return. The absolute tangent multiplier is the product of the four line-to-line projection factors, \(\eta=u^2(1-u)^2/(st)<1\). This proves local attraction on the union of the three lines and least period four, not merely period dividing four.

**6. Exact isosceles cutoff.** For \(u=1/2\), write \(q=v^2+1/4=s=t\). The first and third tests are \(q^2>1/16\), automatically true for \(v>0\). The second and fourth both reduce to \(q/4>v^4\), equivalent to \(16v^4-4v^2-1<0\). Solving its positive root gives precisely (4). Equality is excluded by Step 3, proving the sharp threshold.

## Verification
The accompanying standalone standard-library Python program `verify.py` computes rational orthogonal projections and literal farthest-choice comparisons. On a finite exact grid of \(204\) nondegenerate rational triangles and \(32\) additional isosceles heights, it exhaustively enumerates all length-four line-label words, independently solves their affine projection returns, tests actual branch selection, and compares all genuine primitive four-cycles with the closed-form predicate and orbit (1)–(2). It also checks the isosceles quartic sign criterion and never observes more than one cycle. Its expected output is `CHECK_OK exact rational triangles: 236; grid cycles zero/one: [161, 43]`. This **finite diagnostic is not an exhaustive classification of all real triangles**; the continuum theorem follows from Steps 1–6.

## Relationship to prior work
Everett introduces the farthest-projection map, its tie convention, convergence to fixed or periodic orbits, and a qualitative/numerical isosceles bifurcation picture. In Section 4 the original paper **changes the map to the bounded triangle boundary**, which is not identical to the unrestricted three-line setting here. A separate prior result, *Golden-ratio period-four cutoff and three-attractor coexistence in a triangle projection map* (identifier `dea05cf4-28ff-41cb-9742-a7fad4b5e103`), **already establishes the unique four-cycle and its precise golden-ratio cutoff for the acute isosceles subfamily \(u=1/2,\ v>1/2\)**. That theorem and its corollaries are NOT claimed as new here. The present theorem extends beyond that one-dimensional symmetric subfamily to **all scalene, acute, right and obtuse triangles**, supplies the explicit four strict shape inequalities and all-cycle coordinates, and proves the global **longest-side rigidity and at-most-one count**. Another prior finding, *Exact two-orientation classification of primitive three-cycles for the farthest-projection triangle map*, treats **least period three only**, not the period-four global geometry. The prior equilateral basin classification *Log-periodic attraction-basin densities for an equilateral farthest-projection map* concerns three-cycle basins, not four-cycle existence. The separate Wang–Zhang geometric iterated-function system acts on the **moduli space of triangles**. Externally prescribed alternating-projection contraction gives candidate uniqueness for a word, but cannot alone enforce the four farthest-choice comparisons or longest-side obstruction. These are statement-and-implication distinctions, not merely different terminology.

## Limitations
The result does not classify periods other than four, all basins of attraction, or possible global coexistence with longer attracting cycles. Local attraction does not imply a global attractor. The map on the union of **complete lines** is essential; a map clipped to the three bounded segments requires separate boundary conventions and need not share these conditions. The known isosceles cutoff is recovered as a corollary, not as an independent new priority claim. The genuinely new scope is the all-triangle period-four decision, coordinates and longest-side rigidity. No independent mathematical audit or exhaustive historical-priority guarantee is claimed.

## References
1. Samuel Everett, *A Piecewise Contractive Map on Triangles*, *Journal of Dynamical Systems and Geometric Theories* **18** (2020), no. 2, 183–192; DOI `10.1080/1726037X.2020.1847765`; publisher's verified first online posting: **2021-01-07**. Author preprint, arXiv `2408.16019v1` (posted 2024-08-26), Definition 2.1 and Sections 3–4.
2. *Golden-ratio period-four cutoff and three-attractor coexistence in a triangle projection map*, mathematical research result, stable identifier `dea05cf4-28ff-41cb-9742-a7fad4b5e103`; establishes the four-cycle threshold on the acute isosceles family.
3. *Exact two-orientation classification of primitive three-cycles for the farthest-projection triangle map*, mathematical research result, stable identifier `2944d54e59d8`; period-three classification only.
4. *Log-periodic attraction-basin densities for an equilateral farthest-projection map*, mathematical research result, stable identifier `ff88be28-f88b-44b2-aa58-e45df2eb7604`; equilateral three-cycle basins.
5. Jiajun Wang and Ying Zhang, *A geometric iterated function system on triangles*, arXiv `1605.01794v1` (2016); concerns the moduli of ordered triangles, not periodic points of the farthest-projection line map.
