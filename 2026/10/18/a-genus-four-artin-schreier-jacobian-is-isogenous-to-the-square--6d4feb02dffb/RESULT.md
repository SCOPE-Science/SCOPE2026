# A genus-four Artin–Schreier Jacobian is isogenous to the square of an explicit simple genus-two Jacobian

## Finding

Over \(\mathbb F_3\), let \(X\) be the smooth projective curve with function field
\[
 y^3-y=\frac{x^2}{x^3+2x^2+1},
\]
and let \(C\) be the smooth projective genus-two hyperelliptic curve
\[
 v^2=u^5+u^4+u^2+1.
\]
The two complete Hasse–Weil numerators satisfy
\[
 L_X(T)=L_C(T)^2,\qquad
 L_C(T)=1+T+T^2+3T^3+9T^4.
\]
Consequently there is an **unpolarized** isogeny defined over \(\mathbb F_3\)
\[
 \operatorname{Jac}(X)\sim_{\mathbb F_3}\operatorname{Jac}(C)^2.
\]
The abelian surface \(\operatorname{Jac}(C)\) is simple and ordinary over \(\mathbb F_3\). In particular,
\[
 \#\operatorname{Jac}(X)(\mathbb F_3)=225.
\]
The defining curve \(X\), its genus, its ordinary nature and its full geometric automorphism group \(C_3\) are previously known [1]. The claimed contributions here are the **exact numerator** and the **explicit genus-two square isogeny class**.

## Assumptions and scope

All varieties and isogenies are defined over \(\mathbb F_3\), and a curve defined by an affine function-field equation always means its unique smooth projective model. The polynomial \(q(x)=x^3+2x^2+1\) has no root in \(\mathbb F_3\), hence is irreducible cubic; its three roots are simple geometric poles of \(x^2/q(x)\). At infinity this rational function has value zero. Thus the degree-three Artin–Schreier map is totally ramified once above each geometric pole, and unramified over infinity, with three \(\mathbb F_3\)-rational points over infinity. The standard Riemann–Hurwitz formula gives
\[
 2g(X)-2=-6+3\cdot(3-1)(1+1)=6,
\]
so \(g(X)=4\). The simple-pole Deuring–Shafarevich formula gives \(3\)-rank \(4\), hence ordinarity. These numerical geometric premises can be derived directly from the defining equation and agree with [1, Lemma 5.3].

The genus-two equation is squarefree in characteristic three: for \(h(u)=u^5+u^4+u^2+1\) its derivative is \(h'(u)=2u^4+u^3+2u\), and the following explicit polynomial Bézout identity holds in \(\mathbb F_3[u]\):
\[
 (1-u^2-u^3)h(u)+(-u^2-u^4)h'(u)=1.
\]
Thus \(C\) is a smooth genus-two curve, with a single rational point at infinity.

## Proof

**1. The four extension-field counts for \(X\).** Write \(F_n=\mathbb F_{3^n}\), let \(e_n\) count the poles of \(x^2/q(x)\) rational over \(F_n\), and let \(z_n\) count finite, nonpole \(a\in F_n\) with \(\operatorname{Tr}_{F_n/\mathbb F_3}(a^2/q(a))=0\). The Artin–Schreier equation \(b^3-b=c\) has three solutions in \(F_n\) precisely when \(\operatorname{Tr}(c)=0\), and none otherwise. A rational pole contributes exactly one rational point of \(X\); the three points over infinity always contribute three. Since the three roots of \(q\) form one Frobenius orbit, \(e_n=3\) when \(3\mid n\), otherwise \(e_n=0\). It follows that
\[
 N_n:=\#X(F_n)=3+e_n+3z_n.
\]
Exact finite-field arithmetic gives

| \(n\) | \(e_n\) | \(z_n\) | \(N_n\) |
|---:|---:|---:|---:|
| 1 | 0 | 1 | 6 |
| 2 | 0 | 3 | 12 |
| 3 | 3 | 12 | 42 |
| 4 | 0 | 43 | 132 |

The enclosed dependency-free code constructs each finite field from a proved-irreducible modulus, checks these trace counts, and also calculates the fibres by the independent value-table method for \(b^3-b\). Every finite set in this four-row calculation is exhausted; no extrapolation is made from sampling.

**2. Recover the complete numerator.** Write
\[
 L_X(T)=\sum_{j=0}^{8}c_jT^j,\qquad c_0=1.
\]
For \(s_n=3^n+1-N_n\) the first four power sums are \((-2,-2,-14,-50)\). Newton's identity gives
\[
 nc_n=-\sum_{k=1}^{n}c_{n-k}s_k,
\]
so \((c_1,c_2,c_3,c_4)=(2,3,8,25)\). The genus-four Weil functional equation is
\[
 c_{8-j}=3^{4-j}c_j\quad (0\le j\le4),
\]
and determines the entire numerator:
\[
 L_X(T)=1+2T+3T^2+8T^3+25T^4+24T^5+27T^6+54T^7+81T^8.
\]
Direct multiplication verifies
\[
 L_X(T)=(1+T+T^2+3T^3+9T^4)^2.
\]
Point enumeration for the additional extension degrees \(5,6,7,8\) agrees with this same polynomial; it is a consistency check, not a replacement for the genus-four functional equation.

**3. Construct a genus-two isogeny factor.** For the squarefree quintic model \(C\), exhaustive arithmetic yields
\[
 \#C(\mathbb F_3)=5,\qquad \#C(\mathbb F_9)=11.
\]
The genus-two numerator has first two coefficients \(1,1\), by the same Newton identity, and its functional equation forces
\[
 L_C(T)=1+T+T^2+3T^3+9T^4.
\]
Therefore \(L_X=L_C^2\), and the finite-field isogeny theorem [2, 4] gives an \(\mathbb F_3\)-isogeny \(\operatorname{Jac}(X)\sim\operatorname{Jac}(C)^2\).

**4. Simplicity, ordinarity and rational points.** The characteristic polynomial of Frobenius of \(\operatorname{Jac}(C)\) is
\[
 P(t)=t^4+t^3+t^2+3t+9.
\]
Modulo \(2\), it is the irreducible cyclotomic polynomial \(\Phi_5(t)=t^4+t^3+t^2+t+1\), since the multiplicative order of \(2\) modulo \(5\) is \(4\). Hence \(P\) is irreducible over \(\mathbb Q\) and \(\operatorname{Jac}(C)\) is simple over \(\mathbb F_3\). The coefficient of \(t^2\) in \(P\) is \(1\), so this abelian surface is ordinary. Finally,
\[
 \#\operatorname{Jac}(X)(\mathbb F_3)=L_X(1)=L_C(1)^2=15^2=225.
\]

## Verification

Run `python3 verify.py` with the Python standard library. It verifies irreducibility of each field modulus by checking all possible monic factors up to half the degree, exhaustively counts the rational fibres in extensions of degrees \(1\) through \(8\), and compares two independent fibre-count formulas (direct \(b^3-b\) image histogram and absolute trace). It then checks Newton identities, the genus-four functional equation, the full perfect-square identity, and the genus-two Bézout certificate and point counts. Successful execution ends with `VERIFY_OK`. The entire proof needs only the first four field extensions and the first two genus-two field extensions; remaining counts are redundant arithmetic cross-checks.

## Relationship to prior work

Tafazolian and Kazemifard [1, Lemma 5.3] supply precisely the genus-four curve \(X\) and establish its genus, \(3\)-rank and geometric automorphism group. Their results do not present its zeta polynomial, the explicit genus-two curve \(C\), or the square isogeny between the Jacobians. Howe, Nart and Ritzenthaler [2] classify genus-two Weil polynomials and furnish general finite-field isogeny background. Their existence criteria do not calculate the Frobenius polynomial of this specified Artin–Schreier curve. Bruin and Kulkarni [3] study much stronger polarization-dependent geometric decompositions of some genus-four Jacobians; no such polarization-compatible decomposition is asserted here. The equality proved here is of unpolarized isogeny classes, with a new explicit pairing of models.

## Limitations

The theorem is about the displayed \(\mathbb F_3\)-models and isogenies over \(\mathbb F_3\); it is not a uniform theorem about all genus-four Artin–Schreier curves. No isogeny morphism, kernel, minimal degree, compatible principal polarization or geometric automorphism of order two is constructed or claimed. Simplicity is established over \(\mathbb F_3\), not absolute simplicity. These calculations use a published curve and familiar finite-field tools; a previously unindexed exact zeta tabulation of the same curve would reduce the originality claim.

## References

[1] S. Tafazolian and A. Kazemifard, *Artin-Schreier curves of prescribed p-rank without extra automorphisms*, arXiv:2610.13279v1 (first public submission 9 October 2026), Lemma 5.3, Section 6. https://arxiv.org/abs/2610.13279

[2] E. W. Howe, E. Nart and C. Ritzenthaler, *Jacobians in isogeny classes of abelian surfaces over finite fields*, arXiv:math/0607515v3 (2007), Theorem 1.2. https://arxiv.org/abs/math/0607515

[3] N. Bruin and A. Kulkarni, *On (2,2)-decomposable genus 4 Jacobians*, Canadian Journal of Mathematics (2025), Section 7, DOI:10.4153/S0008414X25101557. https://doi.org/10.4153/S0008414X25101557

[4] J. Tate, *Endomorphisms of abelian varieties over finite fields*, Inventiones Mathematicae 2 (1966), 134–144.
