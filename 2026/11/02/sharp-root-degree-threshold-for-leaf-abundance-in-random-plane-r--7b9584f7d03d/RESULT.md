# Sharp root-degree threshold for leaf abundance in random plane recursive trees

## Finding

For a uniformly chosen increasing rooted plane tree on \(n\ge3\) labeled vertices, let \(R_n\) count children of the root and \(L_n\) count all leaves (vertices having zero children). Put \(m=n-1\). The exact conditional leaf-count regression, for **every** \(1\le r\le m\), is

\[\boxed{\mathbb E[L_n\mid R_n=r]=\frac{2m+r}{3}-\frac{2(r+1)(m-r)}{3(2m-r-1)}.}\]

Since \(\mathbb E L_n=(2n-1)/3\), the exact bias is

\[\boxed{\mathbb E[L_n\mid R_n=r]-\mathbb E L_n=\frac{(r+1)^2-4(n-1)}{3(2n-r-3)}.}\]

Its sign changes sharply at root degree \(r+1=2\sqrt{n-1}\): the conditional mean is below, equal to, or above its unconditional value according as this expression is smaller, equal, or larger. Exact equality is possible precisely when \(n=k^2+1\) and \(r=2k-1\) for an integer \(k\ge2\). The conditional mean is strictly increasing in root degree. In addition,

\[\operatorname{Cov}(R_n,L_n)=\frac13\left(\frac{4^{n-1}}{\binom{2n-2}{n-1}}-2\right)>0.\]

Thus the covariance grows as \(\sqrt{\pi n}/3\), even though the Pearson correlation tends to zero as \(\sqrt{\pi/(4-\pi)}\,n^{-1/2}\).

## Assumptions and scope

An increasing rooted plane tree has labels \(1,\ldots,n\), with smaller labels along every path out of the root; the children at every vertex are linearly ordered. Each such tree has the same probability. Equivalently, start from root label \(1\) and insert label \(t+1\) uniformly among the \(2t-1\) available ordered-child gaps of the size-\(t\) tree. There are \((2n-3)!!\) trees of size \(n\). The root has at least one child for \(n\ge2\), and every \(r\in\{1,\ldots,n-1\}\) has positive probability. A leaf has no children, so the root is not a leaf for \(n\ge2\). The theorem excludes the degenerate \(n=2\) case because its rational closed form contains an endpoint denominator zero; at \(n=2\), both statistics equal one deterministically. No asymptotic approximation is used in the finite-size formulas.

## Proof

**1. Exact fixed-root-degree regression.** Let \(T(z,u)\) be the exponential generating function of increasing plane trees, with \(u\) marking leaves and \(z\) marking vertices. The standard recursive insertion decomposition of an increasing plane tree gives

\[\frac{\partial T}{\partial z}=u+\frac{T}{1-T},\qquad T(0,u)=0.\]

At \(u=1\), solve for \(T_0(z)=T(z,1)=1-\sqrt{1-2z}\). Differentiating the differential equation with respect to \(u\), and writing \(U(z)=\partial_u T(z,u)|_{u=1}\), gives

\[U'(z)=1+\frac{U(z)}{(1-T_0(z))^2},\quad U(0)=0,\qquad U(z)=\frac{(1-2z)^{-1/2}-(1-2z)}3.\]

Consequently,

\[U(z)=\frac{T_0(z)}3\left(2-T_0(z)+\frac1{1-T_0(z)}\right).\]

An increasing plane tree whose root has exactly \(r\) ordered child branches is counted by the coefficient of \(T(z,u)^r\), with the root removed. Set \(m=n-1\) and \(A_{m,r}=[z^m]T_0(z)^r\). Lagrange inversion applied to \(z=T_0-T_0^2/2\) yields, for \(1\le r\le m\),

\[A_{m,r}=\frac rm\binom{2m-r-1}{m-r}2^{-(m-r)}>0.\]

Therefore the conditional mean equals

\[\mathbb E[L_n\mid R_n=r]=\frac{[z^m]rT_0^{r-1}U}{A_{m,r}}.\]

The coefficient identities

\[\frac{A_{m,r+1}}{A_{m,r}}=\frac{2(r+1)(m-r)}{r(2m-r-1)},\qquad \frac{[z^m]T_0^r/(1-T_0)}{A_{m,r}}=\frac{2m-r}{r}\]

follow from the displayed Lagrange formula and from \(\frac{d}{dz}T_0^{r+1}=(r+1)T_0^r/(1-T_0)\). Substitution proves the first boxed formula. Taking the known (or directly derived below) unconditional mean \((2m+1)/3\) and simplifying proves the second boxed formula. All denominators are positive for \(m\ge2\), \(1\le r\le m\): \(2m-r-1\ge m-1>0\).

**2. Strict monotonicity and threshold.** Let \(f_m(r)\) denote the conditional mean just found. Direct rational simplification gives, for each \(1\le r<m\),

\[f_m(r+1)-f_m(r)=\frac{(m-r)(4r+2)+(r-1)(3r+2)}{3(2m-r-1)(2m-r-2)}>0.\]

The first numerator summand is strictly positive and all denominator factors are positive. The sign of the conditional bias is therefore the sign of \((r+1)^2-4m\). Exact zero requires \(m=k^2\), \(r=2k-1\); the allowed range forces \(k\ge2\). At the largest possible degree \(r=m\), the first formula yields \(\mathbb E[L_n\mid R_n=m]=m\), as it must for the star.

**3. Exact covariance from the insertion process.** At size \(t\ge2\), define \(W_t=R_t+1\) and let \(d_t=2t-1\) be the total gap count. Exactly \(W_t\) gaps attach a new vertex to the root, and exactly \(L_t\) gaps attach to leaves. These sets are disjoint. Let \(X_t\) and \(Y_t\) indicate these two events. Then

\[W_{t+1}=W_t+X_t,\qquad L_{t+1}=L_t+1-Y_t,\]

with \(\Pr(X_t=1\mid\mathcal F_t)=W_t/d_t\), \(\Pr(Y_t=1\mid\mathcal F_t)=L_t/d_t\), and \(X_tY_t=0\). Taking expectations gives

\[\mathbb E W_{t+1}=(1+d_t^{-1})\mathbb E W_t,\quad \mathbb E W_2=2,\qquad \mathbb E L_t=\frac{2t-1}{3}.\]

The first recurrence solves to

\[w_t:=\mathbb E W_t=\frac{4^{t-1}}{\binom{2t-2}{t-1}}.\]

Writing \(c_t=\operatorname{Cov}(W_t,L_t)=\operatorname{Cov}(R_t,L_t)\), the law of total covariance gives

\[c_{t+1}=(1-d_t^{-2})c_t+\frac{\mathbb E(W_tL_t)}{d_t^2}=c_t+\frac{w_t}{3d_t}=c_t+\frac{w_{t+1}-w_t}{3}.\]

The middle equality uses \(\mathbb E L_t=d_t/3\), while the last uses the recurrence for \(w_t\). Since \(c_2=0\), telescoping yields \(c_n=(w_n-2)/3\). Because \(w_3=8/3\) and \(w_t\) increases, the covariance is strictly positive for \(n\ge3\).

For the asymptotic correlation statement, the same insertion recurrence gives \(\mathbb E[W_n(W_n+1)]=2(2n-1)\), hence

\[\operatorname{Var}(R_n)=4n-2-w_n-w_n^2.\]

The leaf update yields \(\mathbb E[L_{t+1}^2\mid L_t]=(1-2/d_t)L_t^2+(2-1/d_t)L_t+1\) and thus, with the size-two initial condition,

\[\operatorname{Var}(L_n)=\frac{2n(n-2)}{9(2n-3)}.\]

Finally \(w_n\sim\sqrt{\pi n}\) by the central binomial coefficient asymptotic. Therefore \(\operatorname{Var}R_n\sim(4-\pi)n\), \(\operatorname{Var}L_n\sim n/9\), and the claimed covariance and correlation asymptotics follow.

## Verification

The included Python standard-library checker `verify.py` separately enumerates every labeled increasing ordered tree for \(2\le n\le8\), and separately implements exact integer-count recursions for the joint \((R_n,L_n)\) distribution through \(n=60\). It checks each exact conditional mean for all feasible root degrees; threshold signs; the adjacent regression increment; leaf and root moments; the covariance; and exact tree counts. It completed 7,374 exact assertions successfully when executed from the packaged file. These finite checks are diagnostic; the unrestricted theorem is proved by the coefficient and insertion arguments above.

## Relationship to prior work

Mahmoud, Smythe and Szymański (1993) established the PORT insertion model and exact marginal mean/variance of leaves, as well as root-degree moments. Janson (2008) established the equivalent Stirling-permutation picture: leaves correspond to plateaux, and root outdegree to the number of top-level factors (his Example 1.6). His urn covariance theorem concerns ascents, descents, and plateaux, not the factor-count/plateau pair. The root-degree/leaf *conditional regression* and sharp sign boundary are not consequences of either marginal law separately. Acan and Hitczenko (first public preprint November 21, 2014) simplify asymptotic covariance matrices for *counts of vertices of fixed outdegree*, rather than the joint behavior of the distinguished root outdegree and the global leaf count. Kuba and Panholzer (2006) study root/label degree distributions in increasing trees, including generating-function tools from which degree marginals can be obtained; their studied statements do not give the mixed root-degree/leaf regression. Janson's random-tree degree-count limit results likewise concern different joint observables. The standard increasing-tree generating-function machinery is acknowledged as the method and is not itself new. A matching exact conditional theorem was not found in the inspected material or targeted searches; this is not an exhaustive proof of priority.

## Limitations

This is a self-review, not independent validation. The claim concerns the uniformly distributed plane-oriented **increasing** recursive tree, not all preferential-attachment laws or the uniform-parent recursive tree. It gives a conditional *mean* and covariance, not conditional stochastic ordering of the entire leaf-count distribution. The covariance asymptotic alone does not imply independence. Historical implicit derivation from broader multivariate increasing-tree generating functions cannot be excluded; results should be checked by independent specialists before publication. The discrete threshold is finite-sample and is valid only for the stated integer domain.

## References

- H. M. Mahmoud, R. T. Smythe, and J. Szymański, “On the Structure of Random Plane-oriented Recursive Trees and Their Branches,” *Random Structures & Algorithms* **4** (1993), 151–176, https://doi.org/10.1002/rsa.3240040204.
- S. Janson, “Plane recursive trees, Stirling permutations and an urn model,” arXiv:0803.1129, first posted 2008-03-07, https://arxiv.org/abs/0803.1129; *Discrete Mathematics & Theoretical Computer Science Proceedings* AI (2008), 541–547.
- H. Acan and P. Hitczenko, “On the covariances of outdegrees in random plane recursive trees,” arXiv:1411.5756, first posted 2014-11-21, https://arxiv.org/abs/1411.5756; subsequently *Journal of Applied Probability* **52** (2015), 904–907.
- M. Kuba and A. Panholzer, “On the Degree Distribution of the Nodes in Increasing Trees,” 2006, https://paperzz.com/doc/7154780/on-the-degree-distribution-of-the-nodes-in-increasing-trees.
- S. Janson, “Asymptotic degree distribution in random recursive trees,” *Random Structures & Algorithms* **26** (2005), 69–83, https://doi.org/10.1002/rsa.20046.
