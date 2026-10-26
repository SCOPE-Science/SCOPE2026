# Complete Cartier-iterate ranks for prime-power Hurwitz curves

## Finding
Let \(k\) be algebraically closed of characteristic \(p\), where \(p\) is any prime, and choose an integer \(e\ge1\). Put \(q=p^e\) and \(T=p(p+1)/2\). Consider the smooth projective Hurwitz curve
\[
C:\quad X^{q+1}Y+Y^{q+1}Z+Z^{q+1}X=0.
\]
For the \(p^{-1}\)-linear Cartier operator \(\mathcal C:H^0(C,\Omega_C^1)\to H^0(C,\Omega_C^1)\), define \(\rho_r=\dim_k\operatorname{im}(\mathcal C^r)\), with \(\rho_0=g(C)\). Then for every integer \(0\le r\le e\),
\[
\boxed{\rho_r=T^r\frac{p^{e-r}(p^{e-r}+1)}2.}
\]
For every \(r\ge e\), \(\rho_r=T^e\). In fact \(\rho_{e-1}=\rho_e=T^e\), so the image filtration stabilizes at \(e-1\). Consequently the Jacobian has
\[
\boxed{\gamma(C)=\left(\frac{p(p+1)}2\right)^e}
\]
for its \(p\)-rank. The multiplicity of nilpotent strings of length \(j\ge1\) in the Cartier monomial transition is exactly \(\rho_{j-1}-2\rho_j+\rho_{j+1}\), with all terms understood via the stabilized rank formula. There are no nilpotent strings when \(e=1\); for \(e\ge2\) the longest has length exactly \(e-1\). This is a complete rank-profile classification, not an assertion of a full Ekedahl–Oort classification.

## Assumptions and scope
The equation is considered over the algebraic closure of the prime field. Here \(q\) denotes \(p^e\), not an independently varying field size. The genus is \(g=q(q+1)/2\), because this is a smooth plane curve of degree \(q+2\). Smoothness also follows from the standard Hurwitz criterion: with \(n=q+1\), one has \(n^2-n+1=q^2+q+1\equiv1\pmod p\). The claim covers all primes, including characteristic two, and all positive exponents. The operator is semilinear; each rank is taken as the dimension of its \(k\)-linear image, not the rank of an incorrectly untwisted matrix product.

## Proof
**1. Canonical basis and a monomial Cartier transition.** On \(Z=1\) the equation is \(F=x^{q+1}y+y^{q+1}+x\). The usual canonical-adjoint basis on a smooth plane curve consists of
\[
\omega_{i,j}=\frac{x^iy^j\,dx}{F_y},\qquad i,j\in\mathbf Z_{\ge0},\quad i+j\le q-1.
\]
There are \(q(q+1)/2\) such pairs. The Stöhr–Voloch Cartier formula extracts those terms of \(F^{p-1}x^iy^j\) for which both variable exponents are congruent to \(p-1\) modulo \(p\), subtracts \(p-1\) from each exponent, divides each by \(p\), and takes the \(p\)-th root of the coefficient. Write
\[
F^{p-1}=\sum_{A+B+D=p-1}\binom{p-1}{A,B,D}
 (x^{q+1}y)^A(y^{q+1})^B x^D.
\]
For a chosen basis pair write \(i=pI+b\), \(j=pJ+c\), with \(0\le b,c<p\). The two exponent congruences force \(B=b\), \(D=c\), and \(A=p-1-b-c\). This term exists precisely when \(b+c\le p-1\). In that case its multinomial coefficient is nonzero modulo \(p\) (all factorial arguments are strictly less than \(p\)), and
\[
\mathcal C(\omega_{i,j})
 =\lambda_{b,c}\,\omega_{\,I+p^{e-1}(p-1-b-c),\;J+p^{e-1}b},
\quad\lambda_{b,c}\in\mathbb F_p^\times.
\]
Otherwise \(\mathcal C(\omega_{i,j})=0\). Writing \(Q=p^{e-1}\), the source inequality gives \(I+J\le Q-1\), and the target index sum is at most \(I+J+Q(p-1-c)\le pQ-1=q-1\); hence the target lies in the displayed basis. Because its highest base-\(p\) digits recover \((p-1-b-c,b)\), and its other digits recover \((I,J)\), two different nonzero source columns cannot have the same target. Thus this is an injective **partial monomial permutation**, also under every iterate; there can be no cancellation of distinct surviving basis images.

**2. Exact survival criterion.** Expand \(i=\sum_{h=0}^{e-1}b_hp^h\) and \(j=\sum_{h=0}^{e-1}c_hp^h\). On a nonzero Cartier step the digit pair \((b_0,c_0)\) is deleted from the low end; the remaining digit pairs shift down one position; and the new top pair is \((p-1-b_0-c_0,b_0)\). The new top pair is automatically no-carry because its sum is \(p-1-c_0\). Therefore, for every \(0\le r\le e\), the iterate \(\mathcal C^r(\omega_{i,j})\) is nonzero if and only if
\[
b_h+c_h\le p-1\qquad\text{for all }0\le h<r.
\]
Once all original digit positions have been checked, new top pairs stay no-carry forever, so surviving vectors remain on permutation cycles. Since every nonzero transition is injective, \(\rho_r\) is exactly the number of pairs obeying this condition.

**3. Enumeration without extrapolation.** There are exactly \(T=p(p+1)/2\) possibilities for each admissible digit pair. Write \(i=p^r I+u\) and \(j=p^r J+v\). The no-carry condition on their lowest \(r\) digits implies \(u+v\le p^r-1\), while \(i+j\le p^e-1\) then holds exactly when \(I+J\le p^{e-r}-1\). Thus the lower digits contribute \(T^r\) independent choices and the two high parts contribute \(p^{e-r}(p^{e-r}+1)/2\) choices. This proves the formula for all \(0\le r\le e\); beyond this point every surviving vector remains nonzero. As \(\rho_{e-1}=T^{e-1}p(p+1)/2=T^e\), stabilization already occurs at \(e-1\).

**4. Consequences.** The standard Hasse–Witt identification gives \(\gamma(C)=\operatorname{rank}\mathcal C^r\) for all sufficiently large \(r\), hence the stated \(p\)-rank. Differences \(d_j=\rho_{j-1}-\rho_j\) count nilpotent strings of length at least \(j\), and the second differences \(d_j-d_{j+1}\) give the stated exact multiplicities; these are intrinsic rank-sequence invariants. When \(e\ge2\), \(\rho_{e-2}>\rho_{e-1}\), so the maximal string length is exactly \(e-1\). For \(e=1\), \(\rho_0=\rho_1=g\) and the curve is ordinary.

## Verification
The accompanying file `hurwitz_cartier_checker.py` enumerates the canonical basis independently for small prime powers, expands the full trinomial \(F^{p-1}\) coefficient-by-coefficient modulo \(p\), reconstructs every Cartier column without assuming the asserted digit map, and compares exact image sets for all iterates with the claimed formulas. It checks \(p\in\{2,3,5,7,11\}\) and multiple exponents, including \((p,e)=(3,4)\) and \((5,3)\). It checks that the single-step rank agrees with the published \(a\)-number, that all nonzero targets are distinct, and that nilpotent string counts are nonnegative and have the correct total size. The script reports `VERIFY_OK`. This finite computation independently tests but does not replace the proof for all primes and exponents.

For example, \((p,e)=(3,3)\) gives genus \(378\), iterated ranks \(378,270,216,216,\ldots\), \(p\)-rank \(216\), and exactly \(54\) nilpotent strings of length one and \(54\) of length two. The previously known \(a\)-number is \(108\), corresponding to the first rank drop.

## Relationship to prior work
Montanucci–Speziali, *The a-numbers of Fermat and Hurwitz curves* (2016 preprint, arXiv:1603.03604), Theorem 4.1 and Proposition 4.6, derive the **one-step Cartier rank** for general Hurwitz degree \(n\); their Theorem 4.7 establishes the \(a\)-number when \(n=sp+1\). Setting \(s=p^{e-1}\) recovers our \(r=1\) value but does **not** determine the higher iterates, stabilized image, or nilpotent-string lengths. These known one-step facts are not presented here as new. Dawson and collaborators, *The Supersingularity of Hurwitz Curves* (arXiv:1810.01582), classify supersingularity using a congruence modulo \(n^2-n+1\); their result concerns the Newton polygon rather than the exact Cartier-iterate rank profile. Borges–Gonçalves, *The p-rank of curves of Fermat type* (arXiv:2212.03987), give general formulas for Fermat-type curves; the cover by a Fermat curve does not by itself give the iterated Cartier ranks of its Hurwitz quotient.

## Limitations
The formula addresses the \(p\)-rank and Cartier filtration but does not determine the full Newton polygon, canonical principal polarization, or complete Ekedahl–Oort type. For \(e=1\) the profile is the already familiar ordinary case; the substantive new filtration begins at \(e\ge3\). A logically equivalent classification could appear in more specialized historical studies not located by available searching. The verification code tests finitely many primes and exponents; the proof is the symbolic digit argument above.

## References
1. M. Montanucci and P. Speziali, *The a-numbers of Fermat and Hurwitz curves*, arXiv:1603.03604v1 (first posted 2016-03-11), §2 and §4, especially Theorem 4.1, Proposition 4.6 and Theorem 4.7. https://arxiv.org/abs/1603.03604
2. E. Dawson et al., *The Supersingularity of Hurwitz Curves*, arXiv:1810.01582 (2018 preprint), §2 and main theorem. https://arxiv.org/abs/1810.01582
3. H. Borges and C. Gonçalves, *The p-rank of curves of Fermat type*, arXiv:2212.03987 (2022 preprint), Theorem 1.1 and §3. https://arxiv.org/abs/2212.03987
