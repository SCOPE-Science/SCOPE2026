# Perrin top components and motivic square-zero strata in fourth-truncated cyclic quiver algebras

## Finding

Let \(n\ge 4\) be an integer, let \(k\) be any field, let \(Q_n\) be the consistently oriented cycle with vertices \(\mathbb Z/n\mathbb Z\), and let \(\Lambda_n=kQ_n/J^4\), where \(J\) denotes the arrow ideal. Let \(X_n\) be the **reduced** affine variety of elements \(x\in\Lambda_n\) satisfying \(x^2=0\).

Write \(\mathcal I_n\) for the independent subsets of the ordinary cycle graph \(C_n\). For nonempty \(S\in\mathcal I_n\), put \(r=|S|\); list its elements in cyclic order, and write \(g_1,\ldots,g_r\ge2\) for the forward cyclic gaps, of total length \(n\). Set
\[
h(S)=\#\{j:g_j\ge4\}.\]
The subset \(X_{n,S}\) on which the path-length-one coefficient is nonzero exactly at \(S\) is a locally closed subvariety with an isomorphism over \(k\)
\[
 X_{n,S}\cong(\mathbb G_m)^r\times\mathbb A^{2n-r-h(S)}.
\]
The zero-support stratum is \(X_{n,\varnothing}\cong\mathbb A^{2n}\). These strata partition \(X_n\) over every field, without a characteristic restriction.

Consequently, in the Grothendieck ring of \(k\)-varieties, with \(\mathbb L=[\mathbb A^1]\),
\[
 [X_n]=\mathbb L^{2n}+
 \sum_{\substack{S\in\mathcal I_n\\S\ne\varnothing}}
 (\mathbb L-1)^{|S|}\mathbb L^{2n-|S|-h(S)}.
\]
The variety has dimension exactly \(2n\) and has precisely \(1+P_n\) geometrically irreducible **top-dimensional** components, where the Perrin sequence satisfies \(P_0=3\), \(P_1=0\), \(P_2=2\), and \(P_n=P_{n-2}+P_{n-3}\) for \(n\ge3\). Every top-dimensional component is defined over \(k\).

For every prime power \(q\),
\[
 \#X_n(\mathbb F_q)=q^{2n}+
 \sum_{\substack{S\in\mathcal I_n\\S\ne\varnothing}}
 (q-1)^{|S|}q^{2n-|S|-h(S)}.
\]
This has a rational generating series in the cycle length. Define the rational function
\[
 W_q(z)=\frac{q-1}{q}\left(z^2+z^3+\frac{z^4}{q(1-z)}\right).
\]
For every \(n\ge4\), the coefficient of \(z^n\) in
\[
 \frac{z}{1-z}+\frac{zW_q'(z)}{1-W_q(z)}
\]
equals \(q^{-2n}\#X_n(\mathbb F_q)\). The convention for the first three formal coefficients makes no claim about cycles with fewer than four vertices.

## Assumptions and scope

The algebra is the usual finite-dimensional path algebra quotient, with the length-zero idempotents and paths of lengths one, two, and three forming a basis of dimension \(4n\). The square-zero condition applies to a single element, not a commuting tuple or a module representation space. The scheme of equations may carry nilpotent scheme structure; the geometric statements refer to its reduced variety. The finite-field statement counts field-valued points of that variety and the original equation scheme equally.

A top-dimensional component means an irreducible component of dimension \(2n\). No assertion is made that every irreducible component has this dimension, or that the unreduced equation scheme is reduced.

## Proof

**1. Path coefficients and exact equations.** For \(i\in\mathbb Z/n\mathbb Z\), let \(e_i\) be the trivial path and \(u_i,v_i,w_i\) the unique paths of lengths one, two, three starting at \(i\), respectively. Path multiplication is concatenation when defined and zero at total length at least four. Write
\[
 x=\sum_i(a_ie_i+b_iu_i+c_iv_i+d_iw_i).
\]
The length-zero coefficients of \(x^2\) are \(a_i^2\). At every field-valued point of \(x^2=0\) all \(a_i\) vanish. Hence on the reduced variety, the remaining equations are exactly
\[
 b_ib_{i+1}=0,\qquad
 b_ic_{i+1}+c_ib_{i+2}=0\quad(i\bmod n),
\]
while all \(d_i\) are unrestricted. No division by a field characteristic occurs.

**2. Independence and gap-by-gap rank.** The first equations say that the support \(S=\{i:b_i\ne0\}\) is independent in \(C_n\). Fix a nonempty such \(S\). For one gap of length \(g\) from occupied position \(s\) to the next occupied position \(t=s+g\), the only potentially nonzero equations in the gap come from rows \(i=s\) and \(i=t-2\).

If \(g=2\), these rows coincide and give the single equation \(b_sc_{s+1}+b_tc_s=0\). Since \(b_s\ne0\), it solves uniquely for \(c_{s+1}\) as a Laurent-polynomial multiple of \(c_s\). If \(g=3\), the two equations each force \(c_{s+1}=0\), giving one independent constraint. If \(g\ge4\), they force the two distinct entries \(c_{s+1}=c_{t-2}=0\), giving two independent constraints. The coordinates involved in different gaps do not overlap. Therefore the complete linear system in the \(c_i\) has constant rank
\[
 \sum_{j=1}^r\bigl(1+\mathbf 1_{g_j\ge4}\bigr)=r+h(S).
\]
The equations can be solved algebraically over the torus where all \(b_s\) for \(s\in S\) are units. There are \(n-r-h(S)\) free \(c\)-coordinates and \(n\) free \(d\)-coordinates, proving the claimed **isomorphism of locally closed varieties**, not just a bijection of field points. If \(S=\varnothing\), every \(c_i\) and \(d_i\) is free, giving \(\mathbb A^{2n}\).

**3. Geometry of the top-dimensional components.** Each nonempty stratum is geometrically irreducible and has dimension \(2n-h(S)\). The empty stratum has dimension \(2n\), so the dimension of \(X_n\) is \(2n\). A nonempty independent set has \(h(S)=0\) exactly when every cyclic gap has length two or three, equivalently when \(S\) is a maximal independent set of \(C_n\). Every such stratum is irreducible of full dimension, so its closure is a top-dimensional irreducible component. Distinct maximal independent supports yield distinct closures: the coordinate functions \(b_i\) that vanish identically distinguish the closures, and incomparable maximal supports cannot have the same nonzero-coordinate pattern. The closed zero-support stratum also has full dimension and is a distinct component. Conversely, every full-dimensional component contains a dense constructible subset belonging to one of the finitely many full-dimensional strata, so this list exhausts the top-dimensional components.

The known enumeration of maximal independent subsets of \(C_n\) is the Perrin number \(P_n\). It can also be obtained directly: gap compositions using only parts two and three give
\[
 \sum_{n\ge1}P_nz^n=\frac{2z^2+3z^3}{1-z^2-z^3},
\]
which agrees with the stated recurrence and initial values in positive degree. This proves the count \(1+P_n\), without asserting anything about smaller-dimensional irreducible components.

**4. Motivic, arithmetic, and rational-series identities.** The finite disjoint stratification and the explicit product isomorphisms yield the Grothendieck-class identity. Evaluating the strata over \(\mathbb F_q\) gives the point-count formula. To obtain the generating function, give each cyclic gap of length two or three weight \((q-1)/q\), and each gap of length at least four weight \((q-1)/q^2\). Their length-generating series is \(W_q(z)\). A cyclic composition of \(r\ge1\) gaps, with one occupied position distinguished, is counted \(n/r\) times over a cycle with labeled vertices; the factor accounts correctly for periodic compositions as well. It follows that
\[
 q^{-2n}\#X_n(\mathbb F_q)
 =1+n[z^n]\sum_{r\ge1}\frac{W_q(z)^r}{r}
 =1+n[z^n]\log\frac{1}{1-W_q(z)}.
\]
Taking the formal logarithmic derivative produces the stated rational generating series. All identities are formal in \(z\); no convergence assumptions are involved.

## Verification

The standalone file `verify.py` constructs the path-product equations directly, independently counts all admissible coefficient tuples \((b,c)\), evaluates the support-gap formula, and independently computes the linear-equation rank on each support over small prime fields. It exhaustively checks the full algebra's square equation over \(\mathbb F_2\) when \(n=4\), including diagonal and length-three coefficients.

The tested finite-field totals, for \(n=4,5,6\) and \(q=2\), are respectively \(640\), \(3584\), and \(17408\); at \(q=3\) they are \(18225\), \(255879\), and \(2735937\). The verifier checks additional cases and compares the maximal-support counts to the Perrin recurrence for \(4\le n\le15\). The program prints `VERIFY_OK` on success. These are finite corroborations; the arbitrary-field and all-size assertions follow from the proof above.

## Relationship to prior work

The algebra family is standard: Xu, Han and Jiang studied Hochschild cohomology of truncated quiver algebras, including basic cyclic quivers, in 2005. Their invariant is Hochschild cohomology rather than the square-zero-element locus. Babson, Huisgen-Zimmermann and Thomas study components of **module-representation varieties** for path algebras; those parametrization spaces do not themselves equal the locus of square-zero elements of the algebra. Goodearl and Huisgen-Zimmermann subsequently give stronger general results on components of such module-representation varieties, which likewise do not directly imply the particular support-gap geometry and point-count formula here.

The fact that maximal independent sets of a cycle are counted by Perrin numbers is established graph theory, explicitly acknowledged by Bisdorff and Marichal in 2007 (attributing it to Füredi). The contribution assessed here is the exact bridge from path-algebra square-zero geometry to those independent-set counts, together with the torus-affine stratification and the full finite-field count. An equivalent result in specialized literature not identified by these searches remains a possibility.

## Limitations

Only top-dimensional irreducible components are classified, not every lower-dimensional component. No scheme-theoretic reducedness, multiplicity, singular-locus classification, or mixed-characteristic flatness is asserted. For \(n<4\), paths can wrap around the cycle before the fourth truncation and require a separate treatment. The discovery comparison does not establish absolute literature uniqueness; independent expert review has not been performed.

## References

1. Y. Xu, Y. Han, W. Jiang, *Hochschild cohomology of truncated quiver algebras*, arXiv:math/0509202v1, 9 September 2005. https://arxiv.org/abs/math/0509202
2. R. Bisdorff, J.-L. Marichal, *Counting non-isomorphic maximal independent sets of the n-cycle graph*, arXiv:math/0701647v1, 23 January 2007. https://arxiv.org/abs/math/0701647
3. E. Babson, B. Huisgen-Zimmermann, R. Thomas, *Generic representation theory of quivers with relations*, arXiv:1407.2673v1, 10 July 2014. https://arxiv.org/html/1407.2673v1
4. K. R. Goodearl, B. Huisgen-Zimmermann, *Closures in varieties of representations and irreducible components*, arXiv:1801.09168v1, 28 January 2018. https://arxiv.org/html/1801.09168v1
