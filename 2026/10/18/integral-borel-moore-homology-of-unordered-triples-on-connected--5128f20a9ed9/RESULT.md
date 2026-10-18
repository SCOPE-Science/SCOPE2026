# Integral Borel–Moore homology of unordered triples on connected graphs

## Finding
Let \(G\) be any finite connected graph regarded as a one-dimensional compact CW complex, and write \(b=\operatorname{rank}H_1(G;\mathbb Z)\). Let
\[
U_3(G)=\{\{x_1,x_2,x_3\}\subset |G|:x_1,x_2,x_3\text{ are pairwise distinct}\}
\]
be its space of three **unordered**, collision-free points. Its integral Borel–Moore homology is completely determined by \(b\):
\[
H_i^{\mathrm{BM}}(U_3(G);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{\,b(b^2+5)/6},&i=3,\\
\mathbb Z^{\,b}\oplus(\mathbb Z/2\mathbb Z)^{\binom b2},&i=2,\\
0,&i\notin\{2,3\}.
\end{cases}
\]
For \(b=0\), all these groups vanish. For \(b\ge2\), there are exactly \(\binom b2\) independent order-two classes in degree two. In particular, the complete answer at cycle rank two is \(H_3^{\mathrm{BM}}\cong\mathbb Z^3\) and \(H_2^{\mathrm{BM}}\cong\mathbb Z^2\oplus\mathbb Z/2\mathbb Z\).

## Assumptions and scope
Graph edges are interpreted as closed unit intervals attached to vertices; multiple edges and loops are permitted, although the theorem also applies to simple graphs. The graph is finite and connected, and may be a single vertex. All homology groups in this statement use integral **Borel–Moore** chains, not ordinary singular homology of the noncompact configuration space. The one-point compactification is employed only after taking the space of collision-free *unordered* triples.

Write \(\operatorname{Sym}^3(X)=X^3/S_3\) for the third symmetric product of a compact space \(X\), and let \(A(X)\) be the image of the fat diagonal \(\{(x_1,x_2,x_3):x_i=x_j\text{ for some }i\ne j\}\). Thus \(U_3(X)=\operatorname{Sym}^3(X)\setminus A(X)\). Since \(A(X)\) is closed, the one-point compactification of \(U_3(X)\) is \(\operatorname{Sym}^3(X)/A(X)\), and
\[
H_*^{\mathrm{BM}}(U_3(X);\mathbb Z)
\cong H_*(\operatorname{Sym}^3(X),A(X);\mathbb Z).
\]

## Proof
**1. Reduction to a rose is valid for the compactified problem.** If \(f:X\to Y\) is a homotopy equivalence of compact spaces, then \(\operatorname{Sym}^3(f)\) maps the repeated-coordinate subspace \(A(X)\) into \(A(Y)\). A homotopy \(H_t\) similarly induces the homotopy of *pairs* \(\operatorname{Sym}^3(H_t)\). Consequently the pairs \((\operatorname{Sym}^3(X),A(X))\) and \((\operatorname{Sym}^3(Y),A(Y))\) are homotopy equivalent. Every finite connected graph is homotopy equivalent to the rose \(R_b=\bigvee_{i=1}^{b}S^1\). This statement does not require, and does not assert, a homotopy equivalence of the uncompactified configuration spaces themselves.

**2. Relative cells for the rose.** Give every petal a chosen orientation and let \(v\) be the common vertex. A collision-free unordered triple has either no point at \(v\), or exactly one point there. In the first case a cell is indexed by a weak composition \(m=(m_1,\ldots,m_b)\) of three, recording the numbers of points in the interiors of the petals; it is a product of open simplices and has dimension three. In the second case it is indexed by a weak composition \(n=(n_1,\ldots,n_b)\) of two and has dimension two. Boundaries in which two particles collide are collapsed to the point at infinity. The compactified relative chain complex therefore has only
\[
C_3\cong\mathbb Z^{\binom{b+2}{3}},\qquad
C_2\cong\mathbb Z^{\binom{b+1}{2}},
\]
with no lower-dimensional relative cells. This cell decomposition is the quotient by free particle relabelings of the integral rose configuration-cell decomposition of Bibby, Chan, Gadish, and Yun (Lemma 2.4), or equivalently follows directly by ordering the interior coordinates of each petal.

**3. The exact signed boundary.** Give the product of ordered petal coordinates the orientation in increasing petal order. Denote by \(a_m\) the degree-three cell and by \(c_n\) the degree-two cell. The only surviving codimension-one faces of \(a_m\) arise when the *first* or *last* point in a nonempty petal reaches its endpoint \(v\). The first endpoint contributes the negative face sign; the last contributes the positive face sign, adjusted by its coordinate position. Therefore, if \(p_i=\sum_{j<i}m_j\),
\[
\partial_3 a_m=
\sum_{i:m_i>0}(-1)^{p_i}
\bigl((-1)^{m_i-1}-1\bigr)c_{m-e_i}.
\]
Here \(e_i\) is the \(i\)-th unit vector. When \(m_i\) is odd the two endpoint contributions cancel. When \(m_i=2\), their sum is \(\pm2\). Because \(\sum m_i=3\), at most one coordinate equals two. Thus the only nonzero columns are indexed by \(m=2e_i+e_j\) with distinct \(i,j\), and such a column is exactly \(\pm2c_{e_i+e_j}\). For each unordered pair \(\{i,j\}\), either of the two cells \(a_{2e_i+e_j}\) and \(a_{e_i+2e_j}\) provides such a nonzero column. Distinct unordered pairs have distinct target rows. All cells \(a_{3e_i}\) and \(a_{e_i+e_j+e_k}\) with distinct indices have zero boundary.

**4. Integral diagonal form.** Reordering the basis and subtracting one of the two nonzero columns for each unordered pair from the other gives an exact integral diagonal form with \(\binom b2\) diagonal entries of absolute value two and no other nonzero entries. These are unimodular column operations: no division by two is performed. Hence
\[
\operatorname{im}\partial_3
=\bigoplus_{i<j}2\mathbb Z\,c_{e_i+e_j}
\subset C_2.
\]
The remaining \(b\) basis elements \(c_{2e_i}\) contribute free degree-two classes, while the \(\binom b2\) mixed basis elements contribute elements of exact order two. The kernel is a free abelian group of rank
\[
\binom{b+2}{3}-\binom b2=\frac{b(b^2+5)}6.
\]
As there is no further differential, these are exactly the asserted Borel–Moore homology groups. For \(b=0\), the rose is a point and \(U_3(R_0)=\varnothing\), with zero homology.

## Verification
The included self-contained Python program `verify.py` independently builds the cellular boundary in two ways: from oriented endpoint incidence and from the labeled first-minus-last deletion formula. Their matrices agree up to reversing the chosen orientation of every top cell. For each \(1\le b\le15\) it performs exact integral column operations to diagonalize the boundary, checks rank over \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_7\), and compares free ranks and two-torsion multiplicities with the closed formulas. It additionally reproduces the published unordered **two**-particle Borel–Moore groups as a normalization test and handles the rank-zero rose separately. It terminates with `ALL_CHECKS_OK`. Reproduce using `python3 verify.py` without third-party packages.

These tests verify the model on finite ranks; the proof above, not finite enumeration, establishes the result for every \(b\).

## Relationship to prior work
Khan's 2026 theorem computes the **two**-particle unordered integral Borel–Moore groups for connected graphs and explicitly identifies extension to more particles as a future direction. In contrast, the present theorem gives a complete **three**-particle integral classification, including new degree-two torsion. The proof uses a different, compactification-first reduction rather than assuming ordinary graph-configuration spaces are homotopy invariant.

Bibby, Chan, Gadish, and Yun (2023) give a general integral two-term cellular presentation for **ordered** compactified graph configurations. It underlies step 2 but does not state the evaluation of the integral coinvariant Smith form for unordered triples; that calculation is made in steps 3–4 here. Gadish and Hainaut (2024) develop rational compactly supported cohomology and representation-theoretic decompositions on wedges of spheres. Their rational results account for the possibility of the free ranks but do not distinguish the integral order-two groups above. No claim of priority over unexamined publications is made.

## Limitations
This result concerns exactly three unlabeled collision-free particles, and Borel–Moore homology with constant integral coefficients. It does not compute ordinary singular homology of \(U_3(G)\), the homotopy type of \(U_3(G)\), integral automorphism representations, or four-or-more-particle groups. Although the homology depends only on cycle rank, graph embeddings and ordinary particle-braid homology can retain more information. Literature coverage may be incomplete; the proof supplies an explicit closed-form calculation rather than a new general method to construct the known rose CW complex.

## References
1. Munawar Khan, *Borel–Moore Homology of 2-Particle Unordered Configuration Spaces of Graphs via Discrete Morse Theory*, arXiv:2608.18143v1, first public 2026-08-07, Theorem 3.4 and §4. https://arxiv.org/abs/2608.18143
2. Christin Bibby, Melody Chan, Nir Gadish, and Claudia He Yun, *Homology representations of compactified configurations on graphs applied to \(\mathcal M_{2,n}\)*, arXiv:2109.03302v6 (2023), Proposition 2.1 and Lemmas 2.4 and 2.6. https://arxiv.org/pdf/2109.03302
3. Nir Gadish and Louis Hainaut, *Configuration spaces on a wedge of spheres and Hochschild–Pirashvili homology*, Annales Henri Lebesgue 7 (2024), 841–902, §§4.2–4.3 and 5, DOI:10.5802/ahl.213. https://ahl.centre-mersenne.org/articles/10.5802/ahl.213/
