# A mod-four orbit census for parity automata on distance-two Boolean cubes

## Finding
Let \(n\ge2\) be an integer, let \(G_n=\mathbb F_2^n\), and let \(X_n=\mathbb F_2^{G_n}\) be the state space of binary labelings of the Boolean cube. Define the synchronous distance-two parity automaton
\[
(F_nx)(v)=\sum_{\substack{u\in G_n\\\operatorname{wt}(u-v)=2}}x(u)\pmod2,
\qquad v\in G_n.
\]
The sum is over exactly the \(\binom n2\) vertices at Hamming distance two, with no self-input. Put
\[
M_n=2^n,\qquad
c_n=\binom n2\bmod2,\qquad
r_n=\begin{cases}
2^{n-1},&n\text{ even},\\
2^{n-1}-2^{(n-1)/2},&n\text{ odd}.
\end{cases}
\]
Then, as \(\mathbb F_2\)-linear maps on \(X_n\),
\[
\boxed{(F_n+c_nI)^2=0,\qquad \operatorname{rank}_{\mathbb F_2}(F_n+c_nI)=r_n.}
\]
In particular the entire functional graph, consisting of \(2^{M_n}\) states, is determined exactly:

When \(n\equiv0,1\pmod4\), the map satisfies \(F_n^2=0\). Its only periodic state is zero; exactly \(2^{M_n-r_n}\) states reach zero in at most one update, and the remaining \(2^{M_n}-2^{M_n-r_n}\) states reach it for the first time at the second update. The former class includes the initially zero state, so the numbers of states with **first hitting times** zero, one, and two are respectively \(1\), \(2^{M_n-r_n}-1\), and \(2^{M_n}-2^{M_n-r_n}\).

When \(n\equiv2,3\pmod4\), the map satisfies \(F_n^2=I\). Exactly \(2^{M_n-r_n}\) states are fixed, and there are exactly
\[
\boxed{\frac{2^{M_n}-2^{M_n-r_n}}{2}}
\]
primitive two-cycles. All trajectories are periodic from the outset; no period greater than two occurs. The result is for every cube dimension, with no cutoff on the state support.

## Assumptions and scope
All sums and ranks in the orbit classification are in characteristic two. Vertex labels are elements of the \(n\)-dimensional vector space \(G_n\); configurations are functions on its \(2^n\) vertices. Hamming weight \(\operatorname{wt}(v)\) is the number of nonzero coordinates. There is no affine forcing, no asynchronous update, and no interaction at Hamming distances other than two. The graph has two parity components, but the theorem classifies the combined full-state dynamics without choosing a component.

## Proof
**Step 1: convert the update to multiplication in a group algebra.** The translation operators \(t_i\) on configurations toggle the \(i\)-th vertex coordinate. They commute, satisfy \(t_i^2=I\), and the update operator is
\[
F_n=\sum_{1\le i<j\le n}t_it_j.
\]
Identify the group algebra \(\mathbb F_2[G_n]\) with the finite-dimensional algebra
\[
R_n=\mathbb F_2[y_1,\ldots,y_n]/(y_1^2,\ldots,y_n^2),
\quad y_i=1+t_i.
\]
The regular representation identifies \(X_n\) with \(R_n\) as a vector space, and the adjacency update with multiplication by its group-algebra element. Since \(t_i=1+y_i\), writing \(e_1=\sum_i y_i\) and \(e_2=\sum_{i<j}y_iy_j\), one obtains
\[
F_n=c_nI+\big((n-1)\bmod2\big)e_1+e_2.
\]
Call the positive-degree part \(N_n=F_n+c_nI\). For every \(z\) of positive degree in \(R_n\), the characteristic-two Frobenius identity and \(y_i^2=0\) imply \(z^2=0\). In particular multiplication by \(N_n\) squares to zero. This establishes the first assertion. Independently, two successive distance-two updates have coefficient \(\binom n2\) at displacement of weight zero, \(2(n-2)\) at weight two, \(6\) at weight four, and zero at all other weights. All off-diagonal coefficients are even, verifying \(F_n^2=c_nI\) by direct path counting.

**Step 2: calculate the rank in even dimension.** If \(n\) is even, then \(N_n=e_1+e_2\). Separate the first variable and write
\[
N_n=(1+s)y_1+p,
\quad s=\sum_{j=2}^n y_j,
\quad p=\sum_{j=2}^n y_j+\sum_{2\le i<j\le n}y_iy_j.
\]
Because \(s^2=0\), the element \(1+s\) is a unit with inverse \(1+s\). The generator substitution \(z_1=N_n\), \(z_j=y_j\) for \(j\ge2\) is invertible, with explicit inverse \(y_1=(z_1+p)(1+s)\). Hence multiplication by \(N_n\) is similar to multiplication by a coordinate generator \(z_1\) in a square-zero polynomial algebra. The latter has image spanned by exactly the \(2^{n-1}\) squarefree monomials containing \(z_1\), proving \(r_n=2^{n-1}\).

**Step 3: calculate the rank in odd dimension.** If \(n=2m+1\) is odd, then \(N_n=e_2\). As a quadratic element in the square-zero algebra, its alternating coefficient matrix \(B\) has entries \(B_{ij}=1\) for \(i\ne j\) and \(B_{ii}=0\), so \(B=J+I\) over \(\mathbb F_2\). For odd \(n\), \(\ker B\) is the one-dimensional span of the all-ones vector: the equation \(Bv=0\) forces every coordinate of \(v\) to equal \(\sum_j v_j\). Thus \(\operatorname{rank}B=2m\). The standard alternating-form normal form supplies invertible linear generators \(u_1,v_1,\ldots,u_m,v_m,w\) with
\[
N_n=\sum_{j=1}^{m}u_jv_j.
\]
Linear generator changes are algebra automorphisms because every linear combination of the original square-zero generators also squares to zero.

View multiplication by \(N_n\) as a differential \(d\) on \(R_n\), so \(d^2=0\). The normal form decomposes this complex as the tensor product of \(m\) four-dimensional complexes \(B_j=\mathbb F_2[u_j,v_j]/(u_j^2,v_j^2)\) and the two-dimensional zero-differential complex \(\mathbb F_2[w]/(w^2)\). On \(B_j\), multiplication by \(u_jv_j\) sends \(1\) to \(u_jv_j\) and kills \(u_j,v_j,u_jv_j\), leaving a two-dimensional homology. The tensor differential is the sum of these individual multiplications (signs vanish in characteristic two). Künneth over the field \(\mathbb F_2\) therefore gives
\[
\dim H(R_n,d)=2^m\cdot2=2^{m+1}.
\]
For any square-zero endomorphism on an \(M_n\)-dimensional vector space, rank-nullity yields \(\dim H=M_n-2\operatorname{rank}d\). Consequently
\[
r_n=\frac{2^{2m+1}-2^{m+1}}2=2^{n-1}-2^m,
\]
as claimed. This computation holds for every odd \(n\ge3\), not just the finite dimensions used in verification.

**Step 4: count orbits and transients.** The parity of \(\binom n2\) is zero for \(n\equiv0,1\pmod4\), and one for \(n\equiv2,3\pmod4\). In the first case \(F_n=N_n\) is square-zero. Its kernel has dimension \(M_n-r_n\), and it is the full set of states reaching zero after one application. Every state reaches zero after at most two updates, giving the three exact hitting-time counts. In the second case \(F_n=I+N_n\), so \(F_n^2=I\). A state is fixed exactly when it belongs to \(\ker N_n\), also of dimension \(M_n-r_n\). Every other state lies in a primitive pair, giving the cycle count. This exhausts all possible trajectories.

## Verification
The included `verification.py` builds the distance-two adjacency matrix directly from bit-flip masks, shifts it by the diagonal when the degree is odd, and performs exact Boolean Gaussian elimination. For dimensions \(2\) through \(10\) it verifies the derived rank and square-zero identity on every standard basis vector. For dimensions \(2\), \(3\), and \(4\) it additionally enumerates every binary configuration and independently checks the precise fixed-point/two-cycle or transient counts. A verified run prints:

`VERIFY_OK; assertions=67861`

This finite independent check corroborates the theorem; the unrestricted conclusion rests on the group-algebra, alternating-normal-form, and Künneth proof above.

## Relationship to prior work
Rollier and Baetens (2026) prove exact real tangent-space Lyapunov spectra for affine cellular automata and the parity rule on arbitrary graphs, with the adjacency matrix as the Boolean Jacobian. Their paper explicitly distinguishes real tangent multiplication from the modulo-two configuration dynamics. It does not give a Boolean temporal-cycle census or the rank of the shifted distance-two Hamming adjacency operator. The present result concerns the latter finite-field dynamics, and it does **not** claim a new real adjacency spectrum.

The binary distance-two Hamming graph and its neighborhood design are standard objects in Hamming association schemes. Key's 2010 survey slides explicitly define the general distance-\(k\) Hamming graphs and discuss codes from graph adjacency matrices, but the inspected adjacency-code formulas address the ordinary distance-one cube. They do not imply the shifted distance-two operator rank displayed here. Godsil's association-scheme notes supply the general Hamming-scheme setting, not an explicit temporal orbit census.

Related published mathematical research on positive-definite optimization over the weight-two Boolean shell concerns a distinct Turán extremum, while a modular-Laplacian parity reduction concerns time-varying modulus schedules on a spatial lattice. Neither statement implies the displayed orbit-count formulas or binary shifted adjacency ranks. Published descriptions and pertinent complete result texts were compared by their hypotheses and conclusions, not merely by title or vocabulary.

## Limitations
The parity automaton is specified by the **exact distance-two** neighborhood; conclusions do not cover an arbitrary graph, higher Hamming shells, or affine forcing. The formulas concern binary state evolution, not the real-valued Lyapunov exponents or stochastic damage spreading. The exceptional small case \(n=1\) has an empty neighborhood and is excluded by definition. Search and examination of the cited literature did not identify an equivalent all-dimensional formula, but an earlier coding-theoretic rank theorem or an alternate Hamming-scheme formulation remains a meaningful originality risk. No independent audit has been performed.

## References
1. M. Rollier and J. M. Baetens, *Exact Lyapunov spectra of affine cellular automata and the parity rule on networks*, arXiv:2606.14521v1, first publicly posted 2026-06-12. https://arxiv.org/abs/2606.14521
2. J. D. Key, *Linear codes from designs from Hamming graphs*, conference slides, 2010-04-13. https://www.algorithm.uni-bayreuth.de/en/research/alcoma2010/participants/talk_key.pdf
3. C. Godsil, *Association Schemes*, lecture notes, 2010. https://www.math.uwaterloo.ca/~cgodsil/pdfs/assoc2.pdf
4. *Sharp Turán constant and all extremizers for the weight-two Boolean Hamming shell*, published mathematical result (2026). https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-sharp-tur-n-constant-and-all-extremizers-for-the-weight-two-bool--e912a3cb52c4/RESULT.md
5. *Boundary-controlled parity reduction in modular Laplacian dynamics*, published mathematical result (2026). https://github.com/published-finding corpus/2026/blob/main/2026/9/19/SCOPE-boundary-parity-reduction-modular-laplacian--329faea3aeba/RESULT.md
