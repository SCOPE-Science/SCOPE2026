# Prime-order symmetry components of full-support evolution algebras

## Finding

Fix an integer \(n\ge4\) and a field \(k\). Let \(\mathcal X_n\) be the parameter space of matrices \(B=(b_{ij})\in\operatorname{GL}_n(k)\) with \(b_{ii}=1\) and \(b_{ij}\ne0\) for every \(i\ne j\). The matrix defines a perfect evolution algebra with natural basis \(e_1,\ldots,e_n\) via \(e_j^2=\sum_i b_{ij}e_i\) and \(e_ie_j=0\) for distinct indices. These are exactly the diagonal-normalized representatives of full-support perfect evolution algebras; their ordinary \(k\)-linear automorphism groups equal their simultaneous row-column permutation stabilizers in \(S_n\).

Put \(N=n(n-1)\). Over an algebraic closure of any ground field, define the *symmetry locus* \(\mathcal D_n\subset\mathcal X_n\) to be the set of matrices with a nonidentity ordinary algebra automorphism. **The irreducible components of \(\mathcal D_n\) are indexed bijectively by the subgroups of prime order in \(S_n\).** If a subgroup has prime order \(p\) and its nonidentity elements have cycle type consisting of \(r\) disjoint \(p\)-cycles and \(n-pr\) fixed points, its component is a nonempty open subvariety of a split torus of codimension
\[
c_{p,r}=r(p-1)(2n-pr-1)
\]
inside \(\mathcal X_n\). The number of distinct components of this type is exactly
\[
\frac{n!}{(p-1)p^r r!(n-pr)!}.
\]
In the finite quotient \(\mathcal X_n/S_n\), the corresponding components are indexed instead by the pairs \((p,r)\) with \(p\) prime and \(1\le r\le\lfloor n/p\rfloor\), with the same codimensions. No assertion is made about nonreduced automorphism group schemes.

The components of maximal dimension are exactly the \(\binom n2\) transposition-fixed components; each has codimension \(2n-3\). Consequently, as prime powers \(q\to\infty\), for a uniform \(B\in\mathcal X_n(\mathbb F_q)\),
\[
\Pr\bigl(\operatorname{Aut}_{\mathbb F_q}(\mathcal E(B))\ne1\bigr)
=\binom n2 q^{-(2n-3)}+O_n\bigl(q^{-(2n-2)}\bigr).
\]
The implied constant depends only on \(n\), not on the characteristic. This probability is only defined when the finite-field parameter space is nonempty; for \(q=2\), it is empty when \(n\ge2\).

For illustration, at \(n=4\) there are six codimension-five components (transpositions), three codimension-six components (double transpositions), and four codimension-eight components (three-cycles). The quotient symmetry locus has three components, of those respective codimensions.

## Assumptions and scope

The phrase *full support* means that all \(n^2\) structure coefficients in some natural basis are nonzero. *Perfect* means \(\mathcal E^2=\mathcal E\), equivalently invertibility of the structure matrix. Isomorphisms and automorphisms are ordinary base-field-linear algebra maps. The parameter space \(\mathcal X_n\) is a Zariski-open subvariety of the split torus \((\mathbb G_m)^N\); the diagonal coefficients have been normalized to \(1\). The geometry and irreducible-component statements refer to the geometric reduced locus of matrices with nonidentity ordinary automorphisms, not to the scheme of infinitesimal automorphisms. The finite quotient is the geometric finite-group quotient by simultaneous index permutations. All geometric assertions hold in arbitrary characteristic.

## Proof

**1. Monomial reduction and unique diagonal normalization.** If \(\phi\) is an algebra isomorphism between perfect evolution algebras, then the images of distinct natural basis vectors multiply to zero. Because the squares of the target basis vectors form a basis, disjointness of supports forces the matrix of \(\phi\) to be monomial. If the new basis has vectors \(e'_i=t_i e_i\), its structure matrix entries change by \(b'_{ji}=t_i^2b_{ji}/t_j\); in particular \(b'_{ii}=t_i b_{ii}\). When every diagonal entry is nonzero, there is a unique scaling \(t_i=b_{ii}^{-1}\) making the diagonal all \(1\). An isomorphism between two already-normalized matrices must therefore have all scaling factors equal to \(1\), and acts by a permutation of the indices. Thus the algebra automorphism group is the ordinary \(S_n\)-stabilizer of \(B\). All full-support perfect algebras are also absolutely simple: any nonzero ideal contains some \(e_i^2\); full support and multiplication by all \(e_j\) then put every \(e_j^2\) into the ideal, and invertibility makes these a basis.

**2. The fixed subtori.** Let \(\Omega=\{(i,j):1\le i,j\le n,\ i\ne j\}\), of size \(N\). For a permutation \(\sigma\in S_n\), a normalized structure matrix is \(\sigma\)-fixed precisely when \(b_{ij}\) is constant on each cyclic orbit of \(\langle\sigma\rangle\) on \(\Omega\). Hence the fixed locus in the ambient coordinate torus is a split torus of dimension equal to the number of these orbits. Its intersection \(F_\sigma\) with \(\mathcal X_n\) is nonempty and geometrically irreducible: the determinant polynomial restricted to the orbit variables has constant term \(1\), so it is not identically zero, and its nonvanishing cuts out a nonempty open torus subset. The symmetry locus is the finite union of these closed-in-\(\mathcal X_n\) sets for nonidentity permutations.

**3. Why the maximal fixed loci have prime order.** Every element \(\sigma\) of composite order has a nonidentity prime-order power \(\tau\); then \(F_\sigma\subseteq F_\tau\). Conversely, distinct prime-order subgroups give incomparable fixed loci. Here is the needed orbital-rigidity lemma. Suppose \(H=\langle\sigma\rangle\) has prime order and \(\tau\) preserves *each individual* \(H\)-orbit on \(\Omega\). The first-coordinate projections of these orbits force \(\tau\) to preserve every \(H\)-orbit on vertices. On each nontrivial vertex orbit, preserving the ordered-pair orbit of \((x,\sigma x)\) forces \(\tau\sigma x=\sigma\tau x\), so \(\tau\) is a power \(\sigma^{a_C}\) on that orbit. Preserving the ordered-pair orbit between any two nontrivial vertex orbits forces their exponents \(a_C\) to agree modulo \(p\). Fixed vertices stay fixed. Therefore \(\tau=\sigma^a\) globally, for some \(a\). If the fixed locus of one prime subgroup \(H\) were included in that of another prime subgroup \(K\), then the equality constraints defining \(F_H\) would force the generator of \(K\) to preserve every \(H\)-orbital. The lemma would give \(K\subseteq H\), hence equality. Thus the prime-order fixed loci are precisely the irreducible components.

**4. Exact component dimensions and multiplicities.** If \(\sigma\) has order \(p\), with \(r\) moved \(p\)-cycles and \(f=n-pr\) fixed vertices, exactly \(f(f-1)\) ordered off-diagonal pairs are fixed; every other orbit has size \(p\). Hence its fixed-torus dimension is
\[
o_{p,r}=f(f-1)+\frac{N-f(f-1)}p
=N-r(p-1)(2n-pr-1).
\]
This proves the codimension. Permutations of cycle type \(p^r1^{n-pr}\) number \(n!/[p^r r!(n-pr)!]\). Every subgroup of order \(p\) has exactly \(p-1\) generators of this same cycle type, so division by \(p-1\) proves the component count. A finite quotient preserves dimension of closed invariant images; the \(S_n\)-orbits of these components correspond exactly to conjugacy classes of their prime-order subgroups, namely the pairs \((p,r)\). Thus the quotient-component claim follows.

**5. Maximal dimension is attained only at a transposition.** A transposition moves two vertices, and its codimension is \(2n-3\). If \(\sigma\) moves at least three vertices, then at most \(n-3\) vertices are fixed. Of the \(N\) ordered pairs in \(\Omega\), at most \((n-3)(n-4)\) are fixed by \(\sigma\); every other orbit has size at least \(2\). Consequently
\[
\operatorname{codim}F_\sigma
\ge \frac{N-(n-3)(n-4)}2=3n-6\ge2n-2
\]
for \(n\ge4\). Distinct transpositions give distinct irreducible subtori of the same dimension, hence their pairwise intersections have dimension at least one less than their individual dimensions. The \(\binom n2\) transposition components are therefore precisely the top-dimensional components.

**6. Sharp finite-field asymptotics.** Let \(d_\sigma\) denote the number of orbital variables in step 2. Over \(\mathbb F_q\), the ambient fixed torus has \((q-1)^{d_\sigma}\) points. The determinant has total degree at most \(n\) and is a nonzero polynomial in those variables, so a standard finite-field polynomial-zero bound shows
\[
|F_\sigma(\mathbb F_q)|=(q-1)^{d_\sigma}+O_n(q^{d_\sigma-1}).
\]
In particular, \(|\mathcal X_n(\mathbb F_q)|=(q-1)^N+O_n(q^{N-1})\). The \(\binom n2\) transposition loci each contribute \((q-1)^{N-2n+3}+O_n(q^{N-2n+2})\). Their intersections contribute only \(O_n(q^{N-2n+2})\), since distinct fixed subtori are incomparable. All other prime-order components also have codimension at least \(2n-2\). Finite inclusion-exclusion gives
\[
|\mathcal D_n(\mathbb F_q)|
=\binom n2(q-1)^{N-2n+3}+O_n(q^{N-2n+2}).
\]
Dividing by \(|\mathcal X_n(\mathbb F_q)|\) establishes the claimed probability with its sharp constant and exponent.

## Verification

The standalone standard-library program `artifacts/check_symmetry_locus.py` independently constructs every prime-order permutation of degrees \(4,5,6\); computes its orbits on ordered off-diagonal pairs; checks both the codimension formula and the orbital-rigidity lemma by testing every possible permutation. It also directly enumerates all normalized full-support matrices over \(\mathbb F_2\) and \(\mathbb F_3\) in degree \(4\), tests invertibility and nontrivial automorphisms, and independently enumerates selected prime-order fixed loci for degree \(4\) over \(\mathbb F_3,\mathbb F_5\), and degree \(5\) over \(\mathbb F_3\). Successful output ends with `ALL_PRIME_ORDER_SYMMETRY_CHECKS_PASSED`. These are finite tests; the theorem for all \(n\ge4\) and all fields rests on the preceding proof.

## Relationship to prior work

Wei and Zou (2023) establish the general monomial-orbit formulation and Burnside enumeration for perfect evolution algebras over finite fields, with explicit total class counts in dimensions \(2\), \(3\), and \(4\). Their framework supplies the equivalence principle in step 1; neither their total-class formulas nor the monomial-action statement identifies the prime-order geometric components or the sharp all-dimensional rare-symmetry probability given here. Costoya, Muñoz, Tocino, and Viruel (2023) construct simple Cayley evolution algebras realizing specified automorphism groups. Costoya, Mayorga, and Viruel (2025) analyze permutation representations, faithfulness, and high-transitivity restrictions on automorphism groups. Those results concern realizability and restrictions, not this complete symmetry-discriminant geometry and leading finite-field density.

Exact dimension-three automorphism-order counts for full-support perfect evolution algebras address a different range and invariant. The present theorem applies for \(n\ge4\): it classifies symmetry-locus components in all those dimensions and determines their leading arithmetic density, rather than enumerating individual small-dimensional groups. The group-orbital argument is related to the classical theory of colored directed graph stabilizers; the claimed contribution is its explicit realization in the normalized algebra parameter variety and the complete prime-subgroup component and codimension formulas.

## Limitations

This theorem does not treat evolution algebras with zero structure coefficients, nonperfect structure matrices, or the complete finite-field distribution of every possible automorphism subgroup. It counts geometric symmetry-locus components and the *first* asymptotic term, not all terms of the finite-field counting polynomial. Over very small fields the open parameter set may have no rational points. No assertion about scheme-theoretic infinitesimal stabilizers or publication priority beyond the inspected sources is made. A general theorem on fixed-locus arrangements for weighted directed graphs could potentially subsume part of the present argument; that remains an originality risk. No independent audit has been performed.

## References

1. Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368, first public arXiv version 18 October 2023, https://arxiv.org/abs/2310.12368 .
2. C. Costoya, V. Muñoz, A. Tocino, and A. Viruel, *Automorphism groups of Cayley evolution algebras*, RACSAM 117 (2023), article 82, https://doi.org/10.1007/s13398-023-01414-w .
3. C. Costoya, P. Mayorga, and A. Viruel, *Permutation representations and automorphisms of evolution algebras*, arXiv:2401.05924 (2024), https://arxiv.org/abs/2401.05924 ; published in Mediterranean Journal of Mathematics 22 (2025), article 149.
