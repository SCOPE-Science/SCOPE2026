# Two-point counting-logic dichotomy for dual symplectic quadrangles

## Finding

Let \(q\ge3\) be an **odd prime power**. Let \(W(q)\) be the symplectic generalized quadrangle on the one-dimensional and totally isotropic two-dimensional subspaces of a nondegenerate four-dimensional alternating space over \(\mathbb F_q\), and let \(W(q)^*\cong Q(4,q)\) be its point-line dual. Regard their incidence graphs as vertex-coloured graphs with separate point and line colours. In each graph, mark two **distinct point vertices** with the same respective pair of fresh, distinct unary colours.

**Dichotomy.** The two marked incidence graphs are equivalent in two-variable first-order logic with counting, \(C^2\), **if and only if** the two marked points are collinear in both quadrangles. If the marked points are noncollinear in both, colour refinement distinguishes the marked graphs within **four refinement rounds**. If just one marked pair is collinear, the relation between the marks already distinguishes the graphs.

**Complete collinear-marking extension.** For any finite thick generalized quadrangle of order \((s,t)\), marking \(r\) distinct points on a single line with individual colours, where \(2\le r\le s+1\), yields exactly
\[
3r+2+3\mathbf 1_{r<s+1}
\]
stable one-dimensional colour-refinement classes. The partition is reached by the third round (the second if \(r=s+1\)), and its cell sizes and quotient incidence numbers depend only on \((s,t,r)\), not on the quadrangle. In particular, **even individually marking every point of a line** does not let \(C^2\) distinguish \(W(q)\) from its nonisomorphic dual for odd \(q\).

For two noncollinear marked points \(A,B\), write \(C=\{Z:Z\text{ is a point collinear with both }A\text{ and }B\}\). For a point \(X\) collinear with neither mark, define the *center count* \(c(X)=|\{Z\in C:Z\text{ is collinear with }X\}|\). There are exactly \(q^2(q-1)\) such points. Their center-count distributions are:

| Quadrangle | Center count | Number of points |
|---|---:|---:|
| \(W(q)\) | \(1\) | \((q-1)(q^2-1)\) |
| \(W(q)\) | \(q+1\) | \(q-1\) |
| \(W(q)^*\) | \(0\) | \(q(q-1)^2/2\) |
| \(W(q)^*\) | \(2\) | \(q(q^2-1)/2\) |

The center count is recovered by four rounds of refinement in the two-sorted incidence graph, and the supports \(\{1,q+1\}\) and \(\{0,2\}\) are disjoint for odd \(q\ge3\).

## Assumptions and scope

A finite generalized quadrangle of order \((s,t)\), with \(s,t\ge2\), has \(s+1\) points on each line and \(t+1\) lines through each point, with at most one joining line through any two points. For every point \(P\) off a line \(L\), exactly one point of \(L\) is collinear with \(P\). Points are *collinear* when they share a line; distinct points not sharing a line are *noncollinear*, also called opposite.

The incidence graph has an edge precisely for a point-line incidence, never between two points or two lines. Point and line sort colours are retained through every round. Marked point colours are distinguished from both sort colours and from each other. Colour refinement starts with this colouring at round zero and replaces a vertex colour by the ordered pair of its previous colour and the multiset of neighbouring previous colours at each round. The comparison of two graphs uses common colour labels and joint multisets.

The general collinear-marking theorem applies to **every** finite thick generalized quadrangle; the symplectic/dual separation and the explicit center-count distributions require odd prime-power order. The two graphs have identically named point/line sorts, not an isomorphism that swaps the sorts.

## Proof

**1. The universal linewise quotient.** Fix a line \(L\), let \(S=\{P_1,\ldots,P_r\}\subseteq L\) be the individually marked points, and set \(R=L\setminus S\). Every point \(X\notin L\) has a unique *foot* \(\pi_L(X)\in L\), the unique point of \(L\) collinear with \(X\). Define point cells \(\{P_i\}\), \(R\),
\[
X_i=\{X\notin L:\pi_L(X)=P_i\},\qquad
X_R=\{X\notin L:\pi_L(X)\in R\}.
\]
The cells involving \(R\) are omitted if \(R\) is empty. Define line cells \(\{L\}\), \(Y_i\) (the \(t\) lines through \(P_i\) other than \(L\)), \(Y_R\) (the lines through points in \(R\) other than \(L\)), and \(Z\) (the lines disjoint from \(L\)). The sizes are
\[
|X_i|=st,\quad |X_R|=|R|st,\quad |Y_i|=t,\quad
|Y_R|=|R|t,\quad |Z|=st^2.
\]
Indeed each of the \(t\) lines through a foot other than \(L\) contains \(s\) off-line points, and distinct off-line points have unique feet. There are \((st+1)(t+1)\) lines altogether.

The complete nonzero quotient-incidence counts are as follows. Each \(P_i\) meets \(L\) once and \(Y_i\) in \(t\) lines; each point in \(R\) meets \(L\) once and \(Y_R\) in \(t\) lines; each point in \(X_i\) meets \(Y_i\) once and \(Z\) in \(t\) lines; each point in \(X_R\) meets \(Y_R\) once and \(Z\) in \(t\) lines. Conversely \(L\) meets every marked point and all of \(R\); each \(Y_i\) contains \(P_i\) and \(s\) members of \(X_i\); each \(Y_R\) contains one point of \(R\) and \(s\) members of \(X_R\); and each \(Z\) contains exactly one member of each \(X_i\) and \(|R|\) members of \(X_R\). The last assertion holds because projecting the points of a line disjoint from \(L\) to \(L\) is injective by the generalized-quadrangle axiom, hence bijective.

These counts prove that the proposed partition is equitable and that its quotient and sizes depend only on \((s,t,r)\). It is **exactly** the stable refinement partition: in round one the individually coloured marks distinguish \(L\), each \(Y_i\), and the remaining lines; in round two these line colours distinguish \(R\), each \(X_i\), and \(X_R\), while in round three the points in \(R\) distinguish \(Y_R\) from \(Z\). When \(R=\varnothing\), this last split is unnecessary. As \(r\ge2\), the uniquely marked common line \(L\) is already visible at round one. Thus there are exactly \(r+\mathbf1_{R\ne\varnothing}+r+\mathbf1_{R\ne\varnothing}+1+r+\mathbf1_{R\ne\varnothing}+1=3r+2+3\mathbf1_{R\ne\varnothing}\) cells.

The equitable quotient and all initial colour multiplicities coincide for any two such marked generalized quadrangles with equal parameters. Inductively their canonical refinement colours have identical multiplicities at every round. By the standard colour-refinement/\(C^2\) correspondence, they are \(C^2\)-equivalent. Taking \((s,t)=(q,q)\) proves the collinear half of the dichotomy, including the full-line assertion.

**2. The center count is visible to two-variable counting logic.** For two noncollinear marked points \(A,B\), the generalized-quadrangle axiom gives exactly \(q+1\) common collinear points, forming \(C\). The point set \(C\) is independent: two distinct points of \(C\) cannot lie on the same line, since the external point \(A\) or \(B\) would then be collinear with two points on that line. Initial refinement first detects the lines through each named point, then (at round two) exactly the points collinear with both named points, hence \(C\). At round three it detects lines meeting \(C\), among other line colours. At round four every point \(X\) noncollinear with \(A,B\) has its number of incident \(C\)-meeting lines encoded in its colour. Since \(C\) is independent, a line contains at most one member of \(C\), so that number is exactly \(c(X)\). All these properties are expressible using only two variable names, alternating point and line quantification with unary mark predicates and counting quantifiers.

**3. The symplectic center-count spectrum.** Write the nondegenerate alternating form as \(\beta\) on a four-dimensional \(\mathbb F_q\)-vector space \(V\). Points of \(W(q)\) are its one-spaces; two distinct points are collinear in \(W(q)\) precisely when their representatives are orthogonal under \(\beta\). For noncollinear \(A,B\), the two-dimensional subspace \(U=\langle a,b\rangle\) is nondegenerate. Among the \(q^2(q-1)\) points \(X\) opposite both marks, the \(q-1\) other projective points of \(U\) all have \(c(X)=q+1\): their common orthogonal subspace is the two-space \(U^\perp\). Every remaining \(X\) is linearly independent of \(a,b\), so the common orthogonal subspace has dimension one and gives exactly one projective point. Thus \(c(X)=1\) on the remaining \((q-1)(q^2-1)\) points.

**4. The dual center-count spectrum.** A point of \(W(q)^*\) is a totally isotropic two-dimensional vector subspace of \(V\). Two such points are opposite precisely when the corresponding projective lines are disjoint. Fix opposite points represented by complementary isotropic two-spaces \(U\) and \(U'\). The alternating form identifies \(U'\) with \(U^*\), so, after choice of coordinates,
\[
V=U\oplus U^*,\qquad
\beta((u,f),(v,g))=g(u)-f(v).
\]
A third isotropic two-space opposite both \(U\) and \(U^*\) is the graph \(\{(u,Tu):u\in U\}\) of an **invertible symmetric** linear map \(T:U\to U^*\). A common-neighbour point in the dual is a totally isotropic line meeting these three pairwise skew projective lines. A line meeting the first two has the form \(\langle(u,0),(0,f)\rangle\); to meet the third it must have \(f\) proportional to \(Tu\). Thus common-neighbour points correspond to projective roots
\[
[u]\in\mathbb P(U)\quad\text{of}\quad (Tu)(u)=0.
\]
Because \(q\) is odd and \(T\) is nonsingular symmetric, this is a nondegenerate binary quadratic form, with **zero or two**, never one or \(q+1\), projective roots. Hence \(c(X)\in\{0,2\}\) for every \(X\) opposite both marks in the dual.

To obtain the exact multiplicities, there are \(q^2(q-1)\) such \(X\) in either order-\((q,q)\) quadrangle. Each of the \(q+1\) common neighbours \(Z\in C\) is collinear with exactly \(q(q-1)\) eligible \(X\): take its \(q-1\) lines other than the two through \(A\) and \(B\), each with \(q\) further points. Therefore
\[
\sum_X c(X)=q(q-1)(q+1).
\]
Writing \(N_2\) and \(N_0\) for the dual multiplicities and using \(2N_2=q(q-1)(q+1)\) and \(N_0+N_2=q^2(q-1)\) gives the two displayed formulas.

Since \(q+1\ge4\), the symplectic and dual center-count supports are disjoint; round-four refinement distinguishes any two **opposite** marked pairs. If exactly one pair is collinear, an incident line through both marked points exists in exactly one structure, which refinement already detects. This completes the dichotomy. The triad center-count discrepancy also proves that \(W(q)\) and its dual are nonisomorphic as point-line-sorted incidence structures for odd \(q\).

## Verification

Two standalone checking programs are provided with the exact source and deterministic outputs. Run `python check_incidence.py` and `python check_quadratic.py` from the directory containing the files, using a standard Python 3 implementation. In `check_incidence.py`, point and line sets are constructed directly from a symplectic form over prime fields \(q=3,5,7\); their incidence duals are constructed by transposing incidence. The program checks the full claimed center-count spectra, equal joint-refinement colour histograms for collinear marked sets of sizes \(2,3,q,q+1\), unequal histograms for noncollinear pairs, and the predicted number of collinear stable classes. In `check_quadratic.py`, every invertible symmetric two-by-two matrix is enumerated for prime fields \(q=3,5,7,11,13\) and checked for exactly zero or two projective roots, in agreement with its determinant/discriminant. All tests passed; saved results are `check_incidence.out` and `check_quadratic.out`.

For example, at \(q=3\) and a noncollinear marked pair the center-count multisets are \(\{1^{16},4^2\}\) for \(W(3)\) and \(\{0^6,2^{12}\}\) for its dual. With two collinear marks both graphs stabilize at exactly eleven classes. At \(q=5\), the spectra are \(\{1^{96},6^4\}\) and \(\{0^{40},2^{60}\}\), respectively.

These finite calculations corroborate the incidence and quadratic lemmas but are not used as substitutes for their all-prime-power proofs. The programs do not implement arbitrary extension-field arithmetic; the proof does not rely on that restriction.

## Relationship to prior work

Brouns, Thas and Van Maldeghem discuss the standard notion of triad centers and explicitly cite the classical **zero-or-two center** property of \(Q(4,q)\) for odd \(q\) (their Section 3, referring to Payne–Thas). Their result does **not** assert the present refinement dichotomy, stable linewise quotient, or the refinement-round threshold. The center property itself is **not claimed as new** here.

Ball and Weiner's finite-geometry notes establish the generalized-quadrangle incidence axioms, the numbers of points and lines, the relation between \(W(3,q)\) and \(Q(4,q)\), and moment identities for center-count distributions (Section 4.1, Proposition 4.1.4). Those moment identities alone do not determine the different supports for the two families; the symplectic/dual linear-algebra arguments above do. The standard counting-logic/colour-refinement correspondence and individualization framework appear in Arvind, Köbler, Rattan and Verbitsky (2015). The present synthesis is the **exact two-landmark collinearity-dependent logical comparison** of an infinite dual pair, together with the universal all-line-marking blindness result.

The closest relevant finite-model-theoretic incidence results known to this study concern marked points in projective planes, Steiner designs and affine planes. They have different incidence axioms: in particular, they do not imply the symmetric-bilinear quadratic-form split for opposite symplectic lines. No claim of independent priority certification is made.

## Limitations

This theorem concerns one-dimensional colour refinement and its equivalent \(C^2\) sentences, not higher-dimensional Weisfeiler–Leman algorithms or all graph isomorphism tests. It applies to point-line-sorted incidence graphs; allowing a priori uncoloured point-line exchange changes the comparison problem. The sharp dichotomy is proved only for odd prime powers: at even order, symplectic and parabolic quadrangles are self-dual and this separation phenomenon does not occur. The universal collinear part holds for every finite thick generalized quadrangle, but the opposite-pair center spectra are established specifically for the stated classical pair. Prior literature already contains geometric triad-center facts; originality and relevance of the new logical formulation remain subject to future independent scrutiny.

## References

1. L. Brouns, J. A. Thas and H. Van Maldeghem, “A Characterization of \(Q(5,q)\) Using One Subquadrangle \(Q(4,q)\),” *European Journal of Combinatorics* **23** (2002), 163–177, DOI: 10.1006/eujc.2001.0554. Lawfully accessible author PDF: https://cage.ugent.be/~hvm/artikels/113.pdf. See p. 3 for the established center-count property.
2. S. Ball and Z. Weiner, *An Introduction to Finite Geometry*, dated 5 September 2011, especially Section 4.1, Proposition 4.1.4, and Section 4.3. https://web.mat.upc.edu/simeon.michael.ball/IFG.pdf.
3. V. Arvind, J. Köbler, G. Rattan and O. Verbitsky, “Graph Isomorphism, Color Refinement, and Compactness,” initial public arXiv submission 4 February 2015, arXiv:1502.01255. https://arxiv.org/abs/1502.01255.
4. V. Arvind, F. Fuhlbrück, J. Köbler, S. Kuhnert and G. Rattan, “The Parameterized Complexity of Fixing Number and Vertex Individualization in Graphs,” initial public arXiv submission 14 June 2016, arXiv:1606.04383. https://arxiv.org/abs/1606.04383.
