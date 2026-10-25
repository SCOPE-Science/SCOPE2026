# Sharp \(5\)-rank floor and equianharmonic rigidity for genus-\(17\) Humbert–Edge curves

## Finding
Let \(k\) be algebraically closed of characteristic \(5\), and let \(B\subset\mathbb P^1(k)\) comprise six distinct points. Define \(C_B\) to be the maximal connected tame elementary abelian double cover of \(\mathbb P^1\) branched at all six points. It has genus \(17\). Let \(h(B)\) count those four-element subsets whose double-cover elliptic curve is supersingular, and let \(r(B)\) be the \(5\)-rank of the genus-two double cover branched at all of \(B\).

**Theorem.** For every such \(B\), \(h(B)\le4\), and if \(h(B)\ge3\), then \(r(B)=2\). The sharp Jacobian bound is
\[
 f_5(C_B)=15-h(B)+r(B)\ge13,
 \qquad a(C_B)\le4.
\]
The configuration \(h(B)=4\) occurs in exactly one \(\operatorname{PGL}_2(k)\)-orbit, represented by
\[
 B_*=\{\infty,0,1,2,\alpha,1-\alpha\},\qquad \alpha^2-\alpha+1=0.
\]
Here \(\alpha\in\mathbb F_{25}\setminus\mathbb F_5\). At \(B_*\), \(r(B_*)=2\), \(f_5(C_{B_*})=13\), \(a(C_{B_*})=4\), and the Newton slopes of its Jacobian are \(0^{13},(1/2)^8,1^{13}\). No assertion is made that every configuration with rank \(13\) belongs to this orbit.

## Assumptions and scope
All curves and invariants are geometric over an algebraically closed field of characteristic \(5\), and all branch points are distinct. The maximal cover has Galois group \((\mathbb Z/2\mathbb Z)^5\), obtained by adjoining five independent square roots of rational functions on \(\mathbb P^1\) whose ramification is supported at \(B\). There is no wild ramification. Riemann–Hurwitz gives \(2g-2=32(-2)+6\cdot16=32\), hence \(g=17\). The parameter \(h(B)\) concerns all \(15\) four-subsets, not merely rational branch points. A genus-two curve is **ordinary** when its Hasse–Witt/Cartier–Manin matrix is invertible. The \(a\)-number is \(\dim_k\operatorname{Hom}(\alpha_5,\operatorname{Jac}(C_B)[5])\).

## Proof
**1. Prime-to-\(5\) character decomposition.** Each nontrivial character of \((\mathbb Z/2)^5\) corresponds to a nonempty even subset \(T\subseteq B\), with the corresponding double quotient \(D_T\to\mathbb P^1\) branched at \(T\). A two-subset gives genus zero, each of the \(\binom64=15\) four-subsets gives an elliptic curve \(E_T\), and the six-subset gives one genus-two curve \(H_B\). For different characters the norm–pullback composites vanish, while for each quotient map of degree \(16\), the norm followed by pullback is multiplication by \(16\) in the appropriate order. The map
\[
  \prod_{|T|=4}\operatorname{Jac}(E_T)\times\operatorname{Jac}(H_B)\longrightarrow\operatorname{Jac}(C_B)
\]
formed from the pullbacks has kernel killed by \(16\) and is an isogeny, since the dimensions sum to \(15+2=17\). As \(5\nmid16\), it induces an isomorphism of \(5\)-divisible groups. The supersingular elliptic quotients have \(5\)-rank zero and \(a\)-number one, the ordinary elliptic quotients rank one and \(a\)-number zero. Therefore
\[
 f_5(C_B)=15-h(B)+r(B),\qquad a(C_B)=h(B)+a(H_B).
\]

**2. The four-point criterion.** For a normalized quadruple \(\{\infty,0,1,\lambda\}\), the Legendre elliptic curve has \(5\)-Hasse invariant proportional to \(\lambda^2-\lambda+1\). Hence it is supersingular exactly when \(\lambda\) is one of the two distinct roots \(\alpha,\beta=1-\alpha\) of that polynomial in \(\mathbb F_{25}\). Every ordered triple of branch points therefore has exactly two possible supersingular completions. In a five-point set two distinct supersingular quadruples, if present, share a triple; their remaining two points must be these two completions. Thus any five-point set contains at most two supersingular quadruples, with the two-case projectively equivalent to \(B_0=\{\infty,0,1,\alpha,\beta\}\).

**3. Six-point combinatorics and the shared-triple case.** Two four-subsets of a six-set intersect in two or three points. If a family of supersingular four-subsets has no pair sharing three points, their complementary two-subsets are pairwise disjoint, so the family has size at most three. Consequently \(h(B)\ge4\) forces two four-subsets sharing a triple. Normalizing their five-point union gives \(B=B_0\cup\{u\}\). Whenever \(h(B)\ge3\), the extra point \(u\) completes some triple of \(B_0\) to a supersingular quadruple. Such a completion belongs to \(\mathbb F_{25}\), hence \(u\in\mathbb F_{25}\setminus B_0\). This is a finite set of exactly \(21\) points. An exact enumeration, using only the displayed Legendre polynomial, gives \(12\) values with \(h=2\), \(6\) with \(h=3\), and \(3\) with \(h=4\). Precisely the values \(u=2,3,4\) give \(h=4\). The full five-root polynomial \(F_u(X)=X(X-1)(X-\alpha)(X-\beta)(X-u)\) has nonzero genus-two Hasse–Witt determinant for every one of the nine values with \(h\ge3\). The code in `verify_humbert17.py` independently enumerates all \(21\) cases with exact \(\mathbb F_{25}\) operations. The six anharmonic transformations permuting \(\infty,0,1\) preserve \(\{\alpha,\beta\}\) and act transitively on \(\{2,3,4\}\), proving the unique projective orbit for \(h=4\).

**4. Three supersingular quadruples without a shared triple.** The omitted pairs of the three four-subsets are disjoint and partition \(B\). Normalize the three quartets as \(\{\infty,0,1,\alpha\}\), \(\{\infty,0,b,c\}\), and \(\{1,\alpha,b,c\}\). The second one being supersingular forces \(b=\alpha c\) or \(b=(1-\alpha)c\). The supersingularity equation for the third quartet is obtained from
\[
 A=(c-1)(b-\alpha),\quad D=(c-\alpha)(b-1),\quad A^2-AD+D^2=0.
\]
Write \(P_1(c),P_2(c)\) for the two polynomials obtained by substituting the respective values of \(b\) (coefficients in \(\mathbb F_{25}\)). Let \(\Delta_i(c)\) be the determinant of the genus-two Hasse–Witt matrix computed from the square of \(X(X-1)(X-\alpha)(X-b)(X-c)\); its entries are the coefficients of degrees \(4,3,9,8\), arranged in that order as a two-by-two matrix. Exact polynomial Euclidean divisions over \(\mathbb F_{25}\) give
\[
 \gcd(P_1,\Delta_1)=\gcd(P_2,\Delta_2)=1.
\]
These are polynomial identities, not experimental samples. The attached verifier constructs the cross-ratio polynomials and Hasse determinants by symbolic polynomial arithmetic over \(\mathbb F_{25}\) and reproduces both coprimality certificates. Consequently the genus-two quotient is ordinary also in this disjoint-pairs case. This proves that \(h(B)\ge3\) always implies \(r(B)=2\).

**5. Sharp bounds.** If \(h\le2\), then \(15-h+r\ge13\) and \(h+a(H_B)\le2+2=4\). If \(h=3\) or \(4\), step 4 gives \(r=2\) and \(a(H_B)=0\); thus the \(5\)-ranks are \(14\) and \(13\) respectively, and the \(a\)-numbers are \(3\) and \(4\). The explicit sextuple \(B_*\) attains both bounds. Its Jacobian is prime-to-\(5\) isogenous to thirteen ordinary and four supersingular elliptic factors (counting the two ordinary factors of \(H_B\) only at the level of slopes), giving the stated Newton polygon.

## Verification
Run `python3 verify_humbert17.py` with Python 3 and only its standard library. It constructs \(\mathbb F_{25}=\mathbb F_5[\alpha]/(\alpha^2-\alpha+1)\); exhausts exactly \(21\) allowed choices \(u\) in the shared-triple case; independently computes the genus-two Hasse determinant from squared quintic coefficients; verifies the two disjoint-triple polynomial coprimality identities via full Euclidean division; and verifies the explicit extremal sextuple. Expected terminal line begins `VERIFY_OK: GF25 exceptional five-set completions`. No test over a finite set is treated as a proof for arbitrary \(B\): the finite restriction is derived in step 3, and step 4 is a symbolic identity covering the remaining algebraic-closure case.

## Relationship to prior work
Carvacho–Hidalgo–Quispe, *Isogenous decomposition of the Jacobian of generalized Fermat curves* (first public arXiv version 2015-07-10, arXiv:1507.02903), Section 5.3 and Theorem 5.3, gives the classical sixteen-factor decomposition (fifteen elliptic quotients and one genus-two quotient) in the complex setting, building on Yamauchi's earlier work. Edge's 1969 treatment and subsequent Humbert–Edge work supply the historic family and its geometric context. These decompositions are **inputs**, not the new claim. The contribution here is the sharp characteristic-five genus-seventeen rank bound, the simultaneous supersingular-quartet cap, the genus-two ordinarity compatibility, and the unique maximal quartet configuration. The prime-to-characteristic argument is included rather than inferred from a complex isogeny alone.

## Limitations
The theorem concerns the maximal exponent-two cover with its specified six-point branch configuration, over an algebraically closed field of characteristic five. It is not a classification of all genus-seventeen curves, all minimal-rank branch orbits, or all possible Newton polygons of this family. The unique-orbit assertion applies **only** to \(h=4\). The full classification of ranks for \(h\le2\) is not attempted. This proof has not undergone independent external validation, and historical priority beyond the cited and searched sources remains a residual risk.

## References
1. M. Carvacho, R. A. Hidalgo, S. Quispe, *Isogenous decomposition of the Jacobian of generalized Fermat curves*, arXiv:1507.02903, first submitted 2015-07-10; in particular Section 5.3.
2. W. L. Edge, *Three Plane Sextics and their Automorphisms*, Canadian Journal of Mathematics 21 (1969), 1263–1278, DOI: 10.4153/CJM-1969-139-6.
3. A. Castorena, J. B. Frías-Medina, *Geometric aspects on Humbert-Edge curves of type 5, Kummer surfaces and hyperelliptic curves of genus 2*, Glasgow Mathematical Journal (2023), Section 3 (geometric context; no characteristic-five rank theorem claimed).
