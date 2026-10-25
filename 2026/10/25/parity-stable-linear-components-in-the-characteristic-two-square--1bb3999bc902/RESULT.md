# Parity-stable linear components in the characteristic-two square-zero derivation cone

## Finding
For every field \(k\) of characteristic \(2\) and every integer \(m\ge1\), let
\[
A_n=k[t]/(t^n),\qquad \mathcal X_n=\{D\in\operatorname{Der}_k(A_n):D^2=0\}_{\mathrm{red}}.
\]
The two reduced affine varieties \(\mathcal X_{2m}\) and \(\mathcal X_{2m+1}\) are linearly isomorphic. Each has exactly \(\lfloor m/2\rfloor+1\) geometrically irreducible components; these are distinct \(m\)-dimensional affine-linear subspaces. More precisely, put \(c=\lceil m/2\rceil\), \(S=k[s]/(s^m)\), and
\[
L_j=\{(a,b)\in S^2:a\in s^{m-j}S,\ b\in s^jS\},\qquad c\le j\le m.
\]
Then each \(\mathcal X_n\) is identified with \(\bigcup_{j=c}^{m} L_j\), and for \(c\le j<\ell\le m\),
\[
\dim L_j=m,\quad \dim(L_j\cap L_\ell)=m-(\ell-j).
\]
For every finite field \(\mathbb F_q\) of characteristic \(2\),
\[
\#\mathcal X_{2m}(\mathbb F_q)=\#\mathcal X_{2m+1}(\mathbb F_q)
=q^m+\lfloor m/2\rfloor(q-1)q^{m-1}.
\]
The coefficient correspondence also preserves the rank of each square-zero derivation. Exactly \((q-1)q^{m-1}\) derivations on \(A_{2m}\) have vanishing homology as complexes of vector spaces; no square-zero derivation on the odd-dimensional algebra \(A_{2m+1}\) is acyclic.

## Assumptions and scope
All derivations are \(k\)-linear, act on the underlying ungraded algebra, and satisfy the Leibniz rule. The condition \(D^2=0\) means vanishing of the composite linear map, equivalently vanishing of the characteristic-two restricted Lie square. No grading on \(A_n\) or degree-one condition on \(D\) is assumed. The variety is the **reduced** locus, not the possibly nonreduced zero scheme of the matrix entries of \(D^2\). The geometric assertions hold after extension to an algebraic closure of any characteristic-two field. The point counts additionally require \(k=\mathbb F_q\), \(q\) a power of two.

## Proof
**1. Coordinates for derivations.** A derivation of \(A_n\) is determined by \(f=D(t)\). Applying \(D\) to \(t^n=0\) gives \(n t^{n-1}f=0\). In characteristic two, \(f\) is arbitrary when \(n=2m\), whereas \(f\in tA_{2m+1}\) when \(n=2m+1\). Put \(S=k[s]/(s^m)\), \(s=t^2\). Every derivation on \(A_{2m}\) is uniquely encoded by \((a,b)\in S^2\) through \(D(t)=a(t^2)+t b(t^2)\). Every derivation on \(A_{2m+1}\) is uniquely encoded by the **same** pair via \(D(t)=t^2a(t^2)+t b(t^2)\). These give \(k\)-linear affine-space identifications of the two derivation spaces with \(S^2\).

**2. Exact square-zero equation.** The composite \(D^2\) is a derivation in characteristic two: the mixed terms in the Leibniz expansion cancel. It therefore vanishes exactly when \(D^2(t)=0\). Formal differentiation gives \(D^2(t)=f(t)f'(t)\). In either coordinate model, \(f'(t)=b(t^2)\). For \(n=2m\), compare the even and odd powers of \(t\) to obtain \(a b=0\) and \(b^2=0\) in \(S\). For \(n=2m+1\), the equalities are \(t^2ab=0\) and \(t b^2=0\) modulo \(t^{2m+1}\), again exactly \(ab=b^2=0\) in \(S\). The comparison is coefficientwise and holds over any field of characteristic two.

**3. Reduced components and dimensions.** Work first over an algebraic closure of \(k\). Since \(S\) is a truncated discrete valuation algebra, \(b^2=0\) is equivalent on field-valued points to \(b\in s^cS\), where \(c=\lceil m/2\rceil\). If \(b\ne0\) has \(s\)-order \(j\) (necessarily \(c\le j<m\)), then \(ab=0\) holds exactly when \(a\in s^{m-j}S\); when \(b=0\), take \(j=m\). Thus the underlying set equals \(\bigcup_{j=c}^{m}L_j\). Each \(L_j\) is a closed linear space with \(j\) free coefficients of \(a\) and \(m-j\) free coefficients of \(b\), hence has dimension \(m\). None is contained in another: increasing \(j\) relaxes the restriction on \(a\) and tightens that on \(b\). Thus these are exactly the irreducible components of the **reduced** variety. Their intersection has \(j\) free coefficients of \(a\) and \(m-\ell\) free coefficients of \(b\), establishing the formula. All spaces are defined over \(k\), proving geometric irreducibility and the linear isomorphism between adjacent truncation lengths.

**4. Rational-point count.** For \(j>c\), the intersection of \(L_j\) with the union of all preceding components \(L_c\cup\cdots\cup L_{j-1}\) is exactly \(L_j\cap L_{j-1}\), an \((m-1)\)-dimensional subspace: the other pairwise intersections lie inside it. The first component has \(q^m\) points; each subsequent component contributes \(q^m-q^{m-1}\). There are \(m-c=\lfloor m/2\rfloor\) subsequent components, proving the count.

**5. Differential ranks and acyclic locus.** Let \(v_s(0)=m\) and let \(v_s(a),v_s(b)\) denote truncated \(s\)-valuations. A derivation vanishes on all even powers of \(t\), and on odd powers it sends \(t^{2i+1}\) to \(t^{2i}D(t)\). Under either coordinate identification, the first vanishing product is at \(i=m-\min(v_s(a),v_s(b))\); its preceding successive products are linearly independent. Therefore
\[
\operatorname{rank}_k D=m-\min(v_s(a),v_s(b)).
\]
In dimension \(2m\), the maximal rank \(m\) is equivalent to \(a\) being a unit (the condition \(ab=0\) then forces \(b=0\)). There are precisely \((q-1)q^{m-1}\) such \(a\); their image equals their kernel, hence homology vanishes. A square-zero operator on an odd-dimensional space cannot be acyclic because its rank is at most \(\lfloor n/2\rfloor\).

## Verification
The standalone program `verify_char2_derivations.py` exhaustively constructs all derivations by their generator images, directly computes the Leibniz derivative matrices and their squares, and independently tests component membership and matrix ranks over \(\mathbb F_2\) (\(1\le m\le5\)) and \(\mathbb F_4\) (\(1\le m\le3\)), at both truncation lengths in every case. The tests cover sixteen field/truncation pairs, including the acyclic counts and rank distributions. The program prints `CHAR2_DERIVATION_SQUARE_ZERO_OK` on success. The infinite-family statements follow from the preceding proof, not from finite enumeration.

## Relationship to prior work
Premet's *Regular derivations of truncated polynomial rings* (first public version May 10, 2014; arXiv:1405.2426) studies regular derivations and invariant-theoretic fibres of Jacobson–Witt derivation algebras over algebraically closed fields of characteristic strictly greater than two, with exponents equal to the characteristic. The present theorem instead classifies the reduced **square-zero** cone in characteristic two for every one-variable truncation length, including its components and exact finite-field arithmetic. Those claims are not asserted by the inspected regular-derivation theorems. The broader theory of \(p\)-complexes provides context for square-zero linear maps but does not supply these algebra-specific equations or component counts.

## Limitations
Only characteristic two is covered. The equations define a potentially nonreduced scheme; this theorem identifies its reduction, not its scheme-theoretic multiplicities. The counts concern labelled derivations, not conjugacy orbits under algebra automorphisms. The acyclic statement concerns the ungraded vector-space complex \((A_n,D)\), not an assertion that \(D\) has cohomological degree one. Independent mathematical audit and exhaustive historical priority verification have not been performed.

## References
1. A. Premet, *Regular derivations of truncated polynomial rings*, arXiv:1405.2426, first submitted 2014-05-10, v3 2014-07-22. https://arxiv.org/abs/1405.2426 ; full text https://arxiv.org/html/1405.2426v3 .
2. *Free \((\mathbb Z/p)^n\)-complexes and \(p\)-DG modules*, Journal of Algebra (2020), DOI: 10.1016/j.jalgebra.2020.07.028, introductory definitions and §6 (context only, not a source of the theorem). https://doi.org/10.1016/j.jalgebra.2020.07.028 .
