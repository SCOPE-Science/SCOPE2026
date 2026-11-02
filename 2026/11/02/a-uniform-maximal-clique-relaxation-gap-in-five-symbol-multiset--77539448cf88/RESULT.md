# A uniform maximal-clique relaxation gap in five-symbol multiset deletion coding

## Finding

Let \(G_5(n)\) be the unit-transfer graph on five-coordinate nonnegative integer vectors of coordinate sum \(n\), with two distinct vertices adjacent when their difference is \(e_i-e_j\) for distinct coordinates. Let \(L_5(n)\) denote the maximum of \(\sum_{x\in V(G_5(n))}p_x\) over nonnegative real \(p_x\) satisfying \(\sum_{x\in K}p_x\le1\) for every clique \(K\) of \(G_5(n)\).

**Theorem.** For every integer \(n\ge8\),
\[
L_5(n)\ge\frac15\binom{n+4}{4}+\frac43.
\]
In particular, the previously established formula \(\alpha(G_5(n))=\lceil\binom{n+4}{4}/5\rceil\) implies
\[
L_5(n)-\alpha(G_5(n))\ge\frac8{15}>0.
\]
Thus even the *complete family of maximal-clique inequalities* cannot certify the sharp single-deletion code size at any of these infinitely many block lengths. This is a statement about a specified linear relaxation, not a new determination of the integer independence number.

## Assumptions and scope

Fix the alphabet \(\{0,1,2,3,4\}\). A transmitted multiset of size \(n\) is its multiplicity vector \(x=(x_0,\ldots,x_4)\in\mathbb Z_{\ge0}^5\) with \(\sum_i x_i=n\). Exactly one deletion decreases one positive coordinate by one. Two distinct transmitted multisets have intersecting one-deletion output sets precisely when they differ by \(e_i-e_j\), hence single-deletion codes are independent sets in \(G_5(n)\). The theorem concerns \(n\ge8\) and the nonnegative fractional stable-set relaxation defined by *all* cliques; neither ordered-string deletion nor multiple deletions is included.

## Proof

**1. The complete clique family.** Every lower clique has the form
\[
D(y)=\{y+e_i:0\le i\le4\},\quad y\in\mathbb Z_{\ge0}^5,\quad\sum_i y_i=n-1.
\]
Every upper clique has the form
\[
U(z)=\{z-e_i:z_i>0\},\quad z\in\mathbb Z_{\ge0}^5,\quad\sum_i z_i=n+1.
\]
Every edge lies in one of these. To see that every larger clique does too, take an adjacent pair \(x=w+e_i\), \(y=w+e_j\) with \(i\ne j\). A third common neighbor is either \(w+e_k\) (a lower neighbor) or \(w+e_i+e_j-e_k\) (an upper neighbor, with \(w_k>0\)). A lower common neighbor distinct from \(x,y\) is never adjacent to an upper common neighbor distinct from \(x,y\). Consequently all vertices of any clique containing the edge are inside one \(D(w)\) or one \(U(w+e_i+e_j)\). Isolated singleton inequalities are also contained in lower cliques. Therefore checking both displayed families checks **every** clique inequality.

**2. A finite corner perturbation.** Put \(b=1/5\). For each coordinate \(i\), define \(f_i(x)=0\) except when the coordinates of \(x\) other than \(i\) are zero or one, and their total number \(t\) of ones is at most three. In the exceptional cases set
\[
f_i(x)=\begin{cases}
4/5,&t=0,\\
-1/5,&t=1,\\
1/15,&t=2,\\
-1/30,&t=3.
\end{cases}
\]
Define \(p_x=b+\sum_{i=0}^4 f_i(x)\). For \(n\ge8\), a vertex belongs to at most one modified corner, so \(0\le p_x\le1\). Moreover two distinct vertices from different modified corners cannot be adjacent: if \(x_i\ge n-3\) and \(y_j\ge n-3\) for distinct \(i,j\), adjacency would imply \(n\ge x_i+y_j-1\ge2n-7\), forcing \(n\le7\). Thus one clique cannot meet two different modified corners.

**3. Feasibility of the clique inequalities.** It is enough to inspect one corner. Write \(t\) for the total multiplicity outside its distinguished coordinate. For lower cliques, the perturbation sum is zero when the outside profile is squarefree with \(t=0,1,2\), equals \(-1/30\) when it is squarefree with \(t=3\), and otherwise equals zero. In every case it is nonpositive. Since a lower clique has five vertices, its baseline sum is one.

For upper cliques, the baseline sum is \(s/5\), where \(s\) is the number of positive coordinates of its center. Its available slack is \((5-s)/5\). When \(t\le4\), the outside multiplicity partition and the corner perturbation sum are:

| Outside partition | Perturbation sum | Available slack |
| --- | ---: | ---: |
| empty | \(4/5\) | \(4/5\) |
| \((1)\) | \(3/5\) | \(3/5\) |
| \((2)\) | \(-1/5\) | \(3/5\) |
| \((1,1)\) | \(-1/3\) | \(2/5\) |
| \((3)\) | \(0\) | \(3/5\) |
| \((2,1)\) | \(1/15\) | \(2/5\) |
| \((1,1,1)\) | \(1/6\) | \(1/5\) |
| \((4)\) | \(0\) | \(3/5\) |
| \((3,1)\), \((2,2)\) | \(0\) | \(2/5\) |
| \((2,1,1)\) | \(-1/30\) | \(1/5\) |
| \((1,1,1,1)\) | \(-2/15\) | \(0\) |

When \(t\ge5\), every affected child has outside multiplicity at least four, so the perturbation sum is zero. Every displayed perturbation is at most its available slack. This proves feasibility for both clique families and hence all cliques.

**4. Objective and the strict gap.** For any one corner the perturbation changes exactly one pure vertex, four one-off vertices, six squarefree two-off vertices, and four squarefree three-off vertices. Its total mass is
\[
\frac45-4\frac15+6\frac1{15}-4\frac1{30}=\frac4{15}.
\]
The five corners are disjoint for \(n\ge8\), so \(\sum_xp_x=\binom{n+4}{4}/5+5(4/15)\), proving the fractional bound. The published exact independence theorem gives \(\alpha(G_5(n))=\lceil\binom{n+4}{4}/5\rceil\). Since the difference between the ceiling and the number is at most \(4/5\), the relaxation exceeds the true integer optimum by at least \(4/3-4/5=8/15\), as claimed.

## Verification

The standalone `verify.py` uses exact rational arithmetic only. It verifies every affected one-corner pattern and, independently, enumerates the complete original vertex set and every lower and upper clique at lengths \(8,9,10,11,12,15,20\). It checks nonnegativity, every clique inequality, the exact objective, and the displayed strict separation. Its final status is `VERIFY_OK`. This finite replay supplements the all-length combinatorial proof and does not purport to exhaust infinitely many lengths.

## Relationship to prior work

Kreindel, Essayag and Zabokritskiy's January 2026 multiset-deletion paper introduced the coding setting and general constructive bounds. Their March paper studied deletion-ball geometry and sphere-packing bounds. Zabokritskiy's July 2026 paper **already determined** \(\alpha(G_5(n))\) for every degree, apart from explicitly resolved small exceptions, and developed weighted local-cover inequalities with non-clique templates. In Section 9, that paper also exhibits a distinct clique-relaxation obstruction at \((q,d)=(32,28)\). These results establish the integer optimum and the general relaxation framework but do not state or imply the present explicit *all-degree, five-symbol maximal-clique integrality gap*. Here the integer optimum is used as a known premise, not claimed as new.

## Limitations

The additive gap \(8/15\) is a proved uniform lower bound, not an exact computation of the optimal fractional LP value. The proof does not characterize all fractional maximizers, handle five-symbol degrees below eight, extend the bound to other alphabet sizes, or show a multiplicative gap bounded away from one. It demonstrates necessity of inequalities beyond cliques for a sharp LP certificate, but does not say that no other combinatorial proof of integer optimality exists. Publication priority for closely related but unindexed fractional-relaxation constructions remains a residual risk.

## References

1. A. Kreindel, I. B. Essayag and A. L. Zabokritskiy, *Multiset Deletion-Correcting Codes: Bounds and Constructions*, arXiv:2601.05636v1, publicly posted 9 January 2026. https://arxiv.org/html/2601.05636v1
2. A. Kreindel, I. B. Essayag and A. L. Zabokritskiy, *Polynomial Constructions and Deletion-Ball Geometry for Multiset Deletion Codes*, arXiv:2603.18322v1, 18 March 2026. https://arxiv.org/html/2603.18322v1
3. A. L. Zabokritskiy, *Independent Sets in Multiset Profile Graphs via Weighted Local Covers*, arXiv:2607.13733, first publicly posted 15 July 2026, in particular Sections 3, 6 and 9. https://arxiv.org/abs/2607.13733
4. D. Kovačević and V. Y. F. Tan, *Codes in the Space of Multisets—Coding for Permutation Channels with Impairments*, arXiv:1612.08837, December 2016. https://arxiv.org/abs/1612.08837
