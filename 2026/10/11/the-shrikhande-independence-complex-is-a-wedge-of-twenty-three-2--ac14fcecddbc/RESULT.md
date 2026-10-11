# The Shrikhande independence complex is a wedge of twenty-three 2-spheres
## Finding
Let \(\mathrm{Sh}\) be the Shrikhande graph in its standard Cayley realization
\[
\mathrm{Sh}=\operatorname{Cay}\!\left(\mathbb Z_4^2,\{\pm(1,0),\pm(0,1),\pm(1,1)\}\right).
\]
Then
\[
\operatorname{Ind}(\mathrm{Sh})\simeq\bigvee^{23}S^2.
\]

## Assumptions and scope
The graph is finite, simple, and uses the displayed undirected connection set in \(\mathbb Z_4^2\). The independence complex contains exactly the vertex subsets with no graph edge. The claim is only about this canonical sixteen-vertex graph; it is not a family theorem for strongly regular graphs.

## Proof
Index \(\mathbb Z_4^2\) lexicographically by \(4a+b\), with \(0\le a,b<4\). Direct enumeration gives \(200\) nonempty independent faces and face vector
\[
(f_0,f_1,f_2,f_3)=(16,72,96,16).
\]
On the nonempty face poset, apply repeated vertex toggles in the order
\[
1,8,2,14,12,7,10,3,6,9,0,13,4,11,15,5.
\]
At a toggle stage, whenever both an unmatched face \(F\) not containing the toggled vertex \(v\) and \(F\cup\{v\}\) remain unmatched, pair them. This produces \(88\) matched Hasse pairs. Exhaustive reconstruction of all \(496\) Hasse covers shows that the Forman orientation obtained by reversing exactly those matched covers is acyclic. The unmatched faces consist of one \(0\)-simplex and exactly \(23\) \(2\)-simplices, with no other critical dimensions.

Forman's discrete Morse theorem therefore gives a CW complex with one \(0\)-cell and twenty-three \(2\)-cells and no positive-dimensional attaching targets below dimension \(2\). Every \(2\)-cell attaches to the single \(0\)-cell, so the CW complex is \(\bigvee^{23}S^2\), proving the claim.

## Verification
The bundled `verify.py` independently reconstructs the Cayley graph, confirms \(48\) edges, degree \(6\), and strongly regular parameters \((16,6,2,2)\); enumerates every independent face; rebuilds every Hasse cover; reconstructs the \(88\) matching pairs; and topologically sorts the full Morse-oriented Hasse graph to certify acyclicity. As a separate chain-level check it computes mod-2 homology from the entire simplicial boundary complex: the boundary ranks are \((15,57,16)\), giving ordinary Betti vector \((1,0,23,0)\). Running `python3 verify.py` ends with `VERIFY_OK`.

## Relationship to prior work
Matsushita and Wakatsuki study exact homotopy types of independence complexes and emphasize that such types can be difficult to determine even for simply described graphs; their paper treats square-grid families and not the Shrikhande graph. The Shrikhande graph is the exceptional strongly regular graph with parameters \((16,6,2,2)\), sharing those parameters with the \(4\times4\) rook graph. Targeted searches for the graph name, its Cayley realization, its strongly regular parameters, its complementary Latin-square formulation, and clique-complex aliases did not locate this exact homotopy statement. The 2026 monograph devoted to the Shrikhande graph was also checked through its public contents, index, and relevant chapter summaries; those materials document the graph and its structural properties but did not surface an independence-complex computation.

## Limitations
The result is an exact finite computation for one canonical graph. The proof does not classify independence complexes of strongly regular graphs, and the originality assessment cannot exclude an unindexed or differently named computation. The recent Shrikhande monograph was not available here as fully searchable full text, so an equivalent result hidden in inaccessible material remains a residual literature risk.

## References
1. T. Matsushita and S. Wakatsuki, “Independence complexes of \((n\times6)\)-grid graphs,” arXiv:2207.10363, first public 2022-07-21; 2020 MSC 55P10, 05C69.
2. P. J. Cameron, A. Lakshmanan S., and A. Vijayakumar, *The Shrikhande Graph: A Window on Discrete Mathematics*, Cambridge University Press, 2026, DOI 10.1017/9781009709118.
3. A. E. Brouwer, “Shrikhande graph,” distance-regular/strongly-regular graph tables; standard parameters and complementary Latin-square description.
