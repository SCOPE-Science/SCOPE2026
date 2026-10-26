# Two rational components and exact finite-field counts for commuting tuples in the six-generator exterior algebra

## Finding

Let \(k\) be an algebraically closed field of characteristic different from \(2\), let \(V=k^6\), let \(E=\bigwedge V\) be its associative exterior algebra, and let \(s\ge3\) be an integer. The **reduced** affine commuting-tuple variety
\[
\mathcal C_s(E)=\{(a_1,\ldots,a_s)\in E^s:a_i a_j=a_j a_i\text{ for all }i<j\}_{\mathrm{red}}
\]
has **exactly two geometrically irreducible, rational components**, of dimensions
\[
\boxed{\dim X_s=48s+16},\qquad
\boxed{\dim Y_s=\begin{cases}
58s-\binom{s}{2},&3\le s\le10,\\
48s+55,&s\ge10.
\end{cases}}
\]
The component \(X_s\) is the closure of tuples with nonzero degree-one odd part, necessarily of collective rank one. The component \(Y_s\) consists precisely of tuples with all degree-one parts zero and pairwise orthogonal degree-three parts for the wedge pairing. Thus the variety is reducible and **non-equidimensional for every \(s\ge3\)**. In particular, at \(s=3\) the dimensions are \(160\) and \(171\); from \(s=10\) onward the dimension gap is constantly \(39\).

There is also an exact count over every finite field \(\mathbb F_q\) of **odd** order. Define
\[
S_s(q)=\sum_{r=0}^{\min(s,10)}
\prod_{i=0}^{r-1}\frac{(q^{20-i}-q^i)(q^s-q^i)}{q^r-q^i},
\]
with the empty product equal to \(1\). The number of ordered pairwise-commuting tuples is
\[
\boxed{\#\mathcal C_s(E_{\mathbb F_q})(\mathbb F_q)
=q^{32s}\left[q^{6s}S_s(q)
+\frac{(q^6-1)(q^s-1)}{q-1}q^{15s+11}\right].}
\]
The formula is an integer-valued expression, not an asymptotic approximation.

## Assumptions and scope

The degree-one, degree-three, and degree-five components of each odd element are taken with respect to the usual exterior grading. The even subspace of \(E\) is central and has dimension \(32\); its odd subspace also has dimension \(32=6+20+6\). Characteristic different from \(2\) is essential for equating associative commutation of two odd elements with vanishing of their exterior product. The geometric assertions hold over algebraically closed fields of such characteristic; the arithmetic assertion holds over all odd finite fields. The claim concerns **reduced** varieties and set-theoretic point counts, not the nonreduced commuting scheme.

## Proof

**1. Reduction to two strata.** Write each tuple entry as an arbitrary even part plus an odd part \(u_i=\ell_i+\alpha_i+\beta_i\), where \(\ell_i\in\bigwedge^1V\), \(\alpha_i\in\bigwedge^3V\), and \(\beta_i\in\bigwedge^5V\). Since even elements are central and odd elements anticommute, pairwise commutation is equivalent to \(u_i\wedge u_j=0\). Splitting the degrees \(2,4,6\) gives, for every \(i<j\),
\[
\ell_i\wedge\ell_j=0,\qquad
\ell_i\wedge\alpha_j+\alpha_i\wedge\ell_j=0,\qquad
\ell_i\wedge\beta_j+\alpha_i\wedge\alpha_j+\beta_i\wedge\ell_j=0.
\]
The first equations force the span of \(\ell_1,\ldots,\ell_s\) to have dimension either zero or one. These are the only possible strata.

**2. Nonzero linear stratum.** Work on a chart where \(\ell_1=v\ne0\) and write \(\ell_j=c_jv\), with \(c_1=1\). Choose \(V=kv\oplus U\), where \(\dim U=5\), and set \(\eta_1=0\). The degree-four equations hold precisely when
\[
\alpha_j=c_j\alpha_1+v\wedge\eta_j,\qquad
\eta_j\in\bigwedge^2U,\quad j\ge2.
\]
Indeed, the kernel of \(v\wedge-:\bigwedge^3V\to\bigwedge^4V\) is \(v\wedge\bigwedge^2U\). Substituting into degree six, the equations reduce to
\[
 v\wedge\bigl(\beta_j-c_j\beta_1-\alpha_1\wedge\eta_j\bigr)=0
\qquad(j\ge2).
\]
They are solved, with no further pairwise compatibility conditions, by
\[
\beta_j=c_j\beta_1+\alpha_1\wedge\eta_j+v\wedge\zeta_j,
\qquad \zeta_j\in\bigwedge^4U.
\]
Substitution checks the equations for *all* pairs, not only those involving index one. The independent parameters on each chart are \(\alpha_1\) (dimension \(20\)), \(\beta_1\) (dimension \(6\)), and for each \(j\ge2\), \(\eta_j\) (dimension \(10\)) and \(\zeta_j\) (dimension \(5\)). The rank-one locus of ordered \(6\)-vectors has dimension \(6+s-1=s+5\), is irreducible and rational, and the displayed fibers are affine spaces of dimension \(15s+11\). Consequently the nonzero linear stratum is irreducible and rational of odd-coordinate dimension \(16s+16\), hence of total dimension \(48s+16\). Let \(X_s\) be its closure.

**3. Zero linear stratum.** If all \(\ell_i=0\), the only equations are \(\alpha_i\wedge\alpha_j=0\). On the \(20\)-dimensional space \(W=\bigwedge^3V\), the coefficient of a fixed volume form in \(\alpha\wedge\alpha'\) is a nondegenerate alternating bilinear form: each monomial three-form pairs nontrivially with exactly its complementary three-form. Thus the \(\alpha_i\) constitute an ordered isotropic tuple in a symplectic space of dimension \(20\), while the \(\beta_i\) are arbitrary, as are all even coordinates.

Every isotropic subspace extends to a Lagrangian \(10\)-plane. The incidence variety of a Lagrangian together with \(s\) vectors lying in it is a vector bundle over the irreducible Lagrangian Grassmannian \(\operatorname{LG}(10,20)\), and its projection onto all isotropic ordered tuples is surjective. Therefore the zero-linear stratum \(Y_s\) is irreducible. Its dense open rank-\(r\) locus has \(r=\min(s,10)\). If \(s\le10\), the dimension of the isotropic tuple space is
\[
\dim\operatorname{IG}(s,20)+s^2
=s(20-s)-\binom{s}{2}+s^2
=20s-\binom{s}{2}.
\]
If \(s\ge10\), its dimension is \(\dim\operatorname{LG}(10,20)+10s=55+10s\). Adding \(6s\) freely chosen degree-five and \(32s\) even coordinates gives the displayed dimension of \(Y_s\). On the generic rank-\(r\) locus, the isotropic span is uniquely determined; it is a frame bundle over the rational symplectic isotropic Grassmannian, or a surjection bundle over the rational Lagrangian Grassmannian. Hence \(Y_s\) is rational.

**4. Exhaustion and component separation.** Every commuting tuple belongs either to the nonzero-linear stratum or to the closed zero-linear stratum. The closure \(X_s\) is irreducible, and \(Y_s\) is irreducible and closed. Moreover
\[
\dim Y_s-\dim X_s=
\begin{cases}10s-\binom{s}{2}-16,&3\le s\le10,\\39,&s\ge10,
\end{cases}
\]
which is strictly positive for all \(s\ge3\). Therefore \(Y_s\) is not contained in \(X_s\); and \(X_s\) is not contained in \(Y_s\) because it contains tuples with nonzero linear parts. These are exactly the two irreducible components.

**5. Finite-field count.** Over \(\mathbb F_q\), the number of nonzero rank-one matrices of shape \(6\times s\) is \((q^6-1)(q^s-1)/(q-1)\), and each admits \(q^{15s+11}\) choices of its degree-three/five data. For the zero-linear stratum, partition isotropic \(s\)-tuples of \(W\) by span dimension \(r\). The number of isotropic \(r\)-subspaces in a symplectic \(20\)-space is
\[
\frac{\prod_{i=0}^{r-1}(q^{20-i}-q^i)}{\prod_{i=0}^{r-1}(q^r-q^i)},
\]
and the number of spanning ordered \(s\)-tuples in each is \(\prod_{i=0}^{r-1}(q^s-q^i)\). Summing yields \(S_s(q)\). The \(6s\) degree-five coordinates and the \(32s\) even coordinates are free. Adding the disjoint strata gives the claimed formula.

## Verification

The accompanying standalone \(\texttt{verify.py}\) checks literal exterior multiplication for randomly sampled commuting tuples over fields of orders \(3,5,7\), exhaustively enumerates isotropic tuples in smaller symplectic spaces, verifies the middle-wedge pairing, checks the new dimension formulas, and compares the \(s=2\) specialization against a separately obtained commuting-pair polynomial over four odd field orders. It reports \(\texttt{VERIFY_OK_EXTERIOR_TUPLE_COMPONENTS_AND_COUNTS}\). These finite checks support, but do not replace, the all-length proof above.

## Relationship to prior work

Domokos and Zubor (2014, arXiv:1403.2916) characterize maximal commutative subalgebras of Grassmann algebras using square-zero subspaces and symplectic pairings. Their Sections 2–8 and Theorem 7.1 do not enumerate ordered commuting tuples, determine irreducible components of the commuting-tuple variety for arbitrary length, or give the finite-field point count. Márki, Meyer, Szigeti, and van Wyk (2013, arXiv:1307.0292) study matrix embeddings and polynomial identities rather than tuple geometry. A separate earlier computation for commuting **pairs** in the six-generator exterior algebra gives dimensions \(112,115\) and an exact finite-field polynomial; the present theorem claims novelty only for all lengths \(s\ge3\), including the length-10 isotropic-rank threshold and the uniform component formulas. The known pair polynomial agrees exactly with the specialization of the new count formula, but the pair statement does not entail the higher-tuple classification. Historical priority is not independently established.

## Limitations

The statement is about associative pairwise commutation in the six-generator exterior algebra and does not claim the corresponding result for other numbers of generators, characteristic two, or the nonreduced scheme structure. The point-count formula is for odd finite fields. No claim is made that the isotropic-frame count alone resolves unrelated matrix-commuting varieties. The possibility of an unlocated earlier equivalent description remains.

## References

1. M. Domokos and M. Zubor, *Commutative subalgebras of the Grassmann algebra*, arXiv:1403.2916 (first public version 2014-03-12), especially Sections 2, 4, 7, and 8. https://arxiv.org/abs/1403.2916
2. L. Márki, J. Meyer, J. Szigeti, and L. van Wyk, *Matrix representations of finitely generated Grassmann algebras and some consequences*, arXiv:1307.0292 (first public version 2013-07-01). https://arxiv.org/abs/1307.0292
