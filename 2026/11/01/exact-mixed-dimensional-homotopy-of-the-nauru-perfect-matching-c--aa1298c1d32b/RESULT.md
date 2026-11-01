# Exact mixed-dimensional homotopy of the Nauru perfect-matching complex

## Finding

Let \(N=\operatorname{GP}(12,5)\) be the Nauru graph. Its perfect-matching complex \(\mathcal P(N)\) has facets precisely the sets of twelve edges forming perfect matchings of \(N\). The complete **integral homotopy type** is

\[
\mathcal P(N)\simeq\bigvee^{6}S^3\vee\bigvee^{32}S^4.
\]

In particular, the reduced integral homology is \(\mathbb Z^6\) in degree \(3\), \(\mathbb Z^{32}\) in degree \(4\), and zero in every other degree. The computation establishes an actual homotopy equivalence, rather than an inference from Betti numbers.

## Assumptions and scope

The graph has vertices \(u_i,v_i\) for \(i\in\mathbb Z/12\mathbb Z\), and exactly the undirected edges
\[
\{u_i,u_{i+1}\},\qquad\{u_i,v_i\},\qquad\{v_i,v_{i+5}\}
\quad(i\in\mathbb Z/12\mathbb Z).
\]
The labels in the executable are \(u_i=i\) and \(v_i=12+i\), with graph edges sorted lexicographically and indexed starting at zero. Thus \(N\) has \(24\) vertices and \(36\) edges. A face of \(\mathcal P(N)\) is an edge subset contained in at least one perfect matching. All computations are finite and exact; no claim is made for other generalized Petersen graphs.

## Proof

**1. Exhaustive face generation.** Let \(E\) be the sorted list of the \(36\) graph edges. Recursive elimination of the least-indexed still-uncovered graph vertex lists every perfect matching exactly once: choose one incident edge and repeat on the other uncovered vertices. The recursion stops only when all \(24\) graph vertices have been covered. This gives exactly \(120\) twelve-edge perfect matchings. A second recursion selecting the greatest-indexed uncovered vertex produces the same set. Their complete downward closure contains \(346{,}822\) simplices including the empty face; the vector of face counts by dimension \(-1,0,\ldots,11\) is

\[
(1,36,558,4692,21861,55872,85680,85176,57258,26208,7920,1440,120).
\]

**2. Explicit acyclic discrete-Morse matching.** On the set of all faces (including the empty face) perform successive element toggles at edge indices \(0,1,\ldots,35\). In stage \(j\), pair every remaining face \(\sigma\) not containing \(j\) with \(\sigma\cup\{j\}\) when both remain, and delete both from the remaining set. Every pair is a face/coface incidence. The resulting matching has \(173{,}357\) pairs. It leaves exactly \(108\) unmatched faces: \(22\) of dimension \(3\), \(67\) of dimension \(4\), and \(19\) of dimension \(5\). There are no other critical nonempty faces. The empty face is paired, giving the usual one base zero-cell in the reduced CW model.

The element-pairing theorem for simplicial complexes proves acyclicity of successive toggles. Independently, reverse each matched incidence in the directed Hasse graph, orient every other incidence downwards, and run a complete topological sort: every one of the \(346{,}822\) vertices is visited, over \(2{,}282{,}760\) directed incidences. Forman's discrete Morse theorem therefore supplies a CW model with one zero-cell and the positive-dimensional cell counts above, and no one- or two-cells. This CW model is \(2\)-connected.

**3. Exact integral attaching degrees.** Orient each simplicial face by increasing edge index. The signed simplicial incidence obtained by deleting the \(t\)-th indexed edge is \((-1)^t\). For every upper-matched \((k-1)\)-simplex \(\sigma\), with paired \(k\)-simplex \(\tau\), repeatedly eliminate \(\sigma\) using the coefficient \(\pm1\) of \(\sigma\) in \(\partial\tau\). Sum the resulting signed gradient-path coefficients to critical \((k-1)\)-simplices. A critical target maps to its basis vector; a target matched downward is zero. This recursive, terminating rule produces the integral Morse cellular boundaries \(A=\partial_4\) of size \(22\times67\) and \(B=\partial_5\) of size \(67\times19\). The standalone artifact `certificate.json` records every matrix entry, critical-face label and perfect matching, while `verify.py` reconstructs every entry rather than trusting the record.

Exact rational row elimination gives \(\operatorname{rank}A=16\) and \(\operatorname{rank}B=19\). For \(A\), the \(16\) row indices

`[0,1,2,3,4,5,6,7,8,9,11,13,14,16,19,21]`

and the \(16\) column indices

`[0,1,2,3,7,8,10,14,16,18,30,39,45,51,54,55]`

select a determinant \(+1\) minor. For \(B\), row indices

`[2,3,4,5,7,8,10,14,15,16,17,22,30,32,35,39,43,46,48]`

and all \(19\) columns select a determinant \(-1\) minor. Both determinants are recomputed by exact fraction-free integer elimination. The entire product \(AB\) is also checked to vanish entry by entry. Thus the Smith invariant factors consist exclusively of units, with \(16\) for \(A\) and \(19\) for \(B\). The resulting reduced integral homology ranks are \(22-16=6\) in degree three, \(67-16-19=32\) in degree four, and \(19-19=0\) in degree five, without torsion.

**4. Upgrade from homology to homotopy.** The CW three-skeleton is \(\bigvee^{22}S^3\). Its \(67\) four-cell attaching maps lie in \(\pi_3(\bigvee^{22}S^3)\cong\mathbb Z^{22}\), where they are completely determined by their integral degrees. By the unit Smith factors of \(A\), integral basis changes on the three- and four-cells reduce these maps to \(16\) standard degree-one inclusions plus \(51\) zero maps. The four-skeleton is therefore homotopy equivalent to \(\bigvee^{6}S^3\vee\bigvee^{51}S^4\).

The \(19\) five-cell attaching maps now belong to
\[
\pi_4\left(\bigvee^{6}S^3\vee\bigvee^{51}S^4\right)
\cong(\mathbb Z/2)^6\oplus\mathbb Z^{51}.
\]
Here there are no lower-dimensional mixed Whitehead terms because the first products of two three-sphere inclusions occur in dimension five. The \(\mathbb Z^{51}\) coordinates of these attaching maps form the induced boundary \(B\) in the integral kernel of \(A\). Since \(B\) has \(19\) unit invariant factors, basis changes make these free coordinates the first \(19\) coordinate inclusions. Any remaining \((\mathbb Z/2)^6\) components can be absorbed by a homotopy self-equivalence of \(\bigvee^{6}S^3\vee\bigvee^{51}S^4\) which sends each corresponding four-sphere inclusion to that inclusion plus its prescribed map into the three-spheres; the map is a simply connected homology equivalence, hence a homotopy equivalence. The \(19\) five-cells consequently cancel \(19\) four-spheres. The remaining CW model is precisely \(\bigvee^{6}S^3\vee\bigvee^{32}S^4\), proving the result.

## Verification

Run `python3 verify.py` with `certificate.json` in the same directory; no third-party Python packages are required. The verifier constructs the graph, enumerates perfect matchings independently in two vertex orders, generates all faces, performs and topologically sorts the full acyclic matching, rebuilds the two signed integer Morse boundaries, checks every entry against the certificate, computes exact rational ranks and the specified unit minors, and verifies their zero composite.

As a separate mod-two check, repeating the toggle procedure in *reverse* edge order leaves \(11\) critical three-cells, \(55\) four-cells and \(18\) five-cells. Its mod-two boundary ranks are \(5\) and \(18\), independently recovering reduced Betti ranks \(6\) and \(32\). The recorded successful execution is `CHECK_LOG.txt`. Euler characteristic independently agrees: the reduced Euler characteristic is \(26=-6+32\). The full matrix data are required for replay; the recorded log alone is not a proof.

## Relationship to prior work

The motivating definition and a discrete-Morse strategy are developed by Bayer, Jelić Milutinović and Vega (arXiv:2209.02803v1, publicly posted 2022-09-06). Their theorems concern finite planar honeycomb patches, notably \(H_{1\times m\times n}\) and \(H_{2\times2\times2}\), and do not treat the Nauru graph, which is a distinct toroidal hexagonal graph. Chandrakar and Singh (arXiv:2407.05809) treat polygonal line tilings and two-row rectangular grids; neither class covers this closed symmetric cubic graph. A later preprint by Agarwal and Basak (arXiv:2608.30601) treats Möbius ladders and circular ladders, not \(\operatorname{GP}(12,5)\). The Nauru graph's independence complex and other cubic graphs' matching complexes are different simplicial constructions and do not imply this perfect-matching homotopy calculation.

## Limitations

This is a finite, graph-specific classification. It does not prove an all-parameter generalized Petersen theorem, does not determine the natural automorphism representation, and does not compute the map induced by inclusion into the ordinary matching complex. Search results and inspected sources cannot rule out every unindexed equivalent computation. The proof depends on the exhaustive explicit finite certificate and on standard discrete-Morse and CW homotopy facts; its reproducibility is supported by the included executable and full data, not by an external audit.

## References

1. M. Bayer, M. Jelić Milutinović and J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803v1 (first submitted 2022-09-06), https://arxiv.org/abs/2209.02803.
2. H. Chandrakar and A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809, https://arxiv.org/abs/2407.05809.
3. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601, https://arxiv.org/abs/2608.30601.
4. Wolfram MathWorld, *Nauru Graph*, https://mathworld.wolfram.com/NauruGraph.html (standard identification of the graph as \(\operatorname{GP}(12,5)\)).
5. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics **134** (1998), 90–145.
