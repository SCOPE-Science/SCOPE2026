# Sharp square packing and orientation-uniform enumeration in order-three de Bruijn cycles

## Finding

For every integer \(q\ge 2\) and every cyclic de Bruijn sequence \(C\) of order three on an alphabet \(A\) of \(q\) symbols, there are at most \(\binom{q}{2}\) cyclic consecutive factors of the form \(abab\) (squares of a length-two word). A factor with \(a=b\) never occurs. For distinct symbols \(a,b\), at most one of \(abab\) and \(baba\) occurs.

This bound is attained. More precisely, for each of the \(2^{\binom q2}\) choices of exactly one ordered pattern \(abab\) or \(baba\) for every unordered pair \(\{a,b\}\), there exists an order-three de Bruijn cycle having exactly the chosen squares. **Each pattern of choices is attained equally many times.**

Put \(V=A\times A\), and let \(G_q\) be the directed graph on \(V\) with an edge \((a,b)\to(b,c)\) for every triple \(abc\) except the triples \(aba\) with \(a\ne b\). Parallel edges are treated as distinct when applicable; its loops \(aaa\) are retained. Let \(L\) be its out-degree Laplacian, \(L_{uv}=\delta_{uv}\deg^+_G(u)-m_G(u,v)\). Let \(T_q\) be the determinant obtained by deleting from \(L\) the row and column indexed by \((a_0,a_0)\) for any fixed alphabet symbol \(a_0\). The count, modulo cyclic rotation but *not* relabeling symbols, for each prescribed orientation pattern is exactly

\[
T_q\,((q-1)!)^{q+\binom q2}\,((q-2)!)^{\binom q2}.
\]

In particular \(T_2=1\), \(T_3=108\), \(T_4=3{,}538{,}944\). For the ternary alphabet exactly \(55{,}296\) cycles attain the maximum three length-four squares, with \(6{,}912\) cycles for each of the eight orientation patterns.

## Assumptions and scope

A cyclic de Bruijn sequence of order three is a cyclic word of length \(q^3\) in which every word of length three appears exactly once as a cyclic factor, counting starting positions modulo \(q^3\). A length-four square is four consecutive cyclic symbols \(abab\); occurrences are counted by starting position, not as an abstract pattern up to symbol relabeling. As different triple prefixes occur once, every such four-factor is unique if present. A prescribed orientation is a selection of one of \(abab\) and \(baba\) separately for each unordered pair of distinct symbols. The counted cycles are distinct up to rotation only: neither reversal nor alphabet permutations are identified.

## Proof

**Step 1: universal exclusion and upper bound.** Represent a de Bruijn cycle as an Euler tour of the order-two de Bruijn digraph: its vertices are ordered symbol pairs and its directed edges are all distinct length-three triples \(abc\), from \((a,b)\) to \((b,c)\). Consecutive cyclic edges in the tour correspond to consecutive length-three factors. The length-four square \(abab\) corresponds to the directed consecutive edge-pair \(aba,bab\). If both \(abab\) and \(baba\) occurred, then both successors would be forced, giving a closed, proper two-edge circuit \(aba,bab\) within the Euler tour; since \(q^3>2\), this is impossible. The constant square \(aaaa\) would force the triple \(aaa\) immediately to follow itself, a proper one-edge circuit; this is likewise impossible. Consequently at most one square per unordered unequal symbol-pair occurs.

**Step 2: arbitrary simultaneous realizability.** Delete the \(q(q-1)\) alternating triples \(aba\) with \(a\ne b\) from the original de Bruijn digraph, obtaining \(G_q\). Fix any orientation pattern. For each unordered pair \(\{a,b\}\) whose choice is \(abab\), add one *distinguished artificial loop* at vertex \((a,b)\), encoding the two removed edges \(aba\) followed by \(bab\). For the opposite choice \(baba\), add the loop at \((b,a)\), encoding \(bab\) followed by \(aba\). Denote the resulting directed multigraph by \(H\).

Every vertex \((a,a)\) in \(G_q\) has indegree and outdegree \(q\); every vertex \((a,b)\) with \(a\ne b\) has indegree and outdegree \(q-1\). Thus both \(G_q\) and \(H\) are balanced. They are also strongly connected: an off-diagonal vertex \((a,b)\) reaches \((b,b)\) by the retained triple \(abb\); for unequal \(x,y\), the retained triples \(xxy\) and \(xyy\) give \((x,x)\to(x,y)\to(y,y)\); and every \((x,y)\) is reached from \((x,x)\) using \(xxy\). These paths use no deleted alternating triple. Since \(H\) is finite, connected and balanced, it has an Euler tour. Expand each distinguished loop into the two original alternating edges it encodes. Every length-three edge now occurs exactly once and consecutive edges fit, giving a de Bruijn cycle. Each artificial loop creates its selected length-four square. By Step 1 no other square can occur, so the bound is attained with exactly the specified orientation pattern.

**Step 3: exact equal enumeration.** Conversely, in any maximum-square de Bruijn cycle, for each unordered pair the corresponding two alternating length-three edges must be successive in the selected orientation. Contract that consecutive pair into its distinguished loop in \(H\). Expansion and contraction are inverses on cyclic Euler tours. Each cyclic tour has exactly one occurrence of the triple \(a_0a_0a_0\), so fixing that edge as the first edge gives a unique rooted linear representation of each rotational cycle.

The directed BEST theorem gives the number of Euler tours of \(H\) beginning with this fixed edge as \(t_{(a_0,a_0)}(H)\prod_{v\in V}(\deg^+_H(v)-1)!\), where \(t_{(a_0,a_0)}\) counts in-arborescences towards the named vertex. Artificial loops never belong to arborescences, so \(t_{(a_0,a_0)}(H)=t_{(a_0,a_0)}(G_q)=T_q\) by the directed matrix-tree theorem. There are \(q\) diagonal vertices of degree \(q\), \(\binom q2\) off-diagonal vertices given a loop and hence degree \(q\), and \(\binom q2\) remaining off-diagonal vertices of degree \(q-1\). The displayed factorial product follows; it is independent of the selected orientation pattern. This completes the proof.

## Verification

The accompanying standalone `verify.py` uses an Euler-tour construction for every orientation when \(q=2,3,4\), and tests further selected orientations for \(q=5,6,7\). It computes exact Laplacian cofactors for \(q=2,3,4\) using fraction-free integer elimination. An independent exhaustive edge-tour enumeration roots at the unique triple \(000\) for \(q=2,3\). The ternary square-count histogram is \(\{0:27648,1:124416,2:165888,3:55296\}\), and each maximum orientation has \(6912\) cycles. The executable prints `SQUARE_RICH_DEBRUIJN_CHECKS_PASSED`. These tests are finite corroboration; Step 1–3 establish the theorem for all \(q\ge2\).

## Relationship to prior work

The construction of de Bruijn sequences via Euler tours and the BEST and directed matrix-tree theorems are classical tools, not new claims. Sawada–Sears–Trautrim–Williams (2023) develop general universal-cycle and de Bruijn construction frameworks. Álvarez and collaborators (2023) investigate extremal factors of de Bruijn-like graphs; Chee and collaborators (2024) study run-length-limited de Bruijn graph sequences. Their inspected principal results do not state the present sharp length-four square bound, freely chosen pair orientations, or equal-size extremal orientation classes. The result concerns nonpalindromic alternating squares \(abab\), not palindromes \(abba\); a palindrome-factor spectrum does not imply these orientation constraints or their enumerator.

## Limitations

No formula is claimed for the distribution of *nonmaximum* numbers of length-four squares for arbitrary alphabet size. No extension to order greater than three or squares of length greater than four is asserted. The determinant \(T_q\) is given as an explicit graph cofactor, not a simplified closed product in \(q\). The literature comparison does not rule out equivalent results in unindexed work or implicit consequences of previously developed local-transition enumeration frameworks. The mathematical result has not undergone independent validation.

## References

1. J. Sawada, J. Sears, A. Trautrim, A. Williams, *Concatenation trees: A framework for efficient universal cycle and de Bruijn sequence constructions* (2023), arXiv:2308.12405, https://arxiv.org/abs/2308.12405.
2. N. Álvarez et al., *On extremal factors of de Bruijn-like graphs* (2023), arXiv:2308.16257, https://arxiv.org/abs/2308.16257.
3. Y. M. Chee et al., *Maximum Length RLL Sequences in de Bruijn Graph* (2024), arXiv:2403.01454, https://arxiv.org/abs/2403.01454.
4. The BEST theorem and directed matrix-tree theorem for Eulerian directed multigraphs (standard classical results).
