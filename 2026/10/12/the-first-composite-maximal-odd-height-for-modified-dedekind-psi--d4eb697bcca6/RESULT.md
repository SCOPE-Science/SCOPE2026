# The first composite maximal odd height for modified Dedekind \(\psi\) iteration

## Finding

For the multiplicative modified Dedekind function \(\bar\psi\) introduced by Defant, let \(\lambda(n)\) count iterations to reach \(2\), and for \(k\ge2\) let \(B(k)\) denote the largest odd positive integer satisfying \(\lambda(n)=k\). Then

\[
B(23)=8{,}193{,}151=127\cdot64{,}513,
\]

and \(B(k)\) is prime for every integer \(2\le k\le22\). Thus \(k=23\) is the first rank at which the maximal odd element is composite, disproving the primality pattern expressly suggested in Defant's 2015 paper. The largest prime of height \(23\) is \(8{,}126{,}431\), strictly smaller than \(B(23)\).

## Assumptions and scope

For prime \(p\) and integer \(a\ge1\), let

\[
\bar\psi(p^a)=
\begin{cases}
2^{a-1}&p=2,\\
p^{a-1}(p+1)&p\text{ odd},
\end{cases}
\qquad \bar\psi(1)=1,
\]

extended multiplicatively. Let \(\lambda(n)\) be the least number of applications of \(\bar\psi\) needed to reach \(2\), for \(n\ge2\). Set \(\lambda(1)=0\) as a convention. The bound and finding concern all odd positive integers of the respective heights, not a chosen search interval or a restricted factorization family. No conjecture about larger heights is asserted.

## Proof

**Step 1: additive recurrence and its relation to iteration.** Define \(H(1)=0\), \(H(2)=1\), and for every odd prime \(p\) define

\[
H(p)=1+H((p+1)/2),
\]

then extend \(H\) completely additively over prime factorizations. The recursion is well founded since \((p+1)/2<p\). In particular \(H(p+1)=H(2)+H((p+1)/2)=H(p)\) for odd primes. Consequently the multiplicativity of \(\bar\psi\) gives, for every odd \(m\ge1\),

\[
H(\bar\psi(m))=H(m),
\]

and, for every even \(n\ge2\),

\[
H(\bar\psi(n))=H(n)-1.
\]

Each odd \(m>1\) has \(H(m)\ge2\) and \(\bar\psi(m)\) even; the only even integer with \(H\)-value \(1\) is \(2\). Thus repeated application to \(m\) reaches \(2\) after exactly \(H(m)\) iterations, establishing \(\lambda(m)=H(m)\) for odd \(m>1\). An even input \(n\ge2\) needs \(H(n)-1\) iterations. This proves the necessary structural lemma, without assuming the external additivity theorem.

**Step 2: rigorous finite cutoff.** For odd \(m>1\), \(\bar\psi(m)\ge m+1\). For even \(t>2\), \(\bar\psi(t)\ge t/2\). If \(\lambda(m)=k\), then the first step lands at an even number and the remaining \(k-1\) iterations terminate at \(2\). Therefore

\[
2\ge \frac{m+1}{2^{k-1}},\qquad m+1\le 2^k.
\]

In particular all odd elements of height at most \(23\) lie below \(2^{23}=8{,}388{,}608\). This theoretical bound makes the following finite computation *exhaustive* rather than heuristic sampling.

**Step 3: exact complete arithmetic certificate.** For every integer \(3\le n<2^{23}\), a smallest-odd-prime-factor sieve and the following identities compute \(H(n)\) from strictly smaller arguments:

\[
H(n)=\begin{cases}
H(n/2)+1,&2\mid n,\\
H(p)+H(n/p),&n\text{ odd composite and }p\text{ its smallest prime factor},\\
1+H((n+1)/2),&n\text{ odd prime}.
\end{cases}
\]

The fully specified standalone program `verify_defant_B23.py` implements these three exhaustive branches, certifies primality with the sieve, and takes the largest odd \(n\) in each height class. It outputs \(B(k)\) equal to the largest prime of class \(k\) for every \(2\le k\le22\), and

\[
B(23)=8{,}193{,}151,\qquad P(23)=8{,}126{,}431.
\]

It independently factors \(8{,}193{,}151=127\cdot64{,}513\), and checks direct \(\bar\psi\)-iteration trajectories with lengths \(7\) and \(16\) for the two factors. These verify that the composite candidate has height \(23\). The program additionally verifies original-function trajectories for all \(97{,}728\) larger odd competitors in the proven range, none of which has height \(23\). Therefore the displayed composite is the actual class maximum, not merely an example. All smaller heights have prime maxima, proving minimality of the failing rank.

The exhaustive class maxima are:

| Height \(k\) | Maximum \(B(k)\) |
| ---: | ---: |
| 2 | 3 |
| 3 | 7 |
| 4 | 13 |
| 5 | 31 |
| 6 | 61 |
| 7 | 127 |
| 8 | 223 |
| 9 | 487 |
| 10 | 991 |
| 11 | 1951 |
| 12 | 3967 |
| 13 | 8191 |
| 14 | 16381 |
| 15 | 32257 |
| 16 | 64513 |
| 17 | 131071 |
| 18 | 262111 |
| 19 | 524287 |
| 20 | 1048573 |
| 21 | 2096893 |
| 22 | 4194271 |
| 23 | 8193151 (composite) |

## Verification

Run `python3 verify_defant_B23.py` with Python 3.9 or newer. The self-contained program uses only `array` and `math`. It requires memory for a sieve and an eight-million-entry height array. The run actually returned `EXACT_CERTIFICATE_OK first_composite_class=23 B23=8193151 prime_max_23=8126431 suffix_checked=97728`, followed by every height maximum and the prime maxima. The certificate tests the full logically sufficient domain, not a random sample.

## Relationship to prior work

Defant's *An Arithmetic Function Arising from the Dedekind \(\psi\) Function*, arXiv:1501.00971, introduced \(B(k)\). Theorem 2.3 of that paper gives \(B(k)<2^k\). After Theorem 2.4 the paper expressly identifies an empirical all-prime pattern without proof or known counterexample. Theorem 2.5 proves divisor inheritance for the set of record maxima, but neither settles the primality pattern nor identifies its first failure. The present finding supplies a finite, exact counterexample *and proves earliest failure*. The original upper-bound argument and terminology are prior work, not claimed as new. A search of related indexed literature and semantically related mathematical records identified no covering height-23 extremal classification.

## Limitations

The theorem decides \(B(k)\) only for \(2\le k\le23\), and identifies the first nonprime maximum. It does not describe later maxima or a density of composite maxima. Correctness is conditional on executing the provided finite arithmetic specification accurately; the independently implemented direct-iteration checks provide redundancy, but no external independent audit is claimed. Unindexed earlier computations could contain the same exceptional maximum.

## References

1. C. Defant, *An Arithmetic Function Arising from the Dedekind \(\psi\) Function*, arXiv:1501.00971v1 (first public submission 2015-01-05), especially Theorems 2.3–2.5 and the discussion following Theorem 2.4. https://arxiv.org/abs/1501.00971
2. C. Defant, *An Arithmetic Function Arising from the Dedekind \(\psi\) Function*, Mathematical Journal of Okayama University 59 (2017), 81–92 (later journal manifestation of the same research, not the first-publication date).
