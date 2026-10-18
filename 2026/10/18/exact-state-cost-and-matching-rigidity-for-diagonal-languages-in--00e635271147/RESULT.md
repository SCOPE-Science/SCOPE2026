# Exact state cost and matching rigidity for diagonal languages in cactus automata

## Finding
For each integer \(n\ge1\), take an alphabet \(\Sigma_n=\{a_1,\ldots,a_n\}\) of distinct symbols and the finite *diagonal* language
\[
D_n=\{a_i a_i:1\le i\le n\}.
\]
For epsilon-free NFAs with one initial state and any set of accepting states (incomplete transitions allowed), let \(\nu_{\mathcal G}(D_n)\) be the minimum number of states among automata whose **underlying simple undirected transition graph** belongs to graph class \(\mathcal G\). Directions and labels are forgotten; multiple edges are identified, as in Grobler–Koziel–Siebertz.

The exact values, for all \(n\ge1\), are
\[
\begin{aligned}
\nu_{\mathrm{unrestricted}}(D_n)&=\nu_{\mathrm{planar}}(D_n)=n+2,\\
\nu_{\mathrm{bipartite\ cactus}}(D_n)&=1+n+\lceil n/2\rceil,\\
\nu_{\mathrm{tree}}(D_n)&=2n+1.
\end{aligned}
\]
In particular, all three minima are distinct when \(n\ge3\).

**Rigidity.** Every trim state-minimal bipartite-cactus NFA for \(D_n\) is isomorphic, preserving letter labels and initial/final status, to the matching construction in the proof. The isomorphism classes correspond bijectively to partitions of the \(n\) alphabet symbols into \(\lfloor n/2\rfloor\) unordered pairs and, for odd \(n\), one singleton. Their number is
\[
\frac{n!}{2^{\lfloor n/2\rfloor}\lfloor n/2\rfloor!}.
\]
No assumption of determinism, unambiguity, or acyclicity is made for a competing NFA.

## Assumptions and scope
An NFA is \((Q,\Sigma,\Delta,s,F)\) with finite state set \(Q\), initial state \(s\), accepting subset \(F\), and \(\Delta\subseteq Q\times\Sigma\times Q\). There are no epsilon transitions. A state is *useful* if it occurs on an accepting run from \(s\); an automaton is *trim* if every state is useful. Deleting non-useful states and their transitions does not change its language and cannot destroy graph planarity, the cactus property, or acyclicity, so state minima admit trim witnesses. A cactus graph is one in which every edge lies on at most one simple cycle. A tree is connected and acyclic; useful NFAs have connected underlying graphs. The alphabet size \(n\) is not held fixed as a parameter tending to infinity: each \(D_n\) is a language over its explicitly declared \(n\)-letter alphabet.

## Proof
**1. Three layers and the private middle states.** Fix any trim epsilon-free NFA recognizing precisely \(D_n\). Because every accepted word has length exactly two, each useful state has a unique possible depth among \(0,1,2\): if it were reached by two prefixes of different lengths, appending a single coaccessible suffix would give accepted words of different lengths. Thus the initial state \(s\), all intermediate states, and all accepting end states are disjoint. Every useful transition goes from depth \(0\) to depth \(1\) or from depth \(1\) to depth \(2\). All depth-two states are accepting and have no outgoing useful transitions.

For each \(i\), select an accepting run
\[
s\xrightarrow{a_i}p_i\xrightarrow{a_i}f_i.
\]
The intermediate states \(p_i\) are pairwise distinct: if \(p_i=p_j\) for \(i\ne j\), the first transition for \(a_i\) followed by the last transition for \(a_j\) would accept the forbidden mixed word \(a_i a_j\). Hence any NFA has at least one initial state, \(n\) intermediate states, and at least one final state, proving \(\nu_{\mathrm{unrestricted}}(D_n)\ge n+2\). The automaton with a common accepting state \(f\) and transitions \(s\xrightarrow{a_i}p_i\xrightarrow{a_i}f\) attains this bound. Its underlying graph is \(K_{2,n}\), planar for all \(n\) (draw the \(n\) two-edge paths side-by-side). Therefore \(\nu_{\mathrm{planar}}(D_n)=n+2\).

Further, if a trim automaton has exactly \(n\) intermediate states, these must be the \(p_i\). Each \(p_i\) has only the first-letter label \(a_i\) on incoming useful transitions, and only the second-letter label \(a_i\) on outgoing useful transitions; otherwise a mixed two-letter word would be accepted. In particular, its entire useful graph has edges \(sp_i\) and edges from \(p_i\) to accepting states. Every \(p_i\) has at least one such second edge.

**2. Cactus lower bound.** Let \(t\) be the number of distinct accepting states in a trim cactus NFA; there may be more than \(n\) intermediate states, but the selected \(n\) paths suffice. For each accepting state \(f\), at most two of the selected \(p_i\) can equal a last-step predecessor of \(f\). Otherwise the five-vertex subgraph consisting of \(s,f\) and three distinct selected middle states contains \(K_{2,3}\): every edge \(sp_i\) then belongs to at least two simple four-cycles, contrary to the cactus condition. Each \(i\) has its chosen end state \(f_i\), so \(n\le2t\). Together with the \(n\) private intermediate states, the initial state, and \(t\) finals, this gives
\[
|Q|\ge1+n+\lceil n/2\rceil.
\]
Partition the letters into pairs and at most one singleton. For each letter introduce its own middle state \(p_i\), and for each pair or singleton introduce one accepting state \(f_B\). Put precisely the two transitions \(s\xrightarrow{a_i}p_i\xrightarrow{a_i}f_B\) when \(i\in B\). Each pair contributes a four-cycle through \(s\), each singleton contributes a two-edge path, and distinct components share only \(s\). The graph is bipartite cactus. There are \(1+n+\lceil n/2\rceil\) states and the accepted language is exactly \(D_n\). This proves the second equality.

**3. Exact tree minimum.** In a tree, no final vertex can have two of the private middle states as predecessors: together with \(s\), they would create a four-cycle. Thus there are at least \(n\) distinct final states, for a total of at least \(2n+1\). Using a private final state for each letter creates an accepting two-edge branch for each letter and a tree with exactly \(2n+1\) states, proving the third equality.

**4. Rigidity and counting.** Suppose a trim cactus NFA attains the bound \(1+n+\lceil n/2\rceil\). It then has exactly \(n\) intermediate and \(t=\lceil n/2\rceil\) accepting states. Write \(d(f)\) for the number of its middle-state predecessors. No accepting state has \(d(f)>2\), and each middle state has at least one final successor. Thus \(\sum_f d(f)\ge n\) and \(\sum_f d(f)\le2t\).

If \(n\) is even, \(2t=n\); equality forces every intermediate to have exactly one final successor and every final to have exactly two predecessors. If \(n\) is odd, \(2t=n+1\). Were \(\sum_f d(f)=n+1\), every final would have two predecessors while exactly one middle vertex would have two final successors. The two resulting four-cycles would both contain the initial-to-middle edge, violating the cactus property. Hence \(\sum_f d(f)=n\), every middle state again has a unique final successor, and exactly one final has one predecessor while all other finals have two. Together with the forced transition labels proved in step 1, this establishes the claimed unique matching form (no extraneous transitions exist in a trim automaton). Pair partitions are counted by \(n!/(2^{\lfloor n/2\rfloor}\lfloor n/2\rfloor!)\). Finally, for \(n\ge3\), the three displayed state minima strictly increase from planar to cactus to tree. \(\square\)

## Verification
The self-contained `check.py` enumerates all nonempty middle-to-final transition choices in the normalized useful layered model for \(1\le n\le5\), tests the cactus condition by counting alternative undirected paths edge-by-edge, and checks acceptance on every input word through length three. It reproduces the minimum states and the labelled optimal assignments (one, one, six, six, and ninety), corresponding to one, one, three, three, and fifteen pair/singleton partitions. It also checks the tree lower threshold. Running `python3 check.py` prints `ALL CHECKS PASS`; its literal output is in `check-output.txt`. These finite tests corroborate, but do not substitute for, the proof for arbitrary \(n\).

## Relationship to prior work
Grobler, Koziel and Siebertz prove that every regular language has an epsilon-free NFA with a bipartite cactus transition graph. Their Figure 1 already uses \(D_3=\{aa,bb,cc\}\) to contrast a noncactus \(K_{2,3}\) automaton with a tree representation. Their conclusion explicitly leaves optimal state blow-up open. The present result resolves the state minimum, exact optimal-structure count and the separation from planar and tree representations for the entire natural family \(D_n\). In particular, the displayed seven-state tree example for \(n=3\) is not a minimum cactus representation: a six-state cactus representation exists.

Book and Chandra proved general planar NFA representability; no sharp cactus-state statement follows. The Kutrib–Malcher–Schneider paper concerns automata with *symmetric transitions* (each labelled step can be reversed with the same label), not graphs obtained by forgetting directions; its theorems do not directly apply here. A matching or biclique-packing formulation is equivalent for this depth-two language, so equivalent historical descriptions remain a possible priority risk.

## Limitations
This is an exact result for the growing-alphabet diagonal length-two language family, not a worst-case asymptotic conversion bound for arbitrary regular languages or fixed alphabets. Only epsilon-free, single-initial-state NFAs are considered; epsilon transitions and edge-labelled multigraph topology are different models. Classifications and counts are up to state renaming with alphabet labels fixed, after trimming non-useful states. Independent external validation and comprehensive historical-priority certification have not been performed.

## References
1. M. Grobler, T. Koziel, S. Siebertz, *Every Regular Language Has a Bipartite Cactus Automaton*, EPTCS 454 (2026), 117–129, arXiv:2610.11717v1, doi:10.4204/EPTCS.454.9 (first submitted 2026-10-08).
2. R. V. Book, A. K. Chandra, *Inherently Nonplanar Automata*, Acta Informatica 6 (1976), 89–94, doi:10.1007/BF00263745.
3. M. Kutrib, A. Malcher, C. Schneider, *Finite automata with undirected state graphs*, Acta Informatica 59 (2022), 163–181, doi:10.1007/s00236-021-00402-0.
