# The three-rank complexity spectrum of McKinsey validity on incidence frames

## Finding
Let \(\mathcal{H}=(V,\mathcal E)\) be a finite, simple, \(k\)-uniform hypergraph, with \(k\in\{1,2,3\}\); isolated vertices and the empty edge family are allowed, but individual hyperedges have exactly \(k\) distinct vertices. Form its **three-layer incidence Kripke frame** \(F(\mathcal H)\) with worlds \(\{r\}\sqcup\mathcal E\sqcup V\), edges \(rRe\) for each \(e\in\mathcal E\), \(eRv\) exactly when \(v\in e\), and \(vRv\) for every \(v\in V\), and no other accessibility edges. Write \(\mathsf M=\Box\Diamond p\rightarrow\Diamond\Box p\).

The frame validates \(\mathsf M\) precisely when \(\mathcal H\) admits **no** vertex two-colouring with every hyperedge nonmonochromatic. Consequently the decision problem \(F(\mathcal H)\models\mathsf M\), promised that the input has this incidence form, has the following sharp uniform-rank spectrum:

* \(k=1\): first-order definable (and decidable in uniform \(\mathsf{AC}^{0}\)); it holds exactly when \(\mathcal E\ne\varnothing\).
* \(k=2\): \(\mathsf L\)-complete under first-order interpretations (hence uniform \(\mathsf{AC}^{0}\) many-one reductions). It holds exactly when the underlying undirected graph has an odd cycle.
* \(k=3\): \(\mathsf{coNP}\)-complete under logspace many-one reductions, by the NP-completeness of two-colouring 3-uniform hypergraphs.

In particular, **rank three is the minimum uniform edge size in this natural incidence family where the known general \(\mathsf{coNP}\) bound remains complete**, whereas exact rank two is deterministic-logspace complete. No strict complexity separation between \(\mathsf L\) and \(\mathsf{coNP}\) is asserted. First-order nondefinability on the rank-two slice already follows from the cycle family of van Benthem, ten Cate, and Yang [1]; it is not claimed here as a new result.

## Assumptions and scope
A frame validates \(\mathsf M\) if the formula holds at *every* world for *every* classical Boolean valuation of \(p\). The three sorts \(\{r\}\), \(\mathcal E\), and \(V\) in \(F(\mathcal H)\) are formally disjoint even when labels coincide. The decision problems accept standard finite relational encodings of promised incidence frames, or equivalent hypergraph encodings: the distinguished root, the nonreflexive edge worlds, and the reflexive element worlds can be identified on this promised class in logarithmic space. For \(\mathcal E=\varnothing\), \(r\) is an isolated world and the axiom is invalid there. Empty **individual** hyperedges are excluded, which matters for the validity argument at hyperedge worlds.

First-order reductions are used in their standard finite-model-theory sense: fixed-arity tuple encodings may construct polynomially many output vertices, with adjacency defined by first-order formulas over the ordered input structure. The \(\mathsf L\) hardness statement can equivalently be read for standard DLOGTIME-uniform \(\mathsf{AC}^{0}\) encodings.

## Proof
**Semantic lemma.** Fix any valuation \(P\subseteq W\). At a reflexive element-world \(v\), both \(\Box\Diamond p\) and \(\Diamond\Box p\) have the truth value of \(p\) at \(v\); hence \(\mathsf M\) holds. At a nonempty hyperedge-world \(e\), if \(\Box\Diamond p\) holds, then every \(v\in e\) satisfies \(p\) (because \(v\) sees only itself). Since \(e\) has at least one successor, at least one such \(v\) satisfies \(\Box p\), so \(\Diamond\Box p\) holds. Therefore failure can only occur at \(r\).

At \(r\), \(\Box\Diamond p\) holds exactly if every \(e\in\mathcal E\) meets \(P\cap V\). On the other hand, \(\Diamond\Box p\) fails exactly if no \(e\in\mathcal E\) is contained in \(P\cap V\). Thus failure at \(r\) is equivalent to a two-colouring of \(V\), with colour classes \(P\cap V\) and \(V\setminus P\), in which every hyperedge meets both colours. This equivalence is still correct for \(\mathcal E=\varnothing\), because the vacuous premise is true and the empty existential conclusion is false.

**Rank one.** A singleton hyperedge cannot meet both colours. Therefore, whenever an edge exists, no refuting colouring exists and the frame validates \(\mathsf M\); with no hyperedges, the axiom fails at \(r\). The condition \(\mathcal E\ne\varnothing\) is first-order on the incidence encoding.

**Rank two: characterization and upper bound.** Two-colouring a graph with every edge bichromatic is ordinary graph bipartiteness. Hence frame validity is equivalent to graph nonbipartiteness, equivalently the existence of an odd cycle. An undirected graph has an odd cycle exactly if its parity double cover, with vertices \((v,b)\) for \(b\in\{0,1\}\) and edges \((u,b)\sim(v,1-b)\) whenever \(u\sim v\), connects \((v,0)\) to \((v,1)\) for some vertex \(v\). Reingold's deterministic-logspace undirected connectivity algorithm [3] checks each candidate using logarithmic workspace. Iterating over \(v\) also uses logarithmic workspace. Thus rank-two frame validity lies in \(\mathsf L\).

**Rank two: hardness.** Reduce **undirected \(s\)-\(t\) connectivity** to rank-two frame validity. Take a finite undirected input graph \(G=(U,E)\) with distinct designated \(s,t\). Subdivide every original edge once, creating a bipartite graph \(S(G)\) whose original vertices lie in one side, and then add the single edge \(st\). Call the resulting graph \(H\). If \(s\) and \(t\) are connected in \(G\), a subdivided \(s\)-to-\(t\) path in \(S(G)\) has even length; adding \(st\) produces an odd cycle in \(H\). Conversely, if they are disconnected in \(G\), they lie in different connected components of \(S(G)\), whose bipartite two-colourings can be flipped independently so that the new edge \(st\) also joins opposite colours. Thus
\[
 s\stackrel G\longleftrightarrow t\quad\Longleftrightarrow\quad
 H\text{ has an odd cycle}\quad\Longleftrightarrow\quad F(H)\models\mathsf M.
\]
The construction is first-order interpretable: original vertices, subdivider vertices indexed by original edges, and incidence-frame worlds can all be represented by bounded tuples and fixed tags, with relation membership given by local formulas. Undirected \(s\)-\(t\) connectivity is \(\mathsf L\)-complete under first-order reductions (alternatively, reduce a halting deterministic logarithmic-space computation to undirected connectivity using its time-bounded functional configuration graph, which has a unique terminal sink in each component). Hence rank-two frame validity is \(\mathsf L\)-hard under first-order reductions and therefore \(\mathsf L\)-complete.

**Rank three.** Nonvalidity has a witness consisting of a two-colouring of \(V\) that makes every 3-element hyperedge bichromatic, checkable in polynomial time. Conversely, monotone not-all-equal 3-SAT, equivalently two-colourability of simple 3-uniform hypergraphs, is NP-complete [4]. By the semantic lemma, a yes-instance of that problem maps in logspace to a rank-three incidence frame **not** validating \(\mathsf M\). Thus validity is \(\mathsf{coNP}\)-complete.

## Verification
The standalone `verify_mckinsey_rank.py` (Python standard library only) implements the Kripke satisfaction test at **every world** over **all full valuations** on the smaller frames and tests the structurally sufficient root/leaf valuations on larger frames. It checks the semantic equivalence for all \(62\) labelled singleton-edge hypergraphs of orders \(1\) through \(5\), all \(1099\) labelled simple undirected graphs of orders \(1\) through \(5\), and all \(1042\) labelled simple 3-uniform hypergraphs of orders \(3\) through \(5\). It also checks \(410\) marked graph reductions up to four original vertices against a separate graph connectivity algorithm. Command: `python3 verify_mckinsey_rank.py`; expected output starts `PASS: 62 rank-one, 1099 graph, 1042 rank-three hypergraph instances; 410 marked connectivity reductions`. These finite checks corroborate the construction but do not replace the unrestricted proofs or prove any complexity lower bound on their own.

## Relationship to prior work
Van Benthem, ten Cate, and Yang [1, §5.4, Theorem 26] give the general set-splitting construction and prove \(\mathsf{coNP}\)-completeness for finite-frame McKinsey validity. Their [1, §5.2, Lemma 23] explicitly uses odd/even incidence cycles to distinguish validity and obtain non-first-order-definability. Those semantic and first-order facts are **prior results**, not novelty claims here. What is distinguished here is the *complete decision-complexity spectrum at fixed hyperedge ranks*, especially the exact first-order-reduction \(\mathsf L\) lower bound at rank two together with its logspace upper bound, and the sharp transition at rank three. Takahashi [2] provides further recent context for using finite-frame validity complexity to study modal logics, not the restricted incidence-frame classification. Reingold [3] supplies the logspace graph reachability algorithm; Schaefer's dichotomy [4] supplies the established hard rank-three colouring problem.

## Limitations
The statement concerns only the specified incidence-frame family, not arbitrary Kripke frames with bounded *total* outdegree; the root may have arbitrarily many successors. It does not claim first-order definability or a logspace algorithm for unrestricted frame validity. The rank-three conclusion relies on classical NP-completeness of monotone not-all-equal 3-SAT, and the rank-two upper bound relies on Reingold's theorem. First-order nondefinability on the rank-two cycle subfamily is credited to [1], not reproved. Completeness labels do not imply \(\mathsf L\ne\mathsf{coNP}\). Unindexed equivalent treatments of rank-restricted McKinsey validity could exist.

## References
[1] J. van Benthem, B. ten Cate, X. Yang, *When do modal definability and preservation theorems transfer to the finite?*, arXiv:2603.12171v1, first public 2026-03-12, §§5.2 and 5.4, https://arxiv.org/html/2603.12171v1.

[2] T. Takahashi, *Non-elementary modal logics, assuming P ≠ NP*, arXiv:2609.10872v1, first public 2026-09-09, https://arxiv.org/abs/2609.10872.

[3] O. Reingold, *Undirected connectivity in log-space*, Journal of the ACM **55** (2008), article 17, https://doi.org/10.1145/1391289.1391291.

[4] T. J. Schaefer, *The complexity of satisfiability problems*, Proceedings of the Tenth Annual ACM Symposium on Theory of Computing (1978), 216–226; https://doi.org/10.1145/800133.804350; the NP-complete monotone NAE-3SAT / 3-uniform hypergraph two-colouring case.
