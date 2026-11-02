# Field-dependent Ising ground-state separation of the Shrikhande and rook graphs

## Finding

Let \(S\) be the Shrikhande graph and \(R=K_4\square K_4\) the rook graph. Both have 16 vertices, 48 edges and adjacency eigenvalue multiset \(\{6^1,2^6,(-2)^9\}\). For classical spins \(\sigma_v\in\{-1,+1\}\), the uniform antiferromagnetic Hamiltonian is

\[
\mathcal H_G(\sigma)=J\sum_{\{u,v\}\in E(G)}\sigma_u\sigma_v-h\sum_v\sigma_v,\qquad J>0,\quad h\in\mathbb R.
\]

Despite the identical adjacency spectra, the exact positive critical fields are \(h/J\in\{1,3,6\}\) for \(S\), versus \(h/J\in\{2,6\}\) for \(R\). Only \(S\) has a strictly stable ground-state magnetization \(M=4\) plateau. The sector minima, multiplicities, and all coexistence counts are given below. The rook sector formula is a comparator already obtainable from its general line-graph classification; the specific Shrikhande classification and the resulting field-response separation are the claims at issue.

Put \(r=\#\{v:\sigma_v=-1\}\), so \(M=16-2r\). Let \(B_G(r)\) be the maximum number of edges with opposite spins when there are \(r\) negative spins, and let \(C_G(r)\) count configurations attaining that maximum. Since spin complementation maps \(r\) to \(16-r\), both functions are symmetric about \(r=8\).

| \(r\) | \(B_S(r)\) | \(C_S(r)\) | \(B_R(r)\) | \(C_R(r)\) |
|---:|---:|---:|---:|---:|
| 0 | 0 | 1 | 0 | 1 |
| 1 | 6 | 16 | 6 | 16 |
| 2 | 12 | 72 | 12 | 72 |
| 3 | 18 | 96 | 18 | 96 |
| 4 | 24 | 16 | 24 | 24 |
| 5 | 26 | 432 | 26 | 432 |
| 6 | 30 | 32 | 28 | 1224 |
| 7 | 30 | 816 | 30 | 816 |
| 8 | 32 | 42 | 32 | 90 |

For \(h\ge0\), the complete field response, with \(r\)-sectors and the total labelled ground-state degeneracy, is:

| Graph | Field range | Ground-state \(r\) | Total degeneracy |
|---|---|---|---:|
| Shrikhande | \(0\le h<J\) | 8 | 42 |
| Shrikhande | \(h=J\) | 6, 8 | 74 |
| Shrikhande | \(J<h<3J\) | 6 | 32 |
| Shrikhande | \(h=3J\) | 4, 6 | 48 |
| Shrikhande | \(3J<h<6J\) | 4 | 16 |
| Shrikhande | \(h=6J\) | 0, 1, 2, 3, 4 | 201 |
| Shrikhande | \(h>6J\) | 0 | 1 |
| Rook | \(0\le h<2J\) | 8 | 90 |
| Rook | \(h=2J\) | 4, 5, 6, 7, 8 | 2586 |
| Rook | \(2J<h<6J\) | 4 | 24 |
| Rook | \(h=6J\) | 0, 1, 2, 3, 4 | 209 |
| Rook | \(h>6J\) | 0 | 1 |

The response at negative fields follows by simultaneous spin reversal and \(h\mapsto-h\). The zero-field ground-state energy is \(-16J\) for both graphs, but their ground-state counts are 42 and 90, respectively.

## Assumptions and scope

The vertex set is \(\mathbb Z_4^2\). Vertices are indexed \(u=4i+j\) with \(0\le i,j<4\). In \(S\), \((i,j)\) and \((i',j')\) are adjacent precisely when their difference modulo four is one of \((\pm1,0),(0,\pm1),(\pm1,\pm1)\), where the last two signs agree. In \(R\), adjacency means equal first or second coordinate and distinct vertices. Edges are undirected and counted once. All sixteen spin sites are labelled; degeneracies count labelled configurations, not symmetry orbits. Interactions are identical, antiferromagnetic, classical and at zero temperature. No thermodynamic-limit assertion is made.

## Proof

For a set of \(r\) negative spins, write \(e_G(r)\) for its number of induced edges. Six-regularity gives exactly \(B=6r-2e\). The spin energy is \(48J-2JB-h(16-2r)\), hence minimizing it is equivalent to maximizing \(B-(h/J)r\).

The two graphs satisfy the exact strongly regular adjacency identity \(A^2=4I+2\mathbf 1\mathbf 1^{\mathsf T}\), checked directly from their vertex descriptions. Their adjacency spectrum is therefore \(6\) once, \(2\) six times and \(-2\) nine times. If \(x\in\{0,1\}^{16}\) indicates an \(r\)-set, decompose it into \((r/16)\mathbf1\) and its perpendicular part. The least adjacency eigenvalue gives

\[
2e=x^{\mathsf T}Ax\ge \frac{6r^2}{16}-2\left(r-\frac{r^2}{16}\right)
=\frac{r^2}{2}-2r,
\qquad e\ge\frac{r^2}{4}-r.
\]

For \(r=0,1,2,3,4\), the lower bound \(e\ge0\) is attained by subsets of an independent four-set in each graph. For \(r=5,6,7,8\), integrality yields lower bounds of 2, 3, 6 and 8 induced edges. In the rook graph at \(r=6\), there is an additional obstruction: the induced edge count equals the sum of \(\binom t2\) over the four row occupancies plus the same sum over the four column occupancies. Six occupied squares give at least two pairs in the rows and two in the columns, so \(e\ge4\). The following masks (bit \(4i+j\) denotes vertex \((i,j)\)) attain every corresponding lower bound; the rook six-site witness attains its stronger bound:

| \(r\) | Shrikhande mask | Rook mask |
|---:|---|---|
| 4 | `0x0505` | `0x1248` |
| 5 | `0x0345` | `0x112c` |
| 6 | `0x152c` | `0x116a` |
| 7 | `0x070f` | `0x136c` |
| 8 | `0x0f0f` | `0x33cc` |

This proves all \(B_G(r)\) entries by exact upper and lower bounds, rather than extrapolation from enumeration. The finite multiplicities \(C_G(r)\) follow from a complete census of all \(2^{16}=65536\) assignments, performed in two mathematically independent ways in `verify.py`: (i) Gray-code flipping with exact incremental cut changes, and (ii) explicit enumeration of all \(16^4\) ordered four-row states using intrarow and interrow interactions. Both implementations calculate the entire bivariate population \(\#\{\sigma:\,r(\sigma)=r,\,B(\sigma)=b\}\), agree exactly, and separately verify each sector contains \(\binom{16}{r}\) assignments. Thus their maximum-cut coefficients give the displayed exact degeneracies, not estimates.

The upper convex envelopes of the nine sector points \((r,B_G(r))\) for \(0\le r\le8\) have vertices \((8,32),(6,30),(4,24),(0,0)\) for the Shrikhande graph and \((8,32),(4,24),(0,0)\) for the rook graph. Their consecutive slopes are respectively \(1,3,6\) and \(2,6\). Other \(r\) values lie strictly below those envelope segments except for the sectors explicitly listed at the critical fields. Inserting the enumerated \(C_G(r)\) gives every coexistence count. For \(h\ge0\), complement symmetry implies that no sector \(r>8\) can improve the energy, completing the proof.

## Verification

Run `python3 verify.py` using only the Python standard library. The program reconstructs both graphs from explicit coordinates; checks their degree and exact common-neighbor matrix; independently enumerates every one of their 65,536 spin configurations twice; compares the full bivariate populations; checks all 17 sector optima and multiplicities using complement symmetry; checks the ten constructive witness masks; verifies all displayed critical fields and degeneracies; and returns `VERIFY_OK`. A record of the actual execution is included in `verification_output.txt`. The computation is finite and exhaustive; its validity depends on the transparent, inspectable enumeration code, not on a numerical optimization solver or floating-point tolerances.

## Relationship to prior work

Vinci et al. introduced graph Ising spectra and longitudinal-field refinements as physically meaningful graph invariants; their main study explores other pairs and reports vertex-transitive tests up to fifteen sites. This finding supplies an exact sixteen-site comparison for the canonical cospectral strongly regular pair. Brouwer's graph description documents their common strongly regular parameters and adjacency spectrum, but does not give field-dependent Ising ground-state populations. The general rook-graph antiferromagnet sector classification already implies the comparator's rook entries; none of those entries is presented as independently new. The Shrikhande six-site induced-edge bound is attained while the rook counterpart is not, giving a structural explanation for the different field envelopes.

## Limitations

The result is exact only for these two finite graphs, uniform positive \(J\), classical binary spins, a uniform longitudinal field and zero temperature. It does not address transverse fields, variable edge weights, thermal partition functions, other strongly regular graphs or universal spectral distinguishability. A broader unlocated table of exact field-dependent ground states could affect historical priority. No independent scientific audit has been performed.

## References

1. W. Vinci, K. Markström, S. Boixo, A. Roy, F. M. Spedalieri, P. A. Warburton and S. Severini, *Hearing the Shape of the Ising Model with a Programmable Superconducting-Flux Annealer*, arXiv:1307.1114 (first posted 2013-07-03); *Scientific Reports* **4**, 5703 (2014), https://doi.org/10.1038/srep05703. Accessible full article: https://discovery.ucl.ac.uk/id/eprint/1443487/1/srep05703.pdf.
2. A. E. Brouwer, *Shrikhande graph*, https://aeb.win.tue.nl/drg/graphs/Shrikhande.html (graph parameters and spectrum).
