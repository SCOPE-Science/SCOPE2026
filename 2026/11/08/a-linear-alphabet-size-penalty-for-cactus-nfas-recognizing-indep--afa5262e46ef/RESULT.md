# A linear alphabet-size penalty for cactus NFAs recognizing independent parity

## Finding
For every integer \(k\ge 3\), let \(\Sigma_k=\{a_1,\ldots,a_k\}\) and let
\[
L_k=\{w\in\Sigma_k^*:|w|_{a_i}\equiv 0\pmod 2\text{ for every }1\le i\le k\}.
\]
Every **epsilon-free, single-initial-state nondeterministic finite automaton** accepting \(L_k\) whose underlying *simple undirected* transition graph is a cactus has at least
\[
\boxed{1+3k\,2^{k-3}}
\]
states. In contrast, an unrestricted nondeterministic automaton accepting \(L_k\) needs exactly \(2^k\) states. Consequently the ratio of the minimum cactus-NFA size to the unrestricted minimum is at least \(3k/8+2^{-k}\), and in particular grows without bound with the alphabet size. The lower bound applies even without separately requiring the cactus graph to be bipartite.

The sample lower bounds are \(10\), \(25\), and \(61\) states at \(k=3,4,5\), compared with \(8\), \(16\), and \(32\) unrestricted states. These are **lower bounds**, not asserted sharp cactus-state counts.

## Assumptions and scope
An NFA is a finite directed, letter-labelled transition system with one initial state, a set of accepting states, no epsilon transitions, and ordinary existential word acceptance. Its transition graph is the undirected simple graph obtained by ignoring transition orientation, symbols, and parallel arcs; loops, if present, count as loops and so cannot occur in a bipartite graph. A *cactus* is an undirected graph whose simple cycles have no edges in common (equivalently, distinct cycles meet at most at one vertex in each connected component). The proof trims to states on successful paths; this retains the recognized language and the cactus property.

No completeness, determinism, unambiguity, or fixed-size alphabet is assumed. No upper bound on cactus-state complexity or exact minimum is claimed. The ambient alphabets have \(k\) distinct letters, and the result concerns the simultaneous even-count language, not just total-length parity.

## Proof
**1. Every useful NFA state has a well-defined group phase.** Put \(G=(\mathbb Z/2\mathbb Z)^k\), with standard basis \(e_1,\ldots,e_k\), and define the monoid homomorphism \(\mu:\Sigma_k^*\to G\) by \(\mu(a_i)=e_i\). Then \(L_k=\mu^{-1}(0)\). Remove all states not on any accepting path. For each remaining state \(q\), select a word \(u\) taking the initial state to \(q\), and a word \(v\) taking \(q\) to some accepting state. Since \(uv\in L_k\), we have \(\mu(u)+\mu(v)=0\). If another word \(u'\) also reaches \(q\), the run \(u'v\) accepts and so \(\mu(u')+\mu(v)=0\). Thus \(\mu(u')=\mu(u)\). Write this unique value as \(\phi(q)\in G\).

For any useful transition \(q\xrightarrow{a_i}q'\), prefixing a run to \(q\) with that transition shows
\[
\phi(q')=\phi(q)+e_i.
\]
In particular, the parity of the sum of the \(k\) coordinates of \(\phi(q)\) changes along every transition. The underlying simple transition graph of the trimmed automaton is therefore bipartite, even if bipartiteness was not assumed.

**2. Every hypercube edge has a distinct graph-edge lift.** Fix \(g\in G\) and \(1\le i\le k\). Choose \(u\) with \(\mu(u)=g\) and \(v\) with \(\mu(v)=g+e_i\). Then \(\mu(ua_iv)=0\), so the NFA has an accepting run on \(ua_iv\). At its designated \(a_i\) transition, the initial and terminal states have phases \(g\) and \(g+e_i\). Thus for each undirected edge \(\{g,g+e_i\}\) of the \(k\)-dimensional Boolean cube, the underlying transition graph has an edge whose endpoint phases are exactly that unordered pair. Distinct cube edges force distinct graph edges, even when multiple NFA states share the same phase. The cube has \(2^k\) vertices of degree \(k\), hence exactly \(k2^{k-1}\) undirected edges. Writing \(E\) for the number of edges of the trimmed simple graph, we have
\[
E\ge k2^{k-1}.
\]
All useful states are reachable from the single initial state, and every successful prefix path is useful, so this undirected trimmed graph is connected.

**3. Bipartite cacti have few edges.** Let a connected simple bipartite cactus have \(N\) vertices, \(E\) edges, and \(c\) distinct cycles. Its blocks are bridges or simple cycles. Each cycle has length at least four. Counting along the block tree gives \(E=N-1+c\). A cycle of length \(\ell\) contributes \(\ell-1\) vertices after its attachment vertex; each bridge contributes one. Consequently \(N-1\ge3c\), and therefore
\[
E=N-1+c\le \frac{4}{3}(N-1).
\]
Combining this with Step 2 yields
\[
N\ge 1+\frac{3}{4}k2^{k-1}=1+3k2^{k-3}.
\]
For \(k\ge3\), the right-hand side is an integer. Since trimming cannot increase the number of states, this is also a lower bound for the original NFA.

**4. The unrestricted NFA minimum is \(2^k\).** A complete deterministic parity-vector automaton with state set \(G\), start and sole accepting state \(0\), and transitions \(g\xrightarrow{a_i}g+e_i\), recognizes \(L_k\). For the converse, choose for each \(g\in G\) a word \(u_g\) with phase \(g\), and let \(v_g=u_g\). Then \(u_gv_h\in L_k\) precisely when \(g=h\). On any accepting run for \(u_gv_g\), mark the state following \(u_g\). If the same marked state occurred for distinct \(g\) and \(h\), splicing the prefix run for \(u_g\) to the suffix run for \(v_h\) would accept \(u_gv_h\), a contradiction. These \(2^k\) states are therefore distinct. This gives the exact unrestricted minimum.

## Verification
The standalone `checker.py` regenerates the Boolean cube's vertices and edges in dimensions \(1\) through \(12\), checks the edge count and all phase-parity changes, independently enumerates \(97{,}742\) short words for the target-language equivalence, and verifies cactus edge inequalities on \(3{,}500\) generated connected bipartite cacti. Run `python3 checker.py`; success prints `VERIFY_OK`. These finite checks are illustrative and do not certify all infinite instances; the proof above handles every \(k\ge3\).

## Relationship to prior work
Grobler, Koziel, and Siebertz (first publicly posted October 8, 2026) prove that every regular language has an epsilon-free NFA with a bipartite cactus transition graph, an existence statement that motivates asking about the size cost of this structural restriction. The present result is a quantitative **lower bound** for the canonical independent-parity family, not a strengthening of their general existence construction. The full openly readable primary text was inspected across Sections 1–4. Theorem 1.1 gives the existence construction and Section 4 expressly leaves optimization and tight state-complexity bounds open; no statement in its constructions gives this independent-parity hypercube-edge lower bound. Historical priority outside the inspected literature remains a risk.

General NFA lower-bound methodology, including fooling sets, is classical (for example, Gruber and Holzer). Here the extra factor is obtained instead from the novel combination of the mandatory phase map, surjective lifting of every Boolean-cube edge, and the edge-density bound for a bipartite cactus. The full recent source explicitly lists tight state-complexity bounds as an open direction in its Conclusion; its construction does not state the factor. Searches for equivalent Cayley-graph, outerplanar, cactus-automaton, and group-language formulations did not identify a previously published theorem implying the bound. Search absence alone does not prove novelty.

## Limitations
The exact minimal number of states among cactus NFAs is not determined. The argument requires epsilon-free, single-initial-state NFAs and a growing \(k\)-letter alphabet. Its \(\Omega(k)\) overhead is not a fixed-alphabet lower bound, and no matching upper bound or classification of all restricted automata is asserted. The complete recent primary text was inspected, but an earlier or unindexed stronger lower bound may still exist. Independent mathematical review remains outstanding.

## References
1. M. Grobler, T. Koziel, S. Siebertz, *Every Regular Language Has a Bipartite Cactus Automaton*, arXiv:2610.11717 (first submitted 2026-10-08); EPTCS 454 (2026), 117–129, DOI 10.4204/EPTCS.454.9. https://arxiv.org/abs/2610.11717
2. H. Gruber, M. Holzer, *Finding Lower Bounds for Nondeterministic State Complexity is Hard*, ECCC TR06-027 (2006). https://eccc.weizmann.ac.il/report/2006/027/
