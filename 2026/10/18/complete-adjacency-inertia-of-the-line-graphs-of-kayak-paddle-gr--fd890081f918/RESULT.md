# Complete adjacency inertia of the line graphs of kayak-paddle graphs

## Finding
Let \(K(p,q,r)\) be the connected simple graph consisting of disjoint cycles \(C_p\) and \(C_q\), joined at one vertex of each by a path of exactly \(r\) edges, where \(p,q\ge3\) and \(r\ge1\). The connecting path has no other vertices in either cycle. Let \(L(K(p,q,r))\) be its line graph. Write \(\operatorname{In}(A)=(n_+,n_0,n_-)\) for real symmetric adjacency inertia, and \(s=n_+-n_-\).

The **complete inertia** is given by a two-parameter residue table and the parity of the connecting path. Define \(p_0=3+((p-3)\bmod4)\) and \(q_0=3+((q-3)\bmod4)\). Exchange the two if necessary so that \(p_0\le q_0\). The following entries are ordered pairs \((s,n_0)\):

| \((p_0,q_0)\) | \(r\) odd | \(r\) even |
|:---:|:---:|:---:|
| \((3,3)\) | \((-2,1)\) | \((-2,0)\) |
| \((3,4)\) | \((-1,1)\) | \((-1,2)\) |
| \((3,5)\) | \((-1,0)\) | \((0,0)\) |
| \((3,6)\) | \((-2,0)\) | \((-1,0)\) |
| \((4,4)\) | \((0,3)\) | \((0,2)\) |
| \((4,5)\) | \((1,1)\) | \((0,1)\) |
| \((4,6)\) | \((0,1)\) | \((-1,1)\) |
| \((5,5)\) | \((1,0)\) | \((0,0)\) |
| \((5,6)\) | \((0,0)\) | \((-1,0)\) |
| \((6,6)\) | \((-1,0)\) | \((-1,1)\) |

Put \(m=p+q+r\), the number of vertices of the line graph. Once the table determines \(s\) and \(n_0\), the other two inertia indices are exactly
\[
n_+=\frac{m-n_0+s}{2},\qquad n_-=\frac{m-n_0-s}{2}.
\]
In particular \(s\le1\) for every kayak paddle, and equality holds **if and only if** \(r\) is odd and the unordered residues of \((p,q)\) modulo four are \(\{0,1\}\) or \(\{1,1\}\). Moreover, the maximum adjacency nullity is three, attained **if and only if** both cycle lengths are divisible by four and \(r\) is odd.

## Assumptions and scope
All graphs are finite, simple, undirected, and connected; the two cycles are vertex disjoint. The joining path is internally disjoint from both cycles. All eigenvalues are counted with multiplicity over the reals, with zero eigenvalues kept as a separate inertia index. The bridge length is the number of path edges, not the number of internal path vertices. The table applies to every positive integer \(r\) and every \(p,q\ge3\); no generic nonsingularity assumption is made. The two cycle lengths may be exchanged.

## Proof
**Incidence transfer.** Let \(B\) be the unoriented vertex–edge incidence matrix of \(G=K(p,q,r)\). Then \(Q(G)=BB^{\mathsf T}\) is the signless Laplacian and \(B^{\mathsf T}B=A(L(G))+2I\). The graph has \(n=p+q+r-1\) vertices and \(m=n+1\) edges. If \(\operatorname{In}(Q(G)-2I)=(a,z,b)\), equality of the nonzero spectra of \(BB^{\mathsf T}\) and \(B^{\mathsf T}B\) shows that \(\operatorname{In}(A(L(G)))=(a,z,b+1)\). This remains true when \(G\) is bipartite, because any additional incidence nullity contributes an eigenvalue \(-2\) to the line graph, while the same zero of \(Q\) already contributes negatively to \(Q-2I\).

**Four-subdivision congruence.** Replace an arbitrary edge \(uv\) by a path with five edges and four new degree-two internal vertices. In \(Q-2I\), the principal block on those internal vertices is the adjacency matrix \(T_4=A(P_4)\), with inertia \((2,0,2)\). Its inverse has zero diagonal at the two ends and endpoint-to-endpoint entry \(-1\). Taking the Schur complement thus restores the original \(+1\) off-diagonal \(uv\) entry, without changing either endpoint diagonal. Consequently the new shifted signless Laplacian is congruent to the old one direct-summed with \(T_4\). Its positive and negative indices each increase by two; nullity and signature are unchanged. Subdivision on either cycle therefore changes its length by four without changing the two table entries.

**Two-subdivision of the joining bridge.** Replace one edge of the connecting path by a three-edge path, inserting two degree-two vertices. The internal block is \(T_2=A(P_2)\), with inertia \((1,0,1)\), zero inverse endpoint diagonals, and inverse endpoint-to-endpoint entry \(+1\). Its Schur complement produces an off-diagonal \(-1\) across the original bridge instead of \(+1\). Since that edge is a bridge, multiplying all coordinates on one side of the bridge by \(-1\) is an invertible diagonal congruence that restores the original shifted signless Laplacian. Thus increasing \(r\) by two increases both nonzero inertia indices of \(Q-2I\) by one, preserving nullity and signature.

**Finite exact base calculation.** Applying the preceding two congruences reduces every parameter triple to \(p_0,q_0\in\{3,4,5,6\}\) and \(r_0\in\{1,2\}\). Exchanging the cycles leaves exactly twenty base matrices. Their entries are obtained by the following finite exact rational-congruence procedure, fully specified and implemented in the accompanying standalone verifier. Construct \(Q-2I\) from its degree diagonal and \(+1\) adjacency entries. If a nonzero diagonal entry exists, eliminate it by a scalar symmetric Schur complement and record one positive or negative eigenvalue according to its sign. Otherwise, if some off-diagonal entry is nonzero, pivot on the corresponding \(2\times2\) block \(\left(\begin{smallmatrix}0&t\\t&0\end{smallmatrix}\right)\), record one positive and one negative eigenvalue, and take its symmetric Schur complement. If all entries vanish, record the remaining dimension as nullity. Each step is an invertible real congruence, and all arithmetic is exact rational arithmetic, so the algorithm terminates after at most the matrix order, determines every sign with certainty, and handles singular cases. Executing this finite procedure gives exactly the twenty table entries above. A separate direct line-graph adjacency construction in the verifier gives the same twenty inertias.

Repeated forward application of the congruence reductions increases \(n_+\) and \(n_-\) equally while preserving \((s,n_0)\). The table thus holds for all \(p,q,r\) without any numerical extrapolation. Since the line graph has \(m\) vertices, its two nonzero inertia indices are uniquely determined by the equations \(n_++n_-=m-n_0\) and \(n_+-n_-=s\), giving the stated formulas. Inspection of the finite table yields both exact equality classifications. \(\square\)

## Verification
Run `python3 verify_kayak.py` with Python 3.10 or later. The script uses only the Python standard library. It reconstructs every kayak-paddle edge set, computes all twenty base shifted-signless-Laplacian inertias exactly, reconstructs each base **line graph directly** and checks its inertia exactly, and compares both constructions against the asserted table. It additionally checks all \(1320\) distinct parameter triples with \(3\le p\le q\le17\) and \(1\le r\le11\) using exact rational arithmetic, including singular cases and nonminimal residues. The recorded output is in `verification_output.txt`. These supplemental large instances corroborate the reduction; the infinite proof consists of the two exact subdivision congruences plus the twenty finite exact base calculations.

## Relationship to prior work
Akbari, Elphick, Kumar, Pragada and Tang (first posted August 2, 2025) considered line-graph signature and identified the isolated kayak-paddle equality examples \(K(4,5,1)\) and \(K(5,5,1)\). Francis and Uptain (July 24, 2026) later disproved the universal signature-one conjecture and obtained unbounded signature with more complicated cactus graphs. Paone and Paone (August 1, 2026) obtained exact line-graph inertias for roses and generalized theta graphs; their Remark 9.2 explicitly identifies two disjoint cycles joined by a path as **outside** those classes. Their general path-block machinery and the known four-subdivision principle are antecedents to the method employed here, not claimed innovations. A separate July 30, 2026 paper by the same authors treats pendant-tree responses and fixed-cyclomatic-number bounds, but does not supply an exact kayak-paddle inertia classification.

The present assertion is the closed residue/parity profile of **all** kayak paddles, including every nullity branch and all equality cases. It does not claim a new general incidence identity, a new congruence method, a solution of the fixed-cyclomatic-number conjecture for arbitrary graphs, or novelty for the two previously exhibited equality examples in isolation.

## Limitations
The theorem is restricted to two disjoint cycles with a single connecting path and no attached trees or additional edges. It does not extend the signature bound to arbitrary bicyclic graphs, nor does it resolve the open sharp cyclomatic-number inequality for general connected graphs. Priority remains subject to inspection of any earlier equivalent all-parameter spectral or threshold-inertia characterization of kayak-paddle graphs. The mathematical review is self-review only; no independent validation has occurred.

## References
1. S. Akbari, C. Elphick, H. Kumar, S. Pragada and Q. Tang, *A new conjecture on the inertia of graphs*, arXiv:2508.01163 (first public August 2, 2025); later published in Discrete Mathematics 349 (2026), 114953. https://arxiv.org/abs/2508.01163
2. L. Francis and T. Uptain, *The signature of connected line graphs is unbounded*, arXiv:2607.22874 (first public July 24, 2026). https://arxiv.org/abs/2607.22874
3. A. Paone and M. Paone, *Line-graph inertia of roses and generalized theta graphs*, version 1.0 (August 1, 2026), DOI: 10.5281/zenodo.21744051. https://aletheia-technologies.it/en/research/line-graph-inertia-roses-generalized-theta/reader/
4. A. Paone and M. Paone, *Line-Graph Signature Beyond the 2-Core: Counterexamples, Pendant Attachments, and Bounds at Fixed Cyclomatic Number*, version 1.3 (July 30, 2026). https://aletheia-technologies.it/research/line-graph-signature-beyond-the-2-core/reader/
