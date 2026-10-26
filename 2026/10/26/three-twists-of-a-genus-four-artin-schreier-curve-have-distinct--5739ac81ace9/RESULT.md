# Three twists of a genus-four Artin–Schreier curve have distinct simple Jacobians

## Finding

Let \(X_c\) be the smooth projective model over \(\mathbb F_3\) of
\[
 X_c:\qquad y^3-y=x^2+x+x^{-2}+c,\qquad c\in\{0,1,2\}.
\]
The three curves are **exactly the three** \(\mathbb F_3\)-isomorphism classes of forms of the geometric curve \(X_0\). They are mutually geometrically isomorphic and each has genus \(4\), \(3\)-rank \(2\), and full geometric curve-automorphism group \(C_3\). Their genus-four Weil numerators \(L_c(T)\), with \(Z(X_c,T)=L_c(T)/((1-T)(1-3T))\), are:
\[
\begin{aligned}
L_0(T)&=1+T-2T^2+3T^3+15T^4+9T^5-18T^6+27T^7+81T^8,\\
L_1(T)&=1-2T+T^2+6T^3-21T^4+18T^5+9T^6-54T^7+81T^8,\\
L_2(T)&=1+T+4T^2+9T^3+15T^4+27T^5+36T^6+27T^7+81T^8.
\end{aligned}
\]
Each polynomial is irreducible over \(\mathbb Q\). Consequently, the three Jacobians are **simple and pairwise non-isogenous over \(\mathbb F_3\)**, even though their underlying principally polarized Jacobians become isomorphic over \(\overline{\mathbb F}_3\). The Newton polygon of each has slope multiplicities \(0^{\times2}, (1/2)^{\times4}, 1^{\times2}\).

## Assumptions and scope

All curves and morphisms are over \(\mathbb F_3\) unless a field extension is explicitly indicated. The equation is understood as the smooth projective normalization of its affine function field. The polynomial \(L_c(T)\) is the numerator of the Hasse–Weil zeta function in the convention \(\exp(\sum_{m\ge1}\#X_c(\mathbb F_{3^m})T^m/m)\). “Simple” means no nonzero proper abelian subvariety defined over \(\mathbb F_3\); no claim of absolute simplicity is made. “All forms” refers to the single fixed \(\overline{\mathbb F}_3\)-isomorphism class of \(X_0\), not to all genus-four curves or all Artin–Schreier covers.

## Proof

**Genus and automorphisms.** The rational function \(f(x)=x^2+x+x^{-2}\) has two poles, at \(0\) and \(\infty\), both of order \(2\), prime to \(3\). Each has different exponent \((3-1)(2+1)=6\), so Riemann–Hurwitz gives \(2g-2=-6+6+6=6\), hence \(g=4\); the Deuring–Shafarevich formula gives \(3\)-rank \((2-1)(3-1)=2\). Adding constants does not alter geometric ramification. Proposition 4.2 of Tafazolian–Kazemifard proves \(\operatorname{Aut}_{\overline{\mathbb F}_3}(X_0)=\langle y\mapsto y+1\rangle\cong C_3\). These three automorphisms are defined over \(\mathbb F_3\), hence the Galois action on this full automorphism group is trivial. For the procyclic absolute Galois group of \(\mathbb F_3\), nonabelian descent becomes
\[
 H^1(\operatorname{Gal}(\overline{\mathbb F}_3/\mathbb F_3),C_3)
 =\operatorname{Hom}_{\mathrm{cont}}(\widehat{\mathbb Z},C_3)\cong C_3.
\]
The cocycle classes are represented by translating the Artin–Schreier right-hand side by \(c=0,1,2\). Indeed, over an algebraic closure select \(a\) with \(a^3-a=c\), and the substitution \(y\mapsto y-a\) identifies \(X_c\) with \(X_0\); the Frobenius displacement \(a^3-a=c\) gives the respective cocycle. Thus all forms are represented, once each, by the displayed three curves.

**Point counts.** For \(q=3^m\), the Artin–Schreier map \(y\mapsto y^3-y\) has image the trace-zero subspace of \(\mathbb F_q\), with fibers of size \(3\). Both branch poles are rational and each has a unique point above it, so
\[
 \#X_c(\mathbb F_{3^m})=
 2+3\#\{x\in\mathbb F_{3^m}^{\times}:\operatorname{Tr}_{\mathbb F_{3^m}/\mathbb F_3}(x^2+x+x^{-2})=-mc\}.
\]
Exact enumeration in the finite field \(\mathbb F_3[t]/(t)\) for \(m=1\), \(\mathbb F_3[t]/(t^2+1)\) for \(m=2\), \(\mathbb F_3[t]/(t^3+2t^2+1)\) for \(m=3\), and \(\mathbb F_3[t]/(t^4+t^3+t^2+1)\) for \(m=4\) yields trace histograms (trace \(0,1,2\) in that order):
\[
 (1,1,0),\quad(1,2,5),\quad(14,9,3),\quad(37,29,14).
\]
The resulting table of \(\#X_c(\mathbb F_{3^m})\) for \(m=1,2,3,4\) is
\[
\begin{array}{c|rrrr}
 c\backslash m&1&2&3&4\\\hline
0&5&5&44&113\\
1&2&8&44&44\\
2&5&17&44&89
\end{array}
\]
(The degree-one quotient polynomial is written \(t\) in the verification program; \(\mathbb F_3[t]/(t)\cong\mathbb F_3\).)

**Weil polynomials.** Put \(S_m=3^m+1-\#X_c(\mathbb F_{3^m})\) and \(L_c(T)=\sum_{j=0}^{8}a_jT^j\), \(a_0=1\). Newton identities
\[
 j a_j=-\sum_{m=1}^j a_{j-m}S_m\qquad (1\le j\le4)
\]
determine \(a_1,\ldots,a_4\). The genus-four zeta functional equation gives \(a_{8-j}=3^{4-j}a_j\) for \(0\le j\le4\), determining the remaining coefficients and producing precisely the three displayed polynomials.

**Irreducibility.** Each polynomial is primitive in \(\mathbb Z[T]\), has degree \(8\), and has leading coefficient \(81\), which is a unit modulo both \(2\) and \(5\). Their reductions modulo \(2\) are respectively
\[
\begin{aligned}
 \overline L_0&=(T^4+T+1)(T^4+T^3+1),\\
 \overline L_1&=(T^4+T^3+T^2+T+1)^2,\\
 \overline L_2&=(T^4+T+1)(T^4+T^3+1).
\end{aligned}
\]
Every displayed degree-four factor is irreducible over \(\mathbb F_2\). The reductions modulo \(5\) factor as
\[
\begin{aligned}
 \overline L_0&=(T^2+2)(T^6+2T^5-2T-2),\\
 \overline L_1&=(T^2+T+2)(T^6+2T^4+T^3-T^2-2),\\
 \overline L_2&=(T^2-T+2)(T^6-2T^5+2T^4-2T^3-T^2+2T-2).
\end{aligned}
\]
Each listed quadratic and sextic is irreducible modulo \(5\); this is verified by Rabin's gcd/power criterion in `verify.py`. Any proper factor of \(L_c\) over \(\mathbb Q\) would have degree \(4\) by the modulo-\(2\) factorization (multiplicities included), but have degree \(2\) or \(6\) by the modulo-\(5\) factorization. This contradiction proves irreducibility over \(\mathbb Q\). By the finite-field isogeny theorem, an irreducible characteristic polynomial of geometric Frobenius implies that the Jacobian is simple over \(\mathbb F_3\); the distinct polynomials imply pairwise non-isogeny over that field. The coefficient valuations give a Newton polygon with vertices \((0,0),(2,0),(6,2),(8,4)\) for each curve and hence slopes \(0,1/2,1\) with multiplicities \(2,4,2\).

## Verification

Run `python3 verify.py` with Python 3.9 or newer, no external dependencies. It checks all four finite-field irreducibility certificates, enumerates every nonzero field element and independently every affine pair \((x,y)\) for each of the three twists and degrees \(m=1,2,3,4\), confirms all twelve point counts, derives the coefficients from Newton identities and the functional equation, and verifies both modular factorizations and each factor's irreducibility by finite-field polynomial gcd tests. The expected terminal output begins `VERIFY_OK`. These finite enumerations suffice here because the genus-four zeta functional equation reduces the numerator to the first four point counts; no experiment is used to extrapolate infinitely many unverified points. The geometric automorphism statement is explicitly imported from the cited source; the verification program does not independently reconstruct that paper's proof.

## Relationship to prior work

Tafazolian and Kazemifard, Proposition 4.2, introduce exactly the \(c=0\) curve, determine genus, \(3\)-rank and the full geometric curve-automorphism group, and use it in their existence classification. Their §§6–7 discuss the resulting Jacobian automorphism groups and further invariants but do not provide the three constant twists' complete Weil numerators or the finite-field simplicity/non-isogeny classification. The genus and geometric automorphism conclusions and the general Artin–Schreier and zeta-function methods are prior results, not contributions here. The finite-field zeta numerators, their explicit irreducibility certificates, and the resulting complete arithmetic distinction of the three forms are the present claim.

## Limitations

Simplicity and non-isogeny are asserted only over \(\mathbb F_3\), not over \(\overline{\mathbb F}_3\). The three Jacobians are in fact geometrically isomorphic as principally polarized abelian varieties because the curves are geometrically isomorphic. This is a classification only of forms of one geometric curve; no classification of all genus-four Artin–Schreier curves is claimed. The cited primary geometric automorphism theorem is a premise, not independently reproved by the finite-field script. The literature search did not find identical Weil-polynomial tables, but an unindexed computation in previous work remains possible. Independent validation has not been undertaken.

## References

1. S. Tafazolian and A. Kazemifard, *Artin–Schreier Curves of Prescribed p-Rank Without Extra Automorphisms*, arXiv:2610.13279, first posted 2026-10-09, especially Proposition 4.2 and §§6–7.
2. J. Tate, *Endomorphisms of abelian varieties over finite fields*, Invent. Math. 2 (1966), 134–144 (isogeny/characteristic-polynomial criterion).
3. Standard Artin–Schreier, Riemann–Hurwitz, Deuring–Shafarevich, and Weil zeta functional equation results, as referenced in item 1.
