# Full equivariant Euler character of the \(K_{2,n}\) Morse complex
## Finding
For every integer \(n\ge3\), the equivariant reduced Euler characteristic of \(X_n=\mathcal M(K_{2,n})\) determines an exact virtual rational representation \(E_n=\sum_j(-1)^{j-n}[\widetilde H_j(X_n;\mathbb Q)]\) in the representation ring of the graph automorphism group. This unconditional statement does not require concentration of actual homology. Let \(U_n\subseteq\mathbb Q^n\) denote the \((n-1)\)-dimensional augmentation representation of \(S_n\), and \(\varepsilon_n\) its sign character. Let \(z\in S_2\) exchange the two degree-\(n\) vertices of the original graph. The decomposition of this virtual character into the two central-involution eigenspaces is
\[
\begin{aligned}
&E_n^{z=+1}\cong\varepsilon_n\otimes\operatorname{Sym}^2U_n,\\
&E_n^{z=-1}\cong\varepsilon_n\otimes(\bigwedge^2U_n\oplus U_n^{\oplus2})
\end{aligned}
\qquad\text{if }n\text{ is odd,}
\]
with the two right-hand sides interchanged when \(n\) is even. Consequently, assuming the previously established nonequivariant concentration in degree \(n\), the same identities describe the actual homology module \(\widetilde H_n(X_n;\mathbb Q)\). Regardless of that assumption, the virtual character on all elements of \(S_2\times S_n\) is determined. In particular, if \(\sigma\in S_n\) has \(f\) fixed points and \(t\) cycles of length two,
\[
\chi_n(1,\sigma)=\operatorname{sgn}(\sigma)(f^2-1),\qquad
\chi_n(z,\sigma)=(-1)^{n+1}\operatorname{sgn}(\sigma)(1-f+2t).
\]
The virtual dimension is \(n^2-1\). The earlier reported nonequivariant sphere-wedge homotopy type is not newly asserted or proved here.

## Assumptions and scope
The vertices of \(K_{2,n}\) are \(u,v,w_1,\ldots,w_n\), with every \(w_i\) joined to both \(u\) and \(v\). A simplex of \(X_n\) consists of primitive vertex-edge pairs, at most one pair incident as a cell to each vertex or edge, and contains no closed discrete gradient path. Equivalently, choose for each graph vertex at most one outgoing parent edge; the selected directed edges form a directed forest. An edge \(x\to y\) encodes the pair \((x,xy)\), and the parentless vertices are its roots. Since \(n\ge3\), the degrees distinguish the two bipartition classes and the natural automorphism group is exactly \(S_2\times S_n\). We work over \(\mathbb Q\), with ordinary (not generalized or pure) Morse complexes, and the action induced by permuting primitive vector-field pairs.

## Proof
**Unconditional virtual-character setup.** Define \(E_n=\sum_j(-1)^{j-n}[\widetilde H_j(X_n;\mathbb Q)]\) in the rational representation ring; this is well-defined without assuming any particular homology concentration. The signed simplicial Lefschetz formula computes its character exactly. A separately reported nonequivariant homotopy calculation claims \(X_n\simeq\bigvee^{n^2-1}S^n\) for \(n\ge2\). When that input is used, \(E_n\) is the genuine homology module \(\widetilde H_n(X_n;\mathbb Q)\); none of the virtual-character calculation requires this prior claim. Scoville--Zaremsky [1, §1] define the same Morse complex and prove an independent connectivity bound.

**Equivariant Euler calculation.** Fix \(g\in G_n\). A \(g\)-invariant directed forest comprises full \(g\)-orbits of primitive directed edges. Let \(k\) be the number of these edge-orbits. A fixed nonempty simplex with \(m\) vertices contributes \((-1)^{m-1}\) times the sign of the permutation of its \(m\) vertices, namely \((-1)^{k+1}\), to the reduced Lefschetz number; the empty simplex contributes \(-1\), again corresponding to \(k=0\). Therefore, writing \(P_g(-1)=\sum_F(-1)^{k(F)}\) over all \(g\)-invariant directed forests, the equivariant Euler characteristic yields unconditionally
\[
\chi_{E_n}(g)=(-1)^{n+1}P_g(-1).
\]
This identity includes the empty forest, so there is no missing degree-zero correction; it does not presume vanishing of other homology groups. To enumerate fixed forests, use the vertex orbits of \(g\): an equivariant choice of parent from an orbit of length \(\ell\) is valid precisely when the chosen parent is fixed by \(g^\ell\); cycles in the finite orbit quotient are forbidden. This quotient-cycle criterion is equivalent to forbidding directed cycles upstairs, since an orbit quotient cycle returns to the original vertex after finitely many turns.

**Permutations fixing the two distinguished vertices.** Take \(g=(1,\sigma)\), and let \(c\) be the total number of cycles of \(\sigma\), with \(f\) fixed points. A nontrivial right-hand cycle has three possible parent assignments: root, point to \(u\), or point to \(v\); their alternating total is \(1-1-1=-1\). Distinguished vertices cannot point toward a nonfixed orbit. The remaining fixed part is the directed rooted-forest enumeration of \(K_{2,f}\), evaluated at weight \(-1\) per selected directed edge. The matrix-forest determinant \(\det(I-L_{K_{2,f}})\) equals \((-1)^{f-1}(f^2-1)\) for \(f\ge1\), because the Laplacian eigenvalues are \(0,f+2,f\) and \(2\) repeated \(f-1\) times. For \(f=0\) the determinant and the interpreted formula both equal \(1\). Hence
\[
P_{(1,\sigma)}(-1)=(-1)^{c-1}(f^2-1).
\]
Since \(\operatorname{sgn}(\sigma)=(-1)^{n-c}\), the first character formula follows.

**Permutations exchanging the distinguished vertices.** Take \(g=(z,\sigma)\). The orbit \(\{u,v\}\) has length two. Among right-hand orbits, a fixed point may receive one parent arrow from the distinguished orbit, but cannot send an arrow back. For a two-cycle there are two choices of arrow in either direction, and a two-way directed orbit cycle is disallowed. Every even-length right cycle of length at least four may send an arrow toward the distinguished orbit with two choices, but not receive one. Every odd-length cycle of length at least three must be a root. Write \(t\) for the number of right two-cycles and \(e\) for the number of right cycles of even length at least four. Partition according to whether the distinguished orbit is a root, points to one of the \(f\) fixed right vertices, or points to one of the \(t\) right two-cycles. The respective alternating totals are \((-1)^{t+e}\), \(-f(-1)^{t+e}\), and \(2t(-1)^{t+e}\). Thus
\[
P_{(z,\sigma)}(-1)=(-1)^{t+e}(1-f+2t)
=\operatorname{sgn}(\sigma)(1-f+2t),
\]
proving the second formula.

**Representation identification.** The character of \(U_n\) at \(\sigma\) is \(f-1\), and at \(\sigma^2\) it is \(f+2t-1\). Therefore
\[
\chi_{\operatorname{Sym}^2U_n}=\frac{f^2-f+2t}{2},\qquad
\chi_{\bigwedge^2U_n\oplus U_n^{\oplus2}}=\frac{f^2+f-2t-2}{2}.
\]
Their sum is \(f^2-1\), their difference is \(1-f+2t\), and the parity factor in the swapped character places the two modules in the asserted \(z\)-eigenspaces. Because finite-dimensional rational representations of a finite group are semisimple and characters determine them, the stated identities hold in the rational representation ring for every \(n\ge3\). If actual homology is concentrated in degree \(n\), semisimplicity identifies the actual central-eigenspace modules.

## Verification
The embedded Python program `verify_representation.py` constructs independently all equivariant acyclic directed forests for every conjugacy class of \(S_n\), for both \(S_2\)-components, for every \(3\le n\le7\). For each of the \(82\) resulting pairs it computes the signed reduced Lefschetz trace directly and compares with both the closed polynomial and the symmetric/exterior-square character formulas. It additionally checks the identity character \(n^2-1\). The command `python3 verify_representation.py` completed with `VERIFY_OK` and a total of \(102{,}580\) invariant forests counted across the test instances. The uniform proof is the orbit-forest analysis above, not finite interpolation.

## Relationship to prior work
Scoville and Zaremsky [1] establish structural connectivity of ordinary graph Morse complexes; Lin and Scoville [3] identify the automorphism group of a graph Morse complex under explicit exceptions. Donovan and Scoville [2] compute nonequivariant homotopy types for extended stars and related examples. The separately established nonequivariant \(K_{2,n}\) wedge calculation gives dimension \(n^2-1\) but contains no action of \(S_2\times S_n\) on generators. The unconditional virtual character formulas and the conditional homology eigenspace decomposition are not consequences of the Betti number or abstract wedge type: distinct group representations share those invariants. This contribution concerns the full equivariant refinement, not a new computation of the underlying homotopy type.

## Limitations
The description is rational, not a classification of integral \(\mathbb Z[S_2\times S_n]\)-lattices or equivariant homotopy types. The virtual-character result is unconditional. The actual homology-module identification requires the previously reported nonequivariant homology concentration and checks its consistency on finite instances. Equivalence to an unindexed equivariant calculation remains a literature risk. The case \(n=2\) is excluded because its graph has additional automorphisms. Independent external audit has not been performed.

## References
1. Nicholas A. Scoville and Matthew C. B. Zaremsky, *Higher connectivity of the Morse complex*, first public April 22, 2020, arXiv:2004.10481, https://arxiv.org/abs/2004.10481.
2. Connor Donovan and Nicholas A. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, first public July 27, 2022, arXiv:2207.13780, https://arxiv.org/abs/2207.13780.
3. Maxwell Lin and Nicholas A. Scoville, *On the automorphism group of the Morse complex*, first public April 24, 2019, arXiv:1904.10907, https://arxiv.org/abs/1904.10907.
