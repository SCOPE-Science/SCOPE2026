# Four-query static shattering and logarithmic adaptive depth in circular two-block partitions

## Finding
Let \(n\ge2\), with \(n\) distinct labeled vertices in cyclic order, and let \(\mathcal B_n\) consist of all partitions into **exactly two nonempty blocks**, each a consecutive circular arc. Each query \(\{u,v\}\) reports whether its vertices belong to **different blocks**. Complementing all query outputs (asking equality instead) leaves both dimensions unchanged. Then
\[
\operatorname{VCdim}(\mathcal B_n)=4\quad(n\ge7).
\]
For all \(n\ge2\),
\[
\left\lfloor\log_2(n-1)\right\rfloor\le \operatorname{Ldim}(\mathcal B_n)\le\left\lfloor\log_2\binom n2\right\rfloor.
\]
In particular, for \(n\ge7\) the VC dimension is the fixed constant \(4\), whereas the Littlestone dimension diverges. The smallest strict separation occurs at \(n=5\), where \(\operatorname{VCdim}=2\) and \(\operatorname{Ldim}=3\). Exact finite values for \(2\le n\le16\) are reproduced below.

## Assumptions and scope
The two blocks are unlabelled and nonempty. Label the cyclic gaps following vertices \(0,\ldots,n-1\) by those same integers. Each partition is uniquely specified by an unordered pair of distinct gaps \(0\le a<b<n\); its two blocks are the intervals of vertices \(a+1,\ldots,b\) and their cyclic complement. Hence \(|\mathcal B_n|=\binom n2\). For query \(0\le u<v<n\), its output is
\[
f_{a,b}(u,v)={\bf1}\{u\le a<v\}\mathbin{\oplus}{\bf1}\{u\le b<v\}.
\]
VC dimension is the largest number of fixed queries realizing all their Boolean assignments; Littlestone dimension is the largest depth of a full binary adaptive query tree whose every path admits a distinct consistent concept.

## Proof
**Uniform VC upper bound.** Assume five pair-queries are shattered. Draw each as a chord on the cyclically ordered vertices. If several queried chords share an original vertex, separate their incidences into adjacent cyclic positions, preserving cyclic order, until there are exactly ten distinct endpoints joined by five disjoint matched pairs. Original cut placements extend to the expanded order by keeping each incidence group together. Therefore every response pattern realizable on the five original queries is also realizable on the resulting five-chord matching.

There are exactly \(9\cdot7\cdot5\cdot3\cdot1=945\) perfect matchings of ten cyclically ordered endpoints. For each matching \(M\), the complete two-cut response family is enumerated by the \(45\) pairs of distinct gaps. A response on chord \(\{u,v\}\) is one if exactly one of \(u,v\) lies in the circular interval between the gaps. Exhausting all \(945\) matchings gives a maximum of **30** distinct five-bit vectors (not the \(32\) required for shattering). The complete histogram of number of different vectors is
\[
\{16:42,\ 19:120,\ 21:186,\ 22:50,\ 23:45,\ 24:220,\ 25:70,\ 26:40,\ 27:150,\ 30:22\}.
\]
The two independently expressed finite enumerators and the direct partition model are contained in `verify.py`; the enumeration covers every matching, not a random sample. Thus no five fixed pair-queries are shattered, for any number of vertices.

**Sharpness.** At \(n=7\), the four fixed queries \(\{0,2\},\{0,4\},\{1,3\},\{1,5\}\) yield every one of the sixteen patterns as the unordered cut gaps vary. The file `four_query_witnesses.json` records a corresponding cut-pair witness for each pattern. For larger \(n\), insert further vertices in one unused cyclic gap: all original cut-patterns remain possible. Therefore VC dimension equals four for all \(n\ge7\).

**Adaptive upper and lower bounds.** Since there are \(\binom n2\) hypotheses, a complete depth-\(d\) decision tree has \(2^d\) distinct leaf hypotheses; consequently \(d\le\lfloor\log_2\binom n2\rfloor\). For the lower bound, fix one cut after vertex \(n-1\), vary the other cut over the \(n-1\) gaps \(0,\ldots,n-2\), and query only pairs \(\{0,j\}\) with \(1\le j<n\). The response is one precisely when the variable cut lies before \(j\). This is the complete threshold family on \(n-1\) ordered states. Repeated median queries produce a complete adaptive tree of depth \(\lfloor\log_2(n-1)\rfloor\), proving the lower bound and unbounded adaptive-versus-static separation.

**First strict gap.** Direct exhaustive comparison of all pair queries gives VC dimensions \(0,1,2,2\) at \(n=2,3,4,5\). The binary concept-count bound gives adaptive dimensions at most \(0,1,2,3\), respectively, while the complete depth-three tree in `depth_three_certificate.json` proves the last lower bound. Hence equality prevails through four vertices and first fails at five.

## Verification
Run `python3 verify.py`. The checker enumerates every matched five-chord diagram, compares two independent algorithms for its responses, checks independent representations of two-arc partitions for \(2\le n\le16\), and exhaustively verifies small VC dimensions and Littlestone recurrences plus constructed adaptive trees. Its final marker is `CIRCULAR_TWO_BLOCK_ALL_CHECKS_PASS`. The optional JSON certificates are human-readable extractable witnesses. Exact small values are:

| \(n\) | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VC | 0 | 1 | 2 | 2 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| Ldim | 0 | 1 | 2 | 3 | 3 | 4 | 4 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |

## Relationship to prior work
The learning-theoretic VC/Littlestone framework and closure constructions occur in Ghazi–Golowich–Kumar–Manurangsi (arXiv:2007.03668) and Chase–Freitag–Reyzin (arXiv:2310.04812). Alexandersson–Linusson–Potka–Uhlin (arXiv:2010.11157) treats related noncrossing partition combinatorics, especially Catalan enumeration and cyclic sieving; those enumerative results alone do not imply our query-shattering dimensions. The exact two-block consecutive-arc restriction differs from classes closed under refining arbitrary set partitions. The present proof depends on a complete chord-matching obstruction, not just on the size of the concept class.

## Limitations
The all-size adaptive conclusion is an explicit two-sided logarithmic estimate and divergence, not an exact formula for all \(n\). Exact adaptive values were verified only through \(n=16\). The static upper bound depends on a finite, fully enumerable ten-endpoint check; no purely symbolic classification of all five-chord traces is claimed. Identical work under alternate circular-cut, XOR-of-threshold, or chord-signature terminology may exist; absence of a search hit is not a uniqueness proof. Independent validation has not been performed.

## References
1. B. Ghazi, N. Golowich, R. Kumar, P. Manurangsi, *Near-tight closure bounds for Littlestone and threshold dimensions*, arXiv:2007.03668 (first public 7 July 2020).
2. P. Alexandersson, S. Linusson, S. Potka, J. Uhlin, *Refined Catalan and Narayana cyclic sieving*, arXiv:2010.11157 (first public 21 October 2020).
3. H. Chase, J. Freitag, L. Reyzin, *Applications of Littlestone dimension to query learning and to compression*, arXiv:2310.04812 (first public 7 October 2023).
