# Full two-sided symmetry character of complete-graph Hom complexes

## Finding

For integers \(2\le m<n\), consider the polyhedral graph-homomorphism complex \(X_{m,n}=\operatorname{Hom}(K_m,K_n)\). Its cells are ordered \(m\)-tuples of pairwise disjoint nonempty subsets of an \(n\)-element color set; their dimensions are the total number of used colors minus \(m\). The two symmetric groups act jointly: \(S_m\) permutes the ordered blocks and \(S_n\) permutes colors.

For \(\sigma\in S_m\), list the lengths of its cycles as \(a_1,\ldots,a_t\). For \(\pi\in S_n\), let \(\mathcal C(\pi)\) be its cycles and write \(\ell(C)\) for a cycle's length. Define the integer

\[
L(\sigma,\pi)=(-1)^m\operatorname{sgn}(\sigma)
\sum_{J\subseteq\{1,\ldots,t\}}(-1)^{t-|J|}
\prod_{C\in\mathcal C(\pi)}
\left(1-\sum_{\substack{j\in J\\a_j\mid\ell(C)}}a_j\right).
\]

Then every reduced rational homology group vanishes except possibly degree \(d=n-m\), and the **complete joint character** in that degree is

\[
\boxed{\operatorname{tr}\left((\sigma,\pi)\mid \widetilde H_d(X_{m,n};\mathbb Q)\right)
=(-1)^d\bigl(L(\sigma,\pi)-1\bigr).}
\]

This formula gives the actual rational representation up to isomorphism for every \(m,n\) in the stated range, rather than just an Euler characteristic. Moreover, for the action on colors alone,

\[
\boxed{
\widetilde H_*(|X_{m,n}|/S_n;\mathbb Q)=0,
\qquad
\widetilde H_i(|X_{m,n}|/A_n;\mathbb Q)
\cong
\begin{cases}
\mathbb Q^{\binom{n-2}{m-2}},&i=n-m,\\
0,&i\ne n-m.
\end{cases}}
\]

The known nonequivariant wedge-of-spheres theorem and its Betti numbers are used as inputs, not claimed as new. The new conclusion is the joint group character and the stated color-symmetry quotient calculation.

## Assumptions and scope

Both source and target are finite, undirected, simple, loopless **complete graphs**; \(2\le m<n\) throughout. A cell \(A=(A_1,\ldots,A_m)\) has each \(A_i\ne\varnothing\), with \(A_i\cap A_j=\varnothing\) for \(i\ne j\). Its closure is \(\prod_{i=1}^m\Delta(A_i)\), a product of simplices of dimension \(\sum_i(|A_i|-1)\). The group action is \((\sigma,\pi)A\) obtained by sending the colors of block \(A_i\) to the block \(A_{\sigma(i)}\) via \(\pi\). Quotients are **ordinary geometric orbit spaces**, not homotopy orbit spaces. All group characters and quotient homology are over \(\mathbb Q\).

The earliest cited public source containing the equivalent ordered-disjoint-block face poset is the 1997 preprint by Babson and Kozlov. The later 2003 preprint supplies the explicit modern Hom-complex identification and complete-graph homotopy theorem. The temporal scope is therefore anchored by the earlier source, not its later revisions or journal publication.

## Proof

**1. Homology concentration (previously established).** Babson–Kozlov, *Complexes of graph homomorphisms*, Proposition 4.5, proves \(X_{m,n}\simeq\bigvee S^{n-m}\). In its proof, covering by \(m\) subcomplexes distinguished by which block may contain a fixed color reduces their intersections to \(X_{m,n-1}\) and their members by an explicit acyclic matching to \(X_{m-1,n-1}\). Induction gives \((n-m-1)\)-connectivity; since cells have dimension at most \(n-m\), only degree \(d\) can have reduced homology, freely generated. We use this established theorem, not a conjectural inference from finite computations.

**2. Cellular orientation and fixed-cell signs.** Orient the cell \(A=(A_i)\) as the product of simplices, with increasing color order within each block and ascending block order. Put \(U=\bigcup_i A_i\). A group element \(g=(\sigma,\pi)\) fixes this cell setwise exactly when \(\pi(A_i)=A_{\sigma(i)}\). Its linear action on the direct sum of simplex tangent spaces has determinant

\[
\det(g|T A)=\operatorname{sgn}(\pi|_U)\operatorname{sgn}(\sigma).
\]

Indeed the direct sum is the quotient of the permutation vector space \(\mathbb R^U\) by its \(m\)-dimensional subspace of blockwise constant vectors. The determinants on these two spaces are \(\operatorname{sgn}(\pi|_U)\) and \(\operatorname{sgn}(\sigma)\) respectively; the latter equals its own reciprocal. If exactly \(q\) cycles of \(\pi\) lie in \(U\), then \(U\) is a union of full color cycles and \(\operatorname{sgn}(\pi|_U)=(-1)^{|U|-q}\). Therefore its contribution to the alternating cellular trace is

\[
(-1)^{\dim A}\det(g|TA)
=(-1)^{|U|-m+|U|-q}\operatorname{sgn}(\sigma)
=(-1)^m\operatorname{sgn}(\sigma)(-1)^q.
\]

A cell not preserved setwise contributes zero to the trace. This signed trace calculation is valid for products of simplices and does not assume that fixed cells are pointwise fixed.

**3. Counting signed fixed cells.** Encode a cell by a function \(f:[n]\to\{0,1,\ldots,m\}\), where \(0\) denotes an unused color and every positive value must occur. It is fixed by \((\sigma,\pi)\) precisely when \(f(\pi(c))=\sigma(f(c))\), with \(\sigma(0)=0\). For a given color cycle \(C\) of length \(\ell\), either all its colors are unused (one choice with weight \(+1\)) or its colors map equivariantly onto an entire block-permutation cycle of length \(a_j\mid\ell\). There are exactly \(a_j\) choices of cyclic phase in the latter case, each with weight \(-1\). A fixed labeling which uses one block in a block-permutation cycle necessarily uses every block in that cycle. Inclusion–exclusion over the \(t\) block-permutation cycles thus forces all blocks to be used and yields exactly \(L(\sigma,\pi)\) for the alternating cellular trace.

**4. Passing to homology.** The cellular Hopf trace identity gives

\[
L(\sigma,\pi)=\sum_i(-1)^i\operatorname{tr}\bigl((\sigma,\pi)|H_i(X_{m,n};\mathbb Q)\bigr).
\]

Because \(m<n\), the complex is connected, so \(H_0\) contributes trace one. By step 1 no reduced homology occurs outside degree \(d\). Subtracting this unit trace proves the boxed joint character formula, including its normalization, simultaneous source/target action, and all elements of both groups.

**5. Color quotients.** Set \(\sigma=1\) and let \(c(\pi)\) be the number of cycles of \(\pi\). The fixed-cell formula simplifies to

\[
L(1,\pi)=\sum_{j=0}^{m}(-1)^j\binom mj(1-j)^{c(\pi)}.
\]

The ordinary and sign-weighted cycle-index identities are

\[
\frac1{n!}\sum_{\pi\in S_n}z^{c(\pi)}
=\frac{z(z+1)\cdots(z+n-1)}{n!},
\qquad
\frac1{n!}\sum_{\pi\in S_n}\operatorname{sgn}(\pi)z^{c(\pi)}
=\frac{z(z-1)\cdots(z-n+1)}{n!}.
\]

For \(n>m\), evaluating the rising-factorial average at \(z=1-j\) gives one for \(j=0\) and zero for every \(1\le j\le m\); the trivial \(S_n\)-multiplicity in top homology is therefore zero. For the sign multiplicity, the falling factorial evaluates for \(j\ge2\) to \((-1)^n\binom{n+j-2}{n}\), and the \(j=0,1\) terms vanish. With \(d=n-m\) the sign multiplicity becomes

\[
(-1)^m\sum_{j=2}^m(-1)^j\binom mj\binom{n+j-2}{n}
=\binom{n-2}{m-2}.
\]

The equality follows by taking the coefficient of \(z^n\) in

\[
(1+z)^{n-2}\sum_{j=0}^{m}(-1)^j\binom mj(1+z)^j
=(-z)^m(1+z)^{n-2}.
\]

Finally, for any finite group acting cellularly, barycentric subdivision makes the action admissible, and rational chains of the geometric quotient identify with invariant rational chains. Averaging is exact over \(\mathbb Q\), so quotient rational homology is the invariant portion of the original homology. The \(A_n\)-fixed part of an \(S_n\)-module is the sum of its trivial and sign isotypic multiplicities (both one-dimensional upon restriction). This proves both quotient formulas. Connectivity gives the reduced degree-zero claim.

## Verification

The standalone file `homkmkn_verify.py` uses only the Python standard library. It enumerates every cell as a color-assignment vector, constructs the integral signed cellular boundaries and checks every composition of consecutive differentials equals zero. It independently computes homology ranks over a prime field and evaluates the cellular alternating trace for **every individual group element** in the four cases \((m,n)=(2,4),(3,4),(3,5),(4,5)\), totaling \(3792\) joint actions. Every trace agrees with the closed cycle formula. It separately averages the color characters for six cases, including \((3,6)\) and \((4,6)\), and obtains the predicted \(S_n\)- and \(A_n\)-invariant dimensions. The complete reproducibility log is `homkmkn_verify_output.txt`; run `python3 homkmkn_verify.py`. Finite tests are independent corroboration, **not** proof of the infinite parameter theorem; the proof is the universal fixed-cell enumeration and character argument above.

## Relationship to prior work

Babson and Kozlov's 1997 *Diagrams of classifying spaces and k-fold Boolean algebras* identifies the **same underlying ordered nonempty disjoint-subset poset** in its \(\widehat{\mathcal B}_{n,m}^{o}\) construction (equivalent to the barycentric face poset of \(X_{m,n}\)). Its Theorem 6.2(d) gives the ordinary homotopy concentration, while part (e) treats the quotient under *block permutations*. These already established statements are not novelty claims here. The 2003 *Complexes of graph homomorphisms*, Definition 1.2 and Propositions 4.5–4.6, supplies the modern cellular definition, wedge homotopy theorem, and Betti-number enumeration; these are again explicitly excluded from novelty. The older paper does not furnish the complete joint \(S_m\times S_n\) character for an arbitrary pair of permutations, nor the calculated color-label \(S_n\) versus \(A_n\) quotient multiplicities in its inspected sections.

Pfeifle's *Dissections, Hom-complexes and the Cayley trick* discusses geometric realizations and related cell structures, not this two-sided representation. Dochtermann's *Hom complexes and homotopy theory in the category of graphs* establishes broader functorial homotopy properties, not a competing formula for the present character in the accessible material. General formulas for equivariant Euler characteristics of other graph complexes do not imply the present statement, since their cells and group actions are different.

## Limitations

All conclusions use **rational** coefficients for group characters and quotient homology. They do not identify integral \(S_m\times S_n\) homology lattices, integral torsion in orbit spaces, quotient homotopy types, or Borel-equivariant homology. The proof applies to simple complete source and target graphs and to \(2\le m<n\); connectedness and the homology-degree argument require this strict inequality. The topological concentration theorem is previously published. Existing results about the ordered nonempty-block poset overlap substantially at the nonequivariant and source-quotient levels. Exhaustive publication priority is not guaranteed; an equivalent, differently indexed two-sided character computation might exist. The finite verification cases are bounded and cannot establish infinite cases on their own. Independent mathematical validation has not been performed.

## References

1. E. Babson and D. Kozlov, *Diagrams of classifying spaces and k-fold Boolean algebras*, initial public preprint 1997-04-29, arXiv:math/9704227, https://arxiv.org/abs/math/9704227, especially Definition 6.1 and Theorem 6.2.
2. E. Babson and D. N. Kozlov, *Complexes of graph homomorphisms*, initial public preprint 2003-10-05, arXiv:math/0310056, https://arxiv.org/html/math/0310056v4, especially Definition 1.2 and Propositions 4.5–4.6.
3. J. Pfeifle, *Dissections, Hom-complexes and the Cayley trick*, arXiv:math/0512529, https://arxiv.org/abs/math/0512529.
4. A. Dochtermann, *Hom complexes and homotopy theory in the category of graphs*, European Journal of Combinatorics 30 (2009), 490–509, https://doi.org/10.1016/j.ejc.2008.04.009.
