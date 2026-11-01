# A parity-fractured Jordan law for vertex-deleted hypercube XOR dynamics

## Finding

For every integer \(d\ge 2\), let \(Q_d\) be the ordinary Boolean hypercube, delete any one vertex and all its incident edges, and let \(B_d\) be the resulting \((2^d-1)\)-square adjacency matrix over a finite field \(\mathbb F_q\) of characteristic two. Evolve a configuration synchronously by replacing each vertex value with the sum of the values at its surviving neighbors. Write \(N=2^d\). Then the **complete Jordan form** is

\[
 B_d\sim\begin{cases}
 J_3(0)\oplus J_2(0)^{\oplus(N/2-2)},&d\text{ even},\\
 J_1(0)\oplus J_2(1)^{\oplus(N/2-1)},&d\text{ odd}.
 \end{cases}
\]

Here \(J_r(\lambda)\) is the size-\(r\) Jordan block over \(\mathbb F_q\), and exponent zero means no corresponding blocks. In even dimensions, all trajectories become zero in at most **three** updates, and the time-three stratum has exactly \((q-1)q^{N-2}\) states. In odd dimensions, every state becomes fixed or period-two within **one** update; the proportion requiring that update is exactly \(1-1/q\). In neither case is the bound improvable uniformly over initial configurations.

The exact first-entry-time populations for even \(d\) are

\[
\begin{array}{c|cccc}
 t&0&1&2&3\\\hline
 \#\{x:T(x)=t\}&1&q^{N/2-1}-1&q^{N-2}-q^{N/2-1}&q^{N-1}-q^{N-2}.
\end{array}
\]

For odd \(d\), the first-entry-time populations are \(q^{N-2}\) at time zero and \(q^{N-1}-q^{N-2}\) at time one. In this case the number of fixed configurations is \(q^{N/2-1}\), and the number of distinct primitive two-cycles is

\[
 \frac{q^{N-2}-q^{N/2-1}}2.
\]

Among the configurations with first entry time one, exactly \((q-1)q^{N/2-1}\) enter a fixed point and \((q-1)(q^{N-2}-q^{N/2-1})\) enter a primitive two-cycle. For even \(d\) there is only one periodic configuration, zero. All formulas hold for every deleted vertex by graph vertex-transitivity.

## Assumptions and scope

The underlying graph is the **simple** \(d\)-cube on \(\{0,1\}^d\), adjacent at Hamming distance one; \(d\ge2\), exactly one entire vertex is removed, and every other vertex uses simultaneous **self-exclusive** neighbor sums over the same finite field \(\mathbb F_q\) with \(q=2^r\), \(r\ge1\). There is no forcing, self-feedback, stochastic update, or boundary closure. A state is periodic when \(B_d^{t+p}x=B_d^tx\) for some positive \(p\); \(T(x)\) is the least such nonnegative \(t\), and primitive period is the least \(p\) once periodic. Matrix similarity is over \(\mathbb F_q\), not an assertion about the ordinary real adjacency spectrum.

## Proof

**1. The ambient square-zero operator.** Write \(A\) for the full \(N\)-square adjacency matrix of \(Q_d\). If \(S_i\) toggles coordinate \(i\), then \(A=\sum_{i=1}^d S_i\). The \(S_i\) are commuting involutions, so in characteristic two

\[
 A^2=(d\bmod2)I_N.
\]

Put \(\varepsilon=d\bmod2\) as a field element and \(K=A+\varepsilon I_N\). Then \(K^2=0\). To determine its rank, partition the cube by the first coordinate, write \(H=A_{Q_{d-1}}\), and observe

\[
 K=\begin{pmatrix}C&I_{N/2}\\I_{N/2}&C\end{pmatrix},\qquad
 C=H+\varepsilon I_{N/2},\quad C^2=I_{N/2}.
\]

Thus \(K(x,y)=0\) exactly when \(x=Cy\); its nullity and rank both equal \(N/2\). This argument works over every characteristic-two field.

**2. Compression to the surviving vertices.** By translation symmetry, remove coordinate vertex \(u=0\). In blocks isolating that vertex, the original adjacency matrix has the form

\[
 A=\begin{pmatrix}0&w^{\mathsf T}\\w&B_d\end{pmatrix},
\]

where \(w\in\mathbb F_q^{N-1}\) is the nonzero indicator vector of the deleted vertex's \(d\) neighbors. Equating blocks in \(A^2=\varepsilon I_N\) gives the **exact identities**

\[
 w^{\mathsf T}w=\varepsilon,\qquad B_dw=0,\qquad
 B_d^2=\varepsilon I_{N-1}+ww^{\mathsf T}.
\]

An auxiliary compression-rank fact supplies the needed Jordan multiplicities. Write \(W=\{x:x_u=0\}\) inside the full vector space and \(\pi\) for deletion of the \(u\)-coordinate. Since \(K^2=0\) and \(\operatorname{rank}K=N/2\), \(\operatorname{im}K=\ker K\). This kernel contains a vector with nonzero \(u\)-coordinate: if \(\varepsilon=1\), take \(Ke_u\), whose \(u\)-coordinate is one; if \(\varepsilon=0\), take \(Ke_v\) for any neighbor \(v\) of \(u\), likewise with \(u\)-coordinate one. Therefore \(K(W)=\operatorname{im}K\). Also \(e_u\notin\operatorname{im}K=\ker K\), because \(Ke_u\ne0\). Hence \(\pi\) is injective on \(\operatorname{im}K\), and

\[
\operatorname{rank}(\pi K|_W)=N/2.
\]

When \(d\) is even this is \(\operatorname{rank}B_d=N/2\). When \(d\) is odd it is \(\operatorname{rank}(B_d+I_{N-1})=N/2\).

**3. Even dimensions.** With \(\varepsilon=0\), the block identities give \(B_d^2=ww^{\mathsf T}\ne0\) and \(B_d^3=0\). Consequently all Jordan blocks are nilpotent and have size at most three; exactly one has size three because \(\operatorname{rank}B_d^2=1\). Since \(\operatorname{rank}B_d=N/2\), exactly \(N/2-2\) size-two blocks remain, and their dimensions plus three total \(N-1\). No size-one block occurs. The kernel dimensions of the first three powers are therefore \(0\), \(N/2-1\), \(N-2\), and \(N-1\), with the time-zero kernel understood as \(\ker I=\{0\}\). Taking successive differences of the corresponding field-power populations proves the four first-entry counts.

**4. Odd dimensions.** With \(\varepsilon=1\), write \(P=B_d^2=I_{N-1}+ww^{\mathsf T}\). Since \(w^{\mathsf T}w=1\), \(P\) is an idempotent of rank \(N-2\), with kernel the line \(\mathbb F_qw\). Also \(B_dw=0\), and \(B_d^3=B_d\). Hence the space decomposes into a one-dimensional zero summand and a period-two summand \(\operatorname{im}P\) on which \(B_d^2=I\). On the latter, Jordan blocks of eigenvalue one have size at most two. The computed \(\operatorname{rank}(B_d+I)=N/2\) gives \(\dim\ker(B_d+I)=N/2-1\), while \(\dim\operatorname{im}P=N-2\). Thus there are exactly \(N/2-1\) size-two blocks at eigenvalue one and no size-one block there. The formulas for fixed points, period-two states, primitive two-cycles, and transient fibers follow by counting vectors in these invariant summands. More explicitly, every periodic configuration has exactly \(q\) preimages under \(B_d\), one already periodic and \(q-1\) strictly transient; preimages retain the eventual primitive period.

## Verification

The standalone `verify.py` computes adjacency, matrix products, and Gaussian-elimination ranks over the binary field for every dimension from \(2\) through \(8\), independently evaluates every configuration for \(d=2,3,4\) over the binary field and for \(d=2,3\) over the four-element field, and samples additional configurations in dimensions \(5\) through \(8\). The run covered 51,352 actual configurations. Its reproduced output is in `verification_output.txt` and ends with `PUNCTURED_HYPERCUBE_GF2_RANK_AND_STATE_CHECKS_PASSED`. The finite checks are **not** used in place of the all-dimensional proof; the proof above verifies the nonstandard compression-rank step and derives the complete invariant factors. The verifier needs only standard Python 3 and neither external dependencies nor data files.

## Relationship to prior work

Sutner's 2001 decomposition of finite additive cellular automata provides the established language of nilpotent/regular parts, primitive orbits, and exact rank-based state counts, but treats one-dimensional fixed and periodic boundaries, not a punctured hypercube. A 1996 finite-field linear hybrid automata study also provides context for matrix descriptions of linear updates. Kim, Reiner, and Schoenzeit's August 2026 treatment addresses the **same vertex-deleted graph**, but over the real numbers: their spectral eigenvalue/interlacing conclusions do not give the modular Jordan block sizes or finite-field transient populations, because reduction modulo two does not preserve an orthogonal real eigenbasis. Li, Wang, and Zhang (2024) study characteristic-two adjacency Jordan theory for graphs of uniform degree parity, whereas deleting one hypercube vertex produces a graph with mixed degree parity. Other parity automata on full hypercubes with distance-two edges concern a different adjacency operator.

The result therefore isolates a characteristic-two *vertex-failure* response: the unmodified even cube is square-zero, but deletion creates a genuine size-three nilpotent block; the unmodified odd cube is already an involution, but deletion introduces a one-step transient line. Neither difference follows from titles or from equal characteristic polynomials alone.

## Limitations

The statement concerns exactly one removed vertex, self-exclusive synchronous **linear** neighbor sums, and characteristic two. It does not assert independence from deletion of multiple vertices, an analogous classification over odd characteristic, or any stochastic perturbation law. Published real-spectral work addresses the same graph; the originality assessment is specifically for its characteristic-two Jordan and dynamical refinement, not for the underlying graph or the general linear-algebra method. No assertion of priority beyond the searched corpus or of independent certification is made.

## References

1. K. Cattell and J. C. Muzio, *Analysis of one-dimensional linear hybrid cellular automata over GF(q)*, IEEE Transactions on Computers **45** (1996), 782–792. DOI: https://doi.org/10.1109/12.508317.
2. K. Sutner, *Decomposition of Additive Cellular Automata*, Complex Systems **13** (2001), 245–270. https://www.complex-systems.com/abstracts/v13_i03_a04/ ; author-uploaded accessible full text: https://www.researchgate.net/publication/238213699_Decomposition_of_additive_cellular_automata .
3. J. S. Kim, V. Reiner, and L. Schoenzeit, *Note on adjacency spectra for twice punctured hypercubes*, arXiv:2608.27887 (2026), https://arxiv.org/abs/2608.27887 . The full document also analyzes singly punctured hypercubes over \(\mathbb R\).
4. K. Li, W. Wang, and H. Zhang, *Annihilating polynomial, Jordan canonical form, and generalized spectral characterizations of Eulerian graphs*, arXiv:2410.09833 (2024), https://arxiv.org/abs/2410.09833 .
