# A characteristic jump and generically nonreduced component in power-zero endomorphism schemes

## Finding

Let \(p\) be a prime and \(k\) any field. For the canonical local complete intersection \(A_p=k[x,y]/(x^p,y^p)\), write \(\mathfrak m=(x,y)\). Define the **power-zero scheme** \(N_p\) as the closed subscheme of the affine vector space underlying \(\mathfrak m\) cut out by the coefficients of \(u^p\). The scheme \(\mathcal E_p\) of unital **augmentation-preserving** algebra endomorphisms is isomorphic to \(N_p\times N_p\).

If \(\operatorname{char}k=p\), \(N_p\cong\mathbb A^{p^2-1}\) scheme-theoretically, hence \(\mathcal E_p\cong\mathbb A^{2(p^2-1)}\).

If \(\operatorname{char}k\ne p\), the geometric reduced support is the union of three explicit linear spaces:
\[
(N_p)_{\mathrm{red}}=xA_p\cup yA_p\cup\mathfrak m^2.
\]
For \(p=2\), the third is contained in the intersection, and \(N_2\) is reduced with exactly two components, both of dimension \(2\). For \(p\ge3\) these are three distinct irreducible components, of dimensions \(p(p-1)\), \(p(p-1)\), \(p^2-3\), respectively. When \(p\ge3\), \(N_p\) is **generically nonreduced** on the third component, although generically smooth on the first two. Thus the infinite family exhibits both characteristic sensitivity and a nonreduced geometric component invisible to point counts.

For \(k=\mathbb F_q\) with \(\operatorname{char}k\ne p\),
\[
|N_p(k)|=2q^{p(p-1)}+q^{p^2-3}-2q^{p(p-1)-1},\qquad
|\mathcal E_p(k)|=|N_p(k)|^2.
\]
In characteristic \(p\), these numbers are \(q^{p^2-1}\) and \(q^{2(p^2-1)}\). Over every finite-field extension of degree \(r\), the same formulas hold with \(q\) replaced by \(q^r\). Hence the nonmodular Hasse–Weil zeta function of the reduced support equals
\[
Z(N_p,T)=\frac{(1-q^{p(p-1)-1}T)^2}{(1-q^{p(p-1)}T)^2(1-q^{p^2-3}T)}.
\]

## Assumptions and scope

The field \(k\) is arbitrary; no algebraic closure or perfectness is assumed for the underlying point classification. Geometric components and generic reducedness refer to base change to an algebraic closure. The endomorphisms are required to preserve the specified augmentation \(A_p\to k\), so generator images lie in \(\mathfrak m\). No claim is made about unrestricted algebra endomorphisms that move the augmentation when the coefficient algebra is not reduced. The schemes are the literal coefficient-equation schemes, not merely their sets of field-valued points. The prime \(p\) in the exponents is held fixed as the field characteristic varies.

## Proof

**Endomorphism functor.** A unital augmented homomorphism is determined uniquely by images \(x\mapsto u\) and \(y\mapsto v\) in \(\mathfrak m\), subject to \(u^p=v^p=0\). Because the algebra is commutative, there are no additional constraints. The statement holds for every commutative test algebra and therefore gives \(\mathcal E_p=N_p\times N_p\) scheme-theoretically.

**Modular fiber.** In characteristic \(p\), the Frobenius identity gives \(u^p=\sum c_{ij}^p x^{ip}y^{jp}=0\) for every \(u\in\mathfrak m\), including universal coefficient variables. Thus the defining ideal is zero and \(N_p\) is affine space.

**Nonmodular point classification.** Fix an extension field of characteristic different from \(p\), and expand \(u=ax+by+w\) with \(w\in\mathfrak m^2\). The coefficients of \(x^{p-1}y\) and \(xy^{p-1}\) in \(u^p\) are \(pa^{p-1}b\) and \(pab^{p-1}\). If \(u^p=0\), then \(ab=0\). If \(a=b=0\), then \(u\in\mathfrak m^2\) and \(u^p=0\), since \(\mathfrak m^{2p-1}=0\).

Suppose \(a\ne0\) and \(b=0\). Decompose uniquely \(u=xH(x,y)+W(y)\), where \(H(0,0)=a\) and \(W\in yk[y]/(y^p)\). In the ring \(B=k[y]/(y^p)\), the coefficient of \(x^{p-1}\) in \((xH+W)^p\) equals
\[
W\bigl(pH(0,y)^{p-1}+WQ(y)\bigr)
\]
for some \(Q\in B\). The expression in parentheses is a unit of \(B\), because its residue is \(pa^{p-1}\ne0\). Thus \(W=0\) and \(u\in xA_p\). The case \(b\ne0\) is symmetric. Conversely, each of \(xA_p\), \(yA_p\) and \(\mathfrak m^2\) consists of power-zero elements. This proves the reduced support after arbitrary field extension.

**Components and intersections.** Monomial counting yields
\[
\dim_k xA_p=\dim_k yA_p=p(p-1),\quad \dim_k\mathfrak m^2=p^2-3.
\]
The intersections have dimensions \(\dim(xA_p\cap yA_p)=(p-1)^2\) and \(\dim(xA_p\cap\mathfrak m^2)=\dim(yA_p\cap\mathfrak m^2)=p(p-1)-1\). The triple intersection equals \(xA_p\cap yA_p\). For \(p=2\), \(\mathfrak m^2=(xy)\subseteq xA_p\cap yA_p\); for \(p\ge3\), none of the three spaces contains another. Since each is linear, these are precisely the reduced irreducible components.

**Reducedness and tangents.** For \(p=2\) outside characteristic two, write \(u=ax+by+cxy\). Its square is \(2abxy\); the defining ideal is \((ab)\), which is radical. For \(p\ge3\), the differential of the power map at a point is \(v\mapsto pu^{p-1}v\) with \(v\in\mathfrak m\). On \(\mathfrak m^2\), multiplication vanishes because \(u^{p-1}\mathfrak m\subseteq\mathfrak m^{2p-1}=0\). Hence the tangent dimension is \(p^2-1\), larger than the local component dimension \(p^2-3\) at its generic points away from the other components. This forces nonreducedness at the generic point of that component (after geometric base change). On the dense open set of \(xA_p\) where the linear coefficient of \(x\) is nonzero, \(u=xH\) with \(H\) a unit. Multiplication by \(pu^{p-1}\) on \(\mathfrak m\) has rank exactly \(p-1\), so the tangent dimension is \(p^2-p=p(p-1)\), matching the single reduced component. That open set is smooth; the \(yA_p\) case is symmetric.

**Arithmetic.** Inclusion–exclusion over the three linear spaces gives
\[
2q^{p(p-1)}+q^{p^2-3}-q^{(p-1)^2}-2q^{p(p-1)-1}+q^{(p-1)^2}
=2q^{p(p-1)}+q^{p^2-3}-2q^{p(p-1)-1}.
\]
This remains valid for \(p=2\). The endomorphism count is its square. Substitution over extension fields and the identity \(\exp(\sum_{r\ge1}q^{dr}T^r/r)=(1-q^dT)^{-1}\) yield the zeta function.

## Verification

A standalone standard-library Python script, `verification.py`, constructs the truncated algebra over prime fields, computes the power map by polynomial multiplication, and exhaustively enumerates all elements of \(\mathfrak m\) in the stated small cases. It checks characteristic-dependent power-zero counts, the explicit linear-space union, and the fact that endomorphisms are ordered pairs. It prints `VERIFY_OK`. Finite computations corroborate examples but are not used to infer the theorem for infinitely many primes or field extensions; the preceding proof supplies the general argument.

## Relationship to prior work

Premet's 2014 preprint develops the structure and derivations of the truncated polynomial ring in its native positive characteristic, including its automorphism group; it does not determine the coefficient-equation scheme of power-zero elements as the field characteristic varies. Deo and Maitra (1997) study graded automorphisms of truncated polynomial algebras, rather than all augmentation-preserving endomorphisms or generic scheme-theoretic nilpotence. Work on the \(K\)-theory of multivariable truncations establishes the naturality of these complete-intersection algebras but does not imply their endomorphism-scheme stratification. Neither these results nor the retrieved mathematical records establish the specific three-component support, the generic nonreducedness, and the all-field count jointly. This is a best-knowledge comparison, not a claim of exhaustive bibliographic coverage.

## Limitations

Only augmented homomorphisms are counted. The descriptions are for the square multivariable truncation with two generators and common prime exponent; no statement is asserted for arbitrary exponent vectors or more generators. The exact scheme structure transverse to the thickened component is not computed (only generic nonreducedness is shown). An equivalent theorem in unlocated specialized literature remains a material originality risk. This research has undergone self-review only, not independent validation.

## References

- A. Premet, *Regular derivations of truncated polynomial rings*, arXiv:1405.2426, first posted 10 May 2014; accessible full text: https://arxiv.org/pdf/1405.2426.
- S. Deo and J. K. Maitra, *Automorphism groups of truncated polynomial algebras*, National Academy Science Letters 20 (1997), 5–6; scanned original consulted.
- V. Angeltveit, T. Gerhardt, M. A. Hill and A. Lindenstrauss, *On the algebraic K-theory of truncated polynomial algebras in several variables*, arXiv:1206.0247 (2012), background only.
