# Bipartite-component formula for the absorbing spectral rank of triangular quantum graphs

## Finding
Let \(n\ge5\), let \(T_n=J(n,2)=L(K_n)\), and place strictly positive absorbing rates on an arbitrary nonempty set \(F\subseteq E(K_n)\), regarded as vertices of \(T_n\). Write \(t=|F|\) and \(N=\binom n2\). Let \(b(G)\) count the connected components of a graph \(G\) that are bipartite, **including isolated vertices**. Define \(\varepsilon(F)=1\) if every bipartite component of \(([n],F)\) has equal-sized color classes, and \(\varepsilon(F)=0\) otherwise; nonbipartite components impose no condition. A graph with no bipartite components satisfies this condition vacuously.

For the adjacency-generated continuous-time quantum walk with arbitrarily strong *positive* loss at every vertex in \(F\), the dimension of the absorbing (bright) subspace is **exactly**
\[
\boxed{R(F)=n+t+1-b(([n],F))-b(([n],E(K_n)\setminus F))-\varepsilon(F).}
\]
The complementary, nondecaying (dark) subspace has dimension \(\binom n2-R(F)\). Starting from the maximally mixed one-excitation state, the eventual probability of absorption is \(R(F)/\binom n2\), independently of the individual positive loss rates. The formula is valid for **every** nonempty trap set, including disconnected, spanning, nearly complete, and complete trap sets.

A four-trap placement exposes a topological contrast. For \(n\ge7\), take four trap sites corresponding either to the four edges of a quadrilateral on four labels or to the three edges of a triangle and one incident pendant edge (again four labels). The respective bright dimensions are \(8\) and \(9\), despite identical trap counts and support sizes. Their mean absorption probabilities differ by exactly \(1/\binom n2\); an even cycle produces a surviving extra dark direction.

## Assumptions and scope
Write \(\mathcal E=\{\{i,j\}:1\le i<j\le n\}\) and give \(\mathbb C^{\mathcal E}\) its canonical orthonormal basis \(\{|e\rangle:e\in\mathcal E\}\). The adjacency matrix \(A\) of \(J(n,2)\) joins two distinct two-subsets when they meet in one label. For arbitrary \(\gamma_e>0\), \(e\in F\), define
\[
H_{\mathrm{eff}}=A-i\sum_{e\in F}\gamma_e|e\rangle\langle e|,
\qquad \psi(s)=e^{-isH_{\mathrm{eff}}}\psi(0),\quad s\ge0.
\]
Here \(\|\psi(s)\|^2\) is the probability that the excitation has not yet been absorbed. The absorbing subspace is the orthogonal complement of all eigenvectors of \(A\) that vanish at every trap vertex; its rank is the stated \(R(F)\). No claim is made about mean absorption times, decoherence, spatially varying coherent couplings, or unweighted graphs other than \(J(n,2)\). The integer \(n\) is at least five, ensuring all three displayed adjacency eigenspaces are present.

## Proof
**1. The three spectral subspaces.** Let \(R\) be the real \(n\)-by-\(N\) unsigned vertex-edge incidence matrix of \(K_n\), whose column for \(\{i,j\}\) is \(e_i+e_j\). Then
\[
R^{\mathsf T}R=A+2I_N,\qquad RR^{\mathsf T}=(n-2)I_n+\mathbf1_n\mathbf1_n^{\mathsf T}.
\]
Because \(n\ge5\), \(R\) has full row rank and \(A\) has eigenvalues \(2(n-2)\), \(n-4\), and \(-2\), with eigenspaces \(V_0=\operatorname{span}(\mathbf1_N)\), \(V_1=R^{\mathsf T}(\mathbf1_n^\perp)\), and \(V_2=\ker R\), respectively. Denote their orthogonal projectors by \(P_0,P_1,P_2\).

**2. Bright-mode decomposition.** Define \(\Gamma=\sum_{e\in F}\gamma_e|e\rangle\langle e|\). Every eigenvector of \(A\) orthogonal to \(|e\rangle\) for all \(e\in F\) is annihilated by \(\Gamma\), so this dark space is invariant under \(H_{\mathrm{eff}}\) and its adjoint. Its orthogonal complement is invariant too and is precisely
\[
\mathcal B=\bigoplus_{j=0}^{2}\operatorname{span}\{P_j|e\rangle:e\in F\}.
\]
An eigenvector \(v\) of the restriction of \(H_{\mathrm{eff}}\) to \(\mathcal B\), with eigenvalue \(z\), obeys \(\operatorname{Im}z=-\langle v,\Gamma v\rangle/\|v\|^2\le0\). Equality would make \(v\) a dark eigenvector of \(A\), contradicting \(v\in\mathcal B\). Thus every bright eigenvalue has strictly negative imaginary part. The bright semigroup decays to zero even in the presence of Jordan blocks; the dark semigroup is unitary. Therefore eventual loss from any density matrix \(\rho\) is \(\operatorname{tr}(P_{\mathcal B}\rho)\); in particular it equals \(\dim\mathcal B/N\) for \(\rho=I_N/N\).

**3. The constant and centered-incidence contributions.** As \(F\ne\varnothing\), \(\operatorname{rank}(P_0|_F)=1\). On \(\mathbf1_n^\perp\), \(RR^{\mathsf T}\) acts as \((n-2)I\), hence
\[
P_1=\frac{1}{n-2}R^{\mathsf T}\left(I_n-\frac{\mathbf1_n\mathbf1_n^{\mathsf T}}n\right)R.
\]
If \(R_F\) is the submatrix with columns in \(F\), then \(\operatorname{rank}(P_1|_F)=\operatorname{rank}(R_F)-\varepsilon(F)\). Indeed, projecting the column span onto \(\mathbf1_n^\perp\) loses precisely one dimension when \(\mathbf1_n\in\operatorname{im}R_F\). The orthogonal complement of \(\operatorname{im}R_F\) consists of vertex labelings \(x_i\) satisfying \(x_i+x_j=0\) on every \(F\)-edge. On a connected nonbipartite component this forces zero; on a bipartite component it is an arbitrary constant times the \(\pm1\) bipartition vector, including isolated components. Therefore \(\operatorname{rank}R_F=n-b(([n],F))\), and \(\mathbf1_n\) belongs to its image exactly when every bipartite component is balanced, which proves
\[
\operatorname{rank}(P_1|_F)=n-b(([n],F))-\varepsilon(F).
\]

**4. The orthogonal-incidence contribution.** Set \(\bar F=\mathcal E\setminus F\). Since \(V_2=\ker R\), the kernel of \(P_2\) is \(\operatorname{im}R^{\mathsf T}\). The kernel of the map sending trap-supported vectors into \(V_2\) is therefore exactly the set of \(R^{\mathsf T}x\) supported on \(F\). This support condition means \(x_i+x_j=0\) for every edge of \(\bar F\). Since \(R^{\mathsf T}\) is injective, the dimension of this kernel is \(b(([n],\bar F))\), using the same bipartite-component argument. Rank-nullity gives
\[
\operatorname{rank}(P_2|_F)=t-b(([n],\bar F)).
\]
Adding the three independent spectral ranks proves the boxed formula.

**5. Four-trap example.** When \(n\ge7\), the complement of either displayed four-edge trap graph is connected and contains a triangle on three unused labels, so its bipartite-component count is zero. Both trap graphs have \(n-4\) isolated labels and are not spanning, so \(\varepsilon=0\). A quadrilateral is one bipartite component on four labels, giving \(b(F)=n-3\) and \(R=8\). A triangle with a pendant edge is one nonbipartite component on four labels, giving \(b(F)=n-4\) and \(R=9\). This proves the contrast.

## Verification
A standalone checker, `verify_trap_rank.py`, constructs the three numerical spectral projectors independently and compares the sum of their restricted ranks with the graph-combinatorial formula. It checks every one of the \(2^{10}-1\) nonempty trap subsets for \(n=5\), 500 seeded subsets for each \(n=6,7,8\), and the stated four-trap contrast for \(n=7,8,11,14\): **2531 comparisons passed**. The proof above, not finite enumeration, establishes all \(n\) and every trap set. Reproduce with `python verify_trap_rank.py` and NumPy installed.

## Relationship to prior work
Novo et al. (first public preprint 22 December 2014, arXiv:1412.7209) establish the general Krylov/invariant-subspace method for coherent transport, principally with one trap, and examine several graph families. Wong (first public preprint 16 January 2016, arXiv:1601.04212) examines quantum search on Johnson graphs, using a Hermitian marked-site oracle, not arbitrary multi-site irreversible absorption. Razzoli, Paris, and Bordone (arXiv:2011.13794) analyze coherent absorption for several graphs with a **single** absorbing site; their general spectral-overlap viewpoint supplies context. The present statement specializes to triangular graphs but covers **every** multi-trap pattern and evaluates the entire accessible dimension solely from the bipartite connected components of the pattern and its complement, including the balanced-component correction. It does not claim novelty for the general Krylov idea, the unsigned-incidence rank theorem, or the notion of quantum dark states.

## Limitations
This is a classification of the **dimension** of the eventually absorbed subspace and the uniform-mixture eventual absorption probability. It does not determine absorption probability for every individually localized source, its absorption-time distribution, robustness under dephasing or Hamiltonian disorder, or arbitrary Johnson graphs \(J(n,k)\) for \(k>2\). The argument relies on real symmetric adjacency dynamics and strictly positive sink rates. Broader prior observability theorems might imply special cases of the rank formula after additional specialization; no exhaustive historical-priority claim is made.

## References
- L. Novo, S. Chakraborty, M. Mohseni, H. Neven, and Y. Omar, *Systematic Dimensionality Reduction for Quantum Walks: Optimal Spatial Search and Transport on Non-Regular Graphs*, arXiv:1412.7209 (v1, 2014-12-22), https://arxiv.org/abs/1412.7209.
- T. G. Wong, *Quantum Walk Search on Johnson Graphs*, arXiv:1601.04212 (v1, 2016-01-16), https://arxiv.org/abs/1601.04212.
- L. Razzoli, M. G. A. Paris, and P. Bordone, *Transport efficiency of continuous-time quantum walks on graphs*, arXiv:2011.13794 (2020), https://arxiv.org/abs/2011.13794.
- I. Kassal and A. Aspuru-Guzik, *Environment-assisted quantum transport in ordered systems*, arXiv:1201.5202 (v1, 2012-01-25), https://arxiv.org/abs/1201.5202.
