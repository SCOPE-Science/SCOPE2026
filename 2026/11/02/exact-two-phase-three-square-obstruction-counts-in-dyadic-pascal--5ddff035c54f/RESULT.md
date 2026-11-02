# Exact two-phase three-square obstruction counts in dyadic Pascal rows

## Finding
For an integer \(r\ge1\), let \(E_r\) be the number of indices \(0\le k\le 2^r\) for which the binomial coefficient \(\binom{2^r}{k}\) is **not** a sum of three integer squares. Then
\[
E_1=E_2=0,\qquad E_3=E_4=2,
\]
and for every \(r\ge5\),
\[
\boxed{E_r=\frac{2^{2\lfloor r/2\rfloor-1}+10}{3}.}
\]
In particular, the proportion of such coefficients among the \(2^r+1\) coefficients of the row tends to \(1/6\) as \(r\to\infty\) through even integers and to \(1/12\) as \(r\to\infty\) through odd integers. Therefore these proportions do **not** converge along all dyadic rows.

There is also an exact classification of all obstructed positions. For every \(r\ge3\), every interior index \(1\le k<2^r\), and \(t=\nu_2(k)\), \(u=k/2^t\), \(q=\lfloor(k-1)/2^{r-2}\rfloor\), put
\[
(W_0,W_1,W_2,W_3)=(1,5,3,7).
\]
Then \(\binom{2^r}{k}\) is not a sum of three squares if and only if
\[
\boxed{r-t\equiv0\pmod2\quad\text{and}\quad (-1)^{k-1}uW_q\equiv7\pmod8.}
\]
Neither endpoint coefficient is obstructed.

## Assumptions and scope
All indices and coefficients are ordinary nonnegative integers; the three squares may include zeros. The theorem covers *every* dyadic row of index \(2^r\), and makes no assertion for general top indices. The three-square obstruction criterion is Legendre's classical theorem: an integer \(n\ge0\) fails to be a sum of three squares precisely when \(n=4^a(8b+7)\) for some nonnegative integers \(a,b\). We use \(\nu_2\) for the usual two-adic valuation of a positive integer.

## Proof
**Step 1: The odd part of a dyadic binomial coefficient.** Put \(N=2^r\). For any \(1\le k<N\), with \(t=\nu_2(k)\) and \(u=k/2^t\), the identity
\[
\binom Nk=\frac{N}{k}\binom{N-1}{k-1}
\]
implies \(\nu_2\bigl(\binom Nk\bigr)=r-t\), since \(\binom{N-1}{j}\) is odd for every \(0\le j<N\). The latter parity assertion follows either from Lucas's binomial parity theorem or directly from the next product.

For \(0\le j<N\), in the ring of two-adic integers (where each \(i\) divides \(N\) in the two-adic sense),
\[
\binom{N-1}{j}=(-1)^j\prod_{i=1}^{j}\left(1-\frac{N}{i}\right).
\]
Every factor is odd. For \(r\ge3\), the factor is \(1\pmod8\) unless \(\nu_2(i)\ge r-2\). Precisely three values \(1\le i<N\) meet that condition: \(2^{r-2}\), \(2^{r-1}\), and \(3\cdot2^{r-2}\). Their factors are respectively \(5,7,5\pmod8\). Thus, with \(q=\lfloor j/2^{r-2}\rfloor\),
\[
\binom{N-1}{j}\equiv(-1)^j W_q\pmod8,
\qquad (W_0,W_1,W_2,W_3)=(1,5,3,7).
\]
Taking \(j=k-1\) and dividing the coefficient by its exact power of two gives
\[
2^{-(r-t)}\binom Nk=\frac1u\binom{N-1}{k-1}
\equiv u(-1)^{k-1} W_q\pmod8,
\]
because the inverse of every odd integer modulo \(8\) equals itself.

**Step 2: Classification.** Legendre's theorem applied to that exact valuation and odd residue gives the two displayed necessary and sufficient congruences. For \(k=0,N\), the coefficient is \(1\), which is representable.

**Step 3: Counting.** For each \(t\) satisfying \(0\le t\le r-5\) and \(t\equiv r\pmod2\), indices with \(\nu_2(k)=t\) contribute exactly \(2^{r-t-3}\) obstructions. Indeed each of the four quarters \(q=0,1,2,3\) contains \(2^{r-t-3}\) eligible odd values of \(u\), and among their four possible residues \(1,3,5,7\pmod8\) exactly one satisfies the single odd-part congruence; hence there are \(2^{r-t-5}\) per quarter. (This gives \(4\cdot2^{r-t-5}=2^{r-t-3}\) in total.) This holds also for \(t=0\): the sign \((-1)^{k-1}\) is then positive throughout, and for \(t>0\) it is negative throughout.

For \(r\ge5\), the remaining allowable valuations are \(t=r-4\) and \(t=r-2\). At \(t=r-4\), the odd values \(1\le u\le15\) contributing are exactly \(u=1,5,11,15\), hence four obstructions. At \(t=r-2\), both \(u=1\) and \(u=3\) contribute, hence two further obstructions. Thus
\[
E_r=6+\sum_{\substack{0\le t\le r-5\\t\equiv r\ (2)}}2^{r-t-3}.
\]
The geometric sum equals \((2^{r-1}-8)/3\) for even \(r\ge6\) and \((2^{r-2}-8)/3\) for odd \(r\ge5\), yielding the asserted closed form. For \(r=3,4\), direct use of Step 2 gives two obstructions in each row; for \(r=1,2\), direct inspection gives none.

**Step 4: Limits.** Dividing the exact even and odd formulas by \(2^r+1\) gives the two distinct subsequential limits, completing the proof.

## Verification
The companion stand-alone Python 3 program `verify_dyadic_binomial_three_squares.py` checks every integer binomial coefficient in each row \(1\le r\le13\), comparing the three-square obstruction of its *actual integer value* with the residue classification; this covers \(16{,}395\) coefficient entries. It separately checks the residue classification and closed-form counts for \(14\le r\le20\), covering \(2{,}080{,}761\) interior positions. No symbolic result is inferred from finite tests; Steps 1–4 prove the infinite assertion.

## Relationship to prior work
Granville and Zhu (1990) investigated representability of binomial coefficients by sums of squares, proving in particular existence results for non-three-square coefficients and asymptotics for central coefficients. Moshe (2004/2005) analyzed the global Pascal-triangle counting problem posed there, while Mincu and Panaitopol (2010) studied runs of representable consecutive binomial coefficients. Burns (2022) developed related applications of Legendre's theorem to factorials. The *exact obstruction count at every dyadic row* and its alternating limiting densities are the distinct claims here; those global, central-coefficient, run-length, and factorial statements do not directly imply this formula. The Moshe and Mincu--Panaitopol full texts were not available for complete comparison, so possible implicit coverage remains an originality risk.

## Limitations
This is a dyadic-index theorem, not an enumeration of every row. The verifier cannot certify infinitely many rows, and the literature comparison does not prove priority over unpublished, unindexed, or inaccessible work. The entire proof is given above, but independent mathematical audit has not been performed.

## References
1. A. Granville and Y. Zhu, *Representing Binomial Coefficients as Sums of Squares*, American Mathematical Monthly 97 (1990), 486–493, https://www.dms.umontreal.ca/~andrew/PDF/YZhu.pdf.
2. Y. Moshe, *On a Problem of Granville and Zhu Regarding Pascal's Triangle*, Mathematika 51 (2004/05), 63–82, DOI: 10.1112/S0025579300015515.
3. G. Mincu and L. Panaitopol, *Writing Binomial Coefficients as Sums of Three Squares*, Archiv der Mathematik 95 (2010), 401–409, DOI: 10.1007/s00013-010-0182-5.
4. R. Burns, *Factorials and Legendre's Three-Square Theorem: II*, arXiv:2203.16469v1, first publicly posted 2022-03-30, https://arxiv.org/abs/2203.16469.
