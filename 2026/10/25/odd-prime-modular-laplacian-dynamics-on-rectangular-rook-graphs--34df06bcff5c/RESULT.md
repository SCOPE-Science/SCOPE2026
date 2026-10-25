# Odd-prime modular Laplacian dynamics on rectangular rook graphs

## Finding

Fix an odd prime \(p\) and integers \(m,n\ge 2\). Let \(G=K_m\square K_n\) be the rectangular rook graph, whose vertices are cells \((i,j)\) and whose distinct cells are adjacent exactly when they share a row or a column. On configurations \(x\in\mathbb F_p^{mn}\), apply the graph Laplacian synchronously: \(F(x)=Lx\), where
\[
(Fx)_{ij}=(m+n)x_{ij}-\sum_{u=1}^m x_{uj}-\sum_{v=1}^n x_{iv}\pmod p.
\]
This is the standard degree-minus-adjacency Laplacian: each vertex has degree \(m+n-2\). A configuration has *transient depth* \(s\) if \(s\) is the least nonnegative integer for which \(F^s(x)\) is periodic. Its eventual period is the primitive period of that periodic configuration.

Put \(a=m\bmod p\), \(b=n\bmod p\), and \(N=mn\). The whole finite state diagram, at the resolution of transient depth and eventual primitive period, follows from the explicit formulae below. Let \(h\) be the dimension of the zero-primary subspace of \(L\), and let \(r_t\) be the rank of its \(t\)-th power restricted to that subspace, with \(r_0=h\). All possibilities are:
\[
\begin{array}{c|c|c|c|c|c}
\text{condition}&h&r_0&r_1&r_2&r_3\\\hline
 a\ne0,\ b\ne0,\ a+b\ne0&1&1&0&0&0\\
 a\ne0,\ b\ne0,\ a+b=0&1+(m-1)(n-1)&h&0&0&0\\
 a=0,\ b\ne0&m&m&1&0&0\\
 a\ne0,\ b=0&n&n&1&0&0\\
 a=b=0&mn&mn&m+n-2&1&0
\end{array}
\]
Here arithmetic conditions, including \(a+b\), are in \(\mathbb F_p\). In particular the sharp maximal transient depth \(\tau\) is respectively \(1,1,2,2,3\) in these five rows. The number of recurrent configurations is exactly \(p^{N-h}\), and the number with transient depth at most \(s\), for \(0\le s\le3\), is
\[
\boxed{C_s=p^{N-r_s}}.
\]
For \(s\ge1\), exactly \(C_s-C_{s-1}\) configurations have depth \(s\); \(C_0=p^{N-h}\). Every recurrent configuration has exactly \(p^h\) total initial-state preimages after convergence.

**Sharp extinction law.** All states eventually become zero if and only if \(p\mid m\) and \(p\mid n\). In that case \(F^3=0\), but \(F^2\ne0\), and exactly \(1-p^{-1}\) of all \(p^{mn}\) initial states require all three updates to reach zero. The proportion is independent of both graph sizes. Otherwise a nonzero periodic state always exists.

For the period census, define \(f_t=\dim\ker(L^t-I)\) for integers \(t\ge1\). Let \({\bf1}[P]\) be one if property \(P\) holds and zero otherwise. With \(a,b\) interpreted as nonzero field elements when required, define
\[
 f_t=
 \begin{cases}
 (m-1){\bf1}[a^t=1]+(n-1){\bf1}[b^t=1]+(m-1)(n-1){\bf1}[a+b\ne0\ \land\ (a+b)^t=1],&a,b\ne0,\\
 (n-1)\bigl(m-1+{\bf1}[p\mid t]\bigr){\bf1}[b^t=1],&a=0,\ b\ne0,\\
 (m-1)\bigl(n-1+{\bf1}[p\mid t]\bigr){\bf1}[a^t=1],&a\ne0,\ b=0,\\
 0,&a=b=0.
 \end{cases}
\]
Then exactly \(p^{f_t}\) configurations are fixed by \(F^t\); the number of configurations of **primitive** period \(t\) is
\[
\boxed{Q_t=\sum_{d\mid t}\mu(t/d)p^{f_d}},
\]
where \(\mu\) is the classical Möbius function. The number of distinct primitive \(t\)-cycles is \(Q_t/t\). Define \(H_0=1\) and \(H_s=p^{h-r_s}-p^{h-r_{s-1}}\) for \(s\ge1\). Then the exact joint census is
\[
\boxed{\#\{x:\text{depth}(x)=s,\ \text{period}(x)=t\}=H_sQ_t.}
\]
This formula also applies to \(s=0\). The permutation order on recurrent states is \(\operatorname{lcm}\) of \(\operatorname{ord}_p(a)\), \(\operatorname{ord}_p(b)\), and, when nonzero, \(\operatorname{ord}_p(a+b)\) if \(a,b\ne0\); it is \(p\operatorname{ord}_p(b)\) or \(p\operatorname{ord}_p(a)\) when exactly one residue is zero; and it is one when both residues are zero. Consequently \(F^{\tau+P}=F^\tau\), with both minimal global transient \(\tau\) and minimal eventual global period \(P\).

## Assumptions and scope

The prime \(p\) is odd, \(m,n\ge2\), and all states and graph Laplacian entries are reduced in the field \(\mathbb F_p\) before iteration. Edges are undirected and the graph is simple. Both dimensions refer to **labelled** row-column cells. Periodic states include the zero fixed state, while the depth of a periodic state is zero. The formulas are not about chip-firing, stabilization by sequential legal firings, probabilistic heat flow or integer Smith groups. No claim is made for composite residue rings or other graphs.

## Proof

Write \(J_m\) for the \(m\)-by-\(m\) all-ones matrix and similarly \(J_n\). With \(P=J_m\otimes I_n\) and \(Q=I_m\otimes J_n\), direct evaluation of the degree-minus-adjacency update gives
\[
L=(a+b)I-P-Q,\qquad P^2=aP,\quad Q^2=bQ,\quad PQ=QP=J_m\otimes J_n.
\]
These identities are valid in every \(\mathbb F_p\) and fix the sign and normalization of the operator.

**Both residues nonzero.** The rank-one matrix \(J_m\) is diagonalizable with eigenvalues \(a\) (multiplicity one, on the constants) and zero (multiplicity \(m-1\), on the sum-zero subspace). The same holds for \(J_n\). Tensor the respective eigenspaces. The spectrum of \(L\), with algebraic and geometric multiplicities, is exactly
\[
 0^{[1]},\quad a^{[m-1]},\quad b^{[n-1]},\quad (a+b)^{[(m-1)(n-1)]}.
\]
If \(a+b=0\), the last block joins the zero-primary space. All Jordan blocks have size one. Thus the first two rows of the rank table, the sharp depth one, and the first branch of \(f_t\) follow.

**Exactly one residue zero.** By symmetry let \(a=0\), \(b\ne0\). Decompose \(\mathbb F_p^n\) as its constant one-dimensional subspace and sum-zero \((n-1)\)-subspace. On \(\mathbb F_p^m\otimes\langle{\bf1}_n\rangle\), \(L=-J_m\), which has precisely one nilpotent Jordan block of size two and \(m-2\) nilpotent size-one blocks; hence zero-primary dimension \(m\), with nilpotent ranks \(m,1,0\). On \(\mathbb F_p^m\otimes\ker J_n\), the operator is \(bI-J_m\). Since \(J_m^2=0\) and \(J_m\ne0\), this component has nonzero eigenvalue \(b\), with exactly \(n-1\) Jordan blocks of size two and \((m-2)(n-1)\) additional size-one blocks. Raising a size-two \(b\)-Jordan block to the \(t\)-th power and subtracting the identity gives \((b^t-1)I+t b^{t-1}N\), where \(N\) is its nilpotent off-diagonal; it vanishes precisely when \(b^t=1\) and \(p\mid t\). This proves the second branch of \(f_t\), and also yields sharp transient two. The case \(b=0\), \(a\ne0\) follows by interchanging the coordinates.

**Both residues zero.** Here \(P^2=Q^2=0\) and \(L=-(P+Q)\). Since \(P,Q\) commute and \(p\) is odd,
\[
L^2=2PQ=2J_m\otimes J_n,\qquad L^3=0.
\]
The rank of \(L^2\) is one because \(2\ne0\) and the all-ones matrix is nonzero. For completeness, the image of \(L\) has dimension \(m+n-2\): taking row-sum and column-sum vectors \((r,c)\), they range over the codimension-one hyperplane \(\sum_i r_i=\sum_j c_j\), and \(L(x)_{ij}=-(r_i+c_j)\). The kernel of the map \((r,c)\mapsto(r_i+c_j)_{i,j}\) is the line \((r_i\equiv t,c_j\equiv-t)\). Because \(p\mid m,n\), this line lies in the indicated hyperplane. Therefore the rank is \((m+n-1)-1=m+n-2\). Thus \((r_0,r_1,r_2,r_3)=(mn,m+n-2,1,0)\), and the maximal depth is sharply three. Equivalently, its nilpotent Jordan blocks have one block of size three, \(m+n-4\) blocks of size two, and \((m-2)(n-2)+1\) blocks of size one.

**State census and primitive periods.** Any linear operator on a finite-dimensional vector space over a finite field has the canonical direct-sum decomposition into its zero-primary nilpotent subspace \(U\) and its invertible primary subspace \(W\), defined by the minimal polynomial. Every point of \(W\) is periodic because \(L|_W\) is invertible on a finite set, whereas an element with nonzero component in \(U\) is not periodic. The transient depth of \(u+w\) is the smallest \(s\) with \(L^s u=0\). Therefore the number of points with depth at most \(s\) is \(|\ker(L^s|_U)|\,|W|=p^{h-r_s}p^{N-h}=p^{N-r_s}\). The fibre over any fixed recurrent point after \(s\ge\tau\) has \(p^h\) members. For every positive \(t\), the zero-primary component contributes only its zero vector to \(\ker(L^t-I)\), while the primary block calculations above give exactly \(f_t\). Möbius inversion then supplies \(Q_t\). Multiplying a single periodic component by all nilpotent components of a given depth gives the joint formula \(H_sQ_t\).

Finally, on nonzero eigenvalues a scalar block has order \(\operatorname{ord}_p(\lambda)\). A nontrivial size-two Jordan block \(\lambda I+N\) over \(\mathbb F_p\), with \(p\) odd, has order \(p\operatorname{ord}_p(\lambda)\), as follows from the binomial formula \((\lambda I+N)^t=\lambda^tI+t\lambda^{t-1}N\) and \(N^2=0\). The above blocks attain each listed order, and every nilpotent block attains the stated sharp transient index. This proves all claims.

## Verification

`artifacts/verify_modular_rook_laplacian.py` constructs the literal graph Laplacian matrix independently of a row-column update formula and uses exact finite-field Gaussian elimination. It checked the predicted ranks of the first four powers for 147 triples \((p,m,n)\), with \(p\in\{3,5,7\}\) and \(2\le m,n\le8\). It checked \(\dim\ker(L^t-I)\) for 136 independent parameter-and-time cases, and it exhaustively enumerated 30,080 labelled initial states across six smaller instances, comparing transient depths and eventual primitive periods with the formulas. The original verifier and unaltered recorded output are embedded alongside the proof. These finite checks corroborate, but do not replace, the all-size algebraic proof.

## Relationship to prior work

Finite dynamical systems over finite fields and linearized-polynomial representations are classical, as in Moreno, Bollman and Aviño-Díaz (2006). Ducey, Gerhard and Watson (first public preprint July 2015) compute Smith and critical groups for square rook graphs, and describe earlier rectangular rook-graph Smith-group computations. Those are invariants of the integer Laplacian under **two-sided** row-column equivalence, not its powers under similarity, and hence do not themselves determine modular transient depths, Jordan blocks or primitive-period counts. The present classification fixes a different dynamical question and covers arbitrary rectangular dimensions and every odd prime. Peeters (2002), Theorem 3.4, computes ranks of powers of a shifted adjacency matrix for equal-size Hamming graphs \(H(d,q)\) with \(p\mid q\); in dimension two this **already covers the square divisible-by-\(p\) rank-power subcase** of the displayed three-step nilpotency. The claimed new scope is the uniform **rectangular** \((m,n)\) classification, including unequal sizes and all one-divisible and nonzero-residue phase regimes, with explicit period/depth multiplicities. Known binary parity dynamics on Cartesian products do not imply the odd-characteristic Jordan blocks of these regimes. Published modular Laurent-polynomial replication identities concern translation-invariant lattice rules and do not supply this finite complete-product orbit census.

## Limitations

The displayed formulas follow from elementary finite-dimensional algebra after exploiting the graph's unusually strong row-column symmetry. No general extension to arbitrary graphs, composite moduli, nonlinear rules or noisy updates is proved. A classification of this form could conceivably be implicit in historical graph-Laplacian or finite-automaton literature not located in the searches. Peeters' square Hamming-graph power ranks mean the divisible square extinction subcase is not presented as separately original. The 1991 rectangular rook-graph critical-group work and early modular spectral theses were not separately read in full; their exact similarity-theoretic consequences therefore remain an overlap risk. Verification uses finite examples only; the infinite-family assertion rests on the algebraic proof above. This is not an independently audited result.

## References

1. O. Moreno, D. Bollman, M. A. Aviño-Díaz, *Finite Dynamical Systems, Linear Automata, and Finite Fields*, arXiv:math/0604534v1, first public 2006-04-25, https://arxiv.org/abs/math/0604534.
2. J. E. Ducey, J. Gerhard, N. Watson, *The Smith and Critical Groups of the Square Rook's Graph and its Complement*, arXiv:1507.06583v1, first public 2015-07-23, https://arxiv.org/abs/1507.06583.
3. E. A. Delgado-Eckert, *Boolean Monomial Dynamical Systems*, arXiv:math/0403166v1 (2004), https://arxiv.org/abs/math/0403166.
4. R. Peeters, *On the p-Ranks of the Adjacency Matrices of Distance-Regular Graphs*, Journal of Algebraic Combinatorics 15 (2002), 127–149, Theorem 3.4; DOI:10.1023/A:1013842904024.
5. D. Lorenzini, *A finite group attached to the Laplacian of a graph*, Discrete Mathematics 91 (1991), 277–282; see the historical discussion in reference 2.
