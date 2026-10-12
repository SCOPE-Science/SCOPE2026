# Exact shared-clock randomized uniform quantum mixing on the \(3\times4\) path grid

## Finding

**Theorem.** Let \(P_n\) denote the unweighted path on \(n\) vertices, and let \(G=P_3\square P_4\), whose twelve vertices are the pairs \((i,j)\) with \(1\le i\le3\) and \(1\le j\le4\). Write \(A=A(G)\) and
\[
U(t)=\exp(itA),\qquad M(t)=U(t)\circ\overline{U(t)},\quad t\ge0,
\]
where \(\circ\) is entrywise multiplication. There exist \(k\le15\), nonnegative real times \(t_1,\ldots,t_k\), and nonnegative weights \(w_1,\ldots,w_k\) satisfying \(\sum_{j=1}^k w_j=1\) and
\[
\sum_{j=1}^k w_jM(t_j)=\frac1{12}J_{12}.
\]
Thus a **single shared random observation time** gives exact uniform expected mixing on this twelve-vertex Cartesian grid. In particular, the observation-time distribution may be chosen with finite support of size at most fifteen.

## Assumptions and scope

Every graph is finite, simple, undirected, unweighted, and uses the ordinary adjacency Hamiltonian. The Cartesian product is the graph with adjacency \(A=A_3\otimes I_4+I_3\otimes A_4\), with \(A_n=A(P_n)\). The same time \(t\) is applied to both factors, rather than sampling independent times for each. A probability distribution supported on finitely many real times is allowed; no restrictions on the magnitudes of those times are imposed.

For the spectral proof, put
\[
\alpha=\frac{1+\sqrt5}{2},\qquad\beta=\frac{1-\sqrt5}{2}.
\]
The eigenvalues of \(A_3\) are \(\{\sqrt2,0,-\sqrt2\}\), and those of \(A_4\) are \(\{\alpha,\beta,-\alpha,-\beta\}\). Here \(J_n\) is the \(n\times n\) matrix of ones.

## Proof

**1. Spectral mixing and product phases.** If a real symmetric adjacency matrix has distinct eigenvalues \(\lambda\) and spectral projectors \(E_\lambda\), then
\[
M(t)=\sum_{\lambda,\mu}e^{it(\lambda-\mu)}
(E_\lambda\circ E_\mu).
\]
Each projector can be reconstructed without a numerical eigenvector choice by
\[
E_\lambda=\prod_{\mu\ne\lambda}\frac{A-\mu I}{\lambda-\mu}.
\]
Because \(A=A_3\otimes I_4+I_3\otimes A_4\), exponentiation and entrywise modulus yield
\[
M_G(t)=M_3(t)\otimes M_4(t).
\]
Writing \(\theta=\sqrt2t\), \(\phi=\alpha t\), and \(\psi=\beta t\) modulo \(2\pi\), the first factor's matrix depends only on \(\cos\theta\) and \(\cos(2\theta)\). The second depends only on
\[
\cos(2\phi),\ \cos(2\psi),\ \cos(\phi+\psi),\ \cos(\phi-\psi).
\]
Indeed its distinct positive spectral gaps are \(2\alpha\), \(-2\beta\), \(\alpha+\beta=1\), and \(\alpha-\beta=\sqrt5\).

**2. Strictly positive torus densities.** Let \(m_1\) and \(m_2\) be normalized Haar measures on the circle and on the two-torus, respectively. On these spaces prescribe the probability densities
\[
f_3(\theta)=1-\frac23\cos(2\theta),\qquad
f_4(\phi,\psi)=1-\frac12\cos(\phi-\psi).
\]
They are normalized by Fourier orthogonality and satisfy \(f_3\ge1/3\), \(f_4\ge1/2\) everywhere. For \(f_3m_1\), the moments are
\[
\mathbb E\cos\theta=0,\qquad\mathbb E\cos(2\theta)=-\frac13.
\]
For \(f_4m_2\), the four moments in the displayed order in Step 1 are
\[
0,\quad0,\quad0,\quad-\frac14.
\]
(The vanishing of sine moments follows from the same orthogonality, or from evenness under simultaneous phase reversal.) Substituting these moments in the displayed spectral-projector formula and using the explicit projector products gives the two **exact** identities
\[
\int_{\mathbb T}M_3(\theta)f_3(\theta)\,dm_1(\theta)=\frac13J_3,\qquad
\int_{\mathbb T^2}M_4(\phi,\psi)f_4(\phi,\psi)\,dm_2(\phi,\psi)=\frac14J_4.
\]
Here \(M_3(\theta)\) denotes the spectral-phase form of the first mixing matrix and similarly for \(M_4\). For a direct exact arithmetic check, the companion `verify.py` constructs these projectors using the finite products from Step 1, and verifies every entry of both identities over \(\mathbb Q(\sqrt2,\sqrt5)\).

Let \(F(\theta,\phi,\psi)=M_3(\theta)\otimes M_4(\phi,\psi)\). Taking the product of the two strictly positive densities yields
\[
\int_{\mathbb T^3}F(\theta,\phi,\psi)
 f_3(\theta)f_4(\phi,\psi)\,dm_3(\theta,\phi,\psi)
 =\frac1{12}J_{12}.
\]

**3. The same-clock phase orbit is dense.** The real numbers \(\sqrt2,\alpha,\beta\) are linearly independent over \(\mathbb Q\). Indeed any integer relation becomes a rational relation among \(1,\sqrt2,\sqrt5\), which has only the zero solution. Kronecker's theorem for continuous one-parameter flows implies that the forward orbit
\[
t\longmapsto(\sqrt2t,\alpha t,\beta t)\pmod{2\pi},\qquad t\ge0,
\]
is dense in \(\mathbb T^3\). The restriction \(t\ge0\) does not change its closure: the closure of a positive semiorbit in a compact torus group contains its inverses by recurrent positive returns.

**4. From a full-support torus average to an exact finite-time average.** We spell out the finite-dimensional convexity step, since dense orbits alone give only approximation. Let \(K=F(\mathbb T^3)\), a compact subset of the space of real \(12\times12\) matrices, and let \(B=J_{12}/12\). The strictly positive continuous density in Step 2 implies
\[
B\in\operatorname{relint}\operatorname{conv}K.
\]
To prove this, if \(B\) lay on a proper relative supporting hyperplane, some nonconstant affine functional \(L\) would satisfy \(L(X)\le L(B)\) on \(K\); integration against the full-support density forces \(L(X)=L(B)\) everywhere on \(K\), contradicting proper support. Now a dense subset \(D\subseteq K\) has the property \(\operatorname{relint}\operatorname{conv}K\subseteq\operatorname{conv}D\): take finitely many vertices of a small full-dimensional polytope around \(B\) inside \(\operatorname{conv}K\). Express each of these vertices as a finite convex combination of points of \(K\), then approximate all the points of \(K\) in those combinations by points of \(D\); strict interior containment of \(B\) in the resulting finite convex hull persists under sufficiently small perturbations. Take \(D=\{M_G(t):t\ge0\}\) using Step 3. Consequently \(B\) is an **exact finite convex combination of physical mixing matrices**.

**5. Bound the number of observation times.** By Step 1 the factor curves lie in real linear spaces of dimension at most three and five, respectively (constant matrix and the listed cosine coefficient matrices). Thus all \(M_G(t)\) lie in a tensor-product linear space of dimension at most \(3\cdot5=15\). Every such mixing matrix is stochastic; applying the nonzero linear functional \(X\mapsto\sum_{i,j}X_{ij}\) gives the constant \(12\), so their affine dimension is at most fourteen. Carathéodory's theorem therefore expresses \(B\) as a convex combination of **at most fifteen** actual matrices \(M_G(t_j)\), completing the proof. \(\square\)

## Verification

Running `python verify.py` checks in exact SymPy arithmetic the seven factor spectral idempotents, all factor row entries, and all 144 entries of the uniform product average. Running `python verify.py --numerical` additionally checks the Cartesian full-matrix exponential identity at five times and finds a 15-support **approximate** 300-sampled-time linear-programming witness (matrix residual below \(10^{-8}\)); the numerical witness is not presented as an exact certificate. The argument establishing **exact** support on physical times is Steps 3–5, not the finite linear program.

## Relationship to prior work

Baptista, Coutinho, and Marques introduced arbitrary observation-time distributions for adjacency quantum walks. Their 2023 work explicitly proves separate uniform averaged mixing for \(P_3\) and \(P_4\) (Sections 3.2 and 4.3), and emphasizes in Section 5 that a Cartesian product's averaged mixing matrix need not equal the product of the individually averaged mixing matrices because the two factors use the **same time**. Their Cartesian-product results concern covariance and traces; they do not present an exact uniform-mixing law for \(P_3\square P_4\). This theorem addresses precisely that shared-time gap with an arithmetic-independence and strict-positivity argument.

The quantum-walk survey of Coutinho and Guo (2024) describes generalized averages and related open questions but does not give the present shared-clock twelve-vertex construction. Classical long-time Cesàro mixing and instantaneous mixing are different quantities and do not decide existence of tailored finite observation-time distributions. Literature and prior-record comparison cannot exclude every unindexed equivalent proof.

## Limitations

The fifteen exact observation times and weights are established **existentially**; this result supplies neither closed-form times nor an upper bound on the latest observation time. The torus densities are auxiliary mathematical devices, not sampling distributions of an unconstrained set of independently controlled quantum systems. Their exact realization by shared physical time requires the Kronecker and convexity argument. No instantaneous uniform mixing, minimal number of times, or classification of other path products is asserted. Any finite computed witness is supplementary and does not prove the exact statement. Exhaustive literature uniqueness and independent external validation have not been established.

## References

1. Pedro Baptista, Gabriel Coutinho, and Vitor Marques, *Unexpected Averages of Mixing Matrices*, arXiv:2308.16378v1, first public 2023-08-31, Sections 3.2, 4.3, 5, 7. https://arxiv.org/html/2308.16378v1
2. Gabriel Coutinho and Krystal Guo, *Selected Open Problems in Continuous-Time Quantum Walks*, arXiv:2404.02236v1, 2024, Section on generalized average mixing. https://arxiv.org/abs/2404.02236
3. Peter Lo and collaborators, *Mixing of Quantum Walk on Circulant Bunkbeds*, arXiv:quant-ph/0509059, 2005, Section 5 (different graph class and averaging notion). https://arxiv.org/abs/quant-ph/0509059
