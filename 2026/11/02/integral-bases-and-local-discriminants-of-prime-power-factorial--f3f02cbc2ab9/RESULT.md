# Integral bases and local discriminants of prime-power factorial-Hadamard polynomials

## Finding
Let \(p\) be an odd prime, \(a\ge1\), \(n=p^a\), \(h=(n-1)/(p-1)\), and \(2\le r\le p-1\). Put \(s=rh\) and
\[
P_{n,r}(X)=\sum_{k=0}^{n}\left(\frac{n!}{k!}\right)^r X^k\in\mathbb Z[X].
\]
Then \(P_{n,r}\) is irreducible over \(\mathbb Q_p\), hence over \(\mathbb Q\). If \(\alpha\) is any root, \(K=\mathbb Q_p(\alpha)\) is totally ramified of degree \(n\), with \(\nu_p(\alpha)=s/n\). The exact local integral basis is
\[
\mathcal O_K=\bigoplus_{j=0}^{n-1}\mathbb Z_p\frac{\alpha^j}{p^{\lfloor js/n\rfloor}}.
\]
The index and discriminants satisfy
\[
\nu_p([\mathcal O_K:\mathbb Z_p[\alpha]])=\frac{(n-1)(s-1)}2,\qquad
\nu_p(\operatorname{Disc}(P_{n,r}))=ns,\qquad
\nu_p(\operatorname{Disc}(K/\mathbb Q_p))=n+s-1.
\]
For fixed \(p,a\), the \(p-2\) choices \(2\le r\le p-1\) therefore yield pairwise nonisomorphic degree-\(p^a\) totally ramified local fields: their discriminant exponents are distinct.

## Assumptions and scope
The valuation \(\nu_p\) is normalized by \(\nu_p(p)=1\), including its extension to an algebraic closure of \(\mathbb Q_p\). The ring \(\mathcal O_K\) is the valuation ring of \(K\). The polynomial is monic and integral because every quotient \(n!/k!\) is an integer. Its coefficients are the \(r\)-th Hadamard powers of the factorial-ratio coefficient sequence for truncated exponential polynomials; they also enumerate \(r\) independent ordered injective lists of \(n-k\) selected labels. All statements are for odd prime \(p\), prime-power degree \(n\), and the specified exponents \(r\).

## Proof
**1. One Newton edge and irreducibility.** Legendre's factorial valuation formula and the base-\(p\) digit sum \(s_p(k)\) give
\[
\nu_p(k!)=\frac{k-s_p(k)}{p-1},\qquad \nu_p(n!)=h,
\]
with \(h\equiv1\pmod p\). For the coefficient \(c_k=(n!/k!)^r\),
\[
\nu_p(c_k)-s\left(1-\frac{k}{n}\right)
=\frac{r}{p-1}\left(s_p(k)-\frac{k}{n}\right)>0
\quad(0<k<n).
\]
Indeed \(s_p(k)\ge1\) and \(k<n\). The lower Newton polygon thus consists of the single edge from \((0,s)\) to \((n,0)\). As \(\gcd(s,n)=1\) (because \(p\nmid h\) and \(r<p\)), every root has valuation \(s/n\), in lowest terms with denominator \(n\). Consequently the local degree of any root is at least \(n\), proving irreducibility and total ramification.

**2. Complete local integral basis.** For \(0\le j<n\), define \(b_j=\alpha^j/p^{\lfloor js/n\rfloor}\). Then
\[
\nu_p(b_j)=\left\{\frac{js}{n}\right\}\in[0,1),
\]
and these \(n\) valuations have different fractional parts because \(\gcd(s,n)=1\). If \(z=\sum_{j=0}^{n-1}u_jb_j\), with \(u_j\in\mathbb Q_p\), the valuations of nonzero summands are pairwise distinct: their fractional parts differ. Hence no cancellation is possible at the minimum, and \(z\) is integral precisely when each \(u_j\in\mathbb Z_p\). The \(b_j\) therefore form an integral basis. Comparing them with the ordinary power basis gives
\[
\nu_p([\mathcal O_K:\mathbb Z_p[\alpha]])
=\sum_{j=0}^{n-1}\left\lfloor\frac{js}{n}\right\rfloor
=\frac{(n-1)(s-1)}2,
\]
using the permutation of the nonzero residues \(js\pmod n\).

**3. A unique lowest term of the derivative.** Differentiating,
\[
P'_{n,r}(\alpha)=\sum_{k=1}^n k c_k\alpha^{k-1}.
\]
The \(k=1\) term has valuation \(s\). For \(2\le k\le n\), the valuation difference from the \(k=1\) term is
\[
\Delta_k=\nu_p(k)+\frac r{p-1}\left(s_p(k)-1-\frac{k-1}{n}\right).
\]
If \(s_p(k)\ge2\), then \(\Delta_k>0\) since \((k-1)/n<1\). Otherwise \(k=p^j\) for some \(j\ge1\); in that case
\[
\Delta_k=j-\frac{r(k-1)}{n(p-1)}>j-1\ge0,
\]
strictly, because \(r\le p-1\) and \(k\le n\). Thus \(k=1\) uniquely minimizes valuation, so \(\nu_p(P'_{n,r}(\alpha))=s\).

**4. Discriminants and distinct local fields.** For a monic separable degree-\(n\) polynomial, the discriminant equals \((-1)^{n(n-1)/2}\operatorname{Norm}_{K/\mathbb Q_p}(P'_{n,r}(\alpha))\). Since \(K/\mathbb Q_p\) has degree \(n\), the norm has valuation \(ns\). The discriminant-index formula yields
\[
\nu_p(\operatorname{Disc}(K/\mathbb Q_p))
=ns-2\frac{(n-1)(s-1)}2=n+s-1.
\]
For fixed \(p,a\), this exponent increases by the positive integer \(h\) when \(r\) increases by one, distinguishing the resulting fields.

## Verification
A standalone Python 3 script `verify.py` constructs the polynomials directly from integer factorials. For eight triples \((p,a,r)\), it checks all coefficient valuations and strict Newton inequalities, all derivative-term valuations, the predicted power-basis index, and the polynomial discriminant by an independent exact fraction-free Sylvester determinant. The executed program reports:

`VERIFY_OK cases=8 exact_resultant_discriminants=8 coefficient_checks=56 derivative_competitor_checks=40`

These finite computations corroborate the formulas; the proof above establishes all admissible infinitely many triples.

## Relationship to prior work
The factorial-ratio coefficients are related to truncated exponential and derangement polynomials, which Sun, Wu and Zhuang (arXiv:1009.2929v1, 2010) study mainly through congruences. Jindal and Khanduja (2024) study discriminants and integral bases of ordinary exponential Taylor polynomials; this is substantial coverage of the *unpowered* case \(r=1\), deliberately excluded here. Jakhar (2025) examines local ramification and monogenicity for exponential Taylor polynomials with coefficients of the form \(n!a_k/k!\) where the multipliers satisfy unit conditions; those conditions do not hold for these factorial-power coefficients when \(r\ge2\). The above local integral-basis and exact discriminant classifications for coefficientwise powers \(2\le r\le p-1\) are not immediate statements of these inspected results. Equivalent coverage in other literature remains possible; the 2024 article was available for abstract-level, not full-text, comparison.

## Limitations
The result gives only the \(p\)-local integral basis and discriminant exponent, not the global integral basis, discriminant at other primes, global Galois group, or full classification beyond \(r\le p-1\) and prime-power degrees. Search and comparison cannot establish absolute novelty; an inaccessible closely related article remains a residual risk. 
## References
1. Zhi-Wei Sun, Wei-Feng Wu, Hai-Xia Zhuang, *Congruences on the Bell polynomials and the derangement polynomials* (arXiv:1009.2929v1, publicly posted 2010-09-15).
2. A. Jindal and S. Khanduja, *Discriminant and integral basis of number fields defined by exponential Taylor polynomials* (2024), DOI: 10.1017/S0013091524000105.
3. A. Jakhar, *Nonmonogenity of number fields defined by truncated exponential polynomials* (2025), DOI: 10.1017/S0004972724000819.
