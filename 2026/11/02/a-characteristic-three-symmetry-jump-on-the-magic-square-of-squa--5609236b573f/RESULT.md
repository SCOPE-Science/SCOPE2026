# A characteristic-three symmetry jump on the magic-square-of-squares surface

## Finding

Let \(k\) be an algebraically closed field of characteristic \(p\neq2\), where \(p=0\) is allowed. In \(\mathbb P^8_k\), let \(X_k\) be the projective scheme whose nine homogeneous coordinates \(z_{ij}\), arranged as a three-by-three square, satisfy the condition that the three row sums, three column sums, and two diagonal sums of the **squares** \(z_{ij}^2\) are all equal. Equivalently, \(X_k\) is defined by the seven differences of these eight sums (of rank six).

**Theorem.** The scheme \(X_k\) is an integral normal complete-intersection surface of six quadrics and degree \(64\). Every geometric singularity is an ordinary double point, and its singular locus has exactly
\[
\#\operatorname{Sing}(X_k)=
\begin{cases}
384,&\operatorname{char}k=3,\\
256,&\operatorname{char}k=0\text{ or }\operatorname{char}k\ge5.
\end{cases}
\]
In characteristic three the projective automorphism group contains a faithful subgroup
\[
(\mathbb Z/2\mathbb Z)^8\rtimes\operatorname{AGL}_2(\mathbb F_3),
\qquad\#G=256\cdot432=110592,
\]
and this subgroup acts **transitively on all 384 singular points**. In particular, the characteristic-three surface has at least \(54\) times as many automorphisms in this explicit subgroup as the order-\(2048\) full geometric automorphism group established for the characteristic-zero surface. No assertion is made that the displayed subgroup exhausts the characteristic-three automorphism group.

## Assumptions and scope

The base field is algebraically closed, with characteristic different from two. The nine variables are square roots of the entries of a magic square, not the entries of the magic square itself. The scheme is the indicated homogeneous scheme, not merely its set of rational points. The group statement is a subgroup assertion in characteristic three. The node statement concerns geometric points and is not a count of rational points over any fixed finite field.

## Proof

**1. The plane of magic sums.** Write the eight row/column/diagonal sums as integer coefficient vectors in nine variables, ordered row-major. Subtract the first row-sum vector from each of the other seven. Six of the resulting vectors, those indexed \(0,1,2,3,5,6\) from zero, restricted to columns \(0,1,2,3,4,7\), have determinant \(1\). Thus the seven differences have rank at least six over every field. Lucas's classical three-parameter formula below shows their kernel has dimension at least three, hence rank exactly six in every characteristic.

For parameters \([u:v:w]\in\mathbb P^2\), the nine magic entries can be written in the order
\[
\begin{pmatrix}
w-v&u+v+w&w-u\\
w+v-u&w&w+u-v\\
w+u&w-u-v&w+v
\end{pmatrix}.
\]
These forms are exactly the nine forms \(\ell_{a,b}=w+au+bv\) with \((a,b)\in\{-1,0,1\}^2\), taken in a fixed order. The three coefficient columns are independent in every odd characteristic. Therefore they identify the magic-sum plane with \(\mathbb P^2_k\).

**2. The square-root cover and irreducibility.** The coordinatewise squaring map \(\sigma:\mathbb P^8_k\to\mathbb P^8_k\) is finite flat of degree \(2^8=256\). The scheme \(X_k\) is its fiber product with the linear magic-sum plane; consequently \(\pi:X_k\to\mathbb P^2_k\) is finite flat of degree \(256\). Over the locus on which all nine forms \(\ell_{a,b}\) are nonzero, it is an étale Galois cover with sign group \((\mathbb Z/2\mathbb Z)^9/\langle(-1,\ldots,-1)\rangle\cong(\mathbb Z/2\mathbb Z)^8\).

This cover is generically connected: fixing one form \(\ell_*\), the eight rational functions \(\ell_{a,b}/\ell_*\) for the other forms have independent classes modulo squares in the function field of the plane. Indeed, a purported nontrivial square relation has odd valuation along one of the eight distinct lines \(\ell_{a,b}=0\). Thus the generic extension has degree \(256\). Because the pullback is finite flat and generically integral, it is integral. It is a complete intersection of six quadrics, hence has degree \(2^6=64\).

**3. The branch-line incidence.** The nine branch lines in the plane are \(L_{a,b}:w+au+bv=0\). At a crossing of two or more lines, the line labels \((a,b)\) form a collinear subset of the three-by-three coefficient grid \(\{-1,0,1\}^2\). Three labels are collinear precisely when the corresponding three-by-three determinant vanishes in the base field.

The determinant is an integer of absolute value at most four. In characteristic zero, exactly eight label triples are collinear: three horizontal triples, three vertical triples, and the two principal diagonals of the grid. There are no quadruple intersections. The determinant bound implies that **every** characteristic at least five has the same eight triple crossings and, by counting the \(\binom92=36\) line pairs, twelve ordinary double crossings.

In characteristic three the label grid becomes the **entire affine plane** \(\mathbb F_3^2\). Its affine lines are exactly twelve three-element subsets, so the branch arrangement has precisely twelve distinct ordinary triple crossings and no double crossings or higher crossings. Equivalently, the nine branch lines are the nine projective \(\mathbb F_3\)-lines missing the point \([0:0:1]\), with each of the other twelve projective \(\mathbb F_3\)-points lying on exactly three of them.

**4. Local geometry and node counts.** The cover is étale away from the branch lines. Near a base point on exactly one branch line, its local form is a coordinate change \(s^2=x\), hence smooth. Near a crossing of exactly two lines it has two independent local square roots \(s^2=x\), \(t^2=y\), hence is also smooth.

At a triple crossing, choose two independent vanishing linear forms as local parameters \(x,y\). The third vanishing form is \(\alpha x+\beta y\), with \(\alpha,\beta\in k^*\) because the three lines are distinct. After trivializing any nonvanishing form and choosing étale square-root branches of the remaining nonzero forms, every point of the cover above the crossing has the completed local model
\[
 k[[s,t,r]]/(r^2-\alpha s^2-\beta t^2).
\]
As \(p\neq2\), its quadratic form is nondegenerate: each point is an \(A_1\) ordinary double point. The three vanishing square-root coordinates account for ramification index \(2^3\), so the degree-\(256\) cover has exactly \(256/8=32\) distinct geometric points over each triple crossing. Thus there are \(8\cdot32=256\) nodes in characteristic zero and characteristics at least five, and \(12\cdot32=384\) nodes in characteristic three. There are no other singularities. Since the complete intersection satisfies \(S_2\) and is regular in codimension one, it is normal.

**5. Extra automorphisms at three.** When \(p=3\), the nine labels \((a,b)\) run over all of \(\mathbb F_3^2\). Every affine transformation \(g(z)=Az+t\) with \(A\in\operatorname{GL}_2(\mathbb F_3)\) permutes the nine linear forms under a suitable dual linear change of \((u,v,w)\): the family \(w+au+bv\) is preserved as a set, with no additional scalar factors needed. Consequently, permuting the nine square-root coordinates by \(g\) preserves the defining six-dimensional space of quadratic equations. These permutations lift the order-\(432\) affine group and normalize the order-\(256\) coordinate-sign group. Their intersection is trivial, and their faithful semidirect product is the displayed subgroup of order \(110592\).

The affine group is transitive on the twelve affine lines in \(\mathbb F_3^2\), equivalently on the twelve triple branch points. The sign group acts transitively on the \(32\) geometric square-root choices above each triple point. Therefore their combined action is transitive on all \(12\cdot32=384\) nodes.

## Verification

Run `python3 verify.py` using only Python's standard library. It checks an explicit unit minor for the magic-square relation matrix; all \(\binom93=84\) integer triple determinants and their bound by four; the pair/triple incidence distributions in characteristics three, five, seven and over the rationals; and the full order-\(432\) affine permutation family and its transitivity on twelve affine lines. The expected final output starts with `VERIFY_OK`. These exhaustive finite certificates verify the combinatorial premises; the geometric flatness, irreducibility, local singularity type and transitivity implications are proved above rather than inferred from finite-field experiments.

## Relationship to prior work

Auel and Singer (2026), *The algebraic geometry of 3-by-3 magic squares of squares*, establish the characteristic-zero complete-intersection model, its \(256\) ordinary double points and the characteristic-zero geometric automorphism group of order \(2048\). Their treatment of the automorphism group explicitly uses characteristic zero; the characteristic-three degeneration is not a case of that theorem. Bruin, Thomas and Várilly-Alvarado (2019/2022) also establish the characteristic-zero node count and quasi-hyperbolicity. The present theorem studies **the reduction of the same integral model**: the affine-plane collinearity jump, the new ordinary-double-point count and a larger, node-transitive automorphism subgroup in characteristic three. The characteristic-zero node count is background, not claimed as new.

A thesis by Labruna (2018), *Magic Squares of Squares of Order Three Over Finite Fields*, discusses characteristic-three magic squares over finite fields; its abstract does not resolve the projective singularity and automorphism comparison, and the full thesis was not accessible for a complete priority comparison. This remains a historical-priority limitation, not evidence of uniqueness.

## Limitations

Characteristic two is excluded because coordinatewise squaring is inseparable. The result does not determine the entire characteristic-three automorphism group, its Picard group, or the number of points over individual finite fields. The full text of one relevant finite-field thesis was inaccessible, so historical originality is qualified. No independent mathematical audit has been performed.

## References

- A. Auel and B. Singer, *The algebraic geometry of 3-by-3 magic squares of squares*, arXiv:2609.09351 (first publicly submitted 2026-09-08), Sections 1.1–1.3 and Theorem 1.
- N. Bruin, J. Thomas, A. Várilly-Alvarado, *Explicit computation of symmetric differentials and its application to quasi-hyperbolicity*, arXiv:1912.08908 (first publicly submitted 2019-12-18), especially Theorem 1.5.
- G. Labruna, *Magic Squares of Squares of Order Three Over Finite Fields*, Montclair State University thesis (2018), abstract; full-text priority comparison outstanding.
