# A 736-collapse three-sphere core for the 24-cell Vietoris–Rips complex

## Finding
Let \(R\subset\mathbb R^4\) be the twenty-four standard type-\(D_4\) roots, and let \(K=\operatorname{VR}_{\le 2}(R)\) be the **inclusive** Vietoris–Rips complex in the ordinary Euclidean metric. There is an explicit sequence of exactly **736 elementary simplicial collapses** from \(K\) to a pure three-dimensional subcomplex \(L\) with ten vertices, thirty-three edges, forty-six triangles, and twenty-three tetrahedra. The complex \(L\) is a combinatorial three-sphere: deleting its vertex indexed \(2\) leaves a shellable three-ball with fifteen tetrahedra, whose boundary is the octahedral two-sphere that is the link of that vertex. Hence

\[
K\searrow L\cong_{\mathrm{PL}} S^3,
\qquad K\simeq S^3.
\]

The explicit simple-homotopy reduction and its small PL sphere model, **not** the previously tabulated integral Betti numbers of the 24-cell filtration, are the claim here.

## Assumptions and scope
Write \(e_1,e_2,e_3,e_4\) for the standard orthonormal basis of \(\mathbb R^4\) and take
\[
R=\{\epsilon_i e_i+\epsilon_j e_j:1\le i<j\le4,\ \epsilon_i,\epsilon_j\in\{-1,1\}\}.
\]
The vertices are indexed \(0,\ldots,23\) by lexicographically sorting their integer coordinate quadruples. The complex \(K\) contains precisely the nonempty finite subsets \(\sigma\subseteq R\) satisfying \(\|u-v\|_2\le2\) for all \(u,v\in\sigma\). The theorem concerns this fixed Euclidean metric, not the shortest-path metric of the one-skeleton. An elementary collapse removes a face \(\sigma\) and its unique codimension-one coface \(\tau\), with \(\sigma\) free in the current complex.

## Proof
**1. Complete finite face enumeration.** Distinct unordered pairs of roots have squared distances \(2,4,6,8\), occurring respectively \(96,72,96,12\) times. Therefore the nonempty simplices of \(K\) are exactly the cliques of the graph with edges at squared distances \(2\) or \(4\). Exact backtracking enumeration gives its face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(24,168,480,600,288,24),
\]
with 1,584 nonempty faces. `verify_d4_rips.py` rebuilds all twenty-four vertices and the full face set without reading an external geometry library.

**2. Simple-homotopy certificate.** The `first_collapses` array of `collapse_certificate.json` contains 736 ordered pairs of vertex-index arrays \((\sigma,\tau)\). Starting with all 1,584 faces, remove each pair in the displayed order. At every step the verifier establishes that both faces remain present, \(\sigma\) has codimension one in \(\tau\), and \(\tau\) is the only remaining codimension-one coface of \(\sigma\). A face contained in a still-higher-dimensional simplex would possess at least two codimension-one cofaces, so this also checks freeness against all higher cofaces. The remaining face set is a subcomplex and has face vector
\[
(10,33,46,23).
\]
Its exact twenty-three maximal tetrahedra are listed in `remaining_tetrahedra`, and independently recomputed by the verifier.

**3. A small sphere model.** Let \(v\) be root index \(2\), whose coordinates are \((-1,0,0,-1)\). The link \(\operatorname{lk}_L(v)\) has six vertices indexed \(3,6,9,14,17,20\), twelve edges, and eight triangles. Its only missing edges among the six vertices are \(\{3,20\}\), \(\{6,17\}\), and \(\{9,14\}\), and every compatible triple is a face. Thus it is the join of three two-point sets, the octahedral boundary \(S^2\).

The deletion \(D=L\setminus v\) has 85 nonempty faces and exactly fifteen maximal tetrahedra. The `deletion_tetra_shelling` array supplies a shelling: the first tetrahedron is a ball, and each successive tetrahedron intersects the preceding union precisely in a nonempty proper union of one, two, or three boundary triangles (and their subfaces). These intersections are two-disks, so the union remains a PL three-ball at each step. The verifier also checks that every face of \(D\) is covered by the shelling, that its boundary triangles are exactly those of \(\operatorname{lk}_L(v)\), and separately replays 42 elementary collapses of \(D\) to one vertex. Therefore \(L=D\cup(v*\operatorname{lk}_L(v))\) glues two PL three-balls along their common complete two-sphere boundary, so \(L\) is a PL three-sphere.

By step 2, \(K\) simplicially collapses onto \(L\), proving the stated result, including the stronger simple-homotopy assertion.

## Verification
Place `verify_d4_rips.py` and `collapse_certificate.json` in one directory and run `python3 verify_d4_rips.py`. It uses only the Python standard library. The expected terminal marker is `VERIFY_OK`; the accompanying `verification_output.txt` records the actual successful execution. In particular, the verifier does not merely trust an enumeration log: it reconstructs the vertex set, verifies every one of the 736 free-face pairs against the live simplicial complex, checks the pure three-dimensional residual model, validates the shelling and its boundary, and replays the separate 42-pair deletion collapse.

As a consistency check, at squared threshold \(2\) the Rips complex has \((24,96,96)\) faces in dimensions zero through two: it is the two-skeleton of the 24-cell boundary and has homotopy type \(\bigvee^{23}S^2\). At squared threshold \(6\), exactly twelve antipodal root pairs remain forbidden, so the complex is the boundary of the twelve-dimensional crosspolytope, \(S^{11}\). At squared threshold \(8\) all vertices span one simplex. These observations delimit the finite metric construction; their homology and resulting barcodes are established in earlier literature and are not claimed as discoveries here.

## Relationship to prior work
Dechant's 2013 preprint gives a geometric and root-system construction of the regular 24-cell. The 2023 dissertation of Saleh, especially its Section 4.2, **already tabulates** the integral homology \(H_3\cong\mathbb Z\) of the 24-cell Rips complex at the second distance level, together with the other nonzero homology levels, and lists the 4-polytope homotopy classification among further research questions. These homology computations cannot alone establish the specific simple collapse or certify a PL sphere model. The 2023 paper by Saleh, Titz Mite and Witzel establishes the Rips homotopy types of the five three-dimensional Platonic solids; its introduction remarks that the four-dimensional regular polytopes except the 120-cell should be easy to analyze, but it supplies no 24-cell simple-collapse theorem or certificate. The precise publication priority of the explicit collapse is not established by an index search; the cited remark is a residual risk, not a claim of absence from all literature.

## Limitations
The theorem does not claim that 736 is a minimum number of collapses or that ten is the fewest vertices possible in a residual simplicial sphere. The collapse is not equivariant under the full automorphism group. No new Betti numbers or persistence barcodes are claimed. The argument applies to the exact standard Euclidean 24-cell vertex configuration at inclusive radius \(2\). No independent external mathematical audit has been performed.

## References
1. P.-P. Dechant, *Platonic solids generate their four-dimensional analogues*, arXiv:1307.6768v1, first posted 2013-07-25, https://arxiv.org/abs/1307.6768.
2. N. Saleh, *On Vietoris–Rips Complexes of the 2-Sphere*, dissertation, September 2023, Section 4.2 and subsequent open questions, https://jlupub.ub.uni-giessen.de/items/0a69b981-1372-4ab7-9e75-03b44faa5f67.
3. N. Saleh, T. Titz Mite, S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388v1, 2023, https://arxiv.org/abs/2302.14388.
