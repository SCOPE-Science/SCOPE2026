# Labeled \(5\times5\) Latin-square intercalate graph: eight equal components of diameter \(13\)

## Finding
Let \(\mathcal L_5\) be the set of all Latin squares with the rows, columns, and five symbols individually labeled by \(\{0,1,2,3,4\}\). Form the simple undirected graph \(\mathcal T_5\) on \(\mathcal L_5\) by joining two distinct squares if one results from the other by replacing a two-symbol \(2\times2\) Latin subsquare
\[
\begin{pmatrix}a&b\\b&a\end{pmatrix}
\quad\longleftrightarrow\quad
\begin{pmatrix}b&a\\a&b\end{pmatrix}.
\]
Then \(\mathcal T_5\) has exactly \(161{,}280\) vertices. Its components are \(17{,}280\) isolated vertices and **eight mutually isomorphic, vertex-transitive, \(4\)-regular connected components**, each with \(18{,}000\) vertices, \(36{,}000\) edges, and diameter (and radius) \(13\). Every one of the four possible row/column/symbol parity triples occurs in exactly two of the nontrivial components. All isolated vertices are the isotopes of the cyclic group table, and all nonisolated squares form one isotopy class.

## Assumptions and scope
The graph is on **fully labeled squares**, *not* on isotopy classes, main classes, reduced squares, or improper Latin squares. Row and column positions and symbol labels are fixed, and moves change only the four cells of a genuine two-symbol intercalate. Identifying squares under row/column/symbol permutations would destroy the component structure in this statement. For \(p\in S_5\), write \(\operatorname{sgn}(p)\in\{\pm1\}\), and put \(H=A_5^3\le S_5^3\). The group \(S_5^3\) acts on squares by independent row, column, and symbol relabeling:
\[
((\alpha,\beta,\gamma)\cdot L)_{r,c}
 =\gamma\bigl(L_{\alpha^{-1}(r),\beta^{-1}(c)}\bigr).
\]
All calculations and certificates concern exactly order five and do not imply any analogous statement for other orders.

## Proof
**1. Exhaustive universe and two isotopy orbits.** Fix the first row to \((0,1,2,3,4)\). An exhaustive backtracking over the other four row permutations, rejecting symbol repetitions within every column, gives exactly \(1{,}344\) completions. Independently permuting the five symbols gives each fully labeled Latin square uniquely in this way, so \(|\mathcal L_5|=1{,}344\cdot120=161{,}280\). The standalone verifier implements these finite, complete loops; no sample or probabilistic inference is used.

Take the following two explicit square representatives, using indices \(0,\ldots,4\):
\[
C_{r,c}=r+c\pmod5,
\qquad
B=\begin{pmatrix}
0&1&2&3&4\\
1&0&3&4&2\\
2&3&4&0&1\\
3&4&1&2&0\\
4&2&0&1&3
\end{pmatrix}.
\]
Their autotopism groups under \(S_5^3\) have exactly \(100\) and \(12\) elements, respectively. To verify these counts independently of class tables, iterate all \(120^2\) pairs \((\alpha,\beta)\), derive the unique possible \(\gamma\) from the first transformed row, and test all \(25\) cells. The \(12\) autotopisms of \(B\) each have all three permutation signs even. Consequently orbit–stabilizer gives
\[
|S_5^3\cdot C|=\frac{120^3}{100}=17{,}280,
\qquad
|S_5^3\cdot B|=\frac{120^3}{12}=144{,}000.
\]
The first orbit has no intercalates (the difference between two rows in an odd cyclic group cannot consist of transpositions); the second has exactly four in each square, as is checked directly for \(B\). The two orbits are disjoint, and their sizes sum to \(|\mathcal L_5|\), proving they are all the squares. The \(17{,}280\) squares in the first orbit are isolated, while all \(144{,}000\) squares in the second have degree four.

**2. An even-isotopy obstruction.** The four intercalates of \(B\), recorded as \((r_1,r_2,c_1,c_2)\), are
\[
(0,1,0,1),\ (1,2,0,4),\ (1,3,0,2),\ (1,4,0,3).
\]
For each, one direct certificate that switching it stays in \(H\cdot B\) is a triple of permutations \((\alpha,\beta,\gamma)\) with the action above. The permutations are in one-line notation and each is even:

| Intercalate | \(\alpha\) | \(\beta\) | \(\gamma\) |
|---|---|---|---|
| `(0,1,0,1)` | `(1,0,2,4,3)` | `(1,0,2,4,3)` | `(1,0,3,2,4)` |
| `(1,2,0,4)` | `(0,2,1,4,3)` | `(4,2,1,3,0)` | `(4,2,1,3,0)` |
| `(1,3,0,2)` | `(0,3,1,2,4)` | `(2,3,1,4,0)` | `(2,3,1,4,0)` |
| `(1,4,0,3)` | `(0,4,1,3,2)` | `(3,4,1,2,0)` | `(3,4,1,2,0)` |

Direct substitution into the \(25\) cells verifies each equality. A switch is equivariant under any row/column/symbol relabeling; therefore every switch from any square in \(H\cdot B\) stays inside \(H\cdot B\). Since the stabilizer of \(B\) is contained in \(H\),
\[
|H\cdot B|=\frac{60^3}{12}=18{,}000.
\]
Hence no connected component meeting this even-isotopy orbit can escape it. The full noncyclic orbit is the disjoint union of eight such orbits, indexed by the cosets of \(H\) in \(S_5^3\).

**3. Connectivity and exact metric.** Exhaustive breadth-first search starting at \(B\), generating all legal intercalate switches, reaches exactly \(18{,}000\) distinct squares. This equals the complete size of \(H\cdot B\), proving its connectivity; equivariance makes the remaining seven orbits connected and mutually isomorphic. The group \(H\) acts transitively on each component and by graph automorphisms, so every vertex in a component has the same distance-shell counts. The BFS from \(B\) yields, for distances \(0,1,\ldots,13\), respectively,
\[
(1,4,12,36,108,252,612,1284,2256,3624,4812,3828,1112,59).
\]
These integers sum to \(18{,}000\), and the last shell is nonempty, so every nontrivial component has radius and diameter exactly \(13\). The component edge count follows from \(4\)-regularity.

**4. Parity refinement.** The product of the permutation signs of all rows, columns, and symbol-position permutations gives three parity signs. Switching a two-symbol \(2\times2\) intercalate changes exactly two permutations in each family and hence preserves each sign. The standard product constraint leaves exactly four allowed sign triples at order five. A final exhaustive check of all components confirms that each triple labels exactly two size-\(18{,}000\) components; this is strictly finer than the classical four-sector parity obstruction.

## Verification
Run `python3 verify_latin5.py` with the included standalone file. It must print `VERIFY_OK`. The checker (i) constructs the full \(161{,}280\)-square universe without tables, (ii) enumerates the stabilizers of both explicit representatives, (iii) confirms four even-isotopy witnesses, (iv) performs the root BFS and exact shell count, and (v) independently traverses all \(161{,}280\) squares and checks the degree census, components, and parity sectors. The final independent full-census check returns \(17{,}280\) singleton components and eight components of size \(18{,}000\), corroborating the group-based reasoning. The computation is a finite exhaustive proof because each loop's domain is explicitly all candidate permutations/Latin squares or all neighbors, rather than a bounded search for an infinite statement.

## Relationship to prior work
Wanless (2004) defines the intercalate switching graph on **isotopy or main classes**, establishes parity invariants, and notes that order five has two isolated vertices at that quotient level. A single quotient vertex represents all \(144{,}000\) noncyclic fully labeled squares, so the quotient result does not imply the eight labeled components, their sizes, their vertex transitivity, or diameter. Cavenagh and Stones (2011) study near-automorphisms differing in a \(2\times2\) subsquare; that is a local existence/symmetry question, not the all-state labeled metric. Jacobson and Matthews (1996) prove connectivity using a broader class of moves, including steps through improper squares; this does not imply connectivity under **intercalates only**, and in fact the graph here is disconnected. A separate earlier exact result concerns labeled order-four Latin squares; it cannot imply the order-five classification, whose fixed parity structure differs. No accessible source inspected or semantically matched this complete claim; this absence is not a uniqueness guarantee.

## Limitations
The result does not bound mixing times, characterize the eight components by an elementary formula free of a representative, or extend to order six or above. Exact scientific validity depends on the finite exhaustive search steps in the standalone checker and the explicitly stated group action. The accessible full text of the primary 2004 work was inspected; the related 2011 article was available only at the abstract level and remains a residual literature risk. A published statement about the same labeled graph hidden in an unindexed table or thesis cannot be ruled out. No independent audit or independent validation has been performed.

## References
1. I. M. Wanless, *Cycle Switches in Latin Squares*, Graphs and Combinatorics **20** (2004), 545–570, DOI `10.1007/s00373-004-0567-7`, lawful author-hosted full text: `https://users.monash.edu.au/~iwanless/papers/cycleswapgr.GC.pdf`. Relevant discussion: pp. 550–551, 555–557, and 559–560.
2. N. J. Cavenagh and D. S. Stones, *Near-automorphisms of Latin squares*, Journal of Combinatorial Designs **19** (2011), 365–377, DOI `10.1002/jcd.20282`, first publicly dated 2011-03-03 by its publisher.
3. M. T. Jacobson and P. Matthews, *Generating uniformly distributed random latin squares*, Journal of Combinatorial Designs **4** (1996), 405–437, DOI `10.1002/(SICI)1520-6610(1996)4:6<405::AID-JCD3>3.0.CO;2-J`.
4. B. D. McKay, publicly available reduced Latin square data, `https://users.cecs.anu.edu.au/~bdm/data/latin.html` (context only; no table was used for the proof).
