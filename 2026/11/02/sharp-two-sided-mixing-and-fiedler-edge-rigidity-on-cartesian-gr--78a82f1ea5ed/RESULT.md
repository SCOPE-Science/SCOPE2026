# Sharp two-sided mixing and Fiedler-edge rigidity on Cartesian graph products

## Finding

**Theorem (product mixing and local rigidity).** Let \(s\ge2\) and let \(H_1,\ldots,H_s\) be finite connected, simple, vertex-transitive and edge-transitive regular graphs. For factor \(i\), let \(d_i\) be its degree and \(\alpha_i>0\), \(\beta_i\) its smallest positive and largest (combinatorial) Laplacian eigenvalues. Define
\[
 C=\sum_{i=1}^s\frac{d_i}{\alpha_i},\qquad E=\sum_{i=1}^s\frac{\beta_i}{\alpha_i},\qquad
 \tau=\min\left\{\frac1C,\frac2{E+1}\right\}.
\]
On their Cartesian product \(G=H_1\square\cdots\square H_s\), the minimum of \(\|P-J/N\|_2\), over **all** real symmetric, entrywise nonnegative, row-stochastic matrices with transitions supported on loops and edges of \(G\), is exactly \(1-\tau\). Here \(N=|V(G)|\) and \(J\) is the all-ones matrix. An optimal matrix \(P_*\) has transition probability \(\tau/\alpha_i\) across each undirected edge in factor direction \(i\), with holding probability \(1-C\tau\) at each vertex. These directional probabilities are the **unique** optimum among matrices invariant under the coordinatewise factor automorphism groups.

Let \(\Pi_i\) denote the orthogonal projector onto the \(\alpha_i\)-Laplacian eigenspace in \(\mathbb R^{V(H_i)}\). Suppose the **local Fiedler-edge independence condition** holds at every vertex \(v\) of every factor:
\[
 \{\Pi_i(e_u-e_v):u\sim_{H_i}v\}\quad\text{is linearly independent}.
\]
Then \(P_*\) is the **unique optimum without any factor-invariance assumption**. The condition can be tested by positive definiteness of its \(d_i\times d_i\) Gram matrix, whose entries are \((e_u-e_v)^\mathsf T\Pi_i(e_w-e_v)\).

**Explicit mixed-family corollary.** Let \(\mathcal P\) be the Petersen graph, let \(k\ge1\), \(m\ge4\), and put \(G_{k,m}=\mathcal P^{\square k}\square C_m\). Set
\[
 \alpha_m=2-2\cos(2\pi/m),\qquad
 \beta_m=2-2\cos\big(2\pi\lfloor m/2\rfloor/m\big),
\]
\[
 C_{k,m}=\frac{3k}{2}+\frac2{\alpha_m},\qquad
 E_{k,m}=\frac{5k}{2}+\frac{\beta_m}{\alpha_m},\qquad
 \tau_{k,m}=\min\left\{\frac1{C_{k,m}},\frac2{E_{k,m}+1}\right\}.
\]
For every \(k,m\) in these ranges, the unique unrestricted fastest symmetric stochastic walk has probability \(\tau_{k,m}/2\) on each Petersen-direction edge, probability \(\tau_{k,m}/\alpha_m\) on each cycle-direction edge, and holding probability \(1-C_{k,m}\tau_{k,m}\). Its centered spectral contraction is \(1-\tau_{k,m}\). The holding probability is **strictly positive if and only if \(k=1\)**; it vanishes for every \(k\ge2\), regardless of \(m\).

## Assumptions and scope

All factor graphs are finite, connected, simple, undirected, regular, vertex-transitive, edge-transitive, and contain at least two vertices. The Cartesian product has an edge between two tuples only when they differ along a single factor edge. The optimization is over *every* symmetric stochastic matrix supported on this graph; transition probabilities may vary independently by edge and vertex, and holding is permitted. No nonreversible matrix or time-dependent schedule is included. Each spectral contraction is an operator norm on the orthogonal complement of the uniform stationary vector. The local independence assumption is an explicit **sufficient** condition for unrestricted uniqueness, not asserted to be necessary on arbitrary products.

## Proof

**1. Orbit averaging.** Let \(\Gamma=\prod_i\operatorname{Aut}(H_i)\) act on product vertices. Since \(\|P-J/N\|_2\) is convex and invariant under permutation conjugation, averaging any feasible \(P\) over \(\Gamma\) cannot increase its contraction. Vertex and edge transitivity force the average to have one edge probability \(w_i\ge0\) in each factor direction and constant diagonal \(q=1-\sum_i d_iw_i\ge0\). Thus an orbit-invariant optimizer exists; averaging is not assumed to preserve uniqueness.

**2. Two extreme eigenmodes.** For these matrices,
\[
 P=I-\sum_{i=1}^s w_i\big(I\otimes\cdots\otimes L(H_i)\otimes\cdots\otimes I\big).
\]
The tensor-product Laplacian basis gives all eigenvalues \(1-\sum_i w_i\lambda_{i,j_i}\). The largest nonconstant eigenvalue is \(1-\min_i(\alpha_iw_i)\), attained by a Fiedler mode of a single factor; the smallest eigenvalue is \(1-\sum_i\beta_iw_i\), attained by tensoring top-Laplacian modes. In particular, if the contraction is at most \(r\), every \(w_i\ge(1-r)/\alpha_i\). The stochastic budget then implies \(C(1-r)\le1\). The lower spectral extreme gives \(\sum_i\beta_iw_i\le1+r\), whereas \(\sum_i\beta_iw_i\ge E(1-r)\). Consequently
\[
 r\ge\max\left\{1-\frac1C,\frac{E-1}{E+1}\right\}=1-\tau.
\]
For \(w_i=\tau/\alpha_i\), the budget is feasible because \(C\tau\le1\), and the smallest eigenvalue obeys \(1-E\tau\ge-(1-\tau)\). The largest nontrivial one equals \(1-\tau\), proving the optimum. These same inequalities show uniqueness *within the orbit-invariant class*: every optimal \(w_i\) meets the lower bound \(\tau/\alpha_i\), and either the budget constraint (when \(\tau=1/C\)) or the smallest-eigenvalue constraint (when \(\tau=2/(E+1)\)) makes any strict increase impossible. This includes equality of the two branches.

**3. Rigidity without imposing symmetry.** Let \(Q\) be an arbitrary optimal symmetric stochastic matrix. Its \(\Gamma\)-average is \(P_*\), by orbit-invariant uniqueness. Put \(\mu=1-\tau\) and \(R=\mu I-(Q-J/N)\). Since \(\|Q-J/N\|_2\le\mu\), the symmetric matrix \(R\) is positive semidefinite. Let \(f\) be a lifted factor Fiedler eigenfunction, constant in all coordinates except factor \(i\), and orthogonal to constants. It obeys \(P_*f=\mu f\). Averaging the positive semidefinite conjugates of \(R\) gives \(\mu I-(P_*-J/N)\), whose quadratic form on \(f\) is zero. Because every summand is nonnegative, the unaveraged quadratic form \(f^\mathsf TRf\) must vanish. Positive semidefiniteness implies \(Rf=0\), hence \(Qf=P_*f\).

At any product vertex \(v\), subtracting these two eigenvector equations yields
\[
 \sum_{u\sim_{H_i} v_i}\left(Q_{v,v^{(i\to u)}}-\frac\tau{\alpha_i}\right)
   \big(f_i(u)-f_i(v_i)\big)=0
\]
for **every** Fiedler eigenfunction \(f_i\) of factor \(H_i\). The differences in parentheses are the local projected edge vectors. Their assumed independence forces each coefficient to vanish. Repeating at all vertices and directions fixes all off-diagonal entries of \(Q\); row sums fix its diagonal. Therefore \(Q=P_*\), proving unrestricted uniqueness.

**4. Checking the two factor types.** On \(C_m\), the Fiedler eigenspace is spanned by \(j\mapsto\cos(2\pi j/m)\) and \(j\mapsto\sin(2\pi j/m)\). At vertex zero, the two neighbor-difference columns have determinant \(-2(\cos(2\pi/m)-1)\sin(2\pi/m)\ne0\) for \(m\ge3\). Translation handles every vertex.

For the Petersen graph, its adjacency matrix \(A\) satisfies \(A^2=2I-A+J\), and its eigenvalues are \(3,1,-2\). Thus the Laplacian Fiedler eigenvalue is \(2\), the maximum is \(5\), and the Fiedler projector is \(\Pi=(4I+2A-J)/6\). The three neighbors of each vertex are pairwise nonadjacent. If \(v\) is any vertex with neighbors \(u_1,u_2,u_3\), direct substitution gives
\[
 \big[(e_{u_j}-e_v)^\mathsf T\Pi(e_{u_\ell}-e_v)\big]_{j,\ell=1}^3=\frac23 I_3,
\]
which is positive definite. Therefore every factor of \(\mathcal P^{\square k}\square C_m\) satisfies the independence condition.

**5. Exact holding transition.** Substituting the factor spectra gives \(C_{k,m},E_{k,m}\). The sign controlling the active branch is
\[
 2C_{k,m}-(E_{k,m}+1)=\frac{k}{2}-1+\frac{4-\beta_m}{\alpha_m}.
\]
When \(m\) is even, \(\beta_m=4\) and the last ratio is zero. When \(m\) is odd, elementary trigonometry gives \((4-\beta_m)/\alpha_m=1/[4\cos^2(\pi/(2m))]\), strictly between \(1/4\) and \(1/3\) for odd \(m\ge5\). Hence this difference is negative for \(k=1\), nonnegative for every \(k\ge2\) (and zero precisely for \(k=2\) with \(m\) even). Since \(1/C_{k,m}<2/(E_{k,m}+1)\) exactly when that difference is negative, the balancing branch makes \(C_{k,m}\tau_{k,m}<1\) for \(k=1\), while the budget branch makes \(C_{k,m}\tau_{k,m}=1\) for \(k\ge2\). This proves the stated iff transition.

## Verification

The self-contained `verify.py` uses Python 3 with NumPy and SymPy. Run `python verify.py` in the directory containing this report. It checks the Petersen adjacency identity and exact rational Fiedler projector, all local Petersen Gram matrices, **1,140** dimension pairs with \(1\le k\le20\), \(4\le m\le60\), full product transition matrices and spectra for six small products, plus edge perturbation stress tests. On the recorded run, it printed `PASS 4801 assertions`. The infinite-family conclusions and uniqueness are justified by the analytic argument above; finite tests are not an exhaustive proof. For \(\mathcal P\square C_5\), the exact step is \(\tau=4/(10+\sqrt5)\), the contraction is approximately \(0.673097599052623\), and the holding probability approximately \(0.0365487995263114\). For \(\mathcal P\square\mathcal P\square C_5\), the holding is zero.

## Relationship to prior work

Boyd, Diaconis, Parrilo and Xiao's 2007 preprint (2009 journal article) develops the general FMMC semidefinite formulation, symmetry reduction, and edge-/distance-transitive examples, including a Petersen walk and Cartesian-product examples. Its framework supplies the natural objective, but the relevant inspected examples do not state this local Fiedler-edge independence criterion, arbitrary mixed-factor uniqueness proof, or the Petersen-cycle holding dichotomy. An earlier Microsoft report is catalogued as May 2007 without a verified day; the dated arXiv upload on 2007-09-06 is the first day-resolved public version confirmed for this focal source. The distinct 2026 Laplacian-product analysis treats optimization of algebraic connectivity under a directional budget, not the two-sided stochastic second-largest-eigenvalue modulus with unrestricted edge probabilities. Independent earlier related results for homogeneous complete-graph products and for cycle products do not imply the mixed Petersen-cycle local rigidity conclusion: they treat different factor classes. All consequences that follow directly from the old general semidefinite formulation are used as background rather than separately claimed novel.

## Limitations

This theorem is for symmetric uniform-stationary Markov chains, with loops allowed. Nonreversible, nonuniform-stationary, asynchronous, time-varying or directed-edge laws are outside scope. Local independence is a sufficient uniqueness hypothesis and is not claimed necessary. The general optimum value uses standard tensor spectral structure; the added contribution is the unrestricted local rigidity mechanism and its mixed-family phase consequence. A single model checked the mathematics and verifier; there has been **no independent mathematical audit**. Historical specialist overlap cannot be ruled out, including interpretations of symmetry-reduction theory not explicitly addressing full uniqueness. The earlier Microsoft May 2007 report has month-only bibliographic dating.

## References

1. S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest mixing Markov chain on graphs with symmetries*, arXiv:0709.0955, first arXiv version 2007-09-06; SIAM J. Optim. 20 (2009), 792–819. https://arxiv.org/abs/0709.0955 ; https://doi.org/10.1137/070689413
2. S. Boyd, P. Diaconis and L. Xiao, *Fastest mixing Markov chain on a graph*, SIAM Rev. 46 (2004), 667–689. https://stanford.edu/~boyd/papers/fmmc.html
3. *Algebraic Connectivity and Exact Laplacian Spectra of Generalized Graph Products*, Int. J. Eng. Sci. Technol. (2026), DOI:10.29121/ijoest.v10.i4.2026.781, https://doi.org/10.29121/ijoest.v10.i4.2026.781
