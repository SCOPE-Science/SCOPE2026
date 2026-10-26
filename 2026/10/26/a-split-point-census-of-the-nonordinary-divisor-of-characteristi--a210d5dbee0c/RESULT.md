# A split-point census of the nonordinary divisor of characteristic-five Picard curves

## Finding
Let \(k\) be an algebraically closed field of characteristic \(5\). For every \((a,b,c)\in k^3\) with separable quartic \(f(x)=x^4+ax^2+bx+c\), let \(C_{a,b,c}\) be the smooth projective model of \(y^3=f(x)\). Write \(U\subset\mathbb A^3_k\) for this smooth parameter domain and \(J_{a,b,c}\) for the Jacobian. Define
\[
P(a,b,c)=c^2+a^2c+ab^2.
\]
Then \(C_{a,b,c}\) has genus \(3\), its Jacobian has \(a\)-number exactly \(1\), and its \(5\)-rank satisfies
\[
f_5(J_{a,b,c})=\begin{cases}0,&P(a,b,c)=0,\\2,&P(a,b,c)\ne0.\end{cases}
\]
In particular, rank \(1\) and rank \(3\) never occur in this marked family. The zero-rank locus \(V=U\cap\{P=0\}\) is a smooth geometrically irreducible divisor of \(U\). Its two natural locally closed pieces have explicit isomorphisms
\[
V\cap\{a=0\}\cong\mathbb G_m,\qquad
V\cap\{a\ne0\}\cong\mathbb G_m\times(\mathbb A^1\setminus\{0,-1\}).
\]
Consequently its class in the Grothendieck ring of varieties over \(\mathbb F_5\) is \([V]=[\mathbb G_m]^2\), and for **every** \(q=5^n\) with \(n\ge1\),
\[
\#V(\mathbb F_q)=(q-1)^2,
\quad \#U(\mathbb F_q)=q^3-q^2,
\quad \#\{(a,b,c)\in U(\mathbb F_q):f_5(J)=2\}=(q-1)(q^2-q+1).
\]
These counts enumerate monic centered **coefficient triples**, not curve-isomorphism classes.

## Assumptions and scope
The characteristic is exactly \(5\). The curve equation is the fixed monic, centered quartic model above. The smooth parameter domain is \(U=\{D\ne0\}\), where the quartic discriminant, reduced modulo \(5\), is
\[
D=a^4c+a^3b^2+2a^2c^2-ab^2c-2b^4+c^3.
\]
All algebraic statements hold over any algebraically closed field of characteristic \(5\); finite-field formulas hold for each \(\mathbb F_{5^n}\). Because the cover of the \(x\)-line has four simple finite branch points and one totally ramified point at infinity, Riemann–Hurwitz gives genus \((3-1)(4-1)/2=3\). Equivalently, \(\gcd(3,4)=1\) and the separable quartic yields a smooth projective normalization.

## Proof
**1. Cartier action and the rank dichotomy.** A regular differential basis is
\[
\omega_1=dx/y^2,\quad\omega_2=x\,dx/y^2,\quad\omega_3=dx/y.
\]
In characteristic \(5\), \(\mathcal C(h^5\eta)=h\mathcal C(\eta)\) and \(\mathcal C(x^jdx)=0\) unless \(j\equiv4\pmod5\). Using \(y^3=f(x)\), one obtains
\[
\begin{aligned}
\mathcal C(\omega_1)&=y^{-1}\mathcal C(f(x)dx)=\omega_3,\\
\mathcal C(\omega_2)&=y^{-1}\mathcal C(xf(x)dx)=0,\\
\mathcal C(\omega_3)&=y^{-2}\mathcal C(f(x)^3dx)
=u^{1/5}\omega_1+v^{1/5}\omega_2,
\end{aligned}
\]
where \(u=[x^4]f(x)^3=3(c^2+a^2c+ab^2)=3P\) and \(v=[x^9]f(x)^3=3b\). Here \([x^j]\) denotes polynomial coefficient extraction, and fifth roots exist uniquely in the perfect algebraic closure. Thus the columns of the \(5^{-1}\)-linear Cartier matrix in this basis are \((0,0,1)^T\), \((0,0,0)^T\), and \((u^{1/5},v^{1/5},0)^T\).

For smooth \(f\), \((u,v)\ne(0,0)\) by Step 2, so Cartier always has rank \(2\), yielding \(a(J)=3-2=1\). If \(u\ne0\), successive Cartier images stabilize in dimension \(2\): the images of \(\omega_3\) and \(u^{1/5}\omega_1+v^{1/5}\omega_2\) generate a two-dimensional Cartier-stable subspace. If \(u=0\), then \(v\ne0\) and Cartier has the nilpotent chain \(\omega_1\mapsto\omega_3\mapsto v^{1/5}\omega_2\mapsto0\). The stable Cartier rank, equal to the Jacobian's \(5\)-rank, is therefore \(2\) or \(0\) respectively. Semilinearity merely replaces displayed nonzero coefficients by their fifth roots at each iteration; it does not change these stable ranks.

**2. Smoothness and irreducibility of the divisor.** For \(b=0\), \(P=0\) forces \(c=0\) or \(c=-a^2\). In the first case \(f\) has a repeated root at zero. In the second case, a root with \(x^2=2a\) is simultaneously a root of \(f\) and \(f'\), including the limiting case \(a=0\). Thus \(P=0,D\ne0\) forces \(b\ne0\).

Conversely, suppose \(P=0,b\ne0\). If \(a=0\), then \(c=0\), and \(D=-2b^4\ne0\). If \(a\ne0\), direct polynomial reduction of the discriminant modulo \(P\) gives
\[
a^2D=-2c^3(a^2+c)\qquad\text{whenever }P=0.
\]
If additionally \(D=0\), then \(c=0\) or \(c=-a^2\), and \(P=0\) forces \(b=0\), a contradiction. Hence
\[
V=\{P=0,b\ne0\}.
\]
The derivatives of \(P\) are \(2ac+b^2\), \(2ab\), and \(2c+a^2\). When \(a\ne0\) and \(b\ne0\), the middle derivative is nonzero; when \(a=0\) and \(b\ne0\), the first is nonzero. Thus \(V\) is smooth. Viewing \(P\) as a monic quadratic in \(c\) over \(k(a,b)\), its discriminant is \(a^4-4ab^2=a(a^3+b^2)\), not a square in \(k(a,b)\) because its \(a\)-valuation is one at the generic point of \(a=0\). It follows that \(P\) is geometrically irreducible and hence \(V\) is geometrically irreducible.

**3. Geometric stratification.** On \(a=0\), the equation \(P=0\) gives \(c=0\) and \(b\ne0\), yielding \(\mathbb G_m\). On \(a\ne0\), define \(t=b/a\) and \(s=c/a^2\). Because \(b\ne0\), \(t\ne0\). The equation \(P=0\) becomes \(a\,s(s+1)+t^2=0\), forcing \(s\notin\{0,-1\}\). Its inverse is regular on the stated punctured parameter domain:
\[
a=-\frac{t^2}{s(s+1)},\qquad
b=-\frac{t^3}{s(s+1)},\qquad
c=\frac{t^4}{s(s+1)^2}.
\]
These are genuine inverse morphisms over \(\mathbb F_5\). The disjoint constructible decomposition therefore gives
\[
[V]=(\mathbb L-1)+(\mathbb L-1)(\mathbb L-2)=(\mathbb L-1)^2.
\]
Hence \(\#V(\mathbb F_q)=(q-1)+(q-1)(q-2)=(q-1)^2\) for each finite extension.

**4. Total smooth census.** There are \(q^4-q^3\) monic squarefree quartic polynomials over \(\mathbb F_q\). Since \(4\) is invertible in characteristic \(5\), unique translation removes the cubic term, and each centered monic quartic has precisely \(q\) monic translates. Thus \(\#U(\mathbb F_q)=q^3-q^2\). Subtraction gives the stated rank-two count.

## Verification
The standalone `verify_picard5.py` uses only Python's standard library. It constructs \(\mathbb F_5\), \(\mathbb F_{25}\) and \(\mathbb F_{125}\) by exact polynomial arithmetic, then enumerates all marked triples, testing \(P\) and the quartic discriminant independently. Its expected counts for \((\#U,\#V,\#(U\setminus V))\) are respectively \((100,16,84)\), \((15000,576,14424)\), and \((1937500,15376,1922124)\). The universal statement is proved in the preceding four steps, not inferred from these enumerations.

## Relationship to prior work
Malmskog–Rasmussen (arXiv:1407.7892, first public version 2014-07-29) explain the Picard genus-three quartic model and its arithmetic significance. Kazemifard–Tafazolian (Finite Fields and Their Applications 34 (2015), 107–122, DOI:10.1016/j.ffa.2014.12.002) determine Newton polygons for special Picard equations such as \(y^3=x^4-x\) and \(y^3=x^4-1\), not a census over all centered monic quartics. Nourozi–Rahmati (arXiv:2306.07823) discuss the characteristic-dependent Cartier rank of Picard curves and provide general coefficient formulas; their stated invariant is the \(a\)-number, whereas the present contribution is the full coefficient-dependent **stable** Cartier rank together with the explicit geometry and extension-field counting of the zero-rank divisor. Estrada-Sarlabous (1991, DOI:10.1002/mana.19911520125) is a relevant earlier source on Hasse–Witt conditions; only its abstract was accessible, so historical overlap of the explicit zero-rank equation remains a documented risk. The geometrical stratification and \((q-1)^2\) census are not asserted to be absent from unseen literature.

## Limitations
The theorem classifies \(5\)-ranks and \(a\)-numbers only; it does **not** classify all Newton polygons or complete Ekedahl–Oort types. It does not enumerate geometric isomorphism classes, cubic twists, or the singular boundary. The irreducible divisor is defined for a particular marked normalization of the Picard family. Its novelty has not been independently established, and the 1991 full text could not be inspected. Only the finite tests, not a formal proof assistant, were executed; the universal argument is given explicitly above.

## References
1. B. Malmskog and C. Rasmussen, *Picard curves over Q with good reduction away from 3*, arXiv:1407.7892, initially available 2014-07-29; https://arxiv.org/abs/1407.7892.
2. A. Kazemifard and S. Tafazolian, *A note on some Picard curves over finite fields*, Finite Fields and Their Applications 34 (2015), 107–122; https://doi.org/10.1016/j.ffa.2014.12.002.
3. V. Nourozi and F. Rahmati, *The Rank of the Cartier Operator on Picard Curves*, arXiv:2306.07823 (2023); https://arxiv.org/abs/2306.07823.
4. J. Estrada-Sarlabous, *On the Jacobian Varieties of Picard Curves Defined over Fields of Characteristic p > 0*, Mathematische Nachrichten 152 (1991), 329–340; https://doi.org/10.1002/mana.19911520125 (abstract accessible; full text not inspected).
