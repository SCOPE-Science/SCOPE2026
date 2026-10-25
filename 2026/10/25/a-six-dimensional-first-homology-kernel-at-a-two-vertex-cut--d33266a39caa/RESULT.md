# A six-dimensional first-homology kernel at a two-vertex cut

## Finding

Let \(G\) be the simple graph obtained from \(K_5\) on vertices \(\{u,v,a,b,c\}\) by adjoining two new vertices \(x,y\), each adjacent to both \(u\) and \(v\). For the ordered two-point configuration space
\[
F(G,2)=\{(p,q)\in G\times G:p\ne q\},
\]
the inclusion \(\alpha:F(G,2)\hookrightarrow G\times G\) has
\[
\dim_{\mathbb Q}H_1(F(G,2);\mathbb Q)=22,\qquad
\dim_{\mathbb Q}H_1(G\times G;\mathbb Q)=16,
\]
and therefore
\[
\dim_{\mathbb Q}\ker\!\left(\alpha_*:H_1(F(G,2);\mathbb Q)\to H_1(G\times G;\mathbb Q)\right)=6.
\]
The general two-cut result of Farber and Hanbury guarantees a free subgroup of rank \(4\) in the corresponding integral kernel for this graph; the exact rational calculation gives rank \(6\), a strict excess of two dimensions over that general lower bound.

## Assumptions and scope

The graph has seven vertices and fourteen edges: all ten edges of the indicated \(K_5\), together with \(ux,vx,uy,vy\). It is connected, simple, 2-vertex-connected, and nonplanar because it contains \(K_5\). Its cycle rank is
\[
\beta_1(G)=|E(G)|-|V(G)|+1=14-7+1=8.
\]
The coefficient field throughout the finding is \(\mathbb Q\). The claim concerns the rational first homology of the ordered configuration space and the kernel of the inclusion-induced map. It makes no claim about integral torsion.

## Proof

Barnett and Farber give a strong homotopy retraction from \(F(G,2)\) onto the finite cubical complex \(D(G,2)\) whose cells are ordered pairs of cells of \(G\) with disjoint supports. Thus \(H_1(F(G,2);\mathbb Q)\) can be computed from this finite cellular chain complex.

For the graph specified above, the cells are:
- \(42\) zero-cells \((p,q)\) with \(p\ne q\);
- \(140=2\cdot14\cdot(7-2)\) one-cells of types \((e,p)\) and \((p,e)\), with \(p\) not incident to \(e\);
- \(82\) two-cells \((e,f)\), where \((e,f)\) is an ordered pair of edges with disjoint endpoint sets.

Orient each edge \(e=(s,t)\) with \(s<t\). The one-cell boundaries are
\[
\partial(e,p)=(t,p)-(s,p),\qquad
\partial(p,e)=(p,t)-(p,s).
\]
For a two-cell \((e,f)\), with \(e=(s,t)\) and \(f=(r,w)\), the product boundary is
\[
\partial(e,f)=(t,f)-(s,f)-(e,w)+(e,r).
\]
The included verifier constructs these integer boundary matrices directly, checks \(\partial_1\partial_2=0\), and performs exact Gaussian elimination over \(\mathbb Q\). It obtains
\[
\operatorname{rank}_{\mathbb Q}\partial_1=41,\qquad
\operatorname{rank}_{\mathbb Q}\partial_2=77.
\]
Consequently,
\[
\dim_{\mathbb Q}H_1(F(G,2);\mathbb Q)
=140-41-77=22.
\]

Barnett and Farber prove that for every connected finite graph not homeomorphic to \(S^1\), the inclusion \(\alpha\) induces an epimorphism on first homology. Here \(G\) is connected and not a circle, so \(\alpha_*\) is onto. By the Künneth theorem,
\[
\dim_{\mathbb Q}H_1(G\times G;\mathbb Q)=2\beta_1(G)=16.
\]
Rank-nullity therefore gives \(\dim_{\mathbb Q}\ker\alpha_*=22-16=6\).

For the comparison with the two-cut bound, delete the edge \(uv\) and call the resulting graph \(G'\). The graph \(G'-\{u,v\}\) has three connected components: the triangle on \(\{a,b,c\}\), the isolated vertex \(x\), and the isolated vertex \(y\). Farber and Hanbury's edge-addition theorem therefore supplies a free subgroup of rank \(2\cdot3-2=4\) in the relevant kernel. The computed rank \(6\) is consistent with, and strictly sharpens, that lower bound for this specific graph.

## Verification

The standalone file `verify_graph_configuration.py` uses only the Python standard library. It enumerates every cell of \(D(G,2)\), constructs the two boundary matrices from the displayed formulas, verifies the chain condition, and reproduces the cell counts, exact ranks, first Betti number, target rank, and kernel dimension. Its expected output is:
- cell counts \((42,140,82)\);
- boundary ranks \((41,77)\);
- \(\dim_{\mathbb Q}H_1(F(G,2);\mathbb Q)=22\);
- target rank \(16\);
- kernel dimension \(6\).

The finite matrix calculation proves the stated rational-rank claim; it is not used to infer any uncomputed integral torsion statement.

## Relationship to prior work

Barnett and Farber establish the finite cubical model, the surjectivity of \(\alpha_*\), and the exact-sequence description of \(H_1(F(G,2))\) through the cokernel of an intersection form. Farber and Hanbury define graph maturity by requiring \(\alpha_*\) to be an isomorphism, prove that double wedges of nontrivial connected subgraphs are not mature, and give a general rank lower bound when an edge is added across a disconnected two-vertex deletion. Those results imply that the present graph is non-mature and that the kernel has rank at least \(4\). They do not state the exact value \(6\) for this graph; the exact value here comes from the explicit cellular boundary calculation.

## Limitations

This is one exact finite case, not a classification of all two-vertex cuts or all double wedges. The calculation establishes rational first-homology ranks only. It does not establish a general formula for the kernel, prove a new characterization of mature graphs, or claim integral torsion-freeness.

## References

1. K. Barnett and M. Farber, “Topology of Configuration Space of Two Particles on a Graph, I,” arXiv:0903.2180 (first public date 2009-03-12), especially Lemma 1.1, Proposition 1.3, and Proposition 2.3. https://arxiv.org/abs/0903.2180
2. M. Farber and E. Hanbury, “Topology of configuration space of two particles on a graph, II,” arXiv:1005.2300 (first public date 2010-05-13), especially Theorem 14 and Proposition 19. https://arxiv.org/abs/1005.2300
3. K. Barnett, “The Configuration Space of Two Particles Moving on a Graph,” PhD thesis, Durham University (2010), repository abstract consulted for prior-work context: https://etheses.dur.ac.uk/id/eprint/293/.
4. Reproducible exact chain calculation: `verify_graph_configuration.py` (included with this result).
