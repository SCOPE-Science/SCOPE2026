# Cartier rigidity and the supersingular hyperplane of characteristic-two Picard quartics

## Finding
Let \(k\) be an algebraically closed field of characteristic \(2\), and let \(C_{d,a,b,c}\) be the smooth projective model of
\[
y^3=f(x)=x^4+d x^3+a x^2+b x+c,
\]
where \(f\) is separable. Every such curve has genus \(3\), and its Jacobian has \(a\)-number exactly \(1\). There are precisely two possibilities:

* If \(d=0\) (hence \(b\ne0\)), the Jacobian has \(2\)-rank \(0\), is supersingular but not superspecial, and has six Newton slopes all equal to \(1/2\).
* If \(d\ne0\), the Jacobian has \(2\)-rank \(2\), with Newton slopes \(0,0,1/2,1/2,1,1\).

For every \(q=2^m\), among **smooth monic coordinate-marked quartics** with coefficients in \(\mathbb F_q\), the numbers in the two strata are, respectively,
\[
q^2(q-1)\qquad\hbox{and}\qquad q^2(q-1)^2.
\]
These are counts of polynomial presentations, not of abstract isomorphism classes. In particular, no such smooth plane quartic is ordinary or superspecial. The supersingular locus is the open part \(b\ne0\) of the coefficient hyperplane \(d=0\) in the smooth parameter space.

## Assumptions and scope
The characteristic is exactly \(2\), the quartic is monic, the base field is perfect for the Cartier formulas, and \(f\) is separable. The affine equation defines a smooth plane quartic after homogenization \(y^3z=f_4(x,z)\); its unique point at infinity is rational. The projective genus is \(3\). All Newton polygons, \(a\)-numbers and \(2\)-ranks are geometric invariants. The finite-field formulas count coefficient tuples \((d,a,b,c)\) with chosen variables and do not quotient by transformations of coordinates.

## Proof
**Differentials and Cartier.** At every finite branch point of \(f\), the local parameter \(y\) has order one and \(dx\) has order two. At infinity, \(x\) and \(y\) have pole orders \(3\) and \(4\) and \(dx\) has order \(-4\). Consequently
\[
\omega_1=\frac{dx}{y},\quad \omega_2=\frac{dx}{y^2},\quad \omega_3=\frac{x\,dx}{y^2}
\]
are regular and independent. As the genus is three, they form a basis of \(H^0(C,\Omega^1_C)\). Cartier's rules in characteristic two give \(\mathcal C(h^2\eta)=h\mathcal C(\eta)\), \(\mathcal C(dx)=0\) and \(\mathcal C(x\,dx)=dx\). Moreover, \(f\,dx\) has odd-power terms only at \(b x\) and \(d x^3\), so \(\mathcal C(f\,dx)=(\sqrt b+\sqrt d\,x)dx\). Rewriting \(dx/y=(y/f)^2f\,dx\), one obtains the **exact semilinear Cartier operator**
\[
\mathcal C(\omega_1)=\sqrt b\,\omega_2+\sqrt d\,\omega_3,\quad
\mathcal C(\omega_2)=0,\quad
\mathcal C(\omega_3)=\omega_1.
\]
Its rank is two whenever \((b,d)\ne(0,0)\), as is forced by separability. Therefore \(a(C)=\dim\ker\mathcal C=1\), regardless of the other coefficients.

**Stable Cartier rank.** For \(d=0\), separability requires \(b\ne0\), and the Cartier operator forms the length-three nilpotent chain \(\omega_3\mapsto\omega_1\mapsto\sqrt b\,\omega_2\mapsto0\). Its stable rank, hence the Jacobian's \(2\)-rank, is zero. For \(d\ne0\), the two-dimensional space spanned by \(\omega_1\) and \(\sqrt b\,\omega_2+\sqrt d\,\omega_3\) is Cartier stable, with bijective semilinear Cartier action. Thus the stable rank and \(2\)-rank are two. The remaining two slopes of a polarized three-dimensional abelian variety with \(2\)-rank two are necessarily \(1/2,1/2\), by symmetry, so its Newton slopes are \(0,0,1/2,1/2,1,1\).

**The supersingular stratum.** Set \(d=0\), \(b\ne0\), and \(L(x)=x^4+a x^2+b x\). This is a separable additive polynomial, so its four geometric roots form a translation group \(A\cong(\mathbb Z/2\mathbb Z)^2\) acting faithfully on \(C\) via \(x\mapsto x+t\), fixing \(y\). The full quotient is \(C/A\cong\mathbb P^1_y\), because \(L(x)=y^3-c\). For a nonzero root \(t\) of \(L\), the involution \(x\mapsto x+t\) has invariant \(z=x^2+t x\). Using \(t^3+a t+b=0\), its quotient has equation
\[
E_t:\quad y^3=z^2+(a+t^2)z+c,
\qquad a+t^2=b/t\ne0.
\]
Writing \(X=y\) and \(Y=z\) gives a nonsingular elliptic Weierstrass equation \(Y^2+(b/t)Y=X^3+c\), with \(j(E_t)=0\) in characteristic two. Each of the three nontrivial order-two quotients is therefore supersingular elliptic. For any odd auxiliary prime \(\ell\), the \(A\)-representation on \(H^1_{\acute et}(C,\mathbb Q_\ell)\) decomposes into the three distinct nontrivial characters, each of dimension two: the trivial character contributes nothing since the full quotient has genus zero, while the invariant part for each order-two subgroup comes from its elliptic quotient. Thus the sum of the three quotient pullbacks induces an isogeny over \(\bar k\),
\[
\operatorname{Jac}(C)\sim E_{t_1}\times E_{t_2}\times E_{t_3},
\]
with \(t_1,t_2,t_3\) the nonzero roots of \(L\). All six Newton slopes are \(1/2\). Its independently established \(a\)-number is one, not three, so it is not superspecial. This isogeny statement is geometric; the nonzero roots need not lie in the original finite field.

**Exact parameter counts.** In characteristic two \(f'(x)=d x^2+b\). If \(d=0\), separability is equivalent to \(b\ne0\), giving \(q^2(q-1)\) choices of \((d,a,b,c)\). If \(d\ne0\), the derivative has the single root \(s=\sqrt{b/d}\in\mathbb F_q\). The polynomial is separable iff \(f(s)\ne0\). For each \((d,a,b)\), exactly one \(c\) violates this, yielding \(q^2(q-1)^2\) smooth choices. The total is \(q^3(q-1)\), with no missing cases.

## Verification
The accompanying standard-library-only Python program `verify.py` implements polynomial-basis arithmetic in the fields \(\mathbb F_2\), \(\mathbb F_4\), \(\mathbb F_8\), and \(\mathbb F_{16}\). It exhaustively checks the smoothness count over all coefficient tuples and the iterated semilinear Cartier ranks. The observed triples (total, supersingular, rank-two) are respectively \((8,4,4)\), \((192,48,144)\), \((3584,448,3136)\), and \((61440,3840,57600)\). It also checks illustrative point counts over the first two fields. The final output is `VERIFY_OK`. These finite tests support, but do not substitute for, the symbolic proof above.

## Relationship to prior work
The monic separable quartic form of Picard curves is standard; it is set out by Bouw–Koutsianas–Sijsling–Wewers (2019). Nart–Ritzenthaler (2003) already provide a far broader classification of characteristic-two plane quartics by \(2\)-rank and Newton polygon, including the existing supersingular and rank-two Newton polygon types; **neither shape is claimed new**. Their paper does not present the displayed explicit coefficient-aligned Picard criterion, uniform \(a\)-number, or the counts of smooth marked quartic presentations. The general technique of decomposing genus-three Jacobians via involution quotients is also prior (Nart–Ritzenthaler 2009). Asif–Fité–Pentland (2020) compute Cartier–Manin matrices for Picard curves in good reductions at odd primes, a different characteristic. The specific claimed addition is the complete characteristic-two Picard-coefficient stratification, including uniform \(a\)-number one and exact finite-field presentation counts, not the general theory of genus-three Newton polygons.

## Limitations
No claim is made about every nonhyperelliptic genus-three curve, abstract Picard isomorphism-class counts, endomorphism rings, isomorphism of the three elliptic quotient factors, or finer Ekedahl–Oort types. The curves with \(d\ne0\) need not have the same zeta function. The finite-field checker tests degrees at most four, whereas the algebraic proof covers every perfect field of characteristic two after geometric extension. Prior general quartic classifications create genuine potential overlap by implication; an unindexed source might already give these specific coefficient and \(a\)-number conclusions. No independent audit has been performed.

## References
1. Bouw, Koutsianas, Sijsling and Wewers, *Conductor and discriminant of Picard curves*, arXiv:1902.09624 (2019), https://arxiv.org/html/1902.09624v1.
2. Nart and Ritzenthaler, *Non-hyperelliptic curves of genus three over finite fields of characteristic two*, arXiv:math/0312366 (2003), https://arxiv.org/abs/math/0312366.
3. Nart and Ritzenthaler, *Genus 3 curves with many involutions and application to maximal curves in characteristic 2*, arXiv:0905.0546 (2009), https://arxiv.org/abs/0905.0546.
4. Asif, Fité and Pentland, *Computing L-polynomials of Picard curves from Cartier–Manin matrices*, arXiv:2010.07247 (2020), https://arxiv.org/abs/2010.07247.
