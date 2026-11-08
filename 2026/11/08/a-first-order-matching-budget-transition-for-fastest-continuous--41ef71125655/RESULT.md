# A first-order matching-budget transition for fastest continuous-time mixing on complete bipartite graphs

## Finding
Let \(n\ge3\) be an integer, \(B>0\) and \(c>0\). In the complete bipartite graph \(K_{n,n}\), label the parts \(u_1,\dots,u_n\) and \(v_1,\dots,v_n\). Select completely independent nonnegative edge conductances \(w_{ij}\) at costs \(c\) on the designated perfect matching \(u_iv_i\) and cost one on the remaining edges. Maximize the algebraic connectivity \(\lambda_2(L)\) under
\[
 c\sum_{i=1}^n w_{ii}+\sum_{i\ne j}w_{ij}\le B.
\]
Put \(c_*=2(n-1)/(n-2)\). The optimal value is
\[
\lambda_2^*=\begin{cases}
B/(n-1+c),&0<c<c_*,\
(n-2)B/[n(n-1)],&c\ge c_*.
\end{cases}
\]
Every optimizer, including any initially nonsymmetric candidate, must have one common matching conductance \(x\) and one common nonmatching conductance \(y\). The complete list of optimal designs is:

1. If \(c<c_*\), there is exactly one optimum: \(x=y=B/[n(n-1+c)]\).
2. If \(c>c_*\), there is exactly one optimum: \(x=0\), \(y=B/[n(n-1)]\).
3. If \(c=c_*\), all optimal designs and no others are given by \(0\le x\le B/[n(n-1+c_*)]\), \(y=(B/n-c_*x)/(n-1)\).

The matching-edge investment has a discontinuous limit at the critical price: as \(c\uparrow c_*\) from below, the per-edge matching conductance approaches \(B(n-2)/[n^2(n-1)]>0\); for every \(c>c_*\), it is zero. The cutoff is independent of \(B\), and \(c_*\downarrow2\) as \(n\to\infty\).

## Assumptions and scope
The graph is undirected, with no self-loops or edges within either part. The Laplacian is unnormalized: \(L=\operatorname{diag}(W\mathbf1,W^T\mathbf1)-\left[\begin{smallmatrix}0&W\ W^T&0\end{smallmatrix}\right]\), with the diagonal understood in two blocks, and \(W=(w_{ij})\). Conductances may be zero, so deleting an expensive matching edge is permitted. The objective concerns the continuous-time diffusion generator \(-L\), not the modulus of eigenvalues of a discrete-time Markov kernel. We make no assertion for \(n=2\), where the rigidity argument changes.

## Proof
**1. Two universal upper bounds.** Set \(S_m=\sum_iw_{ii}\), \(S_o=\sum_{i\ne j}w_{ij}\), \(\bar x=S_m/n\), \(\bar y=S_o/[n(n-1)]\). In \(\mathbb R^{2n}\), consider the two mutually orthogonal subspaces
\[
E=\{(a,a):\mathbf1^Ta=0\},\qquad O=\{(a,-a):\mathbf1^Ta=0\}.
\]
Each has dimension \(n-1\), and both lie in \(\mathbf1_{2n}^\perp\). For any orthonormal basis of each space, the average of the corresponding Rayleigh quotients is at least \(\lambda_2(L)\). Explicitly, using the projector \(P=I_n-\mathbf1_n\mathbf1_n^T/n\), the orthogonal average on \(E\) is \(S_o/(n-1)=n\bar y\), since a matched edge makes no contribution. The orthogonal average on \(O\) is \(2S_m/n+(n-2)S_o/[n(n-1)]=2\bar x+(n-2)\bar y\). Thus every feasible design satisfies
\[
\lambda_2(L)\le\min\{n\bar y,\ 2\bar x+(n-2)\bar y\},\qquad
nc\bar x+n(n-1)\bar y\le B.
\]
These inequalities do not assume any symmetry of \(W\).

**2. Sharp scalar maximization.** Because all costs are positive and there is a connected positive design, every optimum exhausts the budget: otherwise scaling all conductances increases \(\lambda_2\). Write \(\bar y=(B/n-c\bar x)/(n-1)\). The two affine bounds cross exactly when \(\bar x=\bar y=B/[n(n-1+c)]\). Before the crossing the second bound is active and has slope \(2-c(n-2)/(n-1)\); after the crossing the first bound is active and strictly decreases. The slope changes sign exactly at \(c_*\). Hence the scalar maximum, its uniqueness away from \(c_*\), and the interval of maximizing mean conductances at equality are precisely as asserted.

**3. Every scalar bound is attained.** When every diagonal entry of \(W\) equals \(x\) and every off-diagonal entry equals \(y\), the full Laplacian has orthogonal eigenvalues and multiplicities
\[
0\ (1),\qquad ny\ (n-1),\qquad 2x+(n-2)y\ (n-1),\qquad2[x+(n-1)y]\ (1).
\]
The last eigenvalue exceeds both middle ones for every \(x\ge0,y>0\). Consequently \(\lambda_2(L)=\min\{ny,2x+(n-2)y\}\), so all scalar maximizers constructed in step 2 attain the upper bound. Every one has \(y>0\), hence defines a connected graph.

**4. Rigidity among all heterogeneous edge allocations.** At every scalar optimum above, the \(O\)-average bound is equal to the optimal value \(\lambda_*\). Thus if an arbitrary nonsymmetric allocation is globally optimal, each vector \(z\in O\) satisfies \(z^TLz=\lambda_*\|z\|^2\): the average of its eigenvalue-bounded Rayleigh quotients is equal to their common lower bound. Since \(L-\lambda_* (I_{2n}-\mathbf1\mathbf1^T/(2n))\) is positive semidefinite, each \(z\in O\) actually obeys \(Lz=\lambda_*z\).

With \(D_r=\operatorname{diag}(W\mathbf1)\) and \(D_c=\operatorname{diag}(W^T\mathbf1)\), substitution of \(z=(a,-a)\) for all \(\mathbf1^Ta=0\) gives
\[
(D_r+W)a=\lambda_*a,\qquad(D_c+W^T)a=\lambda_*a.
\]
Therefore every row of \(D_r+W-\lambda_*I\), and similarly every row of \(D_c+W^T-\lambda_*I\), is constant across its columns. For each \(i\), all \(w_{ij}\) with \(j\ne i\) are equal; for each \(j\), all \(w_{ij}\) with \(i\ne j\) are equal. Because \(n\ge3\), any two rows have a common off-diagonal column, so *all* off-matching entries equal one \(y\). The diagonal row condition then reads \(2w_{ii}+(n-1)y-\lambda_*=y\), forcing all \(w_{ii}\) to equal one \(x\). Therefore every optimum is classwise constant, and step 2 gives the exhaustive list. \(\square\)

## Verification
Run `python3 verify.py` using the Python standard library. The script constructs exact rational weighted Laplacians, checks their eigenactions on the four explicitly described invariant subspaces, checks all budget identities across multiple integers, costs, and budget values, and confirms both universal trace identities for additional nonsymmetric rational allocations. The present package replay returns `VERIFY_OK 498`. The checker is finite corroboration; the dimension-independent algebra and rigidity reasoning in the proof establish the theorem.

## Relationship to prior work
Sun, Boyd, Xiao and Diaconis formulate and analyze general fastest-mixing continuous-time graph processes with linear edge costs. Their general semidefinite framework contains this optimization problem as an instance, but the inspected examples give paths, uniform cycles and illustrative finite networks, not the exact price threshold and complete optimizer set above. Boyd, Diaconis, Parrilo and Xiao analyze a discrete-time fastest-mixing problem and give the uniform-edge complete-bipartite spectral decomposition; that objective and symmetry class do not cover a separately priced matching under a continuous-time conductance budget. Klee and Stamps derive the known *unweighted crown-graph spectrum*, which agrees with the \(x=0\) boundary eigenvalues but does not specify the price transition, equality interval or global rigidity of optimal allocations. Existing results for resistance-minimizing or minimax-resistance budgets on the same graph use different objective functions and do not imply this second-eigenvalue optimizer classification.

## Limitations
The result is for balanced complete bipartite graphs with one *uniform* cost on a fixed perfect matching and unit cost on all other edges. It does not classify unequal matching-edge prices, unbalanced bipartite graphs, time-discrete fastest-mixing kernels, or optimal designs under additional upper bounds on edge rates. The baseline crown spectrum and general convex formulation are known, not claimed as new. Although targeted comparisons found no explicit equivalent formula, unindexed or inaccessible work may contain a stronger equivalent statement; independent publication-priority review is outstanding.

## References
- J. Sun, S. Boyd, L. Xiao and P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review **48** (2006), 681–699, DOI 10.1137/S0036144504443821; published electronically 2006-11-02. https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf
- S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM Journal on Optimization **20** (2009), 792–819, DOI 10.1137/070689413; preprint arXiv:0709.0955. https://web.stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf
- S. Klee and M. T. Stamps, *Eigenvalues of Graph Laplacians via Rank-One Perturbations*, arXiv:2008.01669 (2020), Section 3.3 (the known crown spectrum). https://arxiv.org/pdf/2008.01669
