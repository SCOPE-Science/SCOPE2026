# Shortest cyclic covers of all binary words avoiding \(010\)

## Finding
For every integer \(n\geq 3\), let \(\mathcal L_n\) comprise all length-\(n\) binary strings that do not contain the contiguous factor \(010\). A cyclic string \(s\) is *legal* if no cyclic triple is \(010\). Let \(M_n\) be the minimum positive length of a legal cyclic string in which every member of \(\mathcal L_n\) appears as a cyclic window of length \(n\). Write \(E_n=|\mathcal L_n|\) and \(C_n=M_n-E_n\).

Then the following are exact ordinary generating functions:
\[
\sum_{n\geq0} E_n z^n=\frac{1+z^2}{1-2z+z^2-z^3},
\qquad
\sum_{n\geq3} C_nz^n=\frac{z^3(2-z)}{(1-z)^2}+\frac{z^5(1+z)}{(1-z)^2((1-z)^2-z^3)}.
\]
In particular, for \(n=3,4,\ldots,12\), the optimal lengths are \(9,15,26,47,85,152,270,478,844,1487\). The theorem is constructive: a specified family of shortest paths balances a non-Eulerian restricted overlap graph, and an Euler tour yields an optimal cyclic string.

## Assumptions and scope
The forbidden pattern is the exact contiguous triple \(010\), not a subsequence. A linear length-\(n\) word is allowed when it avoids \(010\) internally; this condition does **not** require its periodic repetition to avoid the pattern. In contrast, a covering cycle must avoid the forbidden pattern even over its boundary. Repeated length-\(n\) windows are allowed and are minimized. All statements hold for every integer \(n\geq3\) and use no probabilistic assumptions.

## Proof
Fix \(n\geq3\), and write \(L=n-1\). Form a directed overlap graph \(G\) whose vertices are all linear \(010\)-avoiding words of length \(L\) and whose edges are the words in \(\mathcal L_n\): edge \(x_1\cdots x_n\) goes from \(x_1\cdots x_L\) to \(x_2\cdots x_n\). Every legal transition is present. For any two vertices \(u,v\), appending \(11v\) to \(u\) avoids \(010\) and terminates at \(v\), so \(G\) is strongly connected. Each edge contributes one cyclic window; a legal covering cycle is precisely a closed walk covering all edges at least once.

For a vertex \(v\), the permitted outgoing degree is \(1\) if \(v\) ends with \(01\) and \(2\) otherwise. The incoming degree is \(1\) if \(v\) begins with \(10\) and \(2\) otherwise. Consequently
\[
\deg^+(v)-\deg^-(v)={\bf1}_{v\text{ begins }10}-{\bf1}_{v\text{ ends }01}.
\]
Call a vertex *negative* when it ends in \(01\) but does not begin in \(10\), and *positive* when it begins in \(10\) but does not end in \(01\). Every nonzero degree imbalance is exactly \(1\) or \(-1\), and there are equally many positive and negative vertices.

Any covering closed walk uses all mandatory edges and some additional multiset of edges. Its additional edges have divergence \(+1\) at each negative vertex, \(-1\) at each positive vertex, and zero elsewhere. By integral flow decomposition, the additional edges contain one directed negative-to-positive path for each negative vertex, possibly together with additional cycles; thus their number is at least the sum, over all negative vertices, of the distance to the nearest positive vertex.

Compute those distances. There is one negative vertex without \(10\), namely \(v_*=0^{L-1}1\). A shift by \(j<L-1\) keeps an initial \(0\); after \(L-1\) shifts the new word begins with the final \(1\) of \(v_*\), and the next appended symbol cannot be \(0\) because it would complete forbidden \(010\). Therefore no positive vertex is reachable in fewer than \(L\) shifts. The appended word \(10^{L-1}\), of length \(L\), reaches the positive vertex \(10^{L-1}\); this route is legal. Hence its distance is exactly \(L\).

Every other negative vertex \(v\) contains \(10\). Let \(j\geq1\) be the zero-based starting position of its *first* \(10\), and write \(v=pt\) with \(|p|=j\). Any shift by fewer than \(j\) positions cannot produce a positive vertex, since its leading pair lies before the first \(10\). Since \(p\) contains no \(10\), it must equal \(0^a1^b\) for integers \(a\geq0,b\geq1\), \(a+b=j\); the restriction \(b\geq1\) follows because a preceding \(0\) immediately before the beginning of \(t\) would create \(010\). The suffix \(t\) begins in \(10\), ends in \(01\), and avoids \(010\). Appending \(q=1^b0^a\) gives exactly \(j\) legal shifts ending at \(w=tq\). This word begins in \(10\), while its ending is not \(01\); therefore it is positive. The distance is exactly \(j\).

These shortest paths can be chosen simultaneously, one for each negative vertex, without sharing a positive destination. Indeed, the exceptional destination \(10^{L-1}\) has no occurrence of \(01\). For each ordinary destination \(w=t1^b0^a\), the *rightmost* occurrence of \(01\) is the ending of \(t\). This identifies the exact cut between \(t\) and \(q\); the suffix \(q\) uniquely determines \(a,b\), hence \(p\), and reconstructs its unique source \(pt\). Thus the negative-to-positive map is injective and, because the two sets have equal cardinalities, bijective. Add all these directed shortest paths to \(G\). The resulting directed multigraph is balanced, remains strongly connected, and therefore admits an Euler tour. Its cyclic edge-label word covers all of \(\mathcal L_n\) and avoids \(010\). Together with the preceding lower bound, this proves that the total number of edges added is exactly \(C_n\).

To enumerate that number, let \(B_m\) count \(010\)-avoiding words of length \(m\) that begin in \(10\) and end in \(01\). Necessarily \(m\geq3\). Each such word is obtained from an initial \(1\), then a nonempty zero-run, followed by any number of (one-run of length at least two, nonempty zero-run) blocks, then a final \(1\). Therefore
\[
B(z):=\sum_{m\geq3}B_mz^m=
\frac{z^3(1-z)}{(1-z)^2-z^3}.
\]
For ordinary negative vertices, specifying the first-\(10\) position \(j\), the prefix \(p=0^a1^b\) has exactly \(j\) possibilities, and its suffix \(t\) has \(B_{L-j}\) possibilities. Every such vertex contributes precisely \(j\) extra edges. The exceptional vertex contributes \(L\). Hence
\[
 C_n=(n-1)+\sum_{j=1}^{n-4} j^2 B_{n-1-j}.
\]
Since \(\sum_{j\geq1}j^2z^j=z(1+z)/(1-z)^3\), this coefficient formula yields the asserted generating function for \(C_n\). The generating function for \(E_n\) follows by a three-state suffix-avoidance recurrence (or by decomposing legal words into runs), yielding \(E_0=1,E_1=2,E_2=4\) and \(E_n=2E_{n-1}-E_{n-2}+E_{n-3}\) for \(n\geq3\). This completes the proof.

## Verification
Run `python3 verify.py` using only the Python standard library. The checker explicitly builds all required overlap edges for \(3\leq n\leq12\), independently calculates shortest distances by breadth-first search, validates injectivity of selected destinations and the Eulerian degree balance, constructs an Euler tour, and verifies both cyclic legality and coverage of every required window. It also checks the coefficient formula, and exhaustively excludes shorter cycles for \(n=3,4\). `checks.txt` records the exact output. These finite checks support, but do not replace, the preceding proof for all \(n\).

## Relationship to prior work
Moreno and Matamala [1] study restricted de Bruijn cycles whose permitted words are periodic-shift admissible, and they optimize the **lexicographic order** of Euler tours. In their definition, a block is in the language only when its periodic extension avoids the forbidden set; our requirement covers all *linearly* admissible blocks, even when their periodic extension violates \(010\), and the overlap graph generally needs repeated edges. Sawada and Gabrić [2] study randomized Eulerian universal-cycle generation for forbidden repeated-zero patterns and other balanced families, not the exact repeated-window optimum for \(010\). These works provide the motivation and graph-theoretic context but their inspected results do not entail the above formula. The classical directed rural/Chinese-postman interpretation explains why augmentation is relevant; the explicit bijective shortest-path solution is special to this forbidden-factor language.

## Limitations
The closed form is established only for the binary forbidden pattern \(010\) and \(n\geq3\). It makes no assertion about general forbidden words, unique optimal cycles, or the complexity of finding optimal covers in general languages. A literature search and direct comparisons cannot exclude differently indexed or unpublished equivalent results. No independent external scientific audit has been performed.

## References
[1] E. Moreno and M. Matamala, *Minimum de Bruijn Sequence in a Language with Forbidden Substrings*, arXiv:0711.1695v1, 12 November 2007. https://arxiv.org/pdf/0711.1695

[2] J. Sawada and D. Gabrić, *Las Vegas algorithms to generate universal cycles and de Bruijn sequences uniformly at random*, arXiv:2510.16545v1, first public 18 October 2025. https://arxiv.org/abs/2510.16545
