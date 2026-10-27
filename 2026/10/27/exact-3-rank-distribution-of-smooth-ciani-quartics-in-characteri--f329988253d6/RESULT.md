# Exact \(3\)-rank distribution of smooth Ciani quartics in characteristic \(3\)

## Finding
For every integer \(m\ge 1\), set \(q=3^m\). Consider all homogeneous quartic equations
\[
 C_{A,B,C,D,E,F}:\quad AX^4+BY^4+CZ^4+DX^2Y^2+EX^2Z^2+FY^2Z^2=0
\]
with coefficients in \(\mathbb F_q\), modulo **common nonzero scalar multiplication only**. Fix the displayed projective coordinates: distinct marked coefficient classes are counted separately even when the resulting curves are isomorphic. Keep only geometrically smooth curves. For such a curve, let \(r\) be the \(3\)-rank of its Jacobian and \(a\) its \(a\)-number.

The complete distribution is
\[
\begin{array}{c|c|c}
 r & a & \text{number of marked equations}\\ \hline
 0 & 3 & (q-1)^2\\
 1 & 2 & 3(q-1)^2(q-2)\\
 2 & 1 & 3(q-1)^2(q-2)(q-3)\\
 3 & 0 & (q-1)^2(q^3-7q^2+18q-18).
\end{array}
\]
Every geometrically smooth member has \(a+r=3\). In particular, over \(\mathbb F_3\), the sixteen smooth marked equations comprise four of \(3\)-rank zero and twelve of rank one: **no smooth marked Ciani quartic over \(\mathbb F_3\) is ordinary**. Over \(\mathbb F_9\), the four rank counts are respectively \(64,1344,8064,19584\). Their sum, for every \(q\), is
\[
 (q-1)^2(q^3-4q^2+6q-5).
\]
The result is a coefficient-marked enumeration, not a count of \(\mathbb F_q\)-isomorphism classes or of geometrically isomorphic curves.

## Assumptions and scope
Throughout, \(q\) is an arbitrary positive integral power of \(3\), the base field is \(\mathbb F_q\), and geometric smoothness is tested after algebraic closure. The genus of every smooth plane quartic is \(3\). The \(3\)-rank is the dimension of the stable Frobenius image on \(H^1(C,\mathcal O_C)\); the \(a\)-number is the dimension of the Cartier kernel on holomorphic differentials. These quantities are invariant under extension to an algebraic closure. No condition is imposed on rational points of the quartic.

Since \(A,B,C\ne0\) for every smooth member, common scalar multiplication gives a **unique** representative with \(A=1\). Write \(B=b\), \(C=c\), \(D=d\), \(E=e\), \(F=f\), so \(b,c\in\mathbb F_q^\times\) and \(d,e,f\in\mathbb F_q\). The letter \(f\) in this local normalization denotes a coefficient, not the \(3\)-rank \(r\).

## Proof
**1. The geometric smoothness test.** Introduce the ternary quadratic form
\[
 Q(U,V,W)=U^2+bV^2+cW^2+dUV+eUW+fVW.
\]
The quartic is obtained by substituting \(U=X^2,V=Y^2,W=Z^2\). In characteristic \(3\), a symmetric matrix for \(Q\) is
\[
 M=\begin{pmatrix}1&-d&-e\\-d&b&-f\\-e&-f&c\end{pmatrix}.
\]
Any vanishing diagonal coefficient of the original quartic makes its corresponding coordinate vertex singular. For \(b,c\ne0\), a double zero on one coordinate line occurs exactly when one of \(b-d^2\), \(c-e^2\), or \(bc-f^2\) vanishes. If none vanishes, a singularity in the dense coordinate torus is equivalent to \(\det M=0\): if a null vector of \(M\) had a zero coordinate, the complementary principal \(2\)-minor would vanish, contradicting the three nonzero binary discriminants. Conversely, a nonzero null vector with three nonzero coordinates lifts by square roots over the algebraic closure to a singular point of the quartic. Therefore geometric smoothness is **equivalent** to
\[
 b,c\ne0,\quad b-d^2\ne0,\quad c-e^2\ne0,\quad bc-f^2\ne0,\quad
 \Delta=(b-d^2)(c-e^2)-(f+de)^2\ne0. \tag{1}
\]
This proves necessity and sufficiency, including points on the coordinate lines.

**2. The Hasse--Witt diagonal.** From the exact sequence of a plane quartic and the standard monomial basis of \(H^2(\mathbb P^2,\mathcal O(-4))\), choose
\[
 X^{-2}Y^{-1}Z^{-1},\quad X^{-1}Y^{-2}Z^{-1},\quad X^{-1}Y^{-1}Z^{-2}.
\]
Frobenius is represented by multiplication by the square of the defining quartic followed by cubing each Laurent monomial. Every monomial of the defining quartic has even exponents. Consequently the off-diagonal Hasse--Witt entries vanish by parity, while the three diagonal coefficients of the squared polynomial at exponent triples \((4,2,2),(2,4,2),(2,2,4)\) give, up to the common nonzero factor \(2\),
\[
 H=\operatorname{diag}(f+de,\;be+df,\;cd+ef). \tag{2}
\]
The displayed basis concerns cohomology, so the irrelevant common scalar does not affect any rank. Because \(\mathbb F_q\) is perfect and the matrix is diagonal, the product of the first \(n\) Frobenius twists has a nonzero entry precisely wherever \(H\) does. Thus the stable Frobenius rank is the number of nonzero expressions in (2), and the Cartier-kernel dimension is three minus this number. This proves \(a+r=3\) and reduces the enumeration to counting zeros of three explicit functions.

**3. Number of smooth equations.** Let \(\chi\) be the quadratic character of \(\mathbb F_q\), extended by \(\chi(0)=0\). First choose \((d,b)\) and \((e,c)\) satisfying \(b,c\ne0\), \(b\ne d^2\), \(c\ne e^2\). Each pair has \((q-1)^2\) choices; there are therefore \((q-1)^4\) such quadruples. With an arbitrary coefficient \(f\), there are \(q(q-1)^4\) preliminary choices.

Write \(S=(b-d^2)(c-e^2)\ne0\). The two remaining excluded conditions are \(f^2=bc\) and \((f+de)^2=S\). For a fixed nonzero target \(t\), the number of solutions of \(z^2=t\) is \(1+\chi(t)\). Direct quadratic-character summation yields
\[
\begin{aligned}
\sum_{d,b:\,b\ne0,\ b\ne d^2}\chi(b)&=-(q-1),\\
\sum_{d,b:\,b\ne0,\ b\ne d^2}\chi(b-d^2)&=-(q-1)\chi(-1).
\end{aligned}
\]
Hence **each** excluded equality contributes exactly \((q-1)^4+(q-1)^2\) preliminary quintuple choices.

Their intersection has \((q-1)^3\) choices. Indeed, if \(d=e=0\), the equality \(f^2=bc\) yields \((q-1)^2\) choices; if precisely one of \(d,e\) vanishes, there are none. If both are nonzero, put \(u=b/d^2\), \(v=c/e^2\), and \(w=f/(de)\). The simultaneous equalities reduce to
\[
 w^2=uv,\qquad (w+1)^2=(u-1)(v-1),
\]
so, in characteristic \(3\), \(w=u+v\) and \((u-v)^2=0\). Thus \(u=v\in\mathbb F_q^\times\setminus\{1\}\), and \(d,e\) are arbitrary nonzero elements, producing \((q-1)^2(q-2)\) choices. Inclusion--exclusion now gives the total
\[
\begin{aligned}
 N_q&=q(q-1)^4-2\big((q-1)^4+(q-1)^2\big)+(q-1)^3\\
 &=(q-1)^2(q^3-4q^2+6q-5). \tag{3}
\end{aligned}
\]
This derivation does not assume an external counting table.

**4. Rank strata.** Let \(T_j\) be the number of smooth marked equations for which a prescribed set of \(j\) of the three diagonal entries of (2) is zero. Symmetry under permuting the coordinates makes this number independent of the prescribed set. Obviously \(T_0=N_q\).

For the first entry to vanish, \(f=-de\); criterion (1) then reduces to \(b,c\ne0\), \(b\ne d^2\), \(c\ne e^2\), and \(bc\ne d^2e^2\). Partitioning into \((d,e)=(0,0)\), exactly one nonzero, and both nonzero gives respectively
\[
 (q-1)^2,\quad 2(q-1)^2(q-2),\quad (q-1)^2(q-2)(q-3).
\]
Therefore
\[
 T_1=(q-1)^2(q^2-3q+3). \tag{4}
\]
If the first two entries vanish, the second equation becomes \(e(b-d^2)=0\). Smoothness forces \(e=0\), and then the first forces \(f=0\). Thus \(d\) is arbitrary subject to \(b\ne d^2\), and
\[
 T_2=(q-1)^3. \tag{5}
\]
The third entry additionally vanishes exactly when \(d=0\), yielding
\[
 T_3=(q-1)^2. \tag{6}
\]
By inclusion--exclusion among the three zero sets, the counts with exactly three, two, one, and zero vanishing diagonal entries are, respectively,
\[
 T_3,\qquad 3(T_2-T_3),\qquad 3(T_1-2T_2+T_3),\qquad T_0-3T_1+3T_2-T_3.
\]
Substitution of (3)--(6) gives exactly the four displayed rank formulas. All quantified statements hold for every \(m\ge1\).

## Verification
The standalone dependency-free program `verify.py` expands the quartic square to reconstruct all three relevant Hasse--Witt coefficients and independently exhausts the normalized sextuples over \(\mathbb F_3\) and \(\mathbb F_9\), implementing \(\mathbb F_9=\mathbb F_3[u]/(u^2+1)\). Running `python3 verify.py` returns `VERIFY_OK` and produces the exact vectors
\[
 (4,12,0,0),\qquad (64,1344,8064,19584).
\]
It additionally checks the total-count identity symbolically at several values of \(q\). The **proof for every finite extension** is the character-sum and rank-stratum argument above; finite enumeration alone would not prove it.

## Relationship to prior work
Ohashi's *On the maximality of genus-3 nonhyperelliptic curves of Ciani type* (first public arXiv version, January 31, 2022) studies smooth Ciani quartics and superspeciality; its Lemma 2.1 gives the smoothness test in normalized geometric coordinates, and Section 3 gives a degree-eight isogeny to three elliptic quotients. Neither is the all-\(q\), coefficient-marked \(3\)-rank distribution established here. This result concerns all four ranks and includes a separate arithmetic count of the indicated rank strata, not just the characterization of superspecial members.

Lercier--Ritzenthaler--Rovetta--Sijsling study moduli representatives and Frobenius-trace distributions for smooth plane quartics, with a large-characteristic hypothesis and finite-field experiments for primes at least eleven. Their isomorphism-class framework and field range differ from the characteristic-three marked-equation enumeration here. General Hasse--Witt/Cartier methods explain how to compute a rank for an individual curve, but do not by themselves give the four uniform counting polynomials.

## Limitations
The count is for fixed-coordinate coefficient sextuples modulo **common scalar**, not a stack-weighted count, moduli-space point count, automorphism-weighted count, or count of isomorphism classes. The assumption of characteristic \(3\) is essential to the diagonal coefficient simplification and the character-sum identities as used here; there is no assertion for other characteristics. The self-review is not an independent mathematical audit, and undiscovered equivalent calculations remain a literature risk.

## References
1. R. Ohashi, *On the maximality of genus-3 nonhyperelliptic curves of Ciani type*, arXiv:2201.12996v1 (posted 2022-01-31), especially Lemma 2.1 and Section 3. https://arxiv.org/abs/2201.12996
2. R. Lercier, C. Ritzenthaler, F. Rovetta, J. Sijsling, *Parametrizing the moduli space of curves and applications to smooth plane quartics over finite fields*, arXiv:1403.0562, particularly the introduction and experimental range described in Section 5. https://arxiv.org/abs/1403.0562
3. T. O. Çelik, Y. Elias, B. Güneş, R. Newton, E. Ozman, R. Pries, L. Thomas, *Non-ordinary curves with a Prym variety of low p-rank*, Women in Numbers Europe II (2018), pp. 117--158, doi:10.1007/978-3-319-74998-3_8 (different Prym-existence problem).
