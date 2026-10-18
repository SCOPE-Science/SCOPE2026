# Branch and Weil spectra of binary bidegree-\((2,3)\) genus-two curves

## Finding

Let \(S=\mathbf P^1_{\mathbf F_2}\times\mathbf P^1_{\mathbf F_2}\). Among the \(2^{12}-1=4095\) nonzero sections of \(\mathcal O_S(2,3)\), exactly **1116** have geometrically smooth zero divisors. All are connected smooth genus-two curves. These equations form exactly **39** orbits under the ruling-preserving ambient automorphism group \(G=\operatorname{PGL}_2(\mathbf F_2)^2\) of order \(36\).

The complete simultaneous classification by rational-point count, Frobenius cycle partition on the geometric branch support of the degree-two ruling, and the Weil polynomial has **18 joint strata**, as follows. For the table, \(N_i=\#C(\mathbf F_{2^i})\), and the partition records Frobenius orbit lengths among *distinct geometric branch points*. All equation and orbit counts are exact.

| \(N_1\) | \(N_2\) | Branch partition | Equations | \(G\)-orbits |
| ---: | ---: | :---: | ---: | ---: |
| 0 | 6 | \((3)\) | 6 | 1 |
| 1 | 7 | \((1,2)\) | 18 | 1 |
| 1 | 9 | \((1)\) | 18 | 1 |
| 2 | 6 | \((3)\) | 18 | 1 |
| 2 | 8 | \((1,1)\) | 36 | 1 |
| 2 | 10 | \((3)\) | 54 | 2 |
| 3 | 3 | \((1,1,1)\) | 6 | 1 |
| 3 | 5 | \((1)\) | 36 | 1 |
| 3 | 7 | \((1,2)\) | 54 | 2 |
| 3 | 9 | \((1)\) | 72 | 2 |
| 4 | 4 | \((1,1)\) | 72 | 2 |
| 4 | 6 | \((3)\) | 90 | 3 |
| 4 | 8 | \((1,1)\) | 108 | 3 |
| 4 | 10 | \((3)\) | 126 | 4 |
| 5 | 5 | \((1)\) | 72 | 2 |
| 5 | 7 | \((1,2)\) | 162 | 5 |
| 5 | 9 | \((1)\) | 90 | 4 |
| 6 | 6 | \((3)\) | 78 | 3 |

There are exactly **13** nonempty strata when \(N_2\) is omitted and **18 distinct Weil numerators** among the smooth equations. The complete per-orbit list of 39 representatives, orbit sizes, branch types, rational totally ramified fibres of the degree-three map, and extension-field counts is the embedded file `census.json`.

The maximal rational-point stratum is particularly rigid. Exactly **78** smooth equations have \(N_1=6\), forming three ambient automorphism orbits of sizes \(36,36,6\), with coefficient-mask representatives `438`, `691`, and `1718`. All have irreducible cubic branch form for the degree-two ruling (three nonrational geometric branch points in one Frobenius orbit), ordinary Jacobian, and the identical Weil numerator
\[
L_C(T)=1+3T+5T^2+6T^3+4T^4.
\]
Nevertheless, their *degree-three* rulings have respectively \(1,0,0\) rational totally ramified fibres. Thus the Weil numerator and both \(N_1,N_2\) do not determine the ramification type of the additional degree-three ruling on an embedded genus-two curve.

## Assumptions and scope

The base field is precisely \(\mathbf F_2\). A section is written uniquely as
\[
F(X_0,X_1;Y_0,Y_1)=A(Y)X_0^2+B(Y)X_0X_1+C(Y)X_1^2,
\]
where \(A,B,C\) are homogeneous binary cubics over \(\mathbf F_2\). Coefficient masks encode the twelve monomials \(X_0^{2-i}X_1^iY_0^{3-j}Y_1^j\), for \(0\le i\le2\), \(0\le j\le3\), at bit position \(4i+j\). There is no nontrivial scalar identification over \(\mathbf F_2\).

The degree-two ruling is projection to \([Y_0:Y_1]\); the degree-three ruling is projection to \([X_0:X_1]\). Smoothness means geometric regularity over the algebraic closure, not absence of singular rational points. Equivalence is induced by \(G\) on the fixed ruled surface, **not** abstract curve isomorphism. The two rulings cannot be exchanged while preserving bidegree \((2,3)\).

## Proof

**Geometric criterion.** For a geometrically smooth member, \(B\ne0\). Otherwise its degree-two function field extension of \(\overline{\mathbf F}_2(Y)\) would be purely inseparable, hence rational after passing to a perfect algebraically closed coefficient field; this contradicts the genus-two adjunction formula. On the chart \(Y_1\ne0\), set \(t=Y_0/Y_1\) and dehomogenize \(A,B,C\) to cubic polynomials. At a root \(t_0\) of \(B\), the quadratic fibre is \(AX_0^2+CX_1^2\) and has a unique geometric double point \([\sqrt C:\sqrt A]\), provided \((A,C)\ne(0,0)\). A singular point is present precisely when its transverse derivative vanishes. Its square is the value of
\[
Q(t)=\bigl(A'(t)C(t)+A(t)C'(t)\bigr)^2+B'(t)^2A(t)C(t).
\]
The same expression also vanishes at a common zero of \(A,B,C\). Thus the curve is geometrically smooth if and only if \(B\ne0\) and \(\gcd(B,Q)=1\) in **each** of the two affine charts \(Y_1\ne0\) and \(Y_0\ne0\). This is an exact test in \(\mathbf F_2[t]\); no extension-degree cutoff or rational-point heuristic is involved.

**Complete coefficient and orbit census.** Exhausting the twelve binary coefficients and applying the preceding gcd criterion yields 1116 smooth masks. The coefficient substitution action of the two six-element groups \(\operatorname{PGL}_2(\mathbf F_2)\) gives 39 disjoint orbits, whose sizes sum to 1116. An independently constructed action and Burnside fixed-point count gives \((1/36)\sum_{g\in G}\#\mathrm{Fix}(g)=39\). Their representatives appear in `census.json`. The distinct roots of the homogeneous cubic \(B\), together with Frobenius squaring, give the branch partition. For a separable Artin–Schreier double cover the Deuring–Shafarevich formula gives Jacobian \(2\)-rank \(r-1\), where \(r\) is the number of geometric branch points.

**Point counts and Weil polynomials.** Evaluate the nine rational points of \(S\) to obtain \(N_1\). For each orbit representative enumerate the \(25\) pairs of projective-line points over \(\mathbf F_4\) to obtain \(N_2\); the \(81\) pairs over \(\mathbf F_8\) give the independent \(N_3\) check. The genus-two zeta numerator is
\[
L_C(T)=1+a_1T+a_2T^2+2a_1T^3+4T^4,
\quad a_1=N_1-3,\quad a_2=(a_1^2-5+N_2)/2.
\]
Every \(N_3\) matches the Newton identity \(N_3=9+a_1^3-3a_1a_2+6a_1\). Counting weighted orbits yields precisely the 18 rows in the table and 18 distinct Weil numerators.

**The maximal stratum.** The degree-two projection has only three rational target points and every smooth fibre has at most two rational geometric points, hence \(N_1\le6\). Equality forces the mixed-term binary cubic \(B\) to be nonzero at all three rational points of \(\mathbf P^1\): at \(B=0\), the quadratic has at most one rational solution for a smooth fibre. Therefore \(B\) has no rational root, is irreducible cubic, has three geometric branch points in one Frobenius orbit, and the Jacobian is ordinary. Checking all smooth members with \(N_1=6\) gives the three complete \(G\)-orbits listed above. Each representative has \(N_2=6\), so the common Weil numerator follows by the previous formula. On each rational fibre of the *degree-three* projection, the binary cubic in \(Y\) is totally ramified exactly when it equals the cube of a linear form, namely one of the coefficient masks `1`, `8`, `15`. Their counts on the three representatives are \(1,0,0\), a \(G\)-invariant distinction not captured by the common Weil polynomial.

## Verification

All necessary scripts and their fixed expected output are embedded alongside this text. With Python 3 from the same directory, run `python3 enumerate.py > regenerated.json` and compare the resulting JSON object to `census.json`. Then run `python3 independent_check.py`. The latter reimplements the geometric criterion using polynomial gcds, verifies every one of the 4095 smoothness decisions against the extension-field approach, independently computes the 39-orbit Burnside sum, and verifies all 39 second-extension counts using an unrelated \(\mathbf F_4\) arithmetic implementation. It also checks all third-extension counts by Newton identities. These checks completed successfully before packaging.

## Relationship to prior work

Zobernig [1] treats coarse-moduli \(p\)-rank strata of genus-two curves in small characteristic. The coarse-moduli problem does not specify this fixed ruled-surface embedding, the degree-three ruling, or weighted projective-coordinate orbit counts. Faber–Grantham [2] already establish that six is the **known** maximum rational-point count for genus two over \(\mathbf F_2\); this bound and existence are not claimed as new. Howe–Nart–Ritzenthaler [3] classify which genus-two Weil polynomials can occur abstractly over finite fields; this is stronger than mere realization of the polynomial in our table but does not give the joint embedding/branch/orbit multiplicities. Rawson [4] studies degree-three morphisms and their discriminants over number fields, providing geometric motivation rather than a positive-characteristic finite embedded census. The new contribution asserted here is only the exact *joint embedded distribution*, including the three maximum-point orbits and their otherwise invisible degree-three ramification distinction.

## Limitations

The classification is solely over \(\mathbf F_2\) and only for smooth bidegree-\((2,3)\) members of the split ruled surface. Its 39 orbits are not counts of abstract genus-two isomorphism classes. In particular, equal zeta numerators do not imply equal embedded or abstract isomorphism types. An unindexed earlier finite embedded census remains a possible priority risk; the numerical and geometric conclusions do not require assuming its absence. No independent mathematical audit has been performed.

## References

[1] L. Zobernig, *Genus 2 Curves in Small Characteristic*, arXiv:2111.07270 (first public 2021-11-14), primary MSC 14H10; https://arxiv.org/abs/2111.07270.

[2] X. Faber and J. Grantham, *Binary Curves of Small Fixed Genus and Gonality with Many Rational Points*, arXiv:2005.07054 (first public 2020-05-14), Theorem 3.1; https://arxiv.org/abs/2005.07054.

[3] E. Howe, E. Nart, C. Ritzenthaler, *Jacobians in Isogeny Classes of Abelian Surfaces over Finite Fields*, arXiv:math/0607515 (first public 2006-07-21), Theorem 1.2; https://arxiv.org/abs/math/0607515.

[4] J. Rawson, *Cyclic Cubic Points on Higher Genus Curves*, arXiv:2405.13743 (first public 2024-05-22), §2; https://arxiv.org/abs/2405.13743.
