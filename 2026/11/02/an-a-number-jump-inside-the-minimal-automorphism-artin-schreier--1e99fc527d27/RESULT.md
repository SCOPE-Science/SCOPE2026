# An a-number jump inside the minimal-automorphism Artin–Schreier locus

## Finding

Let \(k\) be an algebraically closed field of characteristic \(3\). For **every** \(a\in k\), let \(C_a\) denote the smooth projective model of the separable affine Artin–Schreier equation
\[
y^3-y=x^{10}+a x^8+x^7.
\]
Then
\[
g(C_a)=9,\qquad \gamma_3(C_a)=0,\qquad
\operatorname{Aut}_k(C_a)\cong\mathbb Z/3\mathbb Z.
\]
The automorphisms are exactly \((x,y)\mapsto(x,y+c)\), with \(c\in\mathbb F_3\). Nevertheless, the \(a\)-number of the Jacobian is not constant:
\[
\boxed{\quad a(C_a)=\begin{cases}5,&a=0,\\4,&a\neq0.\end{cases}\quad}
\]
Thus the rank-four Cartier locus in this one-parameter family is exactly the reduced parameter divisor \(a=0\); all other fibers have Cartier rank five. Both possibilities occur for curves defined over the prime field \(\mathbb F_3\). In particular, \(C_0\) and \(C_1\) cannot become isomorphic over the algebraic closure.

## Assumptions and scope

All statements concern the **geometric** smooth projective curves, geometric automorphisms and the Jacobian over the algebraically closed field \(k\). The affine equation is not being asserted smooth at its naive projective closure; its smooth projective model is used. The \(3\)-rank \(\gamma_3(C)\) is the rank of the étale part of \(\operatorname{Jac}(C)[3]\); the \(a\)-number is \(\dim_k\operatorname{Hom}(\alpha_3,\operatorname{Jac}(C)[3])\), equivalently the dimension of the kernel of the Cartier operator on holomorphic differentials.

## Proof

**Genus and \(3\)-rank.** The right-hand side has precisely one pole on the rational \(x\)-line, of order ten, which is prime to three. Artin–Schreier Riemann–Hurwitz gives
\[
2g(C_a)-2=-6+(3-1)(10+1)=16,
\]
so \(g(C_a)=9\). The Deuring–Shafarevich formula for a degree-three Artin–Schreier cover with one pole gives \(\gamma_3(C_a)=(3-1)(1-1)=0\). The point \(P_\infty\) over the pole is unique and totally ramified, with
\[
\operatorname{ord}_{P_\infty}(x)=-3,\quad
\operatorname{ord}_{P_\infty}(y)=-10,\quad
\operatorname{ord}_{P_\infty}(dx)=16.
\]
The last equality follows because the affine cover is étale over the finite \(x\)-line, so \(dx\) has no finite zeros or poles and is a canonical differential of degree \(2g-2=16\).

**Full automorphism group.** First, the rational subfield \(k(x)\subset k(C_a)\) of index three is unique. Indeed, if another rational subfield of index three were distinct, its compositum with \(k(x)\) would equal \(k(C_a)\): index three is prime. The two separable degree-three maps to \(\mathbb P^1\) would then, by Castelnuovo–Severi, force
\[
g(C_a)\le(3-1)(3-1)=4,
\]
contrary to \(g(C_a)=9\). Consequently any geometric automorphism preserves \(k(x)\) and normalizes its degree-three deck group. Since the cover is branched only at infinity, it induces an affine map
\[
x\longmapsto ux+v\qquad (u\in k^\times,\ v\in k).
\]
Normalizing the deck translations forces
\[
y\longmapsto\epsilon y+h(x),\qquad
\epsilon\in\mathbb F_3^\times=\{1,-1\},\quad h\in k(x),
\]
and therefore
\[
(ux+v)^{10}+a(ux+v)^8+(ux+v)^7
-\epsilon(x^{10}+ax^8+x^7)=h(x)^3-h(x).\tag{1}
\]
The left side is a polynomial. Any finite pole of \(h\) would produce a pole on the right, hence \(h\in k[x]\). A nonconstant \(h\) has degree at most three, as its coboundary has degree three times its degree. Thus the right side of (1) has no terms of degrees four, five, seven, eight or ten.

If \(a\neq0\), comparing the degree-ten and degree-eight coefficients of (1) (using \(\binom{10}{2}\equiv0\pmod3\)) yields
\[
u^{10}=\epsilon,\qquad au^8=\epsilon a,
\]
so \(u^2=1\) and \(\epsilon=1\). The degree-five coefficient on the left is \(2a u^5v^3\) (since \(\binom{10}{5}\equiv\binom72\equiv0\pmod3\)), so \(v=0\). The degree-seven coefficient then gives \(u^7=1\); together with \(u^2=1\), this forces \(u=1\).

If \(a=0\), comparison at degrees ten and seven gives \(u^{10}=\epsilon=u^7\) (because \(\binom{10}{3}\equiv0\pmod3\)), hence \(u^3=1\). In characteristic three this means \(u=1\) and \(\epsilon=1\). The degree-four coefficient is \(2v^3\) (since \(\binom{10}{6}\equiv0\pmod3\)), so \(v=0\).

In both cases (1) reduces to \(h^3-h=0\), which means \(h\in\mathbb F_3\). The three resulting deck translations are indeed automorphisms; there are no others.

**Holomorphic basis and Cartier.** The pole orders above show that the following nine forms are regular, with pairwise distinct orders at infinity:
\[
\mathcal B=(dx,x\,dx,x^2dx,x^3dx,x^4dx,x^5dx,
 y\,dx,xy\,dx,x^2y\,dx).
\]
There are nine, so \(\mathcal B\) is a basis of \(H^0(C_a,\Omega^1)\). In characteristic three, the semilinear Cartier operator \(\mathcal C\) satisfies
\[
\mathcal C(x^m dx)=\begin{cases}x^{(m-2)/3}dx,&m\equiv2\pmod3,\\0,&m\not\equiv2\pmod3,\end{cases}
\]
and \(\mathcal C(f^3\omega)=f\mathcal C(\omega)\). Using \(y=y^3-(x^{10}+a x^8+x^7)\), the complete nonzero images on \(\mathcal B\) are
\[
\begin{aligned}
\mathcal C(x^2dx)&=dx, &\mathcal C(x^5dx)&=x\,dx,\\
\mathcal C(y\,dx)&=-a^{1/3}x^2dx,
 &\mathcal C(xy\,dx)&=-(x^3+x^2)dx,\\
\mathcal C(x^2y\,dx)&=y\,dx.
\end{aligned}
\]
The other four displayed basis forms have zero image. The vectors \(dx\), \(x\,dx\), \((x^3+x^2)dx\) and \(y\,dx\) are independent. When \(a\neq0\), \(\mathcal C(y\,dx)\) adds the fifth independent vector \(x^2dx\); when \(a=0\), it vanishes. Thus \(\operatorname{rank}\mathcal C=4\) at zero and \(5\) elsewhere, giving \(a(C_a)=9-\operatorname{rank}\mathcal C\). Since the coefficient \(a^{1/3}\) vanishes exactly at \(a=0\), the rank-drop support is a single reduced parameter point (the Cartier rank condition is defined by the nonzero parameter \(a\); no multiplicity statement is made about a chosen Frobenius-twisted determinant scheme).

## Verification

The self-contained standard-library script `verify.py` checks the nine distinct pole orders, all Cartier images and their exact ranks over \(\mathbb F_3\) for \(a=0,1,2\). It also independently enumerates all affine automorphism lifts defined over \(\mathbb F_3\) and checks the key characteristic-three binomial coefficients. Running `python3 verify.py` prints `VERIFY_OK`. The proof above applies to every \(a\) over the algebraic closure; finite-field enumeration alone is **not** used to exclude automorphisms over extension fields or to infer the universal Cartier-rank formula.

## Relationship to prior work

Tafazolian and Kazemifard, *Artin-Schreier curves of prescribed p-rank without extra automorphisms* (first submitted 9 October 2026), prove the admissible genus/\(p\)-rank ranges for minimal full automorphism group and explicitly ask in Question 7.5 which finer invariants, including the \(a\)-number, can occur under that constraint. Their one-pole construction at degree ten uses a different polynomial pattern and does not supply this parameter-dependent Cartier-rank formula. The present calculation gives two \(a\)-numbers in one fixed genus/\(p\)-rank stratum while preserving minimal automorphisms.

Farnell and Pries, *Families of Artin–Schreier curves with Cartier–Manin matrix of constant rank*, establish coefficient-independent \(a\)-numbers under the congruence \(p\equiv1\pmod L\), where \(L\) is the least common multiple of the pole orders. Here \(p=3\), \(L=10\), so their constancy hypothesis does not hold. Pries and Zhu's general \(p\)-rank stratification and the standard Cartier-basis formula are prior methods, not claimed as new.

## Limitations

The result supplies two realized \(a\)-numbers for the particular genus-nine, characteristic-three, \(p\)-rank-zero locus; it does **not** classify all attainable \(a\)-numbers in that locus, determine Newton polygons or Ekedahl–Oort types, or prove any general prescription theorem in arbitrary genus. The nonzero parameters are not claimed pairwise nonisomorphic. Historical priority beyond the inspected sources remains provisional; an earlier obscure exact formula under a coordinate transformation could overlap the calculation. No independent mathematical audit has been performed.

## References

1. S. Tafazolian and A. Kazemifard, *Artin-Schreier curves of prescribed p-rank without extra automorphisms*, arXiv:2610.13279v1 (2026-10-09), particularly Sections 1, 3, 7, Proposition 3.4 and Question 7.5. https://arxiv.org/abs/2610.13279
2. S. Farnell and R. Pries, *Families of Artin–Schreier curves with Cartier–Manin matrix of constant rank*, Linear Algebra and its Applications **439** (2013), 2158–2166, Theorem 1.1 and Section 3; arXiv:1202.4183. https://arxiv.org/abs/1202.4183
3. R. Pries and H. J. Zhu, *The p-rank stratification of Artin–Schreier curves*, Annales de l'Institut Fourier **62** (2012), 707–726. https://doi.org/10.5802/aif.2692
4. J. Duque-Rosero, H. Goodson, E. Lorenzo García, B. Malmskog and R. Scheidler, *On invariants of Artin–Schreier curves*, arXiv:2401.08843 (2024). https://arxiv.org/abs/2401.08843
