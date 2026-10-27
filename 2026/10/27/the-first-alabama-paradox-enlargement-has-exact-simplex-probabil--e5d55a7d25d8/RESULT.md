# The first Alabama-paradox enlargement has exact simplex probability \(1/72\)
## Finding
For Hamilton's largest-remainder apportionment among exactly three labeled parties with strictly positive vote shares summing to one, choose the shares uniformly from the two-dimensional simplex (Dirichlet \(1,1,1\)). With probability one the seat allocations at house sizes \(1,2,3,4\) are uniquely determined. No party can lose a seat in the enlargements \(1\) to \(2\) or \(2\) to \(3\). The probability that some party loses a seat in the first possible enlargement, from \(3\) to \(4\), is **exactly \(1/72\)**.

Writing the strictly ordered shares as \(w>v>u>0\), \(w+v+u=1\), the loss occurs if and only if
\[
w-u<\frac13,\qquad v-u>\frac14.
\]
Every such loss is precisely the transition in sorted seat allocations \((1,1,1)\to(2,2,0)\): the smallest party loses its seat and each larger party gains one. Its strict-inequality region is a nonempty rational polygon, with coordinate area \(1/864\) inside one of the six ordered chambers of the simplex. The overall uniform-simplex probability equals \(6(1/864)/(1/2)=1/72\). The boundary ties have probability zero.

## Assumptions and scope
For \(h\) seats and shares \(p_1,p_2,p_3\), first give party \(i\) exactly \(\lfloor hp_i\rfloor\) seats. Distribute the remaining \(h-\sum_i\lfloor hp_i\rfloor\) seats to the largest fractional remainders. Work outside the finite union of remainder-tie and equal-share lines for \(h=1,2,3,4\); this set has zero area. Each labeled share vector has constant planar density \(2\) on \(p_1>0,p_2>0,p_1+p_2<1\). There is no constitutional minimum-seat constraint, and the house increases by exactly one seat while shares remain fixed.

## Proof
**1. The only possible loser is the smallest party.** At each house size \(h\), there exists a common shift \(\alpha_h\in(0,1)\) such that each Hamilton allocation is
\[
s_i(h)=\lfloor hp_i+\alpha_h\rfloor.
\]
Indeed, choose the shift so the floor adds one precisely for the highest remainders; a strict cutoff leaves a nonempty open interval of shifts. If \(s_i(h+1)<s_i(h)\), set \(d=\alpha_{h+1}-\alpha_h\). The floor inequality implies \(p_i+d<0\), hence \(d<-p_i\). Every party \(j\) with \(p_j\le p_i\) then satisfies \(p_j+d<0\) and cannot gain a seat. Moreover \(p_j+d<p_j<1\) for every party, so no party can gain more than one seat. The total house grows by one while party \(i\) loses exactly one (a shift lies strictly between \(-1\) and \(1\), so a decrease exceeds no one seat). Therefore both other parties must gain one seat, and each has larger share than the loser. In particular the smallest party is the unique possible loser. As Hamilton allocations respect the share ordering, the smallest party holds no seat in a house of size \(1\) or \(2\), proving both earlier enlargements are loss-free.

**2. The first-loss transition is unique.** At house size \(3\), if the smallest party has a seat, the ordered allocation must be \((1,1,1)\). A loss at size \(4\) makes both other parties gain one, necessarily giving \((2,2,0)\).

**3. Exact characterization.** Assume \(w>v>u>0\) and that the allocations are \((1,1,1)\) and \((2,2,0)\). At four seats the middle party has two seats, but its share is below \(1/2\), so its quotient lies strictly between \(1\) and \(2\), and it must be rounded up. The smallest party has zero seats, so \(4u<1\), and the middle party's fractional remainder exceeds the smallest one's: \(4v-1>4u\). Thus \(v-u>1/4\). Together with \(w>v\) and the unit sum, this implies \(u<1/6\). If \(w\ge1/2\), its three-seat quota is at least \(3/2\). When \(w\ge2/3\) it must receive at least two seats; for \(1/2\le w<2/3\) its fractional remainder \(3w-1\) is at least \(1/2\), strictly greater than \(3u<1/2\). In either case the smallest party cannot have a three-seat allocation of one. Hence \(w<1/2\). The unit sum then gives \(v=1-w-u>1/2-u>1/3\). The three-seat floors are exactly \((1,1,0)\), and their sole remainder seat goes to the smallest party only when \(3u>3w-1\), equivalently \(w-u<1/3\).

Conversely, suppose \(w-u<1/3\) and \(v-u>1/4\). Since \(w>v\), the latter inequality gives \(u<1/6\), and the former forces \(w<1/2\). Consequently \(v>1/3\) and both largest shares are in \((1/3,1/2)\). At three seats the floors are \((1,1,0)\), and \(3u>3w-1\ge3v-1\) assigns the one remaining seat to the smallest party. At four seats the floors remain \((1,1,0)\), and \(4v-1>4u\), \(4w-1>4u\), award both remaining seats to the larger parties. This gives exactly the stated paradox transition.

**4. Exact area.** Put the smallest share \(u\) on the horizontal axis and the middle share \(v\) on the vertical axis, with \(w=1-u-v\). The ordered paradox chamber is
\[
\frac19<u<\frac16,\qquad
\max\left\{\frac23-2u,\ u+\frac14\right\}<v<\frac{1-u}{2}.
\]
The two lower boundaries cross at \(u=5/36\). The areas of the two triangular pieces are
\[
\int_{1/9}^{5/36}\left(\frac{1-u}{2}-\frac23+2u\right)du
=\frac1{1728},
\quad
\int_{5/36}^{1/6}\left(\frac{1-u}{2}-u-\frac14\right)du
=\frac1{1728}.
\]
Their sum is \(1/864\). The six relabelings of a strictly ordered triple give disjoint congruent chambers, and the \((p_1,p_2)\) simplex has area \(1/2\). Multiplication by the normalized density \(2\) gives \(6\times2\times(1/864)=1/72\), as claimed.

## Verification
A constructive rational witness is \((w,v,u)=(4/9,5/12,5/36)\). Its Hamilton allocations for \(h=1,2,3,4\) are respectively \((1,0,0),(1,1,0),(1,1,1),(2,2,0)\), with strict remainder cutoffs. Run `python3 verify.py` (Python standard library only). It checks both integrals in rational arithmetic and exhaustively compares the theorem against all sorted positive integer triples of total size at most \(180\) with strict cutoffs, yielding \(153762\) qualifying rational parameter profiles and \(1925\) paradox profiles. These finite checks are consistency tests; Steps 1–4 prove the continuum statement.

## Relationship to prior work
Hamilton's largest-remainder method and its Alabama paradox are classical. Janson and Linusson, *The Probability of the Alabama Paradox* (arXiv:1104.2137; 2011 preprint, 2012 journal publication), Theorem 1.3 and Section 3, instead study the **asymptotic density across increasing house sizes for fixed population shares**, then average over the simplex. Their three-state result \(1/36\) is an average of that limiting density, not the probability of a loss at the specific first possible enlargement \(3\to4\), and does not imply the present finite-cutoff \(1/72\) value. Their worked rational example already exhibits a \(3\to4\) loss; that example is prior art, not claimed here.

Bradberry, *A Geometric View of Some Apportionment Paradoxes* (1992), analyzes geometric susceptible regions, but the complete article could not be compared in this examination; its possible stronger coverage is an important residual originality risk. A published note on tie-independent Alabama losses in equal-larger-population rational triples gives a modular characterization on a lower-dimensional family \(w=v\), not the area of the generic three-share first-expansion chamber. The precise first-house exact volume and complete open-polygon characterization, rather than existence of the paradox, are the contributions assessed here.

## Limitations
The \(1/72\) figure assumes uniformly distributed shares; different distributions have different probabilities. The characterization is an almost-sure (strict-cutoff) statement, not a specification of behavior under arbitrary tie-breaking on measure-zero boundaries. The population vector is held fixed as the house grows; the result is not about population changes, additional states, or larger house transitions. The geometric paper by Bradberry remains incompletely inspected, so the originality assessment has a documented literature-access limitation. No claim of independent verification is made.

## References
1. Janson, S., and Linusson, S., *The Probability of the Alabama Paradox*, arXiv:1104.2137, first public preprint 12 April 2011; *Journal of Applied Probability* 49 (2012), 773–794. https://arxiv.org/abs/1104.2137.
2. Bradberry, B. A., *A Geometric View of Some Apportionment Paradoxes*, *Mathematics Magazine* 65 (1992), 3–17. https://doi.org/10.1080/0025570X.1992.11995970.
3. *Tie-independent Alabama losses for equal-pair rational populations*, published mathematics note, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-tie-independent-alabama-losses-for-equal-pair-rational-populatio--494a0538d100.
