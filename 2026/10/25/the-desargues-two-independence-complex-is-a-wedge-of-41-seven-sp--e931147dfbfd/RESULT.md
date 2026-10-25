# The Desargues two-independence complex is a wedge of 41 seven-spheres

## Finding
Let \(D=\operatorname{GP}(10,3)\) denote the twenty-vertex Desargues graph, and let \(\operatorname{Ind}_2(D)\) consist of all vertex sets whose induced connected components have at most two vertices. Then there is an integral homotopy equivalence
\[
|\operatorname{Ind}_2(D)|\simeq \bigvee^{41}S^7.
\]
In particular, \(\widetilde H_7(\operatorname{Ind}_2(D);\mathbb Z)\cong\mathbb Z^{41}\), and all its other reduced integral homology groups vanish. The statement concerns the second *vertex-independence* complex, not the ordinary independence, edge-matching, or two-matching complex.

## Assumptions and scope
Use vertices \(u_0,\ldots,u_9,v_0,\ldots,v_9\). The thirty unordered edges are exactly \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\), indices modulo ten. The combinatorial orientation of a simplex follows the vertex order \(u_0<\cdots<u_9<v_0<\cdots<v_9\). This graph is isomorphic to the bipartite Kneser graph \(H(5,2)\), and is the Levi graph of the Desargues configuration. No claim is made for other generalized Petersen graphs.

## Proof
**1. Exact complex.** The graph is cubic and triangle-free. A selected vertex subset induces only isolated vertices and edges if and only if every selected vertex has at most one selected neighbor; equivalently it contains none of the sixty distinct three-vertex sets \(\{x,y,z\}\) where \(y,z\) are distinct neighbors of \(x\). Thus the two distinct decision procedures in `verify.py` agree on the mathematical face criterion. Exhaustive enumeration of all \(2^{20}=1{,}048{,}576\) masks produces exactly \(62{,}049\) faces including the empty face. The full dimension-wise face counts are in `verification-output.json`.

**2. Acyclic matching.** Begin with every face unmatched. In vertex order \(u_0,\ldots,u_9,v_0,\ldots,v_9\), at vertex \(w\), match each as-yet-unmatched pair \(\sigma\subset\sigma\cup\{w\}\) when \(w\notin\sigma\), both are faces, and neither has yet been matched. The matching has \(31{,}001\) pairs on the augmented face poset, including \((\varnothing,\{u_0\})\). To verify acyclicity, orient every face-poset cover from its larger face to its smaller face except a matched cover, which is reversed. The supplied checker constructs *every* cover and performs a complete topological sort; all \(62{,}049\) faces are visited. On the ordinary nonempty face poset, delete the empty face and its matching edge. There remain one critical vertex \(u_0\), precisely three critical six-dimensional faces, precisely forty-four critical seven-dimensional faces, and no others. Discrete Morse theory therefore gives a CW complex with exactly these cells and the same homotopy type.

**3. Integral Morse boundary.** Orient each simplex by increasing vertex index. Its face deleting the vertex in position \(j\) has incidence sign \((-1)^j\). The three critical six-faces have integer bit masks \(68436,141906,172618\); all forty-four critical seven-faces are enumerated in `verification-output.json`. For a six-face \(a\), define a projection \(q(a)\) to the free integral group on critical six-faces: \(q(a)=a\) if critical; \(q(a)=0\) when \(a\) is the *upper* member of a lower-dimensional matching pair; and otherwise, if \((a,t)\) is its matching pair with a seven-face \(t\), put
\[
q(a)=-[t:a]\sum_{b\subset t,\;|b|=7,\;b\ne a}[t:b]q(b),
\]
where \([t:a]\in\{\pm1\}\) is the signed simplicial incidence. The acyclic directed Hasse graph guarantees that this recurrence terminates. It is the exact integral algebraic Morse cancellation identity, obtained by solving \(\partial t=0\) for the matched lower face. For each critical seven-face \(c\), the Morse boundary is the column \(q(\partial c)\). The checker records all forty-four exact rows of the resulting \(44\)-by-\(3\) transpose matrix. Its rows numbered \(0,3,14\) in ascending numerical order of the critical seven-face masks have determinant \(-1\). Hence the integer Morse boundary has a unimodular maximal minor, is surjective, and its kernel is free of rank \(44-3=41\).

**4. From integral boundary to homotopy.** With a single critical vertex and no positive cells below dimension six, the Morse CW six-skeleton is \(\bigvee^3 S^6\). The attaching maps for the forty-four seven-cells lie in \(\pi_6(\bigvee^3S^6)\cong\mathbb Z^3\) by the Hurewicz theorem, and are therefore completely determined by the computed degree matrix. An integral unimodular maximal minor allows integral changes of bases (realized by homotopy equivalences and cell slides) that split off three degree-one attachment pairs. The remaining forty-one attaching maps have degree vector zero, hence are null-homotopic. Their cofibers give \(\bigvee^{41} S^7\), as claimed. This establishes the *homotopy type*, not merely Betti numbers or a field calculation.

## Verification
Execute `python3 verify.py > verification-output.json` with Python 3 and no dependencies. The provided output contains `VERIFY_OK`, all forty-four exact Morse-boundary rows, the critical-face masks, the unimodular minor, full face counts, and Hasse-digraph acyclicity evidence. The checker enumerates the complete finite face poset, uses two logically independent face tests, constructs all matched cover arrows, computes a topological order, and recursively evaluates the signed integral Morse projection. No extrapolation from finite samples is involved: the graph has exactly twenty vertices and all vertex subsets are checked. The alternating sum of face counts also independently agrees with the resulting reduced Euler characteristic \(-41\).

## Relationship to prior work
Sawant (2026) defines higher independence complexes and proves vertex decomposability for *trees*, with the two-independence complex also called the three-path-free complex. Deshpande–Singh (2020/2021) compute higher-independence homotopy for complete multipartite, fully whiskered, cycle and certain tree families, while Ghosh–Selvaraja (2025) give shellability criteria for block graphs and related constructions. None of those stated hypotheses includes this cubic girth-six Desargues graph. Published calculations of the **ordinary** Desargues independence complex concern \(\operatorname{Ind}_1(D)\), not \(\operatorname{Ind}_2(D)\); the complexes are distinct and the former's homotopy type does not imply this one. Searches using the equivalent descriptions Desargues, \(\operatorname{GP}(10,3)\), bipartite Kneser \(H(5,2)\), Levi graph, and three-path-free were used to check for coverage. The absence of a matching indexed statement is not a proof of historical priority.

## Limitations
The result is an exact, single-graph homotopy classification rather than a general theorem for a graph family or an equivariant calculation. The finite certificate is a reproducible exact calculation and has not received independent human verification. Unindexed or inaccessible prior results could affect bibliographic priority; no exhaustive priority claim is made.

## References
- R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150v1, first publicly submitted 24 May 2026. https://arxiv.org/abs/2605.25150
- P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448v2 (initial submission 15 Jan 2020). https://arxiv.org/abs/2001.05448
- A. Ghosh and S. Selvaraja, *Shellability of Higher Independence Complexes of Graphs*, arXiv:2505.06614v3 (initial submission 10 May 2025). https://arxiv.org/abs/2505.06614
- E. Weisstein, *Desargues Graph*, MathWorld, https://mathworld.wolfram.com/DesarguesGraph.html
- R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145.
