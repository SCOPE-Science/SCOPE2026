# A uniform Hasse divisor for the bielliptic Picard pencil

## Finding

Let \(p\geq5\) be prime, \(k=\overline{\mathbb F}_p\), and let \(C_t\) be the smooth projective model of
\[
y^3=x^4+2t x^2+1,\qquad t\in k\setminus\{1,-1\}.
\]
Write \(r=\lfloor(p-1)/6\rfloor\) and define the following explicit polynomial over \(\mathbb F_p\):
\[
H_p(T)=\begin{cases}
[u^{3r}](u^2+2Tu+1)^{2r},&p=6r+1,\\
[u^{3r+2}](u^2+2Tu+1)^{2r+1},&p=6r+5.
\end{cases}
\]
Here \([u^m]\) extracts the coefficient of \(u^m\). The polynomial \(H_p\) has degree exactly \(r\), has \(r\) distinct geometric roots, and has no root at \(T=\pm1\). The Newton polygon, geometric \(p\)-rank \(f\), and \(a\)-number of the Jacobian of \(C_t\) are completely determined as follows:

| Prime congruence | Parameter | \(f\) | \(a\) | Newton slopes, with multiplicity |
| --- | --- | ---: | ---: | --- |
| \(p\equiv1\pmod6\) | \(H_p(t)\ne0\) | 3 | 0 | \(0^{[3]},1^{[3]}\) |
| \(p\equiv1\pmod6\) | \(H_p(t)=0\) | 1 | 2 | \(0^{[1]},(1/2)^{[4]},1^{[1]}\) |
| \(p\equiv5\pmod6\) | \(H_p(t)\ne0\) | 2 | 1 | \(0^{[2]},(1/2)^{[2]},1^{[2]}\) |
| \(p\equiv5\pmod6\) | \(H_p(t)=0\) | 0 | 3 | \((1/2)^{[6]}\) |

Thus the non-generic locus is a **reduced divisor consisting of exactly \(\lfloor(p-1)/6\rfloor\) smooth parameter values**. In the final row the curve is superspecial. For \(p=5\), the divisor is empty. All assertions concern the displayed marked parameter, over an algebraically closed field; no quotient by curve isomorphisms is taken.

## Assumptions and scope

A \(p\)-rank is \(f(J)=\dim_{\mathbb F_p}J[p](k)\), and the \(a\)-number is \(a(J)=\dim_k\operatorname{Hom}(\alpha_p,J)\). The Newton slopes are those of the \(p\)-divisible group of \(J\), counted with multiplicity. Prime characteristic \(p\geq5\) is essential: the displayed equation is a tame degree-three cover only away from characteristic three, and the smoothness computation uses characteristic different from two. The quartic in \(x\) is separable precisely when \(t^2\ne1\). Its four finite simple roots and the point over infinity are fully ramified under the degree-three projection, giving genus three by Riemann--Hurwitz.

## Proof

**1. Cartier computation.** Put \(F_t(x)=x^4+2t x^2+1\), and write \(U_t(u)=u^2+2tu+1\), so \(F_t(x)=U_t(x^2)\). A basis of regular differentials on \(C_t\) is
\[
\omega_0=dx/y^2,\quad \omega_1=x\,dx/y^2,\quad \omega_2=dx/y.
\]
For \(j\in\{1,2\}\), choose \(j'\in\{1,2\}\) with \(pj'\equiv j\pmod3\), and set \(k=(pj'-j)/3\). Then
\[
\frac{x^i dx}{y^j}=\frac{x^iF_t(x)^k dx}{(y^{j'})^p}.
\]
The standard Cartier coefficient-extraction rule yields the image of \(x^i dx/y^j\) by selecting coefficients of \(x^{p(i'+1)-(i+1)}\) in \(F_t(x)^k\) and taking their \(p\)-th roots. Odd exponents vanish because \(F_t\) is even.

Define \(A_{k,m}(T)=[u^m]U_T(u)^k\). For \(p=6r+1\), the Cartier operator on the ordered basis \((\omega_0,\omega_1,\omega_2)\) is diagonal up to coefficient-wise \(p\)-th roots, with coefficients
\[
E=A_{4r,3r}(t),\qquad G=A_{4r,6r}(t),\qquad H=A_{2r,3r}(t).
\]
For \(p=6r+5\), its only potentially nonzero entries are
\[
\mathcal C(\omega_0)=H^{1/p}\omega_2,\quad
\mathcal C(\omega_1)=0,\quad
\mathcal C(\omega_2)=A^{1/p}\omega_0,
\]
where \(H=A_{2r+1,3r+2}(t)\), \(A=A_{4r+3,3r+2}(t)\).

**2. Coefficient identities over the prime field.** In \(\mathbb F_p[T]\) one has, for nonzero constants \(\lambda_p,\mu_p,\nu_p\in\mathbb F_p^{\times}\),
\[
\begin{aligned}
&p=6r+1:\qquad E=\lambda_p(T^2-1)^r H_p(T),\quad G=\mu_p(T^2-1)^r,\\
&p=6r+5:\qquad A=\nu_p(T^2-1)^{r+1}H_p(T).
\end{aligned}
\]
For completeness, here is a coefficient proof, including the nontrivial common-factor claim. For \(B(T)=A_{k,m}(T)\), the Gegenbauer coefficient identity gives
\[
(1-T^2)B''+(2k-1)TB'+m(m-2k)B=0.\tag{1}
\]
At \(T=1\), its \(j\)-th derivative is a nonzero scalar times \(\binom{2k-2j}{m-j}\), whenever \(j\le k\). Using \(p=6r+1\), Lucas' binomial congruence shows that the derivatives of \(E\) and \(G\) of orders \(0,\ldots,r-1\) vanish at \(1\): the upper indices are \(8r-2j\), while the lower indices are respectively \(3r-j\) and \(6r-j\), both exceeding the base-\(p\) remainder \(2r-2j-1\). Using \(p=6r+5\), the derivatives of \(A\) of orders \(0,\ldots,r\) vanish at \(1\): the upper index is \(8r+6-2j\) and its base-\(p\) remainder is \(2r+1-2j<3r+2-j\). The same vanishing holds at \(T=-1\) by parity. Therefore \(E,G,A\) have the stated powers of \(T^2-1\) as factors.

The degree bounds from the coefficient formula give
\[
\deg E=3r,\quad \deg G=2r,\quad \deg A=3r+2.
\]
Consequently \(G/(T^2-1)^r\) is a nonzero constant, while \(E/(T^2-1)^r\) and \(A/(T^2-1)^{r+1}\) have degree \(r\). Substituting the respective factorizations into (1), and reducing using \(6r+1=0\) or \(6r+5=0\) in \(\mathbb F_p\), shows that both degree-\(r\) quotients satisfy the same equation (1) as \(H_p\). Its coefficient recurrence, for \(B=\sum c_jT^j\), is
\[
(j+2)(j+1)c_{j+2}=(j-r)(j-m)c_j,
\]
with \(m=3r\) or \(m=3r+2\) respectively. Since \(r<p\) and \(m>r\), this equation has a one-dimensional space of polynomial solutions of degree at most \(r\): the opposite-parity leading coefficient is forced to vanish at degree \(r-1\), and the other coefficients follow recursively. The quotients are therefore nonzero scalar multiples of \(H_p\), as claimed. All scalar factors are nonzero because the displayed coefficient polynomials have nonzero leading coefficients (binomial coefficients with upper index strictly smaller than \(p\)).

**3. Degree and reducedness of the divisor.** Let \((k,m)=(2r,3r)\) if \(p=6r+1\) and \((k,m)=(2r+1,3r+2)\) if \(p=6r+5\). Expanding \(U_T(u)^k\), the highest \(T\)-power in \([u^m]U_T(u)^k\) is \(T^r\), with respective coefficients \(2^r\binom{2r}{r}\) and \(2^r\binom{2r+1}{r}\). Neither vanishes modulo \(p\). Also
\[
H_p(1)=\binom{2k}{m}\ne0,\qquad H_p(-1)=(-1)^m\binom{2k}{m}\ne0,
\]
since \(2k<p\). Every geometric root \(a\) therefore satisfies \(a^2\ne1\). If \(a\) were a multiple root, equation (1) and its successive derivatives at \(a\) would force every derivative of \(H_p\) to vanish at \(a\). This contradicts \(\deg H_p=r<p\). Thus the polynomial has exactly \(r\) distinct roots in \(k\), all in the smooth parameter range.

**4. Ranks, \(a\)-numbers, and Newton slopes.** By step 2, for \(p\equiv1\pmod6\) the Cartier matrix is invertible when \(H_p(t)\ne0\), and otherwise has exactly one invertible one-dimensional block. For \(p\equiv5\pmod6\), the Cartier operator has an invertible two-dimensional swap block and a one-dimensional kernel when \(H_p(t)\ne0\), and vanishes altogether when \(H_p(t)=0\). These decompositions are Frobenius-stable under iteration, so their stable ranks, not merely their first ranks, are respectively \(3,1,2,0\). Since \(a=3-\operatorname{rank}(\mathcal C)\), the asserted \(p\)-ranks and \(a\)-numbers follow. In the rank-zero case the vanishing Cartier operator also proves superspeciality.

The involution \((x,y)\mapsto(-x,y)\) has elliptic quotient \(E_t:y^3=u^2+2tu+1\), equivalently \(v^2=y^3-(1-t^2)\), with \(j(E_t)=0\). A degree-two isogeny decomposes the Jacobian into \(E_t\) and a two-dimensional Prym. Because \(p\ne2\), the \(p\)-divisible groups decompose under this isogeny. The elliptic quotient is ordinary for \(p\equiv1\pmod3\) and supersingular for \(p\equiv2\pmod3\). The remaining Prym is ordinary or \(p\)-rank zero as determined above; a dimension-two abelian variety of \(p\)-rank zero has all slopes \(1/2\). Combining the two slope multisets yields exactly the four Newton polygons in the table.

## Verification

The standalone `verify.py` constructs the coefficient polynomials from exact integer multinomial coefficients reduced modulo \(p\), verifies the relevant polynomial divisibility and proportionality identities, checks the Gegenbauer differential equation, and checks squarefreeness and values at \(\pm1\). It succeeded independently for all 44 primes from \(5\) through \(199\). These finite computations corroborate but do not replace the general coefficient proof above. The public checker has no external package dependencies; run it with `python3 verify.py`.

## Relationship to prior work

Laga and Shnidman, *The geometry and arithmetic of bielliptic Picard curves* (arXiv:2308.15297, first posted 2023-08-29), establish the marked family, elliptic quotient and Prym geometry, and connect the moduli line to a quaternionic Shimura curve of discriminant six. Their stated results concern geometric structures, endomorphisms, and rational torsion rather than an explicit uniform positive-characteristic Cartier stratification. Their *Ceresa cycles of bielliptic Picard curves* (arXiv:2312.12965, 2023-12-20) studies the same normalized pencil but a different cycle-theoretic invariant. Kazemifard and Tafazolian, *A note on some Picard curves over finite fields* (2015), classify Newton polygons for the two special equations \(y^3=x^4-x\) and \(y^3=x^4-1\), not this full parameter-dependent divisor. The special point \(t=0\) is therefore not new in isolation. Terakado, Xue and Yu, *Superspecial Points on Shimura Curves* (arXiv:2608.16036, 2026), provide broader class-number results for moduli of quaternionic abelian surfaces, but not the explicit polynomial for the displayed marked genus-three pencil. The present statement supplies that explicit parameter-level criterion and the complete four-way arithmetic stratification.

## Limitations

No classification of abstract isomorphism classes of the curves is claimed; several marked parameters can describe isomorphic objects. This proof does not determine the factorization degrees of \(H_p\) over individual finite fields, and the root count is geometric. The derivation does not claim that the general theory of supersingular points on Shimura curves is new. Possible overlap with specialized tables of quaternionic Hasse invariants or unindexed calculations remains a literature risk. The finite checker does not constitute independent scientific validation.

## References

1. J. Laga and A. Shnidman, *The geometry and arithmetic of bielliptic Picard curves*, arXiv:2308.15297 (first public version, 2023-08-29), https://arxiv.org/abs/2308.15297.
2. J. Laga and A. Shnidman, *Ceresa cycles of bielliptic Picard curves*, arXiv:2312.12965 (2023-12-20), https://arxiv.org/abs/2312.12965.
3. A. Kazemifard and S. Tafazolian, *A note on some Picard curves over finite fields*, *Finite Fields and Their Applications* **34** (2015), 107--122, https://doi.org/10.1016/j.ffa.2014.12.002.
4. Y. Terakado, J. Xue and C.-F. Yu, *Superspecial Points on Shimura Curves*, arXiv:2608.16036 (2026-08-17), https://arxiv.org/abs/2608.16036.
