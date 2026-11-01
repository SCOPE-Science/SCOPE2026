# Exact state cost of thresholded unary residue languages in bipartite-cactus NFAs

## Finding

**Theorem.** Let \(p\ge 1\) and \(m\ge 0\) be integers, and let
\[
\mathcal L_{p,m}=\{a^{m+kp}:k\in\mathbb Z_{\ge0}\}
\]
be a language over the unary alphabet \(\{a\}\). Among all finite nondeterministic automata with exactly one initial state, no \(\varepsilon\)-transitions, a transition-compatible bipartition of the states, and a cactus underlying simple undirected transition graph, the exact minimum number of states recognizing \(\mathcal L_{p,m}\) is
\[
\boxed{\operatorname{sc}_{\mathrm{bipartite\ cactus}}(\mathcal L_{p,m})
=\max\{\ell,m+\ell-p+1\},\qquad \ell=\operatorname{lcm}(p,2).}
\]
Equivalently, this minimum is \(\max(p,m+1)\) if \(p\) is even, and \(\max(2p,m+p+1)\) if \(p\) is odd. An explicit path leading to a directed even cycle attains the lower bound for every parameter pair. In particular, the parity of the eventual period controls the precise state penalty for delaying the first accepted length.

## Assumptions and scope

The alphabet is the singleton \(\{a\}\); acceptance is by a finite directed path from the unique initial state to any accepting state, with one letter consumed per transition. The specified language accepts exactly the lengths \(m,m+p,m+2p,\ldots\), so \(m\) is its least accepted length and \(p\) is its least positive eventual period. A transition-compatible bipartition assigns one of two colors to each state and requires every transition to join opposite colors; in particular, self-loops are prohibited. The underlying simple undirected transition graph forgets directions, duplicate arcs and labels; it is a cactus when every undirected edge lies on at most one simple undirected cycle. All irrelevant unreachable states can be removed, so an optimal automaton is reachable. The theorem does not address arbitrary regular or multi-residue unary languages, or automata without the specified constraints.

## Proof

**1. Lower bound from cycles and the shortest word.** An automaton accepting the infinite language \(\mathcal L_{p,m}\) has an accepting run with a repeated state. In the repeated-state closed segment, choose a simple directed cycle of length \(d\). Inserting an additional traversal of that cycle into the accepting run gives another accepted length differing by \(d\). Since all accepted lengths belong to the single congruence class \(m\bmod p\), it follows that \(p\mid d\). The bipartition forces every directed cycle to have even length, so \(d\ge\ell=\operatorname{lcm}(p,2)\); the cycle has \(d\) distinct states. Therefore any such automaton has at least \(\ell\) states.

A shortest run accepting \(a^m\) has no repeated state: deleting an intervening closed walk would produce an accepted word of length less than \(m\). Thus it has \(m+1\) distinct states. In particular, any admissible automaton has at least \(\max\{\ell,m+1\}\) states.

**2. Stronger odd-period bound.** Suppose \(p\) is odd. Consider an accepting run of length \(m+p\). If the run repeated a state, deleting the intervening nonempty closed walk of length \(d\) would yield another accepted word. The bipartition implies \(2\mid d\), and congruence of all accepted lengths implies \(p\mid d\). Because \(p\) is odd, any such positive \(d\) is at least \(2p\); deletion would yield length at most \(m-p<m\), a contradiction. Hence every length-\(m+p\) accepting run is simple and requires \(m+p+1\) different states. Combining this with the cycle bound, for odd \(p\) we have at least \(\max(2p,m+p+1)\) states. For even \(p\) the preceding two bounds give at least \(\max(p,m+1)\) states.

**3. A matching bipartite-cactus automaton.** Set
\[
t=\max\{0,m-p+1\},\qquad e=m-t=\min\{m,p-1\},\qquad \ell=\operatorname{lcm}(p,2).
\]
Take a directed path of \(t\) edges from the initial state to the initial vertex of a directed cycle of length \(\ell\), where the path and cycle share precisely that terminal vertex; if \(t=0\), start on the cycle. Declare exactly those cycle vertices at forward offsets
\[
e,\ e+p,\ e+2p,\ldots <\ell
\]
to be accepting; all path-interior states are nonaccepting. The set of accepted lengths is precisely
\[
\{t+e+kp:k\ge0\}=\{m+kp:k\ge0\}.
\]
Indeed, when \(p\) is even the cycle has length \(p\) and a unique accepting offset, and when \(p\) is odd its length is \(2p\) and it has two accepting offsets separated by \(p\). Because \(\ell\) is even, the cycle admits an alternating two-coloring, which extends over the initial path. The simple undirected graph is a path attached to a cycle (a tree when \(\ell=2\) and opposite directed cycle arcs reduce to one undirected edge), so it is a cactus. This automaton has exactly
\[
t+\ell=\max\{\ell,m+\ell-p+1\}
\]
states. It attains the relevant lower bound for both parities of \(p\), completing the proof. \(\square\)

## Verification

The separate source `verify_construction.py` uses only the Python standard library. It checks every pair \(1\le p\le10\), \(0\le m\le25\), verifies accepted-length membership through a bounded range beyond \(m+5p\), and confirms the constructed state count, proper bipartition and cactus condition. The finite checks corroborate the witness construction, but the universal minimum follows from the lower bounds and explicit all-parameter construction proved above. The automata are nondeterministic in the permitted model, although the minimizing witness itself is deterministic.

## Relationship to prior work

Grobler, Koziel and Siebertz, *Every Regular Language Has a Bipartite Cactus Automaton* (2026), prove that an equivalent bipartite-cactus NFA exists for every regular language. Their general existence theorem does not determine the minimum state count for the specified thresholded unary family. Work on unary NFAs and Chrobak normal form studies state complexity for more general unary languages, but does not directly establish the present bipartite-cactus minimum or the odd-period simple-run obstruction. The exact even-period bound agrees with the standard \(m\)-delay/pure-period construction; the additional odd-period cost is created by the bipartite transition restriction. These classical ingredients are not asserted to be original independently.

## Limitations

The theorem assumes one initial state, no epsilon transitions, a transition-compatible bipartition and a simple undirected cactus graph. Removing any restriction may change the optimum. No assertion is made for several accepted residues, other alphabets or unrestricted regular languages. The parity-dependent minimum is an exact invariant of this natural infinite family, not a general solution to NFA minimization. An equivalent formula in less-indexed automata literature cannot be ruled out by the bounded source inspection.

## References

1. M. Grobler, T. Koziel, and S. Siebertz, *Every Regular Language Has a Bipartite Cactus Automaton*, Electronic Proceedings in Theoretical Computer Science **454** (2026), 117–129, DOI: 10.4204/EPTCS.454.9, https://arxiv.org/abs/2610.11717 .
2. W. Czerwiński, M. Dębski, T. Gogasz, G. Hoi, S. Jain, M. Skrzypczak, F. Stephan, and C. Tan, *Languages given by Finite Automata over the Unary Alphabet*, arXiv:2302.06435 (2023), https://arxiv.org/abs/2302.06435 .
