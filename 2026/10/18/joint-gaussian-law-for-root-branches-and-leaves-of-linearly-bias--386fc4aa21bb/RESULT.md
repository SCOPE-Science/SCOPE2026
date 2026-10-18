# Joint Gaussian law for root branches and leaves of linearly biased Hoppe trees

## Finding

**Theorem (critical root-attraction regime).** Let \(T_n\) be a Hoppe recursive tree with \(n\ge2\) labeled vertices, rooted at vertex 1. The root has weight \(\theta_n>0\), every nonroot vertex has weight 1, and each vertex attaches, on arrival, to an earlier vertex with probability proportional to its weight. Let \(B_n\) count children of the root (equivalently, first-generation branches), and let \(L_n\) count nonroot leaves. Suppose \(\theta_n/n\longrightarrow c\in(0,\infty)\). Then

\[
\frac{1}{\sqrt n}\begin{pmatrix}B_n-\mathbb E B_n\\L_n-\mathbb E L_n\end{pmatrix}
\xrightarrow{\mathrm d}\mathcal N_2(0,\Sigma_c),
\qquad
\Sigma_c=\begin{pmatrix}U(c)&K(c)\\K(c)&V(c)\end{pmatrix},
\]

where

\[
U(c)=c\left(\log(1+1/c)-\frac{1}{c+1}\right),\qquad
K(c)=\frac{c}{2(c+1)^2},\qquad
V(c)=\frac{6c^2+4c+1}{12(c+1)^3}.
\]

For every \(c>0\), \(\Sigma_c\) is strictly positive definite and its off-diagonal entry is strictly positive. Thus the two limiting Gaussian fluctuations are dependent, with limiting correlation \(K(c)/\sqrt{U(c)V(c)}\in(0,1)\).

Two exact finite-size identities, useful for checking the normalization, are

\[
\mathbb E L_n=\frac{n-1}{2}+\frac{\theta_n(n-1)}{2(\theta_n+n-2)},\qquad
\operatorname{Cov}(B_n,L_n)=\frac{\theta_n(n-1)(n-2)}{2(\theta_n+n-2)^2}.
\]

Here the parameter \(\theta_n\) is held fixed during the construction of the size-\(n\) tree; it may differ between sizes. The exact mean of \(L_n\) is established in Leckey--Neininger [1]; the finite covariance is an elementary consequence of this mean and the model's attachment law, and is *not* asserted to be the central novelty. The contribution assessed here is the nondegenerate **joint** limit at \(\theta_n\asymp n\), with all three explicit covariance entries.

## Assumptions and scope

For each fixed \(n\), vertex 2 attaches to the root. At stage \(j\ge2\), the existing \(j\) vertices have total attachment weight \(d_j=\theta_n+j-1\); vertex \(j+1\) chooses its parent independently of previous random choices, conditional on the available vertex weights. Root weight is \(\theta_n\) throughout that tree. A nonroot vertex is a leaf when its outdegree is zero. The root is never a leaf after stage 2.

The limiting regime requires \(\theta_n/n\to c\) with a strictly positive, finite \(c\); it does not assert an equivalent limit for fixed \(\theta\), \(\theta_n=o(n)\), or \(\theta_n/n\to\infty\). The centerings are the **exact finite-size expectations**, not merely first-order equivalents. Indeed
\[
\mathbb E B_n=1+\sum_{j=2}^{n-1}\frac{\theta_n}{\theta_n+j-1},
\quad\frac{\mathbb E B_n}{n}\to c\log(1+1/c),\quad
\frac{\mathbb E L_n}{n}\to\frac{1+2c}{2(1+c)}.
\]

## Proof

Write \(\theta=\theta_n\) for a fixed row. Let \(\mathcal F_j\) be the full attachment history through stage \(j\), and let \(I_{j+1}\) indicate attachment of vertex \(j+1\) to the root, while \(J_{j+1}\) indicates attachment to a *nonroot leaf*. These events are disjoint. Define
\[
p_j=\mathbb E[I_{j+1}\mid\mathcal F_j]=\frac{\theta}{d_j},\qquad
q_j=\mathbb E[J_{j+1}\mid\mathcal F_j]=\frac{L_j}{d_j}.
\]
Then \(B_{j+1}=B_j+I_{j+1}\) and \(L_{j+1}=L_j+1-J_{j+1}\). Starting from \(B_2=L_2=1\), taking expectations in the leaf recursion gives
\[
\mu_j:=\mathbb E L_j=\frac{j-1}{2}+\frac{\theta(j-1)}{2(\theta+j-2)}.
\]
The identity is exact at every \(j\ge2\). The analogous root recursion gives the claimed expectation of \(B_n\).

Define centered, bounded martingale differences
\[
\xi^B_{j+1}=I_{j+1}-p_j,\qquad
\xi^L_{j+1}=-(J_{j+1}-q_j).
\]
The centered leaf recursion is \(L_{j+1}-\mu_{j+1}=(1-1/d_j)(L_j-\mu_j)+\xi^L_{j+1}\). Since
\[
\prod_{t=j+1}^{n-1}(1-1/d_t)=\frac{d_j}{\theta+n-2},
\]
we obtain the **exact terminal martingale decomposition**
\[
\begin{pmatrix}B_n-\mathbb E B_n\\ L_n-\mathbb E L_n\end{pmatrix}
=\sum_{j=2}^{n-1}
\begin{pmatrix}\xi^B_{j+1}\\b_{j,n}\xi^L_{j+1}\end{pmatrix},
\qquad b_{j,n}=\frac{\theta+j-1}{\theta+n-2}\in(0,1].
\]
Because \(I_{j+1}J_{j+1}=0\), the conditional covariance of the increment is
\[
\begin{pmatrix}
p_j(1-p_j)&b_{j,n}p_jq_j\\
b_{j,n}p_jq_j&b_{j,n}^{2}q_j(1-q_j)
\end{pmatrix}.
\]
In particular the **positive** cross sign follows from the negative sign in \(\xi^L\) and mutually exclusive attachment choices. By the law of total variance and the conditional mean recursion,
\[
\operatorname{Var}(L_{j+1})=(1-2/d_j)\operatorname{Var}(L_j)
+\bar q_j(1-\bar q_j),\qquad \bar q_j=\mu_j/d_j.
\]
Since \(d_j>1\), this implies \(\operatorname{Var}(L_j)\le(j-2)/4\) for all \(j\ge2\). Thus, whenever \(\theta_n/n\to c>0\),
\[
\max_{2\le j<n}\mathbb E|q_j-\bar q_j|
\le\frac{\sqrt n}{2(\theta_n+1)}=O(n^{-1/2}).
\]
Also, uniformly for grid points \(j/n\in[0,1]\),
\[
p_j\longrightarrow p(x)=\frac{c}{c+x},\quad
\bar q_j\longrightarrow q(x)=\frac{x(x+2c)}{2(c+x)^2},\quad
b_{j,n}\longrightarrow b(x)=\frac{c+x}{c+1}.
\]
Consequently, by uniform continuity and the preceding \(L^1\) bound, each normalized predictable quadratic/cross-variation sum converges in probability to the corresponding Riemann integral
\[
\Sigma_c=\int_0^1
\begin{pmatrix}p(1-p)&bpq\\bpq&b^2q(1-q)\end{pmatrix}\,dx.
\]
Elementary antiderivatives give
\[
\int_0^1p(1-p)\,dx
=c[\log(1+1/c)-(c+1)^{-1}],
\quad\int_0^1bpq\,dx=\frac{c}{2(c+1)^2},
\]
\[
\int_0^1 b^2q(1-q)\,dx
=\frac{1}{4(c+1)^2}\left[\frac{(c+1)^3-c^3}{3}-\frac{c^3}{c+1}\right]
=\frac{6c^2+4c+1}{12(c+1)^3}.
\]
Each martingale increment has Euclidean norm at most \(\sqrt2\), so after scaling by \(n^{-1/2}\), the conditional Lindeberg condition is automatic. Applying the martingale central limit theorem to every deterministic linear combination, followed by Cramér--Wold, proves the claimed bivariate Gaussian convergence.

Finally, for any \(x>0\), the three possible attachment categories (root, nonroot leaf, nonroot nonleaf) have limiting probabilities
\[
p(x)>0,\quad q(x)>0,\quad 1-p(x)-q(x)=\frac{x^2}{2(c+x)^2}>0.
\]
Their covariance matrix after the invertible diagonal scale \(\operatorname{diag}(1,-b(x))\) is positive definite. Integrating over \(x\in(0,1]\) proves positive definiteness of \(\Sigma_c\).

For the exact cross-covariance, letting \(C_j=\operatorname{Cov}(B_j,L_j)\) and using conditional covariance gives
\[
C_{j+1}=\left(1-\frac1{d_j}\right)C_j+\frac{\theta\mu_j}{d_j^2},\qquad C_2=0.
\]
Inserting the exact formula for \(\mu_j\) and simplifying by induction yields
\[
C_n=\frac{\theta(n-1)(n-2)}{2(\theta+n-2)^2}.
\]
This finite identity independently checks \(C_n/n\to K(c)\). It is not used as a substitute for the joint weak-convergence argument. For \(n>2\), elementary differentiation also shows that the finite covariance is uniquely maximized at \(\theta=n-2\); this optimizer is auxiliary and not a separate novelty claim.

## Verification

Run `python3 verify_hoppe.py` using Python's standard library. The program exhausts all parent-choice histories for \(2\le n\le7\) at \(\theta\in\{1/3,1,5/2\}\), computes exact rational probabilities and moments, and checks the displayed finite means and cross-covariance. It separately checks six deterministic covariance Riemann sums at \(n\in\{1000,10000\}\) and \(c\in\{1/4,1,3\}\), and verifies positive definiteness for these parameter values. A successful run prints `VERIFY_OK`. These finite checks are not evidence of a central limit theorem without the preceding martingale argument.

## Relationship to prior work

Leckey and Neininger [1, Theorem 2.5 and its proof] give the leaf expectation and a marginal central limit theorem for **fixed** root weight \(\theta\). Their fixed-parameter asymptotic formula for the leaf variance is not uniform enough to substitute \(\theta=cn\), and no joint branch/leaf limit is stated there. Hiesmayr and Işlak [2, Sections 3 and 6] study marginal leaf statistics and marginal branch-count central limits for a fixed weighted recursive-tree scheme, and explicitly include Hoppe trees as a subcase. Their root-branch marginal CLT does not imply a joint leaf/branch CLT; their results do not state this triangular regime or its off-diagonal covariance. The new regime \(\theta_n/n\to c>0\) is distinct from the ordinary fixed-\(\theta\) uniform-recursive limit. The root-branch count may also be called the Hoppe-urn first-generation family count or Chinese-restaurant table count; the nonroot leaf statistic is not the table count.

## Limitations

Only a strictly positive, finite limit \(c\) is proved. The parameters of different trees may depend on sample size, but the attachment weights remain constant within a given tree. No quantitative rate in Gaussian distance is proved, and no uniformity as \(c\to0\) or \(c\to\infty\) is claimed. Numerical checks examine finitely many cases and do not verify the infinite martingale theorem. A possible broader unpublished or unlocated multivariate weighted-tree result could affect historical priority; the claim is not independently audited.

## References

[1] K. Leckey and R. Neininger, *Asymptotic analysis of Hoppe trees*, arXiv:1202.2439 (first posted 2012-02-11), especially Section 2, Theorem 2.5, and Section 3. https://arxiv.org/html/1202.2439v3

[2] E. Hiesmayr and Ü. Işlak, *Asymptotic results on Hoppe trees and its variations*, arXiv:1712.03572 (2017), especially Sections 3 and 6. https://arxiv.org/pdf/1712.03572

[3] P. Hall and C. C. Heyde, *Martingale Limit Theory and Its Application*, Academic Press (1980), martingale central limit theorem.
