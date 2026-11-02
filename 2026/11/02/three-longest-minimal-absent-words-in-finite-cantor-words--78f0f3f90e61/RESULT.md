# Three longest minimal absent words in finite Cantor words

## Finding

Let \(C_0=1\) and define finite binary words by the morphism \(\mu(1)=101\), \(\mu(0)=000\), so \(C_k=\mu^k(1)\). For every integer \(k\ge2\), put \(G=3^{k-1}\), \(H=3^{k-2}\), \(W=C_{k-1}\), and \(V=C_{k-2}\). The longest minimal absent factors of the **linear** finite word \(C_k\), over the fixed alphabet \(\{0,1\}\), have length exactly \(G+2\), and their complete set is

\[
\left\{\,0W0,\quad 0^{H+1}V0^{H+1},\quad 1\,0^H V0^H1\,\right\}.
\]

In particular, there are exactly three maximal-length minimal absent words at every level \(k\ge2\). The structural refinement is that the only two *distinct* repeated factors of length \(G\) are \(W\), occurring at positions \(0,2G\), and \(F=0^H V0^H\), occurring at positions \(H,2G-H\); no factor of length \(G+1\) repeats. All positions are zero-based.

## Assumptions and scope

A factor is a contiguous linear substring. A minimal absent word \(z\) does not occur in the host word, while every proper factor of \(z\) does. For \(|z|\ge2\), the latter condition is equivalent to the occurrence of both its length-\((|z|-1)\) prefix and suffix. The host is the finite word \(C_k\), not the infinite fixed point, its circularization, or a word weighted by the multiplicities of occurrences. Repeated occurrences may overlap; repeated *factors* are distinct strings having at least two starts. All powers in displayed words denote ordinary concatenation.

## Proof

**1. Recursive geometry.** Since the morphism fixes zero blocks by tripling their lengths,
\[
C_j=C_{j-1}\,0^{3^{j-1}}\,C_{j-1}\qquad(j\ge1).
\]
The length is \(3^j\); each \(C_j\) starts and ends in \(1\). For \(j\ge1\), its longest zero run has length \(3^{j-1}\), since the separating run has that length and the two smaller copies have strictly shorter runs.

The longest proper border of \(C_j\) has length \(3^{j-1}\). Indeed, let \(B=C_{j-1}\), \(T=|B|=3^{j-1}\), and write \(C_j=B0^TB\). Its prefix and suffix of length \(T\) are both \(B\). A putative border of length strictly between \(T\) and \(2T\), inclusive, would have a prefix ending in \(0\) and a suffix ending in \(1\). A putative border longer than \(2T\), but shorter than \(3T\), would contain the entire separating run \(0^T\) in both prefix and suffix at different offsets; this is impossible because \(0^T\) occurs at only one position in \(C_j\). Thus no longer proper border exists. The same reasoning includes \(j=1\).

**2. Complete repeated-factor classification at length \(G\).** Write \(C_k=W0^GW\). Its \((2G+1)\) length-\(G\) factors have starts \(0,1,\ldots,2G\). Starts \(0\) and \(2G\) yield \(W\). For \(1\le i<G\), the factor is
\[
P_i=W[i:G]0^i;
\]
its trailing zero-run is exactly \(i\), so these factors are pairwise distinct. For \(G\le j<2G\), the factor is
\[
Q_j=0^{2G-j}W[0:j-G];
\]
its leading zero-run is exactly \(2G-j\), so these factors also are pairwise distinct. Each \(P_i\) ends with \(0\) while \(W\) ends with \(1\), and each \(Q_j\) begins with \(0\) while \(W\) begins with \(1\). Therefore all other repetition could occur only across the \(P\)- and \(Q\)-families.

Suppose \(P_i=Q_j\), and put \(a=2G-j\), \(b=i\). The common word begins with exactly \(a\) zeros and ends with exactly \(b\) zeros. Those initial zeros must be in the suffix of \(W\) appearing in \(P_i\), and those final zeros must be in the prefix of \(W\) appearing in \(Q_j\). Since the longest zero run of \(W\) is \(H\), we have \(1\le a,b\le H\). Removing the outer zero runs from the equality shows that \(W\) has a border of length \(G-a-b\). This is a proper positive border, and
\[
G-a-b\ge G-2H=H.
\]
The longest proper border of \(W\) has length \(H\). It follows that \(a=b=H\), uniquely. With \(W=V0^HV\), both corresponding factors equal \(F=0^HV0^H\); their starts are \(H\) and \(2G-H\). This proves the asserted complete list of repeated length-\(G\) factors.

**3. No repetition at length \(G+1\).** For starts \(0\le i<G\), length-\((G+1)\) factors are \(P'_i=W[i:G]0^{i+1}\), pairwise distinct by their trailing zero-run lengths. For \(G\le j<2G\), the factors are \(Q'_j=0^{2G-j}W[0:j-G+1]\), pairwise distinct by their leading zero-run lengths. If some \(P'_i=Q'_j\), let \(a=2G-j\) and \(b=i+1\). As above, \(1\le a,b\le H\), and stripping the outer zero runs would give a proper border of \(W\) of length
\[
G+1-a-b\ge H+1,
\]
contradicting the maximal proper border length \(H\). Thus the \(G+1\) factors have pairwise distinct starting positions. Longer repeated factors are impossible, since any two equal longer factors share equal length-\((G+1)\) prefixes.

**4. From repetitions to absent words.** Let \(z=xuy\) be a minimal absent word of length at least three, where \(x,y\) are single symbols. Both \(xu\) and \(uy\) occur in the host. If \(u\) had only one occurrence, that occurrence would simultaneously have the predecessor \(x\) and successor \(y\); then \(xuy\) would occur, a contradiction. Hence \(u\) repeats. Step 3 gives \(|u|\le G\), so every minimal absent word has length at most \(G+2\).

For equality \(|z|=G+2\), its interior \(u\) must be \(W\) or \(F\) by step 2. The two occurrences of \(W\) are exactly the leading and trailing copies, at \(0\) and \(2G\). The leading copy has right context \(0\) and no left context; the trailing copy has left context \(0\) and no right context. Thus the unique missing, but one-sidedly supported, two-sided extension is \(0W0\).

The factor \(F\) occurs exactly twice, at \(H\) and \(2G-H\). Its first occurrence has left context \(1\) and right context \(0\); its second has left context \(0\) and right context \(1\). Consequently its existing two-sided extensions are \(1F0\) and \(0F1\), and precisely its missing but supported extensions are \(0F0\) and \(1F1\). Since \(0F0=0^{H+1}V0^{H+1}\) and \(1F1=1\,0^HV0^H1\), these, together with \(0W0\), are exactly the stated maximal-length minimal absent words. This also shows that the bound \(G+2\) is attained. \(\square\)

## Verification

The accompanying standard-library Python script `checker.py` constructs literal iterates and independently indexes factors by their starting positions. For every \(2\le k\le7\), it checks that only \(W\) and \(F\) repeat at length \(G\), that length-\((G+1)\) factors are all unique, and that the length-\((G+2)\) minimal absent set is exactly the predicted three words. It also directly enumerates minimal absent words of all possible lengths for \(k=2,3,4\) and verifies maximality. The checked host lengths are \(9,27,81,243,729,2187\); these finite tests corroborate but do not prove the theorem for all \(k\).

Run with `python3 checker.py`; no external modules or datasets are required.

## Relationship to prior work

Crochemore, Fici, Mercaş and Pissis (2015, arXiv:1506.04917) give definitions and general linear-time algorithms for minimal absent words, including a distinction between linear and circular settings. A general algorithm does not, by itself, identify the three extremal forbidden factors at every Cantor substitution level. The 2016 paper *On the permutation complexity of the Cantor-like sequences* (Theoretical Computer Science, DOI below) studies infinite Cantor-like factor/right-special and permutation complexity, rather than the length and complete top stratum of minimal absent words for finite substitution iterates. These are comparisons of stated mathematical claims, not proofs of historical uniqueness. No other covering theorem was identified in the searches performed; an equivalent older formulation remains possible.

## Limitations

The theorem does not enumerate *all* minimal absent words or their full length distribution. It is specific to the morphism \(1\mapsto101,\ 0\mapsto000\), to finite **linear** iterates, and to levels \(k\ge2\). The length-\(3\) case \(C_1=101\) is exceptional: its unique maximal-length minimal absent word is \(010\). Historical priority has not been independently established, and complete full-text access to one relevant 2016 article was not obtained.

## References

1. M. Crochemore, G. Fici, R. Mercaş and S. P. Pissis, *Linear-Time Sequence Comparison Using Minimal Absent Words & Applications*, initial public preprint 2015-06-16, arXiv:1506.04917, https://arxiv.org/abs/1506.04917.
2. *On the permutation complexity of the Cantor-like sequences*, *Theoretical Computer Science* 616 (2016), 100–110, DOI:10.1016/j.tcs.2015.12.022, https://doi.org/10.1016/j.tcs.2015.12.022.
