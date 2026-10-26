# A reflected joint law for root degree and newest-vertex depth in random recursive trees

## Finding

Let \(T_n\) be a uniform random recursive tree on labels \(1,\ldots,n\), rooted at \(1\). For \(n\ge2\), write \(R_n\) for the number of children of the root, \(D_n\) for the graph distance from the root to vertex \(n\), and \(L_n\) for the number of vertices with no children. Then the **complete bivariate distributions** satisfy

\[
 (R_n,L_n)\ \stackrel{\mathrm d}=\ (D_n,n-L_n),\qquad n\ge2.
\]

Equivalently, for every integer \(r,\ell\),

\[
 \Pr(R_n=r,L_n=\ell)=\Pr(D_n=r,L_n=n-\ell).
\]

In particular, conditioning on any attainable leaf count reflects the conditional newest-vertex-depth law into the conditional root-degree law. At the covariance level this yields

\[
 \operatorname{Cov}(D_n,L_n)=-\operatorname{Cov}(R_n,L_n)
 =-\frac{n-2}{2(n-1)}.
\]

The distributional reflection holds for uniform attachment. It is sharp with respect to a Hoppe root weight: in the model where the root has weight \(\vartheta>0\) and every other vertex has weight \(1\), the corresponding reflection at size \(3\) holds **if and only if** \(\vartheta=1\).

## Assumptions and scope

A recursive tree has edges directed from a smaller label (parent) to a larger label (child). Each label \(j\in\{2,\ldots,n\}\) independently chooses its parent uniformly from \(\{1,\ldots,j-1\}\). Hence every one of the \((n-1)!\) labeled recursive trees has the same probability. Root degree means outdegree; \(D_n\) is depth measured in edges. For \(n\ge2\), the root is not a leaf. The expression \(n-L_n\) counts nonleaf vertices, including the root. The size \(n=1\) is excluded because its root is itself a leaf and the claimed symmetry does not hold there.

All generating series below are formal in \(z\); the auxiliary weights \(u,v\) are indeterminates. No limit theorem, analytic continuation, or simulation assumption is needed for the finite-size identity.

## Proof

**1. Unmarked-root enumeration.** Let

\[
 T(z;v)=\sum_{n\ge1}\frac{z^n}{n!}\sum_{t\in\mathcal T_n}v^{L(t)},
\]

where \(\mathcal T_n\) is the set of increasing recursive trees on \(n\) labels. Removing the smallest-label root leaves an unordered set of child subtrees. The root contributes weight \(v\) precisely if that set is empty. Therefore

\[
 \frac{\partial T}{\partial z}=v-1+\exp(T),\qquad T(0;v)=0.
\]

Solving for \(\exp(-T)\) gives the formal identity

\[
 T(z;v)=\log\left(\frac{1-v}{1-v\exp((1-v)z)}\right),
\]

interpreted coefficientwise, including its specialization at \(v=1\). Replacing \((z,v)\) by \((vz,v^{-1})\) yields the **leaf reciprocal relation**

\[
 T(vz;v^{-1})=T(z;v)+(1-v)z. \tag{1}
\]

The identity is also equivalent to Eulerian reciprocity for leaf-count polynomials, with its one-vertex correction explicit.

**2. Marking root degree.** Write \(A_n(u,v)=\sum_{t\in\mathcal T_n}u^{R(t)}v^{L(t)}\). Each child subtree of the root is now also marked by a factor \(u\). The same set decomposition gives

\[
 \sum_{n\ge1} A_n(u,v)\frac{z^{n-1}}{(n-1)!}
 =v-1+\exp\bigl(uT(z;v)\bigr). \tag{2}
\]

**3. Marking the newest vertex's depth.** Put \(B_n(u,v)=\sum_{t\in\mathcal T_n}u^{D_n(t)}v^{L(t)}\) and

\[
 B(z;u,v)=\sum_{n\ge1}B_n(u,v)\frac{z^{n-1}}{(n-1)!}.
\]

For \(n\ge2\), vertex \(n\) belongs to exactly one root child subtree. If that subtree has \(k\) vertices, it contains the maximum label and \(k-1\) of the remaining \(n-2\) nonroot labels; the other root children form an arbitrary forest on \(n-1-k\) labels. The distance to vertex \(n\) gains one edge at the root. The labeled product rule thus gives

\[
 \frac{\partial B}{\partial z}
 =uB(z;u,v)\exp(T(z;v)),\qquad B(0;u,v)=v.
\]

Since \(T'=v-1+\exp(T)\), integration gives

\[
 B(z;u,v)=v\exp\left(u\bigl[T(z;v)+(1-v)z\bigr]\right)
 =v\exp\bigl(uT(vz;v^{-1})\bigr), \tag{3}
\]

where the second equality is (1).

**4. Coefficient reflection.** Equation (3), with \(z\mapsto vz\), \(v\mapsto v^{-1}\), gives

\[
 vB(vz;u,v^{-1})=\exp\bigl(uT(z;v)\bigr).
\]

The coefficient of \(z^{n-1}/(n-1)!\) on the left is
\(v^nB_n(u,v^{-1})\), and for \(n\ge2\) equation (2) identifies the right coefficient with \(A_n(u,v)\). Thus

\[
 A_n(u,v)=v^n B_n(u,v^{-1}),\qquad n\ge2,
\]

as polynomials. Coefficient comparison proves the displayed bivariate distributional identity. The \(n=1\) constant-term discrepancy is exactly the exceptional leaf root, not an omitted boundary case.

**5. Covariance and sharp boundary.** For \(n\ge2\), the root-degree/leaf covariance equals \((n-2)/[2(n-1)]\). For completeness, let \(C_n=\operatorname{Cov}(R_n,L_n)\), and let \(I_n\) indicate that vertex \(n\) attaches to the root. From independent uniform attachment, \(R_n=R_{n-1}+I_n\). For \(n\ge3\), \(L_n=L_{n-1}+1-J_n\), where \(J_n\) indicates attachment to any leaf; the root is not a leaf. Conditional on the previous tree, \(\operatorname{Cov}(I_n,J_n\mid T_{n-1})=-L_{n-1}/(n-1)^2\). The conditional mean of \(L_n\) is \((1-1/(n-1))L_{n-1}+1\), and \(I_n\) has constant conditional mean. Consequently

\[
 C_n=\frac{n-2}{n-1}C_{n-1}
 +\frac{\mathbb E[L_{n-1}]}{(n-1)^2},
 \qquad C_2=0.
\]

The standard leaf recursion gives \(\mathbb E[L_m]=m/2\) for \(m\ge2\), so induction gives \(C_n=(n-2)/[2(n-1)]\). Applying the bivariate reflection proves the claimed negative depth/leaf covariance.

For the Hoppe model at \(n=3\), there are only two possible trees: the star with probability \(\vartheta/(\vartheta+1)\), and the chain with probability \(1/(\vartheta+1)\). Their \((R_3,L_3)\) values are \((2,2)\), \((1,1)\), whereas \((D_3,3-L_3)\) has values \((1,1)\), \((2,2)\), respectively. The two laws therefore coincide precisely at \(\vartheta=1\).

## Verification

The accompanying standard-library Python program performs exhaustive comparison of the two joint integer count tables for every size \(2\le n\le10\). Separately, an independent coefficient recursion for increasing-tree forests tests their equality for \(2\le n\le22\), and exact rational arithmetic checks both covariance formulas over that range. Its recorded output is in `checks.txt`; run `python3 verify.py` in the directory containing the two files. These finite checks do not constitute the proof for arbitrary \(n\), which rests on (1)–(3) and coefficient extraction above.

## Relationship to prior work

Leckey and Neininger, *Asymptotic analysis of Hoppe trees* (first public preprint 2012), treats the terminal insertion depth and the leaf count as separate observables, including marginal depth and leaf results. Classical Eulerian/Stirling generating functions, including work of Carlitz and Scoville, cover related permutation-record/descent enumerators; the root-degree/leaf side of (2) is therefore not asserted to be a new polynomial family. Published calculations of root-degree/leaf covariance also supply the positive covariance in step 5. The asserted additional statement is the full reflected **joint law involving the newest node's depth**, which is not a consequence of the corresponding one-dimensional marginals or a single covariance identity. Historical equivalences under permutation encodings remain a priority caveat.

## Limitations

The identity is for uniform, unordered recursive trees with the given labeling convention. It is not a claim about arbitrary recursive attachment kernels, random plane-oriented trees, or unlabeled trees. The Hoppe example shows that it cannot simply be extended to all positive root weights. Earlier generalized Eulerian–Stirling results may contain an unrecognized equivalent permutation-statistic identity; priority has not been independently established.

## References

- K. Leckey and R. Neininger, *Asymptotic analysis of Hoppe trees*, arXiv:1202.2439, first posted 11 February 2012, especially Section 2 and proofs of Theorems 2.1 and 2.5.
- L. Carlitz and R. Scoville, *Generalized Eulerian numbers: combinatorial applications*, Journal für die reine und angewandte Mathematik 265 (1974), 110–137, DOI:10.1515/crll.1974.265.110.
- R. T. Smythe and H. M. Mahmoud, *A survey of recursive trees*, Theory of Probability and Mathematical Statistics 51 (1995), 1–27.
