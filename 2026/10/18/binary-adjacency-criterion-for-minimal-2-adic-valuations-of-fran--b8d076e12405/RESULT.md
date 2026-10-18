# Binary-adjacency criterion for minimal 2-adic valuations of Franel numbers

## Finding

Define the Franel numbers by
\[
f_n=\sum_{k=0}^{n}\binom{n}{k}^{3},\qquad n\geq0.
\]
Let \(s_2(n)\) denote the sum of the binary digits of \(n\), let \(\nu_2\) denote the valuation of a positive integer at the prime \(2\), and let \(t(n)\) count the positions where two consecutive binary digits of \(n\) are both \(1\). Then for **every** \(n\geq0\),
\[
\nu_2(f_n)\ge s_2(n),\qquad
\nu_2(f_n)=s_2(n)\ \Longleftrightarrow\ t(n)=0.
\]
There is a stronger, exact underlying statement: in Strehl's positive-summand expansion
\[
f_n=\sum_{k=0}^{n}\binom{n}{k}^{2}\binom{2k}{n},
\]
precisely \(2^{t(n)}\) nonzero summands have valuation \(s_2(n)\); all remaining nonzero summands have strictly larger valuation.

Writing \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\), this also gives the exact census
\[
\#\{0\le n<2^L:\nu_2(f_n)=s_2(n)\}=F_{L+2},\qquad L\ge0.
\]
For every fixed \(r\ge1\), the set of indices satisfying \(2^r\mid f_n\) has natural density \(1\).

## Assumptions and scope

The index \(n\) is any nonnegative integer, with its ordinary finite binary expansion (leading zeros allowed). The binomial coefficient \(\binom{2k}{n}\) is interpreted as zero if \(2k<n\). No conjectural recurrence, numerical extrapolation, restriction on the bit length, or hypothesis on \(n\) is required. The result concerns only the valuation at the prime \(2\) and identifies when a universal lower bound is sharp; it does not give every larger valuation.

## Proof

We use the classical identity attributed to Strehl, also given with proof as Theorem 2.9 of the 2014 Franel divisibility report:
\[
f_n=\sum_{k=0}^{n}\binom{n}{k}^{2}\binom{2k}{n}.
\]
For a nonzero summand, set \(a=n-k\) and \(b=2k-n\). Thus \(a,b\ge0\), \(k=a+b\), and \(n=2a+b=a+k\). Legendre's formula \(\nu_2(m!)=m-s_2(m)\) yields
\[
\begin{aligned}
\nu_2\!\left(\binom nk^2\binom{2k}{n}\right)
&=2s_2(a)+s_2(k)+s_2(b)-s_2(n)\\
&=s_2(n)+c_1+c_2,
\end{aligned}
\]
where
\[
c_1=s_2(a)+s_2(k)-s_2(n),\qquad
c_2=s_2(a)+s_2(b)-s_2(n).
\]
The first difference is the number of carries in binary addition \(a+k=n\), and the second is the number of carries in \(2a+b=n\) (because \(s_2(2a)=s_2(a)\)). Both are nonnegative. Hence every nonzero summand is divisible by \(2^{s_2(n)}\), proving the lower bound after summation.

Equality in a **summand** holds exactly when both additions are carry-free. The first carry-free identity is equivalent to the nonzero binary positions of \(a\) being a subset of those of \(n\). The second is equivalent to the nonzero binary positions of \(2a\) being a subset of those of \(n\). Consequently the binary positions of \(a\) may be any subset of
\[
B(n)=\{i\ge0:\text{the binary digits of }n\text{ at positions }i\text{ and }i+1\text{ equal }1\}.
\]
Indeed, choosing such a subset produces a nonnegative \(a\) and uniquely determines \(k=n-a\) and \(b=n-2a\), and the two sums are carry-free. Conversely, any carry-free pair has this form. There are therefore exactly \(2^{|B(n)|}=2^{t(n)}\) summands at valuation \(s_2(n)\).

Divide the identity by \(2^{s_2(n)}\) and reduce modulo \(2\). Each summand with the minimum valuation contributes an odd integer, while the other summands contribute zero. Thus
\[
\frac{f_n}{2^{s_2(n)}}\equiv 2^{t(n)}\pmod2.
\]
The quotient is odd if and only if \(t(n)=0\). This proves the sharpness classification, including \(n=0\).

Binary words of length \(L\) that avoid consecutive ones satisfy the standard two-state counting recurrence and are counted by \(F_{L+2}\), yielding the stated census. Finally, indices with \(\nu_2(f_n)<r\) necessarily have at most \(r-1\) nonzero binary digits. There are at most \(\sum_{j=0}^{r-1}\binom Lj\) such indices below \(2^L\), which is \(O_r(L^{r-1})\). The same bound, with \(L\) replaced by \(L+1\), applies below any \(N\in[2^L,2^{L+1})\); dividing by \(N\) proves density zero for the exceptions.

## Verification

The included standalone standard-library Python checker independently evaluates both binomial representations for every \(0\le n\le256\), checks the valuation of every positive Strehl summand against the two-carry identity, and counts the summands at the minimum valuation. It tests the sharpness equivalence, the Franel three-term recurrence, and Fibonacci censuses for binary-word lengths \(0\) through \(13\). Its completed output is:

```text
VERIFY_OK indices=257 positive_strehl_terms=16641 recurrence_instances=255 fibonacci_lengths=14
```

Run `python3 verify.py` from the directory containing this document and the checker. The finite checks are supplementary; the argument above proves the assertions for all nonnegative indices.

## Relationship to prior work

Strehl's sum identity is classical, and the digit-sum carry formula is standard. Sun's *Congruences for Franel numbers* (first arXiv version dated 2011-12-05) establishes congruences principally for odd primes; it does not give this sharp binary-adjacency criterion. Schulte, VanSchalkwyk, and Yang, *On the divisibility and valuations of the Franel numbers* (2014), study prime types and investigate binary valuation trees and empirical relationships. Their Theorem 2.9 supplies the Strehl identity, while their Sections 3–4 discuss the incomplete state of \(2\)-adic valuation classifications; the explicit all-index equality criterion and its exact Fibonacci census are not asserted there. OEIS A000172 records the underlying sequence and Strehl identity, not the stated criterion. These are statement-level comparisons, not assertions that absence from search results proves novelty.

## Limitations

The theorem does not determine \(\nu_2(f_n)\) exactly when the binary representation contains adjacent ones, other than showing strict inequality relative to \(s_2(n)\). It does not determine the distribution of the larger valuation excess or address odd primes. A broader general divisibility theorem or unindexed treatment could independently imply the criterion; independent literature assessment is still warranted.

## References

1. Zhi-Wei Sun, *Congruences for Franel numbers*, arXiv:1112.1034, first version submitted 2011-12-05; journal version *Advances in Applied Mathematics* 51 (2013), 524–535. https://arxiv.org/abs/1112.1034
2. Abraham Schulte, Samantha VanSchalkwyk, and Adela Yang, *On the divisibility and valuations of the Franel numbers*, MSRI Undergraduate Program Research Reports, August 2014, Theorem 2.9 and Sections 3–4. https://legacy.slmath.org/system/cms/files/81/files/original/Research_Reports_2014_MSRI-UP_%28Single_File%29.pdf
3. OEIS A000172, *Franel numbers*, comments on Strehl's identity and bibliography. https://oeis.org/A000172
