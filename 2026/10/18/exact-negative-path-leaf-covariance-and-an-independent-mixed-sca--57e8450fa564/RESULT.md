# Exact negative path–leaf covariance and an independent mixed-scale limit in recursive trees

## Finding

Consider the uniform random recursive tree on labels \(1,\ldots,n\): vertex \(1\) is the root, and for each \(j\ge2\), the parent \(K_j\) is chosen independently and uniformly from \(\{1,\ldots,j-1\}\). Write \(D_j\) for its root distance, \(T_n=\sum_{j=1}^nD_j\) for total path length, and \(L_n\) for the number of vertices with no children. Let \(H_n=\sum_{j=1}^n1/j\), and let \(\mathcal F_\infty=\sigma(K_j:j\ge2)\).

For every integer \(n\ge2\), the finite-size dependence is exactly
\[
\boxed{\operatorname{Cov}(T_n,L_n)=-\frac{n-2}{4}.}
\]
Moreover, the classical normalized path-length martingale
\[
W_n=\frac{T_n-n(H_n-1)}n
\]
converges almost surely and in \(L^2\) to a nondegenerate random variable \(W\). Although the leaf count and total path length are negatively correlated at every \(n\ge3\), their fluctuations separate asymptotically:
\[
\boxed{\left(W_n,\frac{L_n-n/2}{\sqrt{n/12}}\right)\ \Longrightarrow\ (W,Z),\qquad Z\sim N(0,1),\quad Z\perp W.}
\]
In fact the Gaussian leaf fluctuation is **mixing** relative to the whole infinite recursive-tree construction: for every bounded \(\mathcal F_\infty\)-measurable random variable \(B\) and every bounded continuous \(f\),
\[
\lim_{n\to\infty}\mathbb E\!\left[B f\!\left(\frac{L_n-n/2}{\sqrt{n/12}}\right)\right]
=\mathbb E[B]\,\mathbb E[f(Z)].
\]
This last assertion implies independence of the joint limit; it is stronger than the fact that the correlation tends to zero.

Using the known variance of the path-length limit, \(\operatorname{Var}(W)=2-\pi^2/6\), the exact covariance also yields the sharp correlation rate
\[
\operatorname{Corr}(T_n,L_n)\sim-\frac{\sqrt3}{2\sqrt{2-\pi^2/6}}\,n^{-1/2}.
\]

## Assumptions and scope

Every parent choice \(K_j\) is independent, with uniform law on the preceding labels; all trees are constructed from one infinite sequence of these choices. Leaves mean **outdegree zero**, including the root only for the one-vertex tree (which is not used). Edges count one unit of depth; the root has depth zero. The exact covariance identity is asserted for \(n\ge2\), and the Gaussian normalization for \(n\ge3\). The mixing limit keeps every test random variable \(B\) fixed as \(n\to\infty\); it is not a statement of independence at any finite tree size.

## Proof

**1. Path-length martingale and its nondegenerate limit.** The depth recursion is \(D_{n+1}=1+D_{K_{n+1}}\), whence, conditionally on the tree after \(n\) arrivals,
\[
\mathbb E[T_{n+1}\mid\mathcal F_n]=\left(1+\frac1n\right)T_n+1.
\]
Taking expectations recursively gives \(\mathbb ET_n=n(H_n-1)\). Hence \(W_n=(T_n-\mathbb ET_n)/n\) is a martingale, with exact increments
\[
W_{n+1}-W_n=\frac{D_{K_{n+1}}-T_n/n}{n+1}.
\]
For a uniform random parent, \(\mathbb ED_{K_{n+1}}^2=n^{-1}\sum_{j=1}^n\mathbb ED_j^2=O((\log(n+1))^2)\): the standard depth representation is a sum of independent Bernoulli variables with success probabilities \(1,1/2,\ldots,1/(j-1)\), or this bound follows directly by a recursion for the sum of squared depths. Thus
\[
\sum_{n\ge2}\mathbb E[(W_{n+1}-W_n)^2]<\infty.
\]
Martingale convergence proves almost-sure and \(L^2\) convergence. The variance is positive because \(W_3\) is already nonconstant and martingale increments are orthogonal; consequently \(\operatorname{Var}(W)\ge\operatorname{Var}(W_3)=1/36\). The precise known variance coefficient \(2-\pi^2/6\) is background, not required for mixing or the exact covariance.

**2. Exact covariance.** Let \(A_n\) be the sum of depths of all leaves, and let \(I_{n+1}\) indicate that the selected parent \(K_{n+1}\) was a leaf just before the insertion. Then
\[
\begin{aligned}
L_{n+1}&=L_n+1-I_{n+1},\\
A_{n+1}&=A_n+1+D_{K_{n+1}}-I_{n+1}D_{K_{n+1}},\\
T_{n+1}&=T_n+1+D_{K_{n+1}}.
\end{aligned}
\]
Conditional expectations give
\[
\mathbb E[L_{n+1}\mid\mathcal F_n]=\left(1-\frac1n\right)L_n+1,
\qquad
\mathbb E[A_{n+1}\mid\mathcal F_n]=\left(1-\frac1n\right)A_n+1+\frac{T_n}{n}.
\]
With \(L_2=A_2=1\), solving these recurrences yields, for all \(n\ge2\),
\[
\mathbb EL_n=\frac n2,\qquad
\mathbb EA_n=\frac n2H_n-\frac n4.
\]
At fixed past \(\mathcal F_n\), the conditional covariance of the two new statistics is
\[
\operatorname{Cov}(T_{n+1},L_{n+1}\mid\mathcal F_n)
=\frac{T_nL_n}{n^2}-\frac{A_n}{n}.
\]
By total covariance, writing \(c_n=\operatorname{Cov}(T_n,L_n)\),
\[
\begin{aligned}
c_{n+1}
&=\left(1-\frac1{n^2}\right)c_n+\frac{\mathbb E(T_nL_n)}{n^2}-\frac{\mathbb EA_n}{n}\\
&=c_n+\frac{\mathbb ET_n\,\mathbb EL_n}{n^2}-\frac{\mathbb EA_n}{n}\\
&=c_n-\frac14.
\end{aligned}
\]
Since \(c_2=0\), induction gives \(c_n=-(n-2)/4\) for every \(n\ge2\).

**3. Gaussian leaf fluctuation.** The leaf-count transition depends on the past only through \(L_n\):
\[
\Pr\{L_{n+1}=L_n\mid L_n\}=\frac{L_n}{n},\qquad
\Pr\{L_{n+1}=L_n+1\mid L_n\}=1-\frac{L_n}{n}.
\]
Starting from \(L_2=1\), this is exactly the Eulerian recurrence for one plus the number of descents in a uniform permutation of \(n-1\) symbols. Represent that permutation by the ranks of independent continuous uniforms \(U_1,\ldots,U_{n-1}\). Thus
\[
L_n\ \overset d=\ 1+\sum_{j=1}^{n-2}\mathbf1\{U_j>U_{j+1}\}.
\]
The stationary bounded descent indicators are 1-dependent, with mean \(1/2\), variance \(1/4\), and neighboring covariance \(1/6-1/4=-1/12\). The standard bounded 1-dependent central limit theorem gives
\[
\frac{L_n-n/2}{\sqrt{n/12}}\Longrightarrow N(0,1),
\]
and the same computation yields \(\operatorname{Var}(L_n)=n/12\) for \(n\ge3\).

**4. Asymptotic mixing and joint independence.** Fix \(m\ge2\). Split \(L_n=Y_{m,n}+R_{m,n}\) into the number \(Y_{m,n}\) of leaves with labels greater than \(m\) and the number \(R_{m,n}\) with labels at most \(m\). Necessarily \(0\le R_{m,n}\le m\). The leaf status of any label \(j>m\) depends only on parent choices \(K_{j+1},\ldots,K_n\); hence \(Y_{m,n}\) is independent of \(\mathcal F_m\). Since \(Y_{m,n}\) differs from \(L_n\) by at most \(m\), its centered, standardized version has the same normal limit for every fixed \(m\).

For a bounded \(\mathcal F_m\)-measurable \(B_m\) and bounded continuous \(f\), the independence of \(Y_{m,n}\), together with tightness and the vanishing \(m/\sqrt n\) perturbation, implies
\[
\mathbb E[B_m f((L_n-n/2)/\sqrt{n/12})]
\longrightarrow \mathbb E[B_m] \mathbb E[f(Z)].
\]
For arbitrary bounded \(B\in\mathcal F_\infty\), approximate \(B\) in \(L^1\) by \(B_m=\mathbb E[B\mid\mathcal F_m]\), and then send \(m\to\infty\). This proves the asserted mixing convergence. In particular, take \(B=g(W)\) with bounded continuous \(g\). Since \(W_n\to W\) in probability, replacing \(g(W)\) by \(g(W_n)\) costs \(o(1)\); tightness supplies joint weak convergence to independent \((W,Z)\).

The correlation asymptotic follows from the exact covariance, \(\operatorname{Var}(L_n)=n/12\), and the known \(\operatorname{Var}(T_n)/n^2\to2-\pi^2/6\).

## Verification

Run \(\texttt{python3 CHECK.py}\) using the Python standard library. The program exhaustively enumerates every parent sequence for \(2\le n\le9\), verifying all four mixed-moment identities and the exact leaf variance with rational arithmetic. It independently checks the five conditional-moment and covariance recurrences for every integer \(2\le n<500\). A successful run prints \(\texttt{EXACT_OK 2530 assertions}\).

These finite computations are diagnostic only. The infinite covariance law is proved by the algebraic induction; the weak and mixing limits use the Eulerian representation, bounded 1-dependent CLT, and finite-prefix approximation. No simulation or finite enumeration is used to infer an asymptotic theorem.

## Relationship to prior work

Gałązka and Wdowicka (2026, arXiv:2610.00614) provide the recent total-path-length fluctuation framework, including the power-weight generalization and the known uniform-tree variance coefficient. Their stated results are marginal for total path length; they do not give the leaf-count mixing limit or the exact leaf/path covariance.

Bryc, Minda and Sethuraman (2008, arXiv:0809.4741) obtain marginal leaf-count limit theorems using a general birth-process/urn framework. Dobrow and Fill (1999) characterize the non-Gaussian total-path-length limit. Those separate marginal results alone cannot force independence of two statistics built from the same tree.

Lundblad and Wagner (2026, DOI 10.4230/LIPIcs.AofA.2026.2) analyze path length together with external (leaf) path length, and encode leaf counts and depth statistics in multivariate generating functions. Their full-text theorems concern comparisons of mean depths and associated fluctuations; they do not assert mixing on the leaf-count central-limit scale. Their generating-function formalism might nevertheless imply a finite mixed moment such as the covariance found here; the new joint mixing assertion is the substantive distinction.

Two published recursive-tree comparisons concern the degree of the distinguished root jointly with total leaves, and the same root degree jointly with total path length. Neither pair determines the joint law or covariance of leaf count and path length, and their normalized fluctuation scales differ from the present normal/non-Gaussian mixing pair.

## Limitations

The theorem is for **uniform attachment**; the leaf law changes for nonuniform deterministic weights. Mixing concerns a fixed bounded random variable of the infinite growth history, not a triangular sequence of observables selected after seeing \(n\). The exact covariance does not assert finite-size independence. The Gaussian limit is ordinary weak convergence, not a quantitative rate. The full 1999 primary article was not accessible during source comparison; older work combining the path-length and degree-profile processes may affect priority. No independent audit or priority certification has been performed.

## References

1. M. Gałązka and H. Wdowicka, *Total Path Length in Power-Weight Recursive Trees: Martingale Limits and Global Fluctuations* (2026), arXiv:2610.00614, first public September 30, 2026. https://arxiv.org/abs/2610.00614
2. W. Bryc, D. Minda and S. Sethuraman, *Large deviations for the leaves in some random trees* (2008), arXiv:0809.4741. https://arxiv.org/abs/0809.4741
3. R. P. Dobrow and J. A. Fill, *Total path length for random recursive trees*, Combinatorics, Probability and Computing 8 (1999), 317–333. https://doi.org/10.1017/S0963548399003855
4. J. Lundblad and S. Wagner, *Path Length and External Path Length in Random Trees*, AofA 2026, article 2. https://doi.org/10.4230/LIPIcs.AofA.2026.2
5. Relevant published records: *Equal-share covariance of root degree and leaves in a random recursive tree*, and *Root attachments have an exact negative path-length profile in random recursive trees*, published-finding corpus (2026), identifiers 2026/10/4/SCOPE-equal-share-covariance-of-root-degree-and-leaves-in-a-random-rec--ab0acf44833f and 2026/10/4/SCOPE-root-attachments-have-an-exact-negative-path-length-profile-in-r--3b3e0426b1ba.
