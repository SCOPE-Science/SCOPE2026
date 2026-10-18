# Every fastest-mixing kernel on complete split graphs

## Finding
For integers \(r,s\ge 2\), let \(G_{r,s}=K_r\vee\overline{K_s}\) be the complete split graph: a clique of size \(r\), an independent set of size \(s\), and every edge between them. Consider **all** real symmetric, entrywise nonnegative, row-stochastic transition matrices supported by the edges and diagonal of this graph. Their convergence criterion is the second-largest eigenvalue modulus \(\mu(P)=\|P-\mathbf1\mathbf1^T/(r+s)\|_2\).

Define
\[
(x,\mu)=\begin{cases}
\bigl(2/(s+2r),\ s/(s+2r)\bigr),&s\le 2r,\\
\bigl(1/s,\ 1-r/s\bigr),&s\ge 2r,
\end{cases}\qquad c=1-sx.
\]
The two formulas agree at \(s=2r\). **The complete set of globally optimal kernels** consists exactly of
\[
P=\begin{pmatrix}
A & x\mathbf1_r\mathbf1_s^T\\
x\mathbf1_s\mathbf1_r^T &(1-rx)I_s
\end{pmatrix},
\]
where \(A\in\mathbb R^{r\times r}\) is symmetric and entrywise nonnegative, \(A\mathbf1_r=c\mathbf1_r\), and its restriction to \(U_r=\{u:\mathbf1_r^Tu=0\}\) has every eigenvalue in \([-\mu,\mu]\). Every such kernel has \(\mu(P)=\mu\). In particular, **every optimal kernel has the same individual clique-to-independent transition probability** \(x\), even without any symmetry assumption on the kernel.

Let \(T(P)=\sum_{1\le i<j\le r}P_{ij}\) be the total probability assigned to distinct edges within the clique. Across all global optimizers, its set of attainable values is exactly the closed interval
\[
\boxed{\quad\max\{0,\tfrac{r-1}{2}(c-\mu)\}\ \le T(P)\le\
\min\{\tfrac{rc}{2},\tfrac{r-1}{2}(c+\mu)\}.\quad}
\]
Consequently, three sharp phases occur: if \(s<r\), every optimum uses some clique edge; if \(r\le s<2r\), optima exist both with and without clique edges; if \(s\ge2r\), **every optimum deletes every clique edge**, and the entire optimal transition matrix is unique. All statements concern ordinary nonnegative Markov kernels, not signed consensus weights.

## Assumptions and scope
All graph orders \(r,s\) are integers at least \(2\); all transitions, including holding probabilities, are nonnegative; row sums equal \(1\); transitions across nonedges are zero; and the transition matrix is symmetric, hence uniform-stationary. There is no condition that the chain be initially irreducible or have positive weights on every permitted edge. The optimal kernels obtained here are mixing, since \(0<\mu<1\). Eigenvalues are counted on the orthogonal complement of the all-ones vector. The claim is the **full optimizer-face characterization and its internal-edge consequences**; the minimum SLEM itself is already implied by published clique-lift results.

## Proof
**1. Symmetry reduction and optimal value.** For any feasible matrix \(P\), its average over all permutations of the clique and all permutations of the independent vertices remains feasible; convexity of \(\|P-J\|_2\), where \(J=\mathbf1\mathbf1^T/(r+s)\), means averaging cannot increase the objective. An invariant matrix has cross-edge weight \(a\), clique-edge weight \(b\), and row sums impose \(0\le a\le\min\{1/r,1/s\}\) and \(0\le b\le(1-sa)/(r-1)\). Decomposing into the constant vector, independent-set differences, clique differences, and the between-parts contrast gives eigenvalues respectively
\[
1,\qquad 1-ra\quad(s-1\text{ times}),\qquad
1-sa-rb\quad(r-1\text{ times}),\qquad1-(r+s)a.
\]
The choice \(b=(1-sa)/r\) makes the clique-difference eigenvalue zero and is always feasible. Therefore minimizing SLEM among invariant kernels is equivalent to minimizing \(\max\{1-ra,(r+s)a-1\}\) on the admissible interval. Its unique minimum occurs at \(a=2/(s+2r)\) when \(s\le2r\), and at the boundary \(a=1/s\) when \(s\ge2r\). This gives the displayed \(x,\mu\). Every global optimum must have **average cross-edge weight** \(x\), since its averaged matrix is optimal and the minimizing \(a\) is unique.

**2. Rigidity of every cross edge when \(s\le2r\).** Write an arbitrary global optimum in block form \(P=\left(\begin{smallmatrix} A&B\\B^T&D\end{smallmatrix}\right)\). Its lower-right block \(D\) is diagonal because the \(s\) vertices are independent. The total sum of entries in \(B\) is \(rsx\). Let \(z=(s\mathbf1_r,-r\mathbf1_s)^T\), which is perpendicular to \(\mathbf1\). The quadratic form depends only on between-parts transitions, so
\[
\frac{z^TPz}{z^Tz}=1-(r+s)x=-\mu.
\]
The spectral lower bound \(P-J\succeq-\mu I\) is saturated; hence \(Pz=-\mu z\). Componentwise this forces every row sum of \(B\) to be \(sx\) and every column sum to be \(rx\). Thus \(D=(1-rx)I_s=\mu I_s\). For any \(v\perp\mathbf1_s\), the vector \((0,v)^T\) attains the Rayleigh quotient \(\mu\), the maximum permitted on \(\mathbf1^\perp\). It is therefore an eigenvector of \(P\), so \(Bv=0\). The rows of \(B\) are constant over columns, and the known column sums give \(B=x\mathbf1_r\mathbf1_s^T\).

**3. Rigidity when \(s>2r\).** The total sum of entries in \(B\) is now \(rsx=r\). Each clique-vertex row has at most unit mass available to cross edges. Since the total of its \(r\) row capacities is saturated, every clique vertex devotes all mass to cross edges. Thus its holding probability and all within-clique edge weights vanish: \(A=0\); the row sums of \(B\) are all \(1\). Write \(t_j=\sum_i B_{ij}\), so \(D=\operatorname{diag}(1-t_j)\), with \(\sum_j(1-t_j)=s-r=s\mu\). On \(U_s\), the compression of \(D\) has all eigenvalues at most \(\mu\), by the global spectral constraint. Its trace equals \((s-1)\sum_j(1-t_j)/s=(s-1)\mu\). Therefore this compression is identically \(\mu I_{U_s}\). Every \((0,v)^T\), \(v\in U_s\), saturates the upper Rayleigh bound and hence satisfies \(Bv=0\). Every row of \(B\) is constant, and its row sum is \(1\), giving \(B=x\mathbf1_r\mathbf1_s^T\), with \(x=1/s\). The boundary \(s=2r\) was already handled in step 2.

**4. All remaining freedom.** Once \(B=x\mathbf1_r\mathbf1_s^T\), symmetry and stochasticity give \(D=(1-rx)I_s\) and \(A\mathbf1_r=c\mathbf1_r\). The orthogonal decomposition into global constants, the between-parts contrast, independent-set differences, and clique differences is now invariant. Its nontrivial eigenvalues are \(1-(r+s)x\), \(1-rx\), and precisely the eigenvalues of \(A|_{U_r}\). The first two have modulus at most \(\mu\) and at least one has modulus \(\mu\). Thus the proposed conditions on \(A\) are **necessary and sufficient** for global optimality, including the case \(c=0\), where entrywise nonnegativity forces \(A=0\).

**5. Exact internal-edge interval.** Since \(A\) is symmetric and has eigenvalue \(c\) on constants, \(\operatorname{tr}(A)-c=(r-1)c-2T\). Its other \(r-1\) eigenvalues lie in \([-\mu,\mu]\), yielding \((r-1)(c-\mu)/2\le T\le(r-1)(c+\mu)/2\). Entrywise nonnegativity also gives \(T\ge0\) and \(\operatorname{tr}(A)=rc-2T\ge0\). These yield the displayed bounds. Both endpoints and every value between them are attained by the invariant core matrix \(A=(c-ry)I_r+y\mathbf1_r\mathbf1_r^T\), with \(y=2T/(r(r-1))\); its offdiagonal entries are \(y\ge0\), its diagonal entries are \(c-(r-1)y\ge0\), and its difference eigenvalue is \(c-ry\in[-\mu,\mu]\). Finally, \(c>\mu\) exactly when \(s<r\), \(0<c\le\mu\) exactly when \(r\le s<2r\), and \(c=0\) exactly when \(s\ge2r\), proving the three phases and uniqueness in the last phase.

## Verification
The standalone `check_split_face.py` uses exact rational entries and symbolic matrix operations. It independently checks all block eigenvector identities, stochasticity, sharp \(T\) endpoints, and phase cases for \(2\le r\le8\) and \(2\le s\le16\) (217 endpoint/midpoint test instances), six full characteristic polynomials, four compulsory-edge counterchecks, and eight non-invariant optimal-core perturbations. Invoke with `python check_split_face.py` in an environment containing `numpy` and `sympy`. These finite tests verify algebraic examples; the arbitrary-size theorem follows from the proof above, not enumeration.

## Relationship to prior work
Boyd, Diaconis, Parrilo and Xiao (arXiv:0709.0955, Section 3.1.2 and Section 5) develop symmetry reduction and solve the complete-bipartite fastest-mixing **value**, which agrees with the complete-split value when the independent set is not smaller than the clique. Jafarizadeh, *Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs and Subgraphs* (arXiv:2501.02421, Theorem 1 and Section 6.5; journal article cited there as 2020) establishes a stronger prior fact: a complete split graph is a clique lift of a star; its theorem and star formulas already imply the optimal \(\mu\) for **all** \(r,s\) and construct one optimal kernel. Those values and that construction are **not claimed as new**. The new claim is the complete characterization of **every** symmetric uniform-stationary optimal transition matrix without assuming its weights are invariant, including forced uniformity of all cross edges, the exact feasible core spectral face, and the sharp mandatory/optional/forbidden internal-edge phases. The cited prior statements give existence and optimal value, not these universal equality conditions. The proof here derives them from extremal Rayleigh-vector rigidity and compression-trace equality, rather than treating lack of a matching title as evidence.

## Limitations
This is an exact result for undirected complete split graphs with symmetric, nonnegative Markov kernels and uniform stationary distribution. It does not classify nonreversible kernels, nonuniform stationary distributions, weighted support graphs, or optimization of finite-time total-variation mixing. The non-invariant core matrices are described exactly by an eigenvalue interval rather than an entrywise parametrization. Although the closest full texts were inspected, an unindexed prior treatment of equality cases could exist. The proof is self-contained and the numerical script is not a formal proof checker.

## References
1. S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1, publicly submitted 2007-09-06, https://arxiv.org/abs/0709.0955 .
2. S. Jafarizadeh, *Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs and Subgraphs*, arXiv:2501.02421v1, publicly submitted 2025-01-05 (its arXiv record identifies an IEEE journal version from 2020), https://arxiv.org/abs/2501.02421 .
3. S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, https://doi.org/10.1137/S0036144503423264 .
