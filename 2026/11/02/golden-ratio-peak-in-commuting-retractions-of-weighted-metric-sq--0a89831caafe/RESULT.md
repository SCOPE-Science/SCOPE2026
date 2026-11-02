# Golden-ratio peak in commuting retractions of weighted metric squares

## Finding

For any real numbers \(0<a\le b\), equip the four vertices \(M=\{0,1\}^2\) with the weighted Hamming metric
\[
d_{a,b}((u_1,u_2),(v_1,v_2))=a|u_1-v_1|+b|u_2-v_2|.
\]
Root the space at \((0,0)\). Let \(\kappa(a,b)\) denote the minimum, over all orders of its four vertices beginning at the root and all pairwise commuting retractions onto the successive initial segments, of the maximum Lipschitz constant of the retractions. Then
\[
\boxed{\kappa(a,b)=\min\!\left\{\frac ba,\,1+\frac ab\right\}.}
\]
Consequently, in terms of the aspect ratio \(r=b/a\ge1\), the value increases strictly from \(1\) to the golden ratio \(\varphi=(1+\sqrt5)/2\) on \(1\le r\le\varphi\) and decreases strictly to \(1\) as \(r\to\infty\) on \(r\ge\varphi\). The square has a commuting nonexpansive prefix-retraction system exactly when \(a=b\).

## Assumptions and scope

The domain is the **four vertex set**, not the continuous rectangle. The metric is the intrinsic weighted-edge shortest-path metric of the alternating-weight cycle. There are no interior points, and the two diagonals both have length \(a+b\). All maps take values in the same four-point metric space. Each retraction fixes its image pointwise; the successive images consist of the first \(j\) vertices in an ordering with the root first, for \(j=1,2,3,4\). Pairwise commutativity means \(r_i\circ r_j=r_{\min(i,j)}\). The infimum is a minimum because the set of feasible finite systems is finite. Swapping the two coordinates reduces arbitrary positive \(a,b\) to \(a\le b\).

## Proof

Write \(O=(0,0)\), \(X=(1,0)\), \(Y=(0,1)\), and \(Z=(1,1)\). Thus
\[
d(O,X)=d(Y,Z)=a,\quad d(O,Y)=d(X,Z)=b,\quad d(O,Z)=d(X,Y)=a+b.
\]

**Universal lower bound.** In any four-point prefix filtration, the third retraction fixes the root and two other vertices, and sends the last vertex to one of the three fixed points. The following table enumerates all possibilities; entries are the exact Lipschitz constants of these three-point retractions (the unmentioned points are fixed).

| Last vertex | First possible image | Second possible image | Third possible image |
| --- | --- | --- | --- |
| \(Z\) | \(Z\mapsto O: b/a\) | \(Z\mapsto X:1+b/a\) | \(Z\mapsto Y:1+a/b\) |
| \(Y\) | \(Y\mapsto O:1+b/a\) | \(Y\mapsto X:b/a\) | \(Y\mapsto Z:1+a/b\) |
| \(X\) | \(X\mapsto O:1+a/b\) | \(X\mapsto Y:b/a\) | \(X\mapsto Z:1+b/a\) |

For instance, if \(Z\mapsto O\), the edge \((Y,Z)\) of length \(a\) maps to \((Y,O)\) of length \(b\), giving \(b/a\). If \(Z\mapsto Y\), the edge \((X,Z)\) of length \(b\) maps to \((X,Y)\) of length \(a+b\), giving \(1+a/b\). If \(Z\mapsto X\), the edge \((Y,Z)\) gives \(1+b/a\). The other entries follow by the same full pairwise check using the six distances displayed above. Because \(b/a\ge1\), every entry in the table is at least \(\min\{b/a,1+a/b\}\). The Lipschitz constant of the third retraction gives this lower bound for the entire system, regardless of how the first two retractions were chosen.

**Matching upper bound.** Order the vertices as \(O,X,Y,Z\), and set \(r_1\equiv O\). Define \(r_2\) to fix \(O,X\) and send \(Y,Z\) to \(O\). A direct edge check gives \(\operatorname{Lip}(r_2)=1\), since the only potentially nontrivial mapped long edge is \((X,Z)\), which has image distance \(a\le b\). There are two choices for \(r_3\), each fixing \(O,X,Y\): either send \(Z\mapsto O\), giving Lipschitz constant \(b/a\), or send \(Z\mapsto Y\), giving Lipschitz constant \((a+b)/b=1+a/b\). Both commute with \(r_2\) because \(r_2(O)=r_2(Y)=r_2(Z)=O\); they also commute with the constant map \(r_1\), and with \(r_4=\operatorname{id}_M\). Selecting the smaller value proves the upper bound.

**Phase transition.** Substituting \(r=b/a\) gives \(\kappa(r)=\min\{r,1+1/r\}\). The two branches intersect exactly at \(r^2-r-1=0\), whose positive root is \(\varphi\). One branch is strictly increasing and the other strictly decreasing, yielding the asserted unique maximum and contractivity criterion.

## Verification

The standalone script `check_weighted_square.py` independently enumerates all vertex orderings rooted at \(O\), all possible second-stage assignments, and all third-stage choices compatible with commutativity. It compares the exact finite optimum with the formula for every integer pair \(1\le a\le b\le20\) and two rational parameter pairs, performing calculations with `fractions.Fraction`. Observed output: `PASS 212 weight pairs, 7632 commuting filtration candidates`. This finite calculation is a reproducibility cross-check; the unrestricted real-parameter theorem is established by the symbolic table and explicit construction, not by enumeration.

## Relationship to prior work

Retractional bases of metric sets linearize into Schauder bases of Lipschitz-free spaces. Hájek and Medina, *Schauder bases in Lipschitz free spaces over nets in Banach spaces* (arXiv:2112.03095), define the commuting retractional-basis framework and obtain existence bounds for uniformly discrete nets; their constructions do not calculate this four-point weighted optimum. Novotný, *Some Remarks on Schauder Bases in Lipschitz Free Spaces* (arXiv:1905.13188), gives lower bounds for unweighted centered graph circles of increasing radius (its Section 3) rather than the alternating-weight four-vertex metric considered here. Related published computations of interpolation into Lipschitz-free \(p\)-spaces and numerical indices of weighted graph-free spaces involve different mappings or invariants and do not directly imply the stated prefix-retraction constant.

## Limitations

The result concerns only commuting **point retractions** and their linearizations on the Lipschitz-free space. It does not assert a lower bound for arbitrary linear Schauder bases or coordinate projections. The graph has four vertices and opposite edge weights occur in equal pairs; it makes no assertion about arbitrary weighted cycles, higher-dimensional Hamming products, or continuous rectangles. Literature completeness and mathematical correctness have not been independently certified.

## References

1. M. Novotný, *Some Remarks on Schauder Bases in Lipschitz Free Spaces*, arXiv:1905.13188 (first public version 2019-05-30); published in *Bull. Belg. Math. Soc. Simon Stevin* **27** (2020), 111–126. In particular, Section 3 and Theorem 5.
2. P. Hájek and R. Medina, *Schauder bases in Lipschitz free spaces over nets in Banach spaces*, arXiv:2112.03095 (first public version 2021-12-06); especially Definition 1.2, Theorem 1.5, and Section 2.
