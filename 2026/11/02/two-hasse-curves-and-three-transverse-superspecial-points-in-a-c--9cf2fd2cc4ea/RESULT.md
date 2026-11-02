# Two Hasse curves and three transverse superspecial points in a characteristic-seven bielliptic family

## Finding
Let \(k=\overline{\mathbb F}_7\), put
\[
H_a=a^3-ab+3,\qquad H_b=b^3-ab+3,
\]
and consider the coefficient-marked genus-two curves
\[
C_{a,b}:y^2=x^6+a x^4+b x^2+1
\]
over the smooth parameter space \(U=\{\Delta(a,b)\ne0\}\subset\mathbb A_k^2\), where
\[
\Delta=a^2b^2+3a^3+3b^3+4ab+1.
\]
Their geometric \(7\)-rank and \(a\)-number are exactly
\[
f_7(C_{a,b})={\bf1}_{H_a\ne0}+{\bf1}_{H_b\ne0},\qquad
a(C_{a,b})=2-f_7(C_{a,b}).
\]
The two reduced nonordinary Hasse components \(V(H_a)\cap U\) and \(V(H_b)\cap U\) are smooth geometrically irreducible curves, each isomorphic to \(\mathbb G_m\) punctured at three points. Their intersection in \(U\) is exactly the reduced transverse three-point scheme
\[
\{(a,b)=(2,2),(1,4),(4,1)\}.
\]
The full affine Hasse intersection has three additional, nonreduced, length-two points \((3,3),(5,6),(6,5)\), all outside \(U\). Thus its scheme-theoretic length is nine.

For every integer \(r\ge1\), writing \(q=7^r\), the numbers of **ordered coefficient pairs** \((a,b)\in U(\mathbb F_q)\) of \(7\)-rank zero, one, and two respectively are
\[
\boxed{N_0=3,\quad N_1=2q-14,\quad N_2=q^2-3q+12.}
\]
These are coefficient-marked counts, not counts of curve-isomorphism classes.

## Assumptions and scope
The base field has characteristic seven; the pair \((a,b)\) may lie in any extension of \(\mathbb F_7\). The displayed sextic has distinct roots exactly when the cubic \(t^3+a t^2+b t+1\) has distinct roots, because its constant term is nonzero and the characteristic is odd. The characteristic-seven discriminant of that cubic is \(\Delta\). Every fiber over \(U\) therefore has genus two. The \(7\)-rank is the dimension of the geometric \(7\)-torsion group of the Jacobian over \(\mathbb F_7\); the \(a\)-number is the dimension of its kernel under Cartier on regular differentials.

## Proof
**Cartier calculation.** Put \(t=x^2\) and \(g(t)=1+bt+at^2+t^3\). In characteristic seven the Cartier–Manin matrix on the basis \(\{dx/y,x\,dx/y\}\) is built from the coefficients of \(x^{7i-j}\) in \(g(x^2)^3\), for \(1\le i,j\le2\). The off-diagonal indices are odd, hence vanish. The diagonal indices are six and twelve, and direct multinomial expansion gives
\[
[t^3]g(t)^3=b^3+6ab+3=H_b,\qquad
[t^6]g(t)^3=a^3+6ab+3=H_a.
\]
The Cartier operator itself takes the inverse-Frobenius roots of these coefficients, but its two diagonal coordinates never mix under iteration; its stable rank is precisely the number of nonzero diagonal entries. Its ordinary rank is the same. This proves both displayed invariant formulas, including geometric coefficients not fixed by Frobenius.

**Hasse components.** The equation \(H_a=0\) forces \(a\ne0\) and is the graph \(b=(a^3+3)/a\), giving an isomorphism with \(\mathbb G_m\). Similarly \(H_b=0\) forces \(b\ne0\) and is its graph with the coordinates exchanged. They are smooth and geometrically irreducible. Substituting into the discriminant yields the identity in characteristic seven
\[
\left.\Delta\right|_{H_a=0}=-3\frac{(a^3+1)^3}{a^3}.
\]
There are exactly three nonzero solutions of \(a^3=-1\), so each Hasse component loses three geometric points upon restricting to \(U\). Those excluded points are rational over \(\mathbb F_7\).

**Complete intersection and transversality.** Subtraction gives \(H_a-H_b=a^3-b^3\). Since the three distinct cube roots of unity are \(1,2,4\) in characteristic seven, every common point lies on a line \(a=\zeta b\), with \(\zeta\in\{1,2,4\}\). On these lines the remaining equation factors as
\[
\begin{array}{ll}
\zeta=1:&(b-2)(b-3)^2,\\
\zeta=2:&(b-4)(b-6)^2,\\
\zeta=4:&(b-1)(b-5)^2.
\end{array}
\]
The corresponding simple roots give \((a,b)=(2,2),(1,4),(4,1)\), each having \(\Delta\ne0\) and nonzero Jacobian determinant for \((H_a,H_b)\). The repeated roots give \((3,3),(5,6),(6,5)\), each with \(\Delta=0\). The lines do not meet at a point of the Hasse intersection because \(H_a(0,0)=3\). Hence the total intersection scheme has three simple points and three distinct local length-two points, for length nine, and the reduced nonordinary divisor on \(U\) has normal crossings at its three intersections.

**Point counts over all finite extensions.** For any \(q=7^r\), a cubic over \(\mathbb F_q\) is nonseparable exactly when it has a repeated root \(s\in\mathbb F_q^*\). Writing \(t^3+a t^2+b t+1=(t-s)^2(t-u)\) and comparing coefficients and constant terms gives the unique parameter pair
\[
a=s^{-2}-2s,\qquad b=s^2-2s^{-1}.
\]
Different nonzero repeated roots cannot produce the same cubic; consequently there are exactly \(q-1\) singular coefficient pairs and \(q^2-q+1\) smooth pairs. Each Hasse component has exactly \(q-1\) rational points and loses precisely three to the discriminant, giving \(q-4\) smooth points. Their intersection on \(U\) has precisely three rational points. Inclusion–exclusion thus gives \(N_0=3\), \(N_1=2(q-4)-6=2q-14\), and \(N_2=(q^2-q+1)-N_0-N_1=q^2-3q+12\).

## Verification
The standalone `verify_symbolic.py` checks the two coefficients of \(g^3\), the discriminant substitution, all three cubic intersection factorizations, the smooth/singular classification of the six support points, and the three transverse Jacobian determinants using exact characteristic-seven polynomial arithmetic. It prints `GENUS2_CHAR7_EXACT_CARTIER_HASSE_SNC_INTERSECTION_OK`.

An independent `verify_fields.py` constructs \(\mathbb F_{49}=\mathbb F_7[w]/(w^2+1)\) without external algebra packages, recomputes the relevant sextic-power coefficients by convolution rather than using the displayed closed formulas, and enumerates both \(\mathbb F_7\) and \(\mathbb F_{49}\). It independently matches the singular set to the repeated-root parametrization. It reports counts \((N_0,N_1,N_2;N_{\mathrm{sing}})=(3,0,40;6)\) and \((3,84,2266;48)\) respectively. These enumerations corroborate, but do not replace, the geometric proof or the argument for every \(r\).

Reproduction: run `python verify_symbolic.py` and `python verify_fields.py` from the directory containing the scripts; `sympy` is required only for the first program.

## Relationship to prior work
Zobernig studies \(p\)-rank strata of the full genus-two moduli space in small characteristics, giving general Cartier methods and global moduli counts. Pieper constructs supersingular genus-two curves by methods not confined to this coefficient family. Chang–Dragutinović–Groen–Lin–Pacheco-Tallaj–Singhal study dimensions and existence of \(p\)-rank strata for double covers of a fixed elliptic curve; their general existence and dimension results do not imply the present explicit **varying-quotient coefficient-space scheme** and uniform marked counts. The standard characteristic-seven Cartier formula itself is not new. The asserted contribution is the two Hasse components, their transverse smooth intersection versus doubled boundary points, and the exact marked counts in every finite extension.

## Limitations
These counts distinguish ordered coefficient pairs even when the resulting curves are isomorphic. The two Hasse divisors extend to singular fibers at their double intersection points, but no moduli-theoretic compactification or stable-reduction classification is asserted. There may be earlier, unindexed equivalent coefficient calculations. The proof is self-contained apart from the standard Cartier–Manin construction and Riemann–Hurwitz genus formula. Independent external mathematical validation has not been performed.

## References
- Lukas Zobernig, *Genus 2 Curves in Small Characteristic*, arXiv:2111.07270, first posted 2021-11-14, https://arxiv.org/abs/2111.07270 .
- Andreas Pieper, *Constructing all Genus 2 Curves with Supersingular Jacobian*, arXiv:2105.13752, first posted 2021-05-28, https://arxiv.org/abs/2105.13752 .
- Kevin Chang, Dušan Dragutinović, Steven Groen, Yuxin Lin, Natalia Pacheco-Tallaj and Deepesh Singhal, *The p-rank stratification of the moduli space of double covers of a fixed elliptic curve*, arXiv:2502.09540, https://arxiv.org/html/2502.09540v1 .
