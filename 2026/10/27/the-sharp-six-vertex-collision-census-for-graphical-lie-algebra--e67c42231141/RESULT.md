# The sharp six-vertex collision census for graphical Lie-algebra adjoint spectra

## Finding

For a finite simple graph \(G=(V,E)\), form the two-step nilpotent Lie algebra \(L_G(k)=kV\oplus kE\), where \(k\) is a field, each edge basis vector is central, and \([v_i,v_j]=z_{ij}\) for an edge \(ij\) with \(i<j\) (with the opposite bracket determined by alternation); all nonedge brackets are zero. For \(k=\mathbb F_q\) define the **adjoint-rank polynomial**
\[
B_G(q,t)=\sum_{x\in kV}t^{\operatorname{rank}(\operatorname{ad}_x)}.
\]
It counts vertex-coordinate elements, with each actual Lie-algebra element counted \(q^{|E|}\) times since the edge coordinates are central. Its formal polynomial is the already established graphical class-size polynomial of Rossmann, written here as
\[
\mathcal C_G(q,t)=\sum_{S\subseteq V}(q-1)^{|S|}t^{|N_G[S]|-c(G[S])},\qquad B_G(q,t)=\mathcal C_G(q,t).
\]
The formula itself is **prior work** [3]. Our finding is the following sharp classification of where this polynomial stops distinguishing graph-isomorphism classes.

**Theorem (sharp collision boundary and complete six-vertex census).** Across all simple graphs on at most five vertices, equality of \(\mathcal C_G(q,t)\) as a formal polynomial implies graph isomorphism. Among the \(156\) simple-graph isomorphism classes on six vertices, there are exactly \(149\) distinct polynomials. Their collision partition comprises \(142\) singleton classes and precisely **seven pairs**; no three nonisomorphic six-vertex graphs share the same polynomial. The seven pairs are printed completely in the included finite certificate `CENSUS.txt`, using the canonical edge ordering implemented in `verify.py`.

One connected witness pair on \(V=\{0,1,2,3,4,5\}\) is
\[
E_A=\{01,02,03,04,14,23,35\},\qquad
E_B=\{04,05,13,14,23,24,34\},
\]
where \(ij\) denotes the unordered edge \(\{i,j\}\). The two graphs are nonisomorphic: each has exactly two triangles, but those triangles meet in one vertex in \(A\) and in an edge in \(B\). Their identical formal rank-stratum counts, for \(r=0,1,2,3,4,5\), are
\[
\begin{aligned}
N_0(q)&=1,\\
N_1(q)&=q-1,\\
N_2(q)&=(q-1)(2q+1),\\
N_3(q)&=(q-1)(q^3+2q^2-q-1),\\
N_4(q)&=q^2(q-1)(2q^2-1),\\
N_5(q)&=q^4(q-1)^2.
\end{aligned}
\]
These six polynomials sum to \(q^6\). For the associated \(13\)-dimensional graphical Lie algebras, the numbers of elements with adjoint rank \(r\) equal \(q^7N_r(q)\), and the centralizer dimensions are \(13-r\). Thus all rank and centralizer-dimension multiplicities, and their derived commuting probabilities, agree over every finite field. The two Lie algebras are nevertheless nonisomorphic in odd characteristic, by the graph-reconstruction theorem [2]. No nonisomorphism assertion is made here in characteristic two.

## Assumptions and scope

A graph is finite, undirected, simple, and may have isolated vertices. Graph isomorphism allows arbitrary permutations of vertex labels. The statement about the rank-polynomial collision threshold concerns equality as formal polynomials in \(q\) and \(t\), not equality after one particular numerical substitution. The rank formulas hold for every finite field, including characteristic two. The assertion that distinct witness graphs give nonisomorphic Lie algebras is restricted to characteristic different from two. \(N_G[S]\) means the closed neighborhood of \(S\), and \(c(G[S])\) is the number of connected components of the induced graph; both quantities are zero for the empty support in the appropriate conventions.

## Proof

**Support-rank identity (included for reproducibility, not claimed new).** Fix \(x=\sum_{v\in V}x_vv\) and \(S=\{v:x_v\ne0\}\). The linear transformation \(\operatorname{ad}_x\) vanishes on \(kE\). Its kernel in \(kV\) consists of vectors \(y\) satisfying
\[
x_uy_v-x_vy_u=0\quad\text{for every edge }uv\in E.\]
If an edge runs between a supported vertex \(u\in S\) and an unsupported vertex \(v\notin S\), the equation forces \(y_v=0\). Inside each connected component of \(G[S]\), the nonzero ratios \(y_u/x_u\) are equal and give one freely chosen scalar per component. The remaining free zero-support coordinates are precisely the vertices outside \(N_G[S]\). Therefore
\[
\dim(\ker(\operatorname{ad}_x|_{kV}))=c(G[S])+|V\setminus N_G[S]|,
\]
so \(\operatorname{rank}(\operatorname{ad}_x)=|N_G[S]|-c(G[S])\). Exactly \((q-1)^{|S|}\) vectors have support \(S\), proving the displayed polynomial identity. This is the rank interpretation of the adjacency-module dimension calculation in Rossmann [3, Lemma 3.2], not an originality claim.

**Exact finite classification and minimality.** For each integer \(n\in\{0,1,2,3,4,5,6\}\), a labeled simple graph corresponds uniquely to an integer bitmask of the \(\binom n2\) possible edges. The certificate visits *every* such bitmask. Its relabeling routine explicitly applies all \(n!\) vertex permutations and builds their edge-bitmask orbits, marking each orbit visited exactly once. The first mask in an orbit is its canonical representative. It then evaluates the coefficient dictionary
\[
h_G(r,s)=\#\{S\subseteq V: |S|=s,\ |N_G[S]|-c(G[S])=r\},
\]
which is equivalent to \(\mathcal C_G(q,t)=\sum_{r,s}h_G(r,s)(q-1)^st^r\). Distinct dictionaries are distinct formal polynomials because the powers of \(q-1\) and \(t\) are a polynomial basis. The visited orbits number \(1,1,2,4,11,34\) for \(n=0,1,2,3,4,5\), respectively, and every dictionary is unique in each dimension. At \(n=6\), the same complete permutation-orbit enumeration gives \(156\) graph classes and \(149\) dictionaries, partitioned into \(142\) singletons and seven doubletons. All seven pairs and both labeled edge sets in each pair are emitted by the checker. The finite exhaustive argument is a completed certificate at these sizes; it is not used to infer an unbounded result.

**The witness algebraic formula and nonisomorphism.** Direct subset enumeration, independently checked by exact field-rank matrices, gives the six displayed \(N_r(q)\) for both \(A\) and \(B\). Their triangle-intersection patterns establish graph nonisomorphism without reliance on the enumeration. Mainkar [2, Theorem 1.1] proves that graphical two-step nilpotent Lie algebras over fields of characteristic not two are isomorphic only if the underlying simple graphs are isomorphic. Its hypothesis applies here; consequently the two odd-characteristic Lie algebras are nonisomorphic despite the equal adjoint spectra.

## Verification

Run `python3 verify.py`, which requires only the Python standard library. It exhausts all graph bitmasks through six vertices and all label permutations for their orbit decomposition; compares exact coefficient dictionaries in the algebraically independent monomials \((q-1)^st^r\); confirms that the seven six-vertex collisions have multiplicity precisely two; verifies the witness triangle intersections; and independently constructs the actual bracket-coordinate matrix of \(\operatorname{ad}_x\) for *every* vertex vector over the prime fields of sizes \(2\), \(3\), and \(5\). The expected final line is `GRAPHICAL_BREADTH_CERTIFICATE_OK`. The recorded stdout is in `CENSUS.txt`, but is not a substitute for the reproducible code or the support-rank proof.

## Relationship to prior work

Remm [1] treats breadth, the maximum rank of adjoint maps, as a nilpotent Lie-algebra classification invariant. This motivates examining the strictly stronger entire adjoint-rank distribution. Mainkar [2] proves that the underlying graph can be reconstructed from the graphical Lie algebra in characteristic not two. Rossmann [3] already introduces **exactly the same** two-variable polynomial \(\mathcal C_G\), its subset formula, and its graphical-group class-size interpretation; the present finding does not claim any of these identities as new. The distinct new statement is the **sharp injectivity failure at six vertices and the complete seven-pair collision census**, demonstrating concretely that even the full adjoint-rank distribution need not reconstruct the Lie algebra. Rossmann [3] tabulates or refers to graph computations up through five vertices but does not report the seven-pair six-vertex collision classification in the inspected text. Rossmann and Voll [4] provide tables of a different graph-indexed pair of ask zeta functions for six-vertex graphs, not a table explicitly listing collision classes of this two-variable vertex-support polynomial; the possibility that the new census can be recovered indirectly from those data remains a documented literature risk.

## Limitations

The graph-class census is exhaustive only for at most six vertices; no assertion concerns injectivity or collision multiplicity for larger graphs. Although the rank and counting identities hold in all characteristics, the assertion of nonisomorphic Lie algebras uses [2] and is only made in odd characteristic. No independent mathematical audit or absolute publication-priority determination has been performed. The literature search is bounded; the published general polynomial and separate ask-zeta tables provide strong nearby background and potential indirect coverage, but the exact sharp collision census was not found in the inspected material.

## References

1. E. Remm, “Breadth and characteristic sequence of nilpotent Lie algebras,” arXiv:1605.06583v1 (first publicly posted 2016-05-21; primary MSC 17B30), especially the introduction and Section 1.
2. M. G. Mainkar, “Graphs and two-step nilpotent Lie algebras,” arXiv:1310.3414v1 (2013-10-12), Theorem 1.1.
3. T. Rossmann, “Enumerating conjugacy classes of graphical groups over finite fields,” arXiv:2107.05564 (first posted 2021-07-12), Equation (1.2), Theorem A, Proposition 2.3, and Lemma 3.2; later published in Bulletin of the London Mathematical Society 54 (2022), 1923–1943.
4. T. Rossmann and C. Voll, “Groups, graphs, and hypergraphs: average sizes of kernels of generic matrices with support constraints,” arXiv:1908.09589, and the publicly posted six-vertex ask-zeta-function tables at `https://maths.nuigalway.ie/~rossmann/cico/`.
