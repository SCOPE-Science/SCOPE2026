# Alternating Eisenstein classification for a quadratic composite tower
## Finding
Let \(c\) be a positive integer with \(c\equiv 2\pmod 4\). Define \(g(x)=x^2-1\) and, for every integer \(N\ge 0\),
\[
F_{c,N}(x)=\bigl(g^{\circ N}(x)\bigr)^2+c.
\]
Then every \(F_{c,N}\) is irreducible over \(\mathbb Q\). More precisely, \(F_{c,N}\) itself is 2-Eisenstein when \(N\) is even, and \(F_{c,N}(x+1)\) is 2-Eisenstein when \(N\) is odd.

For every \(N\ge1\), the polynomial \(F_{c,N}\) is monogenic if and only if both \(c\) and \(c+1\) are squarefree. Consequently, within \(c\equiv2\pmod4\), the whole positive-level tower is monogenic exactly for consecutive squarefree pairs \(c,c+1\); otherwise no positive level is monogenic.

## Assumptions and scope
A monic irreducible polynomial is called monogenic here when a root generates the full ring of integers of its number field. The statement concerns positive integers \(c\equiv2\pmod4\) and all finite levels \(N\). It uses Theorem 1.8 of arXiv:2610.02111v1 for the monogeneity criterion after irreducibility has been established independently.

## Proof
Over \(\mathbb F_2\), the polynomial \(g(x)=x^2-1\) equals \(x^2+1\). Frobenius therefore gives, by induction,
\[
g^{\circ N}(x)\equiv
\begin{cases}
x^{2^N},&N\text{ even},\\
x^{2^N}+1,&N\text{ odd}
\end{cases}
\pmod2.
\]
Put \(D=2^{N+1}\). Because \(c\) is even,
\[
F_{c,N}(x)\equiv
\begin{cases}
x^D,&N\text{ even},\\
x^D+1,&N\text{ odd}
\end{cases}
\pmod2.
\]
If \(N\) is even, \(g^{\circ N}(0)=0\), hence the constant term of \(F_{c,N}\) is exactly \(c\). Since \(c\equiv2\pmod4\), all nonleading coefficients are divisible by \(2\) and the constant term is not divisible by \(4\). Thus \(F_{c,N}\) is 2-Eisenstein.

If \(N\) is odd, then in characteristic two
\[
F_{c,N}(x+1)\equiv (x+1)^D+1=x^D\pmod2,
\]
because \(D\) is a power of two. Also \(g^{\circ N}(1)=0\) for odd \(N\), so the constant term of the translate is \(F_{c,N}(1)=c\), again of exact 2-adic valuation one. Hence \(F_{c,N}(x+1)\) is 2-Eisenstein. Translation preserves irreducibility, proving irreducibility at every level.

Apply Theorem 1.8 of arXiv:2610.02111v1 with outer polynomial \(f(x)=x^2+c\) and inner polynomial \(g(x)=x^2-1\). Here \(n=m=2\) and \(\operatorname{rad}(m)\mid n\). The orbit of zero under \(g\) is
\[
0,-1,0,-1,\ldots,
\]
so
\[
(f\circ g^{\circ i})(0)=
\begin{cases}c,&i\text{ even},\\c+1,&i\text{ odd}.\end{cases}
\]
For every \(N\ge1\), the squarefreeness condition in that theorem is therefore exactly that both \(c\) and \(c+1\) are squarefree. Its remaining condition has only the prime \(p=2\) and becomes
\[
4\nmid (-c)^2+c=c(c+1).
\]
Since \(c\equiv2\pmod4\) and \(c+1\) is odd, this condition is automatic. The theorem now gives the claimed if-and-only-if classification.

## Verification
The bundled `verify.py` performs exact integer-polynomial checks for \(c\equiv2\pmod4\), \(2\le c<80\), through level \(N=6\). It checks the parity pattern, the exact 2-adic valuation of the relevant constant term before or after translation, the alternating orbit \(0,-1\), and the reduction of Theorem 1.8's conditions to squarefreeness of \(c,c+1\). These finite checks corroborate the symbolic proof; they are not used to replace its universal steps.

## Relationship to prior work
The motivating paper proves a general criterion for monogeneity of binomial composite iterates, conditional on irreducibility. Its Theorem 1.8 specializes to the squarefree critical-value test used above, but it does not state the present \(g(x)=x^2-1\), \(c\equiv2\pmod4\) classification or the alternating shift/no-shift Eisenstein certificate that removes the irreducibility hypothesis at every level. Its explicit infinite-tower example in Section 6 is instead a cyclotomic polynomial composed with a different Misiurewicz trinomial.

Earlier work on binomial composition treats one composition \(f(g(x))\), so it can overlap the first positive level but does not supply the uniform all-level result. Work on dynamically monogenic iterates studies iterates of a single polynomial (and more general backward-orbit formulations); the 2026 composition paper explicitly distinguishes the distinct-polynomial tower considered here.

## Limitations
The monogeneity implication relies on the published Theorem 1.8 of arXiv:2610.02111v1. The result is a classification only inside the congruence class \(c\equiv2\pmod4\); no claim is made for other residue classes, where this 2-Eisenstein mechanism can fail. The verification script samples finitely many levels and parameters and is only a reproducibility check for the algebra used in the proof.

## References
1. A. Jakhar, R. Kalwaniya, S. Laishram, P. Yadav, *On The Index of Polynomial Compositions over Valued Fields*, arXiv:2610.02111v1 (2026), especially Theorem 1.8 and Section 6.
2. A. Jakhar, R. Kalwaniya, P. Yadav, *A Study of monogenity of Binomial Composition*, Acta Arithmetica 221 (2025), 387--395; arXiv:2402.10131.
3. J. König, H. Smith, Z. Wolske, *Critical Point Criteria and Dynamically Monogenic Polynomials*, arXiv:2412.10358; Canadian Journal of Mathematics (2026).
