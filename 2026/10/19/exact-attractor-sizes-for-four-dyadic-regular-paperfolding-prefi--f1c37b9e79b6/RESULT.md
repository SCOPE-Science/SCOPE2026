# Exact attractor sizes for four dyadic regular-paperfolding prefixes

## Finding

Let \(P_N=p_1p_2\cdots p_N\) denote the length-\(N\) prefix of the regular paperfolding word, defined below. The minimum size \(\gamma(P_N)\) of a string attractor is exactly

\[
\gamma(P_{128})=5,\qquad \gamma(P_{256})=6,\qquad
\gamma(P_{512})=6,\qquad \gamma(P_{1024})=7.
\]

Together with the previously recorded exact dyadic prefix values through length \(64\), these values complete the finite dyadic attractor-size profile up to length \(1024\). In particular, the four values are **exact**, not merely upper or lower estimates.

## Assumptions and scope

For every positive integer \(j\), divide \(j\) by its largest power of two, obtaining the odd part \(u(j)\). Define the one-based bit sequence by \(p_j=0\) when \(u(j)\equiv1\pmod 4\), and \(p_j=1\) when \(u(j)\equiv3\pmod 4\). The initial sixteen bits are `0010011000110110`. This specifies the conventional regular paperfolding sequence without relying on a substitution or a choice of a limiting fold.

For a finite word \(w\) with length \(N\), a **string attractor** is a set \(\Gamma\subseteq\{0,\ldots,N-1\}\) such that each nonempty distinct contiguous factor \(f\) of \(w\) has an occurrence occupying some interval \([s,s+|f|-1]\) intersecting \(\Gamma\). All positions in the mathematical statement and accompanying certificates are **zero-based**. The minimum attractor cardinality is \(\gamma(w)\).

The claim concerns exactly the four displayed finite prefixes. It does not assert a formula for all prefix lengths or decide the asymptotic behavior of \(\gamma(P_N)\).

## Proof

**Upper bounds.** The following explicit position sets are attractors (the word-generation rule and exhaustive verification below are part of each finite certificate):

| Prefix length | Attractor positions (zero-based) |
|---|---|
| \(128\) | `19, 39, 55, 77, 95` |
| \(256\) | `37, 55, 83, 107, 143, 191` |
| \(512\) | `119, 141, 191, 295, 351, 403` |
| \(1024\) | `155, 341, 417, 455, 575, 623, 767` |

The verifier forms *all* distinct factors at *every* length \(1\le\ell\le N\), using exact byte-string equality. For each length, it independently forms the set of factors having an occurrence that crosses one of the listed positions, and confirms equality with the complete distinct-factor set. This finite exhaustive test proves the asserted upper bounds, without a randomness assumption or an appeal to an optimization package.

**Lower bounds.** For any nonempty factor \(f\) of \(P_N\), define \(U_f\) to be the union of positions belonging to *any* occurrence of \(f\). Every attractor intersects \(U_f\). Fix a positive integer denominator \(d\) and a list of distinct factors \(f\) with positive integer numerators \(a_f\). Suppose the list satisfies

\[
\sum_{f:\,p\in U_f}a_f\le d\qquad\text{for every }p\in\{0,\dots,N-1\}.
\]

Every attractor \(\Gamma\) then obeys

\[
\sum_f a_f
\le \sum_{p\in\Gamma}\sum_{f:\,p\in U_f}a_f
\le d\,|\Gamma|,
\qquad\text{hence}\qquad
|\Gamma|\ge\left\lceil\frac{\sum_fa_f}{d}\right\rceil.
\]

The complete factor lists, exact numerator weights, and denominators are provided in `certificates.json`. The checked parameters are:

| \(N\) | Number of weighted factors | \(d\) | \(\sum_fa_f\) | Largest exact position load | Certified lower bound |
|---|---:|---:|---:|---:|---:|
| \(128\) | 5 | 1 | 5 | 1 | 5 |
| \(256\) | 11 | 2 | 11 | 2 | 6 |
| \(512\) | 12 | 2 | 12 | 2 | 6 |
| \(1024\) | 21 | 8 | 51 | 8 | 7 |

For each factor, `verify.py` computes its occurrences directly using exact matching, then builds the union \(U_f\) and its position loads. `verify_independent.py` repeats the check by constructing an integer-bitset mask for the occurrence-span union of **every** distinct factor. Each routine confirms that all listed factors occur and that the maximum load does not exceed \(d\). Thus the displayed integer inequality holds simultaneously at every position. Combining the certified lower and upper bounds proves all four equalities.

## Verification

Run from this directory, using Python 3 and its standard library only:

```sh
python3 verify.py
python3 verify_independent.py
```

Both independently reconstruct the word, inspect *all* contiguous factors with exact comparisons, verify the proposed attractor at every factor length, and verify the weighted occurrence-union lower-bound constraints at every position. Successful outputs terminate respectively in `VERIFY_OK` and `INDEPENDENT_VERIFY_OK`.

As an additional cross-check, the enumerated numbers of distinct nonempty factors are respectively \(6479\), \(25775\), \(102767\), and \(410351\). These counts were previously recorded and are not independently claimed as new results. Neither checker uses a solver, search transcript, numerical tolerance, or a hash as a proxy for factor equality.

## Relationship to prior work

Schaeffer and Shallit established general decidability and growth results for automatic-sequence string-attractor profiles; their reported explicit families include period-doubling, Thue–Morse, and Tribonacci, not this paperfolding finite profile. Banbara et al. (first public preprint February 18, 2026) give exact characterizations for Fibonacci and period-doubling words, different automatic-word families. Cassaigne et al. study attractor-profile and related complexities of infinite words, without stating the present four exact paperfolding values.

A publicly available September 2026 dyadic-prefix computational benchmark already reports exact regular-paperfolding values through length \(64\) and, for lengths \(128,256,512,1024\), certified upper estimates \(7,8,10,9\) together with lower estimates \(4,4,4,4\). That source also records the factor counts above. The present finite certificates close precisely those four gaps. Prior values and the general automatic-sequence framework are not part of the claimed novelty.

## Limitations

The four equalities are finite exact results. The certificates prove neither a closed formula for all dyadic prefix lengths nor boundedness or logarithmic divergence of the infinite paperfolding attractor profile. Minimal attractor sets need not be unique; no uniqueness or full enumeration of optimal sets is asserted. The lower-bound factor lists were discovered computationally, but their correctness is verified *from their explicit contents*, without trusting the discovery process. Earlier unindexed enumerations of the same exact values remain a possible literature-coverage risk.

## References

1. L. Schaeffer and J. Shallit, *String Attractors for Automatic Sequences*, arXiv:2012.06840 (2020/2021).
2. M. Banbara, H. Bannai, P. Guo, D. Köppl, T. Mieno, and Y. Okamoto, *The Smallest String Attractors of Fibonacci and Period-Doubling Words*, arXiv:2602.16152 (first public February 18, 2026); CPM 2026, DOI:10.4230/LIPIcs.CPM.2026.33.
3. J. Cassaigne, F. Gheeraert, A. Restivo, G. Romana, M. Sciortino, and M. Stipulanti, *New string attractor-based complexities for infinite words*, Journal of Combinatorial Theory, Series A 208 (2024), 105936, DOI:10.1016/j.jcta.2024.105936.
4. *Exact minimal string attractors for Rudin–Shapiro and regular-paperfolding dyadic prefixes (n ≤ 64), with certified bounds to n = 1024*, public computational benchmark, September 8, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/9/8/SCOPE079.
