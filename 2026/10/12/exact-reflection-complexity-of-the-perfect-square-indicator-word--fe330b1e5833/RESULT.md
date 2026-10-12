# Exact reflection complexity of the perfect-square indicator word

## Finding

Let \(\mathbf{s}=s_0s_1s_2\cdots\) be the infinite binary word indexed by the nonnegative integers, with \(s_j=1\) exactly when \(j=k^2\) for some integer \(k\ge0\), and \(s_j=0\) otherwise. Let \(r_{\mathbf{s}}(n)\) be the number of distinct length-\(n\) contiguous factors of \(\mathbf{s}\), counted up to reversal (each factor is identified with its reversal whenever both factors occur). Then \(r_{\mathbf{s}}(0)=1\), \(r_{\mathbf{s}}(1)=2\), and for every integer \(n\ge2\), writing \(m=\lfloor n/2\rfloor\) and \(\varepsilon=n-2m\),

\[
r_{\mathbf{s}}(n)=2+\left\lfloor\frac{(m+1)^2}{3}\right\rfloor+\varepsilon.
\]

In particular, \(r_{\mathbf{s}}(n)=n^2/12+O(n)\). If \(p_{\mathbf{s}}(n)\) counts distinct length-\(n\) factors without identifying reversals, then \(p_{\mathbf{s}}(n)=n^2/8+O(n)\), so \(\lim_{n\to\infty}r_{\mathbf{s}}(n)/p_{\mathbf{s}}(n)=2/3\).

## Assumptions and scope

Positions begin at \(0\); importantly, \(0=0^2\) and \(1=1^2\) are both marked, so the word begins with `1100100001`. A factor may begin at any nonnegative index; a reversal need not itself be a factor. The reversal equivalence relation is on the finite set of factors actually occurring: \(u\sim v\) exactly if \(v=u\) or \(v=u^{\mathrm{rev}}\). The theorem treats every nonnegative factor length and uses no finite-prefix approximation in the proof. The usual empty word is the sole length-zero factor.

## Proof

**1. Factors with at most one marked position.** Because consecutive-square gaps tend to infinity, the all-zero length-\(n\) word occurs for every \(n\ge1\). All \(n\) words of the form \(0^a1 0^{n-a-1}\), \(0\le a<n\), occur by centering a window at a sufficiently isolated large square. They form exactly \(\lceil n/2\rceil\) reversal classes, in addition to the one all-zero class. Thus the total contribution from at most one \(1\) is \(1+\lceil n/2\rceil\).

**2. Unique indexing of multi-one factors.** Consecutive marked positions are \(k^2\) and \((k+1)^2\), at distance \(g_k=2k+1\). Let a length-\(n\) factor have at least two \(1\)'s, with the first two originating at these squares. Their distance identifies \(k\) uniquely, because the gaps \(g_k\) are strictly increasing. If \(a\) is the number of leading zeros, the factor itself identifies \(a\). The preceding square imposes \(0\le a\le B_k\), with \(B_0=0\) and \(B_k=2k-2\) for \(k\ge1\). Including the second \(1\) imposes \(a\le U_k=n-2k-2\). Thus \(k\) ranges over \(0\le k\le\lfloor(n-2)/2\rfloor\) and the number of distinct factors in class \(k\) is \(N_k=\min(B_k,U_k)+1\). The \(k=0\) class always contributes one reversal class.

**3. Reversal identifications.** A factor with at least three \(1\)'s has successive gaps drawn from the strictly increasing sequence \(1,3,5,\ldots\); its reversal would have strictly decreasing gaps. Such a reversal cannot occur in \(\mathbf{s}\), so these factors are all singleton reversal classes. For a factor containing exactly two \(1\)'s, write it as \(0^a1 0^{g_k-1}1 0^b\), where \(a+b=U_k\). Its reversal also occurs exactly if \(b\le B_k\): the first pair in the reversed factor must have the same distinct gap \(g_k\), and the reversed leading-zero bound is exactly the preceding-square bound. Whenever both \(a,b\le B_k\), neither orientation includes a third \(1\), since both outside runs have length at most \(2k-2\), shorter than either neighboring gap. Consequently, each unequal unordered pair \(\{a,b\}\) satisfying \(0\le a,b\le B_k\) and \(a+b=U_k\) removes exactly one duplicate; the equal pair, if present, is palindromic and removes none. Equivalently, the number of duplicate pairs is

\[
C_k=\left\lfloor\frac{1}{2}\max\Big\{0,\min(U_k,B_k)-\max(0,U_k-B_k)+1\Big\}\right\rfloor.
\]

There are no identifications across different \(k\): two-one factors of different indices have distinct middle gaps, and factors with three or more \(1\)'s have no reversal partners.

**4. Even lengths.** Take \(n=2m\), \(m\ge1\), and \(1\le k\le m-1\). Put \(A=m-k-1\), \(D=k-1\), so \(U_k=2A\), \(B_k=2D\). Direct substitution in the preceding formulas gives

\[
N_k-C_k=\min(A+1,2D+1)=\min(m-k,2k-1).
\]

For clarity: if \(A\le D\), then \(N_k=2A+1\) and \(C_k=A\). If \(D<A\le2D\), then \(N_k=2D+1\) and \(C_k=2D-A\). If \(A>2D\), then \(N_k=2D+1\) and \(C_k=0\). Each case yields the displayed minimum. Including the all-zero and single-one classes and the \(k=0\) factor,

\[
r_{\mathbf{s}}(2m)=m+2+\sum_{k=1}^{m-1}\min(m-k,2k-1).
\]

Put \(q=\lfloor m/3\rfloor\). For \(k\le q\) use \(2k-1\); for \(k>q\) use \(m-k\) (the tie, when present, is harmless). Hence the sum is \(q^2+(m-q-1)(m-q)/2\). Checking \(m\equiv0,1,2\pmod3\) gives

\[
r_{\mathbf{s}}(2m)=2+\left\lfloor\frac{(m+1)^2}{3}\right\rfloor.
\]

**5. Odd lengths.** For \(n=2m+1\), \(m\ge1\), the same indices \(k\) occur. For \(k\ge1\), the new value of \(U_k\) is \(2A+1\), while \(B_k=2D\) is unchanged. If \(A<D\), both \(N_k\) and \(C_k\) increase by one; if \(A\ge D\), neither changes. Therefore each \(N_k-C_k\) remains equal to \(\min(m-k,2k-1)\). The one-one reversal-class count \(\lceil n/2\rceil\) increases by one, while the all-zero and \(k=0\) contributions do not. Thus \(r_{\mathbf{s}}(2m+1)=r_{\mathbf{s}}(2m)+1\), yielding the claimed odd formula. Direct inspection gives \(r_{\mathbf{s}}(0)=1\) and \(r_{\mathbf{s}}(1)=2\).

**6. Asymptotic comparison.** Without merging reversals, the same analysis at even length yields

\[
p_{\mathbf{s}}(2m)=1+3m+2\left\lfloor\frac{(m-2)^2}{4}\right\rfloor
=\frac{m^2}{2}+O(m),\qquad m\ge1.
\]

Indeed the \(k\ge1\) factor count sums to \(\sum_{k=1}^{m-1}(2\min(k-1,m-k-1)+1)=(m-1)+2\lfloor(m-2)^2/4\rfloor\). Passing from length \(2m\) to \(2m+1\) adds at most one candidate for each of the \(m\) possible first-pair indices and one new one-one factor. It therefore changes \(p_{\mathbf{s}}\) by \(O(m)\). Combining this with the exact reflection formula proves \(p_{\mathbf{s}}(n)=n^2/8+O(n)\), \(r_{\mathbf{s}}(n)=n^2/12+O(n)\), and the ratio limit \(2/3\).

## Verification

The self-contained Python program `verify.py` independently constructs sufficiently long square-indicator prefixes, enumerates all distinct factors and reversal classes for every length from \(0\) through \(100\), and compares those counts with the theorem. Separately, it evaluates the exact finite gap enumeration for lengths through \(2000\) and compares the ordinary-factor even-length formula at the same range. Running `python3 verify.py` prints:

```text
VERIFY_OK direct_reversal_census_lengths=0..100 gap_count_lengths=101..2000 ordinary_even_lengths=2..2000
```

The chosen prefix includes every eligible pair of consecutive marked squares and, farther along, a \(1\) separated from its neighbors by more than the tested window length; hence the direct factor census is exhaustive at the tested lengths. These calculations corroborate the general proof but do not establish its infinite quantifiers.

## Relationship to prior work

Allouche, Campbell, Li, Shallit and Stipulanti [1] introduced reflection complexity, proved general structural results and gave evaluations for several automatic sequences. The inspected full text contains no classification for the characteristic word of the perfect squares or the present quadratic formula; its automatic-sequence theorem does not directly supply a formula for a characteristic sequence of squares. Dvořáková and Pelantová [2] study periodicity thresholds and minimal reflection complexity rather than this sparse polynomial support. The standard factor-complexity framework [3] underlies the ordinary-complexity comparison. These comparisons establish the mathematical distinction, not absolute priority.

## Limitations

The theorem concerns the single precisely specified square-support binary word and its reversal-class complexity. It does not classify arbitrary polynomial supports, compute all individual reversal-pair spectra, or give a uniform theorem for general strictly increasing gaps. The finite checker is corroborative only. Literature searches did not identify an identical published formula, but cannot exclude an unindexed result or a less obvious equivalent. The statement has received a self-review, not independent external validation.

## References

[1] J.-P. Allouche, J. M. Campbell, S. Li, J. Shallit and M. Stipulanti, *The reflection complexity of sequences over finite alphabets*, arXiv:2406.09302, first submitted 2024-06-13, https://arxiv.org/abs/2406.09302 ; open HTML text https://arxiv.org/html/2406.09302v4 .

[2] L. Dvořáková and E. Pelantová, *Reflection on the reflection complexity*, arXiv:2511.12358 (2025), https://arxiv.org/html/2511.12358v1 .

[3] J.-P. Allouche and J. Shallit, *Automatic Sequences: Theory, Applications, Generalizations*, Cambridge University Press, 2003, Chapter 10, factor-complexity definitions.
