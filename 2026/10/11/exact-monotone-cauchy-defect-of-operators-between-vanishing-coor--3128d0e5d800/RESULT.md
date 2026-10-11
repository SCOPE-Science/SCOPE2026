# Exact monotone-Cauchy defect of operators between vanishing-coordinate lattices

## Finding
Let \(\Gamma\) and \(\Lambda\) be arbitrary index sets and \(T:c_0(\Gamma;\mathbb R)\to c_0(\Lambda;\mathbb R)\) a bounded linear operator. Put \(a_{\lambda\gamma}=(Te_\gamma)(\lambda)\). For each \(\lambda\), its row \((a_{\lambda\gamma})_{\gamma\in\Gamma}\) belongs to \(\ell_1(\Gamma)\). Define
\[
q_\lambda=\max\left\{\sum_{\gamma\in\Gamma}(a_{\lambda\gamma})_+,\;\sum_{\gamma\in\Gamma}(-a_{\lambda\gamma})_+\right\}.
\]
Here \(t_+=\max\{t,0\}\) for real \(t\). Define the *monotone-Cauchy defect* by
\[
\mathcal D(T)=\sup_{\substack{0\le x_1\le x_2\le\cdots\\\|x_n\|_\infty\le1}}\lim_{N\to\infty}\sup_{m\ge n\ge N}\|Tx_m-Tx_n\|_\infty.
\]
The exact formula is
\[
\boxed{\mathcal D(T)=\inf_{F\subseteq\Lambda\,\mathrm{finite}}\ \sup_{\lambda\in\Lambda\setminus F}q_\lambda.}
\]
Here the supremum over an empty set is zero. Moreover, if \(\|T\|_{\mathrm e}\) denotes distance to the compact operators, then
\[
\|T\|_{\mathrm e}=\inf_{F\subseteq\Lambda\,\mathrm{finite}}\sup_{\lambda\notin F}\sum_\gamma|a_{\lambda\gamma}|,
\qquad
\frac12\|T\|_{\mathrm e}\le\mathcal D(T)\le\|T\|_{\mathrm e}.
\]
Both comparison constants are optimal, even for operators on real \(c_0(\mathbb N)\). The vanishing of the defect characterizes the compact operators and, consequently, the quasi-Levi and complete-quasi-Levi classes (for either bounded increasing sequences or bounded increasing nets) on this pair of sequence lattices.

## Assumptions and scope
For an arbitrary set \(I\), \(c_0(I;\mathbb R)\) consists of real functions that are smaller than every positive threshold outside a finite subset of \(I\), with the supremum norm and pointwise lattice order. A bounded increasing sequence means \(0\le x_n\le x_{n+1}\) and \(\sup_n\|x_n\|_\infty\le1\). An operator need not be positive. There are no countability assumptions on either index set.

A bounded increasing family is *order Cauchy* when for some decreasing-to-zero family of positive elements of the target, all sufficiently late pairwise differences are bounded in modulus by the corresponding regulators. It is *order convergent* when late deviations from one target element have such regulators. These are the (quasi-)Levi conventions of the cited primary literature. The main formula above concerns the norm-Cauchy defect; the order-theoretic classification is a consequence, not an assertion about operators on general Banach lattices.

## Proof
**Rows and compactness.** The coordinate evaluation functional \(\delta_\lambda\circ T\) is in \(c_0(\Gamma)^*=\ell_1(\Gamma)\), with row norm \(b_\lambda=\sum_\gamma|a_{\lambda\gamma}|\). Since \(Te_\gamma\in c_0(\Lambda)\), each fixed column \(a_{\lambda\gamma}\) tends to zero outside finite sets of \(\Lambda\). Let \(P_F\) be output-coordinate projection onto finite \(F\subseteq\Lambda\). Then \(P_FT\) has finite rank and
\[
\|T-P_FT\|=\sup_{\lambda\notin F}b_\lambda.
\]
If \(K\) is compact, uniform finite-coordinate approximation of the compact set \(K(B_{c_0(\Gamma)})\) shows \(\inf_F\sup_{\lambda\notin F}\|\delta_\lambda K\|=0\). The triangle inequality gives the reverse essential-norm estimate against every compact \(K\). Hence the displayed essential-norm identity and \(T\) compact if and only if \(b\in c_0(\Lambda)\).

**Upper estimate.** For any admissible increasing \((x_n)\), the coordinates \(x_n(\gamma)\) converge as real numbers bounded by one. Absolute convergence of each row gives convergence of the scalar sequence \((Tx_n)(\lambda)\) for every fixed \(\lambda\). For \(m\ge n\), the difference \(h=x_m-x_n\) satisfies \(0\le h(\gamma)\le1\) for every \(\gamma\). Thus
\[
-\sum_\gamma(-a_{\lambda\gamma})_+\le(Th)(\lambda)\le\sum_\gamma(a_{\lambda\gamma})_+,
\quad |(Th)(\lambda)|\le q_\lambda.
\]
For every finite \(F\subseteq\Lambda\), the finitely many scalar Cauchy sequences make the supremum over \(\lambda\in F\) vanish in the limit \(N\to\infty\). Outside \(F\), the last bound applies uniformly. Taking successively the limit, the infimum over \(F\), and the supremum over increasing input sequences proves \(\mathcal D(T)\le\inf_F\sup_{\lambda\notin F}q_\lambda\).

**Matching lower estimate.** Write \(\eta=\inf_F\sup_{\lambda\notin F}q_\lambda\). If \(\eta=0\), the upper estimate suffices. Otherwise fix \(0<\varepsilon<\eta/5\). Inductively construct distinct \(\lambda_j\in\Lambda\) and pairwise disjoint finite sets \(A_j\subset\Gamma\). Having chosen \(B_{j-1}=\bigcup_{i<j}A_i\), choose \(\lambda_j\) outside a finite set large enough to ensure simultaneously
\[
q_{\lambda_j}>\eta-\varepsilon,
\qquad\sum_{\gamma\in B_{j-1}}|a_{\lambda_j\gamma}|<\varepsilon.
\]
This is possible because the large-\(q\) indices escape every finite set, while each fixed column vanishes at infinity. Choose a sign \(s_j\in\{-1,1\}\) whose associated signed row mass is \(q_{\lambda_j}\), and take a finite \(A_j\subseteq\Gamma\setminus B_{j-1}\) made of entries with \(s_ja_{\lambda_j\gamma}>0\) such that
\[
s_j\sum_{\gamma\in A_j}a_{\lambda_j\gamma}>q_{\lambda_j}-2\varepsilon.
\]
The deleted previous coordinates cost less than \(\varepsilon\), and an absolutely summable positive row has finite partial sums arbitrarily close to its total. Set \(x_j=\mathbf{1}_{B_j}\in c_0(\Gamma)\). These are increasing positive unit-ball vectors. For each \(n<j\),
\[
\big|(T(x_j-x_n))(\lambda_j)\big|\ge q_{\lambda_j}-3\varepsilon>\eta-4\varepsilon,
\]
because the contribution from \(B_{j-1}\setminus B_n\) has absolute value less than \(\varepsilon\). For every \(N\), take \(j>n\ge N\) to obtain a tail diameter at least \(\eta-4\varepsilon\). Letting \(\varepsilon\downarrow0\) yields \(\mathcal D(T)\ge\eta\).

**Sharp comparison and order consequence.** Since \(b_\lambda=p_\lambda+m_\lambda\) while \(q_\lambda=\max\{p_\lambda,m_\lambda\}\), where the two quantities are the positive and negative row masses, \(b_\lambda/2\le q_\lambda\le b_\lambda\). Passing to finite-output tails proves the two sharp bounds. The identity on \(c_0(\mathbb N)\) has \(\mathcal D=\|T\|_{\mathrm e}=1\). The signed block-difference operator \((Ux)_n=(x_{2n-1}-x_{2n})/2\) has \(\|U\|_{\mathrm e}=1\) and \(\mathcal D(U)=1/2\). For positive \(T\), equality \(\mathcal D(T)=\|T\|_{\mathrm e}\) follows rowwise.

For a target \(c_0(\Lambda)\), an order-Cauchy sequence is norm-Cauchy: once one regulator \(u_0\in c_0(\Lambda)_+\) bounds late differences and regulators decrease pointwise to zero, finitely many coordinates control the supremum norm while \(u_0\) controls the remaining coordinates. Consequently quasi-\(\sigma\)-Levi implies \(\mathcal D(T)=0\), hence compactness. Conversely, if \(T\) is compact, then \(b\in c_0(\Lambda)\). For any bounded increasing net \((x_\alpha)\), each coordinate has a limit, and absolute row convergence gives a pointwise output limit \(y\), bounded in modulus by \(M b\) and hence belonging to \(c_0(\Lambda)\). Finite-output control together with the vanishing tail of \(b\) gives \(\|Tx_\alpha-y\|_\infty\to0\). Moreover \(|Tx_\alpha-y|\le2Mb\); for every \(\delta>0\), eventually \(|Tx_\alpha-y|\le\min\{\delta\mathbf{1},2Mb\}\), whose regulators lie in \(c_0(\Lambda)\) and decrease to zero as \(\delta\downarrow0\). Thus \(Tx_\alpha\) order converges for every such net. This proves the stated agreement of the four quasi-Levi variants with compactness.

## Verification
The proof uses only absolute summability, coordinatewise convergence, finite-set tail control, and a finite-support gliding-hump selection. The lower bound produces one explicit type of increasing witness sequence for every nonzero tail defect, not merely a sequence of unrelated extremizers. The identity and signed block-difference operators are infinite-dimensional witnesses for the optimal constants; they are not finite-dimensional approximations. No computer enumeration is needed or used for the continuum of operators and arbitrary index sets.

## Relationship to prior work
Emelyanov's 2023 preprint defines quasi-Levi and complete-quasi-Levi operators, proves structural inclusions, and gives compact positive operators on \(c_0\) that fail to be Levi operators. His 2024 paper investigates collectively \(\sigma\)-Levi families and their relation to collective compactness. The 2025 follow-up supplies further Levi-class results and the same distinguishing example. The 2021 paper of Alpay, Emelyanov and Gorokhova develops qualitative KB/Levi operator theory. The qualitative compactness-class collapse here is compatible with known quasi-KB and weak compactness principles; it is **not** claimed as the novel quantitative ingredient. The new assertion is the exact signed-row formula for the monotone-Cauchy defect and the attained sharp factor-of-two separation from essential norm. None of the inspected relevant results provides or implies that quantitative identity with its sign-sensitive extremizers.

## Limitations
Only real scalar \(c_0\)-to-\(c_0\) operators are covered. The defect measures norm oscillation of bounded increasing *sequences*, not an independent notion of order oscillation for arbitrary nets. No classification of quasi-Levi operators between general Banach lattices or solution to the unrestricted domination problem is claimed. The analytic argument is self-contained conditional on standard duality \(c_0(I)^*=\ell_1(I)\); equivalence to earlier unindexed formulas cannot be ruled out by literature search alone. No independent mathematical audit has been performed.

## References
1. E. Emelyanov, *On KB and Levi operators in Banach lattices*, arXiv:2312.05685, initial public posting 2023-12-09; especially Definition 2, Example 2, Theorems 1 and 4, and Section 3.
2. E. Emelyanov, *On collectively \(\sigma\)-Levi sets of operators*, arXiv:2408.03686, initially public 2024-08-07; especially Definition 1, Example 2 and Section 3.
3. E. Emelyanov, *On Levi operators between normed and vector lattices*, arXiv:2506.12578, 2025; especially Lemma 2.3 and Proposition 2.4.
4. S. Alpay, E. Emelyanov and S. Gorokhova, *The \(o\tau\)-continuous, Lebesgue, KB, and Levi operators between vector lattices and topological vector spaces*, arXiv:2105.01810, 2021; Sections 2 and 3.
