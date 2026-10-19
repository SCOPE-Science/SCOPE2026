# Circular palindrome spectra of binary words with three marked positions

## Finding
Let \(n\ge3\) and let \(w\) be a binary circular word of length \(n\) with exactly three occurrences of \(1\). In a fixed cyclic orientation, let \(a,b,c\ge0\) be the consecutive numbers of zeros between these occurrences, so \(a+b+c=n-3\). Define \(P(w)\) as the number of **distinct nonempty palindromic circular factors of lengths at most \(n\)**. Put \(\alpha\le\beta\le\gamma\) for the sorted multiset \(\{a,b,c\}\). Then the complete all-length classification is

\[
P(w)=\begin{cases}
2n-2-\gamma,&\alpha<\beta<\gamma,\\
n+1+\lfloor(n-3)/2\rfloor,&\text{exactly two gaps are equal},\\
n+\lfloor\alpha/2\rfloor,&\alpha=\beta=\gamma.
\end{cases}
\]

For every \(n\ge14\), the maximum within this three-one family is
\[
M_3(n)=2n-2-\lceil n/3\rceil
=\begin{cases}
5m-2,&n=3m,\\
5m-1,&n=3m+1,\\
5m+1,&n=3m+2.
\end{cases}
\]
All maximizers have distinct gaps. Up to permutation, their **complete list** is
\[
\begin{array}{c|l}
n&\text{optimal gap multisets}\\\hline
3m&(m-2,m-1,m)\\
3m+1&(m-3,m,m+1),\ (m-2,m-1,m+1)\\
3m+2&(m-2,m,m+1).
\end{array}
\]
Thus there is exactly one dihedral class of maximizing three-one circular words for \(n\equiv0,2\pmod3\) and exactly two for \(n\equiv1\pmod3\), for every \(n\ge14\). For \(n\ge14\) and distinct gaps the exact deficit from the restricted maximum is \(\gamma-\lceil n/3\rceil\).

## Assumptions and scope
A circular factor of length \(\ell\) is the length-\(\ell\) sequence encountered from any of the \(n\) possible starting positions while reading clockwise, with \(1\le\ell\le n\); equal sequences are counted once, not once per occurrence. The empty word is not counted. Reversal or rotation changes neither the count nor the gap multiset. The theorem concerns circular binary words of **exactly** three ones, not an unrestricted binary circular-word maximum.

## Proof
Write \(S=a+b+c=n-3\). Every circular factor of length at most \(n\) contains between zero and three ones. These four possibilities give a complete, disjoint partition of its palindromes.

**Zero ones.** These factors are \(0^r\), for \(1\le r\le\gamma\), giving \(\gamma\) distinct palindromes.

**Exactly one one.** Such palindromes have the form \(0^r1 0^r\). Around a given occurrence of \(1\), the maximum possible \(r\) is the minimum of the two neighboring zero gaps. Taking the maximum over the three ones gives the median gap \(\beta\). Therefore exactly \(\beta+1\) such palindromes occur.

**Exactly two ones.** Their form is \(0^r1 0^s1 0^r\), where \(s\) equals one of the cyclic gaps. For an occurrence of the gap \(s\), the two neighboring gaps bound \(r\) by their minimum; conversely every \(r\) in that interval yields the indicated circular factor. Distinct values of \(s\) give disjoint palindromes. If all gaps are distinct \(\alpha<\beta<\gamma\), the three choices \(s=\alpha,\beta,\gamma\) contribute respectively \(\beta+1,\alpha+1,\alpha+1\), for a total \(\beta+2\alpha+3\). If exactly two gaps are equal to \(t\) and the remaining gap is \(u\), the two distinct choices contribute \(\min(t,u)+1\) and \(t+1\). If all gaps are \(t\), there are \(t+1\) such palindromes.

**Exactly three ones.** They have the form \(0^r1 0^s1 0^s1 0^r\): the two internal zero gaps must coincide because the middle one is the palindrome center. If all gaps are distinct there are none. If precisely two gaps equal \(t\), with third gap \(u\), there are exactly \(\lfloor u/2\rfloor+1\) such palindromes, indexed by \(0\le r\le\lfloor u/2\rfloor\). If all three gaps equal \(t\), there are \(\lfloor t/2\rfloor+1\) distinct such palindromes. There can be no further types because any factor of length at most \(n\) contains at most three ones.

Adding the four counts for pairwise distinct gaps gives
\[
\gamma+(\beta+1)+(\beta+2\alpha+3)
=2S+4-\gamma=2n-2-\gamma.
\]
For gaps \((t,t,u)\) with \(u\ne t\), addition gives
\[
P=3t+u+\lfloor u/2\rfloor+4
=n+1+t+\lfloor u/2\rfloor
=n+1+\lfloor S/2\rfloor.
\]
For three equal gaps \(t\), it gives \(3t+3+\lfloor t/2\rfloor=n+\lfloor t/2\rfloor\). This proves the complete classification for every \(n\ge3\).

To maximize when gaps are distinct, write \(\alpha<\beta<\gamma\), with \(\alpha+\beta+\gamma=n-3\). Since \(\alpha\le\gamma-2\) and \(\beta\le\gamma-1\), one has \(n-3\le3\gamma-3\), and hence \(\gamma\ge\lceil n/3\rceil\). The listed optimal triples have nonnegative, strictly increasing entries for \(n\ge14\), sum to \(n-3\), and attain equality. The requirement \(\alpha<\beta<\gamma\), with \(\gamma=\lceil n/3\rceil\), leaves exactly the listed multisets, by solving \(\alpha+\beta=n-3-\gamma\) with \(0\le\alpha<\beta<\gamma\).

The largest value when exactly two gaps coincide is \(n+1+\lfloor(n-3)/2\rfloor\), and the three-equal case gives a strictly smaller count whenever it is possible. Their gap from the distinct-gap optimum is
\[
\lceil(n-3)/2\rceil-\lceil n/3\rceil,
\]
which is positive at \(n=14\), and is at least one for every \(n\ge15\) because \((n-3)/2\ge n/3+1\). Thus all maximizers have distinct gaps. The residue formulas and the exact deficit follow immediately. With distinct gaps, cyclic rotation identifies three of the six gap orderings, while reversal identifies the other three. Hence each optimal gap multiset gives one dihedral class, completing the proof.

## Verification
The standalone `verify.py` independently constructs every circular binary word with three ones, enumerates its actual palindromic factors as strings, and compares the resulting count to the formula for all \(2{,}300\) ordered gap triples of lengths \(3\le n\le25\). It separately enumerates \(2{,}274{,}994\) ordered gap triples for \(14\le n\le240\) to verify the claimed maxima and their exhaustive sorted optimal gap triples. The command `python3 verify.py` returns `VERIFY_OK`. These experiments corroborate the proof; they do not replace the arbitrary-length arguments above.

## Relationship to prior work
Simpson (2014) proved a general bound strictly below \(5n/3\) for the number of distinct circular palindromic factors and exhibited near-sharp families when \(3\mid n\). The previously described Biggles family is a three-marker construction attaining the \(5n/3-2\) value in that residue class; **that special construction and general bound are not claimed as new**. The result here is the complete three-marker count for every gap triple, the exact all-length restricted extremum for \(n\ge14\), the classification of all restricted maximizers in each residue class, and the sharp deficit law. OEIS A247000 gives finite unrestricted maxima through length 30 and a conjectural recurrence, neither of which implies this three-marker classification.

## Limitations
This does not determine the unrestricted maximum among all binary circular words. It makes no claim about factors longer than one circuit or about alphabets larger than two. The precisely known near-sharp three-marker family makes comparison with Simpson's 2014 article particularly important: the accessible abstract and indexed metadata were inspected, but its complete text could not be obtained in this investigation. An unrecognized stronger result or implicit classification in that article remains an originality risk.

## References
1. Jamie Simpson, *Palindromes in circular words*, Theoretical Computer Science **550** (2014), 66–78, DOI: `10.1016/j.tcs.2014.07.012` (first publicly available online July 22, 2014).
2. OEIS, A247000, *Maximal number of palindromes in a circular binary word of length n*, https://oeis.org/A247000 (finite data and conjectural formula).
3. OEIS, A246999, *Biggles words*, https://oeis.org/A246999 (a previously known near-extremal sparse circular-word construction).
