# Exact random legal-move general-position law on direct products of complete graphs

## Finding
Let \(m,n\ge3\) be integers and \(G=K_m\times K_n\), where two different cells \((i,j)\) and \((i',j')\) are adjacent if and only if both coordinates differ. Starting with the empty set, repeatedly select one vertex uniformly from **all currently legal vertices** whose addition preserves general position (no three selected vertices on a shortest path). Stop when no legal vertex remains. This is the uniform-legal-choice process, not random-permutation scanning and not adversarial play.

The terminal set has exactly one of four disjoint structural types: a full row (type R), a full column (type C), a maximum nonattacking rook placement (type M), or all four corners of a \(2\times2\) rectangle (type Q). Set
\[
 a_{m,n}=\frac{n-1}{mn-1},\quad
 b_{m,n}=\frac{m-1}{mn-1},\quad
 c_{m,n}=\frac{(m-1)(n-1)}{mn-1}.
\]
Their **exact terminal probabilities** are
\[
 \begin{aligned}
 p_R&=a_{m,n}\frac{n-2}{n+2m-4},\\
 p_C&=b_{m,n}\frac{m-2}{m+2n-4},\\
 p_M&=c_{m,n}\frac{(m-2)(n-2)}{(m-2)(n-2)+2},\\
 p_Q&=1-p_R-p_C-p_M.
 \end{aligned}
\]
Consequently the terminal-size probability generating polynomial is
\[
 \mathbb E[z^{|S_{\mathrm{final}}|}]
 =p_Rz^n+p_Cz^m+p_Mz^{\min(m,n)}+p_Qz^4.
\]
This identity is valid when several of the four sizes coincide; the four **types** remain disjoint. Within each type, every labeled terminal set has equal probability. There are respectively \(m\), \(n\), \(\binom m{k}\binom n{k}k!\) (where \(k=\min(m,n)\)), and \(\binom m2\binom n2\) labeled terminal sets of the four types.

Two contrasting limiting laws follow. For square products \(m=n=q\ge4\), the probability of a four-corner terminal set is
\[
 p_Q=\frac{4(q-1)}{(q+1)(3q-4)}
 +\frac{2(q-1)}{(q+1)((q-2)^2+2)}
 =\frac{4}{3q}+O(q^{-2}).
\]
All other outcomes have size \(q\). Hence
\[
 q-\mathbb E|S_{\mathrm{final}}|\longrightarrow\frac43,
 \qquad\frac{\operatorname{Var}(|S_{\mathrm{final}}|)}q\longrightarrow\frac43.
\]
For fixed \(m\ge3\) and \(n\to\infty\), the normalized terminal size converges in distribution to a Bernoulli variable with success probability \(1/m\). In particular \(\mathbb E|S_{\mathrm{final}}|/n\to1/m\).

## Assumptions and scope
A vertex subset is in general position if no three of its members occur on a common geodesic. Choices are uniform over the **currently addable vertices** at each step, with fresh randomness; vertices rejected at an earlier stage are never pre-ordered. The first two choices are always legal. Every transition is finite, and maximality follows from stopping only when no legal addition remains. Results cover **every** integer pair \(m,n\ge3\), including the square \((3,3)\), with labeled rows, columns, and vertices. Standard asymptotic \(O(\cdot)\) notation refers to \(q\to\infty\).

## Proof
**Geodesic reduction.** In \(K_m\times K_n\) with \(m,n\ge3\), adjacent cells differ in both coordinates; distinct cells sharing a row or a column have distance two. For same-row cells a common neighbor is obtained by choosing a different row and a column different from both endpoint columns, and symmetrically for same-column cells. Thus the diameter is two. A selected set is in general position precisely when its induced subgraph has no induced three-vertex path; equivalently, it is a disjoint union of cliques. Indeed, the middle of an induced three-vertex path lies on a geodesic of length two, and any forbidden geodesic triple induces such a path.

**Legal third moves.** Fix the first chosen cell. Its second cell belongs either to the same row (\(n-1\) choices), the same column (\(m-1\) choices), or to a different row and column (\((m-1)(n-1)\) choices). Their probabilities are \(a_{m,n},b_{m,n},c_{m,n}\). If the two lie in one row, a legal third cell is either another of the \(n-2\) cells of that row, or one of the \(2(m-1)\) cells outside the row in one of the two already used columns. There are no others: a cell outside the row and in neither selected column would be adjacent to both selected cells, creating an induced three-vertex path. The same argument gives \(m-2\) cells in the original column and \(2(n-1)\) opposite-corner choices in the column case. If the first two cells differ in both coordinates, a legal third cell must either be adjacent to both (\((m-2)(n-2)\) new row-and-column choices) or to neither (the two crossed corners). Adjacency to exactly one would create a forbidden induced path.

**Forced completion.** Three selected cells in a common row can only be extended by further cells of that row, because any cell outside is adjacent to at least two of them. The process therefore selects all remaining row cells and terminates with a full row; the column case is symmetric. Three cells with pairwise distinct rows and columns form a clique. Any additional selected cell must also differ in row and column from every member: a cell adjacent to only some clique members would form an induced path, and a cell nonadjacent to all three is impossible because it can share a row with at most one and a column with at most one. All remaining moves therefore extend the nonattacking placement until it uses all rows or all columns, giving a maximum placement of size \(\min(m,n)\). Any third move in the crossed-corner case gives three corners of one \(2\times2\) rectangle; its missing fourth corner is legal. No other cell can be added, either before or after adding the fourth corner, because it creates an induced three-vertex path. Thus the process finishes with all four corners.

**Probabilities and labels.** Divide the legal-third-move counts by their row, column, or diagonal totals and multiply by the corresponding probabilities of the second-move types. This gives \(p_R,p_C,p_M\), and their complement is \(p_Q\). The terminal cardinality identity follows. The row-and-column relabeling automorphisms act transitively within each of the four families; since every move is uniform among legal additions, the distribution is uniform within each family. The stated family cardinalities are obtained by choosing a row, choosing a column, choosing and bijecting \(k\) distinct rows and columns, or choosing two rows and two columns, respectively.

**Limits.** For \(m=n=q\), insert \(q\) in the four probabilities and simplify the rectangle probability to the displayed expression. For \(q\ge4\), terminal size is \(4\) with probability \(p_Q\) and \(q\) otherwise. Its mean is \(q-(q-4)p_Q\), and variance is \((q-4)^2p_Q(1-p_Q)\). Since \(qp_Q\to4/3\), both limits follow. For fixed \(m\) and growing \(n\), the exact formulas yield \(p_R\to1/m\), \(p_M\to(m-1)/m\), and \(p_C,p_Q\to0\). Because the row outcome has size \(n\), while the other three types have bounded size (at most \(\max\{m,4\}\)), the normalized terminal-size limit is the claimed Bernoulli law; bounded convergence gives the limiting normalized mean.

## Verification
The standalone `verify_random_greedy.py` constructs graph distances by breadth-first search, identifies forbidden geodesic triples without using the classification, and performs exact rational dynamic programming over **all reachable general-position subsets**. It recomputes the full terminal-type probability distribution and compares it with the four formulas on \(3\times3\), \(3\times4\), \(3\times5\), \(4\times4\), \(4\times5\), and \(5\times5\). The output in `verification_output.txt` records \(4{,}442\) distinct states across these six boards. Additional numerical rational evaluations illustrate the two limits but do not prove them. The infinite claim is supported by the symbolic proof above, not by finite testing.

For \(m=n=3\), the exact terminal probabilities for full row, full column, maximum placement, and rectangle are respectively \(1/20,1/20,1/6,11/15\). For \(m=n=5\), they are \(1/22,1/22,6/11,4/11\).

## Relationship to prior work
The 2021 general-position achievement game establishes the legal-move framework for adversarial alternating play, not uniform random play on the direct product. The 2022–2023 avoidance-game work also analyzes adversarial winning strategies. The 2023 lower-general-position study determines the size of smallest maximal general-position sets for \(K_m\times K_n\), and the 2019 study addresses largest cardinalities. The 2024 general-position-polynomial study defines the all-subset enumeration, while the 2026 paper provides the exact direct-product polynomial and classifies its feasible sets. Those **static enumeration results are prior art** and are not claimed here. The present claim concerns the **path-dependent probability law** produced by uniformly selecting a legal next vertex, including its rare-event versus expected-shortfall asymptotics. Knowing how many maximal sets exist does not mean the random process selects them uniformly.

## Limitations
This result does not determine optimal play in an adversarial achievement or avoidance game. It does not describe a random-priority process that scans a fixed random permutation of all vertices: that is a different stochastic model. It does not claim a new all-subset general-position polynomial or a new classification of general-position sets. Historical literature could contain the same stochastic specialization under a different name; no exhaustive historical-uniqueness guarantee is asserted. Independent external scientific audit has not been performed.

## References
1. S. Klavžar, Neethu P. K., and Ullas Chandran S. V., *The general position achievement game played on graphs*, arXiv:2111.07425v1 (2021); Discrete Applied Mathematics 317 (2022), 109–116, DOI 10.1016/j.dam.2022.04.019.
2. Ullas Chandran S. V., S. Klavžar, Neethu P. K., and R. Sampaio, *The general position avoidance game and hardness of general position games*, arXiv:2205.03526 (2022).
3. G. Di Stefano, S. Klavžar, A. Krishnakumar, J. Tuite, and I. G. Yero, *Lower General Position Sets in Graphs*, arXiv:2306.09965v1 (2023), Theorem 5.4.
4. V. Iršič, S. Klavžar, G. Rus, and J. Tuite, *General position polynomials*, arXiv:2401.05696v1 (2024).
5. B. A. Rather, *Explicit Formulas and Unimodality Phenomena for General Position Polynomials*, arXiv:2603.06930v3 (2026), Theorem 5.3.
6. S. Klavžar and I. G. Yero, *The general position problem and strong resolving graphs*, arXiv:1906.00935v1 (2019), Proposition 3.3.
