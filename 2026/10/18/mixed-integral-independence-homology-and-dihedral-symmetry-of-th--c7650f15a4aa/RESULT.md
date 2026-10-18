# Mixed integral independence homology and dihedral symmetry of the coronene graph

## Finding
Let \(G\) be the finite, planar, seven-hexagon benzenoid graph consisting of a central hexagon and its six edge-adjacent hexagons (the twenty-four-vertex coronene carbon graph). Let \(K=\operatorname{Ind}(G)\) be its ordinary simplicial independence complex. Its only nonzero reduced integral homology groups are
\[
\widetilde H_j(K;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&j=5,\\
\mathbb Z^2,&j=7,\\
0,&j\ne5,7.
\end{cases}
\]
Under the natural dihedral action \(D_6=\langle r,t\mid r^6=t^2=1,\;trt=r^{-1}\rangle\), where \(r\) rotates the patch counterclockwise by sixty degrees and \(t\) reflects it in the horizontal axis, its complete reduced rational homology representation is
\[
\widetilde H_5(K;\mathbb Q)\cong \chi,
\qquad \chi(r)=-1,\quad\chi(t)=1,
\]
\[
\widetilde H_7(K;\mathbb Q)\cong \operatorname{Infl}_{D_3}^{D_6}(V_{\mathrm{std}}),
\]
where the quotient \(D_6\twoheadrightarrow D_3\) has kernel \(\langle r^3\rangle\), and \(V_{\mathrm{std}}\) is the two-dimensional reflection representation of \(D_3\). Equivalently, for \(0\le a<6\), the characters in degrees five and seven are
\[
(\chi_5(r^a),\chi_5(r^at))=((-1)^a,(-1)^a),
\]
\[
\chi_7(r^a)=\begin{cases}2,&3\mid a,\\-1,&3\nmid a,\end{cases}
\qquad\chi_7(r^at)=0.
\]
For every subgroup \(H\le D_6\), this also classifies the rational homology of the geometric quotient \(|K|/H\). With \(\pi:D_6\twoheadrightarrow D_3\) as above, the only possibly nonzero reduced rational Betti numbers are
\[
\widetilde\beta_5(|K|/H)=\begin{cases}1,&H\le\ker\chi,\\0,&\text{otherwise},\end{cases}
\]
\[
\widetilde\beta_7(|K|/H)=
\begin{cases}
2,&|\pi(H)|=1,\\
1,&|\pi(H)|=2,\\
0,&|\pi(H)|\ge3.
\end{cases}
\]
In particular, \(|K|/D_6\) and \(|K|/\langle r\rangle\) are rationally acyclic. No integral homotopy-type splitting or quotient integral-homology claim is made.

## Assumptions and scope
Use integer-coordinate pairs \((X,Y)\) representing Euclidean points \((X/2,\sqrt3Y/2)\). The seven face centers are indexed by the axial pairs
\[
(0,0),(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1).
\]
At center \((q,s)\), take the six vertices \((3q,q+2s)+(2,0),(3q,q+2s)+(1,1),(3q,q+2s)+(-1,1),(3q,q+2s)+(-2,0),(3q,q+2s)+(-1,-1),(3q,q+2s)+(1,-1)\), with cyclic boundary edges. Identify coincident vertices and edges between adjacent hexagons. The resulting graph has twenty-four vertices, thirty edges and seven bounded hexagonal faces; twelve vertices have degree two and twelve have degree three. It is thereby specified without relying on a drawing or chemical convention.

An independent face of \(K\) is a subset of vertices containing no edge of \(G\). The group generators act on integer coordinates by
\[
r(X,Y)=\left(\frac{X-3Y}{2},\frac{X+Y}{2}\right),\qquad t(X,Y)=(X,-Y).
\]
Both preserve the vertex and edge sets and satisfy the stated dihedral relations. Reduced homology is ordinary reduced simplicial homology. The quotient formula concerns the geometric orbit space and coefficients in \(\mathbb Q\), not the simplicial complex of fixed vertices.

## Proof
**Exact finite Morse reduction.** The accompanying Python program `verify_coronene.py`, which has no nonstandard dependencies, builds the explicit graph and enumerates *all* independent subsets using the increasing-vertex backtracking recurrence. It obtains exactly \(62{,}506\) nonempty faces, with face counts in dimensions zero through eleven
\[
(24,246,1412,5001,11358,16663,15540,8853,2876,489,42,2).
\]
For each of the twenty-four vertices, in the stored coordinate order, it pairs every as-yet-unmatched face \(S\) not containing that vertex with \(S\cup\{v\}\) when both faces are as-yet-unmatched. The resulting matching has \(31{,}251\) pairs and exactly four critical cells, one in dimension zero, one in dimension five and two in dimension seven. The program constructs the **entire** face-poset Hasse graph, consisting of \(392{,}364\) cover relations, reverses the matched arrows, and verifies by Kahn's topological ordering algorithm that every one of its \(62{,}506\) nodes is removed. Thus there is no directed cycle, so this is an acyclic discrete-Morse matching, not a heuristic or finite sampling of faces.

By the discrete-Morse CW theorem, \(|K|\) is homotopy equivalent to a CW complex having precisely these four cells. There are no critical cells in dimensions four or six, hence the reduced cellular boundaries in dimensions five and seven vanish, proving exactly the asserted *integral homology groups*. The possible attaching classes of the seven-cells in \(\pi_6(S^5)\) have not been evaluated; therefore an integral wedge-of-spheres homotopy equivalence is neither needed nor asserted.

**Exact Lefschetz traces.** For a simplicial automorphism \(g\), the reduced Lefschetz number is evaluated directly from every setwise-fixed simplex:
\[
\widetilde L(g)=-1+\sum_{\substack{\varnothing\ne S\in K\\gS=S}}
(-1)^{|S|-1}\operatorname{sgn}(g\vert_S).
\]
The sign is the parity of the induced permutation in the globally sorted vertex ordering. The standalone program obtains, in the order \(a=0,1,\ldots,5\),
\[
(\widetilde L(r^a))=(-3,2,0,-1,0,2),\qquad
(\widetilde L(r^at))=(-1,1,-1,1,-1,1).
\]
The reduced simplicial Hopf trace identity and the Morse homology calculation give
\[
\widetilde L(g)=-\chi_5(g)-\chi_7(g).
\]
The one-dimensional integral fifth-homology group gives a sign character. At \(r\), if its trace were \(+1\), the trace on the two-dimensional seventh-homology group would be \(-3\), impossible for an operator of finite order. Therefore \(\chi_5(r)=-1\) and \(\chi_7(r)=-1\). A two-dimensional rational representation of a cyclic order-six rotation with trace \(-1\) has eigenvalues the nontrivial cube roots of unity. Consequently \(r^3\) acts trivially in degree seven. The relation \(trt=r^{-1}\) forces \(t\) to exchange those eigenspaces and have degree-seven trace zero. The value \(\widetilde L(t)=-1\) then gives \(\chi_5(t)=+1\). These determine the two displayed rational representations and reproduce all twelve independently computed Lefschetz numbers.

**Subgroup quotients.** For a finite group of simplicial automorphisms, barycentric subdivision and rational averaging identify \(H_*(|K|/H;\mathbb Q)\) with \(H_*(|K|;\mathbb Q)^H\). The invariant dimension of the sign line is one precisely when \(H\le\ker\chi\). The inflated standard representation of \(D_3\) has invariant dimension two for the trivial image, one for a reflection image of order two, and zero for every image containing a nontrivial rotation (including all images of order at least three). This proves the quotient formulas for **all** subgroups. The program also independently enumerates all sixteen subgroups of \(D_6\) and checks the character averages against these formulas.

## Verification
Run `python3 verify_coronene.py` with Python 3 standard library in the directory containing the file. The script reconstructs the graph, all simplices, every matching pair, every cover relation and all twelve graph automorphisms, and asserts the exact signed character values and quotient dimensions. It emits `VERIFICATION OK` only after all assertions pass. The file `verification_output.txt` records the actual execution output. The directed topological order is recorded by a SHA-256 checksum in the output, and the matched critical faces are recorded as integer bitmasks. This is a complete computational proof for this **specific finite graph**, not a proof from experiments at a few parameter values.

## Relationship to prior work
Chandrakar and Singh, *Independence Complexes of Hexagonal Grid Graphs* [1], determine non-equivariant homotopy types of hexagonal **strip** graphs \(H_{1\times m\times n}\) for \(m=1,2,3\). The reflection-character analysis of the linear subfamily \(H_{1\times1\times n}\) [3] is also a different graph family: those graphs have \(4n+2\) vertices and only a two-dimensional top homology, whereas the coronene graph has twenty-four vertices and two nonzero homology degrees. Moreover, the standard strip graph vertex count is \(2mn+2m+2n\), which cannot equal twenty-four for positive integers \(m,n\), since \((m+1)(n+1)=13\) would be required. These strip results therefore do not imply the present compact seven-hexagon calculation or its \(D_6\)-representation.

Chandrakar [2] studies the shellability of three-cut complexes rather than ordinary independence complexes; the objects and invariants are distinct. The discrete-Morse and Hopf-trace tools applied here are standard. The contribution is the exact finite integral homology and full symmetry/quotient classification on a natural planar hexagonal patch, not a new general-purpose topological theorem. Relevant indexed mathematical records and the cited primary full texts were compared by object and mathematical implication, not merely by title.

## Limitations
Only the ordinary independence complex of the explicitly specified twenty-four-vertex graph and rational homology of its geometric symmetry quotients are determined. The acyclic matching gives the integral Betti groups but does **not** settle unstable seven-cell attaching maps or determine the integral homotopy type. Neither integral quotient torsion nor an infinite family of benzenoid patches is classified. A previously unindexed or differently named exact computation could overlap; mathematical literature and record search cannot establish absolute uniqueness.

## References
[1] H. Chandrakar and A. Singh, *Independence Complexes of Hexagonal Grid Graphs*, arXiv:2512.21318v1, first publicly posted 2025-12-24. https://arxiv.org/pdf/2512.21318

[2] H. Chandrakar, *On Shellability of 3-Cut Complexes of Hexagonal Grid Graphs*, arXiv:2512.21755v1, first publicly posted 2025-12-25. https://arxiv.org/pdf/2512.21755

[3] *Reflection characters of linear hexagonal-chain independence complexes*, published mathematical record `2026/10/11/SCOPE-reflection-characters-of-linear-hexagonal-chain-independence-com--db3e42fb7a57`, result and proof inspected at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-reflection-characters-of-linear-hexagonal-chain-independence-com--db3e42fb7a57

[4] R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (standard discrete-Morse theorem).
