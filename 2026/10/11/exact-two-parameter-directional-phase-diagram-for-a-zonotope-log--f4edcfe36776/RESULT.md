# Exact two-parameter directional phase diagram for a zonotope log-submodularity counterexample

## Finding
For the four-dimensional zonotopes and segments defined below, the log-submodularity defect has the exact expression
\[
\Delta(a,b)=8-4q-3q^2-(8+2q)X+(8+4q)Z,
\quad q=a+b,\quad X=|1-a|+|1-b|,\quad Z=|1-q|.
\]
Here \(a,b\ge0\). The inequality \(|A_{a,b}|\,|A_{a,b}+B+C|\le|A_{a,b}+B|\,|A_{a,b}+C|\) holds exactly when \(\Delta(a,b)\le0\). Its **complete** directional sign phase diagram is:

1. If \(0\le a,b\le1\) and \(q\le1\), then \(\Delta=-q(5q+4)\), strictly negative except at \((a,b)=(0,0)\).
2. If \(0\le a,b\le1\) and \(1\le q\le2\), then \(\Delta=3q^2+4q-16\). It is positive exactly when \(q>\frac23(\sqrt{13}-1)\), zero at equality, and negative below.
3. If \(a,b\ge1\), then \(\Delta=16-4q-q^2\). It is positive exactly when \(q<2(\sqrt5-1)\), zero at equality, and negative above.
4. If \(a\ge1\ge b\ge0\), or \(b\ge1\ge a\ge0\), then \(\Delta=q^2-(8+2q)|a-b|\). It is positive, zero, or negative according as \(|a-b|\) is smaller than, equal to, or larger than \(q^2/(8+2q)\).

The formulas agree on all common chamber boundaries. Thus failure occurs in an explicitly described two-dimensional region, with two distinct radical transition levels and an additional curved angular-asymmetry boundary. For \((a,b)=(1,1)\), the defect equals \(4\), recovering the previously known example. Cartesian product with a unit cube carries the same phase diagram to every Euclidean dimension at least four, with volume normalized as stated below.

## Assumptions and scope
Let \(e_1,e_2,e_3,e_4\) be the standard basis of \(\mathbb R^4\); put \(d_{ij}=e_i-e_j\) and \(Z(g_1,\ldots,g_m)=\sum_i[0,g_i]\), the Minkowski sum of its generator segments. Fix
\[
G=(e_1,e_2,e_3,d_{24},d_{34}),\qquad
h_{a,b}=e_1-ae_2-be_3,\qquad
w=d_{14},\qquad w'=d_{23}.
\]
For **all real** \(a,b\ge0\), define \(A_{a,b}=Z(G,h_{a,b})\), \(B=[0,w]\), and \(C=[0,w']\). Write \(|\cdot|\) for ordinary four-dimensional Lebesgue volume; every \(A_{a,b}\) is full dimensional, since \(G\) already has rank four. The defect is \(\Delta=|A_{a,b}|\,|A_{a,b}+B+C|-|A_{a,b}+B|\,|A_{a,b}+C|\). Positive defect means failure of log-submodularity.

The specified family varies the two independent **directions** of the non-coordinate components of the special generator, while holding its first component at one. It is not the previously published single-parameter scalar rescaling \(s(e_1-e_2-e_3)\); the two deformations coincide only at their common special direction after fixing the scalar normalization.

## Proof
**Exact volumes.** For any finite list of four-dimensional vectors spanning \(\mathbb R^4\), the zonotope-volume identity is
\[
|Z(g_1,\ldots,g_m)|=\sum_{1\le i_1<i_2<i_3<i_4\le m}|\det(g_{i_1},g_{i_2},g_{i_3},g_{i_4})|.
\]
One may enumerate four-minors after adjoining \(h_{a,b}\) to each of the four fixed generator lists \(G\), \((G,w)\), \((G,w')\), and \((G,w,w')\). Minors not containing \(h_{a,b}\) sum respectively to \(4,12,8,24\). For complete independent reproducibility, the nonzero signed determinants of minors **containing** \(h_{a,b}\), with multiplicity, are:

| Fixed list | Nonzero minors with \(h_{a,b}\), recorded as value (multiplicity) |
| --- | --- |
| \(G\) | \(1\) (2), \(-1\) (2), \(a\) (2), \(-b\) (2), \(-(a+b)\) (1) |
| \((G,w)\) | \(1\) (3), \(-1\) (2), \(a\) (5), \(-b\) (5), \(-(a+b)\) (1), \(a-1\) (1), \(1-b\) (1), \(1-a-b\) (1) |
| \((G,w')\) | \(1\) (6), \(-1\) (2), \(a\) (2), \(-b\) (2), \(a+b\) (2), \(-(a+b)\) (1) |
| \((G,w,w')\) | \(1\) (9), \(-1\) (2), \(a\) (5), \(-b\) (5), \(a+b\) (3), \(-(a+b)\) (1), \(a-1\) (1), \(1-b\) (1), \(1-a-b\) (3) |

All omitted minors vanish identically; the list may also be regenerated using the accompanying exact rational determinant code. Since \(a,b\ge0\), sum of absolute determinants produces
\[
\begin{aligned}
|A_{a,b}|&=8+3q,\\
|A_{a,b}+B|&=17+6q+X+Z,\\
|A_{a,b}+C|&=16+5q,\\
|A_{a,b}+B+C|&=35+9q+X+3Z.
\end{aligned}
\]
These formulas are identities on the **entire closed quadrant**, not numerical fits or asymptotics.

**Defect and signs.** Multiply the first and fourth volumes, subtract the product of the second and third, and collect the terms in \(q,X,Z\):
\[
\Delta=8-4q-3q^2-(8+2q)X+(8+4q)Z.
\]
To split the quadrant into sign chambers, note that when \(a,b\le1\), we have \(X=2-q\), and when \(a,b\ge1\), we have \(X=q-2\). In the first case \(Z=1-q\) for \(q\le1\), and \(Z=q-1\) for \(q\ge1\). In the second case necessarily \(q\ge2\) and \(Z=q-1\). In either mixed case, \(X=|a-b|\) (because the larger coordinate is at least one and the smaller at most one), and \(Z=q-1\). Direct substitution yields the four polynomials listed in the Finding section. On the second chamber \(3q^2+4q-16\) strictly increases for \(q\ge1\) and vanishes at \(\frac23(\sqrt{13}-1)\). On the third chamber \(16-4q-q^2\) strictly decreases for \(q\ge2\) and vanishes at \(2(\sqrt5-1)\). The other signs follow immediately by factorization and comparison. The chambers cover all \(a,b\ge0\); shared boundaries give consistent formulas.

**Dimensional lift.** For any integer \(d\ge4\), embed the four-dimensional generators in the first four coordinates and adjoin segments \([0,e_5],\ldots,[0,e_d]\) to \(A_{a,b}\) only. Each of the four resulting zonotopes is a Cartesian product of its original counterpart with \([0,1]^{d-4}\). Every relevant \(d\)-dimensional volume equals its four-dimensional counterpart, proving the same defect and phase diagram in all these dimensions.

## Verification
Running \(`python verify.py`\) computes all maximal determinants exactly via rational arithmetic, independently of the displayed closed formulas, and checks all four volumes and all chamber branches on a grid of \(144\) rational parameter pairs, including chamber boundaries. The expected output is \(`VERIFY_OK 144 exact rational full determinant cases, including all chamber boundaries`\). The proof of the **continuous, infinite** phase classification is the symbolic determinant-minor decomposition and exact sign analysis above, not the finite parameter grid.

## Relationship to prior work
Skorupinski (arXiv:2608.07702v1, August 7, 2026, Section 3) introduced the exact underlying fixed generators and the special point \(h_{1,1}\), finding the four volumes \((14,30,26,56)\); his full available text contains the isolated example, not the two-parameter directional sign classification. A separately published *Exact scale phase diagram for a four-dimensional zonotope log-submodularity defect* derives the one-dimensional scalar ray \(s(1,-1,-1,0)\), with defect \(4s(2-s)\). That ray changes the first coordinate and both negative components together; it does not imply the sign for normalized vectors \((1,-a,-b,0)\) with independently varied \(a,b\), or the present distinct transition curves.

Averkov--von Dichter--Soprunov (arXiv:2608.14909v1) prove a different universal zonoid inequality and a sharp bound on the generator-count regime where the original log-submodularity claim is guaranteed. Their theorem says which classes can have violations, not which directions in this particular six-generator family do. Fradelizi--Hubard--Manui--Ndiaye--Wang--Zvavitch (arXiv:2608.12681v1) relate the global inequality to the Rayleigh property of volume polynomials, but their accessible abstract does not settle the present explicit directional phase. The determinant-volume formula itself is classical and used for the proof; its existence alone does not state the three nontrivial directional frontiers computed here.

## Limitations
The exact classification concerns this normalized nonnegative two-parameter family, not arbitrary zonotope generators, general zonoids, negative \(a\) or \(b\), or all possible segment directions. The extension to higher dimensions is via unit-cube products only. Finite computer checks supplement but do not establish the continuum claim. Originality comparisons are bounded by the available primary literature and public indexes; an uncatalogued equivalent calculation could exist. The Fradelizi et al. manuscript was available in an abstract-level view, not a complete material comparison, and is not claimed to be thoroughly excluded from overlap.

## References
1. R. Skorupinski, *Zonoid volumes are not log-submodular*, arXiv:2608.07702v1 (August 7, 2026), especially Section 3. https://arxiv.org/abs/2608.07702
2. *Exact scale phase diagram for a four-dimensional zonotope log-submodularity defect*, published research note, identifier `75844497-da3f-49e5-89b5-90bfcd3f3d1f` (October 2026).
3. G. Averkov, K. von Dichter, I. Soprunov, *On the Log-submodularity for zonoids: from Mixed Volume inequalities to the Hypercube*, arXiv:2608.14909v1 (August 14, 2026). https://arxiv.org/abs/2608.14909
4. M. Fradelizi, A. Hubard, A. Manui, C. S. Ndiaye, S. Wang, A. Zvavitch, *Volume and Projection Inequalities I: Zonoids and Courtade's Conjecture*, arXiv:2608.12681v1 (August 13, 2026). https://arxiv.org/abs/2608.12681
