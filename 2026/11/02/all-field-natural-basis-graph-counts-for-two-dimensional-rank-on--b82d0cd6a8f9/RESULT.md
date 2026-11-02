# All-field natural-basis graph counts for two-dimensional rank-one evolution algebras

## Finding
Let \(k=\mathbb F_q\) be any finite field and let \(E\) be a two-dimensional, non-degenerate evolution \(k\)-algebra satisfying \(\dim_k E^2=1\). Choose any nonzero \(u\in E^2\) and write its multiplication uniquely as \(xy=B(x,y)u\), with \(B\) a nondegenerate symmetric bilinear form. Because \(E\) is an evolution algebra, \(B\) has an orthogonal basis. Define \(\epsilon(B)\) to be the number of one-dimensional isotropic subspaces of \(B\). Precisely,
\[
\epsilon(B)=\begin{cases}
1,&q\text{ even};\\
2,&q\text{ odd and }-\det B\text{ is a square in }k;\\
0,&q\text{ odd and }-\det B\text{ is a nonsquare in }k.
\end{cases}
\]
Here the determinant may be computed in any basis: its square class is invariant. Put \(m=q+1-\epsilon(B)\). Then the number of **ordered** natural bases of \(E\) is exactly \(m(q-1)^2\), and the number of natural bases up to scaling and reordering is exactly \(m/2\).

Each associated directed graph has two vertices and both vertices point to the same nonempty set of targets. Denote by \(G_{2,j}\) its isomorphism class when that set has cardinality \(j\), for \(j\in\{1,2\}\). If an ordered natural basis is sampled uniformly, the exact graph distribution is
\[
\Pr(G_{2,1})=\begin{cases}0,&B(u,u)=0,\\2/m,&B(u,u)\ne0,\end{cases}
\qquad
\Pr(G_{2,2})=1-\Pr(G_{2,1}).
\]
When \(B(u,u)\ne0\), **exactly one** natural-basis class up to scaling and reordering produces \(G_{2,1}\); the other \(m/2-1\) classes produce \(G_{2,2}\). When \(B(u,u)=0\), all classes produce \(G_{2,2}\).

A two-dimensional non-degenerate evolution algebra with one-dimensional square has a unique natural basis up to scaling and permutation if and only if either \(q=2\), or \(q=3\) and \(B\) is split. In particular these are exact small-field exceptions to the unrestricted field formulation of Corollary 2.7 in the accessible 2020 arXiv version of Boudi–Cabrera Casado–Siles Molina (subsequently published in 2022), which asserts that uniqueness requires linearly independent squares. Two explicit examples are: over \(\mathbb F_2\), \(e_1^2=e_2^2=e_1\); and over \(\mathbb F_3\), \(e_1^2=e_1,\ e_2^2=-e_1\), in each case with \(e_1e_2=0\). Both have unique natural bases up to scaling/reordering, though the squares are dependent. The inspected preprint proof of that corollary invokes the existence of a scalar outside the roots of a quadratic and explicitly assumes more than three field elements at the crucial step.

## Assumptions and scope
All vector spaces, algebras, scalars and bases are over the fixed finite field \(\mathbb F_q\); all algebra homomorphisms are \(\mathbb F_q\)-linear. "Non-degenerate" means \(\operatorname{Ann}(E)=0\). The condition \(\dim E^2=1\) means that \(E^2\) is the linear span of all products. The graph is the standard directed graph of a natural basis, with an arrow \(i\to j\) precisely when the coefficient of basis vector \(j\) in \(e_i^2\) is nonzero; loops are retained. An ordered natural basis is an ordered pair of independent vectors whose product is zero. Scaling/reordering means applying independent elements of \(k^\times\) and swapping the two basis vectors. The scalar \(u\) is any fixed generator of the one-dimensional square; changing it multiplies \(B\) by a nonzero scalar and does not affect isotropic lines, square-zero status, or the formulas.

## Proof
**Intrinsic bilinear presentation.** Fix \(0\ne u\in E^2\). Since the product is bilinear and commutative, there is a unique symmetric bilinear form \(B\) with \(xy=B(x,y)u\). Its radical is exactly \(\operatorname{Ann}(E)\), so it is nonsingular. An ordered basis \((v,w)\) is natural if and only if \(B(v,w)=0\). In such a basis, nonsingularity forces \(B(v,v)B(w,w)\ne0\), since its Gram matrix is diagonal and invertible.

**Counting orthogonal bases.** Projective lines in \(E\) number \(q+1\). Exactly \(\epsilon(B)\) of them are isotropic. For every nonisotropic line \(L\), its orthogonal complement \(L^\perp\) is again nonisotropic and differs from \(L\); conversely \(L\oplus L^\perp=E\). Thus \(L\mapsto L^\perp\) is a fixed-point-free involution on the \(m=q+1-\epsilon(B)\) eligible lines. For each ordered pair \((L,L^\perp)\), there are precisely \((q-1)^2\) choices of nonzero vectors, producing exactly \(m(q-1)^2\) ordered natural bases. Factoring out the free scaling-and-swap action of order \(2(q-1)^2\) yields exactly \(m/2\) natural-basis classes.

**Isotropic-line count.** In odd characteristic, a nonsingular quadratic form in two variables has two projective zeros when it is split and none when anisotropic. Its splitting discriminant is \(-\det B\) up to squares. In characteristic two, an alternating nonsingular binary form has no orthogonal basis and is excluded by the evolution-algebra hypothesis. Every nonalternating nonsingular symmetric binary form has exactly one isotropic projective line: write the nonzero diagonal quadratic form as \(a x^2+c y^2=(\sqrt a x+\sqrt c y)^2\) using perfection of finite fields, where at least one diagonal coefficient is nonzero. Hence \(\epsilon(B)=1\) in characteristic two. This also verifies that \(m\) is even in every case.

**Counting graph types.** Both squares in a natural basis are nonzero scalar multiples of \(u\), so their coefficient supports agree. The graph is \(G_{2,1}\) exactly when \(u\) lies on one of the two basis lines; otherwise it is \(G_{2,2}\). If \(B(u,u)=0\), no nonisotropic basis line can equal \(ku\), hence no \(G_{2,1}\) occurs. If \(B(u,u)\ne0\), the unique unordered orthogonal line pair containing \(ku\) is \(\{ku,(ku)^\perp\}\); it contributes exactly \(2(q-1)^2\) ordered natural bases. Division by the total count yields the stated probability. This also gives exactly one scaling-and-swap class of sparse graphs.

**Exact uniqueness boundary.** Uniqueness up to scaling/reordering is equivalent to \(m=2\). For even \(q\), \(m=q\), so this is exactly \(q=2\). For odd \(q\), \(m=q-1\) in the split case and \(m=q+1\) in the anisotropic case; hence uniqueness holds exactly in the split \(q=3\) case. The explicit examples have nondegenerate diagonal Gram matrices and one-dimensional squares but dependent squared basis vectors, proving the stated exception to the unrestricted criterion in the inspected preprint.

## Verification
Run both embedded standalone programs using Python 3 with no external packages. `verification/check_all_fields.py` directly constructs nondegenerate symmetric forms, enumerates every ordered orthogonal basis and every nonzero square vector, and checks the total and individual graph counts. All Gram forms and all square vectors are tested for fields with \(q=2,3,4,5\); selected additional forms, with all square vectors, are tested for \(q=7,8,9,16\). `verification/check_graph_spectrum.py` independently checks all binary Gram forms and nonzero vectors for prime fields \(q=3,5,7\), plus representative forms for \(q=11,13\). Both programs report `VERIFY_OK`; recorded outputs are included. These finite tests corroborate, but do not replace, the uniform projective-line proof.

## Relationship to prior work
Brache, Martín Barquero, Martín González and Sánchez-Ortega (arXiv:2103.01625, first public March 2, 2021) give the general bilinear-form presentation and classification of algebras with one-dimensional square, including isotropic versus anisotropic square vectors. Boudi, Cabrera Casado and Siles Molina (arXiv:2006.14460, first public June 25, 2020; Publ. Mat. 2022), especially Proposition 2.16 and Corollary 2.13, describe the geometry of natural bases, but do not provide this all-finite-field exact count or graph distribution. In the inspected preprint, Corollary 2.7 is stated without a field-size restriction; its proof explicitly uses \(|k|>3\), and the two small-field examples above contradict the literal unrestricted conclusion. Kaygorodov, Martín González and Viruel (arXiv:2610.22248, first public October 15, 2026) formulate the natural-basis enumeration problem (Question 14), give a nontrivial two-dimensional graph-change example (Remark 22), and ask for simultaneous graphical realizations (Question 30). The mere existence of both graph types over some fields is therefore **prior work**; the complete parameterwise count, exact distribution, rigidity exceptions and sharp small-field boundary are the present claim. Earlier work on the whole family of graphs or higher-dimensional analogues is not excluded.

## Limitations
The result is restricted to two-dimensional nondegenerate evolution algebras with one-dimensional square over finite fields. It does not classify higher-dimensional natural-basis graph distributions or degenerate algebras. It does not prove absolute historical priority; an unstated corollary of classical finite quadratic-space counting or an earlier specialized paper might cover the formulas. The examples refute only the unrestricted small-field reading of the cited corollary, not the valid large-field statement obtained when \(|k|>3\).

## References
1. C. Brache, D. Martín Barquero, C. Martín González, J. Sánchez-Ortega, *Evolution algebras with one-dimensional square*, arXiv:2103.01625 (2021), https://arxiv.org/abs/2103.01625.
2. N. Boudi, Y. Cabrera Casado, M. Siles Molina, *Natural families in evolution algebras*, arXiv:2006.14460 (2020); Publ. Mat. 66 (2022), 159–181, https://arxiv.org/abs/2006.14460.
3. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248 (October 15, 2026), https://arxiv.org/abs/2610.22248.
