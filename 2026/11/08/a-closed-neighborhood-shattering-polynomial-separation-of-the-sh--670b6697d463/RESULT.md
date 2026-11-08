# A closed-neighborhood shattering-polynomial separation of the Shrikhande and rook graphs

## Finding
Let \(R=K_4\square K_4\) be the \(4\times4\) rook graph and let \(S\) be the Shrikhande graph. Both are strongly regular with parameters \((16,6,2,2)\). For a graph \(G\), write \(\mathcal N^+(G)=\{N_G[v]:v\in V(G)\}\) for its family of **closed** vertex neighborhoods. Define \(f_j(G)\) as the number of \(j\)-element vertex subsets shattered by \(\mathcal N^+(G)\), with \(f_0(G)=1\), and \(\Phi_G(z)=\sum_{j\ge0}f_j(G)z^j\).

Then the **complete** polynomials are
\[
\Phi_R(z)=1+16z+120z^2+288z^3,\qquad
\Phi_S(z)=1+16z+120z^2+224z^3.
\]
Thus both have VC dimension \(3\), but their complete closed-neighborhood shattering polynomials differ already at the top-dimensional face count by \(64\). In contrast, the corresponding **open**-neighborhood trace polynomials coincide and equal \(1+16z+120z^2+320z^3\).

More precisely, the \(560\) three-point supports separate by the number of induced edges and shattering status as follows:

| Induced edges | R shattered | R not shattered | S shattered | S not shattered |
|---:|---:|---:|---:|---:|
| 0 | 0 | 96 | 0 | 96 |
| 1 | 288 | 0 | 192 | 96 |
| 2 | 0 | 144 | 0 | 144 |
| 3 | 0 | 32 | 32 | 0 |

## Assumptions and scope
The common vertex set is \(V=(\mathbb Z/4\mathbb Z)^2\). Distinct vertices \((a,b)\) and \((c,d)\) are adjacent in \(R\) precisely when \(a=c\) or \(b=d\). They are adjacent in \(S\) precisely when their difference belongs to
\[
D=\{(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)\}.
\]
All coordinates are reduced modulo \(4\). A support \(A\subseteq V\) is shattered if for every \(B\subseteq A\) some vertex \(v\in V\) has \(N_G[v]\cap A=B\). The theorem concerns only these two graphs and their entire vertex-set closed-neighborhood systems; it does not assert a classification for other strongly regular graphs.

## Proof
**1. Common parameters and low-dimensional faces.** In either explicitly defined graph every vertex has six distinct neighbors, every pair of distinct vertices has two common **open** neighbors, and there are \(48\) undirected edges (see the complete direct checks in `verify.py`). For each two-point support \(\{u,v\}\), all four traces occur. The \(11\) trace is given by a common neighbor if \(u,v\) are nonadjacent and by the center \(u\) if adjacent; \(10\) and \(01\) are given by the vertices themselves if nonadjacent and by suitable neighbors if adjacent, since each endpoint has three neighbors other than the other endpoint and the two common neighbors. The \(00\) trace exists because the complement of the union of the two closed neighborhoods has cardinality \(4\) for a nonedge and \(6\) for an edge. Thus all \(\binom{16}{2}=120\) pairs and all \(16\) singletons are shattered.

**2. No four-point supports.** Every closed neighborhood contains \(7\) vertices. On any shattered four-point support \(A\), the \(16\) vertex-indexed traces would have to realize all \(16\) distinct binary strings, hence every element of \(A\) would belong to exactly \(8\) of those neighborhoods. But by symmetry of graph adjacency a fixed vertex belongs to exactly \(7\) vertex-indexed closed neighborhoods. Contradiction. Supersets of nonshattered supports cannot be shattered, so \(f_j=0\) for \(j\ge4\).

**3. Exact three-point enumeration with a small complete certificate.** Translation by any element of \(V\) preserves each graph, and acts freely on three-element supports: a nonidentity translation has order \(2\) or \(4\), hence every nontrivial translation orbit has even size and cannot stabilize a three-element set. Therefore the \(\binom{16}{3}=560\) triples partition into exactly \(35\) translation orbits, each of size \(16\). The embedded certificate `triple_orbits.tsv` lists the lexicographically minimal representative from each orbit in each graph, the number of its induced edges, and its complete eight-bit trace mask. For a representative \(A=(a_0,a_1,a_2)\), its trace mask is
\[
M_G(A)=\sum_{\ell\in\{0,1,\ldots,7\}\,\colon\,\exists v\in V,\ \ell=\sum_{j=0}^2 2^j\mathbf 1_{a_j\in N_G[v]}}2^\ell.
\]
The support is shattered exactly when \(M_G(A)=255\). For reproducibility, `verify.py` constructs all \(560\) triples, regenerates all \(35\) representatives and masks per graph, compares every row against `triple_orbits.tsv`, and independently enumerates all \(16\) center traces by set intersection. The table has \(18\) complete masks for \(R\), giving \(18\cdot16=288\) shattered triples, and \(14\) for \(S\), giving \(14\cdot16=224\). The displayed induced-edge breakdown is the direct sum of the same exhaustive traces over all \(560\) triples per graph. Combining steps 1–3 proves both polynomials and both VC dimensions.

**4. Open-neighborhood control.** Replacing \(N_G[v]\) with \(N_G(v)\) in the exact same support enumeration yields \(320\) shattered triples for both graphs, all \(120\) pairs and \(16\) singletons; four-point shattering is impossible because each vertex is in only \(6\) open neighborhoods. This comparison is computational, exact, and ancillary to the closed-neighborhood theorem.

## Verification
Run `python3 verify.py` in a directory alongside `triple_orbits.tsv` using Python 3 (standard library only). The script checks adjacency, degrees, the complete \((16,6,2,2)\) strongly regular conditions, all \(16+120+560+1820\) supports through size four for each graph, a separately coded set-based trace computation for every support, all \(70\) translated certificate rows with full orbit coverage, every triple-induced-edge category, and the open-neighborhood controls. The final marker is `SRG16_CLOSED_SHATTER_PASS 2 graphs 70 triple orbit rows 1120 triples 2*1820 four-supports`. No computational extrapolation beyond these fixed finite graphs is used.

## Relationship to prior work
Adler–Benediktsson–Macpherson analyze VC dimension and VC density for **open** neighborhoods in Hamming and Johnson graphs, and observe boundedness for closed neighborhoods; their work does not determine the complete closed-neighborhood shattering polynomial of this pair. Coudert–Csikós–Ducoffe–Viennot (first arXiv version May 13, 2024) give general algorithms and bounds for **closed**-neighborhood graph VC dimension but no explicit comparison of the two \((16,6,2,2)\) graphs by their full shattering polynomials. Byrne–Byrne–Cioabă (2026) study **open**-neighborhood VC dimensions of strongly regular graphs, not the present exact closed-neighborhood face counts. Generic algorithms and common strongly regular parameters alone do not entail the computed \(288\)-versus-\(224\) coefficient distinction. Existing results determining only the VC dimension \(3\) of rook graph neighborhood systems are strictly weaker than the complete face-count assertion. The first source-date used for assignment is the verified May 13, 2024 arXiv version of Coudert et al.; the other sources give context and comparison.

## Limitations
This is an exact, self-contained finite theorem for two specified graphs, not a formula for all strongly regular graphs, not a general inequality separating neighborhood VC dimensions, and not a proof of priority over all historical and differently indexed terminology. The exhaustive table and executable code are the finite proof certificates; no independent human audit has been carried out.

## References
1. D. Coudert, M. Csikós, G. Ducoffe, L. Viennot, *Practical Computation of Graph VC-Dimension*, arXiv:2405.07588v1 (May 13, 2024), https://arxiv.org/abs/2405.07588.
2. I. Adler, B. G. Benediktsson, D. Macpherson, *Vapnik–Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, Discrete Applied Mathematics 312 (2022), 29–44; accepted preprint https://eprints.whiterose.ac.uk/id/eprint/178584/1/Adler_Benediktsson_Macpherson.pdf.
3. I. Byrne, J. Byrne, S. M. Cioabă, *The VC-dimension of strongly regular graphs*, arXiv:2609.10330 (2026), https://arxiv.org/abs/2609.10330.
