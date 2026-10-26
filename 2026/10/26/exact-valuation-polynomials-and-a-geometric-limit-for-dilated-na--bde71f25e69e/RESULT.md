# Exact valuation polynomials and a geometric limit for dilated Narayana rows

## Finding

The valuation profile of each Narayana-triangle row whose index is a prime-power dilation of an integer coprime to that prime has a finite closed form and a rational bivariate generating function. The normalized valuation deficiency has a limiting, explicitly shifted geometric distribution, with an exponential total-variation error bound.

Let \(p\) be any prime, \(m\ge1\) an integer with \(p\nmid m\), and \(r\ge1\). Put \(P=p^r\), \(n=mP\), and define the integer Narayana numbers by
\[
N(n,k)=\frac{1}{n}\binom nk\binom n{k+1}\qquad(0\le k<n).
\]
The convention is \(\nu_p(1)=0\). For \(0\le b\le m\) and \(0\le b<m\), respectively, set
\[
g_b=\nu_p\binom mb,\qquad h_b=\nu_p\binom{m-1}{b}.
\]
Define integer polynomials
\[
B_{p,m}(u)=\sum_{b=0}^{m-1}\left(u^{g_b+h_b}+u^{g_{b+1}+h_b}\right),\qquad
H_{p,m}(u)=\sum_{b=0}^{m-1}u^{2h_b}.
\]
For every \(r\ge1\), the complete valuation-distribution polynomial is exactly
\[
\boxed{\sum_{k=0}^{mp^r-1}u^{\nu_p(N(mp^r,k))}= B_{p,m}(u)+H_{p,m}(u)\left((p-2)p^{r-1}u^r+2(p-1)\sum_{j=1}^{r-1}p^{j-1}u^j\right).}
\]
The inner sum is empty when \(r=1\). Equivalently, as an identity of formal power series in \(z\),
\[
\boxed{\sum_{r\ge1}\left(\sum_{k=0}^{mp^r-1}u^{\nu_p(N(mp^r,k))}\right)z^r=
\frac{B_{p,m}(u)z}{1-z}+\frac{H_{p,m}(u)uz((p-2)+pz)}{(1-z)(1-puz)}.}
\]

There is also a quantitative limit law. Let \(K_r\) be uniform on \(\{0,1,\ldots,mp^r-1\}\), and put \(W_r=r-\nu_p(N(mp^r,K_r))\). Independently choose \(B\) uniformly in \(\{0,\ldots,m-1\}\) and a nonnegative integer-valued \(J\) with
\[
\Pr(J=0)=\frac{p-2}{p},\qquad
\Pr(J=j)=\frac{2(p-1)}{p^{j+1}}\quad(j\ge1).
\]
Then
\[
\boxed{d_{\mathrm{TV}}\bigl(\mathcal L(W_r),\mathcal L(J-2h_B)\bigr)\le 2p^{-r}.}
\]
This includes \(p=2\), when \(\Pr(J=0)=0\), and includes possibly negative values of the shifted limit. No asymptotic condition on \(m\) is needed: it remains fixed as \(r\to\infty\).

A nontrivial illustrative family is \(m=p+1\), where
\[
H_{p,p+1}(u)=2+(p-1)u^2,\qquad B_{p,p+1}(u)=4+2u+2(p-2)u^2.
\]
Here the limiting law is a mixture: with probability \(2/(p+1)\) it is \(J\), and with probability \((p-1)/(p+1)\) it is \(J-2\). This demonstrates that the multiplier can change the limit, even though the geometric tail is universal.

## Assumptions and scope

All primes \(p\), every positive integer \(m\) with \(\gcd(p,m)=1\), and all exponents \(r\ge1\) are included; there is no parity restriction and no bound on the row index or the coefficient \(k\). The valuations are ordinary valuations of positive integers. The formula is an exact finite-row equality, not an asymptotic approximation. The limit keeps \(p,m\) fixed. The notation \(d_{\mathrm{TV}}\) denotes supremum of probability differences over subsets of the integers.

## Proof

**1. Prime-power block lemma.** Write every \(0\le k<mP\) uniquely as \(k=bP+t\), where \(0\le b<m\) and \(0\le t<P\). Let \(s_p(a)\) be the sum of base-\(p\) digits of \(a\). For \(1\le t<P\), digit complementation gives
\[
s_p(t)+s_p(P-t)=(p-1)(r-\nu_p(t))+1.
\]
Because \(p\nmid m\), decrementing \(m\) to \(m-1\) decreases its base-\(p\) digit sum by one. Legendre's digit-sum formula, together with
\[
(mP)-(bP+t)=(m-b-1)P+(P-t),
\]
therefore yields, for every \(0\le b<m\) and \(1\le t<P\),
\[
\nu_p\binom{mP}{bP+t}=r-\nu_p(t)+\nu_p\binom{m-1}{b}=r-\nu_p(t)+h_b.
\]
At a block boundary the base-\(p\) digits simply shift, giving
\[
\nu_p\binom{mP}{bP}=\nu_p\binom mb=g_b\qquad(0\le b\le m).
\]
These statements also hold for the endpoints \(b=0\) and \(b=m-1\).

**2. Valuation of each Narayana entry.** Subtracting \(\nu_p(mP)=r\) from the sum of the two adjacent binomial valuations produces exactly three cases:
\[
\nu_p(N(mP,bP+t))=
\begin{cases}
g_b+h_b,&t=0,\\
r-\nu_p(t(t+1))+2h_b,&1\le t\le P-2,\\
h_b+g_{b+1},&t=P-1.
\end{cases}
\]
For \(P=2\) the interior range is empty. The boundary assertions use \(k+1=bP+1\) at the left endpoint and \(k+1=(b+1)P\) at the right endpoint. Thus the total boundary contribution is precisely \(B_{p,m}(u)\), and each interior block has the common multiplier \(u^{2h_b}\).

**3. Counting interior valuation shells.** Among integers \(1\le t\le p^r-2\), the two consecutive integers \(t,t+1\) cannot both be divisible by \(p\). There are exactly \((p-2)p^{r-1}\) with \(\nu_p(t(t+1))=0\). For each \(1\le d\le r-1\), there are exactly \(2(p-1)p^{r-d-1}\) with \(\nu_p(t(t+1))=d\): they are the classes where precisely one of \(t\) and \(t+1\) has exact valuation \(d\). Substituting \(j=r-d\) yields the interior polynomial
\[
T_{p,r}(u)=(p-2)p^{r-1}u^r+2(p-1)\sum_{j=1}^{r-1}p^{j-1}u^j.
\]
Summing the boundary and interior contributions proves the exact polynomial formula. Summing \(T_{p,r}(u)z^r\) over \(r\ge1\) gives
\[
\sum_{r\ge1}T_{p,r}(u)z^r=\frac{uz((p-2)+pz)}{(1-z)(1-puz)},
\]
which proves the rational bivariate identity. As an elementary normalization check, \(B_{p,m}(1)=2m\), \(H_{p,m}(1)=m\), and \(T_{p,r}(1)=p^r-2\); the row contains exactly \(mp^r\) entries.

**4. Limit law and explicit rate.** Let \(Z\) be a uniformly distributed \(p\)-adic integer and let \(T\) be its residue in \(\{0,\ldots,p^r-1\}\). Choose the block index \(B\) independently and uniformly. Then \(BP+T\) is uniform on the required row. Away from the two residue classes \(T\in\{0,P-1\}\), the valuation in Step 2 satisfies
\[
W_r=\nu_p(T(T+1))-2h_B=\nu_p(Z(Z+1))-2h_B.
\]
The first equality uses that \(\nu_p(T(T+1))<r\) away from these classes. The probability of the excluded residue classes is exactly \(2/p^r\). For Haar-uniform \(Z\), the valuations \(\nu_p(Z)\) and \(\nu_p(Z+1)\) cannot both be positive. Their sum \(J=\nu_p(Z(Z+1))\) consequently has the displayed distribution, since for \(j\ge1\) the probability that exactly one factor has valuation \(j\) is \(2(p-1)/p^{j+1}\). The coupling inequality bounds total variation by the probability \(2p^{-r}\) of a mismatch and proves the limit.

**5. Nontrivial multiplier example.** For \(m=p+1\), the binomial row \(\binom p b\) has valuation one for \(1\le b\le p-1\), and zero at the endpoints. Likewise \(\nu_p\binom{p+1}{b}\) is one exactly for \(2\le b\le p-1\). Inserting these into the definitions of \(B,H\) gives the two example polynomials and the two-component shifted limit.

## Verification

Run \(\texttt{python3 verify.py}\) with Python 3 standard library. It constructs each Narayana number independently from exact binomial coefficients and compares complete \(p\)-adic valuation histograms with the closed formula. Cases cover primes \(2,3,5,7\), multipliers \(1\le m\le27\) coprime to \(p\), exponents \(1\le r\le4\), and row sizes at most \(700\): \(202\) independently computed rows. It also checks the row-size normalization and several named examples. The finite checks support the exact identities; the unbounded and probabilistic conclusions follow from the proof above.

## Relationship to prior work

Bóna and Sagan (2005), *On divisibility of Narayana numbers by primes*, characterize when a Narayana entry is divisible by a given prime, based on Kummer's carry theorem. They explicitly point toward the more difficult problem of understanding full prime-power orders. Their general divisibility test and Kummer's theorem are essential inputs but do not supply this row-histogram polynomial, its rational generating function, or the limiting shifted geometric mixture.

Checcoli and D'Adderio (2013), *Perfect powers in Catalan and Narayana numbers*, analyze perfect-power restrictions and use \(p\)-adic information when the Narayana row index is a prime power. This includes relevant valuation bounds for the special case \(m=1\); that special case is not claimed as new. The present result treats every multiplier coprime to \(p\), exactly enumerates all valuations and detects the nontrivial carry mixture. Standard Kummer and Legendre formulas are invoked as established facts.

OEIS A001263 tabulates Narayana entries, not the stated uniform prime-power-dilation valuation profiles or quantitative limit law. Results about \(p\)-adic valuations of the *Narayana cow sequence* concern a distinct recurrence and do not cover these Catalan/Narayana-triangle numbers. No assertion is made that the published general theorems are false.

## Limitations

The multiplier is required to be coprime to \(p\). The joint limit is for each fixed \(m,p\), not a uniform limit as \(m\to\infty\). The polynomial counts valuations, not residues modulo higher powers of \(p\). Its derivation is elementary once Kummer's theorem is available; independently locating equivalent formulas or implicit earlier treatments remains a meaningful literature risk. No claim of independent external validation is made.

## References

1. M. Bóna and B. E. Sagan, *On divisibility of Narayana numbers by primes*, arXiv:math/0505382, first posted 2005-05-18, published in *Journal of Integer Sequences* 8 (2005), Article 05.2.4.
2. S. Checcoli and M. D'Adderio, *Perfect powers in Catalan and Narayana numbers*, arXiv:1306.5929, first posted 2013-06-25.
3. OEIS A001263, Narayana triangle (integer sequence reference).
4. E. Kummer, theorem on the prime valuation of binomial coefficients (classical result); A.-M. Legendre, factorial valuation formula (classical result).
