# Sharp Gaussian distance-power thresholds for two-level symmetric metric trees

## Finding

For integers \(m,k\ge2\), form the rooted unit-edge tree \(T_{m,k}\) with a root, \(m\) children (hubs), and \(k\) pendant children at each hub. The all-vertex shortest-path metric has \(N=1+m+mk\) points. Define, for a real exponent \(p\),
\[
a=2^p,\quad b=3^p,\quad c=4^p,\qquad
P_{m,k}(p)=\begin{pmatrix}
2m-(m-1)a & m(a+1)-(m-1)b-1\\
m(a+1)-(m-1)b-1 & 2ma-(m-1)c-a(1-1/k)
\end{pmatrix}.
\]

**Theorem.** There is a unique \(\alpha_{m,k}\) with
\[
1<\alpha_{m,k}<\log_2\frac{2m}{m-1},\qquad \det P_{m,k}(\alpha_{m,k})=0.
\]
For the metric \(d\) on **all** vertices, the matrices
\[
K_{\lambda,p}=\bigl(\exp(-\lambda d(u,v)^p)\bigr)_{u,v\in T_{m,k}}
\]
are positive semidefinite for **every** real \(\lambda>0\) exactly when \(0\le p\le\alpha_{m,k}\). Both branching parameters decrease this threshold strictly:
\[
\alpha_{m+1,k}<\alpha_{m,k},\qquad \alpha_{m,k+1}<\alpha_{m,k}.
\]
At the endpoint the zero-sum powered-distance quadratic form has a one-dimensional kernel, invariant under every permutation of branches and leaves within branches. The smallest Euclidean dimension representing \(d^p\) as squared distances is \(N-2\) at the endpoint and \(N-1\) for \(0\le p<\alpha_{m,k}\).

The sharp parameter asymptotics are, for fixed \(m\) as \(k\to\infty\),
\[
\alpha_{m,k}=1+\frac{2}{k\Gamma_m}+O_m(k^{-2}),\qquad
\Gamma_m=(10m-8)\log 2-(6m-6)\log 3>0,
\]
and, for fixed \(k\) as \(m\to\infty\),
\[
\alpha_{m,k}=1+\frac{c_k}{m}+O_k(m^{-2}),
\]
where \(c_k\) is the smaller positive root of
\[
\frac4k-T_k c+\Delta c^2=0,\quad
T_k=20\log2-12\log3+\frac{4\log2}{k},\quad
\Delta=8(\log2)^2-(2\log2-3\log3)^2>0.
\]
In particular, \(\alpha_{2,2}\approx1.527173088280\), agreeing with the previously published *numerical* depth-two binary-tree exponent. The contribution is the exact infinite two-parameter theorem, its mode separation, strict branching monotonicities and both asymptotic constants, **not** this individual previously calculated approximation.

## Assumptions and scope

All edges have length one; all vertices, not merely the leaves, belong to the metric space. We use the standard negative-type definition: \(d^p\) has negative type if \(Q_p(w)=\sum_{u,v}w_u w_v d(u,v)^p\le0\) for every real weight vector satisfying \(\sum_u w_u=0\). At \(p=0\) the powered distance is zero on the diagonal and one off the diagonal. Schoenberg's exponential theorem identifies this property with positive semidefiniteness of \(K_{\lambda,p}\) for every \(\lambda>0\). The condition is **simultaneous for all scales**, not a fixed-scale or large-scale statement. The assertion is restricted to integer \(m,k\ge2\); the single-leaf-per-branch case is excluded from the claimed novelty.

## Proof

**1. The exact three-sector decomposition.** Give the root weight \(w_o\), hub \(i\) weight \(y_i\), and terminal leaf \((i,j)\) weight \(z_{ij}\), with total weight zero. Write \(Y=\sum_i y_i\), \(Z_i=\sum_j z_{ij}\), and \(Z=\sum_iZ_i\), so \(w_o=-Y-Z\). The possible nonzero distances are \(1,2,3,4\). Counting ordered pairs at these distances and using the zero-sum identity gives, without approximations,
\[
\begin{aligned}
Q_p={}&(a-2)Y^2+2(b-a-1)YZ+(c-2a)Z^2
-a\sum_i y_i^2+2(1-b)\sum_i y_iZ_i\\
&+(a-c)\sum_iZ_i^2-a\sum_{i,j}z_{ij}^2.
\end{aligned}
\]
Let \(\widetilde y_i=y_i-Y/m\), \(\widetilde Z_i=Z_i-Z/m\), and \(\delta_{ij}=z_{ij}-Z_i/k\). Since \(\sum_i\widetilde y_i=\sum_i\widetilde Z_i=\sum_j\delta_{ij}=0\), and
\(\sum_{i,j}z_{ij}^2=\sum_iZ_i^2/k+\sum_{i,j}\delta_{ij}^2\), direct completion of squares yields
\[
\boxed{Q_p=-\frac1m\begin{pmatrix}Y&Z\end{pmatrix}P_{m,k}(p)\binom{Y}{Z}
-\sum_{i=1}^m\begin{pmatrix}\widetilde y_i&\widetilde Z_i\end{pmatrix}
R_k(p)\binom{\widetilde y_i}{\widetilde Z_i}
-a\sum_{i,j}\delta_{ij}^2,}
\]
where
\[
R_k(p)=\begin{pmatrix}a&b-1\\b-1&c-a+a/k\end{pmatrix}.
\]
The global two-dimensional mode, the \(m-1\) branch-contrast modes, and the \(m(k-1)\) leaf-contrast modes are independent; together their dimensions sum to \(N-1\). This also confirms no hidden zero-sum directions were omitted.

**2. The global mode is always first.** Set
\[
H_p=\begin{pmatrix}2-a&a+1-b\\a+1-b&2a-c\end{pmatrix},
\qquad P_{m,k}(p)=R_k(p)+mH_p.
\]
For \(1<p<2\), the fractional-power integral representation
\[
t^p=C_p\int_0^\infty(e^{-st}-1+st)\,s^{-p-1}\,ds,\qquad C_p>0,
\]
shows by expanding the products that
\[
-H_p=C_p\int_0^\infty s^{-p-1}
\binom{1-e^{-s}}{1-e^{-2s}}
\begin{pmatrix}1-e^{-s}&1-e^{-2s}\end{pmatrix}ds.
\]
The two functions in the column are not proportional on \((0,\infty)\): their ratio is \(1+e^{-s}\). Hence \(-H_p\) is strictly positive definite. Consequently, whenever \(P_{m,k}(p)\succeq0\), the identity \(R_k(p)=P_{m,k}(p)-mH_p\) implies \(R_k(p)\succ0\). By Step 1, for \(1<p<2\), *the entire zero-sum metric form is nonpositive if and only if \(P_{m,k}(p)\succeq0\)*, and any endpoint nullity comes exclusively from the global mode.

**3. Existence and uniqueness of the threshold.** At \(p=1\),
\[
P_{m,k}(1)=\begin{pmatrix}2&2\\2&2+2/k\end{pmatrix},\qquad
\det P_{m,k}(1)=4/k>0,
\]
so the global matrix is strictly positive definite. Put \(\beta_m=\log_2(2m/(m-1))\). Since \(m\ge2\), one has \(1<\beta_m\le2\). At \(p=\beta_m\), its first diagonal entry is zero while its second diagonal entry is \(-2^{\beta_m}(1-1/k)<0\); hence the matrix is not positive semidefinite. Continuity gives at least one interior first singularity \(\alpha_{m,k}\in(1,\beta_m)\). On the whole open interval \((1,\beta_m)\) the first diagonal entry of \(P\) is positive. Therefore any zero of its determinant in the interval necessarily makes \(P\) positive semidefinite of rank one, not a negative semidefinite or indefinite matrix.

The general strict-inheritance theorem for negative type states that \(q\)-negative type for \(q>0\) implies strict \(p\)-negative type whenever \(0\le p<q\) (Li–Weston). If there were two distinct determinant roots in \((1,\beta_m)\), both would correspond by Step 2 to non-strict negative type. Taking the larger root as \(q\) would force strict negative type at the smaller root, a contradiction. Thus the zero is unique. Before it \(P\) remains positive definite; at it \(P\) has rank one; above it no negative type can recur by the same strict-inheritance theorem. The already positive-definite case at \(p=1\), the interval property for negative type, and direct strict \(0\)-negative type complete the iff assertion for every \(p\ge0\). Schoenberg's theorem converts the statement to the universal Gaussian-kernel condition.

**4. Strict monotonicity in both branching counts.** At \(p=\alpha_{m,k}\) the global \(P\) is singular positive semidefinite, and Step 2 makes \(H_p\) strictly negative definite. The exact identity
\[
P_{m+1,k}(p)=P_{m,k}(p)+H_p
\]
therefore makes the enlarged-branch matrix negative on the old null direction. Strict-inheritance of negative type gives \(\alpha_{m+1,k}<\alpha_{m,k}\). For the terminal branching count,
\[
P_{m,k+1}(p)=P_{m,k}(p)-\frac{2^p}{k(k+1)}\binom01\begin{pmatrix}0&1\end{pmatrix}.
\]
Every null vector of \(P_{m,k}(\alpha_{m,k})\) has nonzero second component, because its first diagonal entry is strictly positive. Thus the second update is also strictly negative on the old null vector. Again the threshold must decrease strictly. The argument uses two distinct rank perturbations and covers all integer parameter boundaries.

**5. Endpoint dependence and Euclidean dimension.** At \(p=\alpha_{m,k}\), write \(P_{ij}\) for entries of \(P_{m,k}(p)\). Since \(P_{11}>0\) and \(\det P=0\), \((Y,Z)=(P_{12},-P_{11})\) is a nonzero global null vector. Assign each hub weight \(Y/m\), each leaf weight \(Z/(mk)\), and root weight \(-Y-Z\). Conversely Step 1, strict positive definiteness of \(R\), and strict positivity of \(a\) show this spans the entire zero-sum nullspace. The squared-Euclidean embedding Gram matrix obtained by centering \(-d^p/2\) has rank \((N-1)-1=N-2\) at the threshold and rank \(N-1\) below; the Hilbert embedding characterization of negative type gives the claimed minimal dimensions.

**6. Sharp two-axis asymptotics.** Put \(L_2=\log2\), \(L_3=\log3\). For fixed \(m\), extend \(1/k\) to a small real parameter. At \((p,1/k)=(1,0)\), the global matrix becomes \(\bigl(\begin{smallmatrix}2&2\\2&2\end{smallmatrix}\bigr)\), with a simple zero eigenmode \(v=(1,-1)\). The perturbation in \(1/k\) contributes \(2/k\) to \(v^TPv\), whereas differentiation in \(p\) contributes
\[
\left.v^T\partial_pP_{m,k}(p)v\right|_{p=1,1/k=0}
=-\Gamma_m,\qquad
\Gamma_m=(10m-8)L_2-(6m-6)L_3>0.
\]
The inequality follows from \(\Gamma_2=6\log(4/3)>0\) and \(\Gamma_{m+1}-\Gamma_m=10L_2-6L_3=\log(1024/729)>0\). The analytic implicit-function theorem at the simple eigenvalue proves \(\alpha_{m,k}=1+2/(k\Gamma_m)+O_m(k^{-2})\).

For fixed \(k\), use \(P_{m,k}(p)=R_k(p)+mH_p\) and set \(p=1+s/m\). Then
\[
P_{m,k}(1+s/m)=\begin{pmatrix}2&2\\2&2+2/k\end{pmatrix}
+s\begin{pmatrix}-2L_2&2L_2-3L_3\\2L_2-3L_3&-4L_2\end{pmatrix}
+O_k(m^{-1}),
\]
locally uniformly for bounded \(s\). The second matrix is negative definite: its negative is the limit of the strictly positive fractional-power integral Gram matrix divided by \(p-1\), equivalently the integral with weight \(s^{-2}\) and nonproportional component functions. Its determinant is \(\Delta>0\). Taking the determinant of the leading matrix gives \(4/k-T_ks+\Delta s^2\). Both roots are positive, and they are distinct because the negative derivative matrix is not proportional to the positive-definite constant matrix (their first-row diagonal/off-diagonal ratios differ). The first singular crossing occurs at the smaller root \(c_k\), with a simple eigenvalue; the implicit-function theorem gives \(\alpha_{m,k}=1+c_k/m+O_k(m^{-2})\). The constants are asserted only with the other integer parameter fixed.

## Verification

The accompanying standalone standard-library script `artifacts/verify.py` separately constructs shortest paths between **all** vertices for \(2\le m,k\le6\), compares the direct powered-distance quadratic form with every term of the three-sector identity for several exponents and deterministic zero-sum weights, confirms \(P=R+mH\), checks signs of \(H\) and \(R\), locates threshold roots, verifies both strict finite parameter monotonicities, and tests the two asymptotic coefficients on large independent parameter values. Run `python3 artifacts/verify.py` from the directory containing the paper. Its recorded successful output is `VERIFY_OK assertions=1257 m=2..6 k=2..6 exact_decomposition_and_asymptotic_checks`. This finite numerical corroboration is not an infinite proof; Steps 1–6 provide the analytic proof for all allowed parameters. No external data or custom packages are needed.

## Relationship to prior work

Doust and Weston (2007) proved strictness gaps for finite metric trees and discussed explicit star metrics, but their parameter-free finite-tree bounds do not supply the present two-level full classification. Li and Weston (2009) prove strict negative-type inheritance, used here to rule out a second singularity. Caffarelli, Doust and Weston (2010), Sections 2 and 5, study spherically symmetric trees and report *numerical* generalized roundness \(1.5272\) for the complete binary depth-two tree; their results do not present the exact two-parameter determinant equation, its single global null sector, both strict parameter monotonicities, or the two asymptotic coefficients proved here. Sánchez (2011) gives a general finite-metric determinant/inverse test and a complete-bipartite example, not the particular analytic uniform-depth-two classification. A previously established depth-two tree with only one pendant leaf per hub is a limiting/special adjacent family, excluded by \(k\ge2\); the present theorem is not asserted to recover its historical priority.

## Limitations

The theorem requires identical downward branching at both levels, positive integer counts \(m,k\ge2\), and unweighted edges. It does not address general finite metric trees, deeper complete binary trees, nonuniform branch sizes, fixed-scale-only positive definiteness, or optimal embeddings above the negative-type threshold. The binary depth-two numerical datum is already in the literature. Other authors may have an equivalent analytical determinant or spectral decomposition in older metric-tree or association-scheme literature; no exhaustive priority claim is made. All numerical root values and checks are corroboration, not standalone certificates of infinite-dimensional statements. Independent external mathematical validation has not been performed.

## References

1. I. Doust and A. Weston, *Enhanced negative type for finite metric trees*, arXiv:0705.0411v1 (first public 2007-05-03), https://arxiv.org/abs/0705.0411 .
2. H. Li and A. Weston, *Strict p-negative type of a metric space*, arXiv:0901.0695v1 (first public 2009-01-06), Theorem 5.4, https://arxiv.org/html/0901.0695v3 .
3. E. Caffarelli, I. Doust and A. Weston, *Metric trees of generalized roundness one*, arXiv:1008.3418v1 (first public 2010-08-20), especially Sections 2 and 5, https://arxiv.org/abs/1008.3418 .
4. S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451v1 (first public 2011-08-02), especially Section 2, https://arxiv.org/abs/1108.0451 .
