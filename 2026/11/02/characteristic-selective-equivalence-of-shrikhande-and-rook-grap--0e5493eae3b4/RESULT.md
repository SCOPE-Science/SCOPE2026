# Characteristic-selective equivalence of Shrikhande and rook graph states

## Finding
Let \(R\) be the \(4\times4\) rook graph, and \(S\) the Shrikhande graph, the two nonisomorphic strongly regular graphs with parameters \((16,6,2,2)\). Put a prime-dimensional qudit at each of their sixteen vertices and prepare the pure, unit-edge-weight graph state in each case.

**Theorem.** At local dimension \(p=2\), the graph states \(|R\rangle_2\) and \(|S\rangle_2\) are locally Clifford equivalent after relabeling the sites. At every **odd prime** local dimension \(p\), they are not locally unitarily equivalent, even after arbitrary relabeling of the sites.

More precisely, for each four-vertex subset \(A\) and \(G\in\{R,S\}\), the reduced state on \(A\) has \(p^{r_p(G,A)}\) nonzero eigenvalues, each \(p^{-r_p(G,A)}\), with \(r_p(G,A)=\operatorname{rank}_{\mathbb F_p}\Gamma_G[A,V\setminus A]\). For every odd prime \(p\), the complete four-site rank profile is

| Graph | Four-site entropy \(3\log p\) | Four-site entropy \(4\log p\) |
|---|---:|---:|
| Rook graph | 36 | 1784 |
| Shrikhande graph | 12 | 1808 |

Here the entropy is in natural logarithm units; in base-\(p\) units the respective values are \(3\) and \(4\). The deficient subsets are **exactly** the induced four-cycles in either graph. In particular, the entire positive-order Rényi spectrum of each reduced state is specified, and the differing four-site profile is a local-unitary invariant up to site relabeling.

## Assumptions and scope
Both graphs have the common vertex set \(V=\mathbb Z_4\times\mathbb Z_4\), with row-major index \(i=4a+b\) for \((a,b)\in V\). The rook adjacency is \((a,b)\sim(c,d)\) exactly when precisely one coordinate agrees. The Shrikhande adjacency is given by the difference set \(\{(\pm1,0),(0,\pm1),(\pm1,\pm1)\}\), with the two signs in the final pair equal, all modulo four.

For a prime \(p\), let \(\omega_p=e^{2\pi i/p}\) and define the standard unweighted graph state
\[
|G\rangle_p=p^{-8}\sum_{x\in\mathbb F_p^{16}}\omega_p^{\sum_{\{u,v\}\in E(G)}x_ux_v}|x\rangle.
\]
This normalization gives unit norm. No claim is made for mixed states, nonunit interaction weights, composite local dimensions, or arbitrary quantum states associated to these graphs.

## Proof
**1. Cut-spectrum lemma.** For any symmetric zero-diagonal graph adjacency \(\Gamma\) over \(\mathbb F_p\), write a configuration as \((x,y)\) across \(A\sqcup B\). The phase separates as a function of \(x\), a function of \(y\), and the cross-term \(x^\mathsf T\Gamma_{A,B}y\). The first two phases are local diagonal unitaries and do not affect Schmidt coefficients. Orthogonality of finite-field additive characters shows that the reduced matrix on \(A\) has entries proportional to \(\mathbf1_{\Gamma_{A,B}^\mathsf T(x-x')=0}\), up to diagonal phases. Its nonzero eigenvalues are therefore all \(p^{-r}\), of multiplicity \(p^r\), where \(r=\operatorname{rank}_{\mathbb F_p}\Gamma_{A,B}\). This proves the asserted flat spectra for every cut and prime.

**2. A local-Clifford path at characteristic two.** Beginning with the rook graph, perform local complementation successively at row-major vertices \(0,5,10,15\): local complementation at \(v\) toggles precisely the edges among distinct neighbors of \(v\). Relabel the resulting graph by the permutation
\[
P=(0,1,4,15,3,2,13,6,12,7,8,9,5,14,11,10),
\]
meaning that old site \(i\) becomes Shrikhande site \(P_i\). Direct substitution in the two explicit adjacency rules shows that the resulting adjacency equals the Shrikhande adjacency on all \(\binom{16}{2}=120\) unordered pairs. The standalone verifier performs exactly this adjacency identity. The standard graph-state local-complementation identity implements each step by a tensor product of one-qubit Clifford unitaries. Thus the two qubit states are locally Clifford equivalent up to this permutation. As an independent consequence, the verifier confirms equality of the binary cut rank on every one of the \(2^{16}\) labeled subsets under \(P\).

**3. Odd-characteristic four-site ranks.** Each graph satisfies \(A^2=4I+2J\), hence the real adjacency eigenvalues are \(6,2,-2\). If an induced four-cycle has vertices alternatingly assigned coefficients \((+1,-1,+1,-1)\), this supported vector attains Rayleigh quotient \(-2\); the global least eigenvalue is \(-2\), hence it is an actual \(-2\)-eigenvector. Its equation at every outside vertex is a zero integer linear combination of the four cut rows. Therefore every induced four-cycle has cross-cut rank at most three in every field. The independent exact checks below establish rank at least three in all odd characteristics.

For full-rank classification, the verifier evaluates the \(4\times12\) cut matrix over \(\mathbb F_3\) for **all** \(\binom{16}{4}=1820\) subsets of each graph; it independently enumerates its \(3^4\) possible left null vectors, and compares the rank-three cases to the explicitly tested induced-four-cycle predicate. Exactly the induced four-cycles have rank three over \(\mathbb F_3\), the others rank four. It repeats modular elimination over \(\mathbb F_5\), finding identical ranks. This is a complete finite enumeration on a fixed graph pair, not an extrapolation from samples.

To extend from these fields to **every odd prime**, the verifier also exhaustively enumerates all \(2^9\) zero-one \(3\times3\) matrices and all \(2^{16}\) zero-one \(4\times4\) matrices, proving sharp determinant absolute-value bounds \(2\) and \(3\), respectively. A rank-four cut over \(\mathbb F_3\) contains a nonzero four-by-four minor whose integer determinant is nonzero, of absolute value at most three, and not divisible by three; hence that determinant is \(\pm1\) or \(\pm2\) and remains nonzero modulo **every** odd prime. A rank-three cut over \(\mathbb F_3\) has a nonzero three-by-three minor with integer determinant \(\pm1\) or \(\pm2\), giving rank at least three over every odd prime. Its rank at most three follows from the integer alternating four-cycle relation established above. Consequently the exact four-site rank classification holds for every odd prime, without needing an unbounded computation.

**4. The two different counts.** Exhaustive induced-subgraph enumeration gives exactly \(36\) induced four-cycles for the rook graph and \(12\) for the Shrikhande graph. Independently, the rook four-cycles are exactly the rectangles obtained by selecting two of four rows and two of four columns, so their number is \(\binom42^2=36\). In the Shrikhande Cayley graph, the twelve induced four-cycles correspond to four translates each of the three order-four cyclic subgroups generated by \((1,0)\), \((0,1)\), and \((1,1)\); the exhaustive check verifies the count directly. These are all the deficient four-site subsets by step 3. Thus the rank histograms are different at every odd prime. A tensor product of local unitaries preserves each subset's reduced spectrum, and a site permutation merely permutes the subsets, so no such equivalence can exist.

## Verification
Run `python3 artifacts/verify.py` using Python 3 with only its standard library. The code directly builds both adjacency matrices, verifies the strongly regular parameters and distinguishes the open-neighborhood structures, replays all four local complementations and the displayed permutation, checks all \(65536\) binary cut ranks, enumerates every zero-one minor of orders three and four, and checks all \(1820\) four-vertex subsets in each graph with modular elimination and independent null-vector counting. It verifies the alternating integer cut relation for every induced four-cycle. The output recorded in `artifacts/verify_output.txt` ends in `VERIFY_OK`. This is a finite complete certificate for the explicit graph pair; the cut-spectrum and local-unitary arguments are separately given above.

## Relationship to prior work
Hein, Eisert and Briegel give the general graph-state entanglement/cut-rank correspondence. Van den Nest, Dehaene and De Moor establish the graph local-complementation/local-Clifford connection. Helwig discusses prime-dimensional graph states and their entanglement. Jafarizadeh, Eghbalifam and Nami examine entanglement and strongly regular graphs using a different continuous-variable harmonic-oscillator construction rather than the prime-dimensional graph states here. The rook graph is the line graph of the complete bipartite graph \(K_{4,4}\); a preexisting general line-graph cut-rank theorem can imply its standalone qudit cut ranks, which are not a new claim here. The established Shrikhande/rook graph construction and their common strongly regular parameters are classical. The present claim is the explicit **same-pair qubit equivalence together with uniform odd-prime local-unitary inequivalence through the exact four-site spectrum**, not the general cut-rank rule or the existence of two nonisomorphic strongly regular graphs.

## Limitations
The proof assumes all graph edges have unit phase weight and each local system has prime dimension. No analogous assertion is made for composite local dimension, arbitrary weighted edges, mixed graph-diagonal states, approximate convertibility, or conversion using entangling gates. Completeness of the finite verification concerns this named sixteen-vertex graph pair; it is not a classification of all strongly regular graph states. Historical priority cannot be settled by an incomplete bibliographic search and requires independent review, especially for specialized graph-state orbit tables.

## References
1. M. Hein, J. Eisert and H. J. Briegel, *Multi-party entanglement in graph states*, arXiv:quant-ph/0307130 (first public 2003-07-18), https://arxiv.org/abs/quant-ph/0307130.
2. M. Van den Nest, J. Dehaene and B. De Moor, *Graphical description of the action of local Clifford transformations on graph states*, arXiv:quant-ph/0308151 (first public 2003-08-27), https://arxiv.org/abs/quant-ph/0308151.
3. W. Helwig, *Absolutely Maximally Entangled Qudit Graph States*, arXiv:1306.2879 (first public 2013-06-12), https://arxiv.org/abs/1306.2879.
4. M. A. Jafarizadeh, F. Eghbalifam and S. Nami, *Investigation graph isomorphism problem via entanglement entropy in strongly regular graphs*, arXiv:1407.4041 (first public 2014-07-15), https://arxiv.org/abs/1407.4041.
5. A. E. Brouwer, *Shrikhande graph* (online graph reference), https://aeb.win.tue.nl/drg/graphs/Shrikhande.html.
