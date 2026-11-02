# Complete closed-factor and length spectra of finite Zimin words

## Finding

Let \(Z_0=\varepsilon\) and \(Z_r=Z_{r-1}a_rZ_{r-1}\) for \(r\geq1\), where all \(a_r\) are different letters. Let \(\operatorname{suf}_i\) and \(\operatorname{pre}_j\) denote the suffix and prefix of the specified length, including the empty word at length zero. A nonempty word is *closed* if it is a letter or has a nonempty proper border occurring exactly twice, as its prefix and suffix; overlapping occurrences are counted.

**Complete classification.** For every integer \(n\geq1\), the distinct closed, nonempty contiguous factors of \(Z_n\) are exactly the words
\[
U_{r;i,j}=\operatorname{suf}_i(Z_{r-1})\,a_r\,\operatorname{pre}_j(Z_{r-1}),
\quad 1\leq r\leq n,
\]
where either \(i=j=0\), or there is an integer \(0\leq t\leq r-2\) for which
\[
2^t\leq i,j\leq2^{t+1}-1.
\]
The representation is unique. In particular, for \(r\geq1\), the number whose largest letter is \(a_r\) is
\[
H_r=\frac{4^{r-1}+2}{3},
\]
and the total number of distinct nonempty closed factors of \(Z_n\) is
\[
\boxed{\displaystyle C_n=\frac{4^n+6n-1}{9}.}
\]

**Complete length distribution.** If \(c_n(\ell)\) counts these factors of length \(\ell\), then \(c_n(1)=n\). For \(0\leq t\leq n-2\) and \(2^{t+1}+1\leq\ell\leq2^{t+2}-1\),
\[
\boxed{\displaystyle c_n(\ell)=(n-t-1)\min\{\ell-2^{t+1},\,2^{t+2}-\ell\}.}
\]
At every other positive length, \(c_n(\ell)=0\). The triangular blocks are separated by missing lengths at all powers of two greater than one.

## Assumptions and scope

The factors are literal contiguous substrings of the complete finite word \(Z_n\), over an alphabet of exactly \(n\) mutually distinct letters; no ordering on the alphabet is needed. The empty word is excluded from all counts. The word \(Z_0\) is used only to define \(Z_1\). The formulas hold for every integer \(n\geq1\), including boundary cases \(n=1\) and \(r=1\). All occurrences, including overlapping occurrences, count for closedness.

## Proof

**1. The ruler structure and a unique marker.** Number letters in \(Z_n\) starting at one. Induction in the displayed recursion gives
\[
Z_n[p]=a_{1+\nu_2(p)},\qquad 1\leq p\leq2^n-1,
\]
where \(\nu_2(p)\) is the largest \(e\geq0\) with \(2^e\mid p\). If a factor contains two occurrences of \(a_r\), between them is a position divisible by \(2^r\), holding a letter of rank greater than \(r\). Therefore every factor whose largest letter is \(a_r\) contains exactly one \(a_r\). The adjacent block on each side of an occurrence of \(a_r\) is a copy of \(Z_{r-1}\) unless a higher-ranked marker or a finite-word endpoint intervenes at the next multiple of \(2^r\). Thus every factor with highest letter \(a_r\) has the unique form \(U_{r;i,j}\), with \(0\leq i,j\leq2^{r-1}-1\); conversely, every such pair is realized around the central \(a_r\) of the embedded copy of \(Z_r\) in \(Z_n\). No two choices give the same word, since the position of its unique \(a_r\) determines \(i\) and \(j\).

In what follows, put the distinguished \(a_r\) at signed position zero. At nonzero relative positions \(h\) with \(|h|<2^{r-1}\), the letter is \(a_{1+\nu_2(|h|)}\); the displayed factor occupies the positions \(-i,-i+1,\ldots,-1,0,1,\ldots,j\).

**2. Two indices in one dyadic shell give a closed factor.** Fix \(d=2^t\), with \(0\leq t\leq r-2\), and \(d\leq i,j\leq2d-1\). Put \(b=i+j-2d+1\); then \(1\leq b\leq\min\{i,j\}\). The prefix of length \(b\) occupies signed positions \([-i,j-2d]\), entirely to the left of the marker, and the suffix of length \(b\) occupies \([2d-i,j]\), entirely to the right. These intervals differ by translation by \(2d\). For \(-2d<h<0\), the equality \(\nu_2(|h|)=\nu_2(h+2d)\) makes their letters identical. Hence the two copies form a border of length \(b\).

The first copy contains the letter \(a_{t+1}\) at relative position \(-d\), and the second at \(+d\). These are the only two occurrences of \(a_{t+1}\) in the entire factor: its side lengths are less than \(2d\), and the central letter is the different symbol \(a_r\). Since the border contains \(a_{t+1}\) exactly once, any occurrence of this border must align that letter with one of those two positions. Thus it has precisely the two required occurrences, and the factor is closed. The case \(i=j=0\) gives the single letter \(a_r\), which is closed by definition.

**3. Different dyadic shells never give a closed factor.** A factor with exactly one of \(i,j\) equal to zero has no nonempty border: such a border would need to contain the unique central \(a_r\) at both ends. Reversal preserves closedness, and \(Z_{r-1}\) is a palindrome, so reversing \(U_{r;i,j}\) gives \(U_{r;j,i}\). For nonzero indices in different shells it therefore suffices to assume \(i<j\). Select \(d=2^t\) such that \(d\leq i<2d\); then \(j\geq2d\).

Suppose a nonempty border \(v\) existed. Its prefix occurrence cannot contain the unique \(a_r\), and has length at most \(i<2d\). It therefore contains no symbol with rank at least \(t+2\). The terminal occurrence of \(v\), entirely on the right, avoids every relative position divisible by \(2d\), because such positions carry letters of rank at least \(t+2\). Since it ends at \(j\geq2d\), this occurrence must be wholly inside an interval \((2qd,2(q+1)d)\) of positive positions for some \(q\geq1\). Translating it by \(-2d\) leaves it entirely in the right-hand side, and leaves its letters unchanged: at all positions not divisible by \(2d\), the valuation is invariant under that translation. This produces a third occurrence of \(v\), distinct from its prefix occurrence and its terminal occurrence. Therefore no border can occur exactly twice, and the factor is not closed. This proves the classification in both directions.

**4. Counting and exact length distribution.** The marker \(a_r\) alone contributes one closed factor. Shell \(t\) has \(2^t\) choices for each of \(i\) and \(j\), contributing \(4^t\) distinct factors. Thus
\[
H_r=1+\sum_{t=0}^{r-2}4^t=\frac{4^{r-1}+2}{3};\qquad
C_n=\sum_{r=1}^n H_r=\frac{4^n+6n-1}{9}.
\]
At a fixed shell \(t\), let \(d=2^t\). The lengths are \(\ell=i+j+1\) with \(d\leq i,j\leq2d-1\). For \(2d+1\leq\ell\leq4d-1\), the number of ordered pairs is exactly \(\min\{\ell-2d,4d-\ell\}\), by counting diagonals in a \(d\)-by-\(d\) integer square. This shell occurs at precisely the marker ranks \(r=t+2,\ldots,n\), giving the announced length formula. The intervals from different shells are disjoint, with a gap at each intervening power of two. No remaining positive lengths occur.

## Verification

Run the standalone file `checker.py` using Python 3 with no third-party packages. It constructs the finite words independently, lists every distinct contiguous factor, checks closedness directly by searching all possible borders and internal occurrences, compares the complete factor sets with the stated classification, and checks every length count and highest-letter count. Exhaustive tests were completed for all ranks \(1\leq n\leq8\), with observed numbers of nonempty closed factors \(1,3,9,31,117,459,1825,7287\). All tests passed. The proof above, not this finite test, establishes the claim for all ranks.

## Relationship to prior work

Badkobeh, Fici, and Lipták (first public preprint May 28, 2013) introduced fundamental bounds and structural criteria for the number of closed factors of general finite words, including quadratic examples, but do not give this literal Zimin-word classification or its dyadic shell criterion. Schaeffer and Shallit (first public preprint August 2015) provide automatic-sequence decision procedures and closed-factor counts for other named infinite sequences; their listed sequence-specific results do not include finite Zimin words. Wojcik (2019 slides) describes the ruler-word representation and one-occurrence highest-letter factor parameterization; those background facts are used here but are not asserted to be novel. Parshina and Puzynina (2021 preprint) prove a general extremal asymptotic for closed factors, not the present exact Zimin distribution. For word length \(N=2^n-1\), the explicit density from this result is \(C_n/N^2\to1/9\), as compared to the universal extremal constant \(1/6\) in that later work; no extremality claim for Zimin words is made. Independent historical priority has not been established.

## Limitations

The argument requires distinct literal symbols \(a_r\) and the complete recursively defined finite words; it does not directly apply to arbitrary noninjective morphic images, altered center letters, or arbitrary prefixes of the infinite ruler word. It classifies distinct factors, not positioned occurrences or all border lengths. The finite checker is a reproducibility check and is not an independent proof or certification. A separate external review and a more exhaustive bibliographic priority examination remain outstanding.

## References

1. G. Badkobeh, G. Fici, Z. Lipták, *On the Number of Closed Factors in a Word*, arXiv:1305.6395 (first publicly submitted 2013-05-28), https://arxiv.org/abs/1305.6395 .
2. L. Schaeffer, J. Shallit, *Closed, Palindromic, Rich, Privileged, Trapezoidal, and Balanced Words in Automatic Sequences*, arXiv:1508.02074 (first public 2015-08-09), https://arxiv.org/abs/1508.02074 .
3. C. Wojcik, *The Zimin word and words with a Lyndon orbit*, CIRM research school slides (2019), https://www.cirm-math.fr/RepOrga/1991/Slides/Wojcik-Lyndon-CIRM.pdf .
4. O. Parshina, S. Puzynina, *Finite and infinite closed-rich words*, arXiv:2111.00863 (first public 2021-11-01), https://arxiv.org/abs/2111.00863 .
