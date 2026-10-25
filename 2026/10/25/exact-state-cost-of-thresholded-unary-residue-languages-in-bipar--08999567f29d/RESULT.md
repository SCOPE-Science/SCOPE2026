# Exact state cost of thresholded unary residue languages in bipartite-cactus NFAs

## Finding

{claim}

## Assumptions and scope

The alphabet is the singleton \(\{a\}\), and \(\mathcal L_{p,m}\) contains exactly the lengths \(m,m+p,m+2p,\ldots\). Thus \(m\) is the least accepted length and \(p\) is the least positive eventual period. The automata are finite, have one initial state, and have no \(\varepsilon\)-transitions. A transition-compatible bipartition means every transition joins states of opposite colors. The simple undirected transition graph forgets transition direction and labels; a cactus is a graph in which each edge belongs to at most one simple cycle. Unreachable states can be deleted, so the lower bound applies to the reachable part.

Equivalently, writing \(\ell=\operatorname{lcm}(p,2)\), the minimum is \(\max(p,m+1)\) for even \(p\), and \(\max(2p,m+p+1)\) for odd \(p\). The theorem concerns this language family and this graph constraint; it does not assert a minimum for arbitrary regular languages.

## Proof

**Lower bound.** Since \(\mathcal L_{p,m}\) is infinite, some accepting run contains a directed cycle. Choose a simple directed cycle of length \(d\) on an accepting run. Repeating that cycle preserves acceptance, so accepted lengths differ by \(d\). Every accepted length is congruent to \(m\pmod p\), hence \(p\mid d\). Every transition crosses the bipartition, so \(d\) is even. The simple cycle therefore has at least \(\ell=\operatorname{lcm}(p,2)\) states.

A shortest accepting path has length \(m\) and is simple: if a state repeated, deleting the intervening nonempty loop would give a shorter accepted word. Therefore at least \(m+1\) states are necessary.

If \(p\) is odd, consider an accepting path of length \(m+p\), which exists by definition of the language. If it repeated a state, deleting the intervening loop would shorten it by a positive even multiple of \(p\), hence by at least \(2p\). The resulting accepted length would be less than \(m\), a contradiction. So this path is simple and requires \(m+p+1\) states. The lower bound is consequently \(\max(2p,m+p+1)\) for odd \(p\), and \(\max(p,m+1)\) for even \(p\).

**Matching construction.** Put \(t=\max(0,m-p+1)\) and \(e=m-t=\min(m,p-1)\). Build a directed path of \(t\) edges leading into a directed cycle of length \(\ell\); when \(t=0\), the initial state is on the cycle. On the cycle, mark exactly the positions with offsets \(e,e+p,e+2p,\ldots\) that are less than \(\ell\) as accepting. If \(p\) is even, the cycle has length \(p\) and one accepting position. If \(p\) is odd, the cycle has length \(2p\) and two accepting positions separated by \(p\). The accepted lengths are therefore exactly \(t+e+kp=m+kp\) for \(k\ge0\).

The cycle length \(\ell\) is even, so its vertices can be colored alternately; extend that coloring along the path. Every transition crosses colors. The underlying simple graph is a path attached to one cycle (or, for \(\ell=2\), a path whose two directed cycle arcs form one undirected edge), hence a cactus. The construction has \(t+\ell=\max(\ell,m+\ell-p+1)\) states, attaining the lower bound in both parity cases.

## Verification

The accompanying `verify_construction.py` uses only the Python standard library. It checks 260 parameter pairs \(1\le p\le10\), \(0\le m\le25\), verifies accepted-length membership through \(m+5p+5\), confirms the state-count formula, checks a proper bipartition, and checks that the underlying simple graph is connected and has at most one cycle. These finite checks test the displayed construction; they are not used as a proof of the universal lower bound.

## Relationship to prior work

Grobler, Koziel, and Siebertz prove that every regular language has an equivalent \(\varepsilon\)-free NFA whose transition graph is a bipartite cactus. Their theorem is an existence theorem and does not give the minimum state count for this unary family. Work on unary automata studies Chrobak normal form and state costs for general unary NFAs, but does not supply the bipartite-cactus constraint or the exact threshold formula proved here. The present statement quantifies the exact cost of a finite initial delay while preserving the prescribed arithmetic progression of accepted lengths.

## Limitations

The result assumes a single initial state, no \(\varepsilon\)-transitions, and a transition-compatible bipartition. Removing those restrictions may change the optimum. The proof establishes no state-minimum formula for arbitrary ultimately periodic unary languages with several accepted residues, nor for non-unary alphabets. Literature searches did not establish uniqueness of this result; differently phrased or unindexed prior work remains a residual risk.

## References

1. M. Grobler, T. Koziel, and S. Siebertz, “Every Regular Language Has a Bipartite Cactus Automaton,” *Electronic Proceedings in Theoretical Computer Science* 454 (2026), 117–129. First public version: 2026-10-08. DOI: 10.4204/EPTCS.454.9. https://arxiv.org/abs/2610.11717
2. W. Czerwiński, M. Dębski, T. Gogasz, G. Hoi, S. Jain, M. Skrzypczak, F. Stephan, and C. Tan, “Languages given by Finite Automata over the Unary Alphabet,” arXiv:2302.06435 (2023). https://arxiv.org/abs/2302.06435
