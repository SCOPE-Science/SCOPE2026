# Exact palindromic-defect distribution of five-run binary words

## Finding

For arbitrary positive integers \(a,b,c,d,e\), consider the five-run binary word \(w=0^a1^b0^c1^d0^e\) of length \(n=a+b+c+d+e\). Let \(p(w)\) be the number of **distinct nonempty contiguous palindromic factors**, with equal strings counted once irrespective of multiplicity. The *palindromic defect* is \(D(w)=n-p(w)\).

**Exact defect theorem.** For every such five-tuple,
\[
D(w)=\mathbf{1}_{b\ne d}\max\{0,\min(a,e)-c\}.
\]
Consequently the word is *rich* (has zero defect) exactly when \(b=d\) or \(c\ge\min(a,e)\). A word of at most four maximal runs is always rich.

**Complete joint distribution.** Let \(H_{n,r}\) count the five-run binary words of length \(n\), beginning with \(0\), with defect exactly \(r\). Then
\[
\sum_{n\ge5}\sum_{r\ge0}H_{n,r}z^ny^r
=\frac{z^5}{(1-z)^5}
+\frac{2z^8}{(1-z)^3(1-z^3)}\left(\frac{y}{1-z^2y}-\frac{1}{1-z^2}\right).
\]
For every \(r\ge1\), an equivalent exact expression is
\[
\sum_{n\ge5}H_{n,r}z^n=\frac{2z^{2r+6}}{(1-z)^3(1-z^3)},
\quad
H_{n,r}=2\sum_{0\le j\le\lfloor(n-2r-6)/3\rfloor}\binom{n-2r-4-3j}{2},
\]
where the sum is defined to be zero for \(n<2r+6\). The zero-defect counts follow by subtracting all positive-defect counts from \(\binom{n-1}{4}\).

For uniformly chosen length-\(n\) five-run binary words (allowing either initial symbol), the probability of positive defect tends to \(1/3\) and the expected defect is \(n/30+O(1)\). The maximum possible defect is
\[
\max D(w)=\max\{0,\lfloor(n-6)/2\rfloor\}\quad(n\ge5).
\]

## Assumptions and scope

All run lengths are positive integers and the alphabet is \(\{0,1\}\). A factor is **contiguous**, not a scattered subsequence; the empty palindrome is excluded from \(p(w)\). The count \(H_{n,r}\) uses the unique five-run representation beginning with \(0\); complementing every symbol bijects this with the family beginning with \(1\) and preserves \(D\), hence all proportions and mean values are the same with both initial symbols allowed. The initial symbol and five-run restriction are essential to the stated enumerator. All identities apply to every indicated integer parameter, not merely to bounded examples.

## Proof

**Classification of palindromic factors.** Any nonconstant binary palindrome must have an odd number of maximal runs, since its initial and terminal symbols coincide; as a factor of \(w\), it consequently has either three or five runs. The following classes exhaust all distinct nonempty palindromic factors and separate them by their run profiles:

1. Constant palindromes \(0^i\) for \(1\le i\le h:=\max(a,c,e)\), and \(1^i\) for \(1\le i\le j:=\max(b,d)\). Together there are \(h+j\).
2. Three-run palindromes \(0^i1^b0^i\) for \(1\le i\le\min(a,c)\), and \(0^i1^d0^i\) for \(1\le i\le\min(c,e)\). A three-run factor must traverse its whole interior run, so these are exhaustive. The two families intersect only when \(b=d\); in that case the intersection has \(\min(a,c,e)\) words.
3. Three-run palindromes \(1^i0^c1^i\) for \(1\le i\le\min(b,d)\). The central zero block must be traversed in full.
4. Five-run palindromes must be \(0^i1^b0^c1^d0^i\). They exist exactly when \(b=d\) and \(1\le i\le\min(a,e)\). No other five-run factor of \(w\) can be palindromic.

The classes with different run profiles or central symbols are disjoint. With \(I=\mathbf{1}_{b=d}\) and \(x=\min(a,e)\), their total is therefore
\[
\begin{aligned}
p(w)={}&\max(a,c,e)+\max(b,d)+\min(a,c)+\min(c,e)\\
&{}-I\min(a,c,e)+\min(b,d)+I\min(a,e).
\end{aligned}
\]
Writing \(v=\max(a,e)\), a three-case comparison (\(c\le x\), \(x<c\le v\), and \(c>v\)) gives the exact identity
\[
\max(a,c,e)+\min(a,c)+\min(c,e)=v+c+\min(x,c).
\]
Also \(\max(b,d)+\min(b,d)=b+d\) and \(\min(a,c,e)=\min(x,c)\). Hence
\[
p(w)=n-(1-I)(x-\min(x,c)),
\]
which proves the defect theorem.

For words with four runs, the same one- and three-run classification yields \(p(0^a1^b0^c1^d)=\max(a,c)+\max(b,d)+\min(a,c)+\min(b,d)=a+b+c+d\). Taking factors handles one-, two-, and three-run words. Thus four or fewer runs are rich.

**Counting positive defects.** Fix \(r\ge1\). The defect formula forces \(b\ne d\), \(c\ge1\), and \(\min(a,e)=c+r\). In ordinary generating functions, positive unequal ordered pairs \((b,d)\) contribute
\[
\sum_{b,d\ge1,\ b\ne d}z^{b+d}
=\frac{z^2}{(1-z)^2}-\frac{z^2}{1-z^2}
=\frac{2z^3}{(1-z)^2(1+z)}.
\]
For fixed \(m=\min(a,e)\), the ordered pairs \((a,e)\) contribute
\[
\sum_{a,e\ge1,\ \min(a,e)=m}z^{a+e}
=z^{2m}\frac{1+z}{1-z}.
\]
Substituting \(m=c+r\), multiplying by the middle-zero weight \(z^c\), and summing over \(c\ge1\) gives
\[
\sum_{\substack{a,b,c,d,e\ge1\\D(w)=r}}z^{a+b+c+d+e}
=\frac{2z^{2r+6}}{(1-z)^3(1-z^3)}.
\]
Expanding \((1-z)^{-3}=\sum_{k\ge0}\binom{k+2}{2}z^k\) and \((1-z^3)^{-1}=\sum_{j\ge0}z^{3j}\) yields the displayed coefficient formula. All five-run positive compositions contribute \(z^5/(1-z)^5\) when unmarked; subtracting the unmarked positive-defect generating series and adding its \(y\)-marked version gives the displayed bivariate identity.

**Consequences.** The positive-defect ordinary generating function is
\[
\sum_{n\ge5}\sum_{r\ge1}H_{n,r}z^n
=\frac{2z^8}{(1-z)^3(1-z^3)(1-z^2)}.
\]
Its leading singular term at \(z=1\) is \(\frac13(1-z)^{-5}\). Since \(\binom{n-1}{4}=n^4/24+O(n^3)\) and all other poles have lower order, asymptotically \(1/3\) of five-run words are non-rich. Differentiating the bivariate series in \(y\) and setting \(y=1\) produces the first-moment generating function
\[
\sum_{n\ge5}\left(\sum_{r\ge0}rH_{n,r}\right)z^n
=\frac{2z^8}{(1-z)^3(1-z^3)(1-z^2)^2}.
\]
Its leading singular term is \(\frac16(1-z)^{-6}\), so the total defect over all beginning-zero words is \(n^5/720+O(n^4)\). Dividing by \(\binom{n-1}{4}\) gives \(\mathbb E[D]=n/30+O(1)\). Finally, positive defect \(r\) requires \(a,e\ge r+1\), \(c\ge1\), and \(b+d\ge3\), hence \(n\ge2r+6\). Conversely, \((a,b,c,d,e)=(r+1,1,1,2,r+1)\) realizes \(r\) at length \(2r+6\); increasing \(a\) supplies every greater length without changing the defect. This proves the sharp maximum, with zero for lengths 5–7.

## Verification

The included standalone \(\texttt{verify.py}\) needs only Python 3. It constructs actual distinct contiguous palindromic factors by expanding around every possible center, and checks the defect theorem against that independent implementation on every five-tuple with entries in \(\{1,2,3,4,5\}\), totaling 3,125 instances. It checks that all 625 four-run tuples with entries at most 5 have zero defect. For each length from 5 through 26 it independently enumerates all positive five-part compositions, compares the entire defect histogram with coefficients of the displayed bivariate series, checks the first moment and maximum, and verifies the count of compositions. The script prints \(\texttt{VERIFY_OK}\) on success. These finite experiments check arithmetic and classification boundaries; the unrestricted claims follow from the preceding proof, not from extrapolation.

## Relationship to prior work

Currie, Mol and Rampersad (2019, arXiv:1908.03169) develop structural and critical-exponent results for infinite binary rich words, furnishing a motivating study of the same palindromic-richness invariant. The earlier run-length treatment of Guo, Shallit and Shur (2015 preprint, published 2016) provides sufficient run-inequality criteria and global rich-word growth estimates. The specialized richness condition here may be a consequence of their general necessary-and-sufficient characterization; no priority is asserted for that qualitative criterion alone. The quantitative claim is the complete **positive palindromic-defect law and its bivariate distribution**, which are not statements of the inspected preprint. Mahalingam, Maity and Pandoh (2023) characterize words for which *every* block reversal is rich; that is a stronger different predicate, not an enumeration of the defects of individual five-run words. The exact zero-defect distribution and first-moment asymptotic do not follow merely from these statements without an additional quantitative factor classification.

## Limitations

This is an exact restricted-family result, not a formula for unrestricted binary words or words over larger alphabets. The earliest known non-rich length and general notion of rich words are prior knowledge. Research in the inaccessible journal-version text or unindexed literature could contain an equivalent quantitative five-run formula; the 2015 public preprint and other directly relevant primary sources were read for the comparison. The asymptotic assertions include lower-order error terms, not exact finite-length expectation formulas beyond their generating functions. The computational checks are finite, not an independent proof or independent audit.

## References

- J. D. Currie, L. Mol, and N. Rampersad, *The repetition threshold for binary rich words*, arXiv:1908.03169, first public 2019-08-08; *Discrete Mathematics & Theoretical Computer Science* 22(1), 2020. Primary MSC 68R15.
- C. Guo, J. Shallit, and A. M. Shur, *On the Combinatorics of Palindromes and Antipalindromes*, arXiv:1503.09112, publicly submitted 2015-03-31, especially Section 4. Related journal article: *Palindromic rich words and run-length encodings*, *Information Processing Letters* 116 (2016), 735–738, doi:10.1016/j.ipl.2016.07.001.
- K. Mahalingam, A. Maity, and P. Pandoh, *Rich Words in the Block Reversal of a Word*, arXiv:2302.02109 (2023), especially Proposition 4.17 and Theorem 4.21.
- E. Pelantová and Š. Starosta, *On Words with the Zero Palindromic Defect*, arXiv:1708.06911 (2017), for general background on palindromic defect and richness.
