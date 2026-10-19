# Exact initial non-repetitive complexity of the Rudin–Shapiro word

## Finding

Let \(r=r_0r_1\cdots\) be the binary Rudin–Shapiro word, where \(r_i\) is the parity of the number of overlapping occurrences of `11` in the standard binary expansion of \(i\), and \(r_0=0\). Let \(R(n)\) denote the first starting index at which a length-\(n\) factor of \(r\) equals a factor at an earlier starting index, with indices starting from zero. Equivalently, \(R(n)\) is the initial non-repetitive complexity of \(r\).

For **every integer \(n\ge1\)**,

\[
R(n)=\begin{cases}
1,&1\le n\le2,\\
4,&3\le n\le5,\\
2^{1+\lceil\log_2 n\rceil},&n\ge6.
\end{cases}
\]

The length-\(n\) factor beginning at \(R(n)\) has a **unique** earlier occurrence, at starting index \(0\) for \(n=1,2\) and every \(n\ge6\), and at index \(1\) for \(3\le n\le5\).

In particular,
\[
\liminf_{n\to\infty}\frac{R(n)}n=2,
\qquad
\limsup_{n\to\infty}\frac{R(n)}n=4.
\]

## Assumptions and scope

All indices are nonnegative integers. The factor starting at \(i\) of length \(n\) is \(r_i\cdots r_{i+n-1}\). The first repetition compares *all* earlier starting indices; it is not restricted to repetitions of the initial prefix. The claim concerns the classical binary Rudin–Shapiro word with seed \(r_0=0\), not arbitrary generalized Rudin–Shapiro words. Replacing each bit by its complement leaves \(R(n)\) unchanged.

The two identities
\[
r_{2j}=r_j,\qquad r_{2j+1}=r_j\oplus (j\bmod 2)
\]
follow directly by appending respectively `0` and `1` to the binary expansion of \(j\), where \(\oplus\) is addition modulo two.

## Proof

**1. Parity-recognition lemma.** No length-eight factor starting at an even index is equal to one starting at an odd index, anywhere in the infinite word. A finite exhaustive certificate for this lemma is described next; every claimed coverage step is exact.

Write the four letter states as \((b,p)\in\{0,1\}^2\) and define the length-two morphism
\[
\theta(b,p)=\big((b,0),(b\oplus p,1)\big).
\]
The fixed point beginning at \((0,0)\) is precisely \(g_j=(r_j,j\bmod2)\), by the preceding identities. The entire adjacent-pair language of this state fixed point is the closure, under adjacent pairs in \(\theta(a)\theta(b)\), of the pair obtained from \(\theta(0,0)\). In state notation `bp`, the closure has exactly the following eight ordered pairs:

`00-01, 00-11, 01-00, 01-10, 10-01, 10-11, 11-00, 11-10`.

Indeed, closure contains the seed pair and is stable under each substitution, hence includes all pairs appearing in any finite fixed-point prefix; conversely, every closure step takes an already occurring pair to another occurring pair. Every length-eight factor beginning at an index \(8q+s\), \(0\le s<8\), is a window of length eight at offset \(s\) in the 16-letter coded word \(\theta^3(g_q)\theta^3(g_{q+1})\). Applying the eight adjacent pairs and all eight offsets gives exactly **24** distinct windows at even offsets and **32** at odd offsets, with **no intersection**. The 7-file reproducibility package includes `verify_rs_first_repetition.py`, which constructs these sets and asserts the cardinalities and empty intersection; the finite loops, together with the proven exhaustive covering, constitute the parity-recognition certificate.

**2. Decimation lemma.** Fix \(n\ge8\) and \(m=\lceil n/2\rceil\). If two equal length-\(n\) factors begin at \(i<j\), then \(i,j\) have the same parity by Step 1. If they are even, write \(i=2a\), \(j=2b\). Their even-indexed letters yield equal length-\(m\) factors of \(r\) at \(a,b\). Their odd-indexed letters additionally force \(a\equiv b\pmod2\), because \(r_{2t+1}=r_t\oplus(t\bmod2)\).

If \(i,j\) are odd, write \(i=2a+1\), \(j=2b+1\). Comparing the odd-indexed letters \(r_{2t+1}\) and the following even-indexed letters \(r_{2t+2}=r_{t+1}\) forces \(a\equiv b\pmod2\) (there are overlapping comparisons since \(n\ge8\)). After parity cancellation, their equality implies equal length-\(\lfloor n/2\rfloor+1\) factors of \(r\) at \(a,b\), hence equal length-\(m\) factors. Thus **every** length-\(n\) collision decimates to an earlier length-\(m\) collision; an even-start collision also inherits same parity of the half-indices.

**3. Base.** Direct exact enumeration of factors in the first 44 positions gives

| \(n\) | \(R(n)\) | unique earlier index |
|---|---:|---:|
| 1 | 1 | 0 |
| 2 | 1 | 0 |
| 3, 4, 5 | 4 | 1 |
| 6, 7, 8 | 16 | 0 |
| 9, 10 | 32 | 0 |

For each row, the indicated length-\(n\) factor repeats at \(R(n)\), and all earlier starting factors are pairwise different. The standalone program independently reproduces each individual base case using direct substring equality.

**4. Induction.** Suppose \(n\ge11\) and put \(m=\lceil n/2\rceil\), so \(6\le m<n\). Assume that \(R(m)\) is an even power of two, and that the factor at \(R(m)\) equals the factor at zero and has no other earlier occurrence. If a length-\(n\) collision occurred at index \(j<2R(m)\), Step 2 would produce an earlier length-\(m\) collision at some half-index strictly below \(R(m)\), a contradiction (for odd \(j\), \(j=2b+1<2R(m)\) gives \(b<R(m)\)). Therefore \(R(n)\ge2R(m)\).

Conversely the length-\(m\) blocks at positions \(R(m)\) and zero agree. Since \(R(m)\) is even, the binary recurrence doubles this agreement into equality of the length-\(2m\) blocks at positions \(2R(m)\) and zero; the same holds for the first \(n\le2m\) symbols. Hence \(R(n)=2R(m)\). The unique earlier match is at zero: an odd earlier start is excluded by Step 1, and any other even earlier start would yield a second earlier match for the length-\(m\) factor at \(R(m)\). This completes strong induction, starting from \(6\le m\le10\).

The recurrence \(R(n)=2R(\lceil n/2\rceil)\) for \(n\ge11\), together with the base values, yields the stated formula \(R(n)=2^{1+\lceil\log_2 n\rceil}\) for all \(n\ge6\). Along powers of two the ratio is \(2\); just above successive powers of two the ratio approaches \(4\). The same formula bounds the ratio between these extremes, proving the two limits.

## Verification

Execute `python3 verify_rs_first_repetition.py` with Python 3.10 or later. The verifier independently computes \(131072\) sequence bits by (a) the state morphism and (b) bitwise overlapping-`11` counting, checks the exhaustive adjacent-state-pair closure and disjoint parity-specific length-eight factor sets, and scans first substring collisions for every length from \(1\) through \(1024\) plus nine larger boundary cases through \(8192\). Expected terminal status is `VERIFY_OK`. The finite checks substantiate the explicit finite lemma and bases; the induction, not the long finite scan, proves the infinite formula.

## Relationship to prior work

Nicholson and Rampersad introduced and analyzed initial non-repetitive complexity for several classical infinite words, proving formulas for Thue–Morse, Fibonacci, and Tribonacci words. Their article does not derive the present Rudin–Shapiro formula. Lü, Chen, Wen, and Wu study the *abelian* complexity of Rudin–Shapiro factors, which identifies factors only by letter counts rather than by exact equality or first repeated starting index. The distinct first-collision threshold is not inferred from those results. The four-state morphism and the binary recurrence are classical; their use in the precise first-repetition induction is the substantive claim here.

## Limitations

This theorem concerns the specified classical binary Rudin–Shapiro sequence and its global initial factor scan only. It does not characterize first-repetition positions for arbitrarily shifted scans or generalized Rudin–Shapiro substitutions. An equivalent exact formula in unindexed sources cannot be excluded by searches alone. Independent scientific validation has not been performed.

## References

1. J. Nicholson and N. Rampersad, *Initial non-repetitive complexity of infinite words*, arXiv:1507.08206 (first public version 2015-07-29), https://arxiv.org/pdf/1507.08206 .
2. X. Lü, J. Chen, Z. Wen and W. Wu, *On the abelian complexity of the Rudin-Shapiro sequence*, arXiv:1606.06935 (first public version 2016-06-22), https://arxiv.org/pdf/1606.06935 .
