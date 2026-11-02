# Exact sparse-marker capacity for one adjacent two-deletion burst

## Finding

Let \(\mathcal W_{n,2}\subseteq\{0,1\}^n\) consist of all binary words with exactly two ones. For \(x\in\mathcal W_{n,2}\), define \(B_2(x)\) to be the **set of distinct length-\(n-2\) outputs after deleting exactly two consecutive positions**, with no additional edits. The maximum size \(M(n)\) of \(C\subseteq\mathcal W_{n,2}\) for which \(B_2(x)\cap B_2(y)=\varnothing\) whenever \(x\ne y\) in \(C\) is

\[M(2)=1,\qquad M(n)=\left\lfloor\frac{3(n-1)}{4}\right\rfloor\quad(n\ge3).\]

Both the upper bound and a closed-form optimal code are established below.

## Assumptions and scope

All word coordinates are indexed from \(0\) through \(n-1\). A word of Hamming weight two is identified with the ordered pair \((i,j)\) of the positions of its ones, where \(0\le i<j<n\). The channel removes positions \(t,t+1\) for some \(0\le t\le n-2\), and the receiver observes the order-preserving remaining binary word. In particular, the channel removes **exactly** two adjacent positions, not an arbitrary pair and not a variable number of positions. We require pairwise disjoint sets of possible outputs, i.e. unique zero-error decoding for one such burst.

Put \(m=n-2\). A nonadjacent pair \((i,j)\), with \(j-i\ge2\), has associated (possibly equal) *marker vertices* \(u=i\) and \(v=j-2\) in \(\{0,\ldots,m-1\}\); write its marker edge as \(\{u,v\}\), permitting loops when \(u=v\). This gives a bijection between nonadjacent weight-two words and unordered pairs of marker vertices with loops.

## Proof

**1. Marker collisions.** For a nonadjacent word with marker edge \(\{u,v\}\), \(u\le v\), deleting a length-two block that removes exactly one of the two ones yields a weight-one output with its remaining one at position \(u\) or \(v\). Both possibilities occur; if \(u=v\), they coincide. Consequently, the marker edges of any pairwise-decodable family of nonadjacent words must have mutually disjoint vertex sets. If that family contains \(\ell\) loops and \(e\) ordinary edges, then

\[\ell+2e\le m.\tag{1}\]

**2. Loop restriction and upper bound.** The loop at marker vertex \(u\) represents ones at positions \(u\) and \(u+2\). Loops at distinct vertices \(u\) and \(u+2\), if both admitted, share a weight-two output, since deleting two trailing zeros from the first word and two leading zeros from the second both leave ones at output positions \(u,u+2\). (Both deletion blocks exist for the stipulated marker range.) Thus the selected loop vertices form an independent set in the graph on \(0,\ldots,m-1\) joining vertices at distance two. This graph is the disjoint union of the path of even vertices and the path of odd vertices. Its independence number is

\[\alpha_m=\left\lceil\frac{\lceil m/2\rceil}{2}\right\rceil+\left\lceil\frac{\lfloor m/2\rfloor}{2}\right\rceil.\]

Writing \(m=4q+r\), \(0\le r\le3\), gives \(\alpha_m=2q,2q+1,2q+2,2q+2\), respectively. From (1) and \(\ell\le\alpha_m\), the number of chosen nonadjacent words satisfies

\[\ell+e\le \left\lfloor\frac{m+\alpha_m}{2}\right\rfloor=f(m),\qquad f(4q+r)=3q+\min(r,2).\tag{2}\]

**3. Allowing adjacent ones.** An adjacent word has ones at \((i,i+1)\) and can lose both ones simultaneously, yielding the all-zero output. Therefore a decodable code contains at most **one** adjacent word. Such a word has weight-one outputs at marker positions \(i-1\) (if \(i\ge1\)) and \(i\) (if \(i\le m-1\)). No other selected nonadjacent word may use those vertices.

For an interior adjacent word, \(1\le i\le m-1\), this excludes two vertices. Hence the number of additional nonadjacent words is at most \(\lfloor(m-2+\alpha_m)/2\rfloor=f(m)-1\), by the same loop bound, and the total size is at most \(f(m)\). At either boundary, \(i=0\) or \(i=m\), exactly one end marker vertex is excluded. The remaining \(m-1\) consecutive marker vertices support at most \(f(m-1)\) compatible nonadjacent words, again by (2). Codes with no adjacent word have size at most \(f(m)\). Therefore, for \(m\ge1\),

\[M(n)\le\max\{f(m),1+f(m-1)\}=1+f(m-1)=\left\lfloor\frac{3(m+1)}4\right\rfloor.\tag{3}\]

The equality in (3) follows by checking the four possible residues of \(m\) modulo \(4\).

**4. Construction and attainability.** Take the boundary-adjacent word with ones at \((0,1)\). On the remaining marker vertices \(1,2,\ldots,m-1\), write \(s=m-1=4q+r\) with \(0\le r\le3\). For each \(t=0,\ldots,q-1\), include the three nonadjacent words with one-position pairs

\[(4t+1,4t+3),\qquad(4t+2,4t+4),\qquad(4t+3,4t+6).\tag{4}\]

Also include the \(\min(r,2)\) nonadjacent words with pairs

\[(4q+1+a,\,4q+3+a),\qquad0\le a<\min(r,2).\tag{5}\]

These pairs all lie between \(0\) and \(n-1\). Their marker edges, in each full four-vertex block, are two loops at its first two vertices and an edge joining its final two vertices. The remaining vertices supply at most two initial loops. All selected marker edges are vertex-disjoint. No two loops are at distance two; any two ordinary edges are four or more marker steps apart, so no two chosen edges are translates of one another by two marker steps.

To confirm that these conditions suffice, a nonadjacent word with markers \(u\le v\) can yield weight-two outputs only with one-position pairs \((u,v+2)\), \((u,v)\) when \(u<v\), and \((u-2,v)\) when \(u\ge2\). The three possibilities correspond to deleting two zeros respectively after, between, or before the ones. Comparing these ordered pairs shows: for two nonadjacent parent words whose marker edges have no vertex in common, a shared weight-two output is possible **only if their marker edges are translates by two vertices** (in either direction). The construction prohibits that coincidence. Their weight-one outputs cannot collide either, by vertex-disjointness.

Finally the boundary-adjacent parent \((0,1)\) has the all-zero output, one possible weight-one output at position \(0\), and—if it has any weight-two output—the pair \((0,1)\). Every chosen nonadjacent parent uses only marker vertices \(1,\ldots,m-1\), so it cannot yield the weight-one output at \(0\). It cannot yield the weight-two output \((0,1)\) by the displayed three-case list. Thus all output sets in the constructed code are disjoint.

The code has size \(1+3q+\min(r,2)=1+f(m-1)=\lfloor3(n-1)/4\rfloor\), matching (3) for every \(n\ge3\). For \(n=2\) only the word with ones at \((0,1)\) exists, and it alone is a code of size one. This proves the theorem. \(\square\)

## Verification

The accompanying standalone `verify_burst2.py` uses only the Python standard library. It implements the channel by literally deleting every possible adjacent pair, enumerates the construction, and checks nonintersection of all received-word sets. It independently tests the stated collision classification for every pair of parents through length \(20\), exhaustively determines optimal sizes by independent-set search through length \(10\), checks the construction through length \(250\), and checks the residue arithmetic over \(0\le m\le10000\). These finite checks corroborate but do not replace the all-length proof.

Run from a directory containing the script with `python3 verify_burst2.py`.

## Relationship to prior work

Burst deletion is a standard synchronization-error model. Wang and collaborators study general nonbinary codes correcting bursts of at most \(t\) consecutive deletions [1]. Schoeny and collaborators develop code constructions and bounds for exact and bounded burst channels [2]. Cullina, Kulkarni, and Kiyavash investigate deletion-correcting codes partitioned by Hamming weight [3], but their deletion sets allow arbitrary positions, unlike the consecutive pair here. The result isolates a natural sparse, constant-composition subchannel and exactly solves its zero-error packing number for every length. The cited results, as inspected, do not state this sharp weight-two exact-burst theorem. An implicit equivalent specialization in older coding-theory literature cannot be excluded.

## Limitations

This is the exact-two-**consecutive**-deletion channel restricted to input weight two. The formula does **not** cover arbitrary two-deletion correction, bursts of at most two positions, other input weights, or all binary inputs. The finite verifier is not an infinite proof. Originality comparisons are limited by literature discoverability and are not independent confirmation.

## References

[1] S. Wang, Y. Tang, J. Sima, R. Gabrys, and F. Farnoud, *Non-binary Codes for Correcting a Burst of at Most t Deletions*, arXiv:2210.11818, first public version 2022-10-21. https://arxiv.org/abs/2210.11818

[2] C. Schoeny, A. Wachter-Zeh, R. Gabrys, and E. Yaakobi, *Codes Correcting a Burst of Deletions or Insertions*, arXiv:1602.06820, first public version 2016-02-22. https://arxiv.org/abs/1602.06820

[3] D. Cullina, A. A. Kulkarni, and N. Kiyavash, *Two Approaches to the Construction of Deletion Correcting Codes: Weight Partitioning and Optimal Colorings*, arXiv:1211.4056, first public version 2012-11-16. https://arxiv.org/abs/1211.4056
