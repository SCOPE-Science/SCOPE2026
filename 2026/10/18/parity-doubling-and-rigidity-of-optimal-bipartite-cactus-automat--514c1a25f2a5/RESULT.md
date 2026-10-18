# Parity-doubling and rigidity of optimal bipartite-cactus automata for length congruences

## Finding
Let \(\Sigma\ne\varnothing\) be any finite alphabet, let \(m\ge2\) be an integer, and let \(0\le r<m\). Define the regular length-congruence language
\[
L_{m,r}=\{w\in\Sigma^*: |w|\equiv r\pmod m\}.
\]
Among epsilon-free nondeterministic finite automata with a single initial state and a bipartite-cactus transition graph **with every transition changing color**, the exact minimum number of states is
\[
\boxed{N_{\rm bc}(L_{m,r})=\operatorname{lcm}(m,2)=\begin{cases}m,&m\text{ even},\\2m,&m\text{ odd}.\end{cases}}
\]
Moreover, every minimum-state automaton is isomorphic, including all labeled transitions, its initial state and its accepting set, to the following canonical automaton. Put \(h=\operatorname{lcm}(m,2)\), take states \(\mathbb Z/h\mathbb Z\), initial state \(0\), and, **for every** \(a\in\Sigma\), put the transition \(i\xrightarrow{a}i+1\pmod h\). The accepting states are exactly those residues \(i\pmod h\) with \(i\equiv r\pmod m\). In particular, the minimum realization is deterministic and has one accepting state for even \(m\) and two for odd \(m\).

For comparison, an unrestricted epsilon-free NFA needs exactly \(m\) states. Thus the bipartite-cactus restriction has optimal multiplicative cost precisely \(1\) for even moduli and \(2\) for odd moduli, with uniqueness of the optimal realization.

## Assumptions and scope
An NFA is \((Q,\Sigma,\Delta,s,F)\), with finite \(Q\), single initial state \(s\), arbitrary \(F\subseteq Q\), no epsilon transitions, and possibly incomplete, nondeterministic transitions. Its undirected transition graph forgets labels and directions between distinct states. A *transition-compatible bipartition* \(Q=Q_0\sqcup Q_1\) requires \(\Delta\subseteq(Q_0\times\Sigma\times Q_1)\cup(Q_1\times\Sigma\times Q_0)\), prohibiting self-loops. A cactus has any two simple undirected cycles meeting in at most one vertex. The result includes unary alphabets and the boundary \(m=2\); it does not claim optimality among automata with epsilon transitions.

## Proof
Put \(h=\operatorname{lcm}(m,2)\). **Pump-divisibility lemma.** Suppose an epsilon-free NFA accepts exactly \(L_{m,r}\). Any positive-length closed subwalk of an accepting run has length divisible by \(m\). Indeed, if an accepting run on \(w\) has a state repeated after \(d>0\) letters, inserting an additional traversal of that same closed subwalk gives another accepted word of length \(|w|+d\). Both lengths are \(r\pmod m\), so \(m\mid d\). In a transition-compatible bipartition, every closed walk has even length, whence \(h\mid d\).

**Lower bound.** Pick a word in \(L_{m,r}\) of length at least \(h\) (the alphabet is nonempty, so such a word exists). Take any accepting run \(q_0,q_1,\ldots,q_t\). The first \(h\) states \(q_0,\ldots,q_{h-1}\) must be distinct, for otherwise two equal states would delimit a positive closed subwalk shorter than \(h\). Thus \(|Q|\ge h\).

**Upper bound.** In the claimed \(h\)-state automaton every input letter increments the residue modulo \(h\), so the accepted lengths are exactly those congruent to \(r\pmod m\), because \(m\mid h\). Its graph is an undirected cycle of even length when \(h\ge4\) and a single edge when \(h=2\). Both are bipartite cacti, and every transition changes color. This proves the state bound.

**Rigidity at equality.** Now suppose \(|Q|=h\). For an accepted word of length at least \(h\), every initial \(h\) states of its accepting run are distinct. The next state \(q_h\) must repeat one of the previous \(h\), and pump-divisibility forces that repeated position to be \(q_0\): any other repetition would create a closed subwalk of length strictly between \(0\) and \(h\). Consequently the automaton contains a directed Hamiltonian cycle \(q_0\to q_1\to\cdots\to q_{h-1}\to q_0\) (with \(h=2\) interpreted as two opposing arcs). In the case \(h\ge4\), a cactus containing this spanning undirected cycle cannot contain an additional undirected edge: any chord would share several edges with existing cycles. For \(h=2\), there is just one possible undirected edge.

Every further arc is therefore either a self-loop, a forward cycle arc, or a reverse of a cycle arc. A self-loop at any vertex would allow a productive accepting run to be lengthened by \(1\), violating \(m\ge2\). For \(h\ge4\), a reverse arc at \(q_{i+1}\to q_i\) can be inserted after the existing forward arc \(q_i\to q_{i+1}\) in any sufficiently long accepting run passing through \(q_i\), adding exactly \(2\) letters and violating \(m\ge3\) (indeed \(h\ge4\) implies \(m\ge3\) except \(m=4\), also excluded). Hence every arc is a forward arc of the fixed cycle; for \(h=2\) both directions are precisely its forward cycle arcs. The graph has no unused states.

To recognize **every** word whose length lies in the residue class, all labels must occur on every forward arc: take a sufficiently large accepted length and prescribe an arbitrary alphabet letter at the corresponding phase. The cycle admits no alternative state path, so omitting that label makes this word unrecognizable. Finally each cyclic state must be accepting exactly when its position is congruent to \(r\pmod m\), since arbitrarily long words visit each state at lengths in its residue class modulo \(h\). This yields the asserted unique labeled automaton.

**Unrestricted NFA comparison.** The ordinary \(m\)-state modular DFA gives the upper bound. Any accepting run on a sufficiently long word in \(L_{m,r}\) has no closed subwalk shorter than \(m\), by the same pumping argument; thus it visits at least \(m\) distinct states. This proves the unrestricted lower bound.

## Verification
A standalone Python script (`verify.py`) checks the canonical transition systems for each \(2\le m\le25\), every residue \(r\), and both unary and binary alphabets. It tests each accepted length through \(4h\), checks the actual undirected cactus graph and proper transition coloring, and checks exact acceptance and final-state counts. The infinite result follows from the preceding proof; finite verification is only a consistency check.

## Relationship to prior work
Grobler, Koziel and Siebertz prove that every regular language admits an epsilon-free bipartite-cactus NFA but explicitly leave **tight state-complexity blow-up** open (2026, Theorem 1.1 and Section 4). The present theorem gives an exact, structurally rigid answer for the natural family of length-congruence languages. The general construction does not imply the optimal bound or the classification of equality cases; neither does the textbook \(m\)-state minimal DFA establish a lower bound in the restricted NFA model. The lower bound needs simultaneous preservation of a congruence and the parity of every accepting closed walk.

## Limitations
The result covers a natural but restricted language family and does not settle worst-case blow-up for arbitrary regular languages. The rigidity statement assumes the single-initial-state epsilon-free model and transition-compatible bipartition; a graph convention that ignores self-loops alone is not enough to define the permitted model. Elementary pumping arguments are standard; the claim of originality concerns their sharp combination with the restricted representation model and its full equality classification. Historical priority under another terminology is possible.

## References
1. Mario Grobler, Till Koziel, Sebastian Siebertz, *Every Regular Language Has a Bipartite Cactus Automaton*, arXiv:2610.11717, first public 2026-10-08, Theorem 1.1, Definition 3.2, Section 4. https://arxiv.org/abs/2610.11717
2. Ronald V. Book and Ashok K. Chandra, *Inherently Nonplanar Automata*, Acta Informatica 6 (1976), 89–94. https://doi.org/10.1007/BF00263745
