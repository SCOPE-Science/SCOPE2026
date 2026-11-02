# The Weierstrass semigroup of a non-Galois twisted Artin–Schreier cover

## Finding

**Theorem.** Let \(k\) be an algebraically closed field of odd prime characteristic \(p\ge3\). Let \(f(u)\in k[u]\) have degree \(d\ge2\), with nonzero leading coefficient and \(\gcd(p,d-1)=1\). Let \(C_f\) be the smooth projective normalization of the irreducible affine curve
\[
 u v^p-v=f(u).
\]
There is a unique point \(P_\infty\) of \(C_f\) above \(u=\infty\), and
\[
 g(C_f)=\frac{(p-1)d}{2},\qquad
 H(P_\infty)=\left\langle p,\ p+j(d-1)\ (1\le j\le p-1)\right\rangle.
\]
The displayed \(p\) integers are its **minimal** system of generators, so the semigroup has multiplicity and embedding dimension both equal to \(p\). Writing \(m=d-1\), its Apéry set with respect to \(p\) is
\[
 \operatorname{Ap}(H(P_\infty),p)=\{0\}\cup\{p+jm:1\le j\le p-1\}.
\]
The Frobenius number, conductor, pseudo-Frobenius set and numerical-semigroup type are respectively
\[
 (p-1)m,\qquad (p-1)m+1,\qquad
 \{m,2m,\ldots,(p-1)m\},\qquad p-1.
\]
In particular, the one-point semigroup depends only on \(p\) and \(\deg f\), not on the other coefficients of \(f\). For \(p\ge3\), the degree-\(p\) covering \(C_f\to\mathbb P^1_u\) is non-Galois.

## Assumptions and scope

The characteristic \(p\) is an **odd prime**, \(k\) is algebraically closed, \(d\ge2\) and \(p\nmid d-1\). The statement concerns the smooth projective normalization of the affine equation and its point at infinity; no smoothness claim about a chosen projective plane closure is needed. The Weierstrass semigroup \(H(P)\) consists of nonnegative pole orders of rational functions whose entire pole divisor is supported at \(P\). The geometric genus and semigroup are calculated over \(k\); finite-field rational-point claims are not made. The first relevant public literature source dates to May 28, 2026 (Zhang–Zhao, arXiv:2605.29311).

## Proof

**1. A smooth Artin–Schreier cover and its tame quotient.** Put \(m=d-1\) and \(M=1+(p-1)d\). Consider the smooth projective model \(W\) of
\[
 y^p-y=x f(x^{p-1}).
\]
The polynomial on the right has degree \(M\), and \(M\equiv1-d\not\equiv0\pmod p\). A polynomial of degree prime to \(p\) cannot be an Artin–Schreier coboundary \(h^p-h\) in \(k(x)\) (a rational coboundary with no finite poles must be polynomial, and its positive degree is divisible by \(p\)). Thus \(W\to\mathbb P^1_x\) is a connected separable Artin–Schreier cover of degree \(p\), unramified over finite \(x\), with precisely one point \(Q_\infty\) over infinity. Standard local Artin–Schreier ramification gives
\[
 g(W)=\frac{(p-1)(M-1)}2=\frac{(p-1)^2d}{2},
 \qquad \operatorname{ord}_{Q_\infty}(x)=-p,\quad
 \operatorname{ord}_{Q_\infty}(y)=-M.
\]

Every \(\zeta\in\mathbb F_p^\times\) acts on \(W\) by \((x,y)\mapsto(\zeta x,\zeta y)\), since \(\zeta^{p-1}=1\) and \(\zeta^p=\zeta\). Define invariant functions \(u=x^{p-1}\) and \(v=y/x\). Direct substitution yields \(u v^p-v=f(u)\). Conversely, \(x^{p-1}=u\) and \(y=xv\), so \(k(W)=k(u,v)(x)\). The faithful scalar group has order \(p-1\), and the extension has precisely that degree; hence \(k(C_f)=k(W)^{\mathbb F_p^\times}=k(u,v)\). This also establishes irreducibility of the defining equation and identifies \(C_f=W/\mathbb F_p^\times\).

**2. The quotient genus and infinity.** The scalar action fixes \(Q_\infty\). At a finite point it can fix a nonidentity scalar only if \(x=y=0\): if \(x=0\), the Artin–Schreier equation forces \(y\in\mathbb F_p\), and only \(y=0\) is fixed. Consequently, the tame degree-\(p-1\) quotient \(W\to C_f\) has exactly two branch points, both totally ramified. Riemann–Hurwitz gives
\[
 2g(W)-2=(p-1)(2g(C_f)-2)+2(p-2),
\]
which simplifies to \(g(C_f)=(p-1)d/2\). Since \(W\) has a unique point over \(x=\infty\), the quotient has a unique point \(P_\infty\) over \(u=\infty\), and its pullback is \((p-1)Q_\infty\).

**3. Explicit one-pole functions.** On \(W\), the invariant \(u=x^{p-1}\) has only pole \(Q_\infty\) of order \(p(p-1)\). For \(1\le j\le p-1\), the invariant functions
\[
 u v^j=x^{p-1-j}y^j
\]
are polynomials in \(x,y\), hence have no finite poles, and have pole orders
\[
 (p-1-j)p+jM=(p-1)\bigl(p+jm\bigr)
\]
at \(Q_\infty\). Divide by the tame ramification index \(p-1\) to obtain on \(C_f\)
\[
 \operatorname{pole}_{P_\infty}(u)=p,
 \qquad\operatorname{pole}_{P_\infty}(uv^j)=p+jm.
\]
Thus the numerical semigroup \(T=\langle p,p+m,p+2m,\ldots,p+(p-1)m\rangle\) is contained in \(H(P_\infty)\).

**4. Exact Apéry set and equality by genus.** Because \(\gcd(p,m)=1\), the \(p\) numbers \(0,p+m,\ldots,p+(p-1)m\) have pairwise distinct residues modulo \(p\). Every positive element of \(T\) is of the form \(ap+tm\), where \(a\ge1\) if \(t>0\), and \(t\ge0\) is a sum of indices between \(1\) and \(p-1\). A number congruent to \(jm\pmod p\), for \(1\le j\le p-1\), must have \(t\equiv j\pmod p\); its smallest possible positive \(t\) is \(j\), so its least possible value is \(p+jm\). This proves the displayed Apéry set. The classical Apéry gap formula yields
\[
 g(T)=\frac1p\sum_{j=1}^{p-1}(p+jm)-\frac{p-1}{2}
 =\frac{(p-1)(m+1)}2=g(C_f).
\]
The Weierstrass gap theorem gives exactly \(g(C_f)\) gaps at \(P_\infty\). Since \(T\subseteq H(P_\infty)\) and their gap counts coincide, equality holds.

**5. Minimality, conductor and type.** The Apéry argument also shows that each \(p+jm\) cannot be expressed as a sum of two positive elements of \(T\): any such representation would require at least two positive generator terms but the least representative in its residue contains precisely one; subtracting a multiple of \(p\) contradicts Apéry minimality. Hence all displayed generators are indispensable. The maximal Apéry element is \(p+(p-1)m\), so the Frobenius number is \((p-1)m\), and the conductor is one more. For each \(1\le j\le p-1\), the integer \(jm\) is a gap and adding any generator yields a nongap: adding \(p\) gives \(p+jm\), while adding \(p+\ell m\) gives \(p+(j+\ell)m\), which is either an explicit generator (if \(j+\ell<p\)) or a generator/nonnegative multiple of \(p\) (otherwise). Conversely, every pseudo-Frobenius number must equal an Apéry element minus \(p\). Thus the pseudo-Frobenius set is exactly \(\{m,2m,\ldots,(p-1)m\}\), of cardinality \(p-1\).

**6. Non-Galois nature of the degree-\(p\) projection.** Above \(u=0\), the points \((x,y)=(0,b)\), \(b\in\mathbb F_p^\times\), form a free scalar orbit and descend to a place of \(C_f\) with ramification index \(p-1\) over \(u=0\), since \(W\to\mathbb P^1_u\) has index \(p-1\) there while \(W\to C_f\) is unramified at that orbit. However \([k(C_f):k(u)]=p\), and the index \(p-1\) does not divide \(p\) for \(p\ge3\). Therefore \(k(C_f)/k(u)\) cannot be Galois.

## Verification

The standalone script `verify_semigroup_twisted.py` uses exact integers and exhaustively checks the claimed Apéry sets, gaps, maximal embedding dimension, minimal generators, Frobenius numbers, conductors, pseudo-Frobenius sets, and the Riemann–Hurwitz and pole identities for 324 admissible parameter pairs with \(p\in\{3,5,7,11,13,17,19\}\) and \(2\le d\le54\). It returns `VERIFY_OK`. These are finite checks of formulas, not a replacement for the all-parameter arguments in the proof.

Examples: for \(p=3,d=5\), one gets \(H(P_\infty)=\langle3,7,11\rangle\), genus \(5\), Frobenius number \(8\), and type \(2\). For \(p=5,d=3\), one gets \(H(P_\infty)=\langle5,7,9,11,13\rangle\), genus \(6\), Frobenius number \(8\), and type \(4\).

## Relationship to prior work

Zhang and Zhao, *Weierstrass semigroups at totally ramified places of degree one on linearized function fields* (arXiv:2605.29311, May 28, 2026), study separable **constant-coefficient** linearized extensions \(L(y)=f(x)/g(x)\), in particular Galois extensions of a rational field. Their Proposition 3.4, Corollary 3.6 and Theorem 3.8 give gap, generator, and symmetry descriptions under those hypotheses. The cover \(C_f\to\mathbb P^1_u\) here is non-Galois and has a variable coefficient of \(v^p\), so the formulas are not direct specializations of their stated hypotheses. Their broader motivation for explicit one-point semigroups is adopted here.

Zhang and Zhao, *Weierstrass semigroups at totally ramified places of degree one on Kummer extensions* (arXiv:2605.14583, May 14, 2026), address cyclic Kummer extensions of rational function fields, not the non-Galois degree-\(p\) covers considered here. The literature on Hermitian subcovers and Artin–Schreier curves provides background methods, but is not asserted to exclude every possible implicit equivalent theorem. The scalar-quotient construction, full minimal generators, and pseudo-Frobenius type are the narrowly assessed claims.

## Limitations

The proof assumes odd prime characteristic, algebraically closed ground field, \(d\ge2\), and \(p\nmid d-1\); it makes no assertion when the pole-degree congruence fails or for arbitrary nonpolynomial right-hand sides. It determines the one-point semigroup, not all multi-point semigroups, complete Riemann–Roch bases, code parameters, automorphism groups, or rational-point counts. The full historical literature may contain an equivalent computation under a different curve presentation; no independent mathematical audit has been performed.

## References

1. H. Zhang and C.-A. Zhao, *Weierstrass semigroups at totally ramified places of degree one on linearized function fields*, arXiv:2605.29311 (first public version May 28, 2026), especially Section 3.
2. H. Zhang and C.-A. Zhao, *Weierstrass semigroups at totally ramified places of degree one on Kummer extensions*, arXiv:2605.14583 (May 14, 2026), especially Section 1 and the Kummer-extension hypotheses.
3. Standard Artin–Schreier different/genus and tame Riemann–Hurwitz formulas; standard Apéry-set genus formula and Weierstrass gap theorem (used with explicit derivations above).
