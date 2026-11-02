# Sharp dyadic index shifts and least periods of central Delannoy numbers

## Finding

For every integer \(n\ge 0\), define the central Delannoy number
\[
D_n=\sum_{j=0}^n2^j\binom nj^2.
\]
For each positive integer \(h\) divisible by \(4\), let \(a=\nu_2(h)\) (so \(a\ge2\)). The exact first dyadic shift layer is
\[
\boxed{D_{n+h}-D_n\equiv 2^{a+2}\left(n+\binom n2\right)\pmod{2^{a+3}}.}
\]
In particular, \(\nu_2(D_{n+h}-D_n)=a+2\) for \(n\equiv1,2\pmod4\), whereas \(2^{a+3}\mid D_{n+h}-D_n\) for \(n\equiv0,3\pmod4\). All quantifiers are uniform: this is true for every eligible \(h,n\), not merely for shifts that are powers of two.

Let \(P_k\) denote the least positive period of the infinite sequence \((D_n\bmod 2^k)_{n\ge0}\). Then
\[
\boxed{P_1=1,\qquad P_2=2,\qquad P_3=4,\qquad P_k=2^{k-2}\quad(k\ge4).}
\]
The period is a least *global* period: \(D_{n+P_k}\equiv D_n\pmod{2^k}\) for every \(n\ge0\), and no smaller positive integer has that property.

## Assumptions and scope

All indices and binomial coefficients are ordinary nonnegative integers. We take \(\binom nr=0\) when \(r<0\) or \(r>n\). The valuation \(\nu_2\) is applied to nonzero differences in the exact-valuation clauses, and \(\nu_2(h)\) is well-defined because \(h>0\). No limiting argument in \(n\) or restriction to prime-power shifts is assumed. The identity \(D_n=P_n(3)\), with \(P_n\) the Legendre polynomial, is a standard alternative formulation.

## Proof

**1. Binomial representation and the shift expansion.** The bivariate generating function for lattice paths with east, north, and northeast steps is
\[
\frac1{1-u-v-uv}=\frac1{(1-u)(1-v)}\sum_{j\ge0}\left(\frac{2uv}{(1-u)(1-v)}\right)^j.
\]
Extracting the coefficient of \(u^nv^n\) gives the displayed formula for \(D_n\). For every \(h\ge0\), Vandermonde's identity gives
\[
\binom{n+h}j=\sum_{i\ge0}\binom hi\binom n{j-i}.
\]
Thus the shift difference, with all sums finite, is
\[
\Delta_{n,h}:=D_{n+h}-D_n
=\sum_{j\ge0}2^j\!\!\sum_{\substack{i,\ell\ge0\\ (i,\ell)\ne(0,0)}}
\binom hi\binom h\ell\binom n{j-i}\binom n{j-\ell}.
\tag{1}
\]

**2. Terms with exactly one positive index.** For \(1\le i\le h\), the elementary identity \(\binom hi=(h/i)\binom{h-1}{i-1}\) implies
\[
\nu_2\!\left(\binom hi\right)\ge a-\nu_2(i).
\tag{2}
\]
The two symmetric parts of (1) having one index zero sum to
\[
2\sum_{j\ge0}2^j\binom nj\sum_{i=1}^j\binom hi\binom n{j-i}.
\tag{3}
\]
The summand at \((j,i)\) has valuation at least \(a+1+j-\nu_2(i)\). Since \(j\ge i\ge1\), the only possibilities where \(j-\nu_2(i)<2\) are \((j,i)=(1,1),(2,2)\); indeed \(i-\nu_2(i)\ge2\) for every \(i\ge3\). Hence modulo \(2^{a+3}\), expression (3) is precisely
\[
4h\,n+8\binom h2\binom n2
=4h\left(n+(h-1)\binom n2\right).
\tag{4}
\]

**3. Terms with two positive indices.** Every term of (1) with \(i,\ell\ge1\) has valuation at least
\[
j+2a-\nu_2(i)-\nu_2(\ell)\ge2a,
\tag{5}
\]
because \(j\ge\max(i,\ell)\) and \(\nu_2(r)\le r/2\) for every positive integer \(r\). When \(a\ge3\), inequality (5) makes all such terms zero modulo \(2^{a+3}\).

For \(a=2\), we must work modulo \(32\). Equality in the second inequality of (5) requires \(i=\ell=j\) and \(\nu_2(i)=i/2\). The only positive integers satisfying the latter equality are \(i=2\) and \(i=4\). Thus all two-positive terms are multiples of \(32\), except possibly
\[
4\binom h2^2\quad\text{and}\quad16\binom h4^2.
\]
Since \(\nu_2(h)=2\), \(\nu_2\binom h2=1\), and \(\binom h4\) is odd by the binary-digit form of Lucas's theorem. Each displayed expression is congruent to \(16\pmod{32}\); together they sum to zero. This exceptional cancellation establishes the same conclusion for \(a=2\).

**4. Uniform shift phase.** Combining (1)–(4), the double-positive cancellation, and \(h=2^a u\) for odd \(u\) gives
\[
\Delta_{n,h}\equiv4h\left(n+(h-1)\binom n2\right)
\equiv2^{a+2}\left(n+\binom n2\right)\pmod{2^{a+3}}.
\]
The integer \(n+\binom n2=n(n+1)/2\) is odd exactly when \(n\equiv1,2\pmod4\), proving the sharp/nonsharp clauses.

**5. Exact least periods.** Every \(D_n\) is odd, so \(P_1=1\). Reducing the defining sum modulo \(4\) gives \(D_n\equiv1+2n\pmod4\), so \(P_2=2\). The uniform phase with \(h=4\) shows that \(4\) is a period modulo \(16\), hence also modulo \(8\). Since \(D_0=1\) and \(D_2=13\not\equiv1\pmod8\), neither residue sequence can have period \(1\) or \(2\). A period of \(3\) together with period \(4\) would force period \(1\) by the gcd-of-periods property. Therefore \(P_3=P_4=4\).

For \(k\ge5\), set \(h=2^{k-2}\). The phase congruence implies that \(h\) is a period modulo \(2^k\). Its half \(h/2=2^{k-3}\) is not a period: at \(n=1\), its shift difference has valuation precisely \(k-1\). If some positive \(d<h\) were a period, then \(\gcd(d,h)\), being a common period of a periodic infinite sequence, would also be a period. Because \(h\) is a power of two, \(\gcd(d,h)\mid h/2\), forcing \(h/2\) to be a period, a contradiction. Thus \(P_k=h\). This completes the proof.

## Verification

An independently implemented integer recurrence
\[
nD_n=3(2n-1)D_{n-1}-(n-1)D_{n-2}\quad(n\ge2),
\qquad D_0=1,\;D_1=3
\]
computes the test values without using the shift identity. The included standalone script `delannoy_period_verifier.py` checks the binomial formula against that recurrence for the first \(161\) indices, then checks \(197504\) dyadic shifts and \(98688\) exact-valuation instances, as well as all predicted periods and all shorter candidate shifts for moduli \(2,4,\ldots,2048\). It executes with `python3 delannoy_period_verifier.py` and requires only Python's standard library. The finite checks corroborate, but do not replace, the proof for unbounded \(n,h,k\).

## Relationship to prior work

The central Delannoy sequence and its recurrence are standard (OEIS A001850). Z.-W. Sun's *Congruences involving generalized central trinomial coefficients* (arXiv:1008.3887, publicly available 2010-08-23) identifies this sequence with generalized central trinomial coefficients \(T_n(3,2)\) and proves congruences involving sums of their terms. Sun's *On Delannoy numbers and Schröder numbers* (arXiv:1009.2486, first public 2010-09-13) focuses mainly on odd-prime sums. Guo's *Some congruences involving powers of Delannoy polynomials* (arXiv:1412.7724, 2014-12-10) studies weighted polynomial-power sums modulo odd prime powers. The general power-of-two recurrence methodology of Kauers, Krattenthaler, and Müller (arXiv:1107.2015) is acknowledged; the specific all-index shift phase and closed least-period law do not appear in the examined discussions. None of these comparisons disputes the established Delannoy identities or any previously known general congruence method.

The claimed contribution is narrowly the uniform \(2\)-adic first-shift layer and its consequence for *least* periods, not the defining binomial formula, recurrence, or basic eventual modular periodicity. Related statements could exist under the alternative Legendre polynomial or generalized central trinomial formulations. The literature comparison is bounded and does not prove absolute novelty.

## Limitations

The result is confined to central Delannoy numbers and moduli that are powers of two. It does not classify all higher dyadic layers for \(n\equiv0,3\pmod4\), arbitrary generalized central trinomial coefficients, odd-prime periods, or off-diagonal Delannoy numbers. The exact valuation for the two odd-phase residue classes is proved only for shifts divisible by four. Some potentially relevant older or specialized works were not fully accessible and historical priority needs independent verification.

## References

- Zhi-Wei Sun, *Congruences involving generalized central trinomial coefficients*, arXiv:1008.3887v1 (2010-08-23), https://arxiv.org/abs/1008.3887 .
- Zhi-Wei Sun, *On Delannoy numbers and Schröder numbers*, arXiv:1009.2486v1 (2010-09-13), https://arxiv.org/abs/1009.2486 .
- Manuel Kauers, Christian Krattenthaler, Thomas W. Müller, *A method for determining the mod-\(2^k\) behaviour of recursive sequences*, arXiv:1107.2015v1 (2011-07-11), https://arxiv.org/abs/1107.2015 .
- Victor J. W. Guo, *Some congruences involving powers of Delannoy polynomials*, arXiv:1412.7724v1 (2014-12-10), https://arxiv.org/abs/1412.7724 .
- OEIS A001850, *Central Delannoy numbers*, https://oeis.org/A001850 .
