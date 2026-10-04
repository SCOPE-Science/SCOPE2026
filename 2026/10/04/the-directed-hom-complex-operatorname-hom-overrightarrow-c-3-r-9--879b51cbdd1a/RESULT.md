# The directed Hom complex \(\operatorname{Hom}(\overrightarrow{C}_3,R_9)\) has the homotopy type of a circle

## Finding
Let \(R_9\) be the regular cyclic tournament on \(\mathbb Z/9\mathbb Z\): there is an arc \(i\to j\) exactly when \(1\le (j-i)\bmod 9\le 4\). Let \(\overrightarrow{C}_3\) be the directed three-cycle. Then
\[
\operatorname{Hom}(\overrightarrow{C}_3,R_9)\simeq S^1.
\]
More precisely, its regular-cell vector in dimensions \(0,1,2,3\) is \((90,270,270,90)\), and its face poset admits an acyclic matching with exactly one critical cell in dimension \(0\), one in dimension \(1\), and no other critical cells.

## Assumptions and scope
The directed Hom complex is the regular CW complex of multihomomorphisms: a cell is a triple \((A,B,C)\) of nonempty subsets of \(V(R_9)\) such that every arc in \(A\times B\), \(B\times C\), and \(C\times A\) is present in \(R_9\). Since \(R_9\) is loop-free, the three subsets are automatically pairwise disjoint. Thus every cell can be represented uniquely by assigning each target vertex one of four states: unused, in \(A\), in \(B\), or in \(C\).

The statement is only for the named tournament \(R_9\). It does not assert a formula for all cyclic tournaments or classify directed Hom complexes of tournaments.

## Proof
Enumerating the \(4^9\) possible four-state assignments and applying the multihomomorphism conditions yields exactly \(720\) cells. The numbers by dimension are
\[
f_0=90,\qquad f_1=270,\qquad f_2=270,\qquad f_3=90.
\]

Order the three source coordinates as \(A,B,C\), and the vertices of \(R_9\) as \(0,1,\ldots,8\). Starting with all cells unmatched, process the pairs \((A,0),(A,1),\ldots,(C,8)\) in lexicographic order. At a stage \((X,v)\), pair every still-unmatched cell not containing \(v\) in coordinate \(X\) with the cell obtained by adjoining \(v\) to that coordinate whenever the enlarged cell is valid and still unmatched. This gives \(359\) matched cover pairs.

The only unmatched cells are
\[
(\{0\},\{1\},\{5\})
\quad\text{and}\quad
(\{6\},\{1\},\{2,5\}),
\]
of dimensions \(0\) and \(1\), respectively. Direct every unmatched Hasse cover from the larger cell to the smaller cell and reverse every matched cover. A topological sort visits all \(720\) vertices of this directed Hasse graph, so the matching is acyclic. Forman's discrete Morse theorem therefore replaces the regular CW complex by a homotopy-equivalent CW complex with one \(0\)-cell and one \(1\)-cell and no other cells. Such a CW complex is \(S^1\).

## Verification
The standalone program `verify.py` reconstructs the result from the defining arc relation. It exhausts all \(4^9=262144\) assignments, checks all \(1917\) Hasse covers, constructs the \(359\)-pair matching, and proves acyclicity by topological sorting.

As an independent chain-level check, it builds the cellular boundary matrices over \(\mathbb F_2\). Their ranks in degrees \(1,2,3\) are \((89,180,90)\), giving Betti numbers \((1,1,0,0)\), consistent with the circle and with Euler characteristic \(0\). Running `python3 verify.py` ends with `CYCLIC_R9_HOMC3_VERIFY_OK`.

## Relationship to prior work
Dochtermann and Singh define directed Hom complexes as regular polyhedral complexes of multihomomorphisms and explicitly identify the topology of homomorphism complexes into nontransitive tournaments as an open direction. Their examples include a seven-vertex tournament whose \(\operatorname{Hom}(\overrightarrow{C}_3,-)\) complex is a Möbius strip, but they do not compute the regular cyclic nine-vertex tournament. Their main tournament theorem concerns transitive tournaments, so it does not imply the present result for \(R_9\).

The oriented cycle \(\overrightarrow{C}_3\) is also singled out there as the first natural source graph carrying a free \(\mathbb Z_3\)-action for directed homomorphism obstruction theory. This makes the exact topology for a canonical regular tournament a natural test case rather than an arbitrary finite computation.

## Limitations
This is a single exact finite case, not a family theorem. The computation supplies a complete finite proof for \(R_9\), but it does not determine the equivariant homotopy type of the \(\mathbb Z_3\)-action, nor does it yield a new general obstruction bound. A differently phrased or very recent duplicate outside the checked literature could remain undiscovered.

## References
1. Anton Dochtermann and Anurag Singh, *Homomorphism complexes, reconfiguration, and homotopy for directed graphs*, European Journal of Combinatorics 110 (2023), 103704, DOI 10.1016/j.ejc.2023.103704; first public version arXiv:2108.10948v1, 24 August 2021.
2. Robin Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90-145.
