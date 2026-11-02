# Frobenius-norm discriminants and chain singularities in cyclic smooth linear systems

## Finding
Let \(q=p^h\) be a prime power, let \(m\geq3\) and \(d\geq3\) satisfy \(p\mid d\) and \(p\nmid m\), and set \(a=d-1\). Consider the \((m-1)\)-dimensional linear system \(\mathcal L\) over \(\mathbb F_q\) obtained by Frobenius descent from
\[
F_{\boldsymbol c}(Y_0,\ldots,Y_{m-1})=
\sum_{i=0}^{m-1}c_iY_i^{a}Y_{i+1},\qquad Y_m=Y_0,
\]
where the variables \(Y_i\) are the Moore normal-basis coordinates over \(\mathbb F_{q^m}\) and coefficient Frobenius cyclically permutes the \(m\) monomial summands. This is the characteristic-dividing-degree construction in Asgarli--Ghioca--Reichstein, Section 3, Case 2.

**Theorem.** The reduced discriminant \(D\subset\mathbb P(\mathcal L)\simeq\mathbb P^{m-1}_{\mathbb F_q}\) is the projective zero locus of the field norm \(\operatorname{Norm}_{\mathbb F_{q^m}/\mathbb F_q}(z)\), where the parameter vector space is identified with \(\mathbb F_{q^m}\) by Frobenius descent. It is irreducible over \(\mathbb F_q\) and is a simple-normal-crossings union of \(m\) hyperplanes in general position after passage to an algebraic closure. In particular, \(D(\mathbb F_q)=\varnothing\).

For every integer \(s\geq1\), put \(g=\gcd(m,s)\), \(\ell=m/g\), and \(Q=q^s\). The exact number of **smooth** \(\mathbb F_{q^s}\)-members is
\[
\boxed{N_{\mathrm{sm}}(s)=\frac{(Q^{\ell}-1)^g}{Q-1}.}
\]
More precisely, for \(1\leq k\leq g\), the number of projective members having exactly \(k\) nonzero Frobenius blocks of length \(\ell\) (hence exactly \(m-k\ell\) zero geometric monomial coefficients) is
\[
\boxed{N_k(s)=\binom gk\frac{(Q^{\ell}-1)^k}{Q-1}.}
\]
The case \(k=g\) is exactly the smooth locus. Thus every member defined over \(\mathbb F_{q^s}\) is smooth exactly when \(\gcd(m,s)=1\); the least extension degree admitting a singular member is the smallest prime divisor of \(m\).

At the generic point of each geometric discriminant hyperplane, precisely one coefficient \(c_i\) vanishes. The corresponding hypersurface has exactly **one** geometric singular point, is analytically the isolated chain singularity
\[
f(u_1,\ldots,u_{m-1})=u_1^{a}u_2+u_2^{a}u_3+\cdots+u_{m-2}^{a}u_{m-1}+u_{m-1}^{a}=0,
\]
and has multiplicity \(a\), algebraic Milnor number and Tjurina number equal to
\[
\boxed{\mu=\tau=a^{m-1}-a^{m-2}+\cdots+(-1)^{m-1}.}
\]
The local colengths refer to the Jacobian and Tjurina ideals over the algebraically closed coefficient field. No classification of the singularities at intersections of discriminant hyperplanes is asserted.

## Assumptions and scope
The only field assumptions are \(q=p^h\), \(h\geq1\), \(p\mid d\), \(d\geq3\), \(m\geq3\), and \(p\nmid m\). The Frobenius descent is with respect to the degree-\(m\) extension \(E=\mathbb F_{q^m}\) and any normal basis \(\alpha,\alpha^q,\ldots,\alpha^{q^{m-1}}\). In the ambient projective space, the Moore forms \(Y_i=\sum_{j=0}^{m-1}\alpha^{q^{i+j}}X_j\) give an invertible linear change of variables over \(E\) and satisfy coefficient Frobenius \(\sigma(Y_i)=Y_{i+1}\). The descended parameter space is the \(\mathbb F_q\)-vector space \(E\), mapping \(z\in E\) to the fixed form
\[
\sum_{i=0}^{m-1}z^{q^i}Y_i^aY_{i+1}.
\]
The scalar \(z=0\) is excluded after projectivization. The word *discriminant* here means the **reduced** locus of geometrically singular hypersurfaces, not the possibly nonreduced universal discriminant polynomial or its multiplicities.

## Proof
**1. Geometric smoothness test.** Work over an algebraic closure, set \(t_i=c_iY_i^aY_{i+1}\), with indices modulo \(m\), and note that \(a=-1\) in characteristic \(p\). Direct differentiation gives
\[
Y_i\frac{\partial F}{\partial Y_i}=t_{i-1}-t_i.
\]
At a singular point all \(t_i\) are equal, say to \(t\). Since \(F=mt\) and \(p\nmid m\), the equation \(F=0\) forces \(t=0\). If every \(c_i\ne0\), some \(Y_j=0\), and the derivative at index \(j\) (using \(a-1\geq1\)) forces \(Y_{j-1}=0\). Repeating gives every coordinate zero, impossible in projective space. Thus all-nonzero coefficients imply smoothness. Conversely, if \(c_i=0\), the coordinate point \(e_i\) is on \(F=0\) and all its partial derivatives vanish, as \(a\geq2\). Hence
\[
F_{\boldsymbol c}\text{ is smooth}\quad\Longleftrightarrow\quad\prod_{i=0}^{m-1}c_i\ne0.
\]
This also independently verifies the smoothness premise of the source construction in the present degree range.

**2. Frobenius descent and the discriminant.** The \(m\) monomials \(Y_i^aY_{i+1}\) are linearly independent because the \(Y_i\) are independent linear coordinates and \(a\geq2\). Frobenius permutes their coefficient lines transitively. The map \(z\mapsto(z,z^q,\ldots,z^{q^{m-1}})\) is an injective \(\mathbb F_q\)-linear map \(E\to E^m\), with image exactly the fixed coefficient space by dimension and descent. Its product of geometric coefficient coordinates is \(\operatorname{Norm}_{E/\mathbb F_q}(z)\). The coordinate hyperplanes \(c_i=0\) are linearly independent and permuted transitively by Frobenius. Their projective union is therefore geometrically simple normal crossings and defines one irreducible reduced divisor over \(\mathbb F_q\). Since the norm of every nonzero element of \(E\) is nonzero, the divisor has no \(\mathbb F_q\)-point.

**3. Exact extension strata.** Standard separable finite-field tensor decomposition gives
\[
E\otimes_{\mathbb F_q}\mathbb F_{q^s}\cong
\prod_{j=1}^{g}\mathbb F_{q^{s\ell}},
\qquad g=\gcd(m,s),\quad \ell=m/g.
\]
The nonzero elements in any one factor correspond precisely to a nonzero length-\(\ell\) orbit of geometric coefficients. For a fixed set of \(k\) nonzero factors there are \((Q^\ell-1)^k\) nonzero parameter vectors. Their projectivizations have free scalar action by \(\mathbb F_{q^s}^{\times}\), so division by \(Q-1\), followed by the choice of \(k\) factors, yields the stated count. Summing over \(1\leq k\leq g\) gives \((Q^m-1)/(Q-1)\), the cardinality of \(\mathbb P^{m-1}(\mathbb F_{q^s})\). The smooth members require all \(g\) factors nonzero. If \(g=1\), every projective parameter is smooth; if \(g\geq2\), taking one factor zero and another nonzero gives a singular parameter. The least positive \(s\) with \(g\geq2\) is the least prime divisor of \(m\).

**4. Generic local singularity and colength.** Assume \(c_0=0\) and all other coefficients nonzero. At a critical point the displayed derivative identities make all \(t_i\) equal; since \(t_0=0\), all vanish. If any \(Y_i\ne0\) with \(i\ne0\), then \(t_i=0\) forces \(Y_{i+1}=0\); its derivative forces \(c_iY_i^a=0\), a contradiction. Thus the unique singular point is \(e_0\). On the chart \(Y_0=1\), the equation is
\[
\sum_{j=1}^{m-2}c_j u_j^a u_{j+1}+c_{m-1}u_{m-1}^a.
\]
Successively rescaling coordinates over the algebraic closure makes every coefficient one. Its multiplicity is \(a\), since the final monomial has degree \(a\) and all others degree \(a+1\).

Put \(r=m-1\). The positive rational weights \(w_r=1/a\), \(w_j=(1-w_{j+1})/a\) make the chain polynomial weighted homogeneous of degree one. Choose integer degree \(D=a^r\) and weights \(W_j=Dw_j\in\mathbb Z_{>0}\). The partial derivatives have no common affine zero except the origin by the preceding argument; they form a weighted-homogeneous regular sequence. Thus their finite-dimensional graded quotient has Hilbert series
\[
\prod_{j=1}^r\frac{1-T^{D-W_j}}{1-T^{W_j}},
\]
and its dimension is \(\prod_{j=1}^r(D-W_j)/W_j\). The recurrence \(1-w_{j+1}=aw_j\) telescopes the product to
\[
\mu=a^r(1-w_1)=a^r-a^{r-1}+\cdots+(-1)^r.
\]
Finally, \(D=a^r\) is invertible in characteristic \(p\), and the integer-weight Euler identity
\[
Df=\sum_{j=1}^r W_j u_j\frac{\partial f}{\partial u_j}
\]
shows \(f\) lies in its Jacobian ideal. Therefore the Tjurina quotient has the same length \(\tau=\mu\). This local equality was established directly in positive characteristic rather than inferred from characteristic-zero Milnor-fiber topology.

## Verification
Run `python verify_cyclic.py` with SymPy installed. It independently constructs Jacobian Gröbner bases for \((d,m,p)=(4,3,2),(3,4,3),(4,5,2)\), obtaining local quotient lengths \(7,5,61\). It also verifies integer-weight Euler identities, extension-field block-count identities for ten parameter triples, and exhaustively enumerates the support distribution of the fully split \(\mathbb F_8\) parameter space in the \((q,m)=(2,3)\) example. The script is a finite and symbolic corroboration, not a substitute for the preceding universal proof.

For example, for \((q,m,d)=(2,3,4)\), all seven projective \(\mathbb F_2\)-members are smooth, as are all 21 \(\mathbb F_4\)-members. Over \(\mathbb F_8\), precisely 49 of 73 projective members are smooth; 21 have one zero coefficient and three have two. At a generic geometric discriminant hyperplane, the isolated plane-curve singularity is \(u^3v+v^3=0\) in characteristic two, of Tjurina length seven.

## Relationship to prior work
Asgarli--Ghioca--Reichstein, arXiv:2207.00918, Section 3, Case 2, introduced the Frobenius-descended cyclic family to prove that **every base-field member** is smooth. Their Lemma 4 is the all-coefficients-nonzero smoothness implication. The present result instead determines the reduced discriminant as a norm divisor, counts smooth and singular parameters over **every extension field**, locates the first extension with singular parameters, and identifies the generic discriminant singularity and its local algebra.

Aramaki--Takahashi, arXiv:1903.02732, Eq. (1.1) and the alternating Milnor-number formula in its introduction, study general chain-type invertible singularities over \(\mathbb C\). The abstract chain normal form and its classical characteristic-zero Milnor calculation are therefore **not** claimed as new. The specific occurrence as the generic discriminant singularity of this finite-field linear system, its positive-characteristic Tjurina equality, and the field-extension parameter stratification are the claims assessed here. Known descriptions of norm tori similarly inform the descent argument; the theorem does not claim novelty for the general structure of restriction-of-scalars tori.

## Limitations
The assertion about singularity type and local colength applies only to the geometric open strata with **exactly one** missing coefficient. It does not classify higher-codimension intersections of discriminant hyperplanes or the singularities of their fibers. The discriminant is reduced; no scheme-theoretic multiplicity of the universal discriminant equation is asserted. The local algebraic Milnor number in positive characteristic is a Jacobian-colength invariant, not automatically a topological vanishing-cycle count. No assertion concerns independent certification or the priority of results in uncatalogued literature.

## References
1. S. Asgarli, D. Ghioca, Z. Reichstein, *Linear families of smooth hypersurfaces over finitely generated fields*, arXiv:2207.00918 (initial public version July 2, 2022), Section 3, Lemmas 3--4 and Case 2. https://arxiv.org/abs/2207.00918
2. D. Aramaki, A. Takahashi, *Maximally-graded matrix factorizations for an invertible polynomial of chain type*, arXiv:1903.02732 (2019), introduction and Eq. (1.1). https://arxiv.org/abs/1903.02732
