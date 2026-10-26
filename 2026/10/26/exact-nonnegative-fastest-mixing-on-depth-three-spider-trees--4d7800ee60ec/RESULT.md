# Exact nonnegative fastest mixing on depth-three spider trees

## Finding

**Theorem.** For every integer \(k\geq3\), let \(S(k,3)\) be the tree with one central vertex and \(k\) disjoint three-edge paths attached to that vertex. Among all real symmetric, entrywise nonnegative, row-stochastic transition matrices supported on the edges and loops of this tree, the minimum second-largest eigenvalue modulus (SLEM) is
\[
\mu_k^*=1-\gamma_k,\qquad
\gamma_k=\frac{2}{3k+5+\sqrt{(3k+5)^2-24k}}.
\]
An optimal matrix has equal transition probabilities along edges at each depth, with the following three probabilities (the probability is the same in either direction):
\[
p_1=\frac1k,\qquad p_2=\frac{2-\gamma_k}{3},\qquad
p_3=\frac{1+\gamma_k}{3}.
\]
These are the **unique optimal probabilities among matrices invariant under permutations of the \(k\) arms**. Arbitrary nonsymmetric optimizers are not classified. The central holding probability and the holding probability at depth two are both zero; the depth-one and leaf holding probabilities are strictly positive.

## Assumptions and scope

The vertex set consists of a root \(o\) and vertices \((j,i)\) for \(1\leq j\leq k\) and \(1\leq i\leq3\). Edges join \(o\) to \((j,1)\), and \((j,i)\) to \((j,i+1)\). There are \(3k+1\) vertices, and no other edges. A feasible matrix \(P\) is real, symmetric, satisfies \(P\mathbf 1=\mathbf1\), is entrywise nonnegative, and has zero off-diagonal entries on nonedges. Self-loops are allowed. Its eigenvalue \(1\) is discounted in defining \(\mu(P)=\|P-\mathbf1\mathbf1^T/(3k+1)\|_2\). The theorem optimizes this SLEM, not total-variation mixing time, arbitrary-stationary reversible chains, or consensus weight matrices with negative diagonals.

For a permutation-invariant matrix, write \(x,y,z\) for edge transition probabilities at depths one, two, and three. Feasibility is precisely
\[
x,y,z\geq0,\quad kx\leq1,\quad x+y\leq1,\quad y+z\leq1.
\]
The corresponding holding probabilities at root, depth one, depth two, and depth three are \(1-kx\), \(1-x-y\), \(1-y-z\), and \(1-z\), respectively.

## Proof

**1. Symmetry reduction and block spectra.** Averaging a feasible transition matrix over all arm permutations preserves its constraints and cannot increase the spectral norm \(\mu\). Consequently at least one global minimizer is arm-permutation invariant. Write \(L=I-P\). The permutation representation on arms decomposes \(L\) into the radial block
\[
R=\begin{pmatrix}
kx&-\sqrt{k}x&0&0\\
-\sqrt{k}x&x+y&-y&0\\
0&-y&y+z&-z\\
0&0&-z&z
\end{pmatrix},
\]
and \(k-1\) copies of the arm-contrast block
\[
B=\begin{pmatrix}
x+y&-y&0\\-y&y+z&-z\\0&-z&z
\end{pmatrix}.
\]
The radial block has one zero eigenvalue. The contrast block is a principal submatrix of \(R\). Cauchy interlacing therefore gives, for all feasible \((x,y,z)\),
\[
\lambda_2(L)\leq\lambda_{\min}(B),\qquad
\mu(P)\geq1-\lambda_{\min}(B).
\]
This inequality remains true if a matrix is reducible, in which case the objective is at least one.

**2. An exact spectral-gap certificate.** Write \(\gamma=\gamma_k\), \(x_*=1/k\). Direct substitution gives
\[
6\gamma^2-(3+5x_*)\gamma+x_*=0,
\qquad0<\gamma<\frac15.
\]
Set \(y_*=(2-\gamma)/3\), \(z_*=(1+\gamma)/3\), \(a=(1-5\gamma)/(3\gamma)>0\), and \(v=(a,a+1,a+2)^T\). The displayed quadratic identity implies
\[
B(x_*,y_*,z_*)v=\gamma v.
\]
The vector \(v\) is positive and this symmetric tridiagonal block has strictly negative off-diagonal entries, so its lowest eigenvalue is \(\gamma\). More explicitly, \(B\) is an irreducible symmetric \(M\)-matrix with positive eigenvector for \(\gamma\), hence \(\gamma=\lambda_{\min}(B_*)\).

For any feasible \((x,y,z)\), the quadratic form on the *fixed* vector \(v\) is
\[
v^TB(x,y,z)v=xa^2+y+z\leq\frac{a^2}{k}+1
=\gamma\|v\|^2.
\]
It follows that \(\lambda_{\min}(B)\leq\gamma\), and therefore \(\mu(P)\geq1-\gamma\). Equality in the displayed inequality forces \(x=1/k\) and \(y+z=1\), since \(a>0\). Equality in the Rayleigh principle forces \(Bv=\gamma v\). Its final coordinate gives \(z=\gamma(a+2)=(1+\gamma)/3\), and then \(y=(2-\gamma)/3\). Thus the proposed parameters are the unique maximizers of the branch-contrast gap, and any orbit-invariant SLEM minimizer attaining \(1-\gamma\) must use them.

**3. The negative spectral end is inactive.** The proposed parameters satisfy all stochastic constraints: \(kx_*=1\), \(y_*+z_*=1\), and \(x_*+y_*<1\) for \(k\geq3\). Direct tridiagonal determinant expansion, simplifying with the quadratic equation for \(\gamma\), factors the radial characteristic polynomial:
\[
\det(tI-R_*)=t(t-1-\gamma)
\left[t^2-\left(2+\frac1k-\gamma\right)t
+\frac{(3+1/k)(2-\gamma)}9\right].
\]
Denote the quadratic factor by \(q(t)\). Its roots are real since they are eigenvalues of the symmetric radial block. At \(t=2-\gamma\),
\[
q(2-\gamma)=\frac{(2-\gamma)(3k-8)}{9k}>0.
\]
Also \(2-\gamma\) lies strictly to the right of the quadratic's vertex \((2+1/k-\gamma)/2\). Hence both quadratic roots are strictly smaller than \(2-\gamma\). The remaining positive radial eigenvalue is \(1+\gamma<2-\gamma\). Interlacing implies the largest contrast eigenvalue is no larger than the largest radial eigenvalue. Thus \(\lambda_{\max}(L_*)<2-\gamma\). On the other hand, \(\lambda_2(L_*)=\gamma\) by the contrast eigenvector and radial interlacing. Consequently
\[
\mu(P_*)=\max\{1-\lambda_2(L_*),\lambda_{\max}(L_*)-1\}
=1-\gamma.
\]
Together with the global lower bound and symmetry averaging this completes the proof for every integer \(k\geq3\).

## Verification

The standalone Python script `verify.py` uses exact SymPy polynomial identities for the arm-contrast eigenpair, radial characteristic factorization, determinant relation, and Rayleigh certificate. It independently assembles and diagonalizes the full \((3k+1)\)-by-\((3k+1)\) Laplacian for \(3\leq k\leq14\), compares all reduced blocks for \(3\leq k\leq30\), and tests 2,800 feasible pseudorandom competitors. The exact symbolic proof above establishes the claim for all \(k\geq3\); finite calculations are corroboration, not an exhaustive optimization certificate. Run `python verify.py` with packages in `requirements.txt`.

For example \(k=3\), \(\gamma\approx0.0795686465094432\) and \(\mu^*\approx0.920431353490557\). As \(k\to\infty\), \(\gamma=1/(3k)+O(k^{-2})\), while \(p_2\to2/3\) and \(p_3\to1/3\).

## Relationship to prior work

Boyd, Diaconis, Parrilo, and Xiao (2007/2009) gave the general symmetric fastest-mixing Markov-chain semidefinite formulation and symmetry-averaging theorem, including explicit solutions on various highly symmetric graphs; this note applies the known framework to a nonequivalent three-edge-arm family and derives its exact Markov-feasible optimum. Boyd, Diaconis, and Xiao (2004) introduced the underlying fastest-mixing optimization.

Jafarizadeh and Jamalipour (2010) treated the *same symmetric-star topology* for fastest distributed averaging with weights that may yield negative holding probabilities: their optimal center-edge weight \(2/(k+2)\) has root diagonal \((2-k)/(k+2)<0\) when \(k\geq3\). Therefore their result does not solve optimization over entrywise nonnegative stochastic transition matrices. Jafarizadeh's 2020/2025 reversible-chain treatment gives symmetric-star formulas under inequalities including \(k\pi_1\leq2\pi_0\), which fail for the uniform stationary law and \(k\geq3\); its unconditional depth-two treatment does not cover this depth-three case. Its general constrained symmetric-tree methods remain relevant antecedents.

## Limitations

The uniqueness assertion is restricted to matrices invariant under arm permutations; other globally optimal nonsymmetric transition matrices have not been classified. The optimum is for symmetric Markov matrices with uniform stationary law and loops allowed, not unrestricted consensus averaging or other equilibrium distributions. Literature comparison cannot exclude specialized, unindexed derivations of the same constrained spider solution; the closely overlapping 2010 and 2020 works require particular attention when independently reviewing originality.

## References

1. S. Boyd, P. Diaconis, P. Parrilo, and L. Xiao, “Fastest mixing Markov chain on graphs with symmetries,” arXiv:0709.0955 (first posted 2007-09-06); *SIAM Journal on Optimization* 20 (2009), 792–819. https://arxiv.org/abs/0709.0955
2. S. Boyd, P. Diaconis, and L. Xiao, “Fastest mixing Markov chain on a graph,” *SIAM Review* 46 (2004), 667–689. https://web.stanford.edu/~boyd/papers/fmmc.html
3. S. Jafarizadeh and A. Jamalipour, “Weight optimization for distributed average consensus algorithm in symmetric, CCS & KCS star networks,” arXiv:1001.4278 (first posted 2010-01-24). https://arxiv.org/abs/1001.4278
4. S. Jafarizadeh, “Fastest mixing reversible Markov chain: clique lifted graphs and subgraphs,” *IEEE Transactions on Signal and Information Processing over Networks* (2020), DOI:10.1109/TSIPN.2020.2964211; accessible later arXiv copy 2501.02421, sections 6.6 and 7.2–7.3. https://arxiv.org/abs/2501.02421
