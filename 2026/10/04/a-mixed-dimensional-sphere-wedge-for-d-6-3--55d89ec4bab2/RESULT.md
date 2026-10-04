# A mixed-dimensional sphere wedge for \(D_{6,3}\)
## Finding
For the complex \(D_{6,3}\) of simple graphs on six labeled vertices whose domination number is at least \(3\), \(D_{6,3}\simeq \bigvee^{115} S^4 \vee \bigvee^{24} S^5\).

Equivalently, this finite graph complex is a wedge of spheres in two adjacent dimensions, with exactly \(115\) four-spheres and \(24\) five-spheres. It therefore gives an explicit affirmative instance of the mixed-dimensional sphere-wedge phenomenon asked about for complexes of graphs with bounded domination number.

## Assumptions and scope
Let the ground set be the \(15\) edges of the complete graph on the labeled vertex set \(\{1,2,3,4,5,6}\). A nonempty edge set is a simplex of \(D_{6,3}\) exactly when the corresponding simple graph has domination number at least \(3\). Here a dominating set is a vertex subset whose closed neighborhoods cover all six vertices. The claim concerns this one finite complex only; it makes no assertion for other values of \(n\) and \(k\).

The complex has \(4502\) nonempty simplices. By edge-set cardinality \(1,\ldots,7\), their counts are
\[
15,\ 105,\ 455,\ 1185,\ 1647,\ 915,\ 180.
\]
Its Euler characteristic is \(92\).

## Proof
Order the edges of \(K_6\) as
\[
13,12,23,15,45,46,56,14,34,36,16,26,24,35,25.
\]
Starting with all simplices unmatched, process these edges in order. At the stage for an edge \(e\), pair every currently unmatched simplex \(\sigma\) not containing \(e\) with \(\sigma\cup\{e\}\) whenever both are currently unmatched simplices of \(D_{6,3}\). The finite verifier reconstructs the complex from the domination-number definition and checks that this procedure makes \(2181\) disjoint matching pairs.

Reverse the matched cover relations in the Hasse diagram and leave every unmatched cover relation directed downward. The verifier checks all \(21300\) Hasse cover relations and topologically sorts the resulting directed graph, so the matching is acyclic. Its critical simplices consist of exactly one \(0\)-simplex, \(115\) critical \(4\)-simplices, and \(24\) critical \(5\)-simplices. Forman's discrete Morse theorem therefore gives a CW complex homotopy equivalent to \(D_{6,3}\) with exactly those cells.

It remains to identify the attaching maps of the \(5\)-cells. Exact integer algebraic Morse cancellation, using the same matching with the standard increasing-edge orientation, gives the full Morse differential
\[
\partial_5^M:\mathbb Z^{24}\longrightarrow\mathbb Z^{115}
\]
as the zero matrix. The \(4\)-skeleton of the Morse CW complex is therefore \(igvee^{115}S^4\). This space is \(3\)-connected, so the Hurewicz map \(\pi_4	o H_4\) is an isomorphism. For each \(5\)-cell, the Hurewicz image of its attaching map is precisely the corresponding column of \(\partial_5^M\), hence is zero. Every attaching map is therefore null-homotopic, proving
\[
D_{6,3}\simeq igvee^{115}S^4eeigvee^{24}S^5.
\]

## Verification
Run `python3 artifacts/verify.py`. The verifier uses only the Python standard library and reconstructs every simplex from the domination-number definition rather than reading a precomputed face list. It checks downward closure, the exact face counts, matching disjointness, acyclicity on the full modified Hasse diagram, and the integer Morse differential. As an independent chain-level cross-check, it computes the ordinary simplicial boundary ranks over both \(\mathbb F_2\) and \(\mathbb F_3\), obtaining ranks \(14,91,364,821,711,180\) for successive nontrivial boundary maps. The resulting Betti numbers are \(1\) in degree \(0\), \(115\) in degree \(4\), \(24\) in degree \(5\), and zero otherwise. A successful run ends with `D63_MIXED_WEDGE_VERIFY_OK`.

## Relationship to prior work
González and Hoekstra-Mendoza introduced this family and explicitly singled out \(D_{6,3}\): they reported Euler characteristic \(92\), while leaving its homotopy type undetermined, and asked whether some \(D_{n,k}\) is a wedge of spheres of different dimensions. Their paper also supplies the discrete-Morse framework used here. The present calculation determines the full homotopy type of that singled-out complex and answers the mixed-dimensional question affirmatively for it.

A previously recorded computation for this same complex gave only reduced mod-\(2\) homology in dimensions \(4\) and \(5\). That statement is implied by the wedge decomposition above, but it does not imply the wedge decomposition: homology alone does not determine the attaching maps. The zero integral Morse differential together with the Hurewicz argument is the additional step.

## Limitations
The proof is an exhaustive finite certificate for the single complex \(D_{6,3}\); it is not a uniform theorem for the family \(D_{n,k}\). The verifier checks the complete finite matching and its algebraic Morse boundary, but it does not constitute an independent audit. Literature searches can miss very recent, non-indexed, or differently phrased duplicate results.

## References
J. González and T. I. Hoekstra-Mendoza, “On the homotopy type of complexes of graphs with bounded domination number,” arXiv:1901.07130, first public version 2019-01-22; published in *Contributions to Discrete Mathematics*, DOI 10.55016/ojs/cdm.v16i3.72114.

R. Forman, “Morse theory for cell complexes,” *Advances in Mathematics* 134 (1998), 90–145.
