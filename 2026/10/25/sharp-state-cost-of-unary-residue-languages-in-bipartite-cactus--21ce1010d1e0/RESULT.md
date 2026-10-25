# Sharp state cost of unary residue languages in bipartite-cactus automata

## Finding

For integers \(p\ge1\) and \(0\le r<p\), define the unary residue language
\[
L_{p,r}=\{a^n:n\ge0,\ n\equiv r\pmod p\}.
\]
Among epsilon-free NFAs with one initial state, no self-loops, a transition-compatible two-coloring (every transition crosses the colors), and a cactus as the underlying simple transition graph, the exact minimum number of states is
\[
\operatorname{sc}_{\mathrm{bc}}(L_{p,r})=\operatorname{lcm}(p,2).
\]
For unrestricted epsilon-free NFAs, where self-loops are allowed, the exact minimum is \(p\). Hence the bipartite-cactus constraint costs no states for even \(p\), and exactly a factor of two for odd \(p\).

## Assumptions and scope

An NFA is epsilon-free and has a single initial state. Its transition graph is the undirected simple graph on the states obtained by forgetting transition directions and labels; parallel transitions collapse to one edge. A cactus is a graph in which every edge belongs to at most one simple cycle. A transition-compatible two-coloring assigns each state one of two colors and requires every transition to go between different colors; this explicitly excludes self-loops, including in the one-state case. The alphabet is exactly \(\{a\}\). The accepting set may be any subset of states.

The result concerns the single-residue languages \(L_{p,r}\), not arbitrary unary regular languages, multiple residue classes, or alphabets with two or more symbols.

## Proof

Write \(m=\operatorname{lcm}(p,2)\).

**Lower bound with the bipartition.** Let an NFA of the required kind have \(N\) states and recognize \(L_{p,r}\). The language is infinite, so choose an accepted word \(a^n\) with \(n\ge N\), and fix an accepting run \(q_0,q_1,\ldots,q_n\). By the pigeonhole principle some state repeats. Choose a repeated-state interval of minimum positive length: \(q_i=q_j\), with \(i<j\) and \(\ell=j-i\). Minimality makes \(q_i,q_{i+1},\ldots,q_{j-1}\) distinct, so this interval is a directed simple cycle with \(\ell\) states. Repeating the cycle once more gives an accepting run of length \(n+\ell\). Both \(n\) and \(n+\ell\) are congruent to \(r\) modulo \(p\), so \(p\mid\ell\). Every step changes color; therefore the cycle length \(\ell\) is even. Consequently \(m\mid\ell\), and \(N\ge\ell\ge m\).

**Matching construction.** Take states \(0,1,\ldots,m-1\), initial state \(0\), and the transitions \(i\xrightarrow{a}(i+1)\bmod m\). Declare exactly those states \(i\) with \(i\equiv r\pmod p\) accepting. A run on \(a^n\) ends at state \(n\bmod m\), so it accepts exactly when \(n\equiv r\pmod p\). Since \(m\) is even, coloring state \(i\) by the parity of \(i\) makes every transition cross colors (including the wraparound edge). If \(m=2\), the underlying simple graph is a single edge; if \(m\ge4\), it is an even cycle. In either case it is a bipartite cactus. This gives the matching upper bound \(m\).

**Unrestricted baseline.** For any epsilon-free NFA with \(N\) states recognizing \(L_{p,r}\), the same repeated-state argument on an accepted run of length at least \(N\) produces a directed cycle of length \(\ell\). Pumping the cycle yields accepted lengths differing by \(\ell\); because every accepted length is congruent to \(r\) modulo \(p\), we have \(p\mid\ell\), and hence \(N\ge p\). A directed cycle of length \(p\), with initial state \(0\) and the unique accepting state \(r\), recognizes \(L_{p,r}\). For \(p=1\), this is the one-state automaton with a self-loop, allowed in the unrestricted class. Thus the unrestricted minimum is exactly \(p\).

## Verification

The lower bound uses an actual accepting run and a simple cycle obtained from a shortest repeated-state interval; it does not infer impossibility from a finite enumeration. The cycle-pumping argument applies for every \(p\ge1\) and every residue \(0\le r<p\). The construction explicitly handles \(p=1\) and the graph case \(m=2\). No computational certificate is needed. The conclusion is an exact state minimum within the stated automaton class, not a claim about the size of the general construction for arbitrary regular expressions.

## Relationship to prior work

Grobler, Koziel, and Siebertz prove that every regular language has an epsilon-free NFA whose transition graph is a bipartite cactus. Their conclusion explicitly leaves tight state-complexity bounds for such representations as an open direction. The theorem here gives an exact boundary case for the natural unary residue languages: the parity constraint forces the shortest accepting cycle to have length divisible by both \(p\) and \(2\), and a cycle of that length attains the bound.

Classical work on unary automata studies eventual periodicity, unary state complexity, and the costs of regular-language operations. The cited works do not impose the transition-compatible bipartite-cactus restriction in the statements inspected for this result. No general lower bound for arbitrary unary languages is asserted here.

## Limitations

The result establishes exact complexity only for \(L_{p,r}\). It does not determine the minimum number of states for arbitrary ultimately periodic sets of lengths, for unions of several residue classes, or for non-unary languages. It does not bound the blow-up of the full regular-expression-to-cactus construction. The originality comparison is literature-led rather than an exhaustive proof that no related statement exists.

## References

1. Mario Grobler, Till Koziel, and Sebastian Siebertz, “Every Regular Language Has a Bipartite Cactus Automaton,” in EPTCS 454 (2026), 117–129; the proceedings volume arXiv:2610.08898 was posted 2026-10-06 and lists the paper at pp. 117–129; the article-specific arXiv version is arXiv:2610.11717 (posted 2026-10-08); DOI 10.4204/EPTCS.454.9.
2. Wojciech Czerwiński, Maciej Dębski, Tomasz Gogasz, Gordon Hoi, Sanjay Jain, Michał Skrzypczak, Frank Stephan, and Christopher Tan, “Languages given by Finite Automata over the Unary Alphabet,” arXiv:2302.06435; LIPIcs FSTTCS 2023, Article 22; DOI 10.4230/LIPIcs.FSTTCS.2023.22.
3. Giovanni Pighizzini and Jeffrey Shallit, “Unary Language Operations, State Complexity and Jacobsthal’s Function,” International Journal of Foundations of Computer Science 13(1) (2002), 145–159; DOI 10.1142/S012905410200100X.
