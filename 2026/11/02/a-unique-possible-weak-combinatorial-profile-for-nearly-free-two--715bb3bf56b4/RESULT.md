# A unique possible weak-combinatorial profile for nearly free two-conic five-line arrangements

## Finding
Let \(\mathcal A\subset\mathbb P^2_{\mathbb C}\) consist of precisely two distinct smooth conics and five distinct lines. Suppose that every singularity is an ordinary node \(A_1\), an ordinary tacnode \(A_3\), or an ordinary transverse triple point \(D_4\). If \(\mathcal A\) is nearly free, then its numbers of singularities satisfy
\[
\boxed{(n_2,t,n_3)=(0,5,8).}
\]
Moreover the five-line subarrangement has either exactly one or exactly two triple points. In the one-triple case, exactly seven of the arrangement's triple points contain two lines and a conic, and none contain two conics and a line. In the two-triple case, these two respective counts are four and two. This is a **necessary condition**, not an existence assertion for the remaining configuration.

In fact the following two geometric exclusions hold without assuming nearly freeness: no arrangement of two smooth conics and five distinct lines with only the prescribed singularities has \((n_2,t,n_3)=(2,7,6)\) or \((1,6,7)\).

## Assumptions and scope
We work over \(\mathbb C\). A node is the transverse intersection of two smooth branches; a tacnode is the intersection of two smooth branches with local intersection multiplicity two; an ordinary triple point consists of three pairwise transverse smooth branches. No component is repeated, and no singularities of other types, including quadruple points, are allowed. Numbers count geometric singular points rather than incidences or component-isomorphism classes. 'Nearly free' is the usual condition that the saturation defect module of the reduced defining equation has every graded piece of dimension at most one and is nonzero.

## Proof
**1. Necessary numerical possibilities.** The arrangement has total degree nine. The published lower bound \(\operatorname{mdr}\geq 2m/3-2\), together with the nearly-free exponent relation \(d_1+d_2=m\), forces exponents \((d_1,d_2)=(4,5)\). The standard nearly-free Tjurina formula gives \(\tau=47\). Bézout's pair-incidence identity and \(\tau=n_2+3t+4n_3\) read
\[
n_2+2t+3n_3=34,\qquad n_2+3t+4n_3=47.
\]
Thus \(t+n_3=13\) and \(n_2+n_3=8\). The published inequality \(8k+n_2+\frac34 n_3\geq d+\frac52 t\), with \(k=2\), \(d=5\), gives \(n_3\geq6\). Therefore the three candidates are \((2,7,6)\), \((1,6,7)\), and \((0,5,8)\). We exclude the first two geometrically.

**2. Local parity and triple counting.** Denote by \(x\), \(y\), \(z\) the numbers of ordinary triple points involving, respectively, three lines; two lines and one conic; one line and two conics. Let \(s\) be the number of line-line nodes. Every pair of lines has a unique intersection, so
\[
3x+y+s=10,\qquad x+y+z=n_3.
\]
Three distinct triple points of three lines cannot occur among five distinct lines: two triples of three lines must share exactly one line, after which a third cannot contain three lines while sharing at most one line with each preceding triple. Hence \(x\leq2\).

For a chosen line \(L\), let \(b_L\) count all line-line nodes incident with \(L\), and \(c_L\) all line-conic nodes incident with \(L\). Counting intersections of \(L\) with the other four lines and then with the two conics yields
\[
4=2x_L+y_L+b_L,\qquad 4=y_L+2z_L+c_L+2t_L.
\]
Consequently \(b_L\equiv c_L\pmod2\). If there are at most two nodes in total, no node may be line-line: one line-line node has two distinct odd-degree endpoints, which cannot both be repaired by at most one additional node, and two distinct line-line nodes likewise leave an odd-degree endpoint. Hence a single node must be conic-conic. If there are two nodes, either both are conic-conic or both are line-conic at the same line. In the latter case, counting intersections of each conic with all five lines modulo two shows that both nodes belong to the same conic whenever \(z=0\).

**3. Exclusion of \((1,6,7)\).** The unique node must be conic-conic, hence \(s=0\). The two displayed counts give \(z=2x-3\). With \(x\leq2\), we get \((x,y,z)=(2,4,1)\). But for either conic, its total intersection multiplicity with the five lines is ten. Each two-line/one-conic triple point contributes two, each one-line/two-conic triple point contributes one, and every line-conic tacnode contributes two. There are no line-conic nodes. Thus ten is congruent to \(z=1\) modulo two, a contradiction.

**4. Exclusion of \((2,7,6)\).** By the node parity argument, \(s=0\). Therefore \(3x+y=10\) and \(z=2x-4\); hence \((x,y,z)=(2,4,0)\). The two three-line triples share exactly one line. Up to projective equivalence, write the five lines as
\[
Z=0,\quad X=0,\quad X-Z=0,\quad Y=0,\quad Y-Z=0.
\]
Their remaining four pairwise intersections form the corners \((0,0),(0,1),(1,0),(1,1)\) in the affine chart \(Z=1\). Each corner is a two-line/one-conic triple point. Every conic-coloring of the four corner incidences has even degree at each of the four finite lines: this follows from their intersection number two with each conic, because the two nodes are either conic-conic or belong to one conic on one line, and \(z=0\). Since the four corners form a four-cycle, the only edge colorings even at every vertex are monochromatic. Thus one conic, \(Q\), contains all four corners, and the other, \(R\), contains none of them.

A conic through all four corners has equation
\[
\alpha X(X-Z)+\beta Y(Y-Z)=0.
\]
If it is smooth, \(\alpha\beta\ne0\). Its intersection with \(Z=0\) is then given by \(\alpha X^2+\beta Y^2=0\), which has two distinct points over \(\mathbb C\). In particular, \(Q\) cannot be tangent to the shared line \(Z=0\).

If both nodes are conic-conic, then \(R\) must be tangent to all five lines. This is impossible because three of those lines concur and a smooth conic has at most two tangent lines passing through any given point. If the nodes are line-conic nodes, they lie on one line and the same conic. When that line is one of the four finite lines, the nodes cannot belong to \(Q\), which already has two corner intersections on it. Therefore they belong to \(R\), which must then be tangent to the other four lines; those four include three concurrent lines, again impossible. When both nodes lie on \(Z=0\), either they belong to \(Q\) and \(R\) would be tangent to all five lines, or they belong to \(R\) and \(Q\) would be tangent to \(Z=0\). Both cases are impossible. This completes the exclusion.

**5. Remaining incidence types.** The only numerical possibility is \((0,5,8)\). Here \(s=0\), so \(3x+y=10\) and \(x+y+z=8\), whence \(z=2x-2\). With \(x\le2\) and \(z\ge0\), exactly \((x,y,z)=(1,7,0)\) or \((2,4,2)\) remains. No realizability or nearly-freeness of either type is asserted.

## Verification
The accompanying standalone script `verify_cases.py` checks all numerical candidates using exact rational arithmetic, checks the line-node parity restrictions by a finite enumeration of node supports, enumerates the even two-colorings of the four-cycle, and symbolically verifies that a smooth conic through the four normalized corners cannot be tangent to \(Z=0\). These computations corroborate individual finite reductions; the theorem is proved by the arguments above, not extrapolation from the script.

## Relationship to prior work
Gałecka (2022), arXiv:2204.13969, establishes the numerical inequalities, the degree restriction and the open degree-eight/nine existence question; this proof takes those statements as inputs but narrows the two-conic/five-line degree-nine possibility further. Dimca and Pokora (2021), arXiv:2111.12349, classify **free**, as opposed to nearly free, conic-line arrangements and exclude free five-line arrangements. Their free result does not imply this necessary weak-combinatorial classification of nearly free arrangements. Golla and Pokora (2026), arXiv:2610.12192, prove general topological inequalities and congruences, but the explicitly inspected odd-arrangement hypotheses require odd multiplicity sequences, a condition not met by the node/tacnode candidates excluded here.

## Limitations
The remaining zero-node profile may or may not be geometrically realizable, and even a realization need not be nearly free. The result does not settle all degree-nine conic-line component compositions or the overall existence problem. No independent mathematical audit has been performed. The possibility of a logically equivalent unpublished or unindexed prior case analysis remains.

## References
1. A. Gałecka, *On the nearly freeness of conic-line arrangements with nodes, tacnodes, and ordinary triple points*, arXiv:2204.13969 (first publicly submitted 29 April 2022); *Bol. Soc. Mat. Mex.* **28**, 67 (2022), DOI 10.1007/s40590-022-00461-4. Relevant sections 2–5, especially Proposition 4.4 and the degree-nine gap.
2. A. Dimca and P. Pokora, *On conic-line arrangements with nodes, tacnodes, and ordinary triple points*, arXiv:2111.12349 (first publicly submitted 24 November 2021); *J. Algebraic Combin.* **56**, 403–424 (2022), DOI 10.1007/s10801-022-01116-3. Relevant sections 4–5 and Proposition 5.4 (the free five-line case).
3. M. Golla and P. Pokora, *Topological inequalities for conic-line arrangements with some prescribed singularities*, arXiv:2610.12192 (8 October 2026), especially §5 on odd arrangements.
