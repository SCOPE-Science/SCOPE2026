# Disjoint supersingularity divisors on the characteristic-three Humbert locus

## Finding

Let \(k\) be an algebraic closure of \(\mathbb F_3\). On the ordered parameter surface
\[
U=\{(u,v)\in k^2:uv(u-1)(v-1)(u-v)\ne0\},
\]
consider the smooth canonical genus-five complete intersection
\[
C_{u,v}:\quad
X_1^2+X_2^2+X_3^2=0,\qquad
u X_1^2+X_2^2+X_4^2=0,\qquad
v X_1^2+X_2^2+X_5^2=0
\quad\subset\mathbb P_k^4,
\]
These curves are the tame maximal elementary-abelian \(2\)-covers of \(\mathbb P^1\) branched at the five ordered points \((\infty,0,1,u,v)\).

The nonordinary locus in \(U\) is the **disjoint union of exactly five smooth geometrically irreducible curves**, with equations
\[
\boxed{u+1=0,\qquad v+1=0,\qquad u+v=0,\qquad u+v+1=0,\qquad uv+u+v=0.}
\]
Every one of these curves is isomorphic over \(\mathbb F_3\) to \(\mathbb A^1\setminus\{0,1,-1\}\). At a point on their union the Jacobian of \(C_{u,v}\) has geometric \(3\)-rank \(4\), \(a\)-number \(1\), and Newton slopes \(0^4,(1/2)^2,1^4\). At every other smooth marked parameter it is ordinary, with \(3\)-rank \(5\), \(a\)-number \(0\), and Newton slopes \(0^5,1^5\). **No curve in this family has geometric \(3\)-rank at most \(3\).**

For every positive integer \(m\), let \(q=3^m\), and let \(N_r(q)\) count ordered normalized parameters \((u,v)\in U(\mathbb F_q)\) whose Jacobians have geometric \(3\)-rank \(r\). Then
\[
\boxed{N_4(q)=5(q-3),\qquad N_5(q)=(q-3)(q-7),\qquad N_r(q)=0\text{ for }r\le3.}
\]
The total is \((q-2)(q-3)\). For instance, the rank-four and rank-five counts over \(\mathbb F_9\) are \(30\) and \(12\), and over \(\mathbb F_{27}\) they are \(120\) and \(480\).

## Assumptions and scope

All geometric ranks, \(a\)-numbers and Newton slopes refer to base change to \(k\). The three displayed quadratic equations define the curve scheme-theoretically in characteristic \(3\). The ordered normalization fixes the branch points \(\infty,0,1\); these formulas count **marked pairs**, not unmarked isomorphism classes. The finite-field statements count parameter pairs defined over \(\mathbb F_q\); no choice of quadratic twists of the elliptic factors affects their geometric invariants.

## Proof

**Smoothness and genus.** Write the three quadrics as a coefficient matrix acting on \((X_1^2,\ldots,X_5^2)\). All \(3\)-by-\(3\) minors of its columns are nonzero on \(U\), because their nonconstant factors belong to \(\{u,v,u-1,v-1,u-v\}\). Hence a common nonzero zero of the three quadrics has at least three nonzero homogeneous coordinates; the three gradient rows there have rank \(3\), since \(2\) is invertible. Adjunction for a smooth \((2,2,2)\) complete intersection in \(\mathbb P^4\) gives \(K_C\cong\mathcal O_C(1)\), of degree \(8\); thus \(2g-2=8\) and \(g=5\).

**Elliptic decomposition.** The sign changes of the five homogeneous coordinates form \(G\cong(\mathbb Z/2)^4\), with rational quotient \(\mathbb P^1\) and ordered branch points \((\infty,0,1,u,v)\). Exactly five quadratic characters of \(G\) correspond to double covers of \(\mathbb P^1\) branched at four of the five points; each such cover has genus one, and the other characters have genus zero. Choosing Legendre forms gives the five parameters
\[
\lambda_1=\frac{v-1}{u-1},\quad
\lambda_2=\frac vu,\quad
\lambda_3=\frac{v(1-u)}{v-u},\quad
\lambda_4=v,\quad \lambda_5=u,
\]
with elliptic curves \(E_i:Y^2=X(X-1)(X-\lambda_i)\). Their pullbacks into \(\operatorname{Jac}(C)\) lie in five distinct character eigenspaces and together have dimension five. Orthogonality gives \(\pi_{i*}\pi_j^*=0\) for \(i\ne j\), while \(\pi_{i*}\pi_i^*=[8]\), since the quotient maps have degree \(8\). Thus the product of the five pullbacks induces an isogeny with kernel annihilated by \(8\). In particular, it induces an isomorphism on \(3\)-divisible groups. The decomposition is an algebraic tame-group argument in characteristic \(3\); it does not depend on extending a characteristic-zero isogeny by assertion.

**Supersingularity equations.** In characteristic \(3\), the Hasse coefficient of \(Y^2=X(X-1)(X-\lambda)\) is the coefficient of \(X^2\) in \(X(X-1)(X-\lambda)\), namely \(-(1+\lambda)\). Therefore an elliptic factor is supersingular exactly when \(\lambda=-1\). Substituting the above five \(\lambda_i\), and clearing denominators which are units on \(U\), yields respectively
\[
u+v+1=0,\quad u+v=0,\quad uv+u+v=0,\quad v+1=0,\quad u+1=0.
\]
All five divisors are smooth: the first four are lines, and the final equation solves as \(v=-u/(u+1)\); its denominator is nonzero at every point of its intersection with \(U\).

**Why the five divisors do not meet.** Any two different sets of four among five distinct branch points share exactly three points. Send those three common points to \(\infty,0,1\) by the unique projective linear transformation. In characteristic \(3\), a fourth branch point forms a supersingular elliptic double cover with the common three points only when that fourth point is \(-1\). If two different four-subsets both yielded supersingular elliptic quotients, their two remaining branch points would both have to be \(-1\), contradicting distinctness. Hence the five supersingularity divisors are pairwise disjoint over \(k\). It follows from the prime-to-three product decomposition that precisely zero or one elliptic factor is supersingular; the asserted ranks, \(a\)-numbers, and Newton slopes follow.

**Counts over all extensions.** Each supersingularity divisor becomes, after a permutation of the ordered branch labels and the corresponding rational renormalization, the divisor \(u=-1\). On that divisor \(v\) may be any element except \(0,1,-1\). The renormalization is defined over \(\mathbb F_3\), so each divisor has exactly \(q-3\) rational marked parameter pairs. They are disjoint. Thus \(N_4(q)=5(q-3)\). Since \(U(\mathbb F_q)\) has \((q-2)(q-3)\) points, subtraction yields \(N_5(q)=(q-3)(q-7)\). There is no lower-rank stratum.

## Verification

Run `python verify.py` after installing `sympy` as specified by `requirements.txt`. The verifier uses exact Gröbner-basis saturation with \(\Delta=uv(u-1)(v-1)(u-v)\) to check that every pair of the five equations has no point in \(U\), verifies the cleared Legendre Hasse conditions, and independently enumerates the parameters over \(\mathbb F_3\), \(\mathbb F_9\), and \(\mathbb F_{27}\) using explicit polynomial-field arithmetic. The packaged `verification_output.txt` records its exact output. The all-extension formula and geometric conclusions are proved above, not inferred from the three finite tests.

## Relationship to prior work

Carvacho, Hidalgo, and Quispe (2015 preprint, Section 5.1, Theorem 5.1) give the five elliptic quotient equations and their Jacobian isogeny over the complex numbers. Hidalgo and Reyes-Carocca (2016, Section 2) describe the classical Humbert moduli and the ordered five-point normalization, also in characteristic zero. These supply the natural object and quotient equations. They do not state the characteristic-three disjoint supersingularity geometry, sharp geometric rank floor, or all-extension ordered counts established here. The positive-characteristic use of the tame character decomposition and the Hasse calculation is justified independently in the proof. Historical priority remains conditional on any unindexed earlier characteristic-three calculations.

## Limitations

The theorem concerns the two-dimensional **ordered Humbert parameter surface**; its counts are not counts of geometric isomorphism classes and do not resolve descent of individual unmarked curves or the full isomorphism classification. No statement is made for arbitrary genus-five curves or characteristics other than \(3\). The normal form is only used when all five branch points are distinct. External literature coverage is necessarily incomplete; the historical novelty assessment should not be mistaken for a proof that no prior equivalent statement exists.

## References

1. Mariela Carvacho, Rubén A. Hidalgo, and Saúl Quispe, *Isogenous decomposition of the Jacobian of generalized Fermat curves*, arXiv:1507.02903v1, first public 10 July 2015, especially Sections 2.1.3 and 5.1. https://arxiv.org/html/1507.02903v1
2. Rubén A. Hidalgo and Sebastián Reyes-Carocca, *Fields of moduli of classical Humbert curves*, arXiv:1609.04895v1, first public 16 September 2016, especially Section 2. https://arxiv.org/abs/1609.04895
