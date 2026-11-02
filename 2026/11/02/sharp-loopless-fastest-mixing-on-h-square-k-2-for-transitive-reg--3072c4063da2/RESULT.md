# Sharp loopless fastest mixing on \(H\square K_2\) for transitive regular graphs

## Finding
Let \(H\) be any finite connected simple graph on at least two vertices, regular of degree \(d\ge1\), both vertex-transitive and edge-transitive. Write \(L_H\) for its combinatorial Laplacian, and set
\[
\alpha=\lambda_2(L_H)>0,\qquad \beta=\lambda_{\max}(L_H)\le2d,\qquad \delta=\min\{\alpha,2d-\beta\}.
\]
On the Cartesian two-layer graph \(G=H\square K_2\), consider **all** real symmetric, entrywise nonnegative, row-stochastic transition matrices \(P\) whose diagonal is zero and whose off-diagonal support is contained in the graph edges. Define the nontrivial eigenvalue modulus \(\mu(P)=\|P-J/(2|V(H)|)\|_2\), where \(J\) is the all-ones matrix. Then
\[
\boxed{\min_P\mu(P)=\frac{2d-\delta}{2d+\delta}.}
\]
A globally minimizing chain puts probability \(x_*=2/(2d+\delta)\) on **each** edge within either copy of \(H\), and probability \(y_*=\delta/(2d+\delta)\) on **each** matched interlayer edge. When \(H\) is nonbipartite, \(\delta>0\), the minimizer is unique within the family invariant under the natural simultaneous automorphisms of \(H\) and interchange of the two layers; no uniqueness is asserted for unrestricted matrices. When \(H\) is bipartite, \(\delta=0\), every feasible loopless chain has \(\mu(P)=1\) and cannot mix to the uniform distribution.

The exact comparison with **holding-allowed** symmetric chains is also explicit. Their optimal modulus is
\[
\mu_{\mathrm{hold}}=1-\frac{2\alpha}{\max\{\beta+2\alpha,2d+\alpha\}}.
\]
The cost of forbidding holding is zero precisely when \(\alpha+\beta\le2d\); when \(\alpha+\beta>2d\), it is strictly positive and equals
\[
\boxed{\mu_{\mathrm{loopless}}-\mu_{\mathrm{hold}}=
\frac{2\beta(\alpha+\beta-2d)}{(4d-\beta)(\beta+2\alpha)}.}
\]
The holding-allowed optimum and its criterion for a zero penalty are antecedents, not independently novel claims here. The new assertion is the full loopless global optimum, in particular its exact positive-penalty magnitude and optimizer when the holding-allowed optimum uses self-loops.

## Assumptions and scope
The row-stochastic matrix is discrete-time, reversible with uniform stationary distribution, and may assign zero probability to permitted edges. The only forbidden transitions are nonedges and self-loops. There is no a priori requirement that individual edge probabilities be identical. The matrix norm above is the spectral norm and includes every eigenvalue on the orthogonal complement of constants, even for reducible or periodic chains. The graph \(H\) is unweighted; its vertices and edges are each transitive under its automorphism group. The bound \(0<\alpha\le\beta\le2d\) follows from connected regular-graph Laplacian theory, and \(\beta=2d\) if and only if \(H\) is bipartite.

For two concrete infinite families, the theorem gives:

* For \(H=K_m\), \(m\ge3\), the graph is two cliques joined by a perfect matching, and \(\delta=m-2\). The no-holding optimum is \(m/(3m-4)\), with within-clique probability \(2/(3m-4)\) per neighbor and matching probability \((m-2)/(3m-4)\). The holding-allowed optimum is \(1/3\), giving exact penalty \(4/[3(3m-4)]\).
* For \(H=J(n,2)\), the Johnson graph on two-element subsets, \(n\ge4\), \(d=2(n-2)\), \(\alpha=n\), and \(\beta=2(n-1)\). The no-holding penalty is positive only at \(n=4,5\), zero at the sharp threshold \(n=6\) and thereafter. Its no-holding optimum is \(3/5\) for \(n=4\), \(1/2\) for \(n=5\), and \((3n-8)/(5n-8)\) for every \(n\ge6\). The equality at \(n=6\) has both branches active.

## Proof
**1. Global symmetrization.** The automorphism group of \(H\), acting simultaneously on both layers, together with layer interchange, acts transitively on each of two edge classes: edges internal to the layers and interlayer matching edges. If \(P\) is admissible, average its permutation conjugates over this finite group. The average remains symmetric, stochastic, nonnegative, zero-diagonal and supported on allowed edges. Since \(P\mapsto\|P-J/(2|V(H)|)\|_2\) is convex and is invariant under those conjugations, the averaged matrix has no greater modulus. Thus the unrestricted minimum equals the minimum over the two-class family. Write its internal edge probability as \(x\ge0\), its interlayer edge probability as \(y\ge0\) and its holding probability as \(c=1-dx-y\). For the loopless problem \(c=0\), so \(y=1-dx\) and \(0\le x\le1/d\).

**2. Complete spectral reduction.** The transition matrix on the two layers is
\[
P=\begin{pmatrix}cI+xA_H&yI\\yI&cI+xA_H\end{pmatrix},
\]
where \(A_H=dI-L_H\). If \(L_Hv=\lambda v\), then \((v,v)\) and \((v,-v)\) are eigenvectors with respective eigenvalues \(1-x\lambda\) and \(1-x\lambda-2y\). The sole constant eigenvalue is the first branch at \(\lambda=0\). All other eigenvalues lie between the three endpoints
\[
A=1-\alpha x,\qquad B=1-2y,\qquad C=1-\beta x-2y.
\]
Specifically \(\lambda_{\max}(P|_{\mathbf1^\perp})=\max\{A,B\}\) and \(\lambda_{\min}(P|_{\mathbf1^\perp})=C\), since \(x,y\ge0\), \(\alpha\le\beta\), and \(2y\ge0\). Hence exactly \(\mu(P)=\max\{A,B,-C\}\).

**3. Exact loopless minimax.** Substitute \(y=1-dx\) in the preceding formula:
\[
\mu(P)=\max\{1-\alpha x,\;2dx-1,\;1-(2d-\beta)x\}
=\max\{1-\delta x,\;2dx-1\},\quad 0\le x\le1/d.
\]
For \(\delta>0\), the first affine branch strictly decreases and the second strictly increases. Their unique intersection is \(x_*=2/(2d+\delta)\), which belongs to \((0,1/d)\), and their common value is \((2d-\delta)/(2d+\delta)\). The corresponding interlayer probability is \(y_*=1-dx_*=\delta/(2d+\delta)>0\). This proves the optimum and invariant-family uniqueness. For \(\delta=0\), the objective is identically one on the feasible interval. Independently, the product of two connected bipartite graphs is bipartite, and every loopless stochastic transition on a bipartite graph has eigenvalue \(-1\) on the two-color sign vector; this establishes the unrestricted statement.

**4. Independently reconstructed holding benchmark and threshold.** Allow \(c\ge0\), hence \(dx+y\le1\). For any target \(t\ge\mu(P)\), the inequalities \(A\le t\) and \(B\le t\) give \(x\ge(1-t)/\alpha\) and \(y\ge(1-t)/2\). Using \(-C\le t\) and the row budget gives, respectively,
\[
 t\ge \frac{\beta}{\beta+2\alpha},\qquad
 t\ge \frac{2d-\alpha}{2d+\alpha}.
\]
Let \(M=\max\{\beta+2\alpha,2d+\alpha\}\). The proposed holding chain \(x=2/M\), \(y=\alpha/M\), \(c=1-(2d+\alpha)/M\) is feasible, and its three spectral endpoints all have modulus at most \(1-2\alpha/M\), attaining both lower bounds. Therefore the holding expression is exact. If \(\alpha+\beta\le2d\), then \(M=2d+\alpha\), \(\delta=\alpha\), and holding is not needed. If \(\alpha+\beta>2d\), then \(M=\beta+2\alpha\), \(\delta=2d-\beta\), and the two minima are \(\beta/(\beta+2\alpha)\) and \(\beta/(4d-\beta)\). Subtraction yields the displayed strictly positive penalty. All denominators are positive because \(d>0\), \(\alpha>0\), and \(\beta\le2d\).

## Verification
The supplied `VERIFY.py` uses only the Python standard library. It constructs the actual integer-scaled transition matrices for complete-graph, Johnson-graph, Petersen-graph, cube and cycle bases, checks stochasticity and structural conditions, and compares exact characteristic polynomials by the complete set of integer power-sum traces using Newton identities. It also tests exact-rational probability grids against the analytic minimum and verifies the holding-penalty identity. In the recorded execution, all 1,177 exact assertions passed. Those finite checks are **not** substitutes for the preceding proof for arbitrary \(H\).

Reproduce by running `python VERIFY.py` in the directory containing this result and script. No external downloads, datasets, specialized solvers or pre-existing result files are needed.

## Relationship to prior work
Boyd, Diaconis and Xiao established the symmetric fastest-mixing convex/semidefinite framework; Boyd, Diaconis, Parrilo and Xiao developed edge-orbit symmetrization and Cartesian-product spectral decompositions. The latter paper's worked two-clique example connects the cliques by a **single bridge**, not a full matching. The holding-permitted two-layer problem is an existing antecedent; it does not by itself determine the no-holding optimum where the unconstrained solution holds with positive probability. The known zero-holding result for cyclic prisms \(C_n\square K_2\) covers a special case, not all transitive bases.

Olesker-Taylor and Zanetti discuss the **same** two-cliques-with-perfect-matching graph and establish an order-one optimal spectral-gap conclusion, but the inspected section gives no exact no-holding SLEM, optimizer or quantitative penalty. The unrelated study on the union of two possibly overlapping cliques concerns a different edge set, not two disjoint cliques linked by a complete matching. These are claim-and-assumption comparisons rather than a novelty inference from title mismatch.

## Limitations
Only symmetric stochastic chains and unweighted connected vertex-and-edge-transitive bases are covered. The result is about asymptotic nontrivial spectral modulus, not finite-time total-variation mixing constants, arbitrary nonreversible chains, or complete classification of all nonsymmetric optimal matrices. The bipartite case includes reducible choices because the optimum modulus is one for every admissible loopless chain. This is a self-review, not independent certification. An undiscovered equivalent specialized result could diminish originality despite the inspected comparisons.

## References
1. S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689; https://web.stanford.edu/~boyd/papers/fmmc.html . Original technical report dated February 2003 at https://statistics.stanford.edu/technical-reports/fastest-mixing-markov-chain-graph .
2. S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1, publicly posted September 6, 2007; https://arxiv.org/abs/0709.0955 and full-text HTML https://ar5iv.labs.arxiv.org/html/0709.0955 .
3. S. Olesker-Taylor and L. Zanetti, *Geometric Bounds on the Fastest Mixing Markov Chain*, Probability Theory and Related Fields 188 (2024), 1017–1062, section 1.3.4; https://doi.org/10.1007/s00440-023-01257-x .
4. M. Allison and B. L. Shader, *Fastest Mixing Markov Chain Problem for the Union of Two Cliques*, Linear and Multilinear Algebra 59 (2011), 801–823, https://doi.org/10.1080/03081087.2010.538690 (abstract inspected; full text unavailable).
