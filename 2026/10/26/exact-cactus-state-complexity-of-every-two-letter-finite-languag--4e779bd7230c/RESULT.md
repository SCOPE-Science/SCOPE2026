# Exact cactus state complexity of every two-letter finite language

## Finding

For a finite alphabet \(\Sigma\) and any nonempty relation \(R\subseteq\Sigma\times\Sigma\), let \(L_R=\{ab:(a,b)\in R\}\). Define the rectangle-cover number \(b(R)\) to be the least positive integer \(t\) for which there are nonempty subsets \(A_i,B_i\subseteq\Sigma\) satisfying \(A_i\times B_i\subseteq R\) for all \(1\le i\le t\) and \(R=\bigcup_{i=1}^{t}(A_i\times B_i)\).

**Theorem.** Among epsilon-free nondeterministic finite automata with exactly one initial state, the least number of states recognizing \(L_R\) is \(b(R)+2\). If the underlying simple undirected transition graph must be a bipartite cactus, the least number is

\[
1+b(R)+\left\lceil\frac{b(R)}2\right\rceil.
\]

Both minima are attained. Thus the additional states due to the cactus constraint are exactly \(\lceil b(R)/2\rceil-1\), for *every* nonempty length-two language.

For the inequality relation on \(k\ge2\) letters, \(R_k=\{(a_i,a_j):i\ne j\}\), put

\[
t_k=\min\left\{t\ge1:\binom{t}{\lfloor t/2\rfloor}\ge k\right\}.
\]

The exact minimum is \(t_k+2\) unrestricted states and \(1+t_k+\lceil t_k/2\rceil\) cactus states. In particular, the cactus optimum for this language grows logarithmically in \(k\), unlike the diagonal equality-language example, whose optimum is linear.

## Assumptions and scope

An NFA is a finite transition system with one distinguished initial state, any set of accepting states, and transitions labeled by one alphabet symbol; there are no epsilon transitions. State count includes initial and accepting states. Dead or inaccessible states are permitted in a presented automaton but can be trimmed without increasing its size or violating the cactus restriction. A graph is a cactus if any two distinct simple cycles have at most one vertex in common. The transition graph forgets edge orientations and labels and collapses parallel labeled edges to one undirected edge. Isolated accepted-empty-language cases and multiple-initial-state conventions are excluded.

## Proof

**Layer lemma.** Take a state-minimal NFA recognizing the nonempty language \(L_R\) and trim states that lie on no accepting computation. Every remaining state occurs on some accepting computation, hence at one of the three path positions \(0,1,2\). It cannot occur at two different positions: concatenating either initial-to-state path with one fixed state-to-final suffix would produce accepted words of different lengths, although every accepted word has length two. Therefore the only depth-zero state is the initial state \(s\), all accepting states are precisely the depth-two states \(F\), and all other states lie in the middle layer \(U\). Each middle state has an incoming transition from \(s\) and an outgoing transition to some state of \(F\). Every transition in the trim automaton goes between consecutive layers, since each state belongs to an accepting computation and all accepted paths have length two.

For each \(u\in U\), let \(A_u\) be the labels of \(s\to u\), and let \(B_u\) be the labels of all transitions from \(u\) to \(F\). The accepted relation is exactly \(R=\bigcup_{u\in U}(A_u\times B_u)\). These are nonempty rectangles contained in \(R\). Consequently \(|U|\ge b(R)\). Since \(F\) is nonempty and is disjoint from \(U\cup\{s\}\), every unrestricted epsilon-free NFA has at least \(2+b(R)\) states. Conversely, given a minimum rectangle cover, introduce one state for each rectangle, give each such state first-symbol transitions from one common initial state and second-symbol transitions to one common accepting state. This realizes \(L_R\) with exactly \(b(R)+2\) states.

**Cactus lower bound.** In a cactus transition graph, an accepting state \(f\in F\) can be adjacent to at most two distinct middle states: if it had neighbors \(u,v,w\in U\), then the two distinct four-cycles \(s-u-f-v-s\) and \(s-u-f-w-s\) would share more than one vertex, contradicting the cactus property. Every middle state has at least one accepting neighbor; hence \(|U|\le2|F|\). It follows that every cactus NFA has at least

\[
1+|U|+|F|\ge 1+|U|+\left\lceil\frac{|U|}2\right\rceil
\ge1+b(R)+\left\lceil\frac{b(R)}2\right\rceil
\]

states. This lower bound holds regardless of which bipartition is chosen.

**Matching bipartite-cactus construction.** From a minimum cover of \(t=b(R)\) rectangles, create the same initial and middle states as above, but now use \(\lceil t/2\rceil\) accepting states, pairing the middle states consecutively. The \(i\)-th middle state points only to accepting state \(\lceil i/2\rceil\), with labels \(B_i\). For each pair, the underlying undirected graph is a four-cycle through \(s\); an unmatched middle state gives a two-edge path. Different four-cycles share only \(s\). The graph is therefore a bipartite cactus, with the exact claimed number of states and recognized relation \(R\).

**Inequality-language corollary.** Suppose \(R_k\) is covered by \(t\) rectangles. Let \(S_i\subseteq\{1,\ldots,t\}\) consist of the rectangle indices whose first-coordinate subsets contain symbol \(a_i\). The exclusion of \((a_i,a_i)\) implies that if \(r\in S_i\) then the \(r\)-th rectangle's second-coordinate subset omits \(a_i\). For every \(i\ne j\), the pair \((a_i,a_j)\) must be covered, so some \(r\in S_i\setminus S_j\) exists. Reversing \(i,j\) shows that the \(k\) sets \(S_i\) form an antichain. Sperner's theorem gives \(k\le\binom{t}{\lfloor t/2\rfloor}\). Conversely, choose \(k\) distinct middle-layer subsets \(S_i\subseteq\{1,\ldots,t_k\}\) of size \(\lfloor t_k/2\rfloor\). For each \(r\), let \(A_r=\{a_i:r\in S_i\}\) and \(B_r=\{a_j:r\notin S_j\}\). Then \(A_r\times B_r\) omits the diagonal and covers every ordered off-diagonal pair for some \(r\); no rectangle is empty for a minimal \(t_k\). This proves \(b(R_k)=t_k\). The cactus and unrestricted formulas now follow from the main theorem.

## Verification

The accompanying standard-library script `verify_boolean_rank.py` independently enumerates all \(15\) nonempty binary relations and all \(511\) nonempty ternary relations, constructs minimum rectangle covers via exact breadth-first search on bitmasks, constructs matching cactus NFAs, checks acceptance on all input words through length four, and checks bipartiteness and pairwise intersections of simple cycles. It also constructs Sperner-optimal covers for inequality languages on alphabets of size \(2\) through \(14\). Running `python verify_boolean_rank.py` produced `VERIFY_OK`. These computations test constructions and small cases; the all-alphabet minimality is established by the preceding proof, not by finite enumeration.

## Relationship to prior work

Grobler, Koziel and Siebertz (2026) proved that every regular language has an epsilon-free bipartite-cactus automaton, motivating an exact state-minimization question. Iván and collaborators (2014, Proposition 7) described the biclique-cover correspondence for two-letter languages, optimizing the **number of transitions** of epsilon-free NFAs, not cactus-constrained **numbers of states**. The underlying biclique-cover rank and the crown-graph antichain formula are classical; they are not claimed new here. The new mathematical content is the precise cactus state-cost formula for every nonempty two-letter relation, including the sharp upper construction and its matching cycle-intersection lower bound.

## Limitations

This is a characterization of length-exactly-two languages under a single-initial-state and epsilon-free convention. It does not minimize transition count, decide arbitrary regular-language cactus-state complexity, or apply to automata allowing epsilon transitions. The October 2026 cactus-automata paper was accessible in abstract form but not in full text during the comparison, leaving an explicit possible-overlap risk. Nothing here asserts independent external validation.

## References

1. M. Grobler, T. Koziel, S. Siebertz, *Every Regular Language Has a Bipartite Cactus Automaton*, arXiv:2610.11717 (first posted 2026-10-08), https://arxiv.org/abs/2610.11717.
2. S. Iván, Á. D. Lelkes, J. Nagy-György, B. Szörényi, G. Turán, *Biclique coverings, rectifier networks and the cost of ε-removal*, arXiv:1406.0017 (2014), especially Proposition 7, https://arxiv.org/abs/1406.0017.
3. P. C. Fishburn, P. L. Hammer, *Bipartite dimensions and bipartite degrees of graphs*, Discrete Mathematics 160 (1996), 127–148, DOI:10.1016/0012-365X(95)00154-O.
