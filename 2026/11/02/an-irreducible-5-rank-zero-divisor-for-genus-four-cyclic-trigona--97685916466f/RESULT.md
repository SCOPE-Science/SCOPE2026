# An irreducible \(5\)-rank-zero divisor for genus-four cyclic trigonal quintics

## Finding

Let \(k=\overline{\mathbb F}_5\) and let \(U\subset\mathbb A^5_k\) be the locus where
\[
 F(x)=x^5+c_4x^4+c_3x^3+c_2x^2+c_1x+c_0
\]
has five distinct roots. Let \(C_F\) be the smooth projective curve \(y^3=F(x)\), of genus four. Set
\[
\begin{aligned}
 V_0&=3c_4c_0^2+c_3c_1c_0+3c_2^2c_0+3c_2c_1^2,\\
 V_1&=c_4c_0+c_3c_1+3c_2^2+3c_4^2c_1+c_4c_3c_2+c_3^3,\\
 V_2&=3c_4,\\
 \mathcal P&=c_4^5V_0+c_3^5V_1+c_2^5V_2.
\end{aligned}
\]
All coefficient identities are in characteristic five. Then, for **every geometric point** of \(U\),
\[
\boxed{f_5(C_F)=\begin{cases}2&\mathcal P\ne0,\\0&\mathcal P=0,\end{cases}}
\]
and
\[
\boxed{a(C_F)=\begin{cases}4&c_4=c_3=c_2=0,\\2&\text{otherwise}.\end{cases}}
\]
The polynomial \(\mathcal P\in k[c_0,c_1,c_2,c_3,c_4]\) is **absolutely irreducible**, of total degree eight, and its zero set meets \(U\) in a nonempty, geometrically irreducible, generically smooth hypersurface. Its general member has \(5\)-rank zero and \(a\)-number two. In particular, the ranks \(1,3,4\) never occur; nor do \(a\)-numbers \(0,1,3\). The smooth \(a\)-number-four locus consists exactly of the coefficient-marked equations \(y^3=x^5+c_1x+c_0\) with \(c_1\ne0\); these are all geometrically isomorphic to \(y^3=x^5+x\). This final superspecial isomorphism class is already known in the genus-four literature and is not claimed as new.

## Assumptions and scope

The field is algebraically closed of characteristic five, the quintic is monic and separable, and the curve is the smooth projective normalization of the displayed affine cyclic cover. The \(5\)-rank is the dimension of the stable Frobenius/Cartier image on first cohomology; the \(a\)-number is the dimension of the kernel of Cartier on regular one-forms. The claimed irreducibility is for the **coefficient polynomial** \(\mathcal P\), not a claim of irreducibility or optimality for its image in an unmarked moduli space. No Newton polygons, complete Ekedahl--Oort types, zeta functions, or curves outside this cyclic-cover family are classified.

## Proof

**1. Holomorphic differentials.** For separable degree-five \(F\), the cyclic degree-three map \(C_F\to\mathbb P^1\) is totally ramified at the five finite branch points and at infinity, giving \(2g-2=3(-2)+6(3-1)=6\), hence \(g=4\). At infinity the valuations of \(x,y,dx\) are respectively \(-3,-5,-4\). At finite ramification points \(dx/y\) and \(dx/y^2\) are regular. Therefore
\[
\omega_0=dx/y,\quad \omega_1=dx/y^2,\quad
\omega_2=x\,dx/y^2,\quad \omega_3=x^2\,dx/y^2
\]
form a basis of \(H^0(C_F,\Omega^1)\).

**2. Cartier map.** The identity \(\mathscr C(g^5\eta)=g\mathscr C(\eta)\) and \(y^3=F\) imply
\[
\frac{dx}{y}=\frac{F^3\,dx}{(y^2)^5},\qquad
\frac{x^i dx}{y^2}=\frac{x^iF\,dx}{y^5}\quad(i=0,1,2).
\]
Using \(\mathscr C(x^{5j+4}dx)=x^jdx\) (and zero on other monomial exponents), with coefficients raised to their unique fifth roots in \(k\), gives
\[
\mathscr C(\omega_0)=V_0^{1/5}\omega_1+V_1^{1/5}\omega_2+V_2^{1/5}\omega_3,
\qquad
\mathscr C(\omega_{i+1})=c_{4-i}^{1/5}\omega_0.
\]
Here \(V_j=[x^{5j+4}]F(x)^3\); direct expansion yields exactly the three displayed polynomials. Thus Cartier has off-diagonal blocks of sizes one-by-three and three-by-one, each of rank at most one. Write \(W=(c_4,c_3,c_2)\) and \(V=(V_0,V_1,V_2)\).

**3. Stable semilinear rank.** Cartier is \(5^{-1}\)-semilinear, not an ordinary linear matrix over a general coefficient field. The two-step scalar on \(k\omega_0\) is
\[
 s=\sum_{i=0}^2 V_i^{1/25}W_i^{1/5},\qquad s^{25}=\sum_{i=0}^2V_iW_i^5=\mathcal P.
\]
If \(s\ne0\), the stable image consists of one direction in each of the two character spaces and has dimension two. If \(s=0\), the Cartier map is nilpotent (indeed its fourth iterate is zero). This proves the \(5\)-rank formula for all geometric coefficients.

**4. Exact \(a\)-number.** The first Cartier rank equals \(\mathbf1_{V\ne0}+\mathbf1_{W\ne0}\). If \(W=0\), then \(V=0\) directly, and \(F=x^5+c_1x+c_0\) is separable exactly when \(c_1\ne0\). Conversely, suppose \(V=0\). Since \(V_2=3c_4\), one has \(c_4=0\). If \(c_3=0\), the equation \(V_1=3c_2^2=0\) gives \(c_2=0\), so \(W=0\). If \(c_3=A\ne0\), put \(c_2=B\). The equations \(V_1=V_0=0\) force
\[
 c_1=2B^2/A-A^2,\qquad c_0=3Bc_1^2/A^3.
\]
Substitution \(x=z+3B/A\) transforms \(F\) into
\[
 z^5+Az^3-A^2z=z(z^2-2A)^2,
\]
which is inseparable, contradicting \(F\in U\). Thus on \(U\), either \(V=W=0\) or both are nonzero. The first case has Cartier rank zero and \(a=4\), the second rank two and \(a=2\).

**5. Absolute irreducibility of the rank-drop polynomial.** Put \(u=c_4,v=c_3,w=c_2,t=c_1,z=c_0\). Regard \(\mathcal P\) as a polynomial of degree two in \(z\) over \(R=k[u,v,w,t]\). Its leading coefficient is \(3u^6\); its linear coefficient is \(u^5(vt+3w^2)+uv^5\), and its constant coefficient is not divisible by \(u\), because reduction modulo \(u\) gives \(v^5(vt+3w^2+v^3)\). Thus the three coefficients are primitive in the UFD \(R\). If this quadratic were reducible over \(\operatorname{Frac}(R)\), its discriminant would be a square in \(\operatorname{Frac}(R)\). As \(R\) is integrally closed, a polynomial square in its fraction field is the square of an element of \(R\). But specializing \((u,v,w)=(1,0,1)\) makes this discriminant
\[
 4t^2+3,
\]
which has two distinct roots over the algebraic closure and is not a square polynomial. Contradiction. By Gauss's lemma, \(\mathcal P\) is irreducible over \(k\). It has total degree eight because of the monomial \(v^8\).

**6. Smooth geometric nonemptiness.** The quintic \(x^5+x^3+x\) has discriminant \(4\in\mathbb F_5^\times\) and \(\mathcal P=2\), so the rank-two locus is nonempty. The quintic \(x^5+x^4+x^3+x\) has discriminant \(2\in\mathbb F_5^\times\), \(\mathcal P=0\), and \(\partial\mathcal P/\partial c_0=2\); hence the rank-zero hypersurface meets \(U\) in a smooth point. Since \(\mathcal P\) is irreducible, that intersection is a geometrically irreducible, generically smooth hypersurface. At this point \((c_4,c_3,c_2)=(1,1,0)\ne0\), so its general point has \(a=2\).

**7. The superspecial marked locus.** If \(c_4=c_3=c_2=0\) and \(c_1\ne0\), translate \(x\) by a root of \(T^5+c_1T+c_0\), then scale \(x\) by a fourth root of \(c_1\) and rescale \(y\) by a cube root of the resulting leading coefficient. This produces \(y^3=x^5+x\) over \(k\). Its Cartier operator is zero, agreeing with the established uniqueness of a superspecial genus-four geometric class in characteristic five.

## Verification

Run the standalone scripts, with Python 3 and no third-party dependencies:

```text
python3 verify_symbolic.py
python3 verify_universal.py
python3 verify_extension.py
```

The symbolic checker independently expands the coefficient identities as exact multivariate polynomials over the prime field, verifies the quadratic leading coefficient and its non-square discriminant specialization, and reports `EXACT_POLYNOMIAL_IDENTITIES_AND_NONSQUARE_DISCRIMINANT_OK`. The prime-field checker exhausts all \(5^5=3125\) coefficient tuples over \(\mathbb F_5\), tests squarefreeness by polynomial gcd, expands \(F^3\), checks every coefficient identity, computes the first Cartier rank and stable rank, and checks the formula. It reports 625 singular tuples, and, among 2500 smooth tuples, 1800 with \((f_5,a)=(2,2)\), 680 with \((0,2)\), and 20 with \((0,4)\). The extension-field checker independently implements arithmetic in \(\mathbb F_{25}\) and tests 5764 smooth pseudorandom coefficient tuples; it explicitly iterates the \(5^{-1}\)-semilinear Cartier operator rather than treating a coefficient matrix as linear. These finite-field experiments corroborate, but **do not replace**, the algebraically closed-field proof, the irreducibility argument, or the factorization in Step 4.

## Relationship to prior work

Kudo and Harashita's 2017 study (*Enumerating superspecial curves of genus 4 over prime fields*, arXiv:1702.05313, Theorem A and Section 4) enumerates superspecial isomorphism classes in small characteristic. Its characteristic-five uniqueness is used as context, not claimed as new. Their theorem does not state the full \(5\)-rank-zero coefficient divisor or its absolute irreducibility. The full-text Section 2.2 of Asif, Fité and Pentland (arXiv:2010.07247) develops Cartier methods for cyclic covers, but its main Picard curves have a degree-four branch polynomial and genus three; it does not imply the displayed degree-eight equation or its irreducibility for degree-five branch polynomials. General semilinear Cartier methods are standard and are not claimed as new.

Sohn's *The \(a\)-number of superelliptic curves of genus four* (2025, DOI:10.23091/japm.2025.059) is a directly relevant priority risk. Its accessible abstract establishes its subject as \(a\)-numbers; its full eight-page PDF could not be inspected. Consequently no novelty is asserted for a stand-alone genus-four \(a\)-number formula, and a possibility of overlapping broader conclusions remains. The assessed contribution is the **explicit universal stable \(5\)-rank-zero equation and geometric irreducibility** of its divisor, together with its rigorously derived strata. No exact or stronger covering result was identified in the inspected records or accessible primary texts.

## Limitations

This is a complete classification of the two named invariants only for separable monic quintic cyclic covers in characteristic five. The polynomial \(\mathcal P\) is coordinate-dependent although its vanishing is invariant under equivalence of the associated covers. The geometric irreducibility is in the marked coefficient space; quotient-moduli irreducibility and the Newton polygon are not addressed. No independent mathematical audit has been performed. The inaccessible 2025 Sohn full text and unindexed prior computations create residual priority risk.

## References

1. M. Kudo and S. Harashita, *Enumerating superspecial curves of genus 4 over prime fields*, arXiv:1702.05313 (first submitted February 17, 2017), especially Theorem A, Sections 2 and 4. https://arxiv.org/abs/1702.05313
2. S. Asif, F. Fité and D. Pentland, *Computing L-Polynomials of Picard curves from Cartier-Manin matrices*, arXiv:2010.07247 (first submitted October 14, 2020), Sections 1--2. https://arxiv.org/html/2010.07247v3
3. G. Sohn, *The \(a\)-number of superelliptic curves of genus four*, Journal of Applied and Pure Mathematics 7 (2025), 59--66. DOI:10.23091/japm.2025.059 (relevant source with inaccessible full text).
