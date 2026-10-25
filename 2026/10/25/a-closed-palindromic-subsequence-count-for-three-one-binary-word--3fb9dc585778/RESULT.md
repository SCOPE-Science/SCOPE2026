# A closed palindromic-subsequence count for three-one binary words

## Finding

Let \(a,b,c,d\) be arbitrary nonnegative integers and let
\[
w=0^a1\,0^b1\,0^c1\,0^d,\qquad m=a+b+c+d.
\]
Write \(P(w)\) for the number of **distinct** palindromic scattered subsequence words of \(w\), including the empty word. An embedding is an order-preserving choice of positions, and multiple embeddings of the same word contribute once. Define
\[
\begin{aligned}
h&=\max\{\min(a,b+c+d),\min(a+b,c+d),\min(a+b+c,d)\},\\
x&=\min(a,d),\qquad y=\min(b,c),\\
E&=\begin{cases}\min(b,d-a)(c+1),&a\le d,\\\min(c,a-d)(b+1),&a\ge d.\end{cases}
\end{aligned}
\]
The two definitions of \(E\) agree when \(a=d\). Then the **exact all-parameter identity** is
\[
\boxed{P(w)=m+2+h+(x+1)(b+c+1)+(x+1)(y+1)+E.}
\]

There is also an exact restricted extremal consequence. Among the palindromic binary words with exactly three ones and length \(n=2s+3\), where \(s\ge0\), the unique maximizing word is
\[
0^{\lfloor s/2\rfloor}1\,0^{\lceil s/2\rceil}1\,0^{\lceil s/2\rceil}1\,0^{\lfloor s/2\rfloor}.
\]
Its distinct palindromic-subsequence count is
\[
\boxed{\begin{cases}3t^2+11t+4,&s=2t,\\3t^2+14t+10,&s=2t+1.\end{cases}}
\]
Uniqueness here concerns the palindromic source-word class, not arbitrary weight-three words.

## Assumptions and scope

All alphabets are binary, all exponents are nonnegative integers, the source contains **exactly three** occurrences of the symbol one, and the source is linear, not circular. The empty scattered subsequence is included; its inclusion shifts every nonempty-only count upward by one. The count is by distinct subsequence *strings*, not by multiplicity of embeddings or by contiguous factors. The restricted optimum is only over source words invariant under reversal; these have odd length because their unique central one is fixed.

## Proof

Every palindrome scattered from \(w\) contains \(j\) ones for exactly one \(j\in\{0,1,2,3\}\); these four disjoint types can be counted separately.

**Zero ones.** The words \(0^i\) for \(0\le i\le m\) all occur, yielding \(m+1\) distinct palindromes.

**One one.** Every such palindrome is uniquely of the form \(0^i1\,0^i\). Choosing the first, second or third source one as its central one gives, respectively, the admissible lengths
\[
0\le i\le\min(a,b+c+d),\quad
0\le i\le\min(a+b,c+d),\quad
0\le i\le\min(a+b+c,d).
\]
The union of three initial integer intervals is precisely \(0\le i\le h\), giving \(h+1\) words.

**Two ones.** Every such palindrome is \(0^i1\,0^j1\,0^i\) with \(i,j\ge0\). Choosing any pair of the three source ones produces a down-closed rectangle in the \((i,j)\)-plane. For the first and third, it is
\[
0\le i\le x,\qquad0\le j\le b+c,
\]
with \((x+1)(b+c+1)\) lattice points. If \(a\le d\), the first-and-second rectangle is entirely contained in this rectangle: it has \(i\le a=x\) and \(j\le b\). Only the second-and-third rectangle can add new points, namely
\[
a<i\le\min(a+b,d),\qquad0\le j\le c.
\]
It adds \(\min(b,d-a)(c+1)\) distinct points. If \(a\ge d\), reverse the source word; the analogous new rectangle has \(d<i\le\min(a,c+d)\) and \(0\le j\le b\), giving \(\min(c,a-d)(b+1)\) new points. Thus the two-one count is exactly \((x+1)(b+c+1)+E\). In particular, all intersections and zero-length gaps are handled by the rectangle decomposition, not by an independence assumption.

**Three ones.** Any palindrome using all three source ones has the unique form \(0^i1\,0^j1\,0^j1\,0^i\). The left and right exterior zero requirements give \(0\le i\le\min(a,d)=x\), while the two interior requirements give \(0\le j\le\min(b,c)=y\). These disjoint source intervals can be chosen independently, hence there are \((x+1)(y+1)\) words. Adding the four disjoint counts proves the identity.

Finally, a three-one word is itself palindromic precisely when \(a=d\) and \(b=c\). Put \(a=d=u\), \(b=c=v\), so \(s=u+v\). In this case \(h=u+v\), \(E=0\), and direct substitution gives
\[
P(w)=3uv+5u+6v+4
=-3u^2+(3s-1)u+6s+4.
\]
The concave parabola has real vertex \(u=s/2-1/6\). For integer \(u\in\{0,\ldots,s\}\), its unique maximizer is \(u=\lfloor s/2\rfloor\), with \(v=\lceil s/2\rceil\). Substitution with \(s=2t\) and \(s=2t+1\) gives the two stated formulas, including \(s=0\).

## Verification

The accompanying standalone `checker.py` independently enumerates all potential palindrome strings and tests greedy subsequence membership for every four-gap composition with at most twelve zeros (1,820 cases). A separate interval dynamic program for distinct palindromic subsequences checks all four-gap compositions with at most eighteen zeros (7,315 cases). Restricted maximizers are additionally checked for all \(0\le s\le100\). These are finite regression checks, not replacements for the all-parameter proof.

Run from the directory containing this document and the checker: `python3 checker.py`.

## Relationship to prior work

Elzinga, Rahmann and Wang (2008) study general subsequence counting algorithms; a general counting algorithm does not itself give this explicit sparse-word, four-gap identity or its palindromic-source equality case. Guo, Shallit and Shur (2015) study conjugates, palindromic pairs, rich words and antipalindromes—primarily contiguous-factor structure rather than distinct *scattered palindromic subsequences*. Neither comparison establishes absolute priority; see the associated originality assessment for access limits.

The statistic also differs from the unrestricted distinct-subsequence count of a three-one binary word. For example, the two words corresponding to zero gaps \((0,0,3,2)\) and \((0,4,0,1)\) each have 48 distinct scattered subsequences in total, but have respectively 14 and 15 distinct palindromic scattered subsequences. Therefore a total-subsequence count alone does not determine the statistic.

## Limitations

The explicit formula and palindrome-restricted optimizer are proved. **No** claim is made that the displayed palindromic word maximizes the statistic among *all* binary words of the same weight and length. The full unrestricted extremal classification and its equality cases remain outside this result. The exact formula assumes precisely three source ones; extension to more ones is not established. Computations are finite, while the stated theorem is established by the combinatorial case analysis. No independent external audit has been performed.

## References

- C. H. Elzinga, S. Rahmann, H. Wang, *Algorithms for Subsequence Combinatorics*, Theoretical Computer Science 409(3), 394–404 (2008), doi:10.1016/j.tcs.2008.08.035. Author research-page overview: https://www.rahmannlab.de/research/subseqcomb.html .
- C. Guo, J. Shallit, A. M. Shur, *On the Combinatorics of Palindromes and Antipalindromes*, arXiv:1503.09112, first posted 2015-03-31; https://arxiv.org/abs/1503.09112 .
