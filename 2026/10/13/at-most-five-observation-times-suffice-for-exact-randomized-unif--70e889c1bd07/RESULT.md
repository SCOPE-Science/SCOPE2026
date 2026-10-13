# At most five observation times suffice for exact randomized uniform mixing on the eight-cycle

## Finding

Let \(C_8\) denote the simple unweighted cycle on eight vertices, let \(A\) be its adjacency matrix, and let \(M(t)\) be the entrywise squared modulus of \(U(t)=\exp(itA)\). For **every real \(T\geq 0\)**, there exist an integer \(1\leq k\leq5\), distinct times \(t_1,\ldots,t_k>T\), and strictly positive weights \(w_1,\ldots,w_k\), with \(\sum_j w_j=1\), such that

\[
\sum_{j=1}^{k}w_j M(t_j)=\frac18 J_8.
\]

Thus one common randomized observation time gives exactly uniform transition probabilities between every ordered pair of cycle vertices, using no more than five sampling times. In contrast, neither any single observation time nor the usual infinite-time Cesàro average produces uniform mixing on \(C_8\).

## Assumptions and scope

The Hamiltonian is exactly the adjacency matrix of the undirected simple eight-cycle: no loops, edge weights, magnetic phases, decoherence, or change of Hamiltonian. The time parameter is nonnegative and the same law is used for all starting vertices. The expectation is classical randomization of the observation time of the **same** coherent walk, not averaging over altered Hamiltonians or random walk trajectories. The theorem permits arbitrary positive lower cutoffs \(T\) and asserts **existence**, not an explicit algebraic list of physical sampling times or a minimum possible support size.

## Proof

**1. Spectral reduction.** Label the vertices by \(\mathbb Z/8\mathbb Z\). The adjacency eigenvalues, with multiplicities, are \(2\) (one), \(\sqrt2\) (two), \(0\) (two), \(-\sqrt2\) (two), and \(-2\) (one). Write

\[
\alpha=2t,\quad\beta=\sqrt2t,\quad X=\cos\alpha,\quad Y=\sin\alpha,\quad C=\cos\beta,\quad D=\sin\beta.
\]

Fourier diagonalization of the cycle yields the following transition amplitudes \(u_d\), where \(d\) is a cycle distance from zero through four:

\[
\begin{aligned}
u_0&=(X+1+2C)/4, &u_1&=i(Y+\sqrt2D)/4,\\
u_2&=(X-1)/4, &u_3&=i(Y-\sqrt2D)/4,\\
u_4&=(X+1-2C)/4.
\end{aligned}
\]

Consequently the five transition-probability classes are \(p_d=|u_d|^2\). Every row of \(M(t)\) has the same distance-class profile, and the pointwise normalization is

\[
p_0+2p_1+2p_2+2p_3+p_4=1.
\]

**2. Construct a full-support torus law with exact uniform moments.** Regard \(\alpha\) and \(\beta\) for the moment as independent angles modulo \(2\pi\), with the joint density

\[
f(\alpha,\beta)=\frac{(1-\tfrac12\cos\alpha)(1-\cos(2\beta))}{(2\pi)^2}.
\]

This is nonnegative, integrates to one, and has full topological support on the two-torus: its second factor vanishes only at two isolated angles. Elementary Fourier orthogonality gives

\[
\begin{aligned}
\mathbb E X&=-1/4,&\mathbb E X^2&=1/2,&\mathbb E Y&=0,&\mathbb E Y^2&=1/2,\\
\mathbb E C&=0,&\mathbb E C^2&=1/4,&\mathbb E D&=0,&\mathbb E D^2&=3/4.
\end{aligned}
\]

Independence kills all mixed first-moment terms. The distance-zero and distance-four means both equal

\[
\frac{\mathbb E X^2+2\mathbb E X+1+4\mathbb E C^2}{16}
=\frac{1/2-1/2+1+1}{16}=\frac18.
\]

For the remaining distances,

\[
\mathbb E p_2=\frac{\mathbb E X^2-2\mathbb E X+1}{16}=\frac18,
\quad
\mathbb E p_1=\mathbb E p_3=\frac{\mathbb E Y^2+2\mathbb E D^2}{16}=\frac18.
\]

Hence the expectation over this abstract two-torus of the eight-by-eight mixing matrix is exactly \(J_8/8\).

**3. Replace abstract phases by exact physical times.** Let \(F\) map the two-torus to the real five-vector \((p_0,p_1,p_2,p_3,p_4)\), and set \(b=(1/8,1/8,1/8,1/8,1/8)\). The full-support law in step 2 implies

\[
b\in\operatorname{relint}\bigl(\operatorname{conv}F(\mathbb T^2)\bigr).
\]

Indeed, if a proper supporting hyperplane of that compact convex set passed through \(b\), its affine functional would take a one-sided value on the full image and would have zero average deviation from its supporting value. Since this deviation is continuous and the torus law has full support, it would vanish everywhere. Such a hyperplane would then contain the entire affine hull, contradicting proper support.

The two frequencies \(2\) and \(\sqrt2\) are rationally independent. Continuous-time Kronecker density therefore implies that for **every** \(T\ge0\),

\[
\{(2t,\sqrt2t)\bmod2\pi:t>T\}
\]

is dense in \(\mathbb T^2\). We use the elementary convex-density principle: when \(S\) is dense in a compact subset \(K\) of a finite-dimensional affine space, \(\operatorname{relint}(\operatorname{conv}K)\subseteq\operatorname{conv}S\). To see it, enclose a relative-interior point in a finite polytope made of points of \(K\) with a small relative neighborhood of the point inside that polytope; sufficiently close replacements of its finitely many vertices by points of \(S\) still enclose the point. Apply the principle to the tail-time image of \(F\). It follows that \(b\) is **exactly** a finite convex combination of vectors \(F(2t,\sqrt2t)\) with \(t>T\), not merely a limit of approximate combinations.

Finally, all these vectors lie in the affine hyperplane \(p_0+2p_1+2p_2+2p_3+p_4=1\), of dimension at most four. Carathéodory's theorem thus permits a convex combination of at most **five** actual tail-time vectors. Remove zero weights and coalesce any repeated times. Since all entries of the mixing matrix are determined by these five distance classes, the asserted full matrix equality follows.

**4. Contrasts with conventional mixing.** If a single time had uniform mixing, \(p_2=1/8\) would force \(X=1-\sqrt2\). Equality \(p_0=p_4\) would then force \(C=0\) because \(X+1=2-\sqrt2\neq0\). But this gives \(p_0=(2-\sqrt2)^2/16\neq1/8\). Thus instantaneous uniform mixing is impossible. Under ordinary uniform-in-time Cesàro averaging, \(\mathbb E X=0\) and \(\mathbb E X^2=1/2\), so \(\overline p_2=3/32\neq1/8\), proving failure of conventional average uniformity.

## Verification

The bundled standalone `verify.py` reconstructs the five exact spectral projectors over \(\mathbb Q(\sqrt2)\), checks their completeness, orthogonality, idempotence, and eigenvalue identities, and evaluates all five weighted moment expressions using exact rational arithmetic. It separately compares 256 complex matrix-exponential entries computed by Taylor series with the independent spectral formulas at four observation times. Run `python3 verify.py` with standard Python 3; its successful output is documented in `VERIFICATION.md`. These checks corroborate explicitly specified calculations; the full-support convexity, Kronecker density, and Carathéodory arguments are mathematical proofs of the unrestricted time-existence claim, not conclusions from finite numerical sampling.

## Relationship to prior work

Baptista, Coutinho, and Marques (2023) introduce averages of mixing matrices over general observation-time distributions and give exact uniform examples for the paths on three and four vertices. Their full preprint does not give the present exact five-time construction for the unweighted eight-cycle. Adamczak and collaborators (2007) prove nonuniformity phenomena for cycles under instantaneous or ordinary long-time Cesàro mixing; those statements are compatible with the different distribution optimized here. The distinction between an arbitrary sampling law and uniform-in-time averaging is essential. This result is a specifically eight-cycle existence theorem, not a classification of all even cycles.

## Limitations

The sampling times are obtained nonconstructively from density and convex geometry, and no bound on their magnitudes or separation is derived beyond the ability to choose them after any prescribed cutoff. Five is an upper bound on the number of time atoms, not a proven optimal minimum. The argument does not classify other cycles, Cartesian products, perturbed cycles, or alternative Hamiltonians. An equivalent unpublished or differently formulated convex spectral mixing construction may exist; no global novelty guarantee is claimed. No independent external audit or experimental realization is claimed.

## References

1. P. Baptista, G. Coutinho, V. Marques, *Unexpected Averages of Mixing Matrices*, arXiv:2308.16378, first public preprint 2023-08-31, https://arxiv.org/abs/2308.16378 (full preprint https://arxiv.org/pdf/2308.16378).
2. W. Adamczak, K. Andrew, L. Bergen, D. Ethier, P. Hernberg, J. Lin, C. Tamon, *Non-uniform mixing of quantum walk on cycles*, arXiv:0708.2096, https://arxiv.org/abs/0708.2096 (full preprint https://arxiv.org/pdf/0708.2096).
3. G. Coutinho, K. Guo, *Selected Open Problems in Continuous-Time Quantum Walks*, arXiv:2404.02236, https://arxiv.org/abs/2404.02236.
