# No triple supersingularity in the characteristic-eleven genus-five Humbert family

## Finding
Let \(k\) be algebraically closed of characteristic \(11\) and let
\[
U=\{(u,v)\in\mathbb A_k^2:u v(u-1)(v-1)(u-v)\ne0\}.
\]
For \((u,v)\in U\), take the smooth genus-five complete intersection \(C_{u,v}\subset\mathbb P_k^4\)
\[
X_1^2+X_2^2+X_3^2=uX_1^2+X_2^2+X_4^2=vX_1^2+X_2^2+X_5^2=0.
\]
Its five elliptic quotient Legendre parameters, up to the standard six cross-ratio transformations, are
\[
u,\quad v,\quad v/u,\quad (v-1)/(u-1),\quad u(v-1)/(v(u-1)).\]
Write
\[
H(T)=\sum_{j=0}^{5}\binom5j^2T^j=T^5+3T^4+T^3+T^2+3T+1
=(T-2)(T+1)(T+5)(T^2-T+1)
\]
in \(\mathbb F_{11}[T]\). For each of the five Legendre parameters, let \(D_i\subset U\) be its zero locus under \(H\). Each \(D_i\) is a smooth (possibly disconnected) curve with five geometrically irreducible components. Each distinct pair \(D_i,D_j\) intersects transversely in exactly \(20\) points, and every triple intersection is empty. The ten pairwise intersection sets are disjoint. Thus precisely \(200\) marked geometric parameters lie on exactly two supersingularity divisors; all are \(\mathbb F_{121}\)-rational.

The Jacobian has \(11\)-rank \(5-s\), \(a\)-number \(s\), and Newton slopes \(0^{5-s},(1/2)^{2s},1^{5-s}\), where \(s\in\{0,1,2\}\) is the number of quotient supersingularity conditions satisfied. All three cases occur geometrically; rank below three is impossible.

For \(q=11^m\) with \(m\ge1\), define \(r_m=3\) for odd \(m\) and \(r_m=5\) for even \(m\). The numbers of ordered *marked coefficient pairs* with exactly \(s\) supersingular elliptic quotients are
\[
\begin{aligned}
N_2(q)&=10r_m(r_m-1),\\
N_1(q)&=5r_m(q-3)-20r_m(r_m-1),\\
N_0(q)&=(q-2)(q-3)-5r_m(q-3)+10r_m(r_m-1).
\end{aligned}
\]
For \(q=11\), the three counts \((N_0,N_1,N_2)\) are \((12,0,60)\), and for \(q=121\) they are \((11292,2550,200)\). These are marked-parameter counts, not isomorphism-class counts.

## Assumptions and scope
The characteristic is exactly \(11\). The three quadrics above are the standard model of the maximal elementary abelian two-cover of \(\mathbb P^1\) branched at the five *ordered* distinct points \((\infty,0,1,u,v)\). Since the branch points are distinct and \(2\) is invertible, the cover and canonical complete intersection are smooth of genus five. No assertion is made for other primes, singular boundary parameters or unmarked moduli points.

## Proof
**1. Decomposition and Hasse criterion.** In characteristic different from two, the sign-change group \((\mathbb Z/2)^4\) acts tamely. Its five nonzero genus-one character quotients are the Legendre elliptic curves associated with the five four-element branch subsets. Orthogonal idempotents in the group algebra with denominators dividing \(16\) yield a two-power-degree isogeny from their product to \(\operatorname{Jac}(C_{u,v})\). Because \(11\nmid16\), this preserves the full \(11\)-divisible group, its \(p\)-rank, \(a\)-number, and Newton polygon. Carvacho–Hidalgo–Quispe, Theorem 5.1, supplies the explicit five quotient equations in characteristic zero; the preceding tame-idempotent argument verifies that the needed decomposition survives in characteristic eleven. The Legendre Hasse invariant at \(11\) is, up to a nonzero scalar, \(H(T)=\sum_{j=0}^5\binom5j^2T^j\). An elliptic quotient is supersingular precisely at a zero of this polynomial. The fifth cross ratio above equals an \(S_3\)-transform of the quotient parameter \(v(1-u)/(v-u)\) printed in that theorem: \(v(1-u)/(v-u)=1/(1-u(v-1)/(v(u-1)))\). Supersingularity is invariant under this transformation.

**2. All geometric intersection points and the triple obstruction.** The displayed exact factorization of \(H\) has five distinct roots. The three linear roots lie in \(\mathbb F_{11}\); the remaining two are in \(\mathbb F_{121}\), since \(T^2-T+1\) is irreducible over \(\mathbb F_{11}\). The group of permutations of the five branch labels acts by regular algebraic automorphisms of \(U\) and permutes its five elliptic quotient divisors transitively on ordered pairs of distinct divisors. It therefore suffices to consider \(D_u=\{H(u)=0\}\) and \(D_v=\{H(v)=0\}\). Their intersection consists of the \(5\cdot4=20\) pairs of distinct Hasse roots, and all intersections are transverse because the roots are simple. Every such ordered pair has exactly two supersingular quotients: the finite-field certificate `humbert11_verify.py` enumerates *all* twenty ordered pairs of the complete algebraic root set over \(\mathbb F_{121}\) and evaluates the other three cross ratios. This is an exhaustive proof over \(\overline{\mathbb F}_{11}\), not an extrapolation from bounded-degree point counts. Applying the branch-label permutations rules out three or more simultaneous conditions and proves all ten pairwise intersections are disjoint, comprising \(200\) geometric points. Every one is already \(\mathbb F_{121}\)-rational.

**3. Finite-field counts.** For \(q=11^m\), exactly \(r_m\) of the five Hasse roots are rational: three for odd \(m\), all five for even \(m\). The marked parameter space has \((q-2)(q-3)\) rational points. Each of the five supersingularity divisors contains \(r_m(q-3)\) rational points, and each pair contains \(r_m(r_m-1)\). With no triple overlaps, inclusion–exclusion gives the three formulas above. The rank and Newton assertions follow from the prime-to-eleven isogeny.

## Verification
Run `python3 humbert11_verify.py` (Python standard library only). The program constructs \(\mathbb F_{121}=\mathbb F_{11}[z]/(z^2-2)\), proves the Hasse polynomial factorization and its complete split root set by exhaustive field arithmetic, verifies \(S_3\)-invariance, checks that each of the 20 root pairs yields exactly two supersingular quotients, and independently enumerates the 72 and 14042 smooth marked pairs over \(\mathbb F_{11}\) and \(\mathbb F_{121}\). It prints `VERIFY_OK`; the captured output is `humbert11_verify.out`. The all-extension formulas are proved by the geometric intersection and inclusion–exclusion argument, not merely by these two finite-field enumerations.

## Relationship to prior work
Hidalgo–Kontogeorgis–Leyton-Álvarez–Paramantzoglou give the smooth generalized Fermat model over arbitrary tame characteristic (arXiv:1409.3063, first submitted 2014-09-10). Carvacho–Hidalgo–Quispe (arXiv:1507.02903, first submitted 2015-07-10), Section 5.1 and Theorem 5.1, give the genus-five five-elliptic decomposition and exact Legendre quotients over the complex numbers. Neither primary text asserts the characteristic-eleven double-only supersingularity arrangement or the exact formulas \(N_s(q)\). The classification concerns this explicit specialization and does not claim discovery of the generalized Fermat curves, the elliptic isogeny, or the Legendre Hasse polynomial.

## Limitations
Historical priority cannot be proved by a finite literature/database search; an unindexed prior computation for this exact prime remains possible. The finite-field certificate is exhaustive for the five Hasse roots because all roots lie in \(\mathbb F_{121}\), but the extension to geometric rank claims also relies on the separately proved tame decomposition and branch-label symmetry. Counts refer to ordered marked parameter pairs, not distinct geometric isomorphism classes. The result has self-review only; no independent audit is claimed.

## References
- R. Hidalgo, A. Kontogeorgis, M. Leyton-Álvarez and P. Paramantzoglou, *Automorphisms of the Generalized Fermat curves*, arXiv:1409.3063v1 (2014), Sections 1–2.
- M. Carvacho, R. Hidalgo and S. Quispe, *Isogenous decomposition of the Jacobian of generalized Fermat curves*, arXiv:1507.02903v1 (2015), especially Section 5.1, Theorem 5.1.
- Classical Legendre elliptic Hasse invariant criterion, obtained from the \(x^5\)-coefficient of \((x(x-1)(x-T))^5\) in characteristic \(11\).
