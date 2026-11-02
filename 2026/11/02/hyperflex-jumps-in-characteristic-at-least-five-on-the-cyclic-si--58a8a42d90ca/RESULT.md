# Hyperflex jumps in characteristic at least five on the cyclic-six plane-quartic locus

## Finding
Let \(k\) be algebraically closed of characteristic \(p\ge5\). For every \(r\in k\setminus\{0,2,-2\}\), consider the smooth plane quartic
\[
 C_r:\quad X^3Z+Y^4+rY^2Z^2+Z^4=0.
\]
A hyperflex is a point at which its tangent line has intersection multiplicity exactly four. Put
\[
 P(r)=11r^4-1080r^2+3888\in\mathbb Z[r],
\]
interpreted in \(k[r]\) by reduction modulo \(p\). Then the number of **geometric** hyperflex points on \(C_r\) is exactly
\[
 h(C_r)=\begin{cases}7,&P(r)=0,\\1,&P(r)\ne0.\end{cases}
\]
The point \([1:0:0]\) is always a hyperflex. At every exceptional parameter the six others form one orbit under the order-six automorphism \((X:Y:Z)\mapsto(\zeta_3 X:-Y:Z)\). The exceptional parameter scheme is reduced and disjoint from the excluded singular and extra-automorphism parameters: it has four geometric points for \(p\ne11\) and two for \(p=11\). Since \(C_r\cong C_s\) over \(k\) exactly when \(r^2=s^2\) on this locus (the previously published isomorphism theorem), the exceptional curves give two geometric isomorphism classes for \(p\ne11\) and one for \(p=11\).

In characteristic \(11\) the exceptional condition specializes to \(r^2=8\), and the six extra hyperflexes all have \(Y^2=3r\). Over the prime fields the exceptional parameter polynomial has a single irreducible factor of degree four for \(p=5,7\), and of degree two for \(p=11\); in each of those three characteristics all exceptional parameters form one Frobenius orbit.

## Assumptions and scope
The base field is algebraically closed and \(p\) is prime with \(p\ge5\). The parameter \(r=\pm2\) gives a singular quartic and \(r=0\) has a larger automorphism group; all three are excluded. Hyperflexes are counted as distinct geometric points, not as tangent lines with multiplicity, and coefficient parameters are not automatically isomorphism classes. This is a positive-characteristic theorem; the characteristic-zero hyperflex classification is established elsewhere and is not claimed here.

## Proof
Write the affine equation on \(Z=1\) as \(x^3+g(y)=0\), where \(g(y)=y^4+ry^2+1\). The cited smoothness classification gives exactly \(r\ne\pm2\). Its unique point at infinity is \(Q=[1:0:0]\), and \(Z=0\) cuts out \(4Q\), giving the permanent hyperflex. If \(x=0\), then \(g(y)=0\) and \(g'(y)\ne0\), since \(r^2\ne4\); the tangent \(y=\mathrm{constant}\) intersects to order three, not four. If \(y=0\), then \(x^3=-1\), the tangent is \(x=\mathrm{constant}\), and the contact order is two because \(r\ne0\). Thus any extra hyperflex has \(xy\ne0\).

For such a point put \(u=y^2\), \(G=u^2+ru+1=-x^3\), and write the tangent parametrically as \(x(t)=x+mt\), \(y(t)=y+t\). Tangency forces \(m=-g'(y)/(3x^2)\). Direct expansion gives coefficients of \(t^2,t^3,t^4\) equal to
\[
 3xm^2+6u+r,\qquad m^3+4y,\qquad 1.
\]
Both of the first two coefficients must vanish for a hyperflex. Eliminating \(x,m\) by \(x^3=-G\) and \(g'(y)=2y(2u+r)\) yields exactly
\[
 E_2(u,r)=3(6u+r)(u^2+ru+1)-4u(2u+r)^2=0,
\]
\[
 E_3(u,r)=2u(2u+r)^3-27(u^2+ru+1)^2=0.
\]
Conversely, for any common solution with \(uG\ne0\), the two square roots \(y^2=u\), the three cube roots \(x^3=-G\), and the uniquely determined slope satisfy the original contact equations; the contact order is exactly four because the coefficient of \(t^4\) is one.

An integer-polynomial Sylvester resultant gives
\[
 \operatorname{Res}_u(E_2,E_3)=324(r^2-4)^3P(r).
\]
The degree-one subresultant is
\[
 -18(r^2-4)\bigl(A(r)u-N(r)\bigr),\qquad
 A(r)=33r^4-704r^2+2160,\quad N(r)=196r^3-720r.
\]
For every prime \(p\ge5\), \(P\) and \(A\) have no common geometric root. Indeed their integer resultant is \(2^{34}3^{10}11^2\), which suffices for \(p\ne11\); in characteristic \(11\), \(P=5-2r^2\) and \(A=4\). Therefore any common root must be the unique value \(u=N/A\). Existence follows without a genericity assumption: for \(j\in\{2,3\}\), the numerator obtained by substituting \(u=N/A\) into \(E_j\) and multiplying by \(A^{\deg_u E_j}\) is divisible by \(P\) in \(\mathbb Z[r]\) (the exact identities are replayed in the symbolic verifier).

For every \(p\ge5\), \(P(0)=3888\) and \(P(\pm2)=-256\) are nonzero modulo \(p\), so each exceptional parameter is admitted. Its associated \(u\ne0\) and \(G\ne0\): if \(u=0\), then \(E_3=-27\ne0\); if \(G=0\), then \(E_2=-4u(2u+r)^2=0\), forcing \(2u+r=0\), and \(G=1-r^2/4=0\), contrary to \(r^2\ne4\). Since \(p\ne2,3\), each such \(u\) gives exactly six distinct affine hyperflexes, one order-six orbit. Otherwise none occurs.

Finally the discriminant of \(P\) as a quartic over \(\mathbb Z\) is \(2^{32}3^{15}11\), and its leading coefficient is \(11\). Hence modulo any \(p\ge5\), \(p\ne11\), it is a squarefree quartic; modulo \(11\) it is the separable quadratic \(5-2r^2\). The isomorphism count follows from the published classification \(C_r\cong C_s\iff r^2=s^2\) for \(r,s\notin\{0,\pm2\}\). The factorizations over \(\mathbb F_5,\mathbb F_7,\mathbb F_{11}\) are reproduced by the modular verifier.

## Verification
From the directory containing this file run `python3 verify_symbolic.py` and `python3 verify_modular.py` with SymPy installed. The first script independently expands tangent restrictions and recomputes the two defining polynomials, the Sylvester resultant, subresultant, discriminant, coprimality certificate and substitution identities over the integers. The second script reduces the polynomial certificates in five characteristics, proves the necessary modular coprimality and squarefreeness, and factors the exceptional polynomial over three small prime fields (also testing two further primes). The observed exact completion markers were `SYMBOLIC_HYPERFLEX_OK` and `MODULAR_HYPERFLEX_OK`. The proof over all characteristics is algebraic, not an extrapolation from the finite tests.

## Relationship to prior work
Ohashi–Kudo–Harashita (first public preprint 2021-11-18) give the cyclic-six normal form, smoothness/isomorphism criteria, and positive-characteristic Hasse–Witt and \(a\)-number results. They do not give this hyperflex-contact stratification. Liang (2019) computes bitangents of cyclic-three/six/nine quartics over characteristic zero, including the permanent exceptional bitangent, but does not determine the positive-characteristic seven-hyperflex parameter locus. Girard–Kohel (2006), following Vermeulen, classify certain complex seven-hyperflex moduli strata; their characteristic-zero classification is acknowledged, and its statements do not directly supply the exceptional degeneration in characteristic eleven. These comparisons concern the actual mathematical assertions, not merely matching titles.

## Limitations
This does not enumerate the other bitangent lines, describe the full Weierstrass scheme, compute Jacobian invariants, or classify reductions of every complex Vermeulen stratum. No global claim of priority independent of an unindexed earlier parameter calculation is made. The polynomial describes the chosen normal-form parameter and its quotient by the stated isomorphism equivalence. The classification is confined to characteristic at least five and the exact cyclic-six automorphism locus; no statement is made in characteristics two or three or at the excluded parameters.

## References
1. R. Ohashi, M. Kudo, S. Harashita, *The a-numbers of non-hyperelliptic curves of genus 3 with cyclic automorphism group of order 6*, arXiv:2111.09777, first submitted 2021-11-18, https://arxiv.org/abs/2111.09777.
2. D. Liang, *Invariants, Bitangents and Matrix Representations of Plane Quartics with 3-Cyclic Automorphisms*, arXiv:1902.02914, first submitted 2019-02-08, https://arxiv.org/abs/1902.02914.
3. M. Girard, D. R. Kohel, *Classification of Genus 3 Curves in Special Strata of the Moduli Space*, arXiv:math/0603555, first submitted 2006-03-23, https://arxiv.org/abs/math/0603555.
