# Sharp generator-based rainbow thresholds for one-outlier circulants

## Finding
For integers \(k\ge3\), \(k+2\le\ell\le3k+1\), and \(2\ell+1\le n\le2(\ell+k)+1\), let \(G_{n,k,\ell}\) be the undirected circulant on \(\mathbb Z/n\mathbb Z\) with cyclic step lengths \(1,2,\ldots,k,\ell\). A *generator-based red-blue coloring* assigns each step length one fixed color, used on every edge of that length. We call the coloring rainbow-connecting if every pair of vertices is joined by a path whose edges have pairwise different colors.

**Theorem.** Every graph in this domain is noncomplete and has diameter two. It admits a generator-based rainbow-connecting red-blue coloring **if and only if** one of the following disjoint conditions holds:

\[
\begin{aligned}
&k+2\le\ell\le2k+1;\quad\text{or}\\
&2k+2\le\ell\le3k-1\quad\text{and}\quad n\le2(\ell+k)-1.
\end{aligned}
\]

In these positive cases, \(\operatorname{rc}(G_{n,k,\ell})=\operatorname{src}(G_{n,k,\ell})=2\). In the remaining cases—including every \(3k\le\ell\le3k+1\)—no generator-based red-blue coloring rainbow-connects the graph, **despite its diameter being two**. This negative statement concerns only generator-based colorings, not unrestricted rainbow connection.

## Assumptions and scope
Graphs are finite, simple, and undirected. Since \(2\ell<n\), distinct allowed positive step lengths \(1,\ldots,k,\ell\) determine distinct inverse-pairs of Cayley generators, without involutions. The cyclic distance between vertices \(u,v\) is \(d(u,v)=\min\{|u-v|,n-|u-v|\}\), interpreted using integer representatives. A generator-based coloring is invariant under all cyclic translations and assigns the same color to both signs of one step length. A two-edge rainbow walk between two nonadjacent vertices is necessarily a simple shortest path; edges joining adjacent vertices are already rainbow single-edge paths.

For two distinct step lengths \(a,b\), a rainbow two-edge walk from \(0\) to a vertex of cyclic distance \(d\) exists precisely when at least one signed sum \(\pm a\pm b\) is congruent to \(d\) or \(-d\) modulo \(n\), and the two generator colors differ. Reusing the same length never gives a rainbow two-edge walk. This reduces generator-based connection to finitely many difference constraints on the length colors.

## Proof
**1. Diameter.** Distances \(1,\ldots,k\) and \(\ell\) are edges. Every integer distance in \([k+1,2k]\) is the sum of two allowed short lengths. Every distance in \([\ell-k,\ell-1]\) is a difference \(\ell-j\) for some \(1\le j\le k\), and each in \([\ell+1,\ell+k]\) is a sum \(\ell+j\). Because \(\ell\le3k+1\), the intervals \([1,2k]\) and \([\ell-k,\ell+k]\) touch or overlap. Because \(\lfloor n/2\rfloor\le\ell+k\), these possibilities cover every cyclic distance. Since \(\ell\ge k+2\), distance \(k+1\) is not an edge. Hence the diameter equals two.

**2. The first positive band.** For \(\ell\le2k+1\), color length \(\ell\) red and lengths \(1,\ldots,k\) blue. Every nonedge at distance \(d\) with \(k+1\le d\le\ell-1\) has the rainbow representation \(d=\ell-(\ell-d)\): here \(1\le\ell-d\le k\). Every nonedge with \(\ell+1\le d\le\lfloor n/2\rfloor\) has \(d=\ell+(d-\ell)\) with \(1\le d-\ell\le k\). Thus the coloring is strongly rainbow connecting.

**3. The second positive band.** Assume \(2k+2\le\ell\le3k-1\) and \(n\le2(\ell+k)-1\). Color lengths \(k\) and \(\ell\) red and all lengths \(1,\ldots,k-1\) blue. Distances \(k+1\le d\le2k-1\) are represented as \(k+(d-k)\), with a red and a blue length. Distances \(2k\le d\le\ell-1\) are represented by \(\ell-(\ell-d)\), where \(1\le\ell-d\le\ell-2k\le k-1\), again red-blue. Distances \(\ell+1\le d\le\lfloor n/2\rfloor\) have \(d=\ell+(d-\ell)\), with \(1\le d-\ell\le k-1\) by the upper bound on \(n\). These exhaust the nonedges.

**4. The top two orders in the middle band fail.** Suppose \(2k+2\le\ell\le3k-1\) and \(n=2(\ell+k)+t\), with \(t\in\{0,1\}\). For every \(j\in\{1,\ldots,k\}\), distance \(d=\ell+j\) is a nonedge not exceeding \(\lfloor n/2\rfloor\). To make its two-edge path rainbow, the colors of length \(\ell\) and length \(j\) must differ. Indeed, two short steps have sum at most \(2k<d\); one long and one short step can reach this distance only by the signed sum \(\ell+j\). A wrapped sum would require another short length \(2k+t-j\), which is greater than \(k\), except for the identical choice \(j=k,t=0\). Wrapped differences and equal long steps cannot supply an opposite-color pair. Therefore all short generators \(1,\ldots,k\) must have the color opposite to \(\ell\). But distance \(k+1\) is a nonedge and cannot be reached by a long-short two-edge path (the smallest long-short difference is \(\ell-k\ge k+2\), and all wrapped sums are even larger). Its two-edge paths use only short lengths, all monochromatic. Contradiction.

**5. The band \(\ell=3k\) fails.** First consider distances \(k+j\) for \(j=k-1,k-2,\ldots,1\). Since \(\ell-k=2k\) and \(n\ge2\ell+1\), no two-edge representation of these distances involves the long generator. For \(j=k-1\), the only possible pair of distinct lengths is \(k,k-1\), forcing opposite colors. Inductively, a decomposition \(k+j=a+b\) with both \(a,b<k\) and neither equal to \(j\) has both indices greater than \(j\), previously forced to the color opposite to length \(k\); it is monochromatic. Thus the pair \(k,j\) must have opposite colors. Consequently, all lengths \(1,\ldots,k-1\) have one common color, opposite the color of \(k\). At distance \(2k\), the only potentially rainbow pair of distinct generator lengths is \(\ell,k\): the short-short representation \(k+k\) is monochromatic. Therefore length \(\ell\) has the same color as lengths \(1,\ldots,k-1\).

Write \(n=2\ell+t\) with \(t\ge1\). Distance \(\ell-1=3k-1\) is too large for two short steps. Its direct long-short representation is \(\ell-1\), using a length-\(1\) step with the same color as \(\ell\). The only other potentially rainbow long-short representation comes from wrapping \(\ell+a\), with \(a=t+1\). If \(t\le k-2\), this additional length, when present, also has the color of \(\ell\); if \(t\ge k\), it is not allowed. The exceptional case \(t=k-1\) could use length \(a=k\) to connect distance \(\ell-1\); then instead inspect distance \(\ell-2=3k-2>2k\) (the strict inequality uses \(k\ge3\)). Its direct length-\(2\) step has the color of \(\ell\), and a wrapped alternative would require forbidden length \(a=k+1\). In every case some nonadjacent pair lacks a rainbow path, giving a contradiction.

**6. The band \(\ell=3k+1\) fails.** Distance \(2k\) is a nonedge. Two short steps can realize it only as \(k+k\), not rainbow. A long-short difference is at least \(\ell-k=2k+1\); a wrapped long-short sum is at least \(n-(\ell+k)\ge\ell-k+1=2k+2\). Two long steps again have one color. Hence no generator-based rainbow path connects distance \(2k\).

The cases are exhaustive. In positive cases the explicit constructions yield a rainbow geodesic for every pair. Noncompleteness gives the matching lower bound of two colors for unrestricted rainbow connection.

## Verification
The standalone Python 3 program `verify.py` enumerates every assignment of two colors to the allowed generator lengths (up to color swap) for each of the \(862\) parameter triples \(3\le k\le8\), \(k+2\le\ell\le3k+1\), and \(2\ell+1\le n\le2(\ell+k)+1\). It checks modular signed-sum constraints rather than using the claimed formulas. For each positive triple it additionally constructs the full labeled graph and checks rainbow two-edge paths directly for all vertex pairs. For every triple it separately verifies that the graph has diameter two. Results: \(676\) positive and \(186\) negative cases, with zero discrepancies. Run `python3 verify.py` from a directory containing this file.

These finite experiments test the proof and detect boundary mistakes; the quantified infinite theorem follows from the case analysis, not from extrapolation. No unrestricted two-coloring is ruled out in a generator-based negative case.

## Relationship to prior work
Barát, Boyadzhiyska, and Freschi (arXiv:2609.11437v1, 10 September 2026) introduce the explicit generator-based coloring question for dense Cayley/circulant graphs in §6, exhibit the contiguous-step obstruction at its exact Dirac boundary, and establish rainbow-connection results under minimum-degree hypotheses. Their theorems do not classify the one-outlier families considered here: most of the present graphs are below their minimum-degree regime. The earlier exact contiguous-step cycle-power case \(\ell=k+1\) is deliberately excluded from the theorem's domain.

Li, Li, and Liu (arXiv:1011.0827v3, 2010) establish upper and lower bounds for rainbow connection in abelian Cayley graphs and analyze recursive circulants with multiplicative step sets. Their claims about unrestricted \(\operatorname{rc}\) and \(\operatorname{src}\) do not give this classification of constant-per-generator red-blue colorings on an interval of steps plus one outlier. The present proof is self-contained. A literature search cannot exclude unindexed equivalent descriptions.

## Limitations
This is an exact statement only for \(k\ge3\), \(k+2\le\ell\le3k+1\), and \(2\ell+1\le n\le2(\ell+k)+1\). It does not characterize all circulants, does not prove the minimum-degree conjecture, and does not determine unrestricted rainbow connection in the negative cases. Every new result has received self-review only; no independent external audit has been performed. An unindexed or differently formulated result could overlap the claim.

## References
1. J. Barát, S. Boyadzhiyska, A. Freschi, *Rainbow connecting 2-colorings of super-Dirac graphs*, arXiv:2609.11437v1 (first submitted 10 September 2026), especially Introduction and §6. https://arxiv.org/pdf/2609.11437
2. H. Li, X. Li, S. Liu, *The (strong) rainbow connection numbers of Cayley graphs of Abelian groups*, arXiv:1011.0827v3 (2010), especially Definitions 1–2 and Theorems 2–3. https://arxiv.org/pdf/1011.0827
