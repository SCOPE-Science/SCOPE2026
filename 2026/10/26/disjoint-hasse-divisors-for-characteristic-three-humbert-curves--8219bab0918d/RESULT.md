# Disjoint Hasse divisors for characteristic-three Humbert curves

## Finding
Let \(k\) be algebraically closed of characteristic \(3\), and let \(C_{a,b}\) be the smooth marked genus-five Humbert curve associated to the five distinct points \((\infty,0,1,a,b)\) of \(\mathbb P^1(k)\). Thus \(a,b\notin\{0,1\}\) and \(a\ne b\). Its Jacobian has \(3\)-rank \(4\) or \(5\), never \(0,1,2,3\). The nonordinary locus in the two-dimensional ordered marked parameter space is the *disjoint union of five smooth rational curves*, each isomorphic to \(\mathbb P^1\setminus\{\infty,0,1,-1\}\). Every nonordinary Jacobian has \(3\)-rank \(4\), \(a\)-number \(1\), and Newton slopes \(0\) (four times), \(1/2\) (twice), and \(1\) (four times). Every ordinary Jacobian has \(3\)-rank \(5\), \(a\)-number \(0\), and Newton slopes \(0\) and \(1\), each five times.

For every \(q=3^n\) with integer \(n\ge1\), there are exactly \(5(q-3)\) nonordinary and \((q-3)(q-7)\) ordinary ordered marked parameter pairs \((a,b)\in\mathbb F_q^2\). These are parameter counts, not counts of unmarked geometric isomorphism classes.

## Assumptions and scope
For \(a,b\in k\setminus\{0,1\}\), \(a\ne b\), a specific smooth model in \(\mathbb P^4_k\) has homogeneous coordinates \([u_0:u_1:u_2:u_3:u_4]\) and diagonal quadrics
\[
 u_2^2-u_1^2+u_0^2=0,\qquad u_3^2-u_1^2+a u_0^2=0,\qquad u_4^2-u_1^2+b u_0^2=0.
\]
The quotient by the simultaneous sign-change group \((\mathbb Z/2\mathbb Z)^4\) is \(\mathbb P^1\), via \([u_1^2:u_0^2]\), branched at the ordered points \(\infty,0,1,a,b\). Distinctness and \(\operatorname{char}(k)\ne2\) ensure smoothness; the curve is a degree-eight complete intersection of three quadrics and has genus five by adjunction. The parameter surface is the marked \(M_{0,5}\) chart fixing its first three ordered branch points. Arithmetic assertions refer to the displayed model over \(\mathbb F_q\); p-ranks and Newton polygons refer to its geometric Jacobian.

## Proof
**1. Five elliptic quotients and a prime-to-three isogeny.** Let \(G=(\mathbb Z/2\mathbb Z)^4\). Label the five inertia involutions \(g_0,\dots,g_4\), with product \(g_0\cdots g_4=1\). A character of \(G\) corresponds to an even-cardinality subset of the five branch labels, namely the labels at which it takes value \(-1\). The five characters of weight four give double covers of \(\mathbb P^1\), each branched at exactly four of the five points, and these quotients have genus one by Riemann--Hurwitz. Characters of weight two give genus-zero double covers. Since \(|G|=16\) is invertible in characteristic three, the character idempotents in \(\mathbb Z[1/2][G]\) split the Jacobian's \(3\)-divisible group into exactly the five elliptic parts. Equivalently, the five elliptic quotient Jacobians form an isogeny product with kernel of \(2\)-power order. The dimensions sum to five, so no positive-dimensional part is omitted. Thus the geometric \(3\)-rank and \(a\)-number of \(J(C_{a,b})\) are the sums of those of the five elliptic quotients, and likewise their Newton slopes concatenate.

**2. Characteristic-three supersingularity becomes a unique harmonic completion.** Any four distinct branch points give an elliptic double cover. Put three at \(\infty,0,1\), and call the fourth \(\lambda\); its Legendre equation is \(y^2=x(x-1)(x-\lambda)\). In characteristic three, the Hasse invariant is the coefficient of \(x^2\) in \(x(x-1)(x-\lambda)\), namely \(-(1+\lambda)\). Thus the elliptic curve is supersingular exactly at \(\lambda=-1\). Under permutations of four labels, the three classical harmonic values \(-1,2,1/2\) coincide in characteristic three. Hence, given any three distinct points of \(\mathbb P^1(k)\), there is **exactly one** fourth point that makes their four-point set supersingular. (The uniqueness follows after mapping the triple to \(\infty,0,1\).)

Two different four-element subsets of five labels share exactly three points. If both were supersingular, their two different fourth points would both be the unique harmonic completion of that common triple, a contradiction. Therefore the number \(s\) of supersingular elliptic quotients is \(0\) or \(1\). All remaining elliptic quotients are ordinary. The isogeny of Step 1 then gives \(3\)-rank \(5-s\), \(a\)-number \(s\), and the asserted Newton polygons.

**3. Five disjoint smooth Hasse components.** For each one of the five labels, impose supersingularity on the elliptic quotient obtained by omitting that label. This defines one component \(D_i\) in marked \(M_{0,5}\). Fixing the other four labelled points to a harmonic quadruple by the unique projective transformation of three fixed labels, the omitted fifth label may vary freely on \(\mathbb P^1\) outside those four positions. Hence \(D_i\cong\mathbb P^1\setminus\{\infty,0,1,-1\}\), a smooth geometrically irreducible rational curve. Step 2 shows \(D_i\cap D_j=\varnothing\) for \(i\ne j\) on the smooth parameter surface. The Hasse invariant of each elliptic factor has a simple zero at its harmonic value because \(-(1+\lambda)\) has a simple zero. The prime-to-three splitting in Step 1 makes the Jacobian Hasse determinant locally a unit times the product of these elliptic Hasse invariants. Hence the full scheme-theoretic nonordinary locus is the reduced disjoint union of the five \(D_i\): no hidden multiplicities or intersection components occur.

**4. Uniform finite-field counts.** Over \(\mathbb F_q\) with \(q=3^n\), the ordered normalized parameter space has \((q-2)(q-3)\) points. Each \(D_i\) is defined over \(\mathbb F_3\) and has \(q+1-4=q-3\) rational points. The five \(D_i\) are pairwise disjoint. Therefore exactly \(5(q-3)\) points are nonordinary and \((q-2)(q-3)-5(q-3)=(q-3)(q-7)\) points are ordinary. For \(q=3\) both sets are empty because \(\mathbb P^1(\mathbb F_3)\) has only four points.

For direct coordinate verification, the five reduced Hasse equations in this chart are
\[
 a+1=0,\quad b+1=0,\quad a+b=0,\quad 1+a+b=0,\quad a+b+ab=0.
\]
They are pairwise disjoint after removing \(a,b\in\{0,1\}\) and \(a=b\). These equations are the five possibilities of omitting a branch label and provide an independent check of the geometric argument.

## Verification
The accompanying standalone `finite_field_check.py` uses exact finite-field arithmetic and exhaustively enumerates ordered pairs over \(\mathbb F_3\), \(\mathbb F_9\), and \(\mathbb F_{27}\). It confirms respectively \((0,0)\), \((12,30)\), and \((480,120)\) for (ordinary, nonordinary) counts, and finds no pair on two Hasse components. These finite computations check the formulas at three field sizes but do not replace the all-field proof above. Reproduce with `python3 finite_field_check.py`.

## Relationship to prior work
Hidalgo and Reyes-Carocca (2016, arXiv:1609.04895) provide the marked two-parameter classical Humbert-cover model and study fields of moduli in characteristic zero. Auffarth, Lucchini Arteche, and Rojas (2019, arXiv:1905.12690, Theorems 2.1 and 4.1) describe the general Jacobian decomposition of Humbert--Edge curves; their characteristic-not-two setup supports the factor structure but does not state this characteristic-three Hasse-divisor or finite-field census. The Legendre supersingularity criterion is classical. The present assertion concerns the *compatibility* of five potential supersingular factors in characteristic three, their disjoint geometric loci, and complete marked arithmetic counts. No claim is made to originality of the Humbert construction, its factorization, or the elliptic Hasse criterion.

## Limitations
The proof concerns smooth curves in characteristic three with all five branch points geometrically distinct and ordered. It does not identify moduli isomorphism-class counts, quotient polarization types, singular boundary fibres, or arithmetic Frobenius traces of the individual elliptic factors. Historical novelty coverage is not exhaustive; older specialized papers may contain implicit related statements. Independent validation has not been performed.

## References
- R. A. Hidalgo and S. Reyes-Carocca, *Fields of moduli of classical Humbert curves*, arXiv:1609.04895, first publicly posted 2016-09-16, especially Section 2, https://arxiv.org/abs/1609.04895.
- R. Auffarth, G. Lucchini Arteche, and A. M. Rojas, *A decomposition of the Jacobian of a Humbert--Edge curve*, arXiv:1905.12690, first publicly posted 2019-05-29, especially Theorems 2.1 and 4.1, https://arxiv.org/html/1905.12690v2.
- T. Yamauchi, *On Curves with Split Jacobians*, Communications in Algebra 36 (2008), 1419--1425; doi:10.1080/00927870701866622 (abstract inspected; full text not accessed).
