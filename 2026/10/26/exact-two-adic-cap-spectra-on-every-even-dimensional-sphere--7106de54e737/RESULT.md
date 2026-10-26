# Exact two-adic cap spectra on every even-dimensional sphere

## Finding
For every integer \(k\ge1\), let \(\mathbb S^{2k}\subset\mathbb R^{2k+1}\) have probability surface measure. Fix a rational cutoff \(c=p/q\) in lowest terms with \(-1<c<1\), \(q>0\) even, and set \(s=\nu_2(q)\ge1\). Define the normalized moving-cap averaging operator
\[
 (\mathcal A_{k,c}f)(\xi)=\frac{\int_{\mathbb S^{2k}}\mathbf1_{\{\xi\cdot\eta\ge c\}}f(\eta)\,d\sigma(\eta)}{\int_{\mathbb S^{2k}}\mathbf1_{\{\xi\cdot\eta\ge c\}}\,d\sigma(\eta)}.
\]
This operator has a rational scalar eigenvalue \(\Lambda_\ell(k,c)\) on every spherical-harmonic degree \(\ell\ge0\), and the exact two-adic valuation is
\[
 \boxed{\nu_2(\Lambda_\ell(k,c))=-\ell s-\nu_2\!\left(\frac{(\ell+2k-1)!}{(2k-2)!}\right).}
\]
Here \(\nu_2(a/b)\) is the exponent of \(2\) in any nonzero rational number \(a/b\); \(\Lambda_0=1\) satisfies the displayed formula. In particular **every harmonic eigenvalue is nonzero**. Hence \(\mathcal A_{k,c}\) is injective on complex \(L^2(\mathbb S^{2k})\) for every indicated \(k,c\), and the same conclusion holds on continuous functions. The collection of eligible cutoffs is dense in \((-1,1)\). The operator is compact, so its inverse on the range is unbounded; the claim is uniqueness, not stable unrestricted inversion.

The formula determines the *exact power of two in the reduced denominator* of each nonconstant multiplier, independently of the numerator \(p\). For the ordinary two-sphere \(k=1\), it reads \(\nu_2(\Lambda_\ell)=-\ell s-\nu_2((\ell+1)!)\).

## Assumptions and scope
The dimension \(2k\) is even and at least two. The cutoff is a rational \(p/q\) in lowest terms, with an even positive denominator and with \(-1<p/q<1\); thus \(p\) is odd. Every degree \(\ell\) is a nonnegative integer. \(\nu_2\) is only applied to explicitly nonzero rational numbers. Spherical harmonics are the eigenspaces of the Laplace--Beltrami operator on the full sphere. All averaging uses probability surface measure, but the normalization of surface area cancels in the multiplier ratio. The cap boundary has measure zero and may be included or omitted. No assertion is made for odd-dimensional spheres or for rational cutoffs of odd denominator.

## Proof
Set \(\alpha=k-\tfrac12\) and
\[
 B_k(c)=\int_c^1(1-t^2)^{k-1}\,dt>0.
\]
The Funk--Hecke formula diagonalizes \(\mathcal A_{k,c}\) on the degree-\(\ell\) spherical harmonics and gives
\[
 \Lambda_\ell(k,c)=\frac{\int_c^1 C_\ell^\alpha(t)(1-t^2)^{k-1}\,dt}{C_\ell^\alpha(1)B_k(c)},
 \qquad C_\ell^\alpha(1)=\binom{\ell+2k-2}{\ell}.
\]
Thus \(\Lambda_0=1\). For \(\ell\ge1\), differentiating the Gegenbauer Rodrigues relation yields
\[
 \frac{d}{dt}\left((1-t^2)^k C_{\ell-1}^{k+1/2}(t)\right)
 =-\frac{\ell(\ell+2k-1)}{2k-1}(1-t^2)^{k-1}C_\ell^{k-1/2}(t).
\]
The upper endpoint term vanishes. Consequently
\[
 \Lambda_\ell(k,c)=
 \frac{(2k-1)(1-c^2)^k C_{\ell-1}^{k+1/2}(c)}{\ell(\ell+2k-1)\binom{\ell+2k-2}{\ell} B_k(c)}. \tag{1}
\]

We establish the nonstandard arithmetic input explicitly. Write \(m=\ell-1\) and \(\beta=k+\tfrac12\). The polynomial \(C_m^\beta(x)\) has leading coefficient
\[
 L_m=\frac{\prod_{r=0}^{m-1}(2k+2r+1)}{m!},
 \qquad \nu_2(L_m)=-\nu_2(m!),
\]
with the empty product equal to \(1\). From the ordinary Gegenbauer coefficient formula, the ratio of the coefficient at \(x^{m-2j}\) to \(L_m\), for \(0\le j\le\lfloor m/2\rfloor\), is
\[
 (-1)^j\binom m{2j}\frac{(2j-1)!!}{\prod_{r=m-j}^{m-1}(2k+2r+1)}. \tag{2}
\]
All factors in the denominator of (2) are odd, so its two-adic valuation is nonnegative. Because \(\nu_2(p/q)=-s\), the leading term at \(c\) has two-adic valuation \(-\nu_2(m!)-ms\), whereas the term indexed by \(j\ge1\) has valuation at least \(-\nu_2(m!)-(m-2j)s\), strictly larger. A sum with a unique term of least two-adic valuation has that term's valuation. Therefore
\[
 \nu_2(C_m^{k+1/2}(c))=-\nu_2(m!)-ms,
 \tag{3}
\]
which proves that this Gegenbauer value is nonzero for *every* \(m,k\) in scope.

Next, the finite expansion
\[
 B_k(c)=\sum_{j=0}^{k-1}(-1)^j\binom{k-1}{j}\frac{1-c^{2j+1}}{2j+1}
\]
has a unique term of smallest two-adic valuation: the negative \(c^{2k-1}\) contribution at \(j=k-1\). Its valuation is \(-(2k-1)s\); all terms with lower powers of \(c\), as well as all constant terms, have greater valuation. Hence
\[
 \nu_2(B_k(c))=-(2k-1)s. \tag{4}
\]
Since \(q\) is even and \(p\) odd, \(q^2-p^2\) is odd, giving \(\nu_2(1-c^2)=-2s\). Apply valuations to (1), use (3)--(4), and note \(\nu_2(2k-1)=0\). The sum simplifies to
\[
 \begin{aligned}
 \nu_2(\Lambda_\ell)
 &=-\ell s-\nu_2\left((\ell-1)!\,\ell(\ell+2k-1)\binom{\ell+2k-2}{\ell}\right)\\
 &=-\ell s-\nu_2\left(\frac{(\ell+2k-1)!}{(2k-2)!}\right),\qquad \ell\ge1.
 \end{aligned}
\]
For \(\ell=0\), the proposed valuation is \(-\nu_2(2k-1)=0\), matching \(\Lambda_0=1\). This completes the exact formula and the no-zero assertion for all degrees.

Spherical harmonics of different degrees form a complete orthogonal basis of \(L^2(\mathbb S^{2k})\). Every spectral multiplier is nonzero, so \(\mathcal A_{k,c}f=0\) implies every harmonic coefficient of \(f\) is zero, proving injectivity. Continuous functions embed in \(L^2\), so the same holds there. Dyadic rational numbers in \((-1,1)\), when written in lowest terms, have even denominators unless they are integers; they supply a dense eligible subfamily. Finally the bounded cap indicator is a square-integrable kernel on the product of two compact spheres, hence \(\mathcal A_{k,c}\) is Hilbert--Schmidt and compact. A compact injective operator on the infinite-dimensional \(L^2\) space cannot have a bounded inverse on its image.

## Verification
The standalone \(check.py\) uses exact symbolic integration and rational arithmetic, independently comparing the Funk--Hecke integral and the closed Gegenbauer multiplier. It verifies the full valuation identity for dimensions \(2,4,6,8,10\), seven reduced rational cutoffs of even denominator, and all degrees \(0\) through \(18\). It also checks (3) for every positive degree tested and (4) for all tested cutoffs. The recorded output is in \(check_output.txt\). The analytical coefficient argument, not this finite sample, proves the infinite-degree and all-dimensional statements.

## Relationship to prior work
The spherical-harmonic completeness, addition theorem, and Funk--Hecke formula are classical and are developed in Frye and Efthimiou, *Spherical Harmonics in p Dimensions*, arXiv:1205.3548v1 (2012), particularly Chapter 4. These furnish the familiar diagonalization, not the arithmetic valuation formula above. Jahn and Bokor, *Revisiting the concentration problem of vector fields within a spherical cap* (arXiv:1302.5261v1, 2013), study fixed-cap energy concentration for bandlimited vector fields and commuting differential operators, not the moving-cap convolution multiplier in every degree or its rational valuation. Campi, Gardner, Gronchi, and Kiderlen, *Lightness functions* (2012), discuss spherical-cap geometry and cosine transforms in convex-geometric inverse problems; accessible introductory material does not state (1)--(4), but its full text could not be inspected.

The contribution asserted here is the exact \(2\)-adic spectral law and the resulting explicit dense family of all-degree injective moving-cap transforms on even-dimensional spheres. No general novelty claim is made for Funk--Hecke, the standard Gegenbauer identities, or spectral completeness.

## Limitations
The result does not classify all rational or irrational cutoffs, nor all odd-dimensional spheres. It gives an exact arithmetic valuation, **not** a useful numerical lower bound for real singular values; indeed unrestricted inversion is unbounded. A classical theorem on the rational zeros or prime-adic Newton polygons of half-integer Gegenbauer polynomials might subsume the arithmetic lemma even without mentioning caps; priority for that algebraic formulation remains a literature risk. The full text of a relevant geometric-tomography article was not accessible for statement-by-statement comparison, although its accessible description concerns a distinct problem. No independent audit is claimed.

## References
1. C. Frye and C. J. Efthimiou, *Spherical Harmonics in p Dimensions*, arXiv:1205.3548v1, first public 2012-05-16, especially §4.3 and Theorem 4.24. https://arxiv.org/html/1205.3548v1
2. K. Jahn and N. Bokor, *Revisiting the concentration problem of vector fields within a spherical cap: a commuting differential operator solution*, arXiv:1302.5261v1, 2013. https://arxiv.org/abs/1302.5261
3. S. Campi, R. J. Gardner, P. Gronchi and M. Kiderlen, *Lightness functions*, Advances in Mathematics 231 (2012), 3118–3146. DOI:10.1016/j.aim.2012.08.015 (full text not inspected).
4. NIST Digital Library of Mathematical Functions, Chapter 18 (Gegenbauer polynomials and classical orthogonal polynomials). https://dlmf.nist.gov/18
