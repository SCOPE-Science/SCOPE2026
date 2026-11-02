# Cartier-rank stratification and the first extra superspecial fibers of a cyclic-six genus-three family

## Finding

Let \(k=\overline{\mathbb F}_{31}\) and let \(C_a/k\) be the smooth projective curve
\[
 C_a:\quad y^2=x^7+a x^4+x=x(x^6+a x^3+1),\qquad a\in k,\quad a^2\ne4.
\]
Its Jacobian has the following complete rank stratification, counted at **marked parameter values**, not at geometric isomorphism classes:

| Condition on \(a\) | \(31\)-rank | \(a\)-number | Number of geometric parameter values |
|---|---:|---:|---:|
| \(a=0\) or \(a=12\) or \(a=-12\) | 0 | 3 | 3 |
| \(a^2=12\) | 1 | 2 | 2 |
| \(B(a)=0\) and \(a\notin\{0,12,-12\}\) | 2 | 1 | 12 |
| all remaining smooth parameters | 3 | 0 | infinite |

Here \(B(a)\) is the degree-fifteen polynomial over \(\mathbb F_{31}\)
\[
 B(a)=a^{15}-7a^{13}+6a^{11}+a^9-11a^7+15a^5-2a^3-11a.
\]
In particular, exactly three marked smooth fibers are superspecial, including the two nonzero parameters \(\pm12\). Among primes \(5\le p\le31\), characteristic \(31\) is the first for which the corresponding family \(y^2=x^7+a x^4+x\) has any smooth superspecial fiber with \(a\ne0\).

## Assumptions and scope

The base field is algebraically closed and of characteristic \(31\) for the primary classification. The additional finite-prime comparison covers only the primes \(5,7,11,13,17,19,23,29,31\); nothing is asserted about the first such prime after \(31\), or about all primes in any congruence class. The parameter is marked: distinct parameters might define isomorphic curves. The case \(a^2=4\) is excluded because the degree-seven polynomial is not squarefree.

For a curve of genus \(g\), the \(p\)-rank is the dimension of the stable semilinear Frobenius subspace on \(H^1(C,\mathcal O_C)\); the \(a\)-number is \(g-\operatorname{rank}(\mathcal C)\), with \(\mathcal C\) the Cartier operator on regular one-forms. A genus-three Jacobian of \(a\)-number three is superspecial.

## Proof

**Smoothness and geometry.** Set \(f_a(x)=x(x^6+a x^3+1)\). The root at zero is simple; for nonzero roots, write \(z=x^3\). Since the characteristic is neither two nor three, repeated nonzero roots occur precisely when \(z^2+az+1\) has a repeated root, equivalently \(a^2=4\). Every allowed fiber is therefore smooth of genus three. The substitution
\[
 (x,y)\longmapsto(1/x,y/x^4)
\]
defines an involution. Its elliptic quotient is \(v^2=u^3-3u+a\), with \(u=x+x^{-1}\) and \(v=y/x^2\). The complementary genus-two quotient is \(w^2=(u^2-4)(u^3-3u+a)\). These natural quotient curves motivate the arithmetic stratification.

**Coefficient reduction.** In the standard basis \(dx/y, x\,dx/y,x^2\,dx/y\), the Hasse--Witt coefficient matrix is \(H=(c_{31i-j})_{1\le i,j\le3}\), where \(c_n=[x^n]f_a(x)^{15}\). As
\[
 f_a(x)^{15}=x^{15}\left(1+a x^3+x^6\right)^{15},
\]
and \(31i-j-15\) is divisible by three precisely when \(i=j\), this matrix is diagonal. Its diagonal entries are the coefficients \([z^5]\), \([z^{15}]\), and \([z^{25}]\) of \((1+az+z^2)^{15}\). Reciprocity makes the first and third equal. Explicit multinomial expansion modulo \(31\) gives
\[
 H(a)=\operatorname{diag}(A(a),B(a),A(a)),
 \quad A(a)=-4a^5+4a^3+a.
\]
The displayed polynomial \(B(a)\) is the central coefficient. For every \(i,j\), the coefficient is reproducible from the integer sum
\[
 [z^k](1+az+z^2)^{15}=
 \sum_{\substack{r,s,t\ge0\\r+s+t=15\\2r+s=k}}
 \frac{15!}{r!s!t!}a^s\pmod{31}.
\]

**Root and rank certificates.** In \(\mathbb F_{31}[a]\), exact multiplication yields
\[
 A=-4a(a-12)(a+12)(a^2-12)
\]
and
\[
\begin{aligned}
 B={}&a(a-15)(a-12)(a-8)(a-6)(a+6)(a+8)(a+12)(a+15)\\
 &\cdot(a^2+4)(a^2-4a-11)(a^2+4a-11).
\end{aligned}
\]
The Euclidean algorithm gives \(\gcd(A,B)=a(a^2+11)\). Moreover \(\gcd(A,A')=\gcd(B,B')=1\), and neither \(a=2\) nor \(a=-2\) is a root of either polynomial. Thus the geometric common-zero set consists of three points: \(0\), \(12\), and \(-12\), since \(12^2\equiv-11\pmod{31}\). There are exactly two further zeros of \(A\), exactly twelve further zeros of \(B\), and no other rank drops. A diagonal semilinear matrix has stable rank equal to the number of its nonzero diagonal entries: every nonzero entry stays nonzero under all Frobenius twists. Thus \(p\)-ranks are \(0,1,2,3\) on the respective strata, while Cartier ranks equal the same counts. This proves the \(a\)-numbers and the superspecial assertion.

**Comparison across smaller primes.** For \(p\in\{5,7,11,13,17,19,23,29\}\), form the three-by-three coefficient matrix \(([x^{pi-j}]f_a(x)^{(p-1)/2})_{i,j}\) and take the monic polynomial gcd of all its nonzero entries. These gcds, respectively, are
\[
 1,\ a,\ a,\ 1,\ 1,\ a,\ a,\ 1.
\]
A superspecial fiber forces all entries to vanish. Consequently no nonzero smooth parameter is superspecial in any smaller prime characteristic at least five. In characteristic \(31\) the common gcd is \(a(a^2+11)\), producing the two additional smooth fibers.

## Verification

Run `python3 verify.py` with a standard-library Python 3 interpreter. The script reconstructs the complete Hasse--Witt coefficient matrices from multinomial coefficients; verifies both factorization identities and their gcds; checks squarefreeness and exclusion of the singular boundary; and computes the common gcd of all nine Hasse--Witt entries for each prime \(5\le p\le31\). The expected terminal line is `VERIFY_OK`. This is finite exact arithmetic verifying the complete algebraic certificates; the proof of the rank stratification also uses the standard general Hasse--Witt/Cartier theory explained above.

## Relationship to prior work

Gutierrez--Sevilla--Shaska classify genus-three hyperelliptic curves with extra involutions, their natural quotient structures, and dihedral moduli invariants; those results motivate the present family but do not contain this characteristic-\(31\) Cartier-rank stratification. Recent work of Ohashi and collaborators enumerates superspecial genus-three curves by Richelot-isogeny graphs; it establishes the global classification framework rather than the four rank strata of this marked one-parameter family. General Cartier--Manin coefficient methods are classical. No novelty is claimed for the general matrix formula, for extra involutions, or for the already-known existence of genus-three superspecial curves.

## Limitations

The classification is for **marked fibers** and does not count moduli isomorphism classes. It does not determine all Newton slopes at the nonordinary non-superspecial parameters, nor any Jacobian isomorphism class. The exact rank polynomial is characteristic-specific. The least-prime statement covers only primes at least five. A comprehensive historical search cannot exclude unindexed explicit parameter tables or unpublished calculations; independent mathematical audit has not been performed.

## References

1. J. Gutierrez, D. Sevilla, T. Shaska, *Hyperelliptic curves of genus 3 with prescribed automorphism group*, arXiv:1209.2938v1, posted 2012-09-13. https://arxiv.org/html/1209.2938v1
2. R. Ohashi and collaborators, *Listing superspecial curves of genus three using Richelot isogeny graphs*, Research in Number Theory 11 (2025), article 76, published 2025-08-07. https://doi.org/10.1007/s40993-025-00657-3
3. M. Kudo and collaborators, *Efficient Search for Superspecial Hyperelliptic Curves of Genus Four with Automorphism Group Containing C6*, Mathematics in Computer Science (2023). https://doi.org/10.1007/s11786-023-00571-w (genus-four methods and context, not a genus-three rank classification).
