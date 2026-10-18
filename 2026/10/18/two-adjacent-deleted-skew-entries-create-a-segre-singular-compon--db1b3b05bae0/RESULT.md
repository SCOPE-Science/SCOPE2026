# Two adjacent deleted skew entries create a Segre singular component and a six-vertex splitting

## Finding

Let \(k\) be algebraically closed of characteristic zero, let \(n=2m\ge6\), and let \(A=(a_{ij})\) be the alternating \(n\)-by-\(n\) matrix with independent coordinates \(a_{ij}\) for \(i<j\), except that \(a_{12}=a_{13}=0\). Put
\[
X_n=V(\operatorname{Pf}(A))\subset\mathbb P^{\binom n2-3}_k.
\]
The hypersurface \(X_n\) is geometrically integral and normal. Write \(Y_n=\{[A]:\operatorname{rank}(A)\le n-4\}\). Define the exceptional subvariety
\[
Z_n=V\left(a_{1j}\ (4\le j\le n),\ a_{23},\ a_{2j}a_{3\ell}-a_{2\ell}a_{3j}\ (4\le j<\ell\le n)\right).
\]
Then, with reduced scheme structure,
\[
\operatorname{Sing}(X_n)_{\mathrm{red}}=Y_n\cup Z_n.
\]
The irreducible variety \(Z_n\) is a projective cone over the Segre \(\mathbb P^1\times\mathbb P^{n-4}\), with a free-coordinate vertex \(\mathbb P^{\binom{n-3}{2}-1}\). It has
\[
\operatorname{codim}_{\mathbb P^{\binom n2-3}}Z_n=2n-6,
\quad\dim Z_n=\binom{n-2}{2},\quad\deg Z_n=n-3.
\]
For \(n\ge8\), the variety \(Y_n\) is irreducible of codimension six in the ambient projective space. Thus there are exactly two irreducible singular components. They have different dimensions for every \(n\ge8\). Along general points of \(Y_n\) and \(Z_n\), the transverse germs are nondegenerate ordinary quadratic cones, respectively of ranks six and \(2n-6\).

For \(n=6\), the rank-two locus instead splits into exactly two irreducible components:
\[
Y_6^{(1)}=\{[A]:\operatorname{rank}A\le2,\ a_{14}=a_{15}=a_{16}=0\},
\]
\[
Y_6^{(2)}=\{[A]:\operatorname{rank}A\le2,\ a_{23}=0\}.
\]
The three irreducible singular components \(Y_6^{(1)},Y_6^{(2)},Z_6\) all have dimension six and degrees respectively \(5,9,3\). Therefore the reduced singular locus is pure-dimensional with degree \(17\) for \(n=6\), but non-equidimensional for every even \(n\ge8\). Each component has a generic transverse quadratic cone of rank six in the six-vertex case.

## Assumptions and scope

The base field is algebraically closed and has characteristic zero. Projective coordinates are the \(\binom n2-2\) independent skew entries remaining after the two adjacent deletions. Matrix rank is ordinary linear rank. All singular-locus decompositions concern the *reduced* support of the scheme defined by partial derivatives of the Pfaffian in the remaining coordinates. A nondegenerate transverse quadratic cone of rank \(r\) means, after an étale or formal change of coordinates and removal of smooth factors, a germ \(V(q)\) with \(q\) a rank-\(r\) quadratic form.

## Proof

**Jacobian support.** The derivative with respect to an allowed entry \(a_{ij}\) is the signed complementary Pfaffian \(\operatorname{Pf}(A_{\widehat i\widehat j})\). When \(\operatorname{rank} A\le n-4\), all these derivatives vanish. When \(\operatorname{rank} A=n-2\), the complete matrix of complementary Pfaffians is a nonzero decomposable bivector spanning \(\Lambda^2\ker A\). The derivative restrictions therefore vanish precisely when this bivector is supported on the forbidden coordinates \((1,2),(1,3)\):
\[
\Lambda^2\ker A\subset\operatorname{span}\{e_1\wedge e_2,e_1\wedge e_3\}.
\]
This is equivalent to \(e_1\in\ker A\) and \(\ker A\) containing a nonzero vector \(\alpha e_2+\beta e_3\). The first requirement is exactly \(a_{1j}=0\) for \(j\ge4\). The second requires \(a_{23}=0\) and the two remaining row vectors \((a_{2j})_{j\ge4},(a_{3j})_{j\ge4}\) to be proportional, equivalently the stated two-by-two minors. Conversely these equations provide the required kernel vectors, including at lower-rank points. This proves the stated union *set-theoretically*, hence after reduction.

**Exceptional component.** Once the linear equations of \(Z_n\) are imposed, its remaining essential equations are precisely the two-by-two minors of a generic \(2\)-by-\((n-3)\) matrix. The determinantal ideal is prime, its codimension is \(n-4\), and the associated projective Segre degree is \(n-3\). The other \(\binom{n-3}{2}\) skew entries on vertices \(4,\ldots,n\) are free. Adding the \(n-2\) imposed linear equations gives ambient codimension \(2n-6\) and the displayed dimension. Generic members of \(Z_n\) have rank \(n-2\): choose a nonzero proportional row and a generic alternating form on the remaining \(n-3\) coordinates to obtain an invertible alternating \((n-2)\)-submatrix.

**Rank locus for \(n\ge8\).** Let \(V=k^n\), \(U=\langle e_1,e_2,e_3\rangle\), and let \(G=\operatorname{Gr}(4,V)\). Consider pairs \((K,\omega)\) with \(K\in G\), \(\omega\in\Lambda^2(V/K)^*\), and \(\omega(\bar e_1,\bar e_2)=\omega(\bar e_1,\bar e_3)=0\). Over the open set \(K\cap U=0\), the two linear conditions are independent because \(n-4\ge4\), so the incidence is a vector bundle of fiber dimension \(\binom{n-4}{2}-2\). The rank of these conditions drops by at most one over \(K\cap U\ne0\), a Schubert locus of codimension \(n-6\ge2\), except that both vanish when \(e_1\in K\) (codimension \(n-4\ge4\)) or when \(\dim(K\cap U)\ge2\) (codimension at least \(2n-10\ge6\)). The incidence is the complete intersection of the two tautological linear functions in the total space of a vector bundle: its components all have the expected codimension two. Each lower-rank fiber locus has strictly smaller dimension than the generic locus, so there is no vertical irreducible component. Hence the incidence is irreducible. Its proper projective image is exactly \(Y_n\), because every alternating matrix of rank at most \(n-4\) admits a four-dimensional kernel subspace. The generic image has rank exactly \(n-4\), so its dimension is
\[
4(n-4)+\binom{n-4}{2}-2-1=\binom n2-9,
\]
which is ambient codimension six. Its generic points do not lie in \(Z_n\), which has rank \(n-2\) generically.

**The exceptional six-vertex split.** When \(n=6\), the rank-two locus is the Plücker Grassmannian \(\operatorname{Gr}(2,6)\subset\mathbb P^{14}\) cut by \(p_{12}=p_{13}=0\). Write a rank-two alternating matrix as \(u\wedge v\). If its first Plücker column vanishes, it belongs to \(Y_6^{(1)}\simeq\operatorname{Gr}(2,5)\). Otherwise the two equalities force \(p_{23}=0\), and the resulting locus \(Y_6^{(2)}\) is the Schubert variety of two-planes meeting the fixed three-space \(\langle e_4,e_5,e_6\rangle\). This Schubert variety is irreducible by the incidence of a line in that three-space with a containing two-plane. Both components have dimension six and generically occur with multiplicity one in the codimension-two linear section of \(\operatorname{Gr}(2,6)\). The Plücker degrees \(\deg\operatorname{Gr}(2,6)=14\) and \(\deg\operatorname{Gr}(2,5)=5\) give \(\deg Y_6^{(2)}=9\). The component \(Z_6\) is distinct: its generic matrices have rank four, whereas both other components have rank two. Therefore all three components contribute independently to total degree \(5+9+3=17\).

**Integral normal hypersurface.** Expand the Pfaffian along row one. It is a degree-one form in \(a_{1j}\) for \(4\le j\le n\), with coefficients the complementary generic Pfaffians on the full alternating matrix indexed by \(2,\ldots,n\). At least two coefficients are nonassociate irreducible Pfaffians, hence have greatest common divisor one. Gauss's lemma makes the restricted Pfaffian irreducible. It defines a hypersurface and is thus Cohen–Macaulay. The singular-locus classification has codimension at least five *inside the hypersurface*, so Serre's \(R_1\) and \(S_2\) conditions establish normality.

**Transverse germs.** At a generic rank-\((n-4)\) point of \(Y_n\), a nonsingular alternating \((n-4)\)-block reduces the Pfaffian by a Schur complement to the Pfaffian of a \(4\)-by-\(4\) alternating residual matrix. The two deleted-coordinate conditions are transverse to the generic rank stratum for \(n\ge8\), so its six normal coordinates retain the nondegenerate Pfaffian quadratic form. For \(n=6\), the two smooth rank-two components are likewise transverse at their generic points; the same rank-six Hessian is obtained.

At a generic point of \(Z_n\), change basis among \(e_2,e_3\) so that the kernel is \(\langle e_1,e_3\rangle\). The complementary alternating block on \(\langle e_2,e_4,\ldots,e_n\rangle\) is invertible. In its Schur-complement chart, the defining Pfaffian is a unit times the pairing of the \(n-3\) free entries of row one against the \(n-3\) independent normal variations of row three. This is a nondegenerate bilinear quadratic form of rank \(2n-6\). Its kernel directions are exactly the tangent directions to \(Z_n\). These statements concern dense smooth opens of the components, not their intersection germs.

## Verification

The accompanying `verify.py` uses signed perfect-matching expansions of Pfaffians. It exhaustively checks all \(8191\) nonzero points of the projective coordinate space over \(\mathbb F_2\) when \(n=6\). At every point it independently compares all partial derivatives with the union of the displayed components; the test finds \(351\) singular points and no discrepancy. This is a finite-field check of polynomial identities, not a characteristic-zero completeness argument. It also computes integral Hessian ranks at explicit general-type witnesses for the three six-vertex components, for the exceptional locus at \(n=8,10\), and for a rank-\(4\) witness on \(Y_8\). All checks return `VERIFY_OK`. Run `python3 verify.py` with the standard library.

## Relationship to prior work

De Negri and Gorla, *G-biliaison of ladder Pfaffian varieties* (arXiv:0809.3417v1, first posted 2008-09-19), study primeness, Cohen–Macaulayness, projective normality, codimension and liaison for ladder Pfaffian ideals. Those theorems are not the Jacobian-rank and adjacent-coordinate *specialization* classification here: taking a full Pfaffian and substituting two adjacent entries by zero is not the same operation as generating an ideal by the Pfaffians wholly supported on a ladder. Kodiyalam–Lam–Swan's *Determinantal Ideals, Pfaffian Ideals, and the Principal Minor Theorem* provides the general alternating-rank and Pfaffian expansion framework, not these singular-component equations. Standard Grassmannian and Schubert calculations already imply the rank-two six-vertex component degrees; those known ingredient degrees are not separately claimed to be new.

The existing disjoint-deleted-edge Pfaffian singular-locus classification applies only when omitted edges are pairwise disjoint. Its one-edge case does not imply the adjacent-two-edge singular set; its multi-edge case does not cover the shared vertex, the rank-one two-row condition or the exceptional six-vertex splitting. Unindexed or otherwise unstated implications of general determinantal-section theory remain an originality risk.

## Limitations

Only reduced singular support, generic transverse analytic type, irreducible-component numbers, dimensions and the stated component degrees are established. No assertion is made about the full nonreduced Jacobian singular scheme or scheme-theoretic intersections of the components. Finite-field enumeration does not establish the arbitrary-size geometric theorem. The claim is for characteristic zero. Novelty comparison cannot eliminate the possibility of equivalent existing results outside the inspected sources.

## References

1. E. De Negri and E. Gorla, *G-biliaison of ladder Pfaffian varieties*, arXiv:0809.3417v1 (2008-09-19), https://arxiv.org/abs/0809.3417.
2. V. Kodiyalam, T. Y. Lam, and R. G. Swan, *Determinantal Ideals, Pfaffian Ideals, and the Principal Minor Theorem*, https://math.berkeley.edu/~lam/amspfaff.pdf (primary text inspected; public-first-date not inferred from journal metadata).
3. Classical Plücker embedding, Grassmannian degree and Schubert incidence calculations; used as established background rather than claimed new results.
