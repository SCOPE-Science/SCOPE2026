# Exact game chromatic number of \(M_2(C_5)\)
## Finding
For the two-layer generalized Mycielski graph \(M_2(C_5)\),
\[
\chi_g(M_2(C_5))=4.
\]
Thus the first cyclic instance in the regime \(k\ge 2\), \(n\ge 5\) attains the lower endpoint of the presently published interval \(4\le \chi_g(M_k(C_n))\le 5\).

## Assumptions and scope
All graphs are finite and simple. In the coloring game with a palette of \(q\) colors, Alice and Bob alternately choose an uncolored vertex and assign it a color not present on a neighbor; Alice moves first. Alice wins if all vertices are eventually colored. Bob wins as soon as some uncolored vertex has neighbors in all \(q\) colors, because that vertex can never subsequently be colored.

Write the vertices of \(M_2(C_5)\) as \(v_i^j\), where \(i\in\mathbb Z/5\mathbb Z\) and \(j\in\{0,1,2}\), together with the root \(\omega\). The edges are the five base-cycle edges \(v_i^0v_{i+1}^0\); for \(j\in\{0,1}\), both cross-layer edges \(v_i^jv_{i+1}^{j+1}\) and \(v_{i+1}^jv_i^{j+1}\) for each base edge; and the five edges \(\omega v_i^2\). Hence the graph has \(16\) vertices and \(30\) edges.

## Proof
The published lower bound for generalized Mycielski cycles already gives \(\chi_g(M_2(C_5))\ge 4\). The included checker also verifies this case directly: with three colors, exhaustive minimax from the empty position returns a Bob win.

For the upper bound, the checker evaluates the exact finite game with four colors. A state records one value in \(\{0,1,2,3,4}\) for each of the \(16\) vertices, with zero meaning uncolored. At an Alice state it accepts the position exactly when at least one legal move leads to an accepting child; at a Bob state it accepts exactly when every legal move leads to an accepting child. A completed coloring is accepting, and any position containing an uncolored vertex whose neighborhood already displays all four colors is rejecting. These recurrences are precisely the game quantifiers, so their value at the empty state is the existence or nonexistence of a winning Alice strategy.

The only state identifications are exact symmetries. The ten dihedral automorphisms of \(C_5\) act simultaneously on all three layers and fix \(\omega\); the checker first verifies that each preserves adjacency. Global color permutations are also game automorphisms, so colors are canonically relabeled by first occurrence. Memoization after this canonicalization changes only representation, not the recurrence. The four-color computation returns an Alice win after evaluating \(3,734,489\) canonical states. Therefore \(\chi_g(M_2(C_5))\le4\), and together with the lower bound this proves equality.

## Verification
Compile `artifacts/verify_game.cpp` with a C++17 compiler and optimization enabled, then run the resulting executable. The checker reconstructs \(M_2(C_5)\), verifies that it has \(30\) edges and that all ten symmetry maps used in canonicalization preserve adjacency, and solves the complete game for both \(q=3\) and \(q=4\). The recorded run evaluated \(241\) canonical states for three colors and \(3,734,489\) for four colors, returning respectively `Alice_win=0` and `Alice_win=1`, followed by `ALL CHECKS PASSED`.

The computation is exhaustive rather than experimental: no depth cutoff, random sampling, heuristic pruning, or timeout result is used in the certificate. Move ordering affects only speed. The analytical conclusion depends on the exact minimax recurrence and the verified symmetry quotient.

## Relationship to prior work
Mou, Sun, and Zhang introduced the relevant generalized-Mycielski path-and-cycle analysis in 2026. Their cycle theorem gives \(4\le\chi_g(M_k(C_n))\le5\) for \(k\ge2\) and \(n\ge5\), while their exact two-layer results concern \(M_2(P_5)\) and \(M_2(P_6)\). Their discussion of earlier work records exact game-chromatic values for the classical one-layer Mycielski graphs of cycles; that is a different graph family and does not imply the present two-layer equality. The same paper explicitly notes that strategies for the one-layer construction do not transfer directly to the generalized setting.

Searches for the exact graph name, the parameter pair \((k,n)=(2,5)\), and equivalent descriptions of the generalized Mycielski cycle found no source stating this equality. The strongest directly relevant source inspected remains the 2026 paper above, whose theorem leaves precisely a two-value interval for this instance.

## Limitations
This is a computer-assisted exact result for one graph. It does not determine \(\chi_g(M_2(C_n))\) for \(n\ge6\), nor any new infinite family with \(k\ge3\). The proof relies on exhaustive minimax rather than a short human-readable strategy. The included source makes the state recurrence and all quotient symmetries explicit so the finite certificate can be regenerated independently.

## References
1. Y. Mou, Q. Sun, C. Zhang, *The game chromatic number of generalized Mycielski graphs of paths and cycles*, arXiv:2609.02283v1, 2026.
2. H. L. Bodlaender, *On the complexity of some coloring games*, International Journal of Foundations of Computer Science 2 (1991), 133–147.
3. R. Alagammai, V. Vijayalakshmi, *Game chromatic number and game chromatic index of the Mycielski graphs of some families of graphs*, Applied Mathematics & Information Sciences 13(S1) (2019), 261–265.
