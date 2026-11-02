# Minimum string attractors for permutation-periodic prefixes: a single boundary obstruction

## Finding
For a labeled alphabet \(\Sigma=\{0,1,\ldots,q-1\}\), \(q\ge2\), put \(P=0\,1\,\cdots\,(q-1)\). For integers \(m\ge1\) and \(0\le r<q\), define the **linear** word \(W=P^m(0\,1\,\cdots\,(r-1))\), of length \(N=mq+r\); the last factor is empty when \(r=0\). A string attractor is a set \(\Gamma\subseteq\{1,\ldots,N\}\) that crosses at least one occurrence of every nonempty contiguous factor of \(W\). All smallest attractors have size \(q\), and they contain precisely one position of each symbol.

For \(m=1\) or \(r=q-1\), **every** such one-per-symbol choice is a smallest attractor. For \(m\ge2\), \(r\le q-2\), the only forbidden choices are exactly those satisfying all of the following:

1. The selected position of symbol \(r\) is its first occurrence, \(r+1\).
2. The selected position of symbol \(q-1\) is its last occurrence in the full periods, \(mq\).
3. For every symbol \(j<r\), its selected position is either \(j+1\) or \(mq+j+1\).

No restriction is imposed on the selected occurrence of a symbol \(r<j<q-1\). All forbidden choices fail to intersect **the same single factor** \(U_r=(q-1)\,0\,1\,\cdots\,r\). Hence the number \(C(q,m,r)\) of distinct smallest attractors is
\[
C(q,m,r)=\begin{cases}
2^r,&m=1,\\
m(m+1)^{q-1},&m\ge2,\ r=q-1,\\
m^{q-r}(m+1)^r-2^r m^{q-r-2},&m\ge2,\ 0\le r\le q-2.
\end{cases}
\]
For \(q=2,r=0,m\ge2\), the \(m^2-1\) special case has previously been published and is **not** asserted to be novel; the multi-symbol partial-prefix classification is the subject of this finding.

## Assumptions and scope
All factors are ordinary **linear** contiguous substrings, not cyclic factors or scattered subsequences. Positions are indexed from one and the alphabet symbols are distinct labels. Minimum means minimum cardinality, not inclusion-minimality. The assertions hold for all integers in the stated ranges, including \(m=1\), \(q=2\) and \(r=0\). There is no claim concerning arbitrary periods with repeated symbols.

## Proof

**Minimum cardinality.** Each of the \(q\) one-letter factors forces a marked position carrying its own letter. Thus at least \(q\) positions are needed. Every factor has an occurrence starting among positions \(1,\ldots,q\): shift any occurrence left by whole periods until its start is within the first period. That earliest occurrence intersects its start, so \(\Gamma_0=\{1,\ldots,q\}\) is an attractor of size \(q\). Therefore every minimum set chooses exactly one occurrence of each symbol.

**The single-full-period case.** When \(m=1\), every symbol \(j\ge r\) occurs once and its position is necessarily selected. Consequently every factor containing one of these symbols is covered. A factor containing only symbols less than \(r\) is a contiguous increasing block, occurring both in the initial and terminal copies of \(0,1,\ldots,r-1\). For any letter within that factor, whichever of its two occurrences is selected lies inside one of the two occurrences of the entire factor. All factors are therefore covered for every one-per-letter selection. There are \(2^r\) choices.

Assume now \(m\ge2\). Fix a factor \(u\) of length \(\ell\), and let \(s\in\{1,\ldots,q\}\) be the position of its **earliest** occurrence. The possible start positions of \(u\) are exactly \(s,s+q,\ldots,s+tq\), as far as they fit into \(W\), because each letter of one period is distinct. In particular, there are no other starts.

**Short-factor case, \(1\le\ell<q\).** If \(s+\ell-1\le q\), the factor fits within one period. If its last symbol has index less than \(r\), every copy of each symbol it contains (including the suffix copy) is covered by an occurrence of \(u\). Otherwise the factor contains a symbol of index at least \(r\), all whose copies are in full periods and are covered by the repeated occurrences of \(u\). Either way some selected position lies in an occurrence. Thus a missed factor must wrap across a period boundary.

Put \(t=s+\ell-1-q\), so \(1\le t<q\). The factor then has the form \(s-1,s,\ldots,q-1,0,\ldots,t-1\). If \(t\le r\), a copy begins in each of the \(m\) complete periods, the last extending into the suffix when necessary; hence every occurrence of symbol \(q-1\) lies in an occurrence of \(u\), making it impossible to miss. If \(t>r\), only the first \(m-1\) crossing occurrences fit. For the selected positions to avoid all of them, the symbol \(q-1\) must be chosen at \(mq\), symbol \(r\) must be chosen at \(r+1\), and each \(j<r\) must be chosen in the initial prefix or final appended suffix. These are precisely the three restrictions in the finding. This includes the length-one boundary trivially (a singleton cannot be missed).

**Long-factor case, \(\ell\ge q\).** The occurrence intervals \([s+iq,s+iq+\ell-1]\) overlap or touch. Their union is therefore one interval \([s,e]\), with \(s\le q\) and \(N-e<q\), because the final occurrence cannot be extended by another shift of \(q\). If an entire one-per-letter set avoids \([s,e]\), every marked position lies in the initial prefix \([1,s-1]\) or terminal suffix \([e+1,N]\), both shorter than \(q\). The initial prefix has no symbol \(q-1\); hence the chosen \(q-1\) lies in the terminal suffix, which can only mean position \(mq\). As the suffix contains fewer than \(q\) letters and ends with symbol \(r-1\) (interpreted as \(q-1\) if \(r=0\)), a suffix containing \(q-1\) must contain the appended \(0,\ldots,r-1\) but **cannot** contain symbol \(r\). Thus the selected occurrence of symbol \(r\) must be its first position \(r+1\), in the initial prefix. Likewise every selected symbol \(j<r\) lies at either \(j+1\) or \(mq+j+1\). Once again any missed factor forces the three restrictions.

If \(r=q-1\), the first two restrictions demand that one and the same symbol \(q-1\) be selected both at its first and last occurrences, impossible because \(m\ge2\). Thus all one-per-symbol sets are attractors for this case.

**Sharpness and enumeration.** If \(r\le q-2\), \(U_r=(q-1)0\cdots r\) occurs only at starts \(q,2q,\ldots,(m-1)q\). None of these occurrences crosses a selected position satisfying the restrictions: each \(j<r\) was selected at one of the two boundary copies, the selected \(r\) precedes all starts, the selected \(q-1\) follows all starts, and no other letter belongs to \(U_r\). Hence every restricted choice really fails. The total number of one-per-symbol choices is \(m^{q-r}(m+1)^r\). Exactly \(2^r m^{q-r-2}\) are restricted: two options for each \(j<r\), one forced choice for \(r\) and for \(q-1\), and \(m\) options for every remaining symbol. Subtracting proves the formula. For \(r=q-1\) there are \(m(m+1)^{q-1}\) unrestricted choices. The proof is complete.

## Verification
The attached standalone script `verify.py` enumerates every size-\(q\) candidate for alphabet sizes \(2\le q\le6\), with \(1\le m\le5\) when \(q\le5\), and \(1\le m\le3\) for \(q=6\). It checks the complete set of literal substrings independently of the theorem's substring-periodicity argument, compares the exact marked-set predicate, and checks the counting formula and the specified obstruction occurrences. Its output is `VERIFY_OK parameter_cases=88 candidate_sets=52430 valid_sets=51595 invalid_sets=835 alphabet_sizes=2..6 complete_factors=True`. The finite checks corroborate, but do not replace, the universal proof above.

## Relationship to prior work
String attractors were introduced as a compression-independent factor-covering notion by Prezza (arXiv:1709.05314, initially submitted 2017-09-15). Kempa, Policriti, Prezza and Rotenberg (arXiv:1803.01695) developed general verification, optimization and suffix-tree reductions. Restivo, Romana and Sciortino (arXiv:2206.00376) studied attractor-profile and position-distribution measures for infinite words; Banbara and coauthors (arXiv:2602.16152) classified all smallest attractors of several morphic word families. These results frame the problem but do not state the present all-prefix finite-period enumeration. A publicly posted classification of \((01)^m\) already gives \(m^2-1\) optimal pairs; this known binary full-period case is an explicit overlap rather than new evidence. Unlike a size-only attractor bound, the present statement identifies **all** optimal selections and proves that one boundary factor detects every failure among one-per-symbol sets.

## Limitations
The result applies only when the repeating period contains every alphabet symbol exactly once and the terminal appendage is an initial segment of that period. It is a characterization of minimum-cardinality attractors, not all inclusion-minimal sets of larger size. The standalone finite checker cannot establish the infinite quantifiers. Although relevant primary sources and public results were compared, the possibility of a previous implicit equivalent specialization cannot be excluded without an independent literature review.

## References
1. N. Prezza, *String Attractors*, arXiv:1709.05314, submitted 2017-09-15. https://arxiv.org/html/1709.05314v2
2. D. Kempa, A. Policriti, N. Prezza, E. Rotenberg, *String Attractors: Verification and Optimization*, arXiv:1803.01695, submitted 2018-03-05. https://arxiv.org/abs/1803.01695
3. A. Restivo, G. Romana, M. Sciortino, *String Attractors and Infinite Words*, arXiv:2206.00376, submitted 2022-06-01. https://arxiv.org/abs/2206.00376
4. M. Banbara et al., *The Smallest String Attractors of Fibonacci, Period-Doubling, and Thue–Morse Words*, arXiv:2602.16152, submitted 2026-02-18. https://arxiv.org/html/2602.16152v3
