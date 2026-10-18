# Frobenius-transitive branch loci on eight-point ternary hyperelliptic curves

## Finding

For every integer \(g\ge2\), there is a smooth hyperelliptic curve over \(\mathbf F_3\) with **eight rational points** and an arithmetically irreducible hyperelliptic branch divisor: all \(2g+2\) Weierstrass branch points form **one Frobenius orbit**. More precisely, for even \(n=2g+2\), let
\[
\mathcal I_n=\{P\in\mathbf F_3[T]: P\text{ monic irreducible},\ \deg P=n,\ P(0)=P(1)=P(-1)=1\}.
\]
Then \(\mathcal I_n\ne\varnothing\) for every even \(n\ge6\), and its cardinality is given by the formula below.

Define, for positive even \(d\),
\[
A_d=\frac{3^d-15-2(-3)^{d/2}}8,
\qquad
B_{n,d}=\begin{cases}3^d-3,&n/d\text{ even},\\ A_d,&n/d\text{ odd}.\end{cases}
\]
The exact equation count is
\[
\boxed{|\mathcal I_n|=\frac1n\sum_{d\mid n}\mu(n/d)B_{n,d}.}
\]
For \(n=6,8,10,12\), this gives respectively \(12,90,720,5460\). In the odd-quotient case, \(d\) is necessarily even. These are counts of **monic defining polynomials**, not isomorphism classes of curves.

## Assumptions and scope

All fields and morphisms are over \(\mathbf F_3\) unless explicitly extended. The integer \(n\) is even and at least six, and \(g=(n-2)/2\). The curve associated with a polynomial \(P\in\mathcal I_n\) is the smooth projective completion of \(y^2=P(x)\). A degree-\(n\) closed branch point means one Frobenius orbit of \(n\) geometrically distinct points on \(\mathbf P^1\), not one nonreduced geometric point. No uniqueness up to curve isomorphism is asserted. The bound of eight rational points is the established sharp hyperelliptic bound over \(\mathbf F_3\) for \(g\ge2\) [FG].

## Proof

**1. Geometry of the cover.** An irreducible polynomial over a finite field is separable. Thus \(P\) has exactly \(n\) distinct geometric roots, transitive under Frobenius. The degree-two map \(x:C_P\to\mathbf P^1\) ramifies precisely at these \(n\) roots because \(n\) is even and the characteristic is not two. Riemann--Hurwitz gives \(2g-2=-4+n\), hence genus \(g=(n-2)/2\). Each of the three finite rational fibres \(x=0,1,-1\) has two rational points because \(P(a)=1\). At infinity the leading coefficient is \(1\), again giving two rational points (the local equation has two branches with limiting \(y/x^{n/2}=\pm1\)). Hence \(\#C_P(\mathbf F_3)=8\), and the branch divisor is a single degree-\(n\) closed point.

**2. Character counting.** For even positive \(m\), set \(K=\mathbf F_{3^m}\), and let \(\chi\) be its quadratic character extended by \(\chi(0)=0\). Define
\[
S_m=\{\alpha\in K\setminus\mathbf F_3:\ \chi(\alpha-a)=1\text{ for all }a\in\mathbf F_3\}.
\]
Because \(m\) is even, \(\chi(-1)=1\). Expanding \(\prod_{a\in\mathbf F_3}(1+\chi(X-a))\) and summing over \(X\in K\), the three singleton sums vanish and each of the three pair sums equals \(-1\). At each \(a\in\mathbf F_3\) the product equals \(4\), so removal of those three points subtracts \(12\). For \(\alpha\notin\mathbf F_3\), the product is \(8\) exactly on \(S_m\), and zero otherwise. Therefore
\[
8|S_m|=3^m-15+\sum_{\alpha\in K}\chi(\alpha^3-\alpha).
\]
The elliptic curve \(E:y^2=x^3-x\) over \(\mathbf F_3\) has four rational points (the three affine zeros and infinity), so its Frobenius trace is zero and its characteristic polynomial is \(U^2+3\). Consequently, by the usual elliptic-curve point-count recurrence,
\[
\sum_{\alpha\in\mathbf F_{3^m}}\chi(\alpha^3-\alpha)=-2(-3)^{m/2}
\]
for even \(m\). It follows that \(|S_m|=A_m\), exactly as defined above.

**3. Subfield correction and irreducibility.** Fix even \(n\). For each divisor \(d\mid n\), restrict the quadratic character of \(\mathbf F_{3^n}\) to the nonzero elements of \(\mathbf F_{3^d}\). If \(n/d\) is even, it is trivial, so all \(3^d-3\) elements outside \(\mathbf F_3\) satisfy the three square conditions. If \(n/d\) is odd, then \(d\) is even and the restricted character is the quadratic character of \(\mathbf F_{3^d}\), giving exactly \(A_d\) qualifying elements. Denote these quantities by \(B_{n,d}\). The number of elements of exact degree \(n\) satisfying the three conditions is, by Möbius inversion on subfields,
\[
\sum_{d\mid n}\mu(n/d)B_{n,d}.
\]
An element \(\alpha\) of exact degree \(n\) has monic minimal polynomial \(P_\alpha\) of degree \(n\), and for every \(a\in\mathbf F_3\),
\[
\chi_{\mathbf F_{3^n}}(a-\alpha)
=\chi_{\mathbf F_3}\bigl(\operatorname{Norm}_{\mathbf F_{3^n}/\mathbf F_3}(a-\alpha)\bigr)
=\chi_{\mathbf F_3}(P_\alpha(a)).
\]
Here \(\operatorname{Norm}(a-\alpha)=P_\alpha(a)\), and the unique nonzero square of \(\mathbf F_3\) is \(1\). Thus the three square conditions are equivalent to \(P_\alpha(0)=P_\alpha(1)=P_\alpha(-1)=1\). Every degree-\(n\) minimal polynomial has exactly \(n\) conjugate roots. Division by \(n\) proves the boxed count.

**4. Nonemptiness in every genus.** The lower bound
\[
|S_n|\ge\frac{3^n-15-2\,3^{n/2}}8
\]
holds for even \(n\). Every element of degree strictly below \(n\) lies in a proper subfield, each of which is contained in a subfield of degree at most \(n/2\). An overcount for the union of these subfields is \(\sum_{j=1}^{n/2}3^j<\tfrac32\,3^{n/2}\). Writing \(t=3^{n/2}\ge27\), the strict inequality \(t^2-14t-15>0\) implies \(|S_n|>\tfrac32t\). Hence some qualifying element has degree exactly \(n\); its minimal polynomial belongs to \(\mathcal I_n\). This establishes existence uniformly for all \(g\ge2\).

## Verification

Two separate pure-Python programs requiring no external packages are included: `COUNT.py` implements the Möbius formula and independently enumerates every admissible monic polynomial through degree twelve using irreducibility checks; `CHARACTER_CHECK.py` independently constructs \(\mathbf F_{3^6}\) and \(\mathbf F_{3^8}\) and counts square-character triples and exact-degree elements. Reproduce with `python3 COUNT.py` and `python3 CHARACTER_CHECK.py`. Their outputs are included as `COUNT_OUTPUT.txt` and `CHARACTER_OUTPUT.txt`. Both finite checks are corroboration; the four mathematical steps above prove the infinite family and exact formula.

## Relationship to prior work

Faber--Grantham [FG] already prove that eight is the sharp attainable rational-point count of a genus-at-least-two hyperelliptic curve over \(\mathbf F_3\). This sharp bound and mere existence of eight-point curves are **not new claims**. The additional simultaneous constraints here are a **single Frobenius orbit** on the entire branch divisor in every genus and the **explicit exact number of irreducible defining polynomials** meeting those conditions. Vermeulen [V] also proves eventual attainment of the maximal gonality point count over odd fields by a toric construction, without classifying branch Frobenius orbits. Gao--Kuttner--Wang [GKW] study prescribed leading or terminal coefficients, and Slavov [S] studies large-field factorization statistics in short polynomial intervals. None of these inspected texts states this fixed-ternary all-degree branch-transitivity and count theorem. Known small-genus classifications can cover individual genus-two examples and are not claimed as new.

## Limitations

The formula counts normalized monic equations, not isomorphism classes, Jacobian isogeny classes, or automorphism orbits. The arithmetic structure of the Jacobians and counts over extension fields are not classified. Earlier work on prime polynomials in arithmetic progressions may contain adaptable general methods or a previously implicit exact computation for this particular modulus, and unindexed earlier identical formulas remain a priority risk; these are not independently excluded. No claim of independent external validation is made.

## References

- [FG] X. Faber and J. Grantham, *Ternary and Quaternary Curves of Small Fixed Genus and Gonality with Many Rational Points* (first public 2020-10-15), arXiv:2010.07992, https://arxiv.org/abs/2010.07992 . Theorem 2.4 and its proof.
- [V] F. Vermeulen, *Curves of fixed gonality with many rational points* (first public 2021-02-01), arXiv:2102.00900, https://arxiv.org/abs/2102.00900 . Theorem 1.1 and geometric construction.
- [GKW] Z. Gao, B. Kuttner and Q. Wang, *Counting Irreducible Polynomials with Prescribed Coefficients over a Finite Field* (public 2021-09-05), arXiv:2109.02000, https://arxiv.org/abs/2109.02000 .
- [S] K. Slavov, *Factorization type probabilities of polynomials with prescribed coefficients over a finite field* (first public 2019-03-21), arXiv:1903.09050, https://arxiv.org/abs/1903.09050 .
