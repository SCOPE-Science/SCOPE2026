# Exact dyadic string-attractor size of the powers-of-two indicator word

## Finding

Let \(p=p_1p_2\cdots\) be the binary word with \(p_i=1\) precisely when \(i\) is a positive power of two, and let \(P_k=p_1\cdots p_{2^k}\). If \(\gamma(w)\) is the minimum cardinality of a string attractor of \(w\), then for **every integer \(k\ge2\)**,

\[
\boxed{\gamma(P_k)=\left\lceil\frac{k}{2}\right\rceil+1.}
\]

The remaining dyadic cases satisfy \(\gamma(P_0)=\gamma(P_1)=1\). Both an optimal position set and a disjoint collection of uniquely occurring factors enforcing its size are given below. In particular the dyadic minimum is asymptotically half the size \(k\) produced by the greedy algorithm in the powers-of-two column of the 2026 experiments of Béal, Crochemore, and Romana (Table 2).

## Assumptions and scope

Positions are indexed from \(1\). For a finite word \(w=w_1\cdots w_n\), a set \(\Gamma\subseteq\{1,\ldots,n\}\) is a **string attractor** if each nonempty factor of \(w\) has at least one occurrence whose closed position interval intersects \(\Gamma\). Factors need not occur uniquely. The result concerns the precise prefixes of length \(2^k\) of \(p=1101000100000001\cdots\), not arbitrary prefix lengths or other sparse words.

For \(k\ge2\) put \(N=2^k\) and define

\[
\Gamma_k=\{2^t:1\le t\le k-1,\ t\text{ odd}\}
\ \cup\ \{2^{k-1},\,N-1\}.
\]

Here duplicate positions in the union are counted once. This gives \(|\Gamma_k|=\lceil k/2\rceil+1\).

## Proof

**Upper bound.** The one-positions of \(P_k\) are exactly \(1,2,4,\ldots,N\). Consider any nonempty factor \(u\).

If \(u\) contains at least two ones, one occurrence of \(u\) contains two consecutive one-positions \(2^t,2^{t+1}\), with \(0\le t<k\). Every such pair meets \(\Gamma_k\): among the exponents \(t,t+1\), either an odd exponent in \(1,\ldots,k-1\) is present, or the pair is the final one and contains \(2^{k-1}\). Thus that occurrence meets the attractor.

If \(u\) contains no ones, then \(u=0^a\). The longest zero-run in \(P_k\) is its final run, the positions \(N/2+1,\ldots,N-1\), of length \(N/2-1\). Any occurring \(0^a\) therefore has an occurrence ending at \(N-1\), a selected position.

Finally suppose that \(u\) contains exactly one one, so \(u=0^a10^b\), where \(a,b\ge0\). If \(b\ge1\), the unique one in any chosen occurrence is at a position \(2^t\) with \(t\le k-1\). The numbers of zeros immediately to the left and right of such a one are nondecreasing in \(t\), and attain their maxima among these centers at \(2^{k-1}\). Hence \(u\) occurs with its one centered at \(2^{k-1}\), which is selected. If \(b=0\) and \(a\ge1\), the longest run of zeros preceding a one is before the final one at \(N\). Therefore an occurrence ending at \(N\) crosses the selected \(N-1\). For \(a=b=0\), the factor \(1\) occurs at the selected position \(N/2\). These cases exhaust all factors, proving \(\gamma(P_k)\le|\Gamma_k|\).

**General lower-bound principle.** If \(s\) is a factor of a word that occurs exactly once, then every string attractor must meet the interval of that unique occurrence. A family of pairwise disjoint such occurrence intervals therefore gives a lower bound equal to its cardinality.

For any \(j\ge0\), define \(U_j=10^{2^{2j}-1}1\). The consecutive powers of two have pairwise distinct gaps, so in any \(P_k\) containing the indicated interval, \(U_j\) occurs **exactly once**, at

\[
I_j=[2^{2j},\,2^{2j+1}].
\]

For \(k=2m\) even, where \(m\ge1\), take \(U_j\) for \(0\le j<m\). Their \(m\) occurrence intervals are disjoint. Add \(0^{2^{k-1}-1}\), which occurs only in the final maximal zero-run, at

\[
J=[2^{k-1}+1,\,2^k-1].
\]

This is disjoint from every \(I_j\), yielding \(m+1=\lceil k/2\rceil+1\) forced positions.

For \(k=2m+1\) odd, where \(m\ge1\), let \(q=2^{2m-2}\), so \(N=8q\). Take \(U_j\) for \(0\le j<m\), whose final interval ends at \(2q\). Add the factors

\[
V=0^q10,\qquad W=0^{2q}1.
\]

The factor \(V\) occurs only at \([3q,4q+1]\): the one at \(4q\) is preceded by at least \(q\) zeros and followed by a zero, earlier ones have fewer than \(q\) preceding zeros, and the final one at \(8q\) has no following zero. The factor \(W\) occurs only at \([6q,8q]\): before every one other than \(8q\), there are at most \(2q-1\) immediately preceding zeros. Since \(q\ge1\), the intervals

\[
I_0,\ldots,I_{m-1},\ [3q,4q+1],\ [6q,8q]
\]

are pairwise disjoint. This forces \(m+2=\lceil k/2\rceil+1\) positions. The lower bounds equal the upper bound for both parities. For \(k=0,1\), the words are respectively \(1\) and \(11\), each with a one-position attractor. \(\square\)

## Verification

The accompanying standalone Python standard-library program `checker.py` constructs \(P_k\), \(\Gamma_k\), and the forced uniquely occurring factors. It exhaustively checks every distinct substring and its coverage for \(2\le k\le9\) (through word length \(512\)); it independently checks disjointness, specified occurrences, and uniqueness of all lower-bound witnesses for \(2\le k\le10\) (through word length \(1024\)). Overlapping occurrences are explicitly counted. The tested optimum sizes for \(k=2,\ldots,10\) are \(2,3,3,4,4,5,5,6,6\). The **infinite theorem rests on the preceding symbolic proof**, not on extrapolation from these tests.

## Relationship to prior work

Schaeffer and Shallit [2, Theorem 8 and Section 6] give explicit attractors for all length ranges of the powers-of-two indicator word. In particular their construction **already implies the upper bound of the present formula** at dyadic lengths. They explicitly note that the theorem supplies an upper bound and that a matching lower bound requires other techniques. The new portion here is the **sharp dyadic lower bound** for both parities, especially the pair of boundary-sensitive unique factors in the odd case, which combines with a constructive upper bound to establish the exact minimum for every dyadic length.

Béal, Crochemore, and Romana [1, Section 5, Table 2] give the sizes produced experimentally by a greedy algorithm on powers-of-two prefixes; at length \(2^k\), their reported size is \(k\) for \(k\ge2\). This is an algorithm output, not a proof that \(k\) positions are required. The present exact optimum is asymptotically smaller by a factor approaching two. Mantaci and coauthors [3] establish general foundational attractor properties, not this dyadic optimum. Related exact attractor classifications for Fibonacci and period-doubling words [4] concern different binary sequences.

## Limitations

No exact formula is claimed for non-dyadic prefix lengths, no enumeration of all optimal attractors is claimed, and no general theorem is claimed for arbitrary sparse sequences. The explicit upper-bound cardinality at dyadic lengths was already known from [2]; it is **not** claimed as new. Search and full-text comparisons found no earlier matching exact lower bound, but equivalent or independently discovered results may exist outside the inspected literature. No independent scientific audit has been performed.

## References

[1] M.-P. Béal, M. Crochemore, and G. Romana, *Checking and producing word attractors*, arXiv:2509.08503, originally posted 2025-09-10, revision v2 posted 2026-10-09, Section 5 and Table 2, https://arxiv.org/html/2509.08503v2.

[2] L. Schaeffer and J. Shallit, *String Attractors for Automatic Sequences*, arXiv:2012.06840v6, Section 6, Theorem 8, https://arxiv.org/pdf/2012.06840.

[3] S. Mantaci, A. Restivo, G. Romana, G. Rosone, and M. Sciortino, *A Combinatorial View on String Attractors*, Theoretical Computer Science 850 (2021), 236–248, DOI:10.1016/j.tcs.2020.11.006, https://iris.unipa.it/handle/10447/463264.

[4] M. Banbara et al., *The Smallest String Attractors of Fibonacci and Period-Doubling Words*, CPM 2026, DOI:10.4230/LIPIcs.CPM.2026.33.
