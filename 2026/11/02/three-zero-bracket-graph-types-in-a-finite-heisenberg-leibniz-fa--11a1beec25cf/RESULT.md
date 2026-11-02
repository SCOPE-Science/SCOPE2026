# Three zero-bracket graph types in a finite Heisenberg–Leibniz family

## Finding

Let \(q\) be any odd prime power, \(F=\mathbb F_q\), and \(c\in F^\times\). Define the three-dimensional, two-step nilpotent Leibniz algebra \(L_c=FX\oplus FY\oplus FZ\) by its only potentially nonzero basis brackets
\[
[X,Y]=Z,\qquad [Y,X]=cZ.
\]
The element-based **two-sided zero-bracket graph** \(\Gamma_c\) has vertex set \(L_c\), with an edge between distinct \(a,b\) precisely when **both** \([a,b]=0\) and \([b,a]=0\). This is not the directed, multiplicative-basis graph of an algebra.

Put \(m=q(q-1)\), \(N=q(q-1)^2\), and \(t=(q-1)/2\). Let \(\vee\) denote graph join and \(\sqcup\) disjoint union. There are exactly three graph forms:
\[
\begin{aligned}
\Gamma_{-1}&\cong K_q\vee\bigl((q+1)K_m\bigr),\\
\Gamma_1&\cong K_q\vee\bigl(2K_m\sqcup tK_{m,m}\bigr),\\
\Gamma_c&\cong K_q\vee\bigl(2K_m\sqcup NK_1\bigr)\quad(c^2\ne1).
\end{aligned}
\]
For fixed \(q\), these are distinct graph-isomorphism types whenever all three cases occur; the third exists if \(q\ge5\). In particular, **every** \(c\) with \(c^2\ne1\) produces the same labeled graph in the standard coordinate model, despite distinct Leibniz-algebra isomorphism classes.

The complete clique-counting polynomials \(P_c(z)=\sum_{j\ge0}f_j(\Gamma_c)z^j\), including the empty clique, are
\[
\begin{aligned}
P_{-1}(z)&=(1+z)^q\bigl((q+1)(1+z)^m-q\bigr),\\
P_1(z)&=(1+z)^q\bigl(2(1+z)^m+t(1+2mz+m^2z^2)-(t+1)\bigr),\\
P_c(z)&=(1+z)^q\bigl(2(1+z)^m+N(1+z)-(N+1)\bigr)\quad(c^2\ne1).
\end{aligned}
\]

For \(k\ge0\), let \(T_c(k)\) count ordered \(k\)-tuples \((a_1,\ldots,a_k)\in L_c^k\) such that \([a_i,a_j]=[a_j,a_i]=0\) for all \(i<j\); repeated entries are permitted only when they satisfy these conditions. For \(k=0\), \(T_c(0)=1\). For every \(k\ge1\),
\[
\begin{aligned}
T_{-1}(k)&=(q+1)q^{2k}-q^{k+1},\\
T_1(k)&=2q^{2k}-q^k+t\left(2kmq^{k-1}+\mathbf1_{k\ge2}k(k-1)m^2q^{k-2}\right),\\
T_c(k)&=2q^{2k}-q^k+N kq^{k-1}\quad(c^2\ne1).
\end{aligned}
\]
In the middle formula, the term involving \(q^{k-2}\) is defined to be zero when \(k=1\).

The two exceptional algebras have identical ordered two-sided commuting-pair counts but unequal triple counts:
\[
T_{-1}(2)=T_1(2)=q^5+q^4-q^3,
\qquad T_{-1}(3)-T_1(3)=q^3(q-1)^4>0.
\]
For \(c^2\ne1\), \(T_c(2)=4q^4-4q^3+q^2\).

Finally, for any \(c,d\in F^\times\),
\[
L_c\cong L_d\quad\Longleftrightarrow\quad d\in\{c,c^{-1}\}.
\]
For \(q\ge7\), the generic graph therefore represents exactly \((q-3)/2\) distinct Leibniz-algebra isomorphism classes. Over \(\mathbb F_7\), \(L_2\not\cong L_3\) but \(\Gamma_2=\Gamma_3\) on the common coordinate set. The three graph types also demonstrate that the element-based two-sided zero-bracket relation is not determined by isotopy of the underlying nonsingular bilinear forms.

## Assumptions and scope

All statements concern \(q=p^f\) with odd prime \(p\), \(f\ge1\), and \(c\ne0\). The zero-bracket graph is a simple, undirected graph on **all** elements, including the \(q\) central elements, and uses simultaneous left and right vanishing. It differs from the usual graph of a chosen multiplicative basis. The algebra need not be Lie unless \(c=-1\). The phrase “ordered pairwise commuting tuples” refers to conditions for distinct positions, not a requirement that every entry square to zero for \(k=1\).

## Proof

**1. Leibniz structure and center.** Every bracket lies in \(FZ\), and all brackets involving \(Z\) vanish, so all triple brackets are zero. Consequently both Leibniz identities hold, and \(L_c\) is two-step nilpotent. On \(V=L_c/FZ\), the bracket is represented by the invertible matrix
\[
B_c=\begin{pmatrix}0&1\\c&0\end{pmatrix}.
\]
Since \(c\ne0\), its two-sided radical is zero. Hence \(Z(L_c)=FZ\), of cardinality \(q\). Every central element is adjacent to every other vertex.

**2. Bracket equations.** For \(a=xX+yY+sZ\) and \(b=uX+vY+tZ\), the two vanishing conditions are exactly
\[
xv+cyu=0,\qquad uy+cvx=0. \tag{1}
\]
If \(c=-1\), these are equivalent to \(xv-yu=0\); the two nonzero projected vectors must span the same one-dimensional subspace of \(F^2\). There are \(q+1\) projective lines, each containing \(q-1\) nonzero projected vectors with \(q\) central lifts: a clique of size \(m\).

If \(c=1\), both equations become \(xv+yu=0\). Projective perpendicularity for this hyperbolic symmetric form fixes precisely the two isotropic coordinate axes. Every other line with slope \(r\in F^\times\) is paired with slope \(-r\). Since the characteristic is odd, the \(q-1\) nonzero slopes partition into \(t\) two-element pairs. On a fixed axis the \(m\) lifted nonzero vectors form a clique. For each other projective pair, every vertex of one line is adjacent to every vertex of the other, but no two vertices from the same line are adjacent, because \([a,a]=2xyZ\ne0\). This gives \(K_{m,m}\).

If \(c^2\ne1\), equations (1), considered as a system in \((u,v)\), have coefficient matrix
\[
\begin{pmatrix}cy&x\\y&cx\end{pmatrix}
\]
with determinant \((c^2-1)xy\). If \(xy\ne0\), only \((u,v)=(0,0)\) is allowed: every vertex over that projected vector is isolated after deleting the center. There are \((q-1)^2\) such nonzero vectors and \(q\) central lifts, or \(N\) isolated vertices. If \(xy=0\) and the projection is nonzero, (1) forces \(b\)'s projection onto the same coordinate axis, giving the two cliques of size \(m\). This establishes all graph decompositions without probabilistic assumptions.

**3. Clique polynomials.** The clique polynomial of \(K_a\) is \((1+z)^a\), that of \(K_{a,b}\) is \(1+(a+b)z+abz^2\), and that of \(K_1\) is \(1+z\). For disjoint unions, add these polynomials and subtract one for each extra connected component, because the empty clique was counted repeatedly. For a join with \(K_q\), multiply by \((1+z)^q\). Substitution gives the three displayed polynomials, including the empty-clique coefficient \(1\).

**4. Ordered tuples.** Any admissible tuple with a noncentral entry lies entirely in the center plus one noncentral graph component. The center-only tuples are therefore counted more than once and must be counted once. In an axis or alternating projective-line clique, all \(q+m=q^2\) entries (including the center) have zero self-bracket and can be used in any positions. A generic isolated vertex for \(c^2\ne1\) has nonzero self-bracket, so it can appear in only one position: \(kNq^{k-1}\) possible tuples with one such entry. In a symmetric hyperbolic \(K_{m,m}\) component, noncentral vertices cannot repeat within either part, so an admissible tuple contains at most one from each part; the contributions beyond center-only tuples are \(2kmq^{k-1}\) and, when \(k\ge2\), \(k(k-1)m^2q^{k-2}\). Summing the disjoint possibilities yields exactly the three formulas for \(T_c(k)\). Evaluating at \(k=2,3\) and simplifying yields the pair collision and the strictly positive triple gap \(q^3(q-1)^4\).

**5. Algebra isomorphisms.** Any Leibniz-algebra isomorphism preserves the center \(FZ\). On the two-dimensional quotient it induces \(P\in\operatorname{GL}_2(F)\), while on the center it multiplies by a nonzero scalar. Therefore the two nonsingular bilinear-form matrices are congruent up to a nonzero scalar. The asymmetry operator
\[
B_c^{-1}B_c^{\mathsf T}=\operatorname{diag}(c^{-1},c)
\]
is invariant under such a change up to similarity, and its eigenvalue multiset is therefore invariant. Hence \(\{c,c^{-1}\}=\{d,d^{-1}\}\), forcing \(d=c\) or \(d=c^{-1}\). Conversely, equality is tautological, and inversion is realized by interchanging \(X,Y\) and appropriately rescaling \(Z\), which changes the parameter from \(c\) to \(c^{-1}\). The \(q-3\) parameters outside \(\{1,-1\}\) fall into \((q-3)/2\) inversion pairs. For \(q=7\), \(\{2,4\}\ne\{3,5\}\), proving the stated counterexample.

The graph decompositions are nonisomorphic: after removing the unique universal central \(K_q\), the alternating case has \(q+1\) nontrivial cliques; the symmetric case contains \(t\) noncomplete connected \(K_{m,m}\) components; and the generic case has \(N\) isolated vertices. These distinctions persist for the stated odd-field parameters.

## Verification

The standalone file `verify.py` constructs every element of \(L_c\) over the prime fields of sizes \(3,5,7\), calculates every ordered bracket pair from the definition, and independently verifies component types, two-sided common annihilator sizes, clique coefficients through size three, and ordered tuple counts for lengths one, two, and three. Ten prime-field cases were checked. Four additional cases over \(\mathbb F_9\), implemented independently as \(\mathbb F_3[t]/(t^2+1)\), verify the component decomposition and two- and three-tuple counts in an extension field. For the \(q=7\) witness, it verifies literal equality of the two graph adjacency masks for \(c=2\) and \(c=3\), the pair-count collision at \(c=1,-1\), and the exact triple-count gap. Execute with `python verify.py` from a directory containing this file. These fourteen finite tests corroborate, but do not replace, the uniform symbolic proof for every odd prime power.

## Relationship to prior work

The classification of two-step nilpotent Leibniz algebras via bilinear forms, and the existence of the three-dimensional Heisenberg–Leibniz parameter family, are established in La Rosa–Mancini (first public preprint 2021). Those are not claimed as new here. La Rosa–Mancini–Nagy (2023) investigates isotopism classes, a weaker relation using separate linear maps on the two arguments; its general isotopism results do not determine a graph requiring one common vertex labeling in both argument positions. The basis-directed graph of Barreiro–Calderón–Lopes–Sánchez (2022) has basis vectors as vertices and tracks nonzero structure constants, unlike the element-level simultaneous-zero graph here. The asserted contribution is the full three-type graph classification, clique and tuple enumerators, and the precise loss of algebra-isomorphism information. General results on bilinear orthogonality are a residual priority risk.

## Limitations

Only the nonsingular off-diagonal two-dimensional bilinear forms are considered. Degenerate forms, higher-dimensional Leibniz central extensions, characteristic two, and directed one-sided zero-bracket relations are outside the theorem. An exhaustive check over small prime fields is not an infinite-field proof. Publication priority remains provisional and has not been independently certified; the displayed elementary equations provide a complete mathematical proof for the stated family but no claim of a general classification of finite Leibniz-algebra graphs is made.

## References

1. G. La Rosa and M. Mancini, *Two-step nilpotent Leibniz algebras*, arXiv:2106.12904, first version June 24, 2021; Linear Algebra and its Applications **637** (2022), 119–137. https://arxiv.org/abs/2106.12904
2. G. La Rosa, M. Mancini and G. P. Nagy, *Isotopisms of nilpotent Leibniz algebras and Lie racks*, arXiv:2302.08306, first version February 16, 2023. https://arxiv.org/abs/2302.08306
3. E. Barreiro, A. J. Calderón, S. A. Lopes and J. M. Sánchez, *Leibniz algebras and graphs*, Linear and Multilinear Algebra **71** (2023), 1994–2007, first online June 27, 2022. https://doi.org/10.1080/03081087.2022.2092048
