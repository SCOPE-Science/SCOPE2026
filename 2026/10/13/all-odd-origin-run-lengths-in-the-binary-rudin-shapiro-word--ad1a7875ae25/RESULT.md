# All odd origin-run lengths in the binary Rudin–Shapiro word

## Finding

Let \(e_{11}(n)\) count overlapping occurrences of the binary block \(11\) in the ordinary base-two expansion of the nonnegative integer \(n\), and put \(r(n)=e_{11}(n)\bmod 2\). In particular, \(r(0)=0\). For each integer \(d\ge1\), let
\[
A_r(0,d)=\min\{j\ge1:r(jd)\ne r(0)\}.
\]
This is the number of consecutive monochromatic progression terms beginning with \(0\), in the convention where the first differently colored index is excluded.

**Theorem (complete origin-run spectrum).**
\[
\boxed{\{A_r(0,d):d\in\mathbb Z_{\ge1}\}=\{1,3,5,\ldots\}.}
\]
Every positive odd integer is realized by infinitely many different positive differences. More explicitly, if \(k\ge3\) is odd, let \(Q\) be any power of two satisfying \(Q\ge2k(k-1)\), let \(a\) be the largest positive odd integer with \(a\le Q/(k-1)\), and set
\[
d=a(2Q+1).
\]
Then \(A_r(0,d)=k\). Taking the smallest admissible \(Q\) gives \(d<32k^3\). The value \(1\) is realized by \(d=3\cdot2^m\) for every \(m\ge0\).

## Assumptions and scope

Only the ordinary binary Rudin–Shapiro coloring is considered: each overlapping \(11\) contributes once, with parity reduced modulo two, and positions are indexed from zero. Differences \(d\) are arbitrary positive integers. The invariant \(A_r(0,d)\) is **not** the extremal invariant \(A_r(d)=\sup_{n\ge0}A_r(n,d)\), where one may begin at any position. The theorem concerns possible values of the first-color-change index and gives a polynomial-size constructive difference for every odd prescribed value; it does not compute the smallest such difference or the density of differences realizing it.

## Proof

**Step 1 (exclusion of even values).** Appending a zero to the binary expansion introduces no new occurrence of \(11\), so \(r(2n)=r(n)\) for every \(n\ge0\). If a first color change occurred at an even index \(j=2h\), then \(r(jd)=r(hd)\); hence the color had already changed at the smaller positive index \(h\), a contradiction. Thus whenever a first color change occurs, its index is odd. The minimum exists for every difference: Sobolewski's Theorem 1.4 supplies a finite bound when \(d\ge3\), and \(r(3)=r(6)=1\) settles \(d=1,2\).

**Step 2 (two-copy identity).** Fix \(L\ge1\) and \(0\le x<2^L\). Represent \(x\) by exactly \(L\) binary digits, allowing leading zeros. Because the two shifted copies do not overlap, the binary expansion of \((2^L+1)x\), padded on the left if needed, consists of these \(L\) digits concatenated with themselves. Every \(11\) pair lying strictly inside either copy is counted twice and cancels modulo two. Only the pair across the junction remains. Its value is the product of the last (least significant) digit of the first copy and the first (most significant) digit of the second. Therefore
\[
r\bigl((2^L+1)x\bigr)
\equiv (x\bmod 2)\left(\left\lfloor\frac{x}{2^{L-1}}\right\rfloor\right)\pmod2.
\tag{1}
\]
The quotient in (1) is always \(0\) or \(1\) under the stated range of \(x\).

**Step 3 (construct each odd length).** Fix an odd integer \(k\ge3\). Choose a power of two \(Q\ge2k(k-1)\), and let \(a\) be the largest odd integer not exceeding \(Q/(k-1)\). Then
\[
\frac{Q}{k-1}-2<a\le\frac{Q}{k-1}.
\]
Consequently
\[
(k-2)a<Q,\qquad Q\le ka<2Q.\tag{2}
\]
Indeed the first strict inequality follows from the upper bound on \(a\); the second follows from \(ka>kQ/(k-1)-2k=Q+Q/(k-1)-2k\ge Q\), while \(ka\le kQ/(k-1)<2Q\). Write \(2Q=2^L\), put \(d=a(2^L+1)\), and apply (1) to \(x=ja\) for each \(1\le j\le k\). All these values of \(x\) are below \(2Q\) by (2). If \(j\) is even, \(ja\) is even so (1) gives \(r(jd)=0\). If \(j\) is odd and \(j<k\), then \(ja\le(k-2)a<Q\) so (1) again gives \(r(jd)=0\). Finally \(ka\) is odd and \(Q\le ka<2Q\), giving \(r(kd)=1\). Thus the first color change occurs at exactly \(j=k\), proving \(A_r(0,d)=k\).

For \(k=1\), the binary expansion of \(3\cdot2^m\) is \(11\) followed by \(m\) zeros; hence \(r(3\cdot2^m)=1\) and \(A_r(0,3\cdot2^m)=1\) for every \(m\ge0\). Increasing \(Q\) through powers of two in the preceding construction gives strictly increasing differences for each fixed odd \(k\ge3\), proving infinite realization.

**Step 4 (effective bound).** For the *smallest* power of two \(Q\ge2k(k-1)\), we have \(Q<4k(k-1)\). Since \(a\le Q/(k-1)<4k\),
\[
d=a(2Q+1)<4k\bigl(8k(k-1)+1\bigr)<32k^3
\]
for all \(k\ge3\). Steps 1 and 3 establish both inclusions of the claimed spectrum, including the explicit bound.

## Verification

The accompanying self-contained `verify.py` uses a direct adjacent-bit counter, independent of the bit-concatenation formula. Running `python3 verify.py` produced:

`VERIFY_OK double_checks=20001 concatenation_checks=16382 constructed_odd_k=200 small_d=1024 second_witness_k=25`

In detail it checked \(r(2n)=r(n)\) for \(0\le n\le20000\); identity (1) for all \(0\le x<2^L\) and \(1\le L\le13\); the explicit witness construction for every positive odd \(k\le399\); the oddness of the first change for all \(1\le d\le1024\); and second, larger, independent differences for odd \(3\le k\le51\). The checks are finite corroboration only. The quantified claims for all integers are established by the proof above.

## Relationship to prior work

Sobolewski's work on monochromatic arithmetic progressions in pattern-counting words defines exactly the invariant \(A_r(0,d)\), proves sharp upper bounds for each difference (Theorem 1.4), and develops doubled binary-block constructions for fixed multipliers (Proposition 5.4). **Section 6, Problem 8 explicitly asks for the set of attained values** and suggests all positive odd values occur for patterns ending in \(1\). The present theorem settles that part of Problem 8 for the Rudin–Shapiro pattern \(11\), by choosing the multiplier in a controlled interval that enforces the *first* color change at any prescribed odd index. The underlying idea of duplicated binary blocks is already present in the source and is not presented here as new. The source's fixed-multiplier asymptotic and special-difference formulas do not themselves state the complete origin-run spectrum.

Joshi and Rust subsequently analyzed the **longest** monochromatic progressions over all starting positions, with further particular Rudin–Shapiro differences. That extremal invariant \(A_r(d)\) is different from the fixed-origin \(A_r(0,d)\) classified here. OEIS A364995 and A380593 also concern longest progressions and their first starting positions, not the present origin-run range.

## Limitations

This result concerns the binary pattern \(11\) only. It does not settle the analogous attainable-value question for arbitrary binary patterns, the full-start supremum \(A_r(d)\), uniqueness/minimality of the constructed differences, or the distribution of differences by attained run length. The cubic upper bound on a witnessing difference is constructive, not claimed optimal. Originality relative to unindexed earlier deductions from the duplicated-block method remains a possible literature risk. The accompanying finite checker does not independently certify the infinitely quantified proof.

## References

1. Bartosz Sobolewski, *On monochromatic arithmetic progressions in binary words associated with pattern sequences*, arXiv:2204.05287 (first public 2022-04-11; inspected version 2, Sections 1, 5 and 6, notably Proposition 5.4 and Problem 8); subsequently *Theoretical Computer Science* **1018** (2024), 114815, doi:10.1016/j.tcs.2024.114815.
2. Gandhar Joshi and Dan Rust, *Monochromatic arithmetic progressions in the Fibonacci, Thue–Morse, and Rudin–Shapiro words*, arXiv:2501.05830 (inspected Section 3.3 and introductory definition of its extremal invariant).
3. OEIS A364995, *Length of the longest monochromatic arithmetic progressions of difference n in the Rudin–Shapiro sequence*, and OEIS A380593, *Starting position of the first occurrence of the longest monochromatic arithmetic progression of difference n* (distinguished invariants).
