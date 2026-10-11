# Sharp sixth moments for the resonant three-character spectrum

## Finding
Let \(G\) be any compact abelian group with normalized Haar probability measure \(\mu\). Let \(\gamma,\chi\) be continuous characters, and suppose that \(\chi\) has order at least \(10\), or infinite order. For every \(a,b,c\in\mathbb C\) put
\[
F(g)=\gamma(g)\bigl(a+b\chi(g)+c\chi(g)^3\bigr).
\]
There is an **exact sharp inequality**
\[
\boxed{\ \int_G |F(g)|^6\,d\mu(g)\le\mathcal K\bigl(|a|^2+|b|^2+|c|^2\bigr)^3\ },
\qquad \mathcal K=3.676690884789743660826985\ldots.
\]
Define
\[
\begin{aligned}
N(u,v)&=1+u^6+v^6+9\bigl(u^2+v^2+u^4+v^4+u^2v^4+u^4v^2\bigr)\\
&\quad+36u^2v^2+6u^3v,\qquad D(u,v)=1+u^2+v^2,\\
E_u&=D\partial_uN-6uN,\qquad E_v=D\partial_vN-6vN.
\end{aligned}
\]
The pair \((\beta,\nu)\) is defined *exactly* as the unique positive common zero of \(E_u,E_v\). In particular, \(\nu^2\) is the unique root in \((0.9064,0.9066)\) of
\[
\begin{aligned}
P(s)={}&4800s^{10}+24320s^9-22480s^8-135480s^7+216636s^6\\
&-59622s^5-51379s^4+17526s^3+5227s^2+200s-4.
\end{aligned}
\]
Then \(\mathcal K=N(\beta,\nu)/D(\beta,\nu)^3\), with
\[\beta=1.041902397926431006619\ldots,\qquad\nu=0.9520903910689997578498\ldots.\]
**All** nonzero equality cases are
\[
\boxed{(a,b,c)=\lambda\bigl(1,\beta e^{i\theta},\nu e^{3i\theta}\bigr),\quad\lambda\in\mathbb C\setminus\{0\},\quad\theta\in\mathbb R.}
\]
The character-order threshold \(10\) cannot be reduced: for each order \(4\le n\le9\), there is a positive-coefficient vector violating the same constant.

## Assumptions and scope
The three characters \(\gamma,\gamma\chi,\gamma\chi^3\) are distinct in every claimed case. The norm is a normalized Haar sixth moment, not the spatial Tomas--Stein extension norm for the Euclidean circle. In the finite case \(\mu\) is counting measure divided by \(|G|\), and the measure induced by \(\chi\) is uniform on all roots of unity of its order. When \(\chi\) has infinite order, it induces Haar measure on the full unit circle. Only the order of \(\chi\) matters; no cyclicity assumption on \(G\) is needed. The zero coefficient vector satisfies the inequality but is excluded from the equality classification's nonzero clause.

## Proof
**1. Orthogonality and resonance.** Expanding the cube of \(a+bz+cz^3\) gives monomials with exponents \(0,1,2,3,4,5,6,7,9\). For characters of order at least \(10\), and for infinite-order characters, these exponents are pairwise distinct. Parseval for the cube therefore yields the *exact* identity
\[
\begin{aligned}
\int_G|F|^6\,d\mu
={}&S^3+6S T+12 U+6\operatorname{Re}\bigl(b^3\overline{a^2c}\bigr),\\
S={}&|a|^2+|b|^2+|c|^2,\\
T={}&|ab|^2+|ac|^2+|bc|^2,\quad U=|abc|^2.
\end{aligned}
\]
The last term is caused by the unique non-permutation triple-sum collision \(1+1+1=0+0+3\). For fixed nonzero magnitudes, it is maximal exactly when \(b^3\overline{a^2c}\) is positive real.

**2. Reduction to two positive variables.** On a nonzero vector with \(a\ne0\), divide all magnitudes by \(|a|\), and write \(u=|b|/|a|\), \(v=|c|/|a|\). After maximizing the phase, the quotient is precisely \(N(u,v)/D(u,v)^3\), with \(N,D\) defined above. If any coefficient is zero, the quotient is at most \(5/2\): for two distinct characters its sixth moment equals \(x^3+y^3+9x^2y+9xy^2\), where \(x,y\) are the two squared coefficient moduli. Relative to \((x+y)^3\), this is \(1+6xy/(x+y)^2\le5/2\). But \((a,b,c)=(1,1,1)\) produces \(99/27=11/3>5/2\), so every global maximizer has all three magnitudes positive. Compactness of the unit coefficient sphere guarantees existence.

**3. Exact certification of the unique interior stationary point.** Differentiating the rational quotient gives the stationary equations \(E_u=E_v=0\). Exact polynomial elimination over \(\mathbb Q\) produces
\[
\operatorname{Res}_u(E_u,E_v)=-104485552128\,v^3(v^2-1)(v^2+1)^3(5v^2+1)P(v^2).
\]
For \(v>0\), the extraneous factors cannot vanish except at \(v=1\). That case has no solution with \(u>0\): after dividing the two equations by their nonzero monomial factors and taking their indicated difference, a necessary condition is \(u(u^2+2)=0\). The exact calculation is contained in `checker.py`.

A rational Sturm-sequence isolation finds precisely three positive roots of \(P\), in the disjoint rational intervals \((0.0143,0.0145)\), \((0.9064,0.9066)\), and \((1.099,1.101)\), all simple. The reduced lexicographic Gröbner basis of \((E_u,E_v)\) contains the linear relation
\[
v(v^2+1)\left(K_0u+v(v^2-1)(v^2+1)Q(v^2)\right)=0,
\quad K_0=9096133226180822175068352,
\]
where \(Q\) is an *explicit integer polynomial of degree ten*, computed exactly from the ideal in `checker.py`. The checker reconstructs its full coefficients from the basis, tests the identity and certifies by rational interval arithmetic that the signs of \(Q\) at those three positive roots, in order, are \((-1,+1,+1)\). Since \(K_0>0\), the relation forces \(u<0,u>0,u<0\), respectively. Moreover, substituting the linear expression for \(u\) into each of \(E_u,E_v\) gives numerators divisible exactly by \(P(v^2)\); the checker verifies these polynomial remainders are zero over \(\mathbb Q\). Thus the *middle* root gives one genuine common zero with \(u,v>0\), and it is the only positive stationary point. Existence of an interior global maximizer, proved in step 2, forces this unique stationary point to be the global maximizer. It gives the stated exact sharp \(\mathcal K\) and the displayed algebraic definitions of \(\beta,\nu\). No floating-point root comparison establishes uniqueness; all root counts, signs and remainders use exact rational arithmetic.

**4. Every equality case.** Strict interiority fixes the modulus ratios at \((1,\beta,\nu)\). Equality in the phase reduction is equivalent to \(b^3\overline{a^2c}\) positive real. Writing \(a=\lambda\ne0\), this phase relation is equivalent to \(b=\lambda\beta e^{i\theta}\), \(c=\lambda\nu e^{3i\theta}\) for some \(\theta\in\mathbb R\). These vectors attain the bound by step 1, proving necessity and sufficiency.

**5. Sharp character-order threshold.** For orders \(4\le n\le9\), at least two of the exponents \(0,1,2,3,4,5,6,7,9\) are congruent modulo \(n\). At the positive coefficient vector \((1,\beta,\nu)\), *every coefficient* of the expanded cube is positive. Identifying any such exponent classes therefore strictly increases the sum of squared Fourier coefficients; the resulting sixth moment is strictly greater than \(N(\beta,\nu)\). Because the squared coefficient norm is unchanged, the stable constant \(\mathcal K\) fails at each of these orders. At orders \(n\ge10\), no exponents alias, so the displayed theorem holds exactly.

## Verification
Run `python checker.py` with Python 3 and SymPy at least version \(1.12\). It prints `CERTIFICATE_PASS` after computing the exact polynomial resultant, Sturm root intervals and multiplicities, a rational Gröbner basis, rational interval signs, zero polynomial remainders, the special \(v=1\) contradiction, and exact integer coefficient-convolution structure. It then supplements the proof with randomized complex-coefficient checks and finite-order aliasing checks. Its example numeric output gives \(\beta\approx1.041902397926431\), \(\nu\approx0.9520903910689998\), \(\mathcal K\approx3.6766908847897437\). The symbolic computation supplies checkable finite polynomial identities; finite numerical tests are not treated as proof of the infinite family.

## Relationship to prior work
Ciccone and Gonçalves study a sharp Tomas--Stein Fourier extension inequality for functions on the Euclidean circle with arithmetic restrictions on Fourier support. Their norm is taken **after Fourier transformation of arc-length measure in the Euclidean plane**, rather than the intrinsic sixth moment of a three-character polynomial on a compact group. Their theorem therefore does not imply the constant here. Neuwirth's classification for trigonometric trinomials concerns the *maximum-modulus* norm, multiplier and Sidon norms. Krenedits' majorant results concern different exponents and specific coefficient signs. A published explicit formula for unimodular three-frequency *even moments* includes the phase-resonance structure, but fixes all three coefficient magnitudes at one and explicitly leaves unequal magnitudes outside its claim. Its formula does not optimize the nonuniform weighted quotient here. A published finite-cyclic majorant result concerns a signed-vs-unsigned comparison at the third moment, not this sharp sixth moment.

## Limitations
Originality is assessed against the inspected full texts and the published records searched under weighted \(\Lambda(6)\) inequalities, trigonometric trinomials, resonance and coefficient optimization; an equivalent older formula under a different name cannot be excluded. The result does not describe the sharp constants for orders \(4\) through \(9\); it proves only their strict separation from the stable value. The exact optimizer classification depends on the displayed polynomial certificate and its independently executable exact-arithmetic reconstruction; it has not undergone an independent mathematical audit. The theorem does not address non-even moments, more than three frequencies, or Euclidean spatial extension norms.

## References
1. V. Ciccone and F. Gonçalves, *Sharp Fourier Extension on the Circle Under Arithmetic Constraints*, arXiv:2208.09441v1, initially submitted 2022-08-19. This source motivates resonant third additive sums but treats the Euclidean spatial extension norm.
2. S. Neuwirth, *The maximum modulus of a trigonometric trinomial*, arXiv:math/0703236v1, 2007.
3. S. Krenedits, *Three-term idempotent counterexamples in the Hardy--Littlewood majorant problem*, arXiv:1006.0409v1, 2010.
4. *Even phase moments recover the normalized geometry of a three-frequency spectrum*, published published-finding corpus mathematical record 7849dda51c79, 2026.
5. *A finite-cyclic three-term majorant reversal exactly from order five onward*, published published-finding corpus mathematical record 60a27acbb9f3, 2026.
