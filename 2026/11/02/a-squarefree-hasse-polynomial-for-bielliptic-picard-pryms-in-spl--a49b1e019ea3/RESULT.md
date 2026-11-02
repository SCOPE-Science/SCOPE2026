# A squarefree Hasse polynomial for bielliptic Picard Pryms in split characteristics

## Finding

Let \(p=6m+1\) be a prime, \(m\geq1\), and let \(k\) be an algebraically closed field of characteristic \(p\). For every \((a,b)\in k^2\) satisfying \(b(a^2-4b)\ne0\), let \(C_{a,b}\) be the smooth genus-three curve
\[
 C_{a,b}:\quad y^3=x^4+a x^2+b,
\]
and let \(P_{a,b}\) be the Prym abelian surface of the involution \((x,y)\mapsto(-x,y)\). Define the explicit weighted-homogeneous polynomial
\[
 H_m(a,b)=[z^{3m}](z^2+az+b)^{2m}
 =\sum_{j=0}^{\lfloor m/2\rfloor}
 \frac{(2m)!}{(m+j)!(m-2j)!j!}\,a^{m-2j}b^j
 \pmod p.
\]
Then the Prym is **ordinary exactly when \(H_m(a,b)\ne0\)** and **superspecial exactly when \(H_m(a,b)=0\)**. In the latter case, its \(p\)-rank is zero and its \(a\)-number is two. There is no intermediate Prym Newton or Ekedahl–Oort stratum in this family. The elliptic quotient is ordinary everywhere on the smooth locus; accordingly, the Jacobian of \(C_{a,b}\) has \((p\text{-rank},a\text{-number})=(3,0)\) when \(H_m\ne0\), and \((1,2)\) when \(H_m=0\).

The polynomial \(H_m(a,1)\) has degree \(m\), **exactly \(m\) distinct roots over \(k\)**, and no root at \(a=2\) or \(a=-2\). Therefore all nonordinary parameters lie in the smooth family, and the Hasse divisor is reduced on the normalized coefficient line \(b=1\). The geometric number of isomorphism classes of **marked** bielliptic Picard curves with superspecial Pryms is exactly
\[
 \boxed{\left\lceil\frac{m}{2}\right\rceil=\left\lceil\frac{p-1}{12}\right\rceil.}
\]
When \(m\) is odd, exactly one such class has \(a=0\); for even \(m\), no such class has \(a=0\). For illustration, the exceptional marked classes number one for \(p=7\), one for \(p=13\), and two for \(p=19\).

The central polynomial identities, holding in \(\mathbb F_p[a,b]\), are
\[
 \begin{aligned}
 A&=[z^{3m}](z^2+az+b)^{2m}=H_m(a,b),\\
 B&=[z^{3m}](z^2+az+b)^{4m}
 =\frac{\binom{4m}{m}}{\binom{2m}{m}}\,b^m(a^2-4b)^m A,\\
 F&=[z^{6m}](z^2+az+b)^{4m}
 =\binom{4m}{2m}(a^2-4b)^m.
 \end{aligned}
\]
All displayed binomial coefficients and denominators are nonzero modulo \(p\).

## Assumptions and scope

The base field is algebraically closed, and \(p=6m+1\) is prime (thus \(p\ge7\)). No condition is imposed on \(a\) or \(b\) beyond smoothness \(b(a^2-4b)\ne0\). The Prym is the connected two-dimensional kernel of the norm to the genus-one quotient, equivalently the anti-invariant factor of \(\operatorname{Jac}(C_{a,b})\) under the involution. Superspecial means geometrically isomorphic as an **unpolarized** abelian surface to a product of supersingular elliptic curves; it is stronger than supersingular. Isomorphism-class counts refer to the marked curves with their distinguished \(\mu_6\)-action, under the standard coefficient scaling.

## Proof

**1. Cartier diagonalization.** Put \(g(z)=z^2+az+b\) and \(f(x)=g(x^2)\). The differentials
\[
 \omega_1=dx/y,\qquad \omega_2=dx/y^2,\qquad \omega_3=x\,dx/y^2
\]
form a basis of regular differentials on \(C_{a,b}\). The first two span the anti-invariant (Prym) summand, and the last spans the invariant (elliptic) summand. As \(p-1=6m\), use
\[
 \frac{1}{y^j}=\frac{f(x)^{j(p-1)/3}}{y^{jp}}\quad(j=1,2)
\]
inside the Cartier formula, which retains coefficients of \(x^{p\ell+p-1}\,dx\). The parity of \(f(x)\) forces all off-diagonal entries to vanish. The diagonal entries, up to their unique \(p\)-th roots, are precisely \(A\), \(B\), and \(F\) as above. Thus the Prym Cartier operator has rank either two, one, or zero according to the nonvanishing pattern of \(A,B\), and the elliptic Cartier scalar is \(F^{1/p}\).

**2. A pair of uniform coefficient identities.** Write \(D=a^2-4b\) and expand
\[
 g(z)^{4m}=
 \sum_{j=0}^{4m}\binom{4m}{j}(-D/4)^j(z+a/2)^{8m-2j}.
\]
For \(j<m\) one has \(8m-2j=p+(2m-2j-1)\), with second summand between zero and \(2m-1\). Lucas's theorem therefore gives
\[
 \binom{8m-2j}{3m}=\binom{8m-2j}{6m}=0\pmod p.
\]
Consequently \(D^m\) divides both \(B\) and \(F\). The latter is weighted-homogeneous of degree \(2m\) when \(\deg a=1\), \(\deg b=2\); hence \(F/D^m\) is constant. Putting \(b=0\) identifies this constant as \(\binom{4m}{2m}\), proving the formula for \(F\).

For the first identity, every monomial in \(B=[z^{3m}]g^{4m}\) has exponent of \(b\) at least \(m\): if \(u\) factors contribute \(z^2\), then the exponent of \(b\) is \(m+u\). Since \(b\) and \(D\) are coprime in \(k[a,b]\), \(Q=B/(b^mD^m)\) is a polynomial in \(a,b\), weighted-homogeneous of degree \(m\), and of degree at most \(m\) in \(a\).

Here is a direct way to determine \(Q\). For fixed \(b\), coefficient differentiation shows that
\[
 U_{N,n}(a,b)=[t^n](1+at+bt^2)^N
\]
satisfies
\[
 (4b-a^2)\,\partial_a^2U_{N,n}
 +(2N-1)a\,\partial_aU_{N,n}-n(2N-n)U_{N,n}=0.
\]
For completeness, this equation follows by applying the coefficient-of-\(t^n\) operator to the generating identity
\[
 (4b-a^2)\partial_a^2G+(2N-1)a\partial_aG
 -\left(2N\,t\partial_t-(t\partial_t)^2\right)G=0,
 \qquad G=(1+at+bt^2)^N,
\]
which is verified by differentiating the displayed power of the quadratic polynomial. Apply the resulting equation with \((N,n)=(2m,m)\) to \(A\), and with \((N,n)=(4m,5m)\) to \(B\), noting coefficient reversal. The resulting differential equations are
\[
 (4b-a^2)A''+(4m-1)aA'-3m^2A=0,
\]
\[
 (4b-a^2)B''+(8m-1)aB'-15m^2B=0.
\]
Substitute \(B=b^mD^mQ\) into the second equation. Since \(6m+1=p=0\) in \(k\), all extra terms cancel, leaving the **same equation as for \(A\)**:
\[
 (4b-a^2)Q''+(4m-1)aQ'-3m^2Q=0.
\]
The solution space among polynomials in \(a\) of degree at most \(m\) is one-dimensional: a nonzero solution of degree \(d<m\) would have leading coefficient multiplied by \(-(d-m)(d-3m)\ne0\) in its differential equation. Therefore \(Q=cA\) for some scalar \(c\). The coefficient of \(a^m\) in \(Q\) is \(\binom{4m}{m}\), whereas that in \(A\) is \(\binom{2m}{m}\). This proves the stated formula for \(B\) for every \(m\), without interpolation in small characteristics.

**3. Prym and elliptic strata.** On the smooth locus, \(bD\ne0\), so the identities imply \(B=0\iff A=0\), while \(F\ne0\). The Prym Cartier operator is therefore either invertible (ordinary Prym) or identically zero (\(a(P)=2\)). An abelian surface over an algebraically closed field with \(a\)-number two is superspecial, and its \(p\)-rank is zero. The elliptic factor is always ordinary. The natural isogeny \(P\times E\to\operatorname{Jac}(C)\) has kernel of order four, so it preserves the \(p\)-divisible group for \(p\ne2\), and the stated Jacobian invariants follow.

**4. Exactly \(m\) simple superspecial parameters.** The leading \(a^m\)-coefficient of \(A=H_m(a,b)\) equals \(\binom{2m}{m}\ne0\), hence \(H_m(a,1)\) has degree \(m\). At the discriminant boundary \(a^2=4b\ne0\), one has \(g(z)=(z+a/2)^2\), so
\[
 H_m(a,b)=\binom{4m}{3m}(a/2)^m\ne0.
\]
Suppose \(a_0\) were a multiple root of \(H_m(a,1)\) away from that boundary. The first differential equation, whose coefficient \(4-a_0^2\) is nonzero, successively forces all higher derivatives of \(H_m\) to vanish at \(a_0\). This is impossible because its degree \(m\) is strictly less than \(p\) and its leading coefficient is nonzero. Thus all \(m\) geometric roots are simple and represent smooth curves.

Finally, the marked coefficient equivalence \((a,b)\sim(\lambda^6a,\lambda^{12}b)\) permits normalizing \(b=1\), with the residual action \(a\mapsto\pm a\). As \(H_m(-a,1)=(-1)^mH_m(a,1)\), the \(m\) distinct roots form \(\lceil m/2\rceil\) orbits. If \(m\) is odd, \(a=0\) is one simple root. If \(m\) is even, the nonzero middle coefficient \(\binom{2m}{3m/2}\) gives \(H_m(0,1)\ne0\). This completes the classification.

## Verification

The accompanying `verify_picard_prym.py` uses integer binomial coefficients and polynomial dictionaries modulo nine primes \(p=7,13,19,31,37,43,61,67,73\). It checks **both entire polynomial identities**, the degree and boundary nonvanishing, and the simplicity of all roots that lie in the prime field. For \(p=7,13,19\), it independently enumerates all smooth coefficient pairs over the prime field and verifies that the curve's direct rational-point count agrees modulo \(p\) with the trace of the computed Cartier diagonal. All tests passed. Finite-field checks corroborate but do not prove the universal claim; the proof is the coefficient argument above.

## Relationship to prior work

Laga and Shnidman (arXiv:2308.15297, first posted August 29, 2023) define this precise bielliptic Picard family, its marked moduli parameter, and its quaternionic Prym. Their treatment gives the geometry, automorphisms, and the prime-to-two Prym–elliptic isogeny but does not state this split-characteristic Hasse polynomial, coefficient factorization, or squarefree superspecial divisor. Classical work on Cartier–Manin computations for Picard curves supplies the method. Kazemifard and Tafazolian (2015) classify Newton polygons of two fixed Picard curves including the special Fermat curve, but not the moving parameter. A preceding result for this family in characteristic seven determines that small-prime fiber; the present result extends the classification to **all** primes congruent to one modulo six and proves a uniform simple-root formula. Terakado, Xue, and Yu (2026) count superspecial points on general quaternionic Shimura curves, and may imply related abstract counts; the specific equation and modular Cartier factorization here are not stated in that work. Consequently, novelty is claimed for the **explicit family-level polynomial identity, its squarefree smooth divisor, and its all-prime geometric classification**, not for existence of superspecial points, general Shimura mass formulas, or the isolated characteristic-seven case.

## Limitations

No statement is asserted for primes congruent to five modulo six or for characteristics two and three. The geometric count is for marked isomorphism classes, not rational coefficient values, twists, or rational points of the superspecial locus. The result does not determine zeta numerators or the field of definition of every geometric root. General Shimura mass formulas and earlier specialized computations are potential sources of further consequences; unindexed literature and equivalences under modular parameter changes remain priority risks. An independent mathematical audit has not been performed.

## References

1. J. Laga and A. Shnidman, *The geometry and arithmetic of bielliptic Picard curves*, arXiv:2308.15297, initial submission 2023-08-29. Complete publicly accessible manuscript: https://arxiv.org/html/2308.15297v3, especially Sections 2 and 4–6.
2. A. Kazemifard and S. Tafazolian, *A note on some Picard curves over finite fields*, Finite Fields and Their Applications **34** (2015), 107–122, DOI:10.1016/j.ffa.2014.12.002.
3. Y. Terakado, J. Xue and C.-F. Yu, *Superspecial Points on Shimura Curves*, arXiv:2608.16036, 2026, especially introduction and the geometric class-number formula.
4. S. Baba and H. Granath, *Picard–Fuchs equations for Shimura curves over \(\mathbb Q\)*, Bull. Lond. Math. Soc. **53** (2021), 408–415, DOI:10.1112/blms.12430.
5. Classical Cartier–Manin coefficient formula and the criterion that the vanishing of the Cartier operator on an abelian surface is equivalent to \(a=2\) (superspeciality); Lucas's binomial congruence theorem.
