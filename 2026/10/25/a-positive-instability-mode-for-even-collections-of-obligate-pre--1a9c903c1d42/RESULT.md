# A positive instability mode for even collections of obligate predation cycles

## Finding
**Theorem (even-cycle instability with a mortality-scale eigenvalue).** Let \(k\ge2\) be even. Partition \(n\ge3k\) species into \(k\) pairwise-disjoint directed cycles, each of length at least three, and let \(\sigma(i)\) be the successor (prey) of species \(i\). Consider the generalized Lotka–Volterra equations
\[
\dot x_i=x_i\left(a_i-\sum_{j=1}^n b_{ij}x_j\right),\qquad i=1,\ldots,n.
\]
Assume the strict signs \(a_i<0\), \(b_{ii}>0\), \(b_{i,\sigma(i)}<0\), and \(b_{ij}>0\) for all other \(j\notin\{i,\sigma(i)\}\). Then **every** equilibrium \(x^*\in(0,\infty)^n\), whenever one exists, has a Jacobian eigenvalue \(\lambda_*>0\) with a strictly positive right eigenvector and with the explicit bounds
\[
\boxed{\min_i(-a_i)\ \le\ \lambda_*\ \le\ \max_i(-a_i).}
\]
In particular, no such ecological sign pattern supports a locally asymptotically stable feasible equilibrium, including for an even number of cycles. The positive-eigenvector eigenvalue in the interval is unique, though the Jacobian may have other positive eigenvalues outside it.

**Sharpness and feasibility.** For every even \(k\ge2\) and every such cycle partition, set \(a_i=-3\), \(x_i^*=1\), \(b_{ii}=1\), \(b_{i,\sigma(i)}=-(n+2)\), and \(b_{ij}=1\) otherwise. These data admit the displayed strictly positive equilibrium, and \(\lambda_*=3\) realizes equality at both bounds. The smallest case consists of two three-species cycles.

## Assumptions and scope
A directed cycle of length at least three has exactly one prey for every species. Each species benefits from consuming its successor and is harmed by all other species, including its predecessor; all unordered pairs not connected by predation are competitors. Every coefficient has the specified strict sign. No assumption is imposed on relative coefficient magnitudes, apart from equilibrium feasibility when discussing the Jacobian. Stability means local asymptotic stability of a positive equilibrium for the continuous-time deterministic pairwise generalized Lotka–Volterra system. The proof gives a linear unstable direction, not a claim about global extinction or stability of boundary equilibria.

## Proof
Let \(x^*>0\) be any feasible equilibrium, and put \(D=\operatorname{diag}(x^*)\). Its equilibrium equations are \(Bx^*=a\), and its Jacobian is \(J=-DB\). Similarity by \(D\) gives
\[
D^{-1}JD=-BD=:M,\qquad M\mathbf 1=-a=:d>0.
\]
Decompose \(M=F-V\) as follows:
\[
F_{i,\sigma(i)}=-b_{i,\sigma(i)}x^*_{\sigma(i)}>0,
\qquad F_{ij}=0\ \text{otherwise},
\]
\[
V_{ij}=b_{ij}x^*_j\quad\text{for } j\ne\sigma(i),
\qquad V_{i,\sigma(i)}=0.
\]
The matrix \(F\) is a positive weighted permutation matrix, hence invertible with \(F^{-1}\ge0\). Every other entry of \(V\), including every diagonal entry, is strictly positive. In particular \(V\ge0\), and the equilibrium equations give \(F\mathbf1=V\mathbf1+d\).

For \(\lambda\ge0\) define the nonnegative matrix
\[
K(\lambda)=F^{-1}(V+\lambda I).
\]
Its entries strictly above and below the diagonal are positive (while its diagonal entries vanish): the unique positive position of each row of \(F^{-1}\) selects a row of \(V+\lambda I\) whose unique zero position is the given row index. Thus \(K(\lambda)\) is irreducible for the stated species count, and Perron–Frobenius supplies an eigenvector with all coordinates strictly positive at its spectral radius \(\rho(\lambda)\). The map \(\lambda\mapsto\rho(\lambda)\) is continuous. Moreover
\[
K(\lambda)\mathbf1
=\mathbf1+F^{-1}(\lambda\mathbf1-d).
\]
Writing \(d_-=\min_i d_i\) and \(d_+=\max_i d_i\), nonnegativity of \(F^{-1}\) yields \(K(d_-)\mathbf1\le\mathbf1\) and \(K(d_+)\mathbf1\ge\mathbf1\). The Collatz–Wielandt inequalities yield
\[
\rho(d_-)\le1\le\rho(d_+).
\]
Continuity therefore gives \(\lambda_*\in[d_-,d_+]\) with \(\rho(\lambda_*)=1\). Let \(v>0\) satisfy \(K(\lambda_*)v=v\). Multiplying by \(F\) gives \((F-V)v=\lambda_*v\), or \(Mv=\lambda_*v\). Since \(J(Dv)=D(Mv)\), the strictly positive vector \(Dv\) is a right eigenvector of \(J\) with eigenvalue \(\lambda_*\ge d_->0\). Hence every feasible equilibrium is linearly unstable and cannot be locally asymptotically stable.

For uniqueness among positive-eigenvector eigenvalues, note that \(F^{-1}I\) has a positive entry in every row. For \(0\le s<t\), \(K(t)\ge K(s)\), the inequality is strict somewhere, and both matrices are irreducible with all off-diagonal entries positive. Strict Perron monotonicity gives \(\rho(t)>\rho(s)\). Thus \(\rho(\lambda)=1\) has exactly one nonnegative solution. If a nonnegative real eigenvalue of \(J\) has a strictly positive right eigenvector, similarity by \(D\) produces a positive eigenvector of \(M\), and its nonnegative eigenvalue must give this same Perron crossing; hence it equals \(\lambda_*\).

For the sharpness construction, let \(P\) be the permutation matrix with \(P_{i,\sigma(i)}=1\), and let \(U=\mathbf1\mathbf1^T\). The proposed interaction matrix is \(B=U-(n+3)P\), with row sums \(-3\), so \(Bx^*=a\) at \(x^*=\mathbf1\). Its Jacobian is \(J=(n+3)P-U\), hence \(J\mathbf1=3\mathbf1\), proving both feasibility and sharpness. For \(n=6\) and two three-cycles, the remaining spectrum is \(9\) and the conjugate pair \(-9/2\pm9\sqrt3\,i/2\), each with multiplicity two. In particular the mortality-scale eigenvalue need **not** be the spectral-abscissa eigenvalue.

## Verification
The included standalone `verify.py` reconstructs the exact six-species example using rational-symbolic matrices and checks its equilibrium, strict signs, eigenvalues, and positive eigenvector. It also generates deterministic positive \(V\) matrices and mortality vectors over four cycle decompositions, sets \(F_{i,\sigma(i)}=\sum_j V_{ij}+d_i\) to enforce the positive-equilibrium row equations, and checks numerically that the Perron crossing is within the prescribed mortality interval and agrees with a real eigenvalue of \(F-V\). The sampled cases are corroboration only; the all-parameter assertion follows from the proof above.

## Relationship to prior work
Meng, Horvát, Modes, and Haas (arXiv:2309.16261, first publicly posted 2023-09-28) initiated the impossibility classification, including an obligate three-species predation cycle. Çelik, Haas, Scholten, Wang, and Zucal (arXiv:2509.00165) developed algebraic classification tools for small ecological networks. Most directly, Çelik, Isoldi, Portakal, and Zucal (arXiv:2609.09286v1, Section 3.2, Theorem 3.4) prove impossibility for an **odd** number of disjoint obligate prey–predator cycles with inner competition by the determinant sign \(\operatorname{sign}\det B=(-1)^k\). That determinant obstruction gives a positive sign for even \(k\) and does not itself exclude stability. Their Theorem 3.7 concerns even cycles **plus an additional obligate mutualist pair**, which is a different interaction network, not the present all-cycle sign pattern. The result here settles the even-cycle case by constructing a positive real Jacobian eigenmode and locating it on an intrinsic-mortality scale, rather than by determinant parity. This is a claim about the contents inspected in these sources, not a proof of priority against all literature.

## Limitations
The theorem is conditional on a strictly positive equilibrium when asserting spectral instability; it does not assert feasibility for every choice of magnitudes. Strictly negative intrinsic growth and exactly one negative interaction per row are indispensable to the proof, and conclusions for additional mutualistic pairs, species with positive intrinsic growth, nonpairwise interactions, or non-equilibrium attractors are not established. Classical matrix-theoretic reductions might provide alternative proofs; exhaustive publication priority and independent validation are not claimed.

## References
1. Y. Meng, S. Horvát, C. D. Modes, P. A. Haas, *Impossible ecologies: Interaction networks and stability of coexistence in ecological communities*, arXiv:2309.16261v1 (2023-09-28), https://arxiv.org/abs/2309.16261.
2. T. Ö. Çelik, P. A. Haas, G. Scholten, K. Wang, G. Zucal, *Strata of Ecological Coexistence via Grassmannians*, arXiv:2509.00165v1 (2025), https://arxiv.org/html/2509.00165v1.
3. T. Ö. Çelik, V. A. Isoldi, I. Portakal, G. Zucal, *Stable Coexistence in Ecologies and Games*, arXiv:2609.09286v1 (2026), https://arxiv.org/html/2609.09286v1.
4. Classical Perron–Frobenius theorem and Collatz–Wielandt spectral-radius bounds for irreducible nonnegative matrices.
