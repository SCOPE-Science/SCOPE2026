# Quadratic growth of the first even Catalan residue stratum

## Finding

Let \(C_n=\frac{1}{n+1}\binom{2n}{n}\) be the ordinary Catalan sequence and let \(\nu_2\) denote the exponent of two in a nonzero integer. For every \(b\ge0\) and \(r\ge1\), write
\[
A_{b,r}=C_{2^b(2^r+1)-1}.
\]
Every Catalan number with valuation exactly one occurs uniquely in this two-parameter family. Put
\[
R_1(k)=\#\{C_n\bmod 2^k:\ n\ge0,\ \nu_2(C_n)=1\}.
\]

**Theorem.** The adjacent differences have the exact valuations
\[
\nu_2(A_{b,r+1}-A_{b,r})=r+1\quad(b\ge0,r\ge1),
\qquad
\nu_2(A_{b+1,r}-A_{b,r})=b+2\quad(b\ge1,r\ge1).
\]
For every integer \(k\ge4\), with \(t=\lfloor (k-2)/2\rfloor\),
\[
\boxed{\ t(k-2-t)\ \le\ R_1(k)\ \le\ (k-1)^2\ }.
\]
Consequently \(R_1(k)=\Theta(k^2)\). The lower estimate is explicitly \(\lfloor (k-2)^2/4\rfloor\). For fixed \(b\), the \(A_{b,r}\) attain exactly \(k-1\) distinct residues modulo \(2^k\) as \(r\) varies, whenever \(k\ge2\).

## Assumptions and scope

All indices and residue moduli are integers. We use the binary digit sum \(s_2(n)\), the ordinary integer binomial coefficient, and congruences between odd rational numbers interpreted in the localized ring \(\mathbb Z_{(2)}\). The valuation of a nonzero rational number is defined by the difference of numerator and denominator valuations. No statement here concerns Catalan values with valuation two or greater, or the exact formula for \(R_1(k)\).

## Proof

**1. Identifying the first even stratum.** For every \(n\ge1\),
\[
C_{n-1}=\frac{1}{2(2n-1)}\binom{2n}{n},
\qquad \nu_2\left(\binom{2n}{n}\right)=s_2(n).
\]
The second equality follows from Legendre's formula or the binary carry count. Hence \(\nu_2(C_{n-1})=s_2(n)-1\). Exact valuation one means that the binary expansion of \(n\) has exactly two ones. Its unique representation is \(n=2^{b+r}+2^b\) with \(b\ge0,r\ge1\).

**2. Differences in the gap coordinate.** Define the odd integers
\[
H_j=\frac12\binom{2^{j+1}}{2^j}\quad(j\ge0),
\qquad D(n)=\frac14\binom{2n}{n}
\]
for integers \(n\) of binary digit sum two. Let \(m=2^a\), \(\ell=2^b\), \(a=b+r>b\), and \(n=m+\ell\). The factorial identity
\[
D(n)=H_a H_b Q_{a,b},\quad
Q_{a,b}=\frac{\binom{2m+2\ell}{2\ell}}{\binom{m+\ell}{\ell}^{2}}
\]
is exact. Put \(E=\binom{m+\ell}{\ell}\) and \(E'=\binom{2m+2\ell}{2\ell}\). The product formula
\[
\binom{M+L}{L}=\prod_{j=1}^{L}\left(1+\frac Mj\right)
\]
shows that \(E\equiv 1+2^r\pmod{2^{r+1}}\): only the endpoint \(j=2^b\) contributes modulo \(2^{r+1}\), and all preceding factors are one at that precision. Applying the same argument to \(E'\) with \(M=2^{a+1},L=2^{b+1}\) yields \(E'\equiv1+2^r\pmod{2^{r+1}}\). Since \(E^2\equiv1\pmod{2^{r+1}}\), we obtain
\[
Q_{a,b}\equiv1+2^r\pmod{2^{r+1}},\qquad
Q_{a+1,b}\equiv1\pmod{2^{r+1}}.
\]
On the other hand, iterating the same product formula through the even factors gives
\[
\frac{H_{a+1}}{H_a}=
\prod_{\substack{1\le j<2^{a+1}\\j\ \mathrm{odd}}}
\left(1+\frac{2^{a+1}}j\right)
\equiv1\pmod{2^{a+1}}.
\]
Because \(a+1\ge r+1\), the products for \(D(2^{a+1}+2^b)\) and \(D(2^a+2^b)\) differ by an odd multiple of \(2^r\) modulo \(2^{r+1}\). Thus
\[
\nu_2\bigl(D(2^{a+1}+2^b)-D(2^a+2^b)\bigr)=r.
\]
Using \(A_{b,r}=2D(n)/(2n-1)\), the change in the odd denominator contributes a term of valuation at least \(a+2\), whereas the change in \(D\), after multiplication by two, has valuation \(r+1\). Since \(a+2\ge r+2\), no cancellation is possible. This proves the first asserted valuation, including \(b=0\).

**3. Differences in the scale coordinate.** Let \(n=2^b(2^r+1)\), where \(b\ge1\). Binary digit sum is unchanged by doubling, so the central-binomial quotient satisfies
\[
\frac{D(2n)}{D(n)}=
\prod_{\substack{1\le j<2n\\j\ \mathrm{odd}}}
\left(1+\frac{2n}{j}\right).
\]
There are exactly \(n\) factors, an even number. The sum of their odd reciprocal denominators is therefore even modulo two. As \(\nu_2(2n)=b+1\), the linear term in the product is divisible by \(2^{b+2}\); all terms of degree at least two are divisible by \(2^{2b+2}\), also by \(2^{b+2}\). Consequently
\[
D(2n)\equiv D(n)\pmod{2^{b+2}}.
\]
Now compare \(A_{b+1,r}=2D(2n)/(4n-1)\) and \(A_{b,r}=2D(n)/(2n-1)\). The contribution of the displayed difference in \(D\) has valuation at least \(b+3\), while
\[
2D(n)\left(\frac1{4n-1}-\frac1{2n-1}\right)
=\frac{-4nD(n)}{(4n-1)(2n-1)}
\]
has valuation exactly \(b+2\). Hence the second asserted valuation holds.

**4. Finite cutoff and upper bound.** Adjacent horizontal differences have strictly increasing valuations \(r+1\). Thus values with fixed \(b\) are pairwise distinct for \(1\le r\le k-1\), and every \(r\ge k-1\) gives the same residue as \(r=k-1\), modulo \(2^k\). Similarly, for fixed \(r\), all \(b\ge k-2\) give the same residue as \(b=k-2\), provided \(k\ge3\). The case \(b=0\) is kept as a separate branch. Therefore all first-even residues modulo \(2^k\) are represented by the rectangular set \(0\le b\le k-2\), \(1\le r\le k-1\), giving the bound \(R_1(k)\le(k-1)^2\).

**5. Quadratic injection.** For fixed \(b\), telescoping differences in \(r\) have distinct valuations, so if \(r<r'\), then \(\nu_2(A_{b,r'}-A_{b,r})=r+1\). Likewise, for fixed \(r\) and \(1\le b<b'\), \(\nu_2(A_{b',r}-A_{b,r})=b+2\). Put \(t=\lfloor(k-2)/2\rfloor\) and restrict to
\[
1\le r\le t,\qquad t\le b\le k-3.
\]
This rectangle has \(t(k-2-t)\) pairs. Distinct pairs with equal \(r\) have vertical difference valuation at most \(k-1\), and distinct pairs with equal \(b\) have horizontal difference valuation at most \(t+1<k\). When both coordinates differ, traverse first horizontally and then vertically: the horizontal difference has valuation at most \(t+1\), whereas the vertical difference has valuation at least \(t+2\). Thus they cannot cancel; the resulting difference has valuation less than \(k\). All pairs produce distinct residues modulo \(2^k\), proving the lower bound and \(\Theta(k^2)\).

## Verification

The accompanying standalone `verify_catalan.py` evaluates the odd parts of factorials exactly modulo \(2^{16}\), independently checks 36 terms using integer binomial coefficients, checks 144 horizontal and 132 vertical differences, and compares complete clipped residue sets for every \(3\le k\le12\). The observed residue counts for those exponents are \(2,4,7,13,21,33,46,63,81,102\). These finite computations corroborate the theorem; its universal quantifiers are established by the proof above.

## Relationship to prior work

Lin's work determines the odd Catalan residues modulo \(2^k\) and explicitly proposes studying even residues of fixed two-adic valuation. Liu and Yeh derived general binary-run truncations and classifications for small powers of two. Xin and Xu's Theorems 8 and 9 give a strong truncation principle and distinctness along a fixed odd-factor dilation family; in particular, the upper bound here is compatible with, and can also be obtained in spirit from, their reductions. The new point is a **transverse, exact valuation law in the binary-gap coordinate** and the resulting joint injective rectangle proving quadratic, rather than merely linear, growth of the first even valuation stratum. Rowland and Yassawi's finite automata compute Catalan residues at fixed precision, but the inspected Catalan section does not state this uniform quadratic lower bound. The relation to these results was checked at the level of implications, not just titles. An equivalent derivation in older, differently indexed congruence literature cannot be excluded.

## Limitations

The bounds do not give an exact formula for \(R_1(k)\) or its leading asymptotic coefficient. They cover only valuation exactly one, not all even Catalan residues. Their historical priority requires further expert scrutiny, especially for consequences of the general binary-run classifications. No result about the natural density of indices producing each residue is asserted.

## References

- H.-Y. Lin, *The odd Catalan numbers modulo powers of two*, arXiv:1012.1756 (first posted 2010-12-08), especially Section 5, https://arxiv.org/abs/1012.1756 .
- G. Xin and J.-F. Xu, *A short approach to Catalan numbers modulo powers of two*, Electronic Journal of Combinatorics **18** (2011), P177, Theorems 8–9, https://doi.org/10.37236/664 .
- S.-C. Liu and J. C.-C. Yeh, *Catalan Numbers Modulo Powers of Two*, Journal of Integer Sequences **13** (2010), Article 10.5.4, Theorems 5.2–5.3, https://cs.uwaterloo.ca/journals/JIS/VOL13/Liu2/liu6.html .
- E. Rowland and R. Yassawi, *Automatic congruences for diagonals of rational functions*, arXiv:1310.8635 (2013), Section 3.1, https://arxiv.org/abs/1310.8635 .
