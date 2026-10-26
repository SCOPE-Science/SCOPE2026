# Sharpness of the binary-digit divisibility bound for Franel numbers

## Finding

Let \(F_n=\sum_{k=0}^{n}\binom nk^3\) for every integer \(n\ge0\), let \(s_2(n)\) be the number of ones in the binary expansion of \(n\), and let \(a_2(n)\) count adjacent pairs of ones (overlapping pairs counted separately). Then
\[
F_n\equiv 2^{s_2(n)} 2^{a_2(n)}\pmod{2^{s_2(n)+1}}.
\]
Consequently,
\[
\nu_2(F_n)=s_2(n)\quad\Longleftrightarrow\quad a_2(n)=0.
\]
In particular, Calkin's known divisibility bound \(2^{s_2(n)}\mid F_n\) is sharp precisely at the Fibbinary indices, whose binary expansions have no consecutive ones. For every integer \(L\ge1\), exactly \(\operatorname{Fib}(L+2)-1\) positive indices below \(2^L\) give equality (with \(\operatorname{Fib}(0)=0\), \(\operatorname{Fib}(1)=1\)). Thus the equality indices have natural density zero.

## Assumptions and scope

The index \(n\) ranges over all nonnegative integers. Define \(\nu_2(x)\) for every positive integer \(x\) as the exponent of \(2\) in \(x\). Set \(s_2(0)=a_2(0)=0\). If the binary digits of \(n\) are \(n_i\in\{0,1\}\), then \(a_2(n)=\sum_{i\ge0}n_i n_{i+1}\). A congruence modulo \(2^{s_2(n)+1}\) is asserted, not an exact formula for \(\nu_2(F_n)\) in the strict-inequality cases.

## Proof

**Step 1: an integral decomposition.** A classical identity of Strehl gives
\[
F_n=\sum_{k=0}^{n}\binom nk^{\!2}\binom{2k}{n}.
\]
Put \(j=n-k\); terms with \(2k<n\) vanish. Using factorial cancellation,
\[
\binom n{n-j}^{\!2}\binom{2(n-j)}n
=\binom n{2j}\binom{2j}j\binom{2(n-j)}{n-j}.
\]
It follows that
\[
F_n=\sum_{j=0}^{\lfloor n/2\rfloor}
\binom n{2j}\binom{2j}j\binom{2(n-j)}{n-j}.\tag{1}
\]

**Step 2: termwise valuation.** Legendre's factorial formula implies
\(\nu_2\!\binom{2u}{u}=s_2(u)\) for every \(u\ge0\). The valuation of the summand indexed by \(j\) in (1) is therefore
\[
\nu_2\!\binom n{2j}+s_2(j)+s_2(n-j)\ge s_2(n),\tag{2}
\]
because binary digit sums are subadditive: \(s_2(j)+s_2(n-j)\ge s_2(n)\). Equality in (2) holds if and only if both (i) adding \(j\) to \(n-j\) involves no carries and (ii) \(\binom n{2j}\) is odd. The first condition is equivalent to each set bit of \(j\) also being a set bit of \(n\). Lucas's theorem modulo two shows that (ii) holds if and only if each set bit of \(2j\) is a set bit of \(n\).

**Step 3: exact parity.** Thus the summands whose valuation equals \(s_2(n)\) correspond exactly to subsets of the set of binary positions \(i\) for which \(n_i=n_{i+1}=1\). Every such position may independently be present or absent in \(j\), giving precisely \(2^{a_2(n)}\) minimum-valuation summands. All other summands are divisible by \(2^{s_2(n)+1}\). After division by \(2^{s_2(n)}\), each minimum-valuation summand is odd. Their sum hence has parity \(2^{a_2(n)}\bmod2\). Multiplying back proves the displayed congruence and the sharpness equivalence.

**Step 4: counting.** The count of binary words of length \(L\) without adjacent ones obeys the Fibonacci recurrence with initial counts \(1\) at length zero and \(2\) at length one. It is \(\operatorname{Fib}(L+2)\), including the zero word; remove zero to obtain the asserted positive-index count. As \(\operatorname{Fib}(L+2)=O(\varphi^L)\) for \(\varphi=(1+\sqrt5)/2<2\), the proportion below \(2^L\) tends to zero. The same bound implies ordinary natural density zero between successive dyadic cutoffs.

## Verification

The attached standalone `verify_franels.py` uses only Python's standard library. Run `python3 verify_franels.py` to check 6001 exact values computed from Franel's recurrence, 101 independently evaluated binomial sums and the Strehl decomposition, and termwise equality criteria. It separately checks thirteen Fibonacci counting cutoffs. This finite verification corroborates the universal proof; it does not replace the argument above.

## Relationship to prior work

Calkin (1998), Lemma 12, proved \(2^{s_2(n)}\mid\sum_k\binom nk^r\) for arbitrary positive power \(r\), not the equality characterization for cubic sums established here. Strehl's summation identity is classical and is not claimed as new; it is listed in OEIS A000172. The index sequence having no adjacent binary ones is classical, OEIS A003714, but the asserted equivalence with sharpness of Franel valuations was not identified in the checked source records. Schulte, VanSchalkwyk and Yang's 2014 report directly studies Franel valuations and is a material originality risk: its full text could not be accessed for a decisive comparison, and an equivalent result there or elsewhere has not been excluded.

## Limitations

No exact valuation is claimed when adjacent binary ones occur; only strict inequality beyond Calkin's lower bound follows. The theorem treats cubic binomial sums, not all higher odd powers. Full-text overlap with the 2014 MSRI-UP report remains unverified; independent scholarly review is not performed.

## References

1. N. J. Calkin, “Factors of sums of powers of binomial coefficients,” *Acta Arithmetica* **86** (1998), 17–26, DOI: 10.4064/aa-86-1-17-26 (especially Lemma 12).
2. V. Strehl, “Recurrences and Legendre transform,” *Séminaire Lotharingien de Combinatoire* **B29b** (1992); the Franel identity is also recorded in OEIS A000172, https://oeis.org/A000172.
3. A. Schulte, S. VanSchalkwyk, A. Yang, “On the divisibility and valuations of the Franel numbers,” *2014 MSRI-UP Research Reports* (August 2014), https://legacy.slmath.org/system/cms/files/81/files/original/Research_Reports_2014_MSRI-UP_%28Single_File%29.pdf (relevant but full text inaccessible).
4. OEIS A003714, “Fibbinary numbers,” https://oeis.org/A003714.
