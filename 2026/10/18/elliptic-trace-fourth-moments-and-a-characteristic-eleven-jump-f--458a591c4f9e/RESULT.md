# Elliptic-trace fourth moments and a characteristic-eleven jump for the sixth-power graph

## Finding
Let \(q=p^r\), where \(p\ge 7\) is prime and \(r\ge1\). Over \(\mathbb F_q\), put
\[
C_6=\{(t,t^6):t\in\mathbb F_q\},\qquad
\mathcal A_6(q)=\#\{(x,y,u,v)\in\mathbb F_q^4:x+y=u+v,\ x^6+y^6=u^6+v^6\}.
\]
Write \(\chi\) for the quadratic character, with \(\chi(0)=0\), and define
\[
g=\gcd(6,q-1),\quad \delta=\chi(-3),\quad
B_q=2\#\{z\in\mathbb F_q:z^4+10z^2+5=0\}.
\]
All integer coefficients in polynomials below mean their images in \(\mathbb F_q\).

For \(p\ne11\), let \(a_q,b_q\) be the Frobenius traces of the two elliptic curves
\[
E_1:Y^2=X(X^2+10X-55),\qquad
E_2:Y^2=(X^2+15X+15)(X^2+20X+20),
\]
where the second equation denotes its nonsingular projective genus-one completion. Thus \(a_q=q+1-\#E_1(\mathbb F_q)\) and \(b_q=q+1-\#E_2(\mathbb F_q)\). Both curves are nonsingular in the stated characteristics. Then the **exact additive energy** is
\[
\boxed{\mathcal A_6(q)=1+(q-1)\bigl[3q-2+g-B_q-2\delta-\delta(2a_q+b_q)\bigr],\qquad p\ne11.}
\]
In particular, Hasse's elliptic-curve bound gives the completely explicit estimate
\[
\left|\mathcal A_6(q)-\{1+(q-1)(3q-2+g-B_q-2\delta)\}\right|\le6(q-1)\sqrt q.
\]

**Characteristic eleven is exceptional:** for every \(q=11^r\), with \(\varepsilon=(-1)^r\),
\[
\boxed{\mathcal A_6(q)=1+(q-1)\bigl[4q-13+\gcd(6,q-1)-2\varepsilon\bigr].}
\]
Thus the leading asymptotic energy is \(3q^2+O(q^{3/2})\) in every fixed characteristic \(p\ge7\) other than eleven, whereas it is \(4q^2+O(q)\) in characteristic eleven. These are exact identities, not asymptotic extrapolations from a finite table.

For a nontrivial additive character \(\psi\), define the normalized constant-input Fourier extension
\[
\mathcal E_q\mathbf1(\xi,\eta)=\frac1q\sum_{t\in\mathbb F_q}\psi(\xi t+\eta t^6).
\]
When frequency space has unnormalized counting measure,
\[
\boxed{\sum_{\xi,\eta\in\mathbb F_q}|\mathcal E_q\mathbf1(\xi,\eta)|^4=\frac{\mathcal A_6(q)}{q^2}.}
\]
This determines the **constant-input** fourth extension moment, not the sharp operator norm over all input functions.

## Assumptions and scope
The theorem holds for all finite fields of characteristic \(p\ge7\), including nonprime fields; no restriction on \(r\) or the choice of nontrivial additive character is imposed. Characteristics two, three and five are not covered because some factorizations and discriminants degenerate. For \(p\ne11\), the displayed curves have discriminants supported on the primes two, three, five and eleven; the characteristic-eleven case is handled independently rather than treated as a singular elliptic curve. The correction \(B_q\) is an exact, at-most-eight-point intersection count, not an unspecified error term.

## Proof
**1. Reduce each nonzero first-coordinate sum to a collision quartic.** For \(s=x+y\ne0\), write \(x=s(1+z)/2\) and \(y=s(1-z)/2\). The map \(z\mapsto(x,y)\) is bijective, and the sixth-power sum equals
\[
\frac{s^6}{32}(1+15z^2+15z^4+z^6).
\]
For another ordered pair with normalized parameter \(w\), equality of sixth-power sums is equivalent to
\[
(z^2-w^2)F(z,w)=0,\qquad
F(z,w)=z^4+z^2w^2+w^4+15(z^2+w^2)+15.
\]
There are \(2q-1\) ordered parameter pairs satisfying \(z^2=w^2\). Their overlap with \(F=0\) consists of \(2R\) ordered pairs, where \(R=\#\{z:z^4+10z^2+5=0\}\): indeed \(F(z,\pm z)=3(z^4+10z^2+5)\), and none of these roots is zero. Consequently, writing \(N_q=\#\{(z,w)\in\mathbb F_q^2:F(z,w)=0\}\), every nonzero value of \(s\) contributes exactly \(2q-1+N_q-B_q\) collisions.

**2. Count the zero-sum fiber.** For \(s=0\), the two ordered pairs are \((x,-x)\) and \((u,-u)\). Their sixth-power sums agree precisely when \(x^6=u^6\). The power map on \(\mathbb F_q^\times\) has kernel of cardinality \(g=\gcd(6,q-1)\), hence the zero-sum contribution is \(1+g(q-1)\). Summing over \(s\) yields the unconditional identity
\[
\mathcal A_6(q)=1+(q-1)[2q-1+N_q-B_q+g].\tag{1}
\]

**3. Elliptic character-sum decomposition away from eleven.** Put \(U=z^2\), \(V=w^2\). The equation \(F=0\) becomes
\[
U^2+UV+V^2+15(U+V)+15=0,\tag{2}
\]
and each choice of \(U,V\) has \((1+\chi(U))(1+\chi(V))\) lifts. Expand this weight into four terms. Setting \(A=U+V\), the discriminant for the quadratic with roots \(U,V\) is \(-3(A^2+20A+20)\). Since the latter monic quadratic has nonzero discriminant \(320\), the unweighted count is \(q-\delta\). Fixing \(U\) and solving (2) for \(V\), the quadratic discriminant is \(-3(U^2+10U-55)\); each of the two single-character terms equals
\[
\delta S_3,\qquad S_3=\sum_{U\in\mathbb F_q}\chi\bigl(U(U^2+10U-55)\bigr).
\]
Finally \(UV=A^2+15A+15\), so the double-character term is
\[
\sum_A\chi(A^2+15A+15)\bigl[1+\delta\chi(A^2+20A+20)\bigr]
=-1+\delta S_4,
\]
where
\[
S_4=\sum_{A\in\mathbb F_q}\chi\bigl[(A^2+15A+15)(A^2+20A+20)\bigr].
\]
Here the first sum is \(-1\) because its quadratic has discriminant \(165\ne0\) for \(p\ne11\). We used the standard elementary identity \(\sum_X\chi(X^2+cX+d)=-1\) for nonzero discriminant, obtained by counting \((X-Y)(X+Y)=c^2/4-d\ne0\).

Consequently
\[
N_q=q-1-\delta+\delta(2S_3+S_4).\tag{3}
\]
The cubic defining \(E_1\) has one rational point at infinity, giving \(S_3=-a_q\). The monic quartic defining \(E_2\) has two rational points at infinity on its smooth completion, giving \(S_4=-1-b_q\). Its quartic discriminant is \(33000000\), while the cubic discriminant is \(968000\); both are nonzero for the stated \(p\). Equation (3) therefore simplifies to
\[
N_q=q-1-2\delta-\delta(2a_q+b_q).\tag{4}
\]
Substitution in (1) proves the generic formula. The inequalities \(|a_q|,|b_q|\le2\sqrt q\) imply the claimed explicit error bound.

For geometric context, when \(p\ne11\), the projective closure of \(F=0\) is a smooth plane quartic of genus three. Its points at infinity number \(2(1+\delta)\), so (4) also gives its point count \(q+1-\delta(2a_q+b_q)\). This is a check on, not a replacement for, the direct energy calculation.

**4. The characteristic-eleven degeneration.** Modulo eleven the collision quartic factors exactly as
\[
F(z,w)=(z^2+zw+w^2+2)(z^2-zw+w^2+2).
\]
Each affine conic has \(q-\chi(-3)\) rational points. Their intersection consists of the four points with \(zw=0\) and \(z^2+w^2=-2\), since \(-2=9\) is a square in every extension of \(\mathbb F_{11}\). Thus \(N_q=2q-4-2\chi(-3)\). The quartic \(z^4+10z^2+5\) has the four roots \(\pm3,\pm5\) already over \(\mathbb F_{11}\), hence \(B_q=8\). Finally \(\chi(-3)=(-1)^r\); insert these values into (1) to obtain the exceptional formula. This exhibits the extra reducible-conic component responsible for the jump in the leading collision count.

**5. Fourier normalization.** Expand the fourth power of the constant-input extension operator. Orthogonality of the nontrivial additive character in the two independent frequency variables contributes \(q^2\) exactly when both additive collision equations hold, and zero otherwise. The factor \(q^{-4}\) from four copies of the normalized extension yields \(q^{-2}\mathcal A_6(q)\), as claimed.

## Verification
The bundled standalone program `verify_sextic.py` uses only Python's standard library. It implements prime and quadratic-extension field arithmetic directly, evaluates the two elliptic character sums, reconstructs every value of the collision quartic, and independently enumerates all ordered two-sum fibers of the sixth-power graph. It tests twelve prime fields and the extension fields of orders \(49\), \(121\), and \(169\), covering both the smooth and exceptional characteristic-eleven cases. It also checks the exceptional conic factorization pointwise and the Hasse bounds in all applicable cases. A successful run prints `VERIFY_OK fields=15 total_ordered_pairs=56031 exceptional_characteristic_11=2 elliptic_trace_checks=13 collision_energy=PASS`.

The finite tests do not establish the theorem for infinitely many fields; the preceding character-sum and conic proofs do. There is no claim of a globally sharp fourth-power extension constant.

## Relationship to prior work
Mockenhaupt and Tao established the finite-field restriction framework and the connection between even extension moments and additive representation counts. Their primary geometric examples concern paraboloids, cones and full moment curves; those statements do not provide the present two-coordinate sixth-power graph formula. Koh and Shen proved general \(L^2\)-to-\(L^4\) boundedness criteria for algebraic curves, including graphs of polynomials of sufficiently small degree relative to the characteristic, but not the exact sixth-power constant-input moment, the elliptic-trace decomposition, or the characteristic-eleven exceptional leading term. Their initial arXiv submission of March 22, 2010 is the chronological anchor of this investigation.

Howe, Leprevost and Poonen described general genus-three plane quartics with completely split Jacobians. Their structural genus-three framework is credited; it does not identify the sixth-power graph collision quartic or determine its additive energy. An accessible published calculation of the fourth-power graph's exact energy and a separate fifth-power graph two-sum census involve different collision polynomials, with respectively lower-degree character sums and different arithmetic strata. No conclusion of historical priority follows merely from these differences.

## Limitations
The energy concerns unit coefficients on the entire graph; it does not solve the full optimization of Fourier extension over arbitrary functions. Characteristics two, three and five are excluded. The elliptic curves and their Frobenius traces depend on the base field and need not have elementary closed numerical formulas uniformly in the characteristic. The correction \(B_q\) is explicit but varies arithmetically. The argument determines exact moments but not exact distributions of all individual nonzero Fourier coefficients. An older equivalent monomial-curve energy or Ciani-quartic computation cannot be categorically ruled out from the inspected sources.

## References
1. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234 (first submitted 2002), Duke Math. J. 121 (2004), 35–74. https://arxiv.org/abs/math/0204234
2. D. Koh and C.-Y. Shen, *Sharp extension theorems and Falconer distance problems for algebraic curves in two dimensional vector spaces over finite fields*, arXiv:1003.4240v1 (March 22, 2010). https://arxiv.org/abs/1003.4240
3. E. W. Howe, F. Leprevost and B. Poonen, *Large torsion subgroups of split Jacobians of curves of genus two or three*, arXiv:math/9809210 (1998), Forum Math. 12 (2000), 315–364. https://arxiv.org/abs/math/9809210
4. *Exact additive energy of the finite-field quartic graph*, publicly indexed mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-additive-energy-of-the-finite-field-quartic-graph--235f10989b3f
