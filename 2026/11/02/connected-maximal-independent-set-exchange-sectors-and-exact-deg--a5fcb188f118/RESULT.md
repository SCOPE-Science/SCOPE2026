# Connected maximal-independent-set exchange sectors and exact degree laws on cycles

## Finding

Let \(C_n\) be the simple cycle on vertices \(\mathbb Z/n\mathbb Z\), with \(n\ge4\). Construct a graph \(\mathcal R_n\) whose vertices are **all inclusion-maximal independent sets** of \(C_n\); two configurations are adjacent when one vertex is removed and a distinct vertex inserted, with the result again an inclusion-maximal independent set. Write \(\mathcal R_{n,k}\) for the induced fixed-cardinality sector with \(k\) selected vertices.

**Complete sector classification.** The only possible sizes satisfy \(\lceil n/3\rceil\le k\le\lfloor n/2\rfloor\). Set \(a=3k-n\) and \(b=n-2k\), so \(a,b\ge0\) and \(a+b=k\). Every exchange is necessarily a slide to an adjacent cycle vertex, although adjacency was not imposed in the definition.

If \(a,b>0\), the sector \(\mathcal R_{n,k}\) is connected and has exactly
\[
\frac nk\binom{k}{a}
\]
configurations. Its degree-distribution polynomial and edge count are
\[
\boxed{\sum_{S\in\mathcal R_{n,k}}z^{\deg(S)}=
\sum_{r=1}^{\min(a,b)}\frac nr\binom{a-1}{r-1}\binom{b-1}{r-1}z^{2r}},
\qquad
\boxed{|E(\mathcal R_{n,k})|=n\binom{k-2}{a-1}}.
\]
Thus precisely \(\frac nr\binom{a-1}{r-1}\binom{b-1}{r-1}\) configurations have degree \(2r\), for every integer \(1\le r\le\min(a,b)\), and no others occur. These expressions are integers.

If \(a=0\), necessarily \(n=3k\), and the sector consists of **three isolated vertices**. If \(b=0\), necessarily \(n=2k\), and the sector consists of **two isolated vertices**. The entire reconfiguration graph therefore has
\[
\boxed{\lfloor n/2\rfloor-\lceil n/3\rceil+1+
\mathbf 1_{2\mid n}+2\mathbf 1_{3\mid n}}
\]
connected components. Its total number of edges is
\[
\boxed{|E(\mathcal R_n)|=n[t^{n-5}](1-t^2-t^3)^{-1}}.
\]
For \(n=5m\), \(k=2m\), and \(m\ge3\), one connected nonminimal sector has degree classes \(2,4,\ldots,2m\). Their multiplicities are \(\frac{5m}{r}\binom{m-1}{r-1}^2\), showing arbitrarily high local mobility within a single connected sector.

## Assumptions and scope

The cycles are simple and have at least four vertices; all vertex labels are fixed, and configurations are not quotiented by cyclic or dihedral symmetry. *Independent* means no two selected vertices are adjacent. *Inclusion-maximal independent* means no further vertex can be added without violating independence; on a cycle this is equivalent to dominating every vertex. A reconfiguration step changes one selected and one unselected vertex while retaining both properties. We do not require intermediate states of different cardinality; indeed an edge cannot change cardinality by definition. The polynomial records unnormalized vertex degrees, not graph Laplacian eigenvalues.

## Proof

**1. Gap characterization and legal moves.** List the \(k\) selected vertices in clockwise order. The clockwise distance between successive selected vertices is at least two by independence and at most three by domination: a distance of four or more leaves at least one unselected cycle vertex not adjacent to any selected vertex. Thus each gap is two or three, with counts \(a\) and \(b\), because \(2a+3b=n\) and \(a+b=k\). Conversely, every circular sequence of such gaps defines an inclusion-maximal independent set. Therefore \(\lceil n/3\rceil\le k\le\lfloor n/2\rfloor\).

Suppose \(S'=(S\setminus\{x\})\cup\{y\}\) is a legal exchange. Since \(x-1\) and \(x+1\) were absent from the independent set \(S\), the deleted vertex \(x\) can be dominated in \(S'\) only if \(y=x-1\) or \(y=x+1\). Thus token jumping offers no moves beyond token sliding. A clockwise move of \(x\) is possible precisely when the gap preceding \(x\) is two and the gap following \(x\) is three; it switches these two consecutive gaps from \((2,3)\) to \((3,2)\). The counterclockwise move is the reverse. Each move corresponds uniquely to a boundary between distinct consecutive gap lengths.

**2. Counting and degrees.** Take one distinguished selected vertex as an anchor. There are \(n\) choices for its position and \(\binom{k}{a}\) linear words of length \(k\) recording the circular gaps starting at it. Every independent set appears exactly \(k\) times, giving \(N_{n,k}=\frac nk\binom{k}{a}\). Each boundary between a run of twos and a run of threes gives one legal slide, and distinct boundaries give distinct successor configurations. If the circular gap word has \(r\) runs of twos and \(r\) runs of threes, its degree is \(2r\). For \(a,b>0\), the number of anchored length-\(k\) gap words with exactly \(r\) alternating pairs of runs is
\[
\frac{k}{r}\binom{a-1}{r-1}\binom{b-1}{r-1}.
\]
Indeed, positive compositions of \(a\) and \(b\) into \(r\) ordered nonempty run lengths give the two binomial factors; choose which of the \(k\) indexed positions begins a distinguished two-run and divide by the \(r\) choices of that two-run. Multiplying by \(n/k\) gives the degree multiplicity claimed. Summing half the degree sum and applying Vandermonde's identity,
\[
\sum_{r\ge1}\binom{a-1}{r-1}\binom{b-1}{r-1}
=\binom{a+b-2}{a-1}=\binom{k-2}{a-1},
\]
gives the edge count.

**3. Connectivity.** When \(a,b>0\), fix a particular selected vertex \(x\) and record the gap word beginning there. Sliding any selected vertex other than \(x\) exchanges any prescribed pair of consecutive unequal gaps in positions \(0,\ldots,k-2\). Such adjacent exchanges connect all binary words with the same counts while keeping \(x\) fixed. Next rearrange the gaps so the one immediately before \(x\) is two and the one immediately after \(x\) is three; this is possible because both types occur. Sliding \(x\) one position clockwise exchanges the two gaps surrounding it, and moves the anchored vertex from \(x\) to \(x+1\). Reorder the remaining gap word to any desired canonical form without moving the new anchor. Iterating this procedure moves the distinguished anchor to any cycle vertex; fixed-anchor sorting then reaches any target of the same size. The sector is connected. If either gap type is absent, all gaps coincide and no slide is legal; the number of possible configurations is \(n/k=3\) or \(2\) respectively, all isolated.

**4. Overall components and edge generating function.** Different cardinalities never mix. The number of allowed cardinalities is \(\lfloor n/2\rfloor-\lceil n/3\rceil+1\); a pure gap sector contributes two extra components if \(3\mid n\), or one extra if \(2\mid n\), beyond its baseline one. This proves the component formula. For the total edge count, let \(a'=a-1\), \(b'=b-1\) in every mixed sector. Then \(a',b'\ge0\) and \(2a'+3b'=n-5\), while \(\binom{k-2}{a-1}=\binom{a'+b'}{a'}\). Expanding \((1-t^2-t^3)^{-1}=\sum_{a',b'\ge0}\binom{a'+b'}{a'}t^{2a'+3b'}\) gives the stated coefficient.

## Verification

The standalone `verify_subsets.py` directly enumerates all binary subsets, tests independence and domination separately, constructs **all** one-delete/one-insert feasible exchanges (without requiring adjacency), and verifies degree multiplicities and connected components for every \(4\le n\le18\). The independently designed `verify_gaps.cpp` enumerates anchored cyclic gap arrangements, constructs allowed neighboring slides, and verifies degree distributions, counts, edge totals, and components for every \(4\le n\le22\). The finite checks corroborate but do not replace the all-parameter proof. Run the Python file using `python3 verify_subsets.py`, and compile and run the C++ file with `g++ -O2 -std=c++17 verify_gaps.cpp -o verify_gaps && ./verify_gaps`.

For example, \(n=20\) and \(k=8\) gives \(a=b=4\), with \(175\) configurations: the degree multiplicities at degrees \(2,4,6,8\) are respectively \(20,90,60,5\), totaling \(400\) undirected edges.

## Relationship to prior work

Bonsma, Kamiński, and Wrochna (2014) analyze reconfiguration of **independent sets** under jumps and slides in claw-free graphs, without imposing the inclusion-maximal independent domination condition at every step. Avis and Hoang (2022/2023) likewise analyze token slides among all independent sets at each cardinality. Brewster, Mynhardt, and Teshima (2023) determine the \(i\)-graphs of paths and cycles, but their graph is restricted to **minimum** independent dominating sets, corresponding here solely to \(k=\lceil n/3\rceil\). Its special sector may therefore be recovered as an instance; it is not presented as novel. Goh, Koh, Sagan, and Vatter (2002/2005) study extremal counts of maximal independent sets in graph classes with bounded cycle rank, not reconfiguration sectors and degree distributions on a fixed cycle.

The full-cardinality degree law, connectivity for **every** nonminimal sector, pure-sector isolation counts, and unbounded degree spectrum in the \(n=5m\) family are the present claims. Ordinary circular run-composition enumeration underlies the count; it is not claimed as a new counting principle. A more general published result could imply this classification even without naming these parameters, so residual literature risk remains.

## Limitations

The proof is for simple cycles with \(n\ge4\), labelled configurations, equal-cardinality exchanges, and inclusion-maximal independence throughout. It does not classify exact distances, diameter, spectral data, or token addition/removal moves. No general assertion about arbitrary graphs is made. Novelty has been tested against identified literature and mathematical research records but is not independently certified; unindexed or inaccessible stronger results remain a risk.

## References

1. C. Y. Goh, K. M. Koh, B. E. Sagan, V. Vatter, *Maximal Independent Sets In Graphs With At Most r Cycles*, arXiv:math/0207100 (first public version 2002-07-11), https://arxiv.org/abs/math/0207100.
2. P. Bonsma, M. Kamiński, M. Wrochna, *Reconfiguring Independent Sets in Claw-Free Graphs*, arXiv:1403.0359 (2014-03-03), https://arxiv.org/abs/1403.0359.
3. D. Avis, D. A. Hoang, *On Reconfiguration Graphs of Independent Sets under Token Sliding*, arXiv:2203.16861 (2022-03-31), https://arxiv.org/abs/2203.16861.
4. R. C. Brewster, C. M. Mynhardt, L. E. Teshima, *The i-Graphs of Paths and Cycles*, arXiv:2303.08190 (2023-03-14), https://arxiv.org/abs/2303.08190.
