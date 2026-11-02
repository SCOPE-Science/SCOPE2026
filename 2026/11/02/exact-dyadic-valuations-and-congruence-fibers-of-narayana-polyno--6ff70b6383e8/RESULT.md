# Exact dyadic valuations and congruence fibers of Narayana polynomials

## Finding
For every positive integer \(n\), let
\[
N_n(X)=\sum_{j=1}^{n}\frac{1}{n}\binom nj\binom n{j-1}X^j\in\mathbb Z[X].
\]
Write \(s_2(t)\) for the binary digit sum of a nonnegative integer, \(\nu_2\) for the two-adic valuation, and \(\nu_2(0)=+\infty\). **The exact valuation for every integer \(x\)** is
\[
\nu_2(N_n(x))=
\begin{cases}
\nu_2(x),&x\equiv0\pmod2,\\
s_2(m+1)-1,&x\equiv1\pmod2,\quad n=2m+1,\\
\nu_2(x+1)+s_2(m)-1,&x\equiv1\pmod2,\quad n=2m.
\end{cases}
\]
The second branch has \(m\ge0\) and the third \(m\ge1\). In particular, if \(n\) is odd the valuation is constant across all odd inputs; if \(n\) is even, the valuation of odd inputs is controlled *exactly* by the distance to \(-1\).

The formulas also determine every power-of-two congruence fiber. Fix \(1\le r\le k\) and count the residue classes \(x\pmod{2^k}\) for which \(N_n(x)\equiv0\pmod{2^r}\). For odd \(n\), putting \(h=s_2((n+1)/2)-1\), the number is
\[
2^{k-r}+\mathbf1_{\{r\le h\}}2^{k-1}.
\]
For even \(n\), putting \(h=s_2(n/2)-1\), the number is
\[
2^{k-r}+2^{k-\max(1,r-h)}.
\]
Consequently, the complete zero sets in the two-adic integers are \(\{0\}\) when \(n\) is odd and \(\{0,-1\}\) when \(n\) is even.

## Assumptions and scope
The index \(n\ge1\), weight \(x\in\mathbb Z\), and moduli \(2^r\) are unrestricted except as stated. Divisibility and equality at the zeros are understood using \(\nu_2(0)=+\infty\). The polynomial has integer coefficients because its coefficients enumerate Narayana objects. All statements also hold for \(x\in\mathbb Z_2\) by polynomial continuity and valuation continuity, with \(s_2\) evaluated only on the finite integer indices.

## Proof
The classical Coker gamma expansion, recorded as equation (1.1) by Mansour and Sun and **not claimed here as new**, is
\[
\frac{N_n(X)}{X}
=\sum_{j=0}^{\lfloor(n-1)/2\rfloor}\binom{n-1}{2j}C_j X^j(1+X)^{n-1-2j},
\qquad C_j=\frac{1}{j+1}\binom{2j}{j}.
\]
Legendre's formula gives the exact Catalan valuation
\[
\nu_2(C_j)=s_2(j+1)-1.
\]
For every \(a,b\ge0\), the binary-carry inequality \(s_2(a+b)\le s_2(a)+s_2(b)\) holds. In particular, for every integer \(r\ge1\),
\[
2r-s_2(r)\ge1.
\]
If \(x\) is even, the gamma expansion evaluated at \(x\) is odd: the term \(j=0\) reduces to \(1\pmod2\), while every term \(j\ge1\) contains an even power of \(x\). Therefore \(\nu_2(N_n(x))=\nu_2(x)\), also at \(x=0\) with the infinite-valuation convention.

Suppose \(x\) is odd and \(n=2m+1\). The endpoint summand in the gamma expansion occurs at \(j=m\), equals \(C_mx^m\), and has valuation \(h=s_2(m+1)-1\). For any other index write \(r=m-j\ge1\). Because \(m+1=(j+1)+r\), one has
\[
\nu_2(C_j)+2r=s_2(j+1)-1+2r\ge h+2r-s_2(r)>h.
\]
The factor \((1+x)^{2r}\) has valuation at least \(2r\) since \(x\) is odd, and all other factors are integers. The endpoint is thus uniquely of minimal valuation, so no cancellation is possible. Multiplication by the odd input \(x\) does not affect valuation. This proves the odd-index branch even for \(m=0\).

If \(x\) is odd and \(n=2m\), divide the gamma expansion by the integral factor \(1+X\):
\[
\frac{N_{2m}(X)}{X(1+X)}
=\sum_{j=0}^{m-1}\binom{2m-1}{2j}C_jX^j(1+X)^{2(m-1-j)}.
\]
The endpoint \(j=m-1\) is \((2m-1)C_{m-1}x^{m-1}\), which has valuation \(h=s_2(m)-1\), since \(2m-1\) is odd. For any other term set \(r=m-1-j\ge1\), so \(m=(j+1)+r\) and the same strict bound \(\nu_2(C_j)+2r>h\) holds. Thus the quotient has valuation exactly \(h\). Multiplying by \(x(1+x)\) yields the even-index branch whenever \(x\ne-1\). At \(x=-1\), the gamma expansion itself proves \(N_{2m}(-1)=0\), so the convention establishes the formula there too.

For the fiber counts, an even residue satisfies the congruence precisely when \(2^r\mid x\), giving \(2^{k-r}\) classes in either parity case. If \(n\) is odd, either every odd residue qualifies (when \(r\le h\)), or none does. If \(n\) is even, odd \(x\) qualifies just when \(\nu_2(x+1)\ge r-h\). When \(r-h\le1\) every odd residue qualifies; otherwise the single condition \(x\equiv-1\pmod{2^{r-h}}\) selects exactly \(2^{k-(r-h)}\) classes. Because \(r\le k\) and \(h\ge0\), all counts make sense. Letting \(r\) tend to infinity establishes the claimed zeros in \(\mathbb Z_2\).

## Verification
The attached standalone standard-library program `verify.py` evaluates the defining binomial sum and the independently coded gamma expansion and checks the valuation formula for \(1\le n\le36\) and \(-26\le x\le26\). This gives 1,908 direct/gamma/valuation comparisons. For \(1\le n\le24\), \(1\le k\le8\), and \(1\le r\le k\), it also exhaustively checks all \(2^k\) residues in each of 864 complete congruence-fiber tests. Run `python verify.py`. Finite tests corroborate rather than establish the theorem; the infinite proof is the preceding unique-minimum valuation argument.

## Relationship to prior work
Mansour and Sun (arXiv:0805.1274v1, 2008) reproduce the Coker expansion used above and give specializations at \(x=-1\), including vanishing for even indices. Postnikov and Sagan (arXiv:math/0601339, 2006) prove a general equality of valuations for weighted Catalan numbers satisfying difference constraints; their height-of-ascent weights differ from the number-of-peaks weight underlying the Narayana polynomial. Gao and Gu (arXiv:1908.03914, 2019) broaden that weighted-Catalan framework. Lassalle (arXiv:1112.0156) relates Narayana polynomials to symmetric functions, while Checcoli and D'Adderio (arXiv:1306.5929) study perfect powers of individual Narayana coefficients. The contributions asserted here are the **uniform valuation trichotomy over integer weights, all prime-power congruence fibers, and complete two-adic zero sets**, not the pre-existing gamma identity, Catalan valuation, or \(x=-1\) evaluations.

## Limitations
The classification addresses the prime two, ordinary type-A Narayana polynomials with exponents beginning at one, and integer or two-adic inputs. No analogous assertion is made for other primes, nonintegral rational inputs, or q-deformed Narayana families. The proof uses published identities and elementary valuation estimates, so an equivalent unlocated consequence in broader literature is a residual originality risk. Independent review is not claimed.

## References
1. A. Postnikov and B. E. Sagan, *What power of two divides a weighted Catalan number?*, arXiv:math/0601339v1 (first posted 2006-01-13), https://arxiv.org/abs/math/0601339.
2. T. Mansour and Y. Sun, *Identities involving Narayana polynomials and Catalan numbers*, arXiv:0805.1274v1 (first posted 2008-05-09), equation (1.1), https://arxiv.org/html/0805.1274v1.
3. M. Lassalle, *Narayana polynomials and Hall-Littlewood symmetric functions*, arXiv:1112.0156 (2011), https://arxiv.org/html/1112.0156v2.
4. S. Checcoli and M. D'Adderio, *Perfect powers in Catalan and Narayana numbers*, arXiv:1306.5929 (2013), https://arxiv.org/html/1306.5929v1.
5. Y. Gao and A. Gu, *Arithmetic of weighted Catalan numbers*, arXiv:1908.03914 (2019), https://arxiv.org/pdf/1908.03914.
