# Exact multiple illumination and parity rigidity for polygons with antipodal edge-normal fans

## Finding
Let \(P\subset\mathbb R^2\) be a convex polygon with \(2r\) genuine edges, where \(r\ge2\). Suppose the outward unit normals in cyclic order satisfy
\[
\nu_{j+r}=-\nu_j\qquad(j\in\mathbb Z/(2r)\mathbb Z).
\]
For every integer \(k\ge1\), the exact \(k\)-fold illumination number is
\[
I^{(k)}(P)=\left\lceil\frac{2rk}{r-1}\right\rceil.
\]
For fractional illumination by finite nonnegative weighted direction sets,
\[
I^*(P)=\frac{2r}{r-1}.
\]
More precisely, the circle of directions has \(2r\) open cells \(C_j\), indexed so that every direction in \(C_j\) illuminates exactly the consecutive vertex block \(v_j,v_{j+1},\ldots,v_{j+r-2}\). Every optimal fractional illumination measure has zero mass on the complementary critical directions. Writing \(w_j=\mu(C_j)\), all optimal cell-mass patterns are:
\[
\begin{cases}
w_j=1/(r-1)\text{ for every }j,&r\text{ even},\\
w_{2j}=a,\quad w_{2j+1}=b,\quad a,b\ge0,\quad a+b=2/(r-1),&r\text{ odd}.
\end{cases}
\]
Conversely every such pattern, realized by any finite nonnegative weights within the appropriate open direction cells, is optimal.

## Assumptions and scope
A direction \(u\in S^1\) illuminates a boundary point \(x\) when the ray \(x+tu\), \(t>0\), meets the interior of \(P\). The number \(I^{(k)}(P)\) minimizes the cardinality, counted with repetitions, of a multiset of directions that illuminates every boundary point at least \(k\) times. The fractional number \(I^*(P)\) minimizes total mass of a finite-support nonnegative direction measure that illuminates every boundary point with total mass at least one. All normal and vertex indices are cyclic modulo \(2r\). The polygon has no consecutive collinear sides; no condition of equiangularity, congruence, or central symmetry is imposed.

## Proof
**Direction cells.** At the vertex \(v_j\), a direction \(u\) illuminates \(v_j\) precisely when its scalar products with both incident outward edge normals are strictly negative. By the antipodal normal condition, for a generic direction \(u\) (perpendicular to none of the edges' normals), exactly one from each antipodal normal pair has negative scalar product. Since normals are cyclically arranged, these are exactly \(r\) consecutive edge normals. Consequently exactly their \(r-1\) interior common vertices are illuminated, a consecutive block. As the direction rotates around the circle, each of the \(2r\) critical rays is crossed once and the starting vertex of this block advances cyclically by one. Hence all \(2r\) consecutive \((r-1)\)-vertex blocks are realized, one per open cell. On a critical ray one antipodal pair of edge-normal scalar products is zero; the number of negatively paired consecutive edges is at most \(r-1\), so at most \(r-2\) vertices can be illuminated. Every open edge point is illuminated whenever a chosen direction illuminates either of its two endpoints. Thus it suffices to cover vertices.

**Lower bounds.** Put \(n=2r\) and \(L=r-1\). Each direction illuminates at most \(L\) vertices. A \(k\)-fold multiset with \(N\) directions yields at least \(nk\) vertex-direction incidences, and at most \(NL\). Thus \(N\ge\lceil nk/L\rceil\). Similarly, a fractional measure of total mass \(M\) yields a sum over vertex illumination masses at most \(LM\), but this sum must be at least \(n\). Therefore \(M\ge n/L\).

**Exact integer construction.** Take \(N=\lceil nk/L\rceil\). For \(j=0,\ldots,N-1\), choose one direction in the cell that illuminates the block beginning at
\[
s_j=\left\lfloor\frac{nj}{N}\right\rfloor\pmod n.
\]
Repetitions are allowed. Any vertex belongs to those blocks whose starting labels lie in an interval of \(L\) consecutive residues. Periodically lifting the labels, the number of \(s_j\) in any such interval is either \(\lfloor NL/n\rfloor\) or \(\lceil NL/n\rceil\): indeed, the condition that \(\lfloor nj/N\rfloor\) belongs to an integer interval \([a,a+L)\) is equivalent to \(Na/n\le j<N(a+L)/n\). As \(NL/n\ge k\), every vertex is illuminated at least \(k\) times. This attains the lower bound.

**Fractional construction.** Put weight \(1/L\) on one representative direction in every cell. Each vertex lies in exactly \(L\) cyclic blocks. Thus it receives total weight one, and the total weight is \(n/L\). This attains the fractional lower bound.

**Complete classification of fractional optimizers.** Let \(\mu\) attain the optimal total mass \(n/L\). Write \(t\ge0\) for its total mass on the critical direction rays and \(w_j\) for its mass in the generic cell \(C_j\). Every generic direction illuminates exactly \(L\) vertices, and every critical direction at most \(L-1\). Summing vertex illumination constraints gives
\[
n\le L\sum_j w_j+(L-1)t=L\mu(S^1)-t=n-t,
\]
so \(t=0\), and every vertex constraint is an equality. Therefore
\[
\sum_{h=0}^{L-1}w_{i-h}=1\qquad\text{for all }i\pmod n.
\]
Subtracting consecutive equations yields \(w_i=w_{i-L}\). The number of cycles of this recurrence is
\[
\gcd(n,L)=\gcd(2r,r-1)=\gcd(2,r-1).
\]
For even \(r\), the gcd is one and all weights equal \(1/L\). For odd \(r\), it is two, the parity classes are invariant, and each vertex equation has \(L/2\) terms of each parity, giving \(a+b=2/L\). Nonnegativity gives precisely the stated interval; every such pattern satisfies every vertex equation and is optimal.

**A genuinely noncentral and nonequiangular example.** Use rational unit tangent vectors \(u_0=(1,0)\), \(u_1=(3/5,4/5)\), \(u_2=(-5/13,12/13)\), and set \(u_{j+3}=-u_j\). Put
\[
(d_0,d_1,d_2)=\left(\frac{56}{65},-\frac{12}{13},\frac45\right),\qquad
\ell_j=1+\frac{d_j}{2},\quad \ell_{j+3}=1-\frac{d_j}{2}.
\]
These are positive lengths. The six successive edge vectors \(\ell_j u_j\) close because \(\sum_{j=0}^{2}d_j u_j=0\), and their consecutive oriented cross products are strictly positive; hence they bound a strictly convex hexagon. Its three pairs of opposite edge directions are antipodal. Opposite lengths differ, so it has no center of symmetry. The dot products \(u_0\cdot u_1=3/5\) and \(u_1\cdot u_2=33/65\) differ, so it is not equiangular. The theorem applies nevertheless.

## Verification
The accompanying `verify.py` checks exact cyclic multicover counts for every integer \(2\le r\le40\) and \(1\le k\le50\) (1,950 cases), the fractional parity patterns, and the rational nonequiangular noncentral hexagon using exact fractions. The script returns `VERIFY_OK`. These computations exercise the discrete formulas separately from the proof; the statements for unbounded \(r,k\) follow from the preceding argument, not from finite tests.

## Relationship to prior work
Naszódi introduced fractional illumination and proved universal bounds. Sriamorn proved the multiple-illumination formula \(\lceil nk/\lfloor(n-1)/2\rfloor\rceil\) for regular \(n\)-gons and asked for an algorithm on arbitrary convex polygons (Problem 2). The present theorem concerns every polygon with an antipodally paired **normal fan**, including some neither equiangular nor centrally symmetric, and determines the entire optimum fractional cell-mass face, not just its minimum. Gorodzha's recent general fractional upper bound and equality characterization motivate studying exact polygon-specific values; the general bound is not an exact normal-fan classification.

## Limitations
The result does not address general polygons without antipodally paired normal fans, or give a full classification of optimal integer multisets. For fractional optimizers it classifies mass assigned to each open direction cell, not the distribution *within* a cell. The numerical checks are finite consistency tests, not exhaustive proof of an infinite statement. Priority comparisons are based on the identified primary literature and searchable records, with the possibility of unindexed equivalent arguments; no independent mathematical audit is asserted.

## References
1. Y. Gorodzha, *Fractional illumination and the optimal exponential rate in Hadwiger's covering conjecture*, arXiv:2609.23913 (first submitted 2026-09-20), https://arxiv.org/abs/2609.23913.
2. K. Sriamorn, *On the multiple illumination numbers of convex bodies*, arXiv:2306.13517 (2023), section 3.3, Lemma 3.5 and Problem 2, https://arxiv.org/pdf/2306.13517.
3. M. Naszódi, *Fractional illumination of convex bodies*, Contributions to Discrete Mathematics **4** (2009), 83--88, https://doi.org/10.55016/ojs/cdm.v4i2.62022.
