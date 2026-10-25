# The cap complex of the affine plane of order four is a wedge of \(225\) three-spheres

## Finding
Let \(K\) be the abstract simplicial complex whose vertices are the sixteen points of the Desarguesian affine plane \(\operatorname{AG}(2,\mathbb F_4)\) and whose faces are precisely the point sets containing no three collinear points. Then
\[
K\simeq\bigvee^{225}S^3.
\]
In particular, \(\widetilde H_3(K;\mathbb Z)\cong\mathbb Z^{225}\), all other reduced integral homology groups vanish, and \(K\) is \(2\)-connected. The homotopy statement, not the previously tabulated homology, is the contribution.

## Assumptions and scope
The field \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\) has four elements labeled \(0,1,t,t+1\) by integers \(0,1,2,3\). Addition is bitwise exclusive-or. Multiplication is defined by \(t^2=t+1\). The point \((x,y)\) receives index \(4x+y\), for integers \(x,y\in\{0,1,2,3\}\) representing field elements.

The twenty affine lines are the four vertical lines \(x=b\) and the sixteen lines \(y=mx+b\), with \(m,b\in\mathbb F_4\). Three distinct points are collinear if and only if they lie on one of these lines. Thus the forbidden triples form a set of size \(20\binom43=80\), since each pair determines a unique line. A face is a nonempty set of points containing none of those triples; the empty face is included conventionally.

This is a statement about the full cap complex of this particular affine plane, not a classification for larger fields, non-Desarguesian planes, or other general-position complexes. The complex is nonpure: it has \(120\) maximal faces of cardinality four and \(48\) maximal faces of cardinality six.

## Proof
**Finite model.** Represent each nonempty vertex subset by its integer bitmask \(s\in\{1,\ldots,2^{16}-1\}\). A mask is a face if, for every forbidden triple mask \(u\), one has \(s\mathbin{\&}u\ne u\). The complete face enumeration has face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(16,120,480,840,288,48).
\]
There are \(1792\) nonempty faces. A separate determinant test in \(\mathbb F_4\), namely
\[
(x_2-x_1)(y_3-y_1)=(x_3-x_1)(y_2-y_1),
\]
recovers precisely the same eighty forbidden triples. This cross-check prevents a dependence on a pre-entered line list.

**Explicit acyclic matching.** Begin with all \(1792\) nonempty face masks unmatched. For each vertex index \(v=0,1,\ldots,15\), in that order, traverse the remaining masks \(s\) in increasing integer order. Whenever \(v\notin s\) and both \(s\) and \(s\cup\{v\}\) remain unmatched faces, pair them and remove both from the remaining set. The accompanying `MATCHING.csv` lists all \(783\) resulting lower/upper face pairs, in this exact order. Its contents are regenerated from the preceding rule by `verify.py` and compared byte for byte.

Every pair is a cover relation in the face poset, and no face occurs in two pairs. To verify acyclicity, orient every unmatched Hasse cover relation from the larger face to the smaller face, and reverse the matched cover relations. Enumerating every nonempty face and each of its nonempty codimension-one faces gives exactly \(6768\) oriented incidences. A complete Kahn topological sort visits all \(1792\) vertices of the oriented Hasse graph, so no directed cycle exists. These counts and the topological sort are checked from the field model and certificate by the bundled standard-library-only program. This is an exhaustive finite proof, not a sampling test.

**Critical cells and homotopy.** The matching has precisely one unpaired vertex, namely the point of index zero, and \(225\) unpaired simplices of dimension three; it has no other critical simplices. The discrete-Morse CW theorem therefore gives a CW complex homotopy equivalent to \(K\), with one zero-cell and \(225\) three-cells and with no positive-dimensional cells in any other dimension. Every three-cell attaches to the one-point two-skeleton by the unique constant attaching map. The CW complex is consequently the indicated wedge of \(225\) copies of \(S^3\). This establishes the integral homotopy equivalence, not merely homology over a field.

## Verification
Run `python3 verify.py` in a directory containing the exact `MATCHING.csv` supplied alongside this result. The checker uses only the Python standard library. It constructs \(\mathbb F_4\), all twenty lines, all eighty forbidden triples by two methods, every face, the complete matching and all \(6768\) directed face incidences; it tests pair-disjointness, cell dimensions, certificate identity, the absence of directed cycles and the Euler characteristic \(\chi(K)=-224\). A successful run ends with `VERIFY_OK`. The proof uses the actual certificate pairs, not a previously reported homology table.

## Relationship to prior work
Innamorati and Tondini (2013) study the affine plane of order four through blocking sets and the Möbius–Kantor configuration. Crnković, Rodrigues, Rukavina and Tonchev (2016) study maximal arcs in the same affine plane as ingredients of quasi-symmetric designs. Those results concern incidence geometry and block-design constructions rather than the homotopy type of the complex of all caps.

More directly, Alan Lew's *Spectral gaps of generalized flag complexes* (2018), Section 6.2, Figure 6.4, **already records precisely the face vector above and the integral homology \(\widetilde H_3\cong\mathbb Z^{225}\)**, with other reduced homology vanishing. Those numerical assertions are not novel here. Its table and surrounding spectral arguments do not supply a homotopy decomposition or an acyclic matching of the present complex. Integral homology concentrated in dimension three does not by itself determine the homotopy type of a five-dimensional simplicial complex. The present explicit matching makes the stronger classification possible.

The analogous cap complex of the projective plane \(\operatorname{PG}(2,\mathbb F_4)\) is a different complex on twenty-one vertices. Its topology cannot be restricted to an induced sixteen-vertex subcomplex by simply restricting a homotopy equivalence. Likewise, graph-metric Vietoris–Rips complexes of affine-plane incidence graphs use a different face rule and do not imply this claim.

## Limitations
The proof is finite and specific to \(\operatorname{AG}(2,\mathbb F_4)\). It does not establish a formula for cap complexes of all affine planes or determine any natural symmetry action on the \(225\) homology generators. The historical integral homology and face vector are credited explicitly. Searches of indexed results and the inspected primary sources did not identify an earlier statement of the full homotopy type; they do not rule out unindexed or differently named equivalent work. No independent scientific audit has been performed.

## References
1. S. Innamorati and D. Tondini, *The yin-yang structure of the affine plane of order four*, Ars Combinatoria **110** (2013), 193–197; published 2013-07-31. https://combinatorialpress.com/article/ars/Volume%20110/volume-110-paper-19.pdf
2. D. Crnković, B. Rodrigues, S. Rukavina and V. D. Tonchev, *Classification of quasi-symmetric 2-(64,24,46) designs of Blokhuis-Haemers type*, arXiv:1602.05446v1 (2016-02-17). https://arxiv.org/abs/1602.05446
3. A. Lew, *Spectral gaps of generalized flag complexes*, MSc thesis, Technion (2018), Section 6.2 and Figure 6.4. https://www.math.cmu.edu/users/alanlew/files/theses/msc%20thesis.pdf
4. A. Lew, *Spectral gaps of simplicial complexes without large missing faces*, arXiv:1706.00358v1 (2017-06-01). https://arxiv.org/abs/1706.00358
5. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics **134** (1998), 90–145; standard discrete-Morse CW theorem.
