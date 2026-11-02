# A first non-equidimensional threshold for endomorphism monoids of truncated coordinate crosses

## Finding
For every field \(k\), integer \(n\ge2\), and truncation length \(d\in\{2,3,4\}\), consider the commutative unital local algebra
\[
A_{n,d}(k)=k[x_1,\ldots,x_n]/(x_ix_j\ (i\ne j),\;x_1^d,\ldots,x_n^d).
\]
Let \(\mathcal E_{n,d}(k)\) be the **reduced** affine variety parametrizing unital \(k\)-algebra endomorphisms. In every characteristic and over every algebraic closure, its irreducible components and dimensions are as follows.

* At \(d=2\), the variety is affine \(n^2\)-space: exactly one component, dimension \(n^2\).
* At \(d=3\), it has exactly \(n^n\) geometrically irreducible components, each an affine linear space of dimension \(n(n+1)\).
* At \(d=4\), it has exactly \((n+1)^n\) geometrically irreducible components, each an affine linear space. For every \(0\le j\le n\), precisely \(\binom nj n^j\) components have dimension
\[
2n^2-j(n-2).
\]
All components are defined over \(k\). Thus the first non-equidimensional member among these truncation lengths occurs at \(d=4\) and \(n\ge3\). For \(n=2\), all nine components at \(d=4\) have dimension eight.

For every prime power \(q\), with no restriction on the characteristic, the numbers of **unital** endomorphisms are exactly
\[
\begin{aligned}
|\operatorname{End}_{\mathbb F_q}(A_{n,2})|&=q^{n^2},\\
|\operatorname{End}_{\mathbb F_q}(A_{n,3})|&=\bigl(q^n[1+n(q-1)]\bigr)^n,\\
|\operatorname{End}_{\mathbb F_q}(A_{n,4})|&=\bigl(q^{2n}+n(q-1)q^{n+1}\bigr)^n.
\end{aligned}
\]
For \(d=4\), comparison with the already known automorphism order gives the sharp density dichotomy
\[
\lim_{q\to\infty}\frac{|\operatorname{Aut}(A_{2,4}(\mathbb F_q))|}{|\operatorname{End}(A_{2,4}(\mathbb F_q))|}=\frac29,
\qquad
\lim_{q\to\infty}\frac{|\operatorname{Aut}(A_{n,4}(\mathbb F_q))|}{|\operatorname{End}(A_{n,4}(\mathbb F_q))|}=0\quad(n\ge3).
\]
Here limits range over prime powers. For fixed \(n\ge3\), the ratio equals \(n!q^{-n(n-2)}(1+O(q^{-1}))\).

## Assumptions and scope
Every \(A_{n,d}\) is the fibre product over \(k\) of \(n\) copies of \(k[t]/(t^d)\). Endomorphisms preserve the unit and the base field. The reduced endomorphism variety is the reduced locus in the affine space of images of the \(n\) generators. The statements describe geometric irreducible components of its **reduction**, not the scheme structure or embedded nilpotents of the full representation scheme. No restriction to algebraically closed \(k\) is needed for the formulas or for the fact that the components are defined over \(k\); geometric irreducibility is assessed after scalar extension to an algebraic closure.

For \(d=4\), index the coefficients in the image of a source generator \(x_i\) on target branch \(x_s\) by \(a_{si},b_{si},c_{si}\). These are the coefficients of \(x_s,x_s^2,x_s^3\), respectively. There are \(n\) independent target rows \(s\).

## Proof
**(1) Reduction to independent target rows.** The maximal ideal \(\mathfrak m=(x_1,\ldots,x_n)\) consists of the nilpotent elements of \(A_{n,d}\): an element with nonzero scalar coefficient is a unit, while \(\mathfrak m^d=0\). Every unital algebra map therefore sends every \(x_i\) into \(\mathfrak m\). Conversely, choosing any \(n\) images in \(\mathfrak m\) determines a unital endomorphism exactly when the defining relations are preserved. Because products of different target branches vanish and each element of \(\mathfrak m\) has \(d\)-th power zero, the only nonautomatic conditions are \(\phi(x_i)\phi(x_j)=0\) for \(i\ne j\). Writing
\[
\phi(x_i)=\sum_{s=1}^{n}\sum_{h=1}^{d-1}u_{sih}x_s^h,
\]
these conditions split independently for each target branch \(s\) and define a direct product \(\mathcal E_{n,d}\cong B_{n,d}^{\,n}\), where \(B_{n,d}\) is the reduced variety of \(n\) pairwise-annihilating elements in \(t\,k[t]/(t^d)\). This identifies every unital endomorphism with exactly one tuple of coefficient rows.

**(2) Length two.** In \(t\,k[t]/(t^2)\) every product vanishes. Hence \(B_{n,2}=\mathbb A^n\), giving \(\mathcal E_{n,2}=\mathbb A^{n^2}\) and the asserted count.

**(3) Length three.** Write the \(i\)-th row-entry as \(a_i t+b_i t^2\). The equations are exactly \(a_i a_j=0\) for every \(i\ne j\); the \(b_i\) are free. The reduced locus is the union of \(n\) distinct coordinate-linear spaces, with only one \(a_i\) allowed to be nonzero, each of dimension \(n+1\). Their irreducible components are precisely these maximal distinct linear spaces. For a finite field of size \(q\), disjoint counting by zero versus exactly one nonzero \(a_i\) gives \(q^n+n(q-1)q^n=q^n[1+n(q-1)]\) choices in one target row. Raising to the \(n\)-th power yields the global count and \(n^n\) components of dimension \(n(n+1)\).

**(4) Length four.** Write the \(i\)-th entry on one target branch as \(a_i t+b_i t^2+c_i t^3\). For distinct \(i,j\), multiplying and comparing coefficients of \(t^2\) and \(t^3\) yields
\[
 a_i a_j=0,\qquad a_i b_j+b_i a_j=0.
\]
There is no constraint on the \(c_i\). Define the linear subspaces
\[
L_0=\{a_1=\cdots=a_n=0\},\qquad
L_s=\{a_i=b_i=0\ (i\ne s)\}\quad(1\le s\le n).
\]
All of these satisfy the equations. Conversely, if all \(a_i\) vanish, the point is in \(L_0\). Otherwise the first equation forces precisely one index \(s\) with \(a_s\ne0\), and the second equation then forces \(b_i=0\) for every \(i\ne s\); thus the point lies in \(L_s\). Consequently the *underlying reduced locus* is exactly \(B_{n,4}=L_0\cup L_1\cup\cdots\cup L_n\).

The dimensions are \(\dim L_0=2n\) and \(\dim L_s=n+2\). Each is irreducible and none is contained in the union of the others: \(L_s\) has points with \(a_s\ne0\) and \(L_0\) has, because \(n\ge2\), points with at least two distinct nonzero \(b_i\), hence outside every \(L_s\). All are thus **exactly** the irreducible components. This argument remains valid in characteristic two, since it uses no division by two.

For each target row, the zero-linear locus \(L_0\) has \(q^{2n}\) points; for each \(s\), the disjoint open part \(L_s\setminus L_0\) has \((q-1)q^{n+1}\) points. Therefore \(B_{n,4}(\mathbb F_q)\) has \(q^{2n}+n(q-1)q^{n+1}\) points, giving the third exact count.

**(5) Product components and dimensions.** The product of any selected \(n\) row components is an affine space and hence geometrically irreducible; distinct selections are not contained in each other. Their union is the whole reduced endomorphism locus. Therefore they are all its geometric irreducible components. Choosing \(j\) of the \(n\) target rows to be of an active type \(L_s\), and one of \(n\) source indices \(s\) for each, gives \(\binom nj n^j\) components of dimension
\[
(n-j)2n+j(n+2)=2n^2-j(n-2).
\]
Summing multiplicities gives \(\sum_{j=0}^{n}\binom nj n^j=(n+1)^n\). For \(n\ge3\), dimension decreases strictly with \(j\), proving non-equidimensionality; for \(n=2\), all these dimensions are eight.

**(6) Automorphisms as a consistency boundary, not a new classification.** A unital endomorphism of this local Artinian algebra is invertible exactly when its induced linear map on \(\mathfrak m/\mathfrak m^2\) is invertible (Nakayama's lemma and finite-dimensionality). For \(d=4\), an invertible linear coefficient matrix with pairwise orthogonal columns under coordinatewise multiplication must be monomial. Hence the previously known formula gives \(n!(q-1)^nq^{n(n+1)}\) automorphisms. Dividing by the proven endomorphism count gives the two displayed limits; when \(n\ge3\), the leading term in the row count is \(q^{2n}\), whereas at \(n=2\) the two summands have the same leading degree, giving the factor \(3^2=9\).

## Verification
The standalone script `verify_coordinate_cross.py` enumerates coefficient rows over the prime fields \(\mathbb F_2\), \(\mathbb F_3\) and the extension field \(\mathbb F_4\) represented as \(\mathbb F_2[\omega]/(\omega^2+\omega+1)\). It multiplies truncated polynomials directly, independently tests all pairwise annihilation relations, compares the computed row solutions with the explicit union of linear components, and checks the formulas. It also independently evaluates unital endomorphism relations and invertibility for three exhaustive small cases, and performs five additional bounded checks. The saved `coordinate_cross_check_output.txt` ends with `COORDINATE_CROSS_ENDOMORPHISM_GEOMETRY_OK 13 ROW_CASES 3_GLOBAL_EXHAUSTIVE 5_GLOBAL_SAMPLES`. The finite checks are consistency tests, not proofs of the assertions for arbitrary \(n\), \(q\) or \(k\).

## Relationship to prior work
Perepechko (2008) proves the realizability of abstract affine algebraic monoids as endomorphism monoids of certain finite-dimensional **nonassociative** algebras. His general existence theorem neither computes the endomorphism monoid of the specific commutative associative fibre product \(A_{n,d}\) nor implies its geometric component counts. Timofeeva (2013) develops generators and relations for fibre products of commutative algebras, providing structural context for these algebras, but does not enumerate the maps of the resulting algebras to themselves.

Díaz, Liendo, Manzano-Flores and Regeta (2024 preprint, updated later) classify automorphism groups of finite-dimensional monomial algebras in characteristic zero. The directly relevant published finding *Automorphisms of truncated coordinate-cross algebras over arbitrary fields* gives a normal form for invertible maps of exactly this family in all characteristics, including the unit-group order used above. Those prior works cover the **automorphism** problem, which is expressly excluded from the novelty claim. Their statements do not classify the noninvertible endomorphism locus, count all endomorphisms over finite fields, or determine its reducibility and equidimensionality threshold. Searches for equivalent formulae under fibre-product, truncated-axis, monomial-algebra and algebraic-monoid terminology did not reveal prior complete coverage. Such a prior theorem could still exist under another formulation.

## Limitations
This theorem concerns unital endomorphisms and the **reduced** geometric endomorphism variety at truncation lengths exactly two, three and four. It does not determine the possibly nonreduced endomorphism scheme, its intersection multiplicities, or the geometry at truncation lengths five and above. The elementary linear-row classification for these lengths is sufficient for the stated formulae but must not be extrapolated without proof. Publication priority remains provisional, and no independent external validation was performed.

## References
1. A. Perepechko, *Affine algebraic monoids as endomorphisms' monoids of finite-dimensional algebras*, arXiv:0809.2356v1, first public 2008-09-13, https://arxiv.org/html/0809.2356v1.
2. N. V. Timofeeva, *Fibred product of commutative algebras: generators and relations*, arXiv:1307.2192, first public 2013-07-08, https://arxiv.org/abs/1307.2192.
3. R. Díaz, A. Liendo, G. Manzano-Flores and A. Regeta, *The Automorphism groups of zero-dimensional monomial algebras*, arXiv:2408.02197v1, first public 2024-08-05, https://arxiv.org/abs/2408.02197.
4. *Automorphisms of truncated coordinate-cross algebras over arbitrary fields*, published mathematical research record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-automorphisms-of-truncated-coordinate-cross-algebras-over-arbitr--625ba30274cb.
