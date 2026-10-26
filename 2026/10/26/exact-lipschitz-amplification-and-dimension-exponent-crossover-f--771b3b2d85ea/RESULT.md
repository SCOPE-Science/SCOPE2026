# Exact Lipschitz amplification and dimension–exponent crossover for antipodal hypercube \(p\)-energy interpolation

## Finding
Let \(d\ge3\) be an integer, let \(1<p<\infty\), and endow the Boolean cube \(Q_d=\{0,1\}^d\) with its unweighted shortest-path (Hamming) metric. Fix the two antipodes \(o=(0,\ldots,0)\) and \(v=(1,\ldots,1)\). For each scalar boundary function \(f:\{o,v\}\to\mathbb R\), let \(E_{d,p}f\) uniquely minimize
\[
  \mathcal E_p(u)=\sum_{\{x,y\}\in E(Q_d)}|u(x)-u(y)|^p
\]
over all real functions satisfying \(u(o)=f(o)\) and \(u(v)=f(v)\). This variationally defined map is a real-linear extension operator, and its **exact** operator norm between Lipschitz seminormed spaces (or their quotients by constants) is
\[
\boxed{\|E_{d,p}\|_{\operatorname{Lip}\to\operatorname{Lip}}=\Lambda_{d,p}:=
\frac{d}{\displaystyle\sum_{j=0}^{d-1}\binom{d-1}{j}^{-1/(p-1)}}.}
\]
For normalized boundary data \(f(o)=0,f(v)=1\), and \(k=|x|_1\), the unique extension is
\[
(E_{d,p}f)(x)=\frac{\displaystyle\sum_{j=0}^{k-1}\binom{d-1}{j}^{-1/(p-1)}}{\displaystyle\sum_{j=0}^{d-1}\binom{d-1}{j}^{-1/(p-1)}}.
\]
For arbitrary boundary data, multiply this profile by \(f(v)-f(o)\) and add \(f(o)\).

For each \(d\ge3\), the amplification \(\Lambda_{d,p}>1\) decreases strictly with \(p\), with
\[\lim_{p\downarrow1}\Lambda_{d,p}=d/2,\qquad \lim_{p\to\infty}\Lambda_{d,p}=1.\]
For each fixed \(p>1\), \(\Lambda_{d,p}/d\to1/2\) as \(d\to\infty\). More sharply, for **any** sequence \(p_d>1\), the dimension/exponent crossover is
\[
\lim_{d\to\infty}\Lambda_{d,p_d}=
\begin{cases}
+\infty,&p_d/d\to0,\\
\displaystyle\Bigl(\int_0^1e^{-H(t)/\alpha}\,dt\Bigr)^{-1},&p_d/d\to\alpha\in(0,\infty),\\
1,&p_d/d\to\infty,
\end{cases}
\]
where \(H(t)=-t\log t-(1-t)\log(1-t)\) on \((0,1)\) and \(H(0)=H(1)=0\). In the first case the extended-real limit is meant. The middle limit is strictly greater than one. In particular, keeping \(p\) fixed creates a Lipschitz instability growing linearly with cube dimension, whereas a bounded nontrivial amplification survives precisely on the \(p\asymp d\) scale.

## Assumptions and scope
The graph has unit edges, all \(2^d\) cube vertices, exactly two prescribed antipodal scalar values, and *variational* \(p\)-Dirichlet energy. Edge lengths define the shortest-path metric; the Euclidean chord metric is **not** used. The operator norm is that of this specific energy-minimizing extension, **not** the minimum over all possible linear extensions. Indeed the distance-to-antipode linear interpolation has norm one, which underscores the amplification caused by the variational selection. The case \(d=2\) is degenerate (the norm is one for every \(p>1\)); it is excluded from the strict inequalities and main threshold statements. The family is real scalar-valued and finite-dimensional at each \(d\).

## Proof
**1. Uniqueness and symmetry.** Every edge difference is a linear form in the free values, and \(t\mapsto|t|^p\) is strictly convex for \(p>1\). If two extensions have the same edge differences, their difference is constant on the connected graph, hence zero at the fixed boundary vertices. Consequently the energy is strictly convex on the affine constraint space and coercive there, so there is a unique minimizer. Any permutation of the \(d\) coordinate positions is a graph automorphism fixing both prescribed vertices. It preserves energy and boundary constraints, so uniqueness forces the minimizer to take a single value \(a_k\) on each Hamming layer of weight \(k\).

**2. Exact weighted-chain reduction.** Between layers \(k\) and \(k+1\) there are exactly \(\binom dk(d-k)=d\binom{d-1}{k}\) edges. The energy becomes
\[
\mathcal E_p(a)=d\sum_{k=0}^{d-1}\binom{d-1}{k}|a_{k+1}-a_k|^p,
\quad a_0=f(o),\quad a_d=f(v).
\]
Writing \(\delta_k=a_{k+1}-a_k\), the constraint is \(\sum_{k=0}^{d-1}\delta_k=f(v)-f(o)\). Hölder's inequality gives
\[
\Big|\sum_k\delta_k\Big|^p\le
\Big(\sum_k\binom{d-1}{k}|\delta_k|^p\Big)
\Big(\sum_k\binom{d-1}{k}^{-1/(p-1)}\Big)^{p-1}.
\]
Equality holds, for arbitrary signed endpoint difference, precisely at
\[\delta_k=(f(v)-f(o))\binom{d-1}{k}^{-1/(p-1)}/S_{d,p},\qquad
S_{d,p}:=\sum_{j=0}^{d-1}\binom{d-1}{j}^{-1/(p-1)}.\]
Thus the displayed radial profile is the unique solution on the full graph. The profile is affine in the two boundary values despite nonlinear energy when \(p\ne2\), so \(E_{d,p}\) is linear.

**3. Sharp Lipschitz norm.** A function on a graph endowed with its shortest-path metric has Lipschitz seminorm exactly its largest absolute edge difference: one inequality uses edges and the reverse inequality sums over a shortest path. The original two-point Lipschitz seminorm is \(|f(v)-f(o)|/d\). Since \(\binom{d-1}{k}\ge1\), the largest \(|\delta_k|\) is \(|f(v)-f(o)|/S_{d,p}\), attained on every edge at the first and last layer. Taking the quotient of seminorms gives exactly \(d/S_{d,p}\), with equality for any nonconstant boundary data. No numerical extrapolation is used.

**4. Finite-parameter monotonicity and endpoints.** If \(d\ge3\), an interior binomial coefficient exceeds one while both endpoint coefficients equal one. Therefore \(2<S_{d,p}<d\), and \(S_{d,p}\) increases strictly with \(p\). As \(p\downarrow1\), every interior summand tends to zero and the two endpoint terms remain one. As \(p\to\infty\), every summand tends to one. This proves strict amplification, strict monotonicity, and the two stated fixed-dimensional limits.

**5. Fixed-exponent asymptotic.** Fix \(p>1\). Choose an integer \(J>p-1\). For \(J\le k\le d-1-J\), binomial unimodality gives \(\binom{d-1}{k}\ge\binom{d-1}{J}\asymp d^J\). Summing at most \(d\) such terms produces \(O(d^{1-J/(p-1)})=o(1)\). Among the at most \(2J\) remaining terms, the two outermost equal one and every other term tends to zero. Thus \(S_{d,p}\to2\) and \(\Lambda_{d,p}/d\to1/2\).

**6. Sharp moving-exponent regimes.** Put \(q_d=p_d-1\). If \(p_d/d\to\alpha\in(0,\infty)\), the standard uniform binomial entropy estimate
\[\log\binom{d-1}{k}=dH(k/d)+O(\log d),\qquad 0\le k\le d-1\]
shows that every summand equals \(e^{-H(k/d)/\alpha+o(1)}\), with uniform error. The Riemann sum hence gives \(S_{d,p_d}/d\to\int_0^1e^{-H(t)/\alpha}dt\). If \(p_d/d\to\infty\), then uniformly in \(k\), \(0\le\log\binom{d-1}{k}/q_d\le d\log2/q_d\to0\), so \(S_{d,p_d}/d\to1\). Finally if \(p_d/d\to0\), then for any fixed \(\varepsilon\in(0,1/2)\) all central terms with \(\varepsilon d\le k\le(1-\varepsilon)d\) obey \(\binom{d-1}{k}\ge e^{c_\varepsilon d}\) for some \(c_\varepsilon>0\) and all sufficiently large \(d\). Their contributions to \(S_{d,p_d}/d\) tend to zero because \(d/q_d\to\infty\). The two edge strips contribute at most \(2\varepsilon+o(1)\). Letting \(\varepsilon\downarrow0\) yields \(S_{d,p_d}/d\to0\) and the claimed divergence. The integral is strictly between zero and one for finite positive \(\alpha\), completing the crossover proof.

## Verification
The accompanying standalone standard-library program `verify_hypercube_p_lip.py` independently constructs the entire unweighted cube graph. It exactly solves grounded \(p=2\) Laplace equations over rational numbers for \(d=2,3,4,5\), comparing 52 interior vertex values and all 128 graph edges with the theorem. It separately checks every interior nonlinear Euler equation and every edge for dimensions \(3\le d\le8\) and exponents \(p\in\{1.5,3,5,11\}\): 1,968 interior equations and 7,152 edge values. Three large-dimension calculations at \(d=300\) compare the finite coefficient with the entropy-integral limit for exponent ratios \(1/2,1,2\). All checks pass. The exact proof above, not these finite experiments, establishes the infinite-family statements.

## Relationship to prior work
Bruè, Di Marino and Stra (2018, arXiv:1801.07533v1), especially their introduction and Section 4.1, construct general linear Lipschitz extensions using random projections and doubling estimates. Those are extensions chosen for small norm rather than solutions of the specific \(p\)-energy minimization, and do not determine the present amplification formula. Bridle and Zhu (2013) formulate and analyze graph \(p\)-voltages for two prescribed labels; the variational definition is prior art. Their application and general well-posedness theory do not evaluate this antipodal cube family or its binomial norm and entropy transition. El Alaoui et al. (2016) found a dimension-dependent threshold in a random-geometric-graph/continuum setting; that motivation and qualitative dimension/exponent competition are expressly **not new** here. Flores, Calder and Lerman (2019), especially Section 1.1 and graph variational equations, analyze \(p\)-Laplacian label propagation and continuum limits on nearest-neighbor graphs, not an exact finite-cube Lipschitz operator norm. Calder, Slepčev and Thorpe (2020 preprint) likewise consider sparse labels on random geometric graphs. Classical antipodal hypercube **electrical resistance** and the corresponding \(p=2\) voltage profile are acknowledged as known: see Sedlák (2026), Section 1.3, which states the previously established antipodal resistance formula and studies all pairwise resistance distances. The new assertion is the sharp all-\(p\), all-dimensional Lipschitz amplification together with its exact entropy crossover; a general variational principle and the old \(p=2\) resistance do not by themselves state these conclusions.

## Limitations
The conclusion is about the variationally selected extension, not a globally minimum-norm Lipschitz extension. It covers only a two-point antipodal datum, unit-edge hypercubes and real scalars; it does not concern arbitrary labeled subsets, Euclidean chord-distance cubes, vector-valued targets, other graphs, or game-theoretic graph \(p\)-Laplacians. Existing variational frameworks and dimension-sensitive transitions are prior work, and less-indexed specific hypercube computations could duplicate the explicit formulas. No independent mathematical audit has been performed.

## References
1. E. Bruè, S. Di Marino, F. Stra, *Linear Lipschitz and \(C^1\) extension operators through random projection*, arXiv:1801.07533v1 (first public 2018-01-23), https://arxiv.org/abs/1801.07533.
2. M. Flores, J. Calder, G. Lerman, *Analysis and algorithms for \(\ell_p\)-based semi-supervised learning on graphs*, arXiv:1901.05031v1 (first public 2019-01-15), https://arxiv.org/abs/1901.05031.
3. J. Calder, D. Slepčev, M. Thorpe, *Rates of Convergence for Laplacian Semi-Supervised Learning with Low Labeling Rates*, arXiv:2006.02765v1 (first public 2020-06-04), https://arxiv.org/abs/2006.02765.
4. N. Bridle, X. Zhu, *\(p\)-voltages: Laplacian Regularization for Semi-Supervised Learning on High-Dimensional Data*, MLG workshop (2013), https://snap.stanford.edu/mlg2013/submissions/mlg2013_submission_6.pdf.
5. A. El Alaoui, X. Cheng, A. Ramdas, M. J. Wainwright, M. I. Jordan, *Asymptotic behavior of \(\ell_p\)-based Laplacian regularization in semi-supervised learning*, arXiv:1603.00564 (2016), https://arxiv.org/abs/1603.00564.
6. J. Sedlák, *Hitting times and resistance distances in the hypercube*, J. Phys. A: Math. Theor. 59 (2026) 195202, DOI:10.1088/1751-8121/ae5859 (open-access full text).
